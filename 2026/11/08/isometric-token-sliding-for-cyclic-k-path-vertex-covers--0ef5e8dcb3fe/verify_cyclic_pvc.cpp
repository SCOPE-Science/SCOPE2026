// Independent C++17 re-enumeration of legal cyclic k-path covers and their slide metric.
// Compile: g++ -O2 -std=c++17 verify_cyclic_pvc.cpp -o verify_cyclic_pvc
// Run: ./verify_cyclic_pvc
#include <bits/stdc++.h>
using namespace std;

bool admissible(int n, int k, int s) {
    for (int v = 0; v < n; ++v) {
        int occupied = 0;
        for (int d = 0; d < k; ++d) occupied |= (s >> ((v + d) % n)) & 1;
        if (!occupied) return false;
    }
    return true;
}

int flow_metric(int n, int x, int y) {
    vector<int> imbalance;
    int delta = 0;
    for (int i = 0; i < n; ++i) {
        delta += ((x & (1 << i)) != 0) - ((y & (1 << i)) != 0);
        imbalance.push_back(delta);
    }
    nth_element(imbalance.begin(), imbalance.begin() + n/2, imbalance.end());
    int pivot = imbalance[n/2], total = 0;
    for (int value : imbalance) total += abs(value - pivot);
    return total;
}

int main() {
    long long roots=0, instances=0;
    for(int n=3;n<=12;++n) {
        for(int k=2;k<n;++k) {
            for(int t=(n+k-1)/k;t<=n;++t) {
                vector<int> states;
                unordered_map<int,int> index;
                for(int s=0;s<(1<<n);++s) {
                    if(__builtin_popcount((unsigned)s)==t && admissible(n,k,s)) {
                        index[s] = (int)states.size();
                        states.push_back(s);
                    }
                }
                vector<vector<int>> links(states.size());
                for(int i=0;i<(int)states.size();++i) {
                    int s=states[i];
                    for(int edge=0;edge<n;++edge) {
                        int v=(edge+1)%n, mask=(1<<edge)|(1<<v);
                        int bits=s&mask;
                        if(bits==0 || bits==mask) continue;
                        int q=s^mask;
                        auto it=index.find(q);
                        if(it!=index.end()) links[i].push_back(it->second);
                    }
                }
                bool frozen=(k*t==n);
                for(int i=0;i<(int)states.size();++i) {
                    vector<int> d(states.size(),-1);
                    queue<int> q;d[i]=0;q.push(i);
                    while(!q.empty()) {
                        int v=q.front();q.pop();
                        for(int w:links[v]) if(d[w]<0) {
                            d[w]=d[v]+1;q.push(w);
                        }
                    }
                    for(int j=0;j<(int)states.size();++j) {
                        int expected=(frozen && i!=j)?-1:flow_metric(n,states[i],states[j]);
                        if(d[j]!=expected) {
                            cerr<<"MISMATCH "<<n<<" "<<k<<" "<<t<<" "<<states[i]<<" "<<states[j]<<" "<<d[j]<<" "<<expected<<"\n";
                            return 1;
                        }
                    }
                }
                roots+=states.size(); ++instances;
            }
        }
    }
    cout<<"CPP_INDEPENDENT_PASS instances="<<instances<<" BFS_roots="<<roots<<"\n";
}
