#include <cstdint>
#include <cstdio>
#include <vector>
#include <map>
#include <chrono>
#include <climits>
#include <cstdlib>
using namespace std;
constexpr uint32_t HALF=1u<<14, ALL=1u<<28;
static uint16_t movehalf[HALF*128];
static uint8_t excited[HALF], adjacency[2][128];
static void setup(){
 for(uint32_t v=0;v<HALF;++v){
  for(int k=0;k<7;k++)if(((v>>(2*k))&3)==1)excited[v]|=uint8_t(1u<<k);
  for(int mask=0;mask<128;mask++){
   uint32_t y=0;
   for(int k=0;k<7;k++){
    int a=(v>>(2*k))&3;
    y|=uint32_t(a==0 ? ((mask>>k)&1) : ((a+1)&3))<<(2*k);
   }
   movehalf[(v<<7)|mask]=(uint16_t)y;
  }
 }
 // Direct graph adjacency incidence, row=points, columns=lines, j=i+d mod 7 for d=0,1,3.
 uint8_t neighbor[14]{};
 for(int i=0;i<7;i++)for(int d: {0,1,3}){
  int j=(i+d)%7;
  neighbor[i]|=1u<<j;
  neighbor[7+j]|=1u<<i;
 }
 for(int mask=0;mask<128;mask++)for(int i=0;i<7;i++){
  if(neighbor[i]&mask)adjacency[0][mask]|=1u<<i;
  if(neighbor[i+7]&mask)adjacency[1][mask]|=1u<<i;
 }
}
static inline uint32_t evolve(uint32_t x){
 uint32_t a=x&(HALF-1),b=x>>14;
 return (uint32_t)movehalf[(a<<7)|adjacency[0][excited[b]]] |
     ((uint32_t)movehalf[(b<<7)|adjacency[1][excited[a]]]<<14);
}
int main(){setup();
 vector<uint16_t> in_degree(ALL,0);
 for(uint32_t x=0;x<ALL;x++){
  uint32_t y=evolve(x);
  if(in_degree[y]==65535){printf("degree overflow\n");return 8;}
  in_degree[y]++;
 }
 vector<uint32_t> removed;removed.reserve(ALL);
 for(uint32_t x=0;x<ALL;x++)if(!in_degree[x])removed.push_back(x);
 for(size_t i=0;i<removed.size();i++){
  uint32_t y=evolve(removed[i]);
  if(--in_degree[y]==0)removed.push_back(y);
 }
 // in_degree>0 now is precisely union of directed cycles.
 vector<uint8_t> entry(ALL,255),period(ALL,0);
 map<pair<int,int>,uint64_t> count;
 uint64_t ncore=0, ncycles=0;
 for(uint32_t x=0;x<ALL;x++)if(in_degree[x] && period[x]==0){
  uint32_t y=x;int p=0;
  do {p++;y=evolve(y);}while(y!=x);
  if(p>=255){printf("period overflow\n");return 9;}
  y=x;do {entry[y]=0;period[y]=(uint8_t)p;count[{0,p}]++;ncore++;y=evolve(y);}while(y!=x);
  ncycles++;
 }
 for(size_t i=removed.size();i-->0;){
  uint32_t x=removed[i],y=evolve(x);
  if(entry[y]==255 || entry[y]==254){printf("entry overflow\n");return 10;}
  entry[x]=entry[y]+1;period[x]=period[y];count[{entry[x],period[x]}]++;
 }
 printf("Heawood four-state threshold-one GH indegree-culling\n");
 printf("states %u removed %zu recurrent_states %llu cycles %llu\n",ALL,removed.size(),(unsigned long long)ncore,(unsigned long long)ncycles);
 int max_d=0;map<int,uint64_t> totals;
 for(auto [k,c]:count){totals[k.second]+=c;if(k.first>max_d)max_d=k.first;}
 printf("max_depth %d\n",max_d);
 for(auto [p,c]:totals)printf("period %d count %llu\n",p,(unsigned long long)c);
 for(auto [key,c]:count)if(key.first==0)printf("recurrent period %d count %llu orbit_count %llu\n",key.second,(unsigned long long)c,(unsigned long long)(c/key.second));
 for(auto [key,c]:count)if(key.first==max_d)printf("longest period %d count %llu\n",key.second,(unsigned long long)c);
 for(auto [key,c]:count)printf("COUNT,%d,%d,%llu\n",key.first,key.second,(unsigned long long)c);

}
