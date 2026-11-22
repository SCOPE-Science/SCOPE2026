// Exact enumeration of locating-total dominating sets of C_3 square C_6.
// This implementation uses disjoint-set union rather than graph search.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <utility>
#include <vector>
using namespace std;
constexpr int V = 18, LIMIT = (1 << V);
struct DisjointSet {
  vector<int> p, sz;
  explicit DisjointSet(int n) : p(n), sz(n,1) { iota(p.begin(),p.end(),0); }
  int find(int a) { while(p[a]!=a) { p[a]=p[p[a]]; a=p[a]; } return a; }
  void join(int a,int b) { a=find(a); b=find(b); if(a==b)return;
    if(sz[a]<sz[b])swap(a,b); p[b]=a; sz[a]+=sz[b]; }
};
int main() {
  array<int,V> N{};
  auto index = [](int row, int col) { return 3*((col+6)%6)+((row+3)%3); };
  for(int row=0;row<3;++row)for(int col=0;col<6;++col) {
    int v=index(row,col);
    N[v]=(1<<index(row+1,col))|(1<<index(row-1,col))|
         (1<<index(row,col+1))|(1<<index(row,col-1));
  }
  vector<unsigned char> ok(LIMIT,0), pop(LIMIT,0);
  vector<int> by_size(V+1);
  for(int mask=0;mask<LIMIT;++mask) {
    pop[mask]=__builtin_popcount((unsigned)mask);
    int signatures[V];int sigcount=0;bool good=true;
    for(int v=0;v<V;++v) {
      int sig=N[v]&mask;
      if(!sig) {good=false;break;}
      if(!(mask&(1<<v))) {
        for(int j=0;j<sigcount;++j)if(signatures[j]==sig){good=false;break;}
        if(!good)break;
        signatures[sigcount++]=sig;
      }
    }
    if(good){ok[mask]=1;by_size[pop[mask]]++;}
  }
  cout<<"SIZE_POLYNOMIAL:";
  int total=0;
  for(int i=0;i<=V;++i)if(by_size[i]){cout<<" "<<i<<":"<<by_size[i];total+=by_size[i];}
  cout<<"\n";
  assert(total==103056 && by_size[6]==12);
  for(int budget=6;budget<=18;++budget){
    DisjointSet d(LIMIT);
    for(int mask=0;mask<LIMIT;++mask)if(ok[mask] && pop[mask]<=budget){
      for(int v=0;v<V;++v){
        int changed=mask^(1<<v);
        if(changed>mask && ok[changed] && pop[changed]<=budget)d.join(mask,changed);
      }
    }
    map<int,pair<int,int>> roots;
    for(int mask=0;mask<LIMIT;++mask)if(ok[mask] && pop[mask]<=budget){
      auto &entry=roots[d.find(mask)];entry.first++;
      if(pop[mask]==6)entry.second++;
    }
    map<pair<int,int>,int> profile;
    int sum=0;
    for(auto const&kv:roots){profile[kv.second]++;sum+=kv.second.first;}
    cout<<"BUDGET_"<<budget<<":";
    for(auto const&kv:profile)cout<<" ("<<kv.first.first<<","<<kv.first.second<<","<<kv.second<<")";
    cout<<" STATES:"<<sum<<"\n";
    if(budget==6)assert((profile==map<pair<int,int>,int>{{{1,1},12}}));
    if(budget==7)assert((profile==map<pair<int,int>,int>{{{1,0},216},{{13,1},12}}));
    if(budget==8)assert((profile==map<pair<int,int>,int>{{{1,0},2259},{{132,0},6},{{1257,6},2}}));
    if(budget==9)assert((profile==map<pair<int,int>,int>{{{1,0},60},{{22415,12},1}}));
    if(budget==10)assert((profile==map<pair<int,int>,int>{{{48620,12},1}}));
    if(budget>=11)assert((profile==map<pair<int,int>,int>{{{sum,12},1}}));
  }
  vector<int> minima;
  for(int m=0;m<LIMIT;++m) if(ok[m] && pop[m]==6) minima.push_back(m);
  assert(minima.size()==12);
  for(int start : minima) {
    vector<short> d(LIMIT,-1);
    queue<int> frontier;
    d[start]=0; frontier.push(start);
    int visited=1;
    while(!frontier.empty()) {
      int a=frontier.front(); frontier.pop();
      for(int v=0;v<V;++v){
        int b=a^(1<<v);
        if(ok[b] && pop[b]<=9 && d[b]==-1) {
          d[b]=d[a]+1;frontier.push(b);visited++;
        }
      }
    }
    assert(visited==22415);
    map<int,int> distcounts;
    for(int m : minima) {assert(d[m]>=0);distcounts[d[m]]++;}
    assert((distcounts==map<int,int>{{0,1},{4,3},{6,2},{12,6}}));
  }
  cout<<"MINIMUM_DISTANCE_PROFILE_BUDGET_9: 0:1 4:3 6:2 12:6\n";
  cout<<"PASS\n";
}
