from csvReader import csvReader
from Preprocessing import Preprocessing

def editCSV():
    path = r'G:\Kaggle\PlantPathology\train.csv'
    opPath = r'G:\Kaggle\PlantPathology\upTrain.csv'
    csvReader(path,opPath)


def preprocessImage():
    csvPath = r'G:\Kaggle\PlantPathology\upTrain.csv'
    Preprocessing(csvPath, isTrain=True)


if __name__ == '__main__':
    #editCSV()
    preprocessImage()

