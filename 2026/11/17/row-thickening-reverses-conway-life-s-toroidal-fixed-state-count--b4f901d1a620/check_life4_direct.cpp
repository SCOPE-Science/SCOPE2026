// Exhaustive independent implementation for 4 by n tori (n = 3..6).
#include <iostream>
#include <cstdint>
#include <array>
using namespace std;
int main(){
 for(int n=3;n<=6;++n){
  int sites=4*n;
  array<uint32_t,24> neighborhood{};
  for(int c=0;c<n;c++)for(int r=0;r<4;r++){
   int i=4*c+r; uint32_t mask=0;
   for(int dc=-1;dc<=1;dc++)for(int dr=-1;dr<=1;dr++) if(dc||dr){
    int j=4*((c+dc+n)%n)+(r+dr+4)%4;
    mask|=1u<<j;
   }
   neighborhood[i]=mask;
   if(__builtin_popcount(mask)!=8){cerr<<"bad neighbors";return 1;}
  }
  uint64_t count=0;
  for(uint32_t x=0;x<(1u<<sites);++x){
   bool stable=true;
   for(int i=0;i<sites;++i){
    int s=__builtin_popcount(x&neighborhood[i]);
    bool next=(s==3)||((x>>i&1u)&&s==2);
    if(next!=bool(x>>i&1u)){stable=false;break;}
   }
   count+=stable;
  }
  cout<<"n="<<n<<" fixed="<<count<<" total="<<(1u<<sites)<<"\n";
 }
}
