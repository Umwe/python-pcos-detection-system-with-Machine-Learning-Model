import joblib

def PCOS_predict(age,weight,height,BMI,bldgroup,weightgain,hairgrowth,skindark,hairloss,pimples,fastfood):
    model=joblib.load("/home/shema/Documents/python/PCOS/app/PCOS_Predictor_SVM.joblib")
    return model.predict([[age,weight,height,BMI,bldgroup,weightgain,hairgrowth,skindark,hairloss,pimples,fastfood]])

