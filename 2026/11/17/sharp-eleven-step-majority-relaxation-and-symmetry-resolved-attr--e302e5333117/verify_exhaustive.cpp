#include <cstdio>
#include <vector>
#include <array>
#include <cstdint>
#include <unordered_map>
#include <algorithm>
using namespace std;
constexpr int N=24; constexpr uint32_t SZ=1u<<N;
array<array<int,3>,N> g{};
uint32_t F(uint32_t x){uint32_t y=0;for(int i=0;i<N;i++){int c=((x>>g[i][0])&1)+((x>>g[i][1])&1)+((x>>g[i][2])&1);y |= uint32_t(c>=2)<<i;}return y;}
int main(){
 int shift[3]={-12,7,-7};
 for(int i=0;i<N;i++){g[i]={(i+23)%24,(i+1)%24,(i+shift[i%3]+24)%24};}
 for(int i=0;i<N;i++)for(int k:g[i]){int c=0;for(int j:g[k])if(j==i)c++;if(c!=1){fprintf(stderr,"BAD GRAPH %d %d\n",i,k);return 1;}}
 vector<uint32_t> next(SZ),rep(SZ,0xffffffffu);
 vector<uint8_t> status(SZ,0),entry(SZ,0),period(SZ,0);
 for(uint32_t x=0;x<SZ;x++)next[x]=F(x);
 uint64_t entry_fixed[100]={},entry_two[100]={},ncycles[3]={},states[3]={},basin_consensus[2]={};
 int maxD=0;vector<uint32_t> stack;
 unordered_map<uint32_t,uint32_t> cycle_sizes;
 for(uint32_t x=0;x<SZ;x++){
  if(status[x])continue;
  stack.clear();uint32_t v=x;
  while(status[v]==0){status[v]=1; stack.push_back(v);v=next[v];}
  if(status[v]==1){
   auto it=find(stack.begin(),stack.end(),v);
   if(it==stack.end()){fprintf(stderr,"FAIL visiting not in stack\n");return 1;}
   int len=stack.end()-it;
   if(len>2){fprintf(stderr,"FAIL period %d\n",len);return 1;}
   uint32_t repr=*min_element(it,stack.end());
   ncycles[len]++;
   for(auto jt=it;jt!=stack.end();jt++){status[*jt]=2;period[*jt]=len;rep[*jt]=repr;entry[*jt]=0;}
   stack.erase(it,stack.end());
  }
  while(!stack.empty()){
   uint32_t u=stack.back();stack.pop_back();uint32_t w=next[u];
   status[u]=2;period[u]=period[w];rep[u]=rep[w];entry[u]=entry[w]+1;
   if(entry[u]>maxD)maxD=entry[u];
  }
 }
 unordered_map<uint32_t,uint32_t> basin;
 for(uint32_t x=0;x<SZ;x++){
  int p=period[x],d=entry[x];if(d>=100){fprintf(stderr,"excess transient depth %d",d);return 1;}
  states[p]++;if(p==1)entry_fixed[d]++;else entry_two[d]++;
  basin[rep[x]]++;
  if(rep[x]==0)basin_consensus[0]++;
  if(rep[x]==SZ-1)basin_consensus[1]++;
 }
 printf("n=24 edges=36 vertices degree3 LCF=[-12,7,-7]^8\n");
 printf("periodic cycles fixed=%llu two=%llu; states fixed-basin=%llu two-basin=%llu\n",(unsigned long long)ncycles[1],(unsigned long long)ncycles[2],(unsigned long long)states[1],(unsigned long long)states[2]);
 printf("maximum first periodic entry=%d; consensus basins black=%llu white=%llu\n",maxD,(unsigned long long)basin_consensus[0],(unsigned long long)basin_consensus[1]);
 for(int d=0;d<=maxD;d++)printf("entry %d: fixed %llu, two %llu\n",d,(unsigned long long)entry_fixed[d],(unsigned long long)entry_two[d]);
 vector<uint32_t> b1,b2;
 for(auto [r,size]:basin){ if(period[r]==1)b1.push_back(size);else b2.push_back(size); }
 sort(b1.begin(),b1.end());sort(b2.begin(),b2.end());
 printf("basin size min/max fixed %u %u two %u %u\n",b1.front(),b1.back(),b2.front(),b2.back());
 printf("total basins %zu\n",basin.size());
 return 0;
}
