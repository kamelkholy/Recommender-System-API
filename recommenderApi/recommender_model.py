
import xgboost as xgb
import os
import numpy as np
module_dir = os.path.dirname(__file__)  # get current directory
file_path = os.path.join(module_dir, 'baz.txt')


def load_model():
    module_dir = os.path.dirname(__file__)  # get current directory
    print(module_dir)
    file_path = os.path.join(module_dir, 'models\\trained\\model.json')
    print(file_path)

    model = xgb.Booster()
    model.load_model(file_path)
    return model


def predict(model, data):
    npData = np.array(data)
    xgData = xgb.DMatrix(npData)
    return model.predict(xgData)
