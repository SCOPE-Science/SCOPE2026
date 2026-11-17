// Independent exhaustive orbit checker using Floyd's algorithm.
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <string>
using namespace std;
constexpr int V=10, STATES=59049;
using State=array<int,V>;
using Graph=array<array<int,3>,V>;
Graph make_graph(int k){
    Graph g{};
    for(int i=0;i<5;i++){
        g[i]={ (i+4)%5, (i+1)%5, i+5 };
        g[5+i]={ i, 5+(i+5-k)%5, 5+(i+k)%5 };
    }
    return g;
}
State decode(int s){
    State x{};
    for(int i=0;i<V;i++){x[i]=s%3;s/=3;}
    assert(s==0);return x;
}
State evolve(const State &x,const Graph &g,bool cyclic){
    State y{};
    for(int i=0;i<V;i++){
        int c=x[i];
        if(cyclic){
            int target=(c+1)%3; bool seen=false;
            for(int j:g[i]) if(x[j]==target)seen=true;
            y[i]=seen?target:c;
        } else {
            if(c==0){bool seen=false;
                for(int j:g[i]) if(x[j]==1)seen=true;
                y[i]=seen?1:0;
            } else y[i]=(c+1)%3;
        }
    }
    return y;
}
pair<int,int> orbit(const State &x,const Graph &g,bool cyclic){
    State slow=evolve(x,g,cyclic);
    State fast=evolve(evolve(x,g,cyclic),g,cyclic);
    while(slow!=fast){
        slow=evolve(slow,g,cyclic);
        fast=evolve(evolve(fast,g,cyclic),g,cyclic);
    }
    int pre=0;
    slow=x;
    while(slow!=fast){slow=evolve(slow,g,cyclic);fast=evolve(fast,g,cyclic);pre++;}
    int period=1;
    fast=evolve(slow,g,cyclic);
    while(slow!=fast){fast=evolve(fast,g,cyclic);period++;}
    return {pre,period};
}
int main(){
    for(int k=1;k<=2;k++){
        Graph g=make_graph(k);
        for(int i=0;i<V;i++){
            for(int j:g[i]){
                assert(i!=j && j>=0 && j<V);
                assert(find(g[j].begin(),g[j].end(),i)!=g[j].end());
            }
        }
        map<pair<int,int>,int> ct;
        int maxC=0,maxG=0,different=0;
        for(int s=0;s<STATES;s++){
            auto x=decode(s);
            auto [etC,pC]=orbit(x,g,true);
            auto [etG,pG]=orbit(x,g,false);
            ct[{pC,pG}]++;
            maxC=max(maxC,etC);maxG=max(maxG,etG);
            if(pC!=pG){
                different++;
                assert(k==2 && pC==8 && pG==4);
            }
            if(k==2 && s==421){
                assert(etC==0 && pC==8 && etG==2 && pG==4);
            }
        }
        cout<<"GP(5,"<<k<<") pairs:";
        for(auto [ab,n]:ct) cout<<" "<<ab.first<<"/"<<ab.second<<"="<<n;
        cout<<"; mismatch="<<different<<"; max_CCA_entry="<<maxC<<"; max_GHM_entry="<<maxG<<"\n";
        int sum=0;for(auto [pair,n]:ct)sum+=n;assert(sum==STATES);
    }
}
