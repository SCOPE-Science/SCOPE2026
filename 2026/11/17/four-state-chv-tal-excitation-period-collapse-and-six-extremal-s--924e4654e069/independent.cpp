#include <array>
#include <cstdint>
#include <cstdio>
#include <vector>
#include <map>
#include <cassert>
using namespace std;
constexpr uint32_t N=1u<<24;
constexpr int E[24][2]={{0,1},{0,4},{0,6},{0,9},{1,2},{1,5},{1,7},{2,3},{2,6},{2,8},{3,4},{3,7},{3,9},{4,5},{4,8},{5,10},{5,11},{6,10},{6,11},{7,8},{7,11},{8,10},{9,10},{9,11}};
static array<array<uint8_t,4>,12> adj{};
uint32_t transition(uint32_t state){
 array<uint8_t,12> x{};
 for(int j=0;j<12;j++){x[j]=state%4;state/=4;}
 uint32_t out=0,place=1;
 for(int j=0;j<12;j++){
    int y;
    if(x[j]) y=(x[j]+1)%4;
    else y=(x[adj[j][0]]==1||x[adj[j][1]]==1||x[adj[j][2]]==1||x[adj[j][3]]==1)?1:0;
    out+=place*y;place*=4;
 }
 return out;
}
int main(){
 int deg[12]={};
 for(auto &e:E){adj[e[0]][deg[e[0]]++]=e[1];adj[e[1]][deg[e[1]]++]=e[0];}
 for(int d:deg)assert(d==4);
 vector<uint8_t> status(N,0),period(N,0),depth(N,0);
 vector<uint32_t> trace;
 uint64_t cycles=0;
 for(uint32_t start=0;start<N;start++){
  if(status[start])continue;
  trace.clear();
  uint32_t x=start;
  while(!status[x]){status[x]=1;trace.push_back(x);x=transition(x);}
  size_t first=trace.size();
  if(status[x]==1){
   while(first>0 && trace[first-1]!=x)first--;
   assert(first>0);
   first--;
   uint8_t p=(uint8_t)(trace.size()-first);
   cycles++;
   for(size_t j=first;j<trace.size();j++){
    status[trace[j]]=2;period[trace[j]]=p;depth[trace[j]]=0;
   }
   trace.resize(first);
  }
  for(size_t j=trace.size();j>0;j--){
    auto y=trace[j-1];auto z=transition(y);
    assert(status[z]==2);
    status[y]=2;period[y]=period[z];depth[y]=depth[z]+1;
  }
 }
 map<pair<int,int>,uint64_t> counts;map<int,uint64_t> per,dep;
 uint64_t maxcount=0;int maxd=0;
 for(uint32_t i=0;i<N;i++){
    assert(status[i]==2);assert(period[i]);
    counts[{depth[i],period[i]}]++;
    per[period[i]]++;dep[depth[i]]++;
    if(depth[i]>maxd){maxd=depth[i];maxcount=1;}
    else if(depth[i]==maxd)maxcount++;
 }
 printf("graph=Chvatal vertices=12 edges=24 q=4 threshold=1 total=%u\n",N);
 printf("cycle_orbits");for(auto [d,c]:counts) if(d.first==0) printf(" %d:%llu",d.second,(unsigned long long)(c/d.second)); puts("");
 printf("max_first_entry=%d count=%llu\n",maxd,(unsigned long long)maxcount);
 printf("period_basin");for(auto [p,c]:per)printf(" %d:%llu",p,(unsigned long long)c);puts("");
 printf("depth_census");for(auto [d,c]:dep)printf(" %d:%llu",d,(unsigned long long)c);puts("");
 printf("joint_census");for(auto [dp,c]:counts)printf(" (%d,%d):%llu",dp.first,dp.second,(unsigned long long)c);puts("");
 uint64_t recurring=0;for(auto [dp,c]:counts)if(dp.first==0)recurring+=c;
 printf("sum=%u recurrent=%llu joint_classes=%zu\n",N,(unsigned long long)recurring,counts.size());
}
