// Direct single-failure verification for redundant identifying codes on the
// incidence graph of PG(2,2). Uses a distinct linear-algebra model.
#include <array>
#include <cassert>
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;
constexpr int V=14;
constexpr int FULL=(1<<V)-1;
int main(){
    array<vector<int>,V> adj;
    auto parity=[](int x){return __builtin_popcount((unsigned)x)&1;};
    // Nonzero vectors and nonzero functionals of F_2^3;
    // a point-vector v lies on line-functional a when a dot v=0.
    for(int v=1;v<=7;v++) for(int a=1;a<=7;a++){
       if(!parity(v&a)){
          int p=v-1,l=7+a-1;
          adj[p].push_back(l);adj[l].push_back(p);
       }
    }
    for(int i=0;i<V;i++) assert(adj[i].size()==3);
    auto identifying=[&](int code){
       array<int,V> signatures{};
       for(int v=0;v<V;v++){
           int m=code&(1<<v);
           for(int w:adj[v]) if(code&(1<<w))m|=1<<w;
           if(m==0)return false;
           signatures[v]=m;
       }
       for(int i=0;i<V;i++) for(int j=0;j<i;j++)
           if(signatures[i]==signatures[j])return false;
       return true;
    };
    array<int,V+1> counts{};
    vector<int> valid;
    for(int c=0;c<=FULL;c++){
        bool ok=true;
        for(int v=0;v<V && ok;v++)if(c&(1<<v)){
            if(!identifying(c^(1<<v)))ok=false;
        }
        if(ok && c){counts[__builtin_popcount((unsigned)c)]++;valid.push_back(c);}
    }
    assert(counts[10]==98 && counts[11]==224 && counts[12]==91 && counts[13]==14 && counts[14]==1);
    for(int k=0;k<10;k++)assert(counts[k]==0);
    int minimum=0;
    for(int c:valid){
        bool min=true;
        for(int v=0;v<V;v++) if((c&(1<<v)) &&
             find(valid.begin(),valid.end(),c^(1<<v))!=valid.end()){
               min=false;break;
             }
        if(min){assert(__builtin_popcount((unsigned)c)==10);minimum++;}
    }
    assert(minimum==98);
    cout<<"VERIFY_DIRECT_OK counts=98,224,91,14,1 minimal=98\n";
}
