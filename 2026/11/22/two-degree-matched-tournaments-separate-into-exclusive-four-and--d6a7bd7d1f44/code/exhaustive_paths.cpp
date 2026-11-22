// Independently traverse each orbit using direct per-neighbor tests and memoized path recursion.
// C++17: g++ -O3 -std=c++17 exhaustive_paths.cpp -o exhaustive_paths
#include <array>
#include <cstdint>
#include <iostream>
#include <map>
#include <vector>
using namespace std;
constexpr int N=23,S=1<<N;
int main(){
 for(int mode=0;mode<2;mode++){
  int delta[11]{};int t=0;
  if(mode==0){bool used[N]{};for(int d=1;d<N;d++)used[(d*d)%N]=true;for(int d=1;d<N;d++)if(used[d])delta[t++]=d;}
  else for(int d=1;d<=11;d++)delta[t++]=d;
  if(t!=11)return 2;
  auto update=[&](uint32_t x){uint32_t y=0;for(int i=0;i<N;i++){int count=0;for(int j=0;j<11;j++) count+=(x>>((i+delta[j])%N))&1u;if(count>=6)y|=1u<<i;}return y;};
  vector<uint32_t> mark(S,UINT32_MAX);
  vector<uint8_t> period(S,0),depth(S,0);
  map<int,uint64_t> cycles,basin;map<pair<int,int>,uint64_t> profile;
  for(uint32_t x=0;x<S;x++){
   if(period[x])continue;
   vector<uint32_t> path;uint32_t y=x;
   while(!period[y] && mark[y]==UINT32_MAX){mark[y]=path.size();path.push_back(y);y=update(y);}
   if(!period[y]){
    uint32_t start=mark[y],length=path.size()-start;
    cycles[length]++;
    for(uint32_t j=start;j<path.size();j++){period[path[j]]=length;depth[path[j]]=0;}
    path.resize(start);
   }
   for(int j=int(path.size())-1;j>=0;j--){uint32_t z=path[j],next=update(z);period[z]=period[next];depth[z]=depth[next]+1;}
  }
  int maxDepth=0;for(uint32_t x=0;x<S;x++){profile[{depth[x],period[x]}]++;basin[period[x]]++;maxDepth=max(maxDepth,(int)depth[x]);}
  cout<<(mode==0?"PALEY23":"CAROUSEL23")<<" cycles";for(auto [p,v]:cycles)cout<<" "<<p<<":"<<v;
  cout<<" basin";for(auto [p,v]:basin)cout<<" "<<p<<":"<<v;
  cout<<" maximum_depth="<<maxDepth;
  cout<<" profile";for(auto [pr,v]:profile)cout<<" "<<pr.first<<","<<pr.second<<":"<<v;
  cout<<"\n";
 }
}
