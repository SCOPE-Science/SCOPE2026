// Independent exact functional-graph certification for two twelve-site quartic graphs.
// Compile: c++ -std=c++17 -O3 census_kahn_check.cpp -o check && ./check
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <cstdio>
#include <deque>
#include <map>
#include <vector>
using namespace std;
constexpr int NV=12, STATES=531441;
using Adj=array<array<int,4>,NV>;
using Matrix=array<array<bool,NV>,NV>;
Adj make_graph(int which){
 Matrix a{};
 if(which==0){
  vector<pair<int,int>> cube_edges;
  for(int u=0;u<8;u++)for(int v=u+1;v<8;v++)
   if(__builtin_popcount((unsigned)(u^v))==1)cube_edges.push_back({u,v});
  assert(cube_edges.size()==12);
  for(int i=0;i<12;i++)for(int j=i+1;j<12;j++){
   auto [u,v]=cube_edges[i];auto [w,z]=cube_edges[j];
   a[i][j]=a[j][i]=(u==w||u==z||v==w||v==z);
  }
 } else {
  for(int i=0;i<12;i++)for(int j=0;j<12;j++){
   int d=(j-i+12)%12;
   a[i][j]=(d==1||d==5||d==7||d==11);
  }
 }
 Adj g{};
 for(int i=0;i<12;i++){
  int deg=0;
  for(int j=0;j<12;j++)if(a[i][j]){assert(deg<4);g[i][deg++]=j;}
  assert(deg==4);
 }
 return g;
}
void process(int which){
 auto g=make_graph(which);
 array<int,NV> power{};power[0]=1;for(int i=1;i<NV;i++)power[i]=3*power[i-1];
 vector<int> succ(STATES),indeg(STATES,0);
 for(int s=0;s<STATES;s++){
  uint16_t excited=0,refract=0;
  int tmp=s;
  for(int i=0;i<NV;i++){
   int x=tmp%3;tmp/=3;
   if(x==1)excited|=(1u<<i);
   else if(x==2)refract|=(1u<<i);
  }
  int nxt=0;
  for(int i=0;i<NV;i++){
   int ni=0;
   if(excited>>i&1) ni=2;
   else if(!(refract>>i&1)){
    int near=0;for(int j:g[i])near+=(excited>>j)&1;
    ni=(near>=2);
   }
   nxt+=ni*power[i];
  }
  assert(0<=nxt&&nxt<STATES);
  succ[s]=nxt;indeg[nxt]++;
 }
 deque<int> q;vector<int> removed;removed.reserve(STATES);
 for(int i=0;i<STATES;i++)if(!indeg[i])q.push_back(i);
 while(!q.empty()){
  int s=q.front();q.pop_front();removed.push_back(s);
  int nxt=succ[s];if(--indeg[nxt]==0)q.push_back(nxt);
 }
 vector<int> period(STATES,0),depth(STATES,-1),orbit(STATES,-1);
 vector<int> osizes,oreps,ocnt;
 for(int s=0;s<STATES;s++)if(indeg[s] && period[s]==0){
  int p=0,v=s;do{p++;v=succ[v];assert(p<=STATES);}while(v!=s);
  int idx=osizes.size();osizes.push_back(p);ocnt.push_back(0);oreps.push_back(s);
  do{period[v]=p;depth[v]=0;orbit[v]=idx;ocnt[idx]++;v=succ[v];}while(v!=s);
 }
 for(auto i=removed.rbegin();i!=removed.rend();i++){
  int s=*i,nxt=succ[s];assert(depth[nxt]>=0);
  depth[s]=depth[nxt]+1;period[s]=period[nxt];orbit[s]=orbit[nxt];ocnt[orbit[s]]++;
 }
 map<pair<int,int>,int> joint,basins;map<int,int> ncycles;
 int mx=0,attainers=0;
 for(int s=0;s<STATES;s++){
  assert(depth[s]>=0&&period[s]>0&&orbit[s]>=0);
  joint[{depth[s],period[s]}]++;
  if(depth[s]>mx){mx=depth[s];attainers=1;}else if(depth[s]==mx)attainers++;
 }
 for(int i=0;i<(int)osizes.size();i++){
  basins[{osizes[i],ocnt[i]}]++;ncycles[osizes[i]]++;
 }
 printf("GRAPH %s / total %d / maxdepth %d / maxattainers %d\n",which?"circulant":"cubo",STATES,mx,attainers);
 printf("cycles");for(auto[k,v]:ncycles)printf(" p%d=%d",k,v);puts("");
 printf("joint");for(auto[k,v]:joint)printf(" (%d,%d)=%d",k.first,k.second,v);puts("");
 printf("basins");for(auto[k,v]:basins)printf(" (%d,%d)=%d",k.first,k.second,v);puts("");
 printf("reps");map<int,int> seen;for(int i=0;i<(int)osizes.size();i++)if(!seen[osizes[i]]++)printf(" p%d=%d",osizes[i],oreps[i]);puts("");
}
int main(){process(0);process(1);}
