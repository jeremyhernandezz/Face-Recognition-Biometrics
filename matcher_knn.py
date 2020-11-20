from sklearn.neighbors import KNeighborsClassifier
import numpy as np

''' Version from Project1Demo '''
''' Error found array with dim 3. Estimator expected <= 2 '''
def knn(X, y):
    knn = KNeighborsClassifier(n_neighbors=50, metric='manhattan') 
    gen_scores = []
    imp_scores = []
    
    for i in range(0, len(y)):
        query = X[i, :]
        query_label = y[i]
        
        templates = np.delete(X, i, 0)
        template_labels = np.delete(y, i)
            
        # Set the appropriate labels
        # 1 is genuine, 0 is impostor
        y_hat = np.zeros(len(template_labels))
        y_hat[template_labels == query_label] = 1 
        y_hat[template_labels != query_label] = 0
        
        knn.fit(templates, y_hat) # Train the classifier
        scores = knn.predict_proba(query.reshape(1,-1)).reshape(1,2) # Predict the label of the query
        classes = knn.classes_.reshape(1,2)
        
        gen_scores.extend(scores[classes==1])
        imp_scores.extend(scores[classes==0])

    return gen_scores, imp_scores
