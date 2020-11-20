import get_data
import enhance_images
import features_lbp
import features_pca
import performance
import matcher_nb
import matcher_knn
import score_fusion

'''
The results only need to be the stuff from performance, do not show PCA. But can show LBP in report
'''

def main_menu():
    
    menu = {}
    print("Main Menu")
    print("____________________________________________________________________")
    menu['1']="Run LBP With Matcher_Knn and See Performance Results" 
    menu['2']="Run LBP With Matcher_Nb and See Performance Results"
    menu['3']="Run PCA With Matcher_Knn and See Performance Results"
    menu['4']="Run PCA With Matcher_Nb and See Performance Results"
    menu['5']="Enhance Images and Run LBP With Matcher_Knn and See Performance Results"
    menu['6']="Enhance Images and Run LBP With Matcher_Nb and See Performance Results"
    menu['7']="Enhance Images and Run PCA With Matcher_Knn and See Performance Results"
    menu['8']="Enhance Images and Run PCA With Matcher_Nb and See Performance Results"
    menu['9']="Run LBP With Score Fusion and See Performance Results"
    menu['10']="Run PCA With Score Fusion and See Performance Results"

    options=menu.keys()
    for entry in options: 
        print(entry, menu[entry])

def main_menu2():
    
    menu = {}
    print('\n')
    print("Image Enhance")
    print("____________________________________________________________________")
    menu['1']="Brighten Image" 
    menu['2']="Contrast Image"
    menu['3']="Sharpen Image"
    menu['4']="Combine all of the above"

    options=menu.keys()
    for entry in options: 
        print(entry, menu[entry])

        
main_menu()
image_directory = 'Project Data'
landmarks_directory = 'Project Data/Landmarks'
brightness_directory = 'Group1_FaceData_EnhancedBrightness'
contrast_directory = 'Group1_FaceData_EnhancedContrast'
sharpness_directory = 'Group1_FaceData_EnhancedSharpness'
modify_directory = 'Group1_FaceData_CombinedEnhanced'

print("____________________________________________________________________")
choice = input("Please Select An Option From (1 - 10): ") 
if choice =='1': 
    X, y = get_data.get_images(image_directory)
    X = features_lbp.init_lbp(X)
    gen_scores, imp_scores = matcher_knn.knn(X, y)
    performance.perf(gen_scores, imp_scores)
elif choice == '2': 
    X, y = get_data.get_images(image_directory)
    X = features_lbp.init_lbp(X)
    gen_scores, imp_scores = matcher_nb.nb(X, y)
    performance.perf(gen_scores, imp_scores)
elif choice == '3':
    X, y = get_data.get_images(image_directory) 
    X = features_pca.get_pca(X)
    gen_scores, imp_scores = matcher_knn.knn(X, y)
    performance.perf(gen_scores, imp_scores)
elif choice == '4':
    X, y = get_data.get_images(image_directory) 
    X = features_pca.get_pca(X)
    gen_scores, imp_scores = matcher_nb.nb(X, y)
    performance.perf(gen_scores, imp_scores)
elif choice == '5':
    main_menu2()
    print("____________________________________________________________________")
    choice = input("Please Select An Option From (1 - 4): ") 
#    X, y = enhance_images.get_images(image_directory, choice)           
    if(choice == '1'):
        X, y = get_data.get_images(brightness_directory)
        X = features_lbp.init_lbp(X)
        gen_scores, imp_scores = matcher_knn.knn(X, y)
        performance.perf(gen_scores, imp_scores)
    elif(choice == '2'):
        X, y = get_data.get_images(contrast_directory)
        X = features_lbp.init_lbp(X)
        gen_scores, imp_scores = matcher_knn.knn(X, y)
        performance.perf(gen_scores, imp_scores)
    elif(choice == '3'):
        X, y = get_data.get_images(sharpness_directory)
        X = features_lbp.init_lbp(X)
        gen_scores, imp_scores = matcher_knn.knn(X, y)
        performance.perf(gen_scores, imp_scores)
    elif(choice == '4'):
        X, y = get_data.get_images(modify_directory)
        X = features_lbp.init_lbp(X)
        gen_scores, imp_scores = matcher_knn.knn(X, y)
        performance.perf(gen_scores, imp_scores)
elif choice == '6':
    main_menu2()
    print("____________________________________________________________________")
    choice = input("Please Select An Option From (1 - 4): ") 
#    X, y = enhance_images.get_images(image_directory, choice)           
    if(choice == '1'):
        X, y = get_data.get_images(brightness_directory)
        X = features_lbp.init_lbp(X)
        gen_scores, imp_scores = matcher_nb.nb(X, y)
        performance.perf(gen_scores, imp_scores)
    elif(choice == '2'):
        X, y = get_data.get_images(contrast_directory)
        X = features_lbp.init_lbp(X)
        gen_scores, imp_scores = matcher_nb.nb(X, y)
        performance.perf(gen_scores, imp_scores)
    elif(choice == '3'):
        X, y = get_data.get_images(sharpness_directory)
        X = features_lbp.init_lbp(X)
        gen_scores, imp_scores = matcher_nb.nb(X, y)
        performance.perf(gen_scores, imp_scores)
    elif(choice == '4'):
        X, y = get_data.get_images(modify_directory)
        X = features_lbp.init_lbp(X)
        gen_scores, imp_scores = matcher_nb.nb(X, y)
        performance.perf(gen_scores, imp_scores)
elif choice == '7':
    main_menu2()
    print("____________________________________________________________________")
    choice = input("Please Select An Option From (1 - 4): ") 
#    X, y = enhance_images.get_images(image_directory, choice)           
    if(choice == '1'):
        X, y = get_data.get_images(brightness_directory)
        X = features_pca.get_pca(X)
        gen_scores, imp_scores = matcher_knn.knn(X, y)
        performance.perf(gen_scores, imp_scores)
    elif(choice == '2'):
        X, y = get_data.get_images(contrast_directory)
        X = features_pca.get_pca(X)
        gen_scores, imp_scores = matcher_knn.knn(X, y)
        performance.perf(gen_scores, imp_scores)
    elif(choice == '3'):
        X, y = get_data.get_images(sharpness_directory)
        X = features_pca.get_pca(X)
        gen_scores, imp_scores = matcher_knn.knn(X, y)
        performance.perf(gen_scores, imp_scores)
    elif(choice == '4'):
        X, y = get_data.get_images(modify_directory)
        X = features_pca.get_pca(X)
        gen_scores, imp_scores = matcher_knn.knn(X, y)
        performance.perf(gen_scores, imp_scores)
elif choice == '8':
    main_menu2()
    print("____________________________________________________________________")
    choice = input("Please Select An Option From (1 - 4): ") 
#    X, y = enhance_images.get_images(image_directory, choice)           
    if(choice == '1'):
        X, y = get_data.get_images(brightness_directory)
        X = features_pca.get_pca(X)
        gen_scores, imp_scores = matcher_nb.nb(X, y)
        performance.perf(gen_scores, imp_scores)
    elif(choice == '2'):
        X, y = get_data.get_images(contrast_directory)
        X = features_pca.get_pca(X)
        gen_scores, imp_scores = matcher_nb.nb(X, y)
        performance.perf(gen_scores, imp_scores)
    elif(choice == '3'):
        X, y = get_data.get_images(sharpness_directory)
        X = features_pca.get_pca(X)
        gen_scores, imp_scores = matcher_nb.nb(X, y)
        performance.perf(gen_scores, imp_scores)
    elif(choice == '4'):
        X, y = get_data.get_images(modify_directory)
        X = features_pca.get_pca(X)
        gen_scores, imp_scores = matcher_nb.nb(X, y)
        performance.perf(gen_scores, imp_scores)
elif choice == '9':
        X, y = get_data.get_images(image_directory)
        X = features_lbp.init_lbp(X)
        gen_scores_knn, imp_scores_knn = matcher_knn.knn(X, y)
        gen_scores_nb, imp_scores_nb = matcher_nb.nb(X, y)
        gen_fusion, imp_fusion = score_fusion.fusion(gen_scores_knn, imp_scores_knn, gen_scores_nb, imp_scores_nb)
        performance.perf(gen_fusion, imp_fusion)
elif choice == '10':
        X, y = get_data.get_images(image_directory)
        X = features_pca.get_pca(X)
        gen_scores_knn, imp_scores_knn = matcher_knn.knn(X, y)
        gen_scores_nb, imp_scores_nb = matcher_nb.nb(X, y)
        gen_fusion, imp_fusion = score_fusion.fusion(gen_scores_knn, imp_scores_knn, gen_scores_nb, imp_scores_nb)
        performance.perf(gen_fusion, imp_fusion)
else: 
    print("Closing")
