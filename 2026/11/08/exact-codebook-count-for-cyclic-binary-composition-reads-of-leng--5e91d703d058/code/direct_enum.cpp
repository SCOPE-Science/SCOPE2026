#include <array>
#include <unordered_set>
#include <iostream>
#include <cstdint>
#include <cassert>
using Sig=std::array<uint16_t,14>;
struct Hash {size_t operator()(const Sig& s) const noexcept {uint64_t h=1469598103934665603ULL;for(int x:s){h^=(unsigned)x+0x9e37;h*=1099511628211ULL;}return (size_t)h;}};
int main(){
 for(unsigned n=1;n<=20;++n){
   std::unordered_set<Sig,Hash> seen;
   for(uint32_t x=0;x<(1U<<n);++x){
      Sig sig{};
      for(unsigned i=0;i<n;++i){
         unsigned wt=0;
         for(unsigned k=1;k<=4;++k){
            wt+=((x>>((i+k-1)%n))&1U);
            unsigned offset=(k*(k+1))/2-1; // k1 offset0, k2 offset2, k3 offset5, k4 offset9
            ++sig[offset+wt];
         }
      }
      seen.insert(sig);
   }
   std::cout<<n<<' '<<seen.size()<<'\n';
 }
}
