// Direct independently constructed synchronous update, on indexed cyclic prisms.
// Compile: g++ -O3 -std=c++17 direct_check.cpp -o direct_check && ./direct_check
#include <cstdint>
#include <iostream>
#include <vector>
#include <cassert>
using namespace std;
static uint64_t update(uint64_t x,int n){
    uint64_t y=0;
    for(int j=0;j<n;j++) for(int r=0;r<2;r++){
        int v=2*j+r;
        int a=(x>>(2*v))&3;
        int c;
        if(a>0)c=(a+1)&3;
        else {
            int L=(x>>(2*(2*((j+n-1)%n)+r)))&3;
            int R=(x>>(2*(2*((j+1)%n)+r)))&3;
            int V=(x>>(2*(2*j+1-r)))&3;
            c=(L==1||R==1||V==1)?1:0;
        }
        y|=uint64_t(c)<<(2*v);
    }
    return y;
}
int main(){
    // 4-state alphabet, total 4^(2n)=16^n states.
    const uint64_t expected[]={0,0,0,120,264,2120,7160};
    for(int n=3;n<=5;n++){
        uint64_t c=0;
        uint64_t total=uint64_t(1)<<(4*n);
        for(uint64_t s=0;s<total;s++){
            uint64_t z=s;
            for(int t=0;t<4;t++)z=update(z,n);
            if(z==s && s!=0){
                assert(update(s,n)!=s);
                c++;
            }
        }
        assert(c==expected[n]);
        cout << "n=" <<n<<" checked="<<total<<" period_four="<<c<<"\n";
    }
    cout << "Direct full-state comparison PASS\n";
}
