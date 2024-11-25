#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#                                                                             
# PROGRAMMER: 
# DATE CREATED:
# REVISED DATE: 
# PURPOSE: Create a function print_results that prints the results statistics
#          from the results statistics dictionary (results_stats_dic). It 
#          should also allow the user to be able to print out cases of misclassified
#          dogs and cases of misclassified breeds of dog using the Results 
#          dictionary (results_dic).  
#         This function inputs:
#            -The results dictionary as results_dic within print_results 
#             function and results for the function call within main.
#            -The results statistics dictionary as results_stats_dic within 
#             print_results function and results_stats for the function call within main.
#            -The CNN model architecture as model wihtin print_results function
#             and in_arg.arch for the function call within main. 
#            -Prints Incorrectly Classified Dogs as print_incorrect_dogs within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#            -Prints Incorrectly Classified Breeds as print_incorrect_breed within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#         This function does not output anything other than printing a summary
#         of the final results.
##
# TODO 6: Define print_results function below, specifically replace the None
#       below by the function definition of the print_results function. 
#       Notice that this function doesn't to return anything because it  
#       prints a summary of the results using results_dic and results_stats_dic
# 
def print_results(results, results_stats, model, print_incorrect_dogs=False, print_incorrect_breed=False):
    print("\nResults Summary for Model Architecture:", model.upper())
    print("N Images: {}".format(results_stats['n_images']))
    print("N Dog Images: {}".format(results_stats['n_dogs_img']))
    print("N Not-a-Dog Images: {}".format(results_stats['n_notdogs_img']))
    print("% Correct Dogs: {:.2f}".format(results_stats['pct_correct_dogs']))
    print("% Correct Breed: {:.2f}".format(results_stats['pct_correct_breed']))
    print("% Correct Not-a-Dog: {:.2f}".format(results_stats['pct_correct_notdogs']))
    
    if print_incorrect_dogs:
        print("\nIncorrectly Classified Dogs:")
        for filename, result in results.items():
            if result[3] == 1 and result[4] == 0:
                print(f"Filename: {filename}, Label: {result[0]}, Classifier: {result[1]}")
    
    if print_incorrect_breed:
        print("\nIncorrectly Classified Breeds:")
        for filename, result in results.items():
            if result[3] == 1 and result[4] == 1 and result[2] == 0:
                print(f"Filename: {filename}, Label: {result[0]}, Classifier: {result[1]}")

                