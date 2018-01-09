from __future__ import print_function
from sklearn import metrics
from time import time
import sklearn
import sklearn.datasets
import sklearn
import nltk
from sklearn import metrics
import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn import cluster
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import NMF, LatentDirichletAllocation
from sklearn.pipeline import Pipeline
from sklearn.linear_model import SGDClassifier

categories = ['Chicago']
dataset = sklearn.datasets.load_files(container_path="C:/Users/Anupama/Documents/3SummerSemester/KPT/testProject",load_content=True,shuffle=True, random_state=1)
print(len(dataset.data))
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(dataset.data)
print(X_train_counts.shape)
count_vect.vocabulary_.get(u'algorithm')
tf_transformer = TfidfTransformer(use_idf=False).fit(X_train_counts)
tf_transformer = TfidfTransformer(use_idf=False).fit(X_train_counts)
X_train_tf = tf_transformer.transform(X_train_counts)
print(X_train_tf)
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
clf = MultinomialNB().fit(X_train_tfidf, dataset.target)

with open("ch6.txt",'r') as f:
    docs_new = f.read().split('\n')



#docs_new = ['worst hotel ever','very horrible hotel','do not recommend this to anyone','best hotel ever','very good experienceW']
X_new_counts = count_vect.transform(docs_new)
X_new_tfidf = tfidf_transformer.transform(X_new_counts)
predicted = clf.predict(X_new_tfidf)
for doc, category in zip(docs_new, predicted):
    with open("resclassif.txt",'w') as dest:
        print('%r => %s' % (dataset.target_names[category],doc))
        dest.flush()

""""

text_clf = Pipeline([('vect', CountVectorizer()),
                      ('tfidf', TfidfTransformer()),
                      ('clf', MultinomialNB()),
 ])
text_clf = text_clf.fit(dataset.data, dataset.target)

reviews_test = sklearn.datasets.load_files(container_path="C:/Users/Anupama/Documents/3SummerSemester/KPT/testDataSet",load_content=True,shuffle=True, random_state=1)
docs_test = reviews_test.data
predicted = text_clf.predict(docs_test)
print(np.mean(predicted == reviews_test.target)*100)


text_clf = Pipeline([('vect', CountVectorizer()),
                  ('tfidf', TfidfTransformer()),
                      ('clf', SGDClassifier(loss='hinge', penalty='l2',
                                            alpha=1e-3, n_iter=9, random_state=42)),
 ])

_ = text_clf.fit(dataset.data, dataset.target)
predicted = text_clf.predict(docs_test)
print(np.mean(predicted == reviews_test.target))

print(metrics.classification_report(dataset.target, predicted,
     target_names=dataset.target_names))
"""""