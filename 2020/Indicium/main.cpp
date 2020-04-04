#include<bits/stdc++.h>
#include<algorithm>

using namespace std;

#define N 51

bool check(int &row, int &col, vector<vector<int> > &matrix, int n, int k) {
    for (row = 0; row < n; row++) {
        for (col = 0; col < n; col++) {
            if (matrix[row][col] == -1) {
                return true;
            }
        }
    }
    return false;
}

bool valid(int x, int y, int num, vector<vector<int> > &matrix, int n, int k) {
    for(int i = 0; i < n; i++) {
        if (matrix[i][y] == num) {
            return false;
        }
    }
    for(int i = 0; i < n; i++) {
        if (matrix[x][i] == num) {
            return false;
        }
    }
    return true;
}

bool rec(vector<vector<int> > &matrix, int n, int k) {
    int x, y;
    if (!check(x, y, matrix, n, k)) {
        return true;
    }
    for (int i = 1; i <= n; i++) {
        if (valid(x, y, i, matrix, n, k)) {
            matrix[x][y] = i;
            if (rec(matrix, n, k)) {
                return true;
            }
            matrix[x][y] = -1;
        }
    }
    return false;
}

void solve(int n, int k, int caseNum) {
    if (n == 1) {
        cout << "Case #" << caseNum << ": " << "POSSIBLE" << "\n";
        cout << 1 << "\n";
        return;
    }
    if (k == n + 1 || k == n * n - 1) {
        cout << "Case #" << caseNum << ": " << "IMPOSSIBLE" << "\n";
        return;
    }

    vector<vector<int> > matrix(N, vector<int>(N, -1));
    for(int i = 0; i < n; i++) {
        matrix[i][i] = k / n;
    }
    int t1 = k % n;
    int index = 0;
    while (t1--) {
        matrix[index][index]++;
        index++;
    }
    if ((k % n == 1) || (k % n == n - 1)) {
        matrix[n / 2][n / 2]++;
        matrix[n / 2 - 1][n / 2 - 1]--;
    }
    if (rec(matrix, n, k)) {
        cout << "Case #" << caseNum << ": " << "POSSIBLE" << "\n";
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                cout << matrix[i][j] << " ";
            }
            cout << "\n";
        }
    } else {
        cout << "Case #" << caseNum << ": " << "IMPOSSIBLE" << "\n";
    }
}


int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int t;
    cin >> t;
    int caseNum = 1;

    while (t--) {
        int n, k;
        cin >> n >> k;

        solve(n, k, caseNum);

        caseNum++;
    }
    return 0;
}