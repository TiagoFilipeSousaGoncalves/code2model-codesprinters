# Imports
import _pickle as cPickle
import pandas as pd
from xgboost import XGBClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import f1_score



# Prepare directories
df = pd.read_csv('data/manual_code.csv', encoding='utf-8', sep=';')

# Get first three rows
print(df.head(3))


# Train a model to detect the language
df = df[df['platafor'].notnull()]


# Create features from text
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['corpo'].fillna(''))

# Target value
Y = df['platafor']

# Divide data in train/test 
# Train
X_train = X[:int(X.shape[0]*0.8)]
X_test = X[int(X.shape[0]*0.8):]

# Test
Y_train = Y[:int(Y.shape[0]*0.8)]
Y_test = Y[int(Y.shape[0]*0.8):]


# XGBoost Classifier
clf = XGBClassifier(max_depth=2)
clf.fit(X_train,Y_train, verbose=1)


# Print Metrics
# Acc
print('Accuracy:',clf.score(X_test, Y_test))

# F1-Score
y_pred = clf.predict(X_test)
print('F1:', f1_score(y_pred, Y_test, average='macro'))


# Save model
with open("results/xgboost.pickle", "wb") as f:
    cPickle.dump(clf, f, -1)
