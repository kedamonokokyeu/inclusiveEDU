@ -0,0 +1,31 @@
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

data_dict = pickle.load(open('./data.pickle', 'rb'))
dataD = data_dict['data']
labelsL = data_dict['labels']

max_length = max(len(seq) for seq in dataD)
padded_dataD = [np.pad(seq, (0, max_length - len(seq)), mode='constant') for seq in dataD]

data = np.asarray(padded_dataD)
labels = np.asarray(labelsL)

x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, shuffle=True, stratify=labels)

model = RandomForestClassifier(max_features=84)

model.fit(x_train, y_train)

y_predict = model.predict(x_test)

score = accuracy_score(y_predict, y_test)

print('{}% of samples were classified correctly!'.format(score * 100))

f = open('model.p', 'wb')
pickle.dump({'model': model}, f)
f.close()
