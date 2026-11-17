// Independent edge-by-edge census of cyclic words containing every
// noninjective length-three word exactly once, up to rotation.
// Build: c++ -O2 -std=c++17 crosscheck.cpp -o crosscheck && ./crosscheck
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;

struct Edge { int a,b,c; };

uint64_t exhaustive(int q) {
    vector<Edge> edges;
    for(int a=0;a<q;++a) for(int b=0;b<q;++b) for(int c=0;c<q;++c)
        if(a==b || b==c || a==c) edges.push_back({a,b,c});
    vector<vector<int>> transitions(q*q);
    for(int i=0;i<(int)edges.size();++i)
        transitions[edges[i].a*q+edges[i].b].push_back(i);
    const int limit=edges.size();
    vector<char> used(limit,0);
    used[0]=1;  // Lexicographically first edge is uniquely 000.
    assert(edges[0].a==0 && edges[0].b==0 && edges[0].c==0);
    uint64_t answer=0;
    auto dfs=[&](auto &&self, int vertex, int taken)->void {
        if(taken==limit) {
            if(vertex==0) ++answer;
            return;
        }
        for(int id:transitions[vertex]) if(!used[id]) {
            used[id]=1;
            self(self,edges[id].b*q+edges[id].c,taken+1);
            used[id]=0;
        }
    };
    dfs(dfs,0,1);
    return answer;
}

int main() {
    assert(exhaustive(2)==2);
    assert(exhaustive(3)==288);
    cout << "CROSSCHECK_OK\n";
}
