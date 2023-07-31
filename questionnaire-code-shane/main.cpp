#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include "questionnaire.h"

using namespace std;

int main() {
    vector<string> questions;
    readQuestionsFromFile(questions);

    vector<string> userAnswers;
    bool hasSavedData = false;

    // Check if the user data CSV file exists
    ifstream file(csvFileName);
    if (file.good()) {
        char choice;
        cout << "Do you want to use saved data (Y/N)? ";
        cin >> choice;

        if (choice == 'Y' || choice == 'y') {
            // TODO: Load existing user data from the CSV file
            // Implement this if you want to provide the option to use saved data.
            hasSavedData = true;
        }
    }

    if (!hasSavedData) {
        fillQuestionnaire(userAnswers, questions);
        saveUserData(userAnswers, questions);
    }

    return 0;
}
