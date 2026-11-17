#include <bits/stdc++.h>
using namespace std;
uint64_t count3(int n){
 const int N=3*n; vector<uint32_t> mask(N,0);
 for(int c=0;c<n;c++)for(int r=0;r<3;r++){
   int i=3*c+r;
   for(int dc=-1;dc<=1;dc++)for(int dr=-1;dr<=1;dr++){
    if(dc==0&&dr==0)continue;
    int j=3*((c+dc+n)%n)+((r+dr+3)%3);
    mask[i]|=(uint32_t(1)<<j);
   }
   assert(__builtin_popcount(mask[i])==8);
 }
 uint64_t total=1;for(int i=0;i<N;i++)total*=3;
 uint64_t matches=0;
 for(uint64_t s=0;s<total;s++){
  uint64_t z=s;uint32_t fire=0,ref=0;
  for(int i=0;i<N;i++){
   int v=z%3;z/=3;
   if(v==1)fire|=uint32_t(1)<<i;
   if(v==2)ref|=uint32_t(1)<<i;
  }
  uint32_t u=fire,v=ref;
  for(int k=0;k<3;k++){
   uint32_t newfire=0;
   uint32_t inactive=~(u|v);
   for(int i=0;i<N;i++)if((inactive>>i)&1U){
    if(__builtin_popcount(u&mask[i])==2)
      newfire|=(uint32_t(1)<<i);
   }
   v=u;u=newfire;
  }
  if(u==fire&&v==ref)matches++;
 }
 return matches;
}
int main(){for(int n=3;n<=5;n++){cout<<n<<" "<<count3(n)<<"\n";}}
