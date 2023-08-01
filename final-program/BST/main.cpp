#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

struct Node {
    string value;
    int height;
    Node* left;
    Node* right;

    Node(const string& val) : value(val), height(0), left(nullptr), right(nullptr) {}
};
bool comparePhrasesWithHyphens(const string& str1, const string& str2) {
    string phrase1 = str1;
    string phrase2 = str2;
    transform(phrase1.begin(), phrase1.end(), phrase1.begin(), ::tolower);
    transform(phrase2.begin(), phrase2.end(), phrase2.begin(), ::tolower);
    return phrase1 == phrase2;
}
class AVLTree{
private:
    Node* root;

    int height(Node* node){
        if (node == nullptr){
            return -1;
        } else {
            return node->height;
        }
    }

    int getBalanceFactor(Node* node){
        if (node == nullptr) {
            return 0;
        }
        return height(node->left) - height(node->right);
    }

    Node* rotateRight(Node* node){
        Node* newRoot = node->left;
        node->left = newRoot->right;
        newRoot->right = node;

        node->height = max(height(node->left), height(node->right)) + 1;
        newRoot->height = max(height(newRoot->left), height(newRoot->right)) + 1;

        return newRoot;
    }

    Node* rotateLeft(Node* node){
        Node* newRoot = node->right;
        node->right = newRoot->left;
        newRoot->left = node;

        node->height = max(height(node->left), height(node->right)) + 1;
        newRoot->height = max(height(newRoot->left), height(newRoot->right)) + 1;

        return newRoot;
    }
    Node* searchRecursive(Node* node, const string& value) {
        if (node == nullptr || comparePhrasesWithHyphens(value, node->value)) {
            return node;
        }

        if (value < node->value) {
            return searchRecursive(node->left, value);
        } else {
            return searchRecursive(node->right, value);
        }
    }

    Node* insertRecursive(Node* node, const string& value) {
        if (node == nullptr) {
            return new Node(value);
        }

        // Compare phrases with hyphens
        if (comparePhrasesWithHyphens(value, node->value)) {
            // Handle the case when the phrase already exists in the tree (no duplicates allowed)
            return node;
        }

        if (value < node->value) {
            node->left = insertRecursive(node->left, value);
        } else if (value > node->value) {
            node->right = insertRecursive(node->right, value);
        }

        node->height = max(height(node->left), height(node->right)) + 1;

        int balanceFactor = getBalanceFactor(node);

        if (balanceFactor > 1 && value < node->left->value){
            return rotateRight(node);
        }

        if (balanceFactor < -1 && value > node->right->value){
            return rotateLeft(node);
        }

        if (balanceFactor > 1 && value > node->left->value){
            node->left = rotateLeft(node->left);
            return rotateRight(node);
        }

        if (balanceFactor < -1 && value < node->right->value){
            node->right = rotateRight(node->right);
            return rotateLeft(node);
        }

        return node;
    }

    void inorderTraversalRecursive(Node* node){
        if (node != nullptr) {
            inorderTraversalRecursive(node->left);
            cout << node->value << " ";
            inorderTraversalRecursive(node->right);
        }
    }


public:
    AVLTree() : root(nullptr) {}

    void insert(const string& value){
        root = insertRecursive(root, value);
    }

    void inorderTraversal(){
        inorderTraversalRecursive(root);
    }
    Node* search(const string& value){
        return searchRecursive(root, value);
    }
    string toLowercase(string str){
        transform(str.begin(), str.end(), str.begin(), ::tolower);
        return str;
    }

// Function to replace spaces with hyphens in a string
    string replaceSpacesWithHyphens(string str){
        replace(str.begin(), str.end(), ' ', '-');
        return str;
    }
};



int main() {
    AVLTree avlTree;

    // Populate the AVL tree with words from files (as before)
    string filenames[] = {
            "words_list_output.csv",
            "final_buzzwords_skills_output.csv",
            "combined_words_output.csv",
            "pleaseopen_output.csv",
            "verb_list_output.csv",
            "top_words_output.csv"
    };

    for(const string& filename : filenames){
        ifstream file(filename);
        if (!file.is_open()) {
            cerr << "Failed to open file: " << filename << endl;
            return 1;
        }

        string line;
        while (getline(file, line)) {
            stringstream ss(line);
            string word;
            if (getline(ss, word, ',')){
                avlTree.insert(word);
            }
        }
        //avlTree.inorderTraversal();
        file.close();
    }


    //cout << "Enter a paragraph: ";
    //string paragraph;               //Take input paragraph from the user
    //getline(cin, paragraph);
    string paragraph;
    string line;

    cout << "Paste a job posting then type the word \"ENDPOST\" on a new line and hit enter." << endl;
    while (getline(cin, line) && line != "ENDPOST") {
        paragraph += line + "\n";
    }

    ofstream file1("job-post.txt");
    file1 << paragraph;
    file1.close();

    paragraph = avlTree.toLowercase(paragraph);


    vector<string> overlappingWords;    //Compare to words in tree
    stringstream ss(paragraph);
    string word;
    while (ss >> word) {
        if (avlTree.search(word)) {
            overlappingWords.push_back(word);
        }

        int hyphenPos = word.find('-');        // Check for phrases with hyphens
        while (hyphenPos != string::npos) {
            string phrase1 = word.substr(0, hyphenPos);
            string phrase2 = word.substr(hyphenPos + 1);
            string phraseWithHyphen = phrase1 + "-" + phrase2;
            if (avlTree.search(phraseWithHyphen)) {
                overlappingWords.push_back(phraseWithHyphen);
            }
            hyphenPos = word.find('-', hyphenPos + 1);
        }
    }
    
    ofstream file2("skill-list.txt");

    //cout << "Overlapping:" << endl;
    for (string overlappingWord : overlappingWords) {
        for (char& c : overlappingWord) {
            if (c == '-') {
                c = ' ';
            }
        }
        file2 << overlappingWord;
        if (&overlappingWord != &overlappingWords.back()) {
            file2 << ", ";
        }
    }

    file2.close();

    return 0;
}
