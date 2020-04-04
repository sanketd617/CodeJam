#include <bits/stdc++.h>

using namespace std;

bool allGood = true;

int read(int index) {
    cout << (index + 1) << endl;
    int x;
    cin >> x;
    return x;
}

void _complement(vector<int> &beg, vector<int> &end) {
    for(int i = 0; i < beg.size(); i++) {
        beg[i] = !beg[i];
        end[i] = !end[i];
    }
}

void _reverse(vector<int> &beg, vector<int> &end) {
    for(int i = 0; i < beg.size(); i++) {
        int t = beg[i];
        beg[i] = end[i];
        end[i] = t;
    }
}

void _respond(vector<int> &beg, vector<int> &end) {
    for(int i = 0; i < beg.size(); i++) {
        cout << beg[i];
    }
    for(int i = end.size() - 1; i >= 0; i--) {
        cout << end[i];
    }
    cout << endl;

    char c;
    cin >> c;
    if(c == 'N') {
        allGood = false;
    } else {
        allGood = true;
    }
}


void performOperation(int op, vector<int> &beg, vector<int> &end, int ii, int jj) {
    switch (op) {
        case 1:
            _reverse(beg, end);
            break;
        case 2:
            _complement(beg, end);
            _reverse(beg, end);
            break;
        case 3:
            _complement(beg, end);
            break;
    }
}

int predictOperation(vector<int> &beg, int x, int y, int ii, int jj) {
    if(x == beg[ii] and y == beg[jj]) {
        return 0;
    }
    if(x == beg[ii] and y != beg[jj]) {
        return 1;
    }
    if(x != beg[ii] and y == beg[jj]) {
        return 2;
    }
    return 3;
}

void solve(int N) {
    vector<int> beg, end;
    int ii = -1, jj = -1;
    int start = 1;
    int x, y;
    x = read(0);
    y = read(N - 1);
    beg.push_back(x);
    end.push_back(y);
    if(x == y) {
        ii = 0;
    } else {
        jj = 0;
    }

    while ((ii == -1 or jj == -1) and beg.size() + end.size() < N) {
        if(start != 1) {
            int index = (ii == -1 ? jj : ii);
            x = read(index);
            if(beg[index] != x) {
                _complement(beg, end);
            }
            read(index);
        }

        for(int i = start; i < start + 4 and beg.size() + end.size() < N; i++) {
            x = read(i);
            y = read(N - i - 1);
            beg.push_back(x);
            end.push_back(y);
            if(x == y and ii == -1) {
                ii = i;
            }
            if(x != y and jj == -1) {
                jj = i;
            }
        }
        start += 4;
    }

    while (beg.size() + end.size() < N) {
        x = read(ii);
        y = read(jj);
        performOperation(predictOperation(beg, x, y, ii, jj), beg, end, ii, jj);

        for(int i = start; i < min(start + 4, N/2); i++) {
            x = read(i);
            y = read(N - i - 1);
            beg.push_back(x);
            end.push_back(y);
        }
        start += 4;
    }
    _respond(beg, end);
}

int main() {
    int t, b;
    cin >> t >> b;
    while(t-- && allGood) {
        solve(b);
    }
    return 0;
}