#include <cstdint>
#include <iostream>
using namespace std;
// Standard simultaneous cubic majority on GP(n,k), k=1 or 2.
// Lower n bits index the outer ring; upper n bits index the inner ring.
uint32_t step(uint32_t x, int n, int k) {
  uint32_t y=0;
  for(int i=0;i<n;i++) {
    int a=(i+n-1)%n, b=(i+1)%n;
    int o=((x>>a)&1)+((x>>b)&1)+((x>>(n+i))&1);
    if(o>=2) y|=(1u<<i);
    int c=(i+n-k)%n,d=(i+k)%n;
    int v=((x>>(n+c))&1)+((x>>(n+d))&1)+((x>>i)&1);
    if(v>=2) y|=(1u<<(n+i));
  }
  return y;
}
int main(){
  for(int n=5;n<=11;n++){
    for(int k=1;k<=2;k++){
      uint64_t fixed=0,two=0;
      uint32_t maxstates=(1u<<(2*n));
      for(uint32_t x=0;x<maxstates;x++){
        uint32_t y=step(x,n,k);
        if(y==x) fixed++;
        if(step(y,n,k)==x) two++;
      }
      cout<<n<<" "<<k<<" "<<fixed<<" "<<two<<" "<<(two-fixed)/2<<"\n";
    }
  }
}
