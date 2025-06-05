import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder

data_predict=pd.read_csv('Data_pred.csv')

X_sample=data_predict.copy()
model=joblib.load('/content/PrediksiModel.pkl')
labelencoder=LabelEncoder()
for col in X_sample.select_dtypes(include=['object']).columns:
  X_sample[col]=labelencoder.fit_transform(X_sample[col])


X_sample['Attrition']=model.predict(X_sample)
X_sample.head()

X_sample.to_csv('/content/Hasil_prediksi.csv',index=False)
