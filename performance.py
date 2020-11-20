import numpy as np
import matplotlib.pyplot as plt

############# functions ##########################################################

def dprime(gen_scores, imp_scores):
    x = np.sqrt(2) * abs(np.mean(gen_scores) - np.mean(imp_scores))
    y = np.sqrt(np.power(np.std(gen_scores),2) + np.power(np.std(imp_scores),2))
    return x / y

def plot_scoreDist(gen_scores, imp_scores, plot_title):
    plt.figure()
    plt.hist(gen_scores, color='green', lw=2, histtype='step', hatch='//', label='Genuine Scores')
    plt.hist(imp_scores, color='red', lw=2, histtype='step', hatch='\\', label='Impostor Scores')
    plt.xlim([-0.05,1.05])
    plt.legend(loc='best')
    dp = dprime(gen_scores, imp_scores)
    plt.title(plot_title + '\nD-prime= %.2f' % dp)
    plt.show()
    return

def get_EER(far, frr):
    distances = []
    for i in range(len(far)):
        distances.append(abs(far[i] - frr[i]) / 2.0)
    k = np.argmin(distances)
    eer = (far[k] + frr[k]) / 2.0
    return eer

def plot_det(far, frr, plot_title):
    eer = get_EER(far, frr)               
    plt.figure()
    plt.plot(far, frr, lw=2)
    plt.plot([0,1], [0,1], lw=1, color='black')
    plt.xlim([-0.05,1.05])
    plt.ylim([-0.05,1.05])
    plt.xlabel('FAR')
    plt.ylabel('FRR')
    plt.title(plot_title + '\nEER = %.3f' % eer)
    plt.show()
    return

def plot_roc(far, tpr, plot_title):
    plt.figure()
    plt.plot(far, tpr, lw=2)
    plt.xlim([-0.05,1.05])
    plt.ylim([-0.05,1.05])
    plt.xlabel('FAR')
    plt.ylabel('TAR')
    plt.title(plot_title)
    plt.show()
    return

def compute_rates(gen_scores, imp_scores, num_thresholds):
    thresholds = np.linspace(0, 1, num_thresholds)
    far = []
    frr = []
    tpr = []
    
    for t in thresholds:
        tp = 0
        fp = 0
        tn = 0
        fn = 0
        
        for g_s in gen_scores:
            if g_s >= t:
                tp += 1
            else:
                fn += 1
                
        for i_s in imp_scores:
            if i_s >= t:
                fp += 1
            else:
                tn += 1
                    
        far.append(fp / (fp + tn))
        frr.append(fn / (fn + tp))
        tpr.append(tp / (tp + fn))
        
    return far, frr, tpr

############ main code #############################################################

def perf(gen_scores, imp_scores):
    far, frr, tpr = compute_rates(gen_scores, imp_scores, 150)    
    plot_title = 'GenMean=%0.2f, GenStd=%0.2f\nImpMean=%0.2f, ImpStd=%0.2f' % (np.mean(gen_scores), 
                                                                               np.std(gen_scores), 
                                                                               np.mean(imp_scores), 
                                                                               np.std(imp_scores))
    plot_scoreDist(gen_scores, imp_scores, plot_title)
    plot_roc(far, tpr, plot_title)
    plot_det(far, frr, plot_title)