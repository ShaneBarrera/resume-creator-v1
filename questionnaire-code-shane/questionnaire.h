#pragma once
#include <vector>
#include <string>

using namespace std; 

// Function to read questions from a file
void readQuestionsFromFile(vector<string>& questions);

// Function to handle the questionnaire
void fillQuestionnaire(vector<string>& answers, const vector<string>& questions);

// Function to save user data into a CSV file
void saveUserData(const vector<string>& answers, const vector<string>& questions);

// Define the CSV file name and categories
const string csvFileName = "user_data.csv";
