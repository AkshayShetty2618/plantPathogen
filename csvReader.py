import pandas as pd
import numpy as np

class csvReader:
    def __init__(self, path, opPath):
        self.path = path
        self.opPath = opPath
        self.edit_csv()


    def edit_csv(self):

        #path = r'G:\Kaggle\PlantPathology\train.csv'
        data = pd.read_csv(self.path)
        labels = data.labels.unique()
        n = 0
        for lab in labels:
            data.replace(lab, n, True)
            n = n + 1

        grp = data.groupby('labels')
        df = pd.DataFrame()

        hel = (grp.get_group(0)).sample(n=200)
        sc = (grp.get_group(1)).sample(n=200)
        frg = (grp.get_group(2)).sample(n=200)
        rust = (grp.get_group(3)).sample(n=200)
        comp = (grp.get_group(4)).sample(n=200)
        pwd = (grp.get_group(5)).sample(n=200)
        scfrg = (grp.get_group(6)).sample(n=200)
        scfrgc = grp.get_group(7)
        frgc = grp.get_group(8)
        rusfrg = grp.get_group(9)
        rusc = grp.get_group(10)
        pwdc = grp.get_group(11)

        df = df.append(hel)
        df = df.append(sc)
        df = df.append(frg)
        df = df.append(rust)
        df = df.append(comp)
        df = df.append(pwd)
        df = df.append(scfrg)
        df = df.append(scfrgc)
        df = df.append(frgc)
        df = df.append(rusfrg)
        df = df.append(rusc)
        df = df.append(pwdc)

        df = df.reset_index(drop=True)

        s = (df.shape[0], 12)
        dataList = np.zeros(s)
        images = []
        for ind, row in df.iterrows():
            images.append(row['image'])
            dataList[ind][row['labels']] = 1

        dataframe = pd.DataFrame(dataList,
                                 columns=['healthy', 'scab frog_eye_leaf_spot complex', 'scab', 'complex', 'rust',
                                          'frog_eye_leaf_spot', 'powdery_mildew', 'scab frog_eye_leaf_spot',
                                          'frog_eye_leaf_spot complex', 'rust frog_eye_leaf_spot',
                                          'powdery_mildew complex', 'rust complex'])
        dataframe.insert(0, 'image', images, True)

        #path = r'G:\Kaggle\PlantPathology\upTrain.csv'
        dataframe.to_csv(self.opPath, index=False)

