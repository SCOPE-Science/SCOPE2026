// Independent complete functional-graph census for a canonical 12-vertex graph.
#include <array>
#include <algorithm>
#include <iostream>
#include <map>
#include <queue>
#include <stdexcept>
#include <tuple>
#include <vector>
using namespace std;
constexpr int N=12, S=1<<N;
using Edge=pair<int,int>;
using Counts=array<int,5>;
const vector<Edge> edges={{0,1},{0,4},{0,6},{0,9},{1,2},{1,5},{1,7},
{2,3},{2,6},{2,8},{3,4},{3,7},{3,9},{4,5},{4,8},{5,10},
{5,11},{6,10},{6,11},{7,8},{7,11},{8,10},{9,10},{9,11}};
const map<Edge,Counts> expected={
    {{0,1},{118,82,11,24,3164}},{{0,6},{130,106,8,2,3094}},
    {{2,3},{126,118,7,20,3032}},{{2,6},{106,78,7,8,2996}},
    {{2,8},{144,128,8,4,3080}}};
Counts spectrum(Edge removed){
    array<unsigned,N> mask{};
    array<int,N> degree{};
    for(auto [a,b]:edges){
        if(make_pair(a,b)==removed) continue;
        mask[a]|=1u<<b;mask[b]|=1u<<a;
        ++degree[a];++degree[b];
    }
    array<int,S> out{};
    array<int,S> indeg{};
    for(int x=0;x<S;++x){
        int y=0;
        for(int v=0;v<N;++v){
            int k=__builtin_popcount(static_cast<unsigned>(x)&mask[v]);
            if(2*k>degree[v] || (2*k==degree[v] && (x&(1<<v))))y|=1<<v;
        }
        out[x]=y; ++indeg[y];
    }
    queue<int> q;
    for(int i=0;i<S;++i)if(indeg[i]==0)q.push(i);
    vector<int> peel;
    while(!q.empty()){
        int x=q.front();q.pop();peel.push_back(x);
        if(--indeg[out[x]]==0)q.push(out[x]);
    }
    array<int,S> depth{},period{},terminal{};
    depth.fill(-1);
    for(int i=0;i<S;++i){
        if(indeg[i]>0 && depth[i]<0){
            vector<int> cyc;
            int x=i;
            do{cyc.push_back(x);x=out[x];}while(x!=i);
            int r=*min_element(cyc.begin(),cyc.end());
            for(int a:cyc){depth[a]=0;period[a]=static_cast<int>(cyc.size());terminal[a]=r;}
        }
    }
    for(auto it=peel.rbegin();it!=peel.rend();++it){
        int x=*it;
        if(depth[out[x]]<0)throw runtime_error("bad reversed peel");
        depth[x]=depth[out[x]]+1;
        period[x]=period[out[x]];
        terminal[x]=terminal[out[x]];
    }
    int fixed=0,twophases=0,maxdepth=0,nummax=0,consensus=0;
    map<pair<int,int>,int> histogram;
    for(int x=0;x<S;++x){
        if(depth[x]<0 || period[x]<1 || period[x]>2)throw runtime_error("invalid period");
        ++histogram[{depth[x],period[x]}];
        if(depth[x]==0 && period[x]==1)++fixed;
        if(depth[x]==0 && period[x]==2)++twophases;
        if(depth[x]>maxdepth){maxdepth=depth[x];nummax=0;}
        if(depth[x]==maxdepth)++nummax;
        if(terminal[x]==0 || terminal[x]==S-1)++consensus;
    }
    if(twophases%2)throw runtime_error("odd phase count");
    if(terminal[0]!=0||terminal[S-1]!=S-1)throw runtime_error("unanimity not fixed");
    int total=0;
    for(const auto& [key,c]:histogram)total+=c;
    if(total!=S)throw runtime_error("partial census");
    return {fixed,twophases/2,maxdepth,nummax,consensus};
}
int main(){
    Counts base=spectrum({-1,-1});
    if(base!=Counts{234,136,7,32,2906})return 1;
    cout<<"baseline: " ;for(int a:base)cout<<a<<' ';cout<<'\n';
    map<Counts,int> freq;
    for(Edge edge:edges){
        Counts got=spectrum(edge);
        if(got[4]<=base[4])return 2;
        ++freq[got];
        cout<<"deleted "<<edge.first<<' '<<edge.second<<": ";
        for(int x:got)cout<<x<<' ';cout<<'\n';
    }
    if(freq.size()!=5)return 3;
    for(auto [edge,c]:expected){
        int m=edge==Edge{0,6}?8:4;
        if(freq[c]!=m) return 4;
    }
    cout<<"PASS 25 finite functional graphs, full 4096-state census each\n";
}
