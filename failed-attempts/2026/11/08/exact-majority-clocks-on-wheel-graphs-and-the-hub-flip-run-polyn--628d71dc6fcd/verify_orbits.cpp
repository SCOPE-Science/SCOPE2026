#include <cassert>
#include <cstdint>
#include <iostream>
// Direct synchronous graph-rule enumeration; rim vertices 0..n-1, hub n.
static uint32_t advance(uint32_t state, unsigned n) {
  uint32_t output = 0;
  for (unsigned i = 0; i < n; ++i) {
    unsigned left = (state >> ((i+n-1)%n))&1u;
    unsigned right = (state >> ((i+1)%n))&1u;
    unsigned hub = (state >> n)&1u;
    if (left+right+hub>=2) output |= (1u<<i);
  }
  unsigned pop=__builtin_popcount(state & ((1u<<n)-1u));
  unsigned hub=(state>>n)&1u;
  if (2*pop>n || (2*pop==n && hub)) output|=(1u<<n);
  return output;
}
int main(){
  for(unsigned n=3;n<=19;++n){
    uint64_t fixed=0,pure2=0,hubflip=0,hubfixed=0;
    for(uint32_t state=0;state<(1u<<(n+1));++state){
      uint32_t next=advance(state,n);
      if(next==state){++fixed;continue;}
      if(advance(next,n)==state){
        ++pure2;
        if(((state^next)>>n)&1u)++hubflip;
        else ++hubfixed;
      }
    }
    assert(fixed==2);
    assert(hubfixed==(n%2==0?4:0));
    assert(hubflip%2==0);
    std::cout<<n<<" "<<fixed<<" "<<pure2<<" "<<hubflip/2<<" "<<hubfixed/2<<"\n";
  }
}
