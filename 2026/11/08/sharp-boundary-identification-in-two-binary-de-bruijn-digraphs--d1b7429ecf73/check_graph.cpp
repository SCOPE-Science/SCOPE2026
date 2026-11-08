// Exhaustive graph-theoretic verification via reverse breadth-first search.
// Compile with: g++ -std=c++17 -O2 -Wall -Wextra check_graph.cpp -o check_graph
// Run from this directory: ./check_graph
#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <queue>
#include <string>
#include <cassert>
#include <utility>
using namespace std;

int main() {
    ifstream in("witnesses.tsv");
    if (!in) { cerr << "Missing witnesses.tsv\n"; return 1; }
    int n, t, lines=0;
    string hex;
    while (in >> n >> t >> hex) {
        assert((n==7 && t==4) || (n==9 && t==5));
        int N = 1<<n;
        assert((int)hex.size() == (N/2+3)/4);
        vector<char> chosen(N,0);
        for (int p=0; p<N/2; ++p) {
            char ch = hex[hex.size()-1-p/4];
            int d = (ch>='0' && ch<='9') ? (ch-'0') : (ch-'a'+10);
            int bit = (d>>(p%4))&1;
            chosen[2*p+bit] = 1;
        }
        int count=0;
        for (auto x:chosen) count+=x;
        assert(count == N/2);
        // Build reverse adjacency from forward edges u -> ((2*u+b) mod N).
        vector<vector<int>> incoming(N);
        for (int u=0;u<N;++u) for (int b=0;b<2;++b)
            incoming[((u<<1)&(N-1))|b].push_back(u);
        set<string> signatures;
        for (int v=0;v<N;++v) {
            vector<int> dist(N,-1);
            queue<int> q; q.push(v);dist[v]=0;
            while (!q.empty()) {
                int x=q.front();q.pop();
                if (dist[x]==t) continue;
                for (int u:incoming[x]) if (dist[u]<0) {
                    dist[u]=dist[x]+1;
                    q.push(u);
                }
            }
            string signature(N,'0');
            for (int u=0;u<N;++u) if(chosen[u] && dist[u]>=0) signature[u]='1';
            assert(signature.find('1')!=string::npos);
            assert(signatures.insert(signature).second);
        }
        assert((int)signatures.size()==N);
        cout<<"GRAPH_BFS_OK n="<<n<<" t="<<t<<" code_size="<<count
            <<" unique_signatures="<<signatures.size()<<"\n";
        ++lines;
    }
    assert(lines==2);
    return 0;
}
