#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
#include <unordered_map> 
using namespace std;

struct HeapNode {
    string value;
    int frequency;
    HeapNode(const string& val, int freq) : value(val), frequency(freq) {}
};

class MaxHeap {

private:
    
    vector<HeapNode> heap;

    // Helper function to swap two HeapNode elements in the heap.
    void swapNodes(int i, int j) 
    {
        HeapNode temp = heap[i];
        heap[i] = heap[j];
        heap[j] = temp;
    }

    // Heapify-up operation to maintain max heap after insertion
    void heapifyUp(int index) {
        int parentIndex = (index - 1) / 2;
        while (index > 0 && heap[index].frequency > heap[parentIndex].frequency) {
            swapNodes(index, parentIndex);
            index = parentIndex;
            parentIndex = (index - 1) / 2;
        }
    }

public:

    MaxHeap() {} // Constructor

    // Insert a new word into the heap and update frequency
    void insert(const string& value) {
        
        // Find the word in the heap and update its frequency
        for (HeapNode& node : heap) {
            if (node.value == value) {
                node.frequency++;
                // Perform heapify-up 
                heapifyUp(&node - &heap[0]);
                return;
            }
        }

        // If the word is not in the heap, add it with a frequency of 1
        heap.emplace_back(value, 1);
        // Perform heapify-up 
        heapifyUp(heap.size() - 1);
    }

    // Function to search for a word or phrase in the max heap
    bool search(const string& value) {
        for (const HeapNode& node : heap) {
            if (node.value == value) {
                return true;
            }
        }
        return false;
    }

    // Function to get the top k elements with the highest frequencies
    vector<string> getTopKFrequent(int k) {
        
        vector<string> topWords;
        int n = heap.size();

        for (int i = 0; i < k && i < n; i++) {
            topWords.push_back(heap[i].value);
        }

        return topWords;
    }
};

bool comparePhrasesWithHyphens(const string& str1, const string& str2) {
    string phrase1 = str1;
    string phrase2 = str2;
    transform(phrase1.begin(), phrase1.end(), phrase1.begin(), ::tolower);
    transform(phrase2.begin(), phrase2.end(), phrase2.begin(), ::tolower);
    return phrase1 == phrase2;
}

string toLowercase(string str) {
    transform(str.begin(), str.end(), str.begin(), ::tolower);
    return str;
}

string replaceSpacesWithHyphens(string str) {
    replace(str.begin(), str.end(), ' ', '-');
    return str;
}

int main() {
    
    MaxHeap maxHeap;

    // Populate the max heap with words from files (as before)
    string filenames[] = {
        "words_list_output.csv",
        "final_buzzwords_skills_output.csv",
        "combined_words_output.csv",
        "pleaseopen_output.csv",
        "verb_list_output.csv",
        "top_words_output.csv",
    };

    for (const string& filename : filenames) {
        ifstream file(filename);
        if (!file.is_open()) {
            cerr << "Failed to open file: " << filename << endl;
            return 1;
        }

        string line;
        while (getline(file, line)) {
            stringstream ss(line);
            string word;
            if (getline(ss, word, ',')) {
                maxHeap.insert(word);
            }
        }

        file.close();
    }

    cout << "Enter a paragraph: ";
    
    string paragraph;
    string line;
    // getline(cin, paragraph);

    cout << "Paste a job posting then type the word \"ENDPOST\" on a new line and hit enter." << endl;
    while (getline(cin, line) && line != "ENDPOST") {
        paragraph += line + "\n";
    }

    ofstream file1("job-post.txt");
    file1 << paragraph;
    file1.close();

    paragraph = toLowercase(paragraph);
    
    vector<string> overlappingWords;
    stringstream ss(paragraph);
    string word;
    while (ss >> word) {
        if (find(overlappingWords.begin(), overlappingWords.end(), word) == overlappingWords.end() &&
            find(overlappingWords.begin(), overlappingWords.end(), replaceSpacesWithHyphens(word)) == overlappingWords.end()) {
            if (maxHeap.search(word) || maxHeap.search(replaceSpacesWithHyphens(word))) {
                overlappingWords.push_back(word);
            }
        }
    }

    ofstream file2("skill-list.txt");

    // cout << "Overlapping:" << endl;
    // for (string overlappingWord : overlappingWords) {
    //     cout << overlappingWord << endl;
    // }
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
