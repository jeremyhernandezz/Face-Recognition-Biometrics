from sklearn.naive_bayes import GaussianNB
import numpy as np

def nb(X, y):
    nb = GaussianNB() 
    gen_scores = []
    imp_scores = []


    for i in range(0, len(y)):
        query_img = X[i, :]
        query_label = y[i]
        
        template_imgs = np.delete(X, i, 0)
        template_labels = np.delete(y, i)
            
        # Set the appropriate labels
        # 1 is genuine, 0 is impostor
        y_hat = np.zeros(len(template_labels))
        y_hat[template_labels == query_label] = 1 
        y_hat[template_labels != query_label] = 0
        
        nb.fit(template_imgs, y_hat) # Train the classifier
        scores = nb.predict_proba(query_img.reshape(1,-1)).reshape(1,2) # Predict the label of the query
        classes = nb.classes_.reshape(1,2)
        
        gen_scores.extend(scores[classes==1])
        imp_scores.extend(scores[classes==0])

    return gen_scores, imp_scores