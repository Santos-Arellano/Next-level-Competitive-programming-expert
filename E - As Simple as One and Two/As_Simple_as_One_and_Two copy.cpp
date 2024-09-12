#include <iostream>
#include <string>
#include <vector>

using namespace std;

void calculate(string s) {
    int sz = s.size()-2;
    vector<int> change;
    for (int i=0; i<sz; i++) {
        if (s[i] == 'o' && s[i+1] == 'n' && s[i+2] == 'e') {
            if (i+3<=s.size() && s[i+3] == 'e') {
                s[i] = 'z';
                change.push_back(i+1);
            } else {
                s[i+2] = 'z';
                change.push_back(i+3);
            }
        } else if (s[i] == 't' && s[i+1] == 'w' && s[i+2] == 'o') {
            if (i+3<=s.size() && s[i+3] == 'o') {
                change.push_back(i+3);
            } else {
                change.push_back(i+3);
            }
        }
    }
    cout << change.size() << endl;
    for (int n : change) {
        cout << n << " ";
    }
    cout << endl;

}

int main() {
    int n;
    cin >> n;
    string s;
    for (int i=0; i<n; i++) {
        cin >> s;
        calculate(s);
    }

    return 0;
}