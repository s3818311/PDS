import requests
from bs4 import BeautifulSoup
from collections import defaultdict


def get_street_types():
    """
    Get a dictionary of street types and their abbreviations

    Returns:
        dict: dictionary with street types as key and their abbreviations as value
    """

    # create Session object
    s = requests.Session()
    s.headers[
        "User-Agent"
    ] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36"

    loc = "https://pe.usps.com/text/pub28/28apc_002.htm"

    r = s.get(loc, allow_redirects=False)

    # parse HTML response
    soup = BeautifulSoup(r.content, "html.parser")

    # get table and rows
    table = soup.find("table", id="ep533076")
    rows = table.find_all("tr")

    # skip first row
    rows = rows[1:]

    # prepare defaultdict of abbreviations
    abbr = defaultdict(list)
    st_type = ""

    # building the defaultdict
    for row in rows:
        children = row.contents
        if len(children) == 6:
            st_type = children[-2].text.strip()
            for child in children[:-1]:
                txt = child.text.strip()
                if txt:
                    abbr[st_type].append(txt)
        else:
            for child in children:
                txt = child.text.strip()
                if txt:
                    abbr[st_type].append(txt)

    # build a new dict, reversing the key and values
    final = defaultdict(str)

    # each value now points to their key instead
    for k, v in abbr.items():
        for vv in v:
            final[vv.lower()] = k.lower()

    return final
