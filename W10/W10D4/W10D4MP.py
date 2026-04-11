# Mini-Project: Predicting Heart Disease Using Logistic Regression
# Column: Suggested Encoding
# sex:binary
# cp:one-hot
# fbs:binary
# restecg:one-hot
# exang:binary
# slope:ordinal
# thal:one-hot
features = ['id', 'age', 'sex', 'dataset', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalch', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'num', 'sex_enc', 'fbs_enc', 'exang_enc', 'cp_asymptomatic', 'cp_atypical angina', 'cp_non-anginal', 'cp_typical angina', 'restecg_lv hypertrophy', 'restecg_normal', 'restecg_st-t abnormality', 'thal_fixed defect', 'thal_normal', 'thal_reversable defect', 'slope_enc']
X_train = X_train[features]
X_test = X_test[features]
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)