import numpy as np

def get_pca(X):

    # Squash it
    faces = np.zeros(shape=(X.shape[1] * X.shape[2], X.shape[0]))
    for i in range(X.shape[0]):
        faces[:, i] = X[i].reshape(X.shape[1] * X.shape[2])

    # Get the mean face
    mean_face = faces.mean(axis=1)

    # Subtract the mean face - center everybody
    for col in range(faces.shape[1]):
        faces[:, col] = faces[:, col] - mean_face

        # Compute the covariance matrix, C
    C = np.cov(faces.transpose())

    # Get the eigenfaces from C
    evals, evecs = np.linalg.eig(C)

    # Get eigenfaces
    eigenfaces = np.dot(faces, evecs)

    # get top k pca components
    k = 5
    face_features = np.zeros((faces.shape[1], k))
    for i in range(faces.shape[1]):
        face = faces[:, i]
        for j in range(k):
            face_features[i, j] = np.dot(eigenfaces[:, j].transpose(), face)
    
    return face_features