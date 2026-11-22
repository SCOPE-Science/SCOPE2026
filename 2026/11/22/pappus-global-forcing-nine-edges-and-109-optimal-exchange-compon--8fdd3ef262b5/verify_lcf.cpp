// Independent verification using the Hamiltonian LCF presentation of the Pappus graph.
// Compile: c++ -O2 -std=c++17 verify_lcf.cpp -o verify_lcf
// Run: ./verify_lcf
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;
using U=uint32_t;
static vector<pair<int,int>> E;
static vector<vector<pair<int,int>>> incidence(18);
static vector<U> PM;
static void dfs(uint32_t occupied,U edge_mask){
    if(occupied==(1u<<18)-1){PM.push_back(edge_mask);return;}
    int v=0;while(occupied&(1u<<v))++v;
    for(auto [w,e]:incidence[v]) if(!(occupied&(1u<<w)))
        dfs(occupied|(1u<<v)|(1u<<w),edge_mask|(U(1)<<e));
}
static bool unique_signatures(U chosen){
    U signatures[42];int n=0;
    for(U M:PM){
        U s=M&chosen;
        for(int j=0;j<n;++j)if(signatures[j]==s)return false;
        signatures[n++]=s;
    }
    return n==42;
}
static void enum_k(int from,int need,U mask,vector<U>&found){
    if(!need){if(unique_signatures(mask))found.push_back(mask);return;}
    for(int e=from;e<=27-need;++e)enum_k(e+1,need-1,mask|(U(1)<<e),found);
}
int main(){
    set<pair<int,int>> edge_set;
    for(int v=0;v<18;++v){
        int w=(v+1)%18;edge_set.insert({min(v,w),max(v,w)});
    }
    int offsets[6]={5,7,-7,7,-7,-5};
    for(int v=0;v<18;++v){
        int w=(v+offsets[v%6]+18)%18;
        edge_set.insert({min(v,w),max(v,w)});
    }
    E.assign(edge_set.begin(),edge_set.end());
    assert(E.size()==27);
    for(int e=0;e<27;++e){auto [a,b]=E[e];incidence[a].push_back({b,e});incidence[b].push_back({a,e});}
    for(auto &nbr:incidence)assert(nbr.size()==3);
    dfs(0,0);sort(PM.begin(),PM.end());
    assert(PM.size()==42);assert(unique(PM.begin(),PM.end())==PM.end());
    vector<U> found;
    for(int k=1;k<=9;++k){
        found.clear();enum_k(0,k,0,found);
        if(k<9)assert(found.empty());
    }
    assert(found.size()==13608);
    unordered_map<U,int> idx;
    for(int i=0;i<(int)found.size();++i)idx.emplace(found[i],i);
    vector<vector<int>> neigh(found.size());
    for(int v=0;v<(int)found.size();++v){
        U s=found[v];
        for(int e=0;e<27;++e)if(s&(U(1)<<e))
            for(int f=0;f<27;++f)if(!(s&(U(1)<<f))){
                auto it=idx.find(s^(U(1)<<e)^(U(1)<<f));
                if(it!=idx.end())neigh[v].push_back(it->second);
            }
    }
    int total_degree=0;map<int,int> degrees;
    for(auto &a:neigh){total_degree+=a.size();degrees[a.size()]++;}
    assert(total_degree==208980);
    assert((degrees==map<int,int>{{4,972},{13,2916},{15,1944},{16,1944},{17,2916},{19,1944},{21,972}}));
    vector<int> compid(found.size(),-1);vector<vector<int>> cc;
    for(int v=0;v<(int)found.size();++v)if(compid[v]<0){
        int id=cc.size();vector<int> q{v};compid[v]=id;
        for(size_t k=0;k<q.size();++k)for(int w:neigh[q[k]])if(compid[w]<0){compid[w]=id;q.push_back(w);}
        cc.push_back(q);
    }
    map<int,int> component_hist;
    int giant=-1;
    for(int i=0;i<(int)cc.size();++i){component_hist[cc[i].size()]++;if(cc[i].size()==12636)giant=i;}
    assert((component_hist==map<int,int>{{9,108},{12636,1}}));
    assert(giant>=0);
    int bridges=0;
    for(int ci=0;ci<(int)cc.size();++ci)if(cc[ci].size()==9){
        // Check local nine-state geometry independently.
        for(int v:cc[ci]){
            assert(neigh[v].size()==4);
            for(int w:cc[ci])if(v!=w){
                int common=0;
                for(int a:neigh[v])for(int b:neigh[w])if(a==b)++common;
                bool adjacent=find(neigh[v].begin(),neigh[v].end(),w)!=neigh[v].end();
                assert(common==(adjacent?1:2));
            }
        }
        bool linked=false;
        for(int v:cc[ci]){
            U s=found[v];
            for(int a=0;a<27&&!linked;++a)if(s&(U(1)<<a))
            for(int b=a+1;b<27&&!linked;++b)if(s&(U(1)<<b))
            for(int c=0;c<27&&!linked;++c)if(!(s&(U(1)<<c)))
            for(int d=c+1;d<27;++d)if(!(s&(U(1)<<d))){
                U m=s^(U(1)<<a)^(U(1)<<b)^(U(1)<<c)^(U(1)<<d);
                auto it=idx.find(m);
                if(it!=idx.end()&&compid[it->second]==giant){linked=true;break;}
            }
            if(linked)break;
        }
        assert(linked);bridges++;
    }
    assert(bridges==108);
    cout<<"LCF 18 vertices 27 edges 42 perfect matchings\n";
    cout<<"minimum global forcing size 9, count 13608\n";
    cout<<"R1 edges 104490, components 108*9+1*12636\n";
    cout<<"small components SRG(9,4,1,2)\n";
    cout<<"R2 connected via 108 two-edge bridges\n";
}
