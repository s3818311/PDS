# Instructions to run the notebook

1. Installing modules and libraries

   - It is best to create a virtual environment before continuing.
   - First, follow the guide [here](https://stackoverflow.com/a/60936148) to certain wheel dependencies. It is important that these modules are installed first and foremost. For Linux users, this step is unnecessary.
   - Note that you don't have to download the wheels, they are included in the `wheels` directory.
     - e.g. `pip install ./wheels/Fiona-1.8.20-cp38-cp38-win_amd64.whl`
   - After installing the wheels, install the rest of the necessary modules with `pip install -r requirements.txt`

2. Run the notebook

   - After that, you can go head to the notebook and run all
   - The notebook is written the way so that you can read it from top to bottom like a report
   - Giving notes and insights of decisions for most of the cells

3. Final models report

   - The final models are pickled into a `.model` file and can be reload back if needed
   - Pickled models can be loaded back with

   ```
    model = None
    with open('model_name.model', 'rb') as f:
        model = pickle.load(f)
   ```

   - The model evaluation metrics, time taken to train model, and their hyperparameters are saved into `models.csv`. Which can be loaded back with pandas for an easier view.

## Computer specs

- Created and tested with Python 3.8.2. Ran with VSCode Jupyter extensions.
- OS: Windows 10 64-bit
- CPU: Intel Xeon E3-1271 v3, 4 cores / 8 threads
- RAM: 16GB of DDR3
