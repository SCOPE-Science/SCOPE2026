// Direct, all-configuration verification of Rule 126 temporal returns.
// The output is a reproducibility check, not a replacement for the proof.
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <vector>
using namespace std;
uint32_t update(uint32_t x, int n) {
    uint32_t mask = (uint32_t(1)<<n)-1;
    uint32_t left = ((x<<1)&mask)|(x>>(n-1));
    uint32_t right = (x>>1)|((x&1u)<<(n-1));
    // Rule 126 outputs one iff neighborhood is neither 000 nor 111.
    return (left|x|right)&~(left&x&right)&mask;
}
vector<uint64_t> recurrence(int L, int hi){
    vector<uint64_t> f(hi+1,0), a(hi+1,0);
    f[0]=1;
    for(int n=1;n<=hi;n++){
        for(int j=-1;j<=1;j++){
            int k=L+j;
            int m=(j==0 ? 2:1);
            if(n>=k){f[n]+=m*f[n-k];a[n]+=uint64_t(k)*m*f[n-k];}
        }
    }
    return a;
}
int main(){
    auto t2=recurrence(5,24),t4=recurrence(11,24);
    cout << "n,F2_fixed,F4_fixed,primitive_two_orbits,primitive_four_orbits\n";
    for(int n=3;n<=20;n++){
        uint64_t a2=0,a4=0;
        uint32_t N=uint32_t(1)<<n;
        for(uint32_t x=0;x<N;x++){
            auto y=update(x,n);
            auto z=update(y,n);
            if(z==x)a2++;
            auto w=update(z,n);
            auto v=update(w,n);
            if(v==x)a4++;
        }
        if(a2!=1+t2[n] || a4!=1+t2[n]+2*t4[n]){
            cerr << "FAIL n="<<n<<" observed "<<a2<<","<<a4
                 <<" predicted "<<1+t2[n]<<","<<1+t2[n]+2*t4[n]<<"\n";
            return 1;
        }
        cout << n<<","<<a2<<","<<a4<<","<<t2[n]/2<<","<<t4[n]/2<<"\n";
    }
    cout << "PASS all configurations for n=3..20\n";
}
