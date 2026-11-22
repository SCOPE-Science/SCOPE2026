// Independent exhaustive checker for two induced-path partitions of the icosahedron.
#include <array>
#include <vector>
#include <queue>
#include <algorithm>
#include <iostream>
#include <cassert>
#include <map>
using namespace std;
int main(){
    const int N=12, ALL=(1<<N)-1;
    array<array<bool,N>,N> g{};
    auto edge=[&](int x,int y){g[x][y]=g[y][x]=true;};
    // Two pentagonal rims, two poles, and ten staggered rim-crossing edges.
    for(int j=0;j<5;++j){
        int u=1+j,v=6+j;
        edge(0,u);edge(11,v);
        edge(u,1+(j+1)%5);edge(v,6+(j+1)%5);
        edge(u,v);edge(u,6+(j+4)%5);
    }
    int edges=0;
    for(int i=0;i<N;++i){int degree=0;for(int j=0;j<N;++j)if(g[i][j])++degree;if(degree!=5)return 1;for(int j=i+1;j<N;++j)edges+=g[i][j];}
    if(edges!=30)return 2;
    auto pop=[](int a){return __builtin_popcount((unsigned)a);};
    auto graph_edges=[&](int s){int e=0;for(int u=0;u<N;++u)if(s>>u&1)for(int v=u+1;v<N;++v)if((s>>v&1)&&g[u][v])++e;return e;};
    // Independent predicate: component search, with the identity |E|=|V|-c.
    auto forest=[&](int s){
        array<bool,N> seen{};
        int components=0;
        for(int v=0;v<N;++v)if((s>>v&1) && !seen[v]){
            ++components;queue<int> q;q.push(v);seen[v]=true;
            while(!q.empty()){int w=q.front();q.pop();for(int z=0;z<N;++z)if(g[w][z]&&(s>>z&1)&&!seen[z]){seen[z]=true;q.push(z);}}
        }
        return graph_edges(s)==pop(s)-components;
    };
    array<int,13> forestcounts{};
    vector<int> states;
    int mink6=100,mink7=100;
    for(int s=0;s<=ALL;++s){
        if(forest(s))++forestcounts[pop(s)];
        if(pop(s)==6){mink6=min(mink6,graph_edges(s));if(forest(s)&&forest(ALL^s))states.push_back(s);}
        if(pop(s)==7)mink7=min(mink7,graph_edges(s));
    }
    if(forestcounts!=array<int,13>{1,12,66,200,345,300,60,0,0,0,0,0,0})return 3;
    if(mink6!=5||mink7!=8||states.size()!=60)return 4;
    for(int s=0;s<=ALL;++s)if(pop(s)==6&&forest(s)){
        if(!forest(ALL^s))return 5;
        if(graph_edges(s)!=5)return 6;
    }
    vector<vector<int>> adj(states.size());int count_edges=0;
    for(int a=0;a<(int)states.size();++a)for(int b=0;b<a;++b)if(pop(states[a]^states[b])==2){
        int lost=states[a]&~states[b], gained=states[b]&~states[a];
        int x=__builtin_ctz((unsigned)lost),y=__builtin_ctz((unsigned)gained);
        if(!g[x][y])return 7;
        adj[a].push_back(b);adj[b].push_back(a);++count_edges;
    }
    if(count_edges!=120)return 8;
    for(auto x:adj)if(x.size()!=4)return 9;
    map<vector<int>,int> profiles;
    int diameter_pairs=0;
    map<pair<int,int>,int> hist;
    vector<int> layer(states.size(),-1);
    for(int src=0;src<(int)states.size();++src){
        vector<int> d(states.size(),-1);queue<int>q;d[src]=0;q.push(src);
        while(!q.empty()){int u=q.front();q.pop();for(int v:adj[u])if(d[v]<0){d[v]=d[u]+1;q.push(v);}}
        vector<int> shell(7);
        for(int x:d){if(x<0||x>6)return 10;++shell[x];}
        ++profiles[shell];
        if(shell[6]!=1)return 11;
        int c=-1;for(int j=0;j<(int)states.size();++j)if(states[j]==(ALL^states[src]))c=j;
        if(c<0||d[c]!=6)return 12;
        ++diameter_pairs;
        for(int j=0;j<src;++j){
            int delta=pop(states[src]&~states[j]);
            ++hist[{delta,d[j]}];
        }
        if(src==0)for(int j=0;j<(int)states.size();++j)layer[j]=d[j]%2;
    }
    if(profiles!=map<vector<int>,int>{{{1,4,12,17,16,9,1},60}}||diameter_pairs!=60)return 13;
    map<pair<int,int>,int> expected={{{1,1},120},{{2,2},360},{{2,3},150},
       {{3,3},360},{{3,4},120},{{4,4},360},{{4,5},150},{{5,5},120},{{6,6},30}};
    if(hist!=expected)return 14;
    int side0=0;
    for(int v=0;v<(int)states.size();++v){
        if(layer[v]==0)++side0;
        for(int w:adj[v])if(layer[v]==layer[w])return 15;
    }
    if(side0!=30)return 16;
    cout<<"VALID=60 EDGES=120 DEGREE=4 CONNECTED=YES DIAMETER=6"<<'\n';
    cout<<"SHELLS=1,4,12,17,16,9,1 UNIQUE_ANTIPODE=COMPLEMENT DIAMETER_PAIRS=30"<<'\n';
    cout<<"BIPARTITE=YES SHORES=30,30 JOHNSON_DETOURS=420 MAX_EXCESS=1"<<'\n';
    cout<<"CERTIFICATE_PASS"<<'\n';
}
