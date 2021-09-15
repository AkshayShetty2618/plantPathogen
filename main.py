from csvReader import cvsReader
from Preprocessing import Preprocessing

def editCSV():
    path = r'G:\Kaggle\PlantPathology\train.csv'
    opPath = r'G:\Kaggle\PlantPathology\upTrain.csv'
    cvsReader.edit_csv(path, opPath)

def preprocessImage():

    Preprocessing(isTrain=True)


if __name__ == '__main__':
    editCSV()

