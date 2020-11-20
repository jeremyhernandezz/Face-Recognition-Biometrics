# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 19:50:07 2019

@author: Tyree
"""
import numpy as np

''' Fusing the genuine and imposter scores for both knn and naive bayes '''
def fusion(gen_scores_knn, imp_scores_knn, gen_scores_nb, imp_scores_nb):
  
    fusion_correct = (np.array(gen_scores_knn) + np.array(gen_scores_nb)) / 2.0
    fusion_incorrect = (np.array(imp_scores_knn) + np.array(imp_scores_nb)) / 2.0
    
    return fusion_correct, fusion_incorrect
    
    

