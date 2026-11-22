// Direct finite-state verification of the three-state excitation rule on triangular graphs.
#include <array>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <utility>

int main(int argc, char**argv){
 if(argc!=2)return 2;
 const int n=std::atoi(argv[1]);
 if(n<3||n>6)return 2;
 const int m=n*(n-1)/2, threshold=n-2;
 std::vector<std::pair<int,int>> edges;
 for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)edges.emplace_back(i,j);
 std::vector<uint32_t> adj(m,0);
 for(int e=0;e<m;e++)for(int f=0;f<m;f++)if(e!=f){
  const auto [a,b]=edges[e];const auto [c,d]=edges[f];
  if(a==c||a==d||b==c||b==d)adj[e]|=(uint32_t(1)<<f);
 }
 int count=1;for(int e=0;e<m;e++)count*=3;
 const uint32_t mask=(uint32_t(1)<<m)-1;
 std::array<uint64_t,6> hist{};
 int maxdelay=0,example=-1;
 for(int s=0;s<count;s++){
  int tmp=s;uint32_t excite=0,refractory=0;
  for(int e=0;e<m;e++){
   int r=tmp%3;tmp/=3;
   if(r==1)excite|=(uint32_t(1)<<e);
   if(r==2)refractory|=(uint32_t(1)<<e);
  }
  int hit=-1;
  for(int t=0;t<=5;t++){
   if((excite|refractory)==0){hit=t;break;}
   if(t==5)break;
   uint32_t rest=mask&~(excite|refractory),next=0;
   for(int e=0;e<m;e++)if((rest>>e)&1u){
    if(__builtin_popcount(adj[e]&excite)>=threshold)next|=(uint32_t(1)<<e);
   }
   refractory=excite;excite=next;
  }
  if(hit<0){std::printf("NOT_EXTINCT_WITHIN_5 n=%d state=%d\n",n,s);return 1;}
  hist[hit]++;
  if(hit>maxdelay){maxdelay=hit;example=s;}
 }
 std::printf("n=%d states=%d threshold=%d max=%d witness_base3=%d hist=",n,count,threshold,maxdelay,example);
 for(int i=0;i<=5;i++)std::printf("%s%llu",i?",":"",(unsigned long long)hist[i]);
 std::printf("\n");
}
