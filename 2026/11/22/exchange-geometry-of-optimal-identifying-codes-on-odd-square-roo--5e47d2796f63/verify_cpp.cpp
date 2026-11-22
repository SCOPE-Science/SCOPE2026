// Independent C++17 exhaustive certificate for optimum codes of K_5 square K_5.
// Build: c++ -std=c++17 -O2 verify_cpp.cpp -o verify && ./verify
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <queue>
#include <unordered_map>
#include <vector>
using namespace std;
constexpr int N=5, S=25, K=7;

bool valid(uint32_t mask) {
    array<uint32_t,N> r{}, c{};
    for(int i=0;i<N;i++) for(int j=0;j<N;j++) {
        unsigned index=N*i+j;
        if((mask>>index)&1u) {r[i] |= 1u<<index; c[j] |= 1u<<index;}
    }
    uint32_t sig[25];int t=0;
    for(int i=0;i<N;i++) for(int j=0;j<N;j++) {
        auto x=r[i]|c[j];
        if(x==0) return false;
        sig[t++]=x;
    }
    sort(sig,sig+25);
    for(int t=1;t<25;t++) if(sig[t]==sig[t-1])return false;
    return true;
}
int main() {
    vector<uint32_t> states;
    uint32_t x=(1u<<K)-1;
    while(x < (1u<<S)){
        if(valid(x)) states.push_back(x);
        uint32_t low=x & (~x+1u), y=x+low;
        if(y==0) break;
        x=(((x^y)>>2)/low)|y;
    }
    assert(states.size()==7200);
    unordered_map<uint32_t,int> pos;
    for(int i=0;i<(int)states.size();++i)pos[states[i]]=i;
    vector<vector<int>> adj(states.size());
    long long sumdeg=0;
    for(int i=0;i<(int)states.size();++i){
        auto s=states[i];
        for(int a=0;a<S;a++)if((s>>a)&1u){
            uint32_t sub=s^(1u<<a);
            for(int b=0;b<S;b++)if(!((s>>b)&1u)){
                auto it=pos.find(sub|(1u<<b));
                if(it!=pos.end())adj[i].push_back(it->second);
            }
        }
        sort(adj[i].begin(),adj[i].end());
        adj[i].erase(unique(adj[i].begin(),adj[i].end()),adj[i].end());
        assert(adj[i].size()==14);
        sumdeg+=adj[i].size();
    }
    assert(sumdeg==100800);
    vector<int> dist(states.size(),-1);
    queue<int> q;q.push(0);dist[0]=0;
    array<int,10> shells{};
    int reached=0;
    while(!q.empty()){
        int u=q.front();q.pop();++reached;
        assert(dist[u]>=0 && dist[u]<10);
        ++shells[dist[u]];
        for(int v:adj[u])if(dist[v]==-1){dist[v]=dist[u]+1;q.push(v);}
    }
    assert(reached==7200);
    assert((shells == array<int,10>{1,14,81,208,504,1024,1696,2184,1352,136}));
    cout << "PASS optima=" << states.size() << " k=7 degree=14 edges=" << sumdeg/2 << " connected=1 diameter=9\n";
    cout << "shells";
    for(int a:shells)cout << " " << a;
    cout<<"\n";
}
