// Self-contained finite verification for one-erasure power domination of the four-cube.
// Build: c++ -std=c++17 -O2 verify_direct.cpp -o verify_direct && ./verify_direct
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <queue>
#include <vector>
using namespace std;
int main(){
  constexpr int n=16, lim=1<<n, ALL=lim-1;
  int openN[n], closedN[n];
  for(int u=0;u<n;++u){
    openN[u]=0;
    for(int j=0;j<4;++j)openN[u]|=1<<(u^(1<<j));
    closedN[u]=openN[u]|(1<<u);
  }
  // This is a direct propagation simulation, independent of the distance-three criterion.
  vector<unsigned char> pd(lim,0), ft(lim,0);
  for(int s=1;s<lim;++s){
    int visited=0;
    for(int u=0;u<n;++u) if(s&(1<<u)) visited|=closedN[u];
    while(true){
      int next=visited;
      for(int u=0;u<n;++u){
        if(!(visited&(1<<u)))continue;
        int white=openN[u] & ~visited;
        if(white && !(white&(white-1)))next|=white;
      }
      if(next==visited)break;
      visited=next;
    }
    pd[s]=(visited==ALL);
  }
  array<int,17> pcount{},ftcount{};
  for(int s=1;s<lim;++s){
    int k=__builtin_popcount((unsigned)s);
    pcount[k]+=pd[s];
    bool good=true;
    for(int v=0;v<n;++v)if(s&(1<<v)) if(!pd[s^(1<<v)]){good=false;break;}
    if(good) {ft[s]=1;ftcount[k]++;}
  }
  assert(pcount[1]==0&&pcount[2]==32&&pcount[3]==352);
  const array<int,17> expected_ft = {0,0,0,0,376,3328,7832,11440,12870,11440,8008,4368,1820,560,120,16,1};
  assert(ftcount==expected_ft);
  vector<int> optimum;
  for(int s=0;s<lim;++s)if(ft[s]&&__builtin_popcount((unsigned)s)==4)optimum.push_back(s);
  assert(optimum.size()==376);
  int type[lim]={}; // 1=2K2, 2=P4, 3=C4
  array<int,4> typeCounts{};
  for(int s:optimum){
    int edges=0;
    for(int u=0;u<n;++u)if(s&(1<<u))for(int v=u+1;v<n;++v)
      if(s&(1<<v))if(__builtin_popcount((unsigned)(u^v))==3)++edges;
    assert(edges>=2&&edges<=4);
    type[s]=edges-1; typeCounts[type[s]]++;
  }
  assert(typeCounts[1]==160&&typeCounts[2]==192&&typeCounts[3]==24);
  vector<int> which(lim,-1);
  for(size_t i=0;i<optimum.size();++i)which[optimum[i]]=int(i);
  vector<vector<int>> graph(optimum.size());
  long long jumpEdges=0, slideEdges=0;
  for(size_t i=0;i<optimum.size();++i){
    int s=optimum[i];
    for(int u=0;u<n;++u)if(s&(1<<u))
      for(int v=0;v<n;++v)if(!(s&(1<<v))){
        int t=s^(1<<u)^(1<<v);
        int j=which[t];
        if(j>=0){
          graph[i].push_back(j);
          if((u^v) && !((u^v)&((u^v)-1)))++slideEdges;
        }
      }
    jumpEdges+=graph[i].size();
    int deg=graph[i].size();
    assert(deg==(type[s]==1?12:type[s]==2?14:16));
  }
  assert(jumpEdges==4992 && slideEdges==0);
  map<int,long long> distHist;
  array<int,7> eccHist{};
  for(int i=0;i<(int)optimum.size();++i){
    vector<int> dist(optimum.size(),-1);
    queue<int> q;
    q.push(i); dist[i]=0;
    while(!q.empty()){
      int u=q.front();q.pop();
      for(int v:graph[u]) if(dist[v]<0){dist[v]=dist[u]+1;q.push(v);}
    }
    int ecc=0;
    for(int j=0;j<(int)optimum.size();++j){
      assert(dist[j]>=0);
      ecc=max(ecc,dist[j]);
      if(i<j)distHist[dist[j]]++;
    }
    assert(ecc<=6);
    eccHist[ecc]++;
  }
  assert(eccHist[5]==328 && eccHist[6]==48);
  const map<int,long long> expected_dist = {{1,2496},{2,13536},{3,29520},{4,22992},{5,1932},{6,24}};
  assert(distHist==expected_dist);
  cout<<"DIRECT_VERIFIED Q4 1-fault optimum=4 count=376 types=160,192,24; jump_edges=2496 jump_diameter=6 slide_edges=0"<<endl;
}
