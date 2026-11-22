// Independent finite certificate: BFS graph distances rather than intersection formulas.
// Build Petersen graph using the standard outer/inner GP(5,2) coordinates.
#include <array>
#include <algorithm>
#include <cassert>
#include <iostream>
#include <queue>
#include <set>
#include <vector>
using namespace std;
int main() {
    vector<pair<int,int>> E;
    for (int i=0;i<5;i++) {
        E.emplace_back(i,(i+1)%5); // outer cycle
        E.emplace_back(i,5+i);     // spokes
        E.emplace_back(5+i,5+(i+2)%5); // inner pentagram
    }
    vector<vector<int>> adj(10);
    for (auto [a,b]:E) {adj[a].push_back(b);adj[b].push_back(a);}
    vector<array<int,10>> d(10);
    for(int i=0;i<10;i++) {
        d[i].fill(1000);d[i][i]=0;queue<int> q;q.push(i);
        while(!q.empty()) {
            int v=q.front();q.pop();
            for(int w:adj[v]) if(d[i][w]>d[i][v]+1) {d[i][w]=d[i][v]+1;q.push(w);}
        }
    }
    array<array<int,15>,10> ed{};
    for(int v=0;v<10;v++) for(int e=0;e<15;e++)
        ed[v][e]=min(d[v][E[e].first],d[v][E[e].second]);
    array<int,11> resolving{},covering{},joint{};
    for(int mask=0;mask<(1<<10);mask++) {
        int k=__builtin_popcount((unsigned)mask);
        set<vector<int>> signs;
        bool covers=true;
        for(int e=0;e<15;e++) {
            vector<int> sign;
            bool dominated=false;
            for(int v=0;v<10;v++) if(mask&(1<<v)) {
                sign.push_back(ed[v][e]);
                dominated = dominated || ed[v][e] <=1;
            }
            covers &= dominated;signs.insert(sign);
        }
        bool resolves = signs.size()==15;
        if(resolves)resolving[k]++;
        if(covers)covering[k]++;
        if(covers && resolves)joint[k]++;
    }
    assert((resolving==array<int,11>{0,0,0,0,15,162,195,120,45,10,1}));
    assert((covering==array<int,11>{0,0,0,60,195,252,210,120,45,10,1}));
    assert((joint==array<int,11>{0,0,0,0,0,162,195,120,45,10,1}));
    cout << "PET_X5_BFS_OK\n";
}
