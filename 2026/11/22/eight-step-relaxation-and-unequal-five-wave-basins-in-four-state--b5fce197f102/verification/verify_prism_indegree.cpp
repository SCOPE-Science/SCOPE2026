// Complete exact four-state Greenberg--Hastings census on the pentagonal prism.
// No random sampling; every four-ary ten-vertex assignment is processed.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <queue>
#include <vector>
using namespace std;
constexpr uint32_t STATES=1u<<20;
int main(){
 array<array<int,3>,10> adj{};
 array<int,10> d{};
 for(int r=0;r<2;r++)for(int i=0;i<5;i++){
  int a=r*5+i,b=r*5+(i+1)%5;
  adj[a][d[a]++]=b; adj[b][d[b]++]=a;
 }
 for(int i=0;i<5;i++){
  adj[i][d[i]++]=i+5;adj[i+5][d[i+5]++]=i;
 }
 for(int i=0;i<10;i++)assert(d[i]==3);
 vector<uint32_t> next(STATES);
 vector<uint32_t> indegree(STATES,0);
 for(uint32_t x=0;x<STATES;x++){
  uint32_t y=0;
  for(int v=0;v<10;v++){
   int c=(x>>(2*v))&3;
   int z;
   if(c==0){z=0;for(int j=0;j<3;j++)if(((x>>(2*adj[v][j]))&3)==1)z=1;}
   else z=(c+1)&3;
   y|=uint32_t(z)<<(2*v);
  }
  next[x]=y;
  indegree[y]++;
 }
 vector<uint32_t> deletion;
 deletion.reserve(STATES);
 queue<uint32_t> q;
 for(uint32_t x=0;x<STATES;x++)if(indegree[x]==0)q.push(x);
 while(!q.empty()){
  uint32_t a=q.front();q.pop();deletion.push_back(a);
  uint32_t b=next[a];if(--indegree[b]==0)q.push(b);
 }
 vector<uint16_t> t(STATES,65535),p(STATES,0);
 map<int,uint64_t> primitive;
 for(uint32_t x=0;x<STATES;x++)if(indegree[x] && p[x]==0){
  uint32_t y=next[x];int len=1;
  while(y!=x){assert(len<=20);len++;y=next[y];}
  y=x;do{p[y]=len;t[y]=0;y=next[y];}while(y!=x);
  primitive[len]++;
 }
 for(auto it=deletion.rbegin();it!=deletion.rend();++it){
  uint32_t a=*it,b=next[a];assert(t[b]!=65535);t[a]=t[b]+1;p[a]=p[b];
 }
 map<pair<int,int>,uint64_t> histogram;
 map<int,uint64_t> basins;
 int max_t=0;
 for(uint32_t x=0;x<STATES;x++){
  assert(t[x]!=65535);assert(p[x]==1||p[x]==4||p[x]==5);
  histogram[{t[x],p[x]}]++;basins[p[x]]++;max_t=max(max_t,int(t[x]));
 }
 assert((primitive==map<int,uint64_t>{{1,1},{4,530},{5,6}}));
 assert(max_t==8);
 assert(basins[1]==436846 && basins[4]==579750 && basins[5]==31980);
 assert(histogram[make_pair(8,5)]==20);
 // Independently confirm the sharp global return identity, not just cycle data.
 uint64_t nonzero_seven=0;
 for(uint32_t x=0;x<STATES;x++){
  uint32_t a=x;
  for(int i=0;i<7;i++)a=next[a];
  uint32_t at7=a;
  a=next[a];uint32_t at8=a;
  for(int i=9;i<=27;i++)a=next[a];
  if(a!=at7)nonzero_seven++;
  a=next[a];assert(a==at8);
 }
 assert(nonzero_seven>0);
 cout<<"graph=GP(5,1) n=10 states="<<STATES<<" primitive_orbits";
 for(auto [k,v]:primitive)cout<<" "<<k<<":"<<v;
 cout<<"\nsharp_max_entry="<<max_t<<"\n";
 for(auto [k,v]:basins)cout<<"basin_period="<<k<<" count="<<v<<"\n";
 for(auto [k,v]:histogram)cout<<"census "<<k.first<<" "<<k.second<<" "<<v<<"\n";
 cout<<"F^28=F^8 for all states; F^27 differs from F^7 on "<<nonzero_seven<<" states\n";
 cout<<"PASS: exhaustive indegree-pruning classification\n";
}
