#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

void solve(int t, int n, vector <vector<int> > &m) {
    int r = 0, c = 0, trace = 0;
    for(int i = 0; i < n; i++) {
        vector<int> x(n + 1, 0);
        trace += m[i][i];
        for(int j = 0; j < n; j++) {
            x[m[i][j]]++;
            if(x[m[i][j]] > 1) {
                r++;
                break;
            }
        }
    }

    for(int i = 0; i < n; i++) {
        vector<int> x(n + 1, 0);
        for(int j = 0; j < n; j++) {
            x[m[j][i]]++;
            if(x[m[j][i]] > 1) {
                c++;
                break;
            }
        }
    }

    cout << "Case #" << t << ": " << trace << " " << r << " " << c << endl;
}

int main() {
    int t;
    cin >> t;

    int caseNo = 1;

    while (t--) {
        int n;
        cin >> n;
        vector <vector<int> > m(n, vector<int>(n, 0));

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cin >> m[i][j];
            }
        }

        solve(caseNo, n, m);
        caseNo++;
    }
    return 0;
}