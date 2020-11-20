main.py is setup as a menu: 

Options (1 - 4) will extract features from the "Project Data" folder and run the rest of the commands for that selection.
They consist of the following:

1. Run LBP With Matcher_Knn and See Performance Results
2. Run LBP With Matcher_Nb and See Performance Results
3. Run PCA With Matcher_Knn and See Performance Results
4. Run PCA With Matcher_Nb and See Performance Results

Options (5 - 8) will extract features from the enhanced images folders, based on which you select from the second menu. 
They consist of the following:

5. Enhance Images and Run LBP With Matcher_Knn and See Performance Results
6. Enhance Images and Run LBP With Matcher_Nb and See Performance Results
7. Enhance Images and Run PCA With Matcher_Knn and See Performance Results
8. Enhance Images and Run PCA With Matcher_Nb and See Performance Results

The second menu has 4 options. Brighten Image and Contrast Image are the two primary architectures. The others are used for the presentation: 

1. Brighten Image
2. Contrast Image
3. Sharpen Image
4. Combine all of the above

The folders with the enhanced images are provided, so the features will be extracted directly from them when selecting menu
Options (5 - 8).

NOTE: The enhanced images, depending on processor speeds, will take some time to generate the results.


(Optional)
Options (9 - 10) will run score fusion using LBP and PCA.