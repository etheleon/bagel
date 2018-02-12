import subprocess
import re
import numpy as np

class Utils:
    def loadData():
        """
        loads data and returns stratified test train
        Has to be run in the root directory
        """
        #training
        print("Hello")

    def submit(predictions, message="nothing", filename, columns):
        """
        Submits to KAGGLE

        Requires the KAGGLE CLI to be installed https://github.com/Kaggle/kaggle-api

        Parameters
        ----------
        predictions : list(str)
           array of predictions
        message : str
           Description of the entry
        filename : str, optional
           the file name if `None` will be the concatenated version of message
        predictions : list(str), optional
            the  column names, if `None`, the columns names are `Id` and `Probability`
        """
        df = pd.DataFrame({
            "Id"          : np.arange(len(predictions))+1,
            "Probability" : predictions
        })
        if(columns != None):
            df.columns = columns
        if(filename == None):
            filename = re.sub(" ", "-",  string) + ".csv"
        df.to_csv(filename, index=False)
        subprocess.run(["kaggle","competitions","submit","-c","givemesomecredit","-f",filename,"-m", message], stdout=subprocess.PIPE)
