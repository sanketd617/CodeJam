#include <iostream>
#include <vector>

using namespace std;
typedef pair<int, int> pii;
typedef pair<char, int> pci;

struct node {
    pii interval;
    int index;
};


typedef vector<node> vnode;

bool cmp(node a, node b) {
    if (a.interval.first == b.interval.first) {
        return a.interval.second < b.interval.second;
    }
    return (a.interval.first < b.interval.first);
}

bool cmp2(pci a, pci b) {
    return a.second < b.second;
}

void solve(vnode &se, int n, int caseNum) {
    cout << "Case #" << caseNum << ": ";
    sort(se.begin(), se.end(), cmp);

    int c = se[0].interval.second, j = 0;
    int chance = 0;
    vector<pci> seq(1, make_pair('C', se[0].index));

//    cout << se[0].index << " " << se[0].interval.first << " " << se[0].interval.second << endl;

    for(int i = 1; i < n; i++) {
        pii cp = se[i].interval;
        int index = se[i].index;
//        cout << index << " " << cp.first << " " << cp.second << endl;
        if(chance == 0) {
            if(cp.first >= c) {
                c = cp.second;
                seq.push_back(make_pair('C', index));
            } else if(cp.first >= j){
                j = cp.second;
                chance = 1;
                seq.push_back(make_pair('J', index));
            } else {
                cout << "IMPOSSIBLE" << endl;
                return;
            }
        } else {
            if(cp.first >= j) {
                j = cp.second;
                seq.push_back(make_pair('J', index));
            } else if(cp.first >= c){
                c = cp.second;
                chance = 0;
                seq.push_back(make_pair('C', index));
            } else {
                cout << "IMPOSSIBLE" << endl;
                return;
            }
        }
    }

    sort(seq.begin(), seq.end(), cmp2);

    for(pci s: seq) {
        cout << s.first;
    }

    cout << endl;
}

int main() {
    int t, caseNum = 1;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vnode se(n);
        for(int i = 0; i < n; i++) {
            cin >> se[i].interval.first >> se[i].interval.second;
            se[i].index = i;
        }
        solve(se, n, caseNum);
        caseNum++;
    }

    return 0;
}