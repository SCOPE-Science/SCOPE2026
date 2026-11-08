// Standalone exhaustive check in the generalized-Petersen representation.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <vector>
using namespace std;
int main() {
 constexpr int n=20; array<uint32_t,n> neighbor{};
 auto edge=[&](int a,int b){neighbor[a]|=1u<<b;neighbor[b]|=1u<<a;};
 for(int i=0;i<10;i++){
   edge(i,(i+1)%10); edge(i,10+i);edge(10+i,10+(i+3)%10);
 }
 for(int i=0;i<n;i++)assert(__builtin_popcount(neighbor[i])==3);
 vector<uint32_t> states;map<int,int> counts;
 for(uint32_t s=0;s<(1u<<n);s++){
   int k=__builtin_popcount(s); if(k>6) continue;
   bool independent=true;uint32_t covered=s;
   for(int v=0;v<n;v++) if((s>>v)&1){
      if(neighbor[v]&s){independent=false;break;}
      covered |=neighbor[v];
   }
   if(independent && covered==((1u<<n)-1)){
      counts[k]++;
      if(k==6)states.push_back(s);
   }
 }
 assert(counts.size()==1 && counts[6]==100);
 map<uint32_t,int> id;
 for(int i=0;i<(int)states.size();i++)id[states[i]]=i;
 vector<set<int>> adj(states.size());
 for(int i=0;i<(int)states.size();i++){
   uint32_t s=states[i];
   for(int x=0;x<n;x++) if((s>>x)&1) {
      for(int y=0;y<n;y++) if(((neighbor[x]>>y)&1) && !((s>>y)&1)) {
         uint32_t t=s^(1u<<x)^(1u<<y);
         auto it=id.find(t);if(it!=id.end())adj[i].insert(it->second);
      }
   }
 }
 map<int,int> deg;int e=0;
 for(int i=0;i<(int)states.size();i++){
   deg[adj[i].size()]++;e+=adj[i].size();
   for(int j:adj[i])assert(adj[j].count(i));
 }
 assert((e==240 && deg==map<int,int>({{0,10},{2,60},{4,30}})));
 vector<int> seen(states.size());map<int,int> sizeCount;
 for(int i=0;i<(int)states.size();i++)if(!seen[i]){
   vector<int> cc{i};seen[i]=1;
   for(size_t j=0;j<cc.size();j++){
      for(int y:adj[cc[j]])if(!seen[y]){seen[y]=1;cc.push_back(y);}
   }
   sizeCount[cc.size()]++;
   if(cc.size()==18){
     set<int> high,low;
     for(int v:cc)(adj[v].size()==4?high:low).insert(v);
     assert(high.size()==6 && low.size()==12);
     map<pair<int,int>,int> pairs;
     map<int,set<int>> base;
     for(int v:low){
        assert(adj[v].size()==2);
        auto it=adj[v].begin();int a=*it++, b=*it;
        assert(high.count(a) && high.count(b));
        if(a>b)swap(a,b);
        pairs[{a,b}]++;base[a].insert(b);base[b].insert(a);
     }
     assert(pairs.size()==6);
     for(auto [k,v]:pairs)assert(v==2);
     for(int v:high)assert(base[v].size()==2);
     set<int> vis;queue<int> q;q.push(*high.begin());vis.insert(*high.begin());
     while(!q.empty()){
        int x=q.front();q.pop();for(int y:base[x])if(!vis.count(y)){vis.insert(y);q.push(y);}
     }
     assert(vis.size()==6);
     for(int root:cc){
        vector<int> dist(states.size(),-1);queue<int> q;q.push(root);dist[root]=0;int mx=0,nvis=0;
        while(!q.empty()){
          int x=q.front();q.pop();nvis++;mx=max(mx,dist[x]);
          for(int y:adj[x])if(dist[y]==-1){dist[y]=dist[x]+1;q.push(y);}
        }
        assert(nvis==18 && mx==6);
     }
   }else assert(cc.size()==1);
 }
 assert((sizeCount==map<int,int>({{1,10},{18,5}})));
 // Every fixed-cardinality jump between maximal independent sets is an edge slide.
 int jumps=0;
 for(int i=0;i<(int)states.size();i++)for(int j=i+1;j<(int)states.size();j++){
   uint32_t x=states[i]^states[j];if(__builtin_popcount(x)!=2)continue;
   jumps++;
   assert(adj[i].count(j));
 }
 assert(jumps==120);
 cout<<"OK gp(10,3) min=6 states=100 edges=120 comps=10K1+5D(C6 doubled), jump=slide, ecc=6\n";
}
