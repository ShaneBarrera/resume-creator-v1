#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include "questionnaire.h"

using namespace std;

// Updated categories vector without the "Type" category
const vector<string> categories = {
    "Resume Type", // Resume type 
    "Skills", "Skills",  // Two skill categories
    "Education", "Education", "Education", "Education",  // Four education categories
    "Research",  // Research category
    "Experience", "Experience", "Experience", "Experience", "Experience", "Experience", "Experience", "Experience", "Experience", "Experience"  // Nine experience categories
};

// Function to read questions from a file
void readQuestionsFromFile(vector<string>& questions) {
    ifstream file("questions.txt");
    if (!file) {
        cerr << "Error opening the questions file.\n";
        return;
    }

    string question;
    while (getline(file, question)) {
        // Check if the question already exists in the questions vector before adding it
        if (find(questions.begin(), questions.end(), question) == questions.end()) {
            questions.push_back(question);
        }
    }
}

// Function to handle the questionnaire
void fillQuestionnaire(vector<string>& answers, const vector<string>& questions) {
    cout << "Please fill out the questionnaire:\n";
    for (size_t i = 0; i < categories.size(); ++i) {
        string answer;
        //cout << categories[i] << endl;
        cout << questions[i] << endl;
        getline(cin, answer);
        answers.push_back(answer);
    }
}

void saveUserData(const vector<string>& answers, const vector<string>& questions) {
    ofstream file(csvFileName);
    if (!file) {
        cerr << "Error creating the file.\n";
        return;
    }

    file << "Category,Question,Answer\n"; // Header row

    size_t questionIndex = 0;
    for (size_t i = 0; i < categories.size(); ++i) {
        // Get the count of occurrences for the current category
        size_t categoryCount = count(categories.begin(), categories.begin() + i + 1, categories[i]);

        // Write the question and answer for the current category based on the category count
        file << categories[i] << ",\"" << questions[questionIndex + categoryCount - 1] << "\",\"" << answers[questionIndex + categoryCount - 1] << "\"\n";

        // Increment the question index only when we reach the end of the current category
        if (i + 1 == categories.size() || categories[i] != categories[i + 1]) {
            questionIndex += categoryCount;
        }
    }

    cout << "User data saved successfully.\n";
}






