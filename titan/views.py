# views.py

from django.shortcuts import render


from . import ml_predict_titan




def titanic_result(request):
    
    pclass = request.POST.get('pclass',0)
    sex = request.POST.get('sex',0)
    age = request.POST.get('age',0)
    sibsp = request.POST.get('sibsp',0)
    parch =  request.POST.get('parch',0)
    fare = request.POST.get('fare',0)
    embarked = request.POST.get('embarked',0)
    """
    pclass = request.GET['pclass']
    sex = request.GET['sex']
    age = request.GET['age']
    sibsp = request.GET['sibsp']
    parch = request.GET['parch']
    fare = request.GET['fare']
    embarked = request.GET['embarked']
    """

    prediction = ml_predict_titan.prediction_model(pclass,sex,age,sibsp,parch,fare,embarked)
    return render(request, 'titanic_results.html',{'prediction' : prediction})
