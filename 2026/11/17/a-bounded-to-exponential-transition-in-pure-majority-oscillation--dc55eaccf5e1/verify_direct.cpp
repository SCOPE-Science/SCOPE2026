#include <cstdint>
#include <iostream>
#include <array>
#include <cassert>
using namespace std;
// Independent direct vertex-level simulation. A counted state must update to its bitwise complement.
uint64_t count_direct(int r, int n) {
    const int V=r*n;
    uint64_t total=0;
    for(uint64_t s=0; s<(1ULL<<V); ++s) {
        bool pass=true;
        for(int col=0; col<n && pass; ++col) {
            for(int row=0; row<r; ++row) {
                const int v=col*r+row;
                const int own=(s>>v)&1;
                int opponents=0;
                for(int j=0; j<r; ++j) if(j!=row) opponents += (((s>>(col*r+j))&1)!=own);
                opponents += (((s>>(((col+n-1)%n)*r+row))&1)!=own);
                opponents += (((s>>(((col+1)%n)*r+row))&1)!=own);
                if(2*opponents<=r+1) {pass=false;break;}
            }
        }
        if(pass)total++;
    }
    return total;
}
int main(){
 const uint64_t expect3[]={0,6,0,6,0};
 for(int n=3;n<=7;n++) {
    uint64_t z=count_direct(3,n); cout<<"K3 n="<<n<<" count="<<z<<"\n"; assert(z==expect3[n-3]);
 }
 const uint64_t expect4[]={90,98,270,1388};
 for(int n=3;n<=6;n++) {
    uint64_t z=count_direct(4,n); cout<<"K4 n="<<n<<" count="<<z<<"\n"; assert(z==expect4[n-3]);
 }
 cout<<"DIRECT_CHECKS_PASS\n";
}
