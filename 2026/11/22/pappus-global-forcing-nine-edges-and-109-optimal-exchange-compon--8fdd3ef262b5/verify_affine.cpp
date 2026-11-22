// Exact finite enumeration for the Pappus incidence graph.
// Compile: c++ -O2 -std=c++17 verify_affine.cpp -o verify_affine
// Run: ./verify_affine
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;
using U = uint32_t;
static vector<pair<int,int>> edges;
static vector<U> matchings;
static int endpointIndex[9][9];
static void enumerate_matchings(int point, int used_lines, U mask){
    if(point==9){assert(used_lines==511);matchings.push_back(mask);return;}
    for(int line=0;line<9;++line){
        int e=endpointIndex[point][line];
        if(e>=0 && !(used_lines & (1<<line)))
            enumerate_matchings(point+1,used_lines|(1<<line),mask|(U(1)<<e));
    }
}
static bool forcing(U mask,const vector<U>&differences){
    for(U d:differences) if(!(mask&d))return false;
    return true;
}
static vector<U> all_optima;
static void combinations(int start,int chosen,int k,U mask,const vector<U>&diff){
    if(chosen==k){if(forcing(mask,diff))all_optima.push_back(mask);return;}
    int left=k-chosen;
    for(int e=start;e<=27-left;++e)
        combinations(e+1,chosen+1,k,mask|(U(1)<<e),diff);
}
struct DSU{
    vector<int> p,sz;
    DSU(int n):p(n),sz(n,1){iota(p.begin(),p.end(),0);}
    int find(int x){return p[x]==x?x:p[x]=find(p[x]);}
    void merge(int a,int b){a=find(a);b=find(b);if(a!=b){if(sz[a]<sz[b])swap(a,b);p[b]=a;sz[a]+=sz[b];}}
};
int main(){
    fill(&endpointIndex[0][0],&endpointIndex[0][0]+81,-1);
    for(int p=0;p<9;++p){
        int x=p/3,y=p%3;
        for(int family=0;family<3;++family){
            int c=family==0?x:(family==1?y:(y-x+3)%3);
            int line=3*family+c;
            int idx=edges.size();
            edges.emplace_back(p,9+line);
            endpointIndex[p][line]=idx;
        }
    }
    assert(edges.size()==27);
    enumerate_matchings(0,0,0);
    assert(matchings.size()==42);
    sort(matchings.begin(),matchings.end());
    assert(unique(matchings.begin(),matchings.end())==matchings.end());
    vector<U> differences;
    for(int i=0;i<42;++i) for(int j=i+1;j<42;++j)
        differences.push_back(matchings[i]^matchings[j]);
    assert(differences.size()==861);
    vector<int> counts(10);
    for(int k=1;k<=9;++k){
        all_optima.clear(); combinations(0,0,k,0,differences);
        counts[k]=all_optima.size();
        if(k<9)assert(all_optima.empty());
    }
    assert(all_optima.size()==13608);
    sort(all_optima.begin(),all_optima.end());
    unordered_map<U,int> index;
    for(int i=0;i<(int)all_optima.size();++i)index[all_optima[i]]=i;
    vector<vector<int>> adjacency(all_optima.size());
    DSU dsu(all_optima.size());
    long long exchange_edges=0;
    map<int,int> degree_distribution;
    for(int i=0;i<(int)all_optima.size();++i){
        U m=all_optima[i];
        for(int a=0;a<27;++a) if(m&(U(1)<<a))
            for(int b=0;b<27;++b) if(!(m&(U(1)<<b))){
                U n=m^(U(1)<<a)^(U(1)<<b);
                auto it=index.find(n);
                if(it!=index.end()){
                    adjacency[i].push_back(it->second);
                    if(i<it->second){++exchange_edges;dsu.merge(i,it->second);}
                }
            }
        degree_distribution[(int)adjacency[i].size()]++;
    }
    assert(exchange_edges==104490);
    map<int,vector<int>> comp;
    for(int i=0;i<(int)all_optima.size();++i)comp[dsu.find(i)].push_back(i);
    map<int,int> component_sizes;
    int giant_root=-1;
    for(auto &kv:comp){component_sizes[kv.second.size()]++;
        if(kv.second.size()==12636)giant_root=kv.first;
    }
    assert((component_sizes==map<int,int>{{9,108},{12636,1}}));
    assert(giant_root>=0);
    assert((degree_distribution==map<int,int>{{4,972},{13,2916},{15,1944},{16,1944},{17,2916},{19,1944},{21,972}}));
    // Every small component is the (9,4,1,2) strongly regular rook graph.
    for(auto &kv:comp){
        auto &C=kv.second;
        if(C.size()!=9)continue;
        for(int v:C){
            assert(adjacency[v].size()==4);
            unordered_set<int> Nv(adjacency[v].begin(),adjacency[v].end());
            for(int w:C)if(w!=v){
                int common=0;
                for(int z:adjacency[w]) if(Nv.count(z))++common;
                assert(common==(Nv.count(w)?1:2));
            }
        }
    }
    // Two simultaneous replacements connect each small island to the large one.
    int bridged=0;
    for(auto &kv:comp){
        if(kv.second.size()!=9)continue;
        bool found=false;
        for(int v:kv.second){
            U mask=all_optima[v];
            vector<int> one,zero;
            for(int e=0;e<27;++e)(mask&(U(1)<<e)?one:zero).push_back(e);
            for(int a=0;a<(int)one.size()&&!found;++a)
            for(int b=a+1;b<(int)one.size()&&!found;++b)
            for(int c=0;c<(int)zero.size()&&!found;++c)
            for(int d=c+1;d<(int)zero.size();++d){
                U m=mask^(U(1)<<one[a])^(U(1)<<one[b])^(U(1)<<zero[c])^(U(1)<<zero[d]);
                auto it=index.find(m);
                if(it!=index.end() && dsu.find(it->second)==giant_root){found=true;break;}
            }
            if(found)break;
        }
        assert(found);++bridged;
    }
    assert(bridged==108);
    cout<<"graph 18 vertices 27 edges; perfect matchings 42\n";
    cout<<"global forcing counts k=1..9:";
    for(int k=1;k<=9;++k)cout<<' '<<counts[k];
    cout<<"\nminimum 9; optimal subsets 13608\n";
    cout<<"one-edge-swap exchange edges "<<exchange_edges<<"\n";
    cout<<"components: 108 of order 9, 1 of order 12636\n";
    cout<<"each order-nine component SRG(9,4,1,2)\n";
    cout<<"all 108 smaller components bridge the giant by two-edge replacement\n";
    cout<<"two-edge-swap exchange graph connected; threshold 2\n";
}
