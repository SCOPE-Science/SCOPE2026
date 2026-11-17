// Direct exhaustive enumeration of labelled Langton-ant torus states.
// The independent update implements turn, flip, move, without using column invariants.
// Usage: c++ -std=c++17 -O2 direct_census.cpp -o direct_census && ./direct_census
#include <cstdint>
#include <cstdio>
#include <map>
#include <vector>
#include <cassert>
using namespace std;
using u64=uint64_t;
int main() {
 for(int n=2;n<=9;n++){
  int sites=2*n;
  u64 states=(1ULL<<sites)*(u64)sites*4;
  vector<unsigned char> visited(states,0);
  map<u64,u64> observed, predicted;
  auto next=[&](u64 s)->u64 {
   int d=s%4; s/=4;int p=s%sites; u64 colors=s/sites;
   bool black=(colors>>p)&1ULL;
   d=(d+(black?3:1))%4; // 0=N,1=E,2=S,3=W
   colors^=1ULL<<p;
   int x=p%n, y=p/n;
   if(d==0||d==2)y^=1;
   else if(d==1)x=(x+1)%n;
   else x=(x+n-1)%n;
   return (colors*sites+(u64)(y*n+x))*4+d;
  };
  for(u64 s=0;s<states;s++)if(!visited[s]){
   u64 cur=s, len=0;
   do {
    if(visited[cur]){fputs("Non-bijective cycle closure\n",stderr);return 1;}
    visited[cur]=1;
    cur=next(cur);
    len++;
   } while(cur!=s);
   observed[len]++;
  }
  for(int j=1;j<n;j++)predicted[8*j]+=(u64)n*(1ULL<<(2*n-j-1));
  predicted[4*n]+=(u64)(n+1)*(1ULL<<(n+1));
  if(observed!=predicted){fprintf(stderr,"Mismatch at n=%d\n",n);return 1;}
  u64 sum=0;
  for(auto [period,count]:observed)sum+=period*count;
  if(sum!=states){fputs("State total mismatch\n",stderr);return 1;}
  printf("n=%d full_states=%llu",n,(unsigned long long)states);
  for(auto [period,count]:observed)
   printf(" period%llu=%llu",(unsigned long long)period,(unsigned long long)count);
  puts(" PASS");
 }
}
