import cv2
import pickle
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

def load_model():

    with open('data/names.pkl','rb') as f:
        labels=pickle.load(f)

    with open('data/faces_data.pkl','rb') as f:
        faces=pickle.load(f)

    knn=KNeighborsClassifier(n_neighbors=5)

    knn.fit(faces,labels)

    return knn