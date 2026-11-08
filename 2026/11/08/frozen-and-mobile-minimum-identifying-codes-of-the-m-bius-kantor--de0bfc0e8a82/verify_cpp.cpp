// Standalone direct exact test using 16-bit neighbourhood masks and graph BFS.
#include <array>
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <utility>
#include <vector>
using namespace std;
static const int N=16;
int main() {
    bool edge[N][N] = {};
    auto join=[&](int a,int b) {edge[a][b]=edge[b][a]=true;};
    for(int i=0;i<8;++i) {join(i,(i+1)%8);join(i,8+i);join(8+i,8+(i+3)%8);}
    array<uint32_t,N> closed{};
    for(int i=0;i<N;++i) {closed[i]=1u<<i; for(int j=0;j<N;++j) if(edge[i][j])closed[i]|=1u<<j;}
    vector<uint32_t> req;
    for(int i=0;i<N;++i) req.push_back(closed[i]);
    for(int i=0;i<N;++i) for(int j=i+1;j<N;++j)req.push_back(closed[i]^closed[j]);
    // A code hits each neighbourhood and each symmetric difference exactly when
    // all closed-neighbourhood signatures are nonempty and pairwise distinct.
    vector<int> ids;
    int countBySize[17]={};
    for(int mask=0;mask<(1<<N);++mask){
        bool good=true;
        for(uint32_t r:req) if(!(r & (uint32_t)mask)){good=false;break;}
        if(!good)continue;
        int k=__builtin_popcount((unsigned)mask);
        countBySize[k]++;
        if(k==8)ids.push_back(mask);
    }
    for(int k=0;k<8;++k)assert(countBySize[k]==0);
    assert(countBySize[8]==584);
    const int M=(int)ids.size();
    vector<vector<int>> graph[2];
    graph[0].resize(M);graph[1].resize(M);
    set<pair<int,int>> tedges[2];
    for(int i=0;i<M;++i) for(int j=i+1;j<M;++j) {
        int a=ids[i],b=ids[j],diff=a^b;
        if(__builtin_popcount((unsigned)diff)!=2)continue;
        if(__builtin_popcount((unsigned)(a&diff))!=1)continue;
        int x=__builtin_ctz((unsigned)(a&diff)),y=__builtin_ctz((unsigned)(b&diff));
        for(int g=0;g<2;++g){
            if(g==1 && !edge[x][y])continue;
            graph[g][i].push_back(j);graph[g][j].push_back(i);
            tedges[g].insert({a,b});
        }
    }
    assert(tedges[0].size()==2496 && tedges[1].size()==864);
    auto verify=[&](int g){
        map<int,int> degree,cs,ecc;
        vector<int> cid(M,-1);
        int nc=0;
        for(int i=0;i<M;++i){
            degree[(int)graph[g][i].size()]++;
            if(cid[i]>=0)continue;
            queue<int> q;q.push(i);cid[i]=nc;int size=0;
            while(!q.empty()){
                int u=q.front();q.pop();size++;
                for(int v:graph[g][u]) if(cid[v]<0){cid[v]=nc;q.push(v);}
            }
            cs[size]++;nc++;
        }
        for(int i=0;i<M;++i){
            vector<int>d(M,-1);queue<int>q;q.push(i);d[i]=0;
            while(!q.empty()){
                int u=q.front();q.pop();
                for(int v:graph[g][u]) if(d[v]<0) {d[v]=d[u]+1;q.push(v);}
            }
            int maxdist=0;for(int u=0;u<M;++u)if(d[u]>maxdist)maxdist=d[u];
            ecc[maxdist]++;
        }
        if(g==0){
            assert((cs==map<int,int>{{584,1}}));
            assert((degree==map<int,int>{{4,96},{6,48},{8,48},{9,192},{10,144},{12,48},{24,8}}));
            assert((ecc==map<int,int>{{7,240},{8,344}}));
        }else{
            assert((cs==map<int,int>{{1,96},{488,1}}));
            assert((degree==map<int,int>{{0,96},{2,240},{4,168},{6,48},{8,30},{24,2}}));
            assert((ecc==map<int,int>{{0,96},{8,104},{9,192},{10,192}}));
        }
    };
    verify(0);verify(1);
    map<int,int> frozenInternalEdges;
    for(int i=0;i<M;++i) if(graph[1][i].empty()) {
        int c=0;
        for(int a=0;a<N;++a)for(int b=a+1;b<N;++b)
            if(edge[a][b] && (ids[i]&(1<<a)) && (ids[i]&(1<<b)))++c;
        frozenInternalEdges[c]++;
    }
    assert((frozenInternalEdges==map<int,int>{{5,48},{7,48}}));
    // independently agree with certificate files produced by the Python checker
    auto compare_codes=[&](){ifstream file("codes.txt");assert(file);for(int x:ids){int a=-1;assert(file>>a && a==x);}int spare;assert(!(file>>spare));};
    auto compare_edges=[&](const string &name,int g){ifstream file(name);assert(file);set<pair<int,int>> xs;int a,b;while(file>>a>>b)xs.insert({a,b});assert(xs==tedges[g]);};
    compare_codes();compare_edges("jumps.txt",0);compare_edges("slides.txt",1);
    cout<<"CPP_VERIFY_OK exact enumeration, graph profiles, distance profiles and certificate concordance"<<'\n';
}
