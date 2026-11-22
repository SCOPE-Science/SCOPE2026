// Finite independent check using a Floyd-Warshall distance matrix and bitmask covering.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <vector>
using namespace std;
int main() {
    constexpr int N=14, FULL=(1<<N)-1;
    int d[N][N];
    for(int i=0;i<N;++i) for(int j=0;j<N;++j) d[i][j]=(i==j?0:100);
    vector<pair<int,int>> edges;
    for(int line=0;line<7;++line) for(int off: {0,1,3}) {
        int p=(line+off)%7, l=line+7;
        d[p][l]=d[l][p]=1; edges.push_back({p,l});
    }
    assert(edges.size()==21);
    for(int k=0;k<N;++k) for(int i=0;i<N;++i) for(int j=0;j<N;++j)
        d[i][j]=min(d[i][j],d[i][k]+d[k][j]);
    int diam=0;for(int i=0;i<N;++i) for(int j=0;j<N;++j) diam=max(diam,d[i][j]);assert(diam==3);
    int vertex_pair[N][N]{}; uint32_t edge_pair[N][N]{};
    for(int a=0;a<N;++a) for(int b=a+1;b<N;++b) {
        for(int v=0;v<N;++v) if(d[a][v]+d[v][b]==d[a][b]) vertex_pair[a][b]|=1<<v;
        for(int z=0;z<21;++z) {auto [u,v]=edges[z];
            if(d[a][u]+1+d[v][b]==d[a][b] || d[a][v]+1+d[u][b]==d[a][b])
                edge_pair[a][b]|=1u<<z;
        }
    }
    vector<bool> geo(1<<N),edgegeo(1<<N);
    map<int,int> count,mincount;
    for(int mask=0;mask<(1<<N);++mask){
        int vc=0;uint32_t ec=0;
        for(int a=0;a<N;++a)if(mask&(1<<a))for(int b=a+1;b<N;++b)if(mask&(1<<b)) {
            vc|=vertex_pair[a][b];ec|=edge_pair[a][b];
        }
        geo[mask]=vc==FULL;
        edgegeo[mask]=ec==((1u<<21)-1u);
        assert(geo[mask]==edgegeo[mask]);
        if(geo[mask])count[__builtin_popcount((unsigned)mask)]++;
    }
    int total=0;
    for(int mask=0;mask<(1<<N);++mask) if(edgegeo[mask]) {
        bool minimal=true;
        for(int v=0;v<N;++v) if(mask & (1<<v)) if(edgegeo[mask ^ (1<<v)])minimal=false;
        if(minimal){mincount[__builtin_popcount((unsigned)mask)]++;total++;}
    }
    assert(total==65);
    assert((count==map<int,int>{{4,21},{5,224},{6,931},{7,1962},{8,2394},{9,1862},{10,987},{11,364},{12,91},{13,14},{14,1}}));
    assert((mincount==map<int,int>{{4,21},{5,14},{6,28},{7,2}}));
    cout<<"PASS: independent all-subset vertex and edge geodetic tests agree on 16384 masks.\n";
    cout<<"PASS: counts:";for(auto[k,v]:count)cout<<" "<<k<<":"<<v;cout<<"\n";
    cout<<"PASS: minimal:";for(auto[k,v]:mincount)cout<<" "<<k<<":"<<v;cout<<"\n";
}
