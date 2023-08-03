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
    Node(const string& val) : value(val), height(0), left(nullptr), right(nullptr) {} //Constructor
};
bool comparePhrases(const string& string_1, const string& string_2){
    string phrase1 = string_1;
    string phrase2 = string_2;
    transform(phrase1.begin(), phrase1.end(), phrase1.begin(), ::tolower); //converts to lowercase
    transform(phrase2.begin(), phrase2.end(), phrase2.begin(), ::tolower);
    return phrase1 == phrase2;               //Compares lower case versions of words
}
class AVLTree{
private:
    int height(Node* node){                 //All the helper/rotation functions
        if (node == nullptr){
            return -1;
        }
        else{
            return node->height;
        }
    }

    int getBalanceFactor(Node* node){           //Based on Aman's slides
        if (node == nullptr) {
            return 0;
        }
        return height(node->left) - height(node->right);
    }

    Node* rotateRight(Node* node){              //Rotation functions based on content in Aman's slides
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

public:
    Node* root;
    AVLTree() : root(nullptr) {}

    Node* searchRecursive(Node* node, const string& value){
        if (node == nullptr || comparePhrases(value, node->value)){ //If at end of tree or matched
            return node;
        }
        if (value < node->value){                           //Searches based on alphabetical order
            return searchRecursive(node->left, value);
        }
        else{
            return searchRecursive(node->right, value);
        }
    }

    Node* insertRecursive(Node* node, const string& value){
        if (node == nullptr){               //Once it reaches the end creates the new node
            return new Node(value);
        }

        if (comparePhrases(value, node->value)){  //If already in tree
            return node;
        }

        if (value < node->value){
            node->left = insertRecursive(node->left, value);  //Enters left subtree if less
        }
        else if (value > node->value){
            node->right = insertRecursive(node->right, value); //Right subtree if more
        }

        node->height = max(height(node->left), height(node->right)) + 1;  //Updates height after insertion
        int balanceFactor = getBalanceFactor(node);                 //Checks balance factor and performs rotations

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

    void inorderTraversalRecursive(Node* node){             //Based on Amans Slides
        if (node != nullptr) {
            inorderTraversalRecursive(node->left);
            cout << node->value << " ";                     //Outputs in alphabetical order
            inorderTraversalRecursive(node->right);
        }
    }

    string toLowercase(string str){                         //Lowercase without comparison
        transform(str.begin(), str.end(), str.begin(), ::tolower);
        return str;
    }

};

int main() {
    AVLTree avlTree;
    string filenames[] = {
            "C:\\Users\\chmer\\CLionProjects\\Project3BST\\words_list_output.csv",
            "C:\\Users\\chmer\\CLionProjects\\Project3BST\\final_buzzwords_skills_output.csv",
            "C:\\Users\\chmer\\CLionProjects\\Project3BST\\combined_words_output.csv",
            "C:\\Users\\chmer\\CLionProjects\\Project3BST\\pleaseopen_output.csv",
            "C:\\Users\\chmer\\CLionProjects\\Project3BST\\verb_list_output.csv",
            "C:\\Users\\chmer\\CLionProjects\\Project3BST\\top_words_output.csv"
    };

    for (const string& filename : filenames) {  //Iterates through array and reads files
        ifstream file(filename);
        if (!file.is_open()) {
            return 1;
        }

        string line;
        while (getline(file, line)) {
            stringstream ss(line);
            string word;
            if (getline(ss, word, ',')) {           //Comma as delimiter to read CSV
                avlTree.root = avlTree.insertRecursive(avlTree.root, word);  //Inserts words from files into tree
            }
        }
        file.close();
    }

    string paragraph;               // Take input paragraph from the user
    getline(cin, paragraph);
    paragraph = avlTree.toLowercase(paragraph);

    vector<string> overlappingWords;    // Compare to words in tree
    stringstream ss(paragraph);
    string word;
    while (ss >> word) {
        if (avlTree.searchRecursive(avlTree.root, word)){
            overlappingWords.push_back(word);
        }

        int hyphenPos = word.find('-');        // Check for phrases with hyphens
        while (hyphenPos != string::npos) {
            string phrase1 = word.substr(0, hyphenPos);
            string phrase2 = word.substr(hyphenPos + 1);
            string phraseWithHyphen = phrase1 + "-" + phrase2;
            if (avlTree.searchRecursive(avlTree.root, phraseWithHyphen)){
                overlappingWords.push_back(phraseWithHyphen);
            }
            hyphenPos = word.find('-', hyphenPos + 1);
        }
    }

    for (string overlappingWord : overlappingWords){        //Removes hyphens in words
        for(char& c : overlappingWord) {
            if (c == '-'){
                c = ' ';
            }
        }
        cout << overlappingWord << endl;
    }
    return 0;
}
