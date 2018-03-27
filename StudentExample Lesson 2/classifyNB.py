def classify(features_train, labels_train):   
    ### import the sklearn module for GaussianNB
    ### create classifier
    ### fit the classifier on the training features and labels
    ### return the fit classifier
    
    
    from sklearn import svm
    clf=svm.SVC(C=1000,kernel='rbf')
    clf.fit(features_train, labels_train)
    return clf