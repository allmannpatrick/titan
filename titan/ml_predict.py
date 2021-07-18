import pickle

def prediction_model(pclass,sex,age,sibsp,parch,fare,embarked,title):
    x = [[pclass,sex,age,sibsp,parch,fare,embarked,title]]
    randomforest = pickle.load(open('titanic_model.sav','rb'))
    prediction = randomforest.predict(x)
    if prediction == 1:
        prediction = 'survived'
    elif prediction == 0:
        prediction = 'not survived'
    return prediction


