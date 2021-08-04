import pickle
import numpy as np

def prediction_model(pclass,sex,age,sibsp,parch,fare,embarked):
    """
    np.nan_to_num(pclass)
    np.nan_to_num(sex)
    np.nan_to_num(age)
    np.nan_to_num(sibsp)
    np.nan_to_num(parch)
    np.nan_to_num(fare)
    np.nan_to_num(embarked)
    """
    x = [[pclass,sex,age,sibsp,parch,fare,embarked]]
    randomforest = pickle.load(open('titanic_model.sav','rb'))
    prediction = randomforest.predict(x)
    if prediction == 1:
        prediction = 'survived'
    elif prediction == 0:
        prediction = 'not survived'
    return prediction


