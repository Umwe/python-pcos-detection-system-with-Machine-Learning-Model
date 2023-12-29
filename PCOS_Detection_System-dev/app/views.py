import os
import joblib
from django.shortcuts import render
##from .forms import PCOSForm

def home(request):
    return render(request,"index.html")

def results(request):
    model = joblib.load(os.path.join(os.path.dirname(__file__),'PCOS_Predictor_SVM.joblib'))
    
    lis =[]

    lis.append(request.GET['age'])
    lis.append(request.GET['weight'])
    lis.append(request.GET['height'])
    lis.append(request.GET['bmi'])
    lis.append(int(request.GET['bloodgroup']))
    lis.append(request.GET['hairgrowth'])
    lis.append(request.GET['hairloss'])
    lis.append(request.GET['weightgain'])
    lis.append(request.GET['skindarken'])
    lis.append(request.GET['pimples'])
    lis.append(request.GET['fastfood'])

    print(lis)
    ans = model.predict([lis])
    result_msg = ''
    if ans == 0:
        result_msg = 'You not likely to have PCOS.'
    else:
       result_msg = 'You are likely to have PCOS.'
        
        # Render the results template with the result message
    return render(request, 'results.html', {'name':request.GET['name'],'result': result_msg})

