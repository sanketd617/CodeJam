#include <iostream>
#include <vector>

using namespace std;

void solve(string S, int caseNum) {
    cout << "Case #" << caseNum << ": ";
    int p = 0;
    for(int i = 0; i < S.size(); i++) {
        int n = S[i] - '0';
        while (p < n) {
            cout << "(";
            p++;
        }
        while (p > n) {
            cout << ")";
            p--;
        }
        cout << n;
    }
    while (p > 0) {
        cout << ")";
        p--;
    }
    cout << endl;
}

int main() {
    int t, caseNum = 1;
    cin >> t;
    while (t--) {
        string S;
        cin >> S;
        solve(S, caseNum);
        caseNum++;
    }

    return 0;
}