// Exhaustive finite binary dynamics on two canonically defined oriented 23-vertex tournaments.
// C++17: g++ -O3 -std=c++17 -mpopcnt exhaustive_peel.cpp -o exhaustive_peel
#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <map>
#include <vector>
using namespace std;
static constexpr int N=23, STATES=1<<23;
array<uint32_t,N> adjacency(bool paley){
 array<uint32_t,N> a{};
 for(int i=0;i<N;i++)for(int d=1;d<N;d++){
  bool edge=false;
  if(paley){for(int j=1;j<N;j++)if((j*j)%N==d){edge=true;break;}}
  else edge=(d<=11);
  if(edge)a[i]|=(uint32_t(1)<<((i+d)%N));
 }
 return a;
}
int main(){
 for(int mode=0;mode<2;mode++){
  bool paley=(mode==0);auto a=adjacency(paley);
  vector<uint32_t> nxt(STATES);
  vector<uint8_t> indeg(STATES,0),period(STATES,0),depth(STATES,0),visited(STATES,0);
  for(uint32_t x=0;x<STATES;x++){
   uint32_t y=0;for(int i=0;i<N;i++)if(__builtin_popcount(x&a[i])>=6)y|=(uint32_t(1)<<i);
   nxt[x]=y;
  }
  // Indegrees may exceed 255, so calculate in 32-bit storage.
  vector<uint32_t> incoming(STATES,0);for(uint32_t x=0;x<STATES;x++)incoming[nxt[x]]++;
  vector<uint32_t> peeled;peeled.reserve(STATES);
  for(uint32_t x=0;x<STATES;x++)if(incoming[x]==0)peeled.push_back(x);
  for(size_t t=0;t<peeled.size();t++)if(--incoming[nxt[peeled[t]]]==0)peeled.push_back(nxt[peeled[t]]);
  map<int,uint64_t> cycles,basin;map<int,uint32_t> cycleWitness;
  for(uint32_t x=0;x<STATES;x++)if(incoming[x]&&!visited[x]){
   uint32_t y=x;int p=0;
   do{visited[y]=1;p++;y=nxt[y];}while(y!=x);
   y=x;do{period[y]=p;y=nxt[y];}while(y!=x);
   cycles[p]++;if(!cycleWitness.count(p))cycleWitness[p]=x;
  }
  for(int j=int(peeled.size())-1;j>=0;j--){uint32_t x=peeled[j];period[x]=period[nxt[x]];depth[x]=depth[nxt[x]]+1;}
  map<pair<int,int>,uint64_t> profile;
  int maxdepth=0;uint32_t depthWitness=0;
  for(uint32_t x=0;x<STATES;x++){
   profile[{depth[x],period[x]}]++;basin[period[x]]++;
   if(depth[x]>maxdepth){maxdepth=depth[x];depthWitness=x;}
  }
  cout<<(paley?"PALEY23":"CAROUSEL23")<<" cycles";
  for(auto [p,c]:cycles)cout<<" "<<p<<":"<<c;
  cout<<" basin";for(auto [p,c]:basin)cout<<" "<<p<<":"<<c;
  cout<<" maximum_depth="<<maxdepth<<" witness="<<depthWitness;
  cout<<" periodic_witness";for(auto [p,x]:cycleWitness)cout<<" "<<p<<":"<<x;
  cout<<" profile";for(auto [pr,c]:profile)cout<<" "<<pr.first<<","<<pr.second<<":"<<c;
  cout<<"\n";
 }
}
