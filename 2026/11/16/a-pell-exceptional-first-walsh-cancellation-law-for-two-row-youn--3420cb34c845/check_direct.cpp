// Exact direct Walsh enumeration for Ferrers ideals in two-row rectangles.
// Build: c++ -O2 -std=c++17 check_direct.cpp -o check_direct
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <limits>
#include <vector>
using namespace std;
int main() {
    const long long expected_zero[] = {0,0,6,18,0,0,789,2807,0,0,137820};
    for (int n=1;n<=10;++n) {
        int N=1<<(2*n);
        vector<int> a(N,0);
        for(int top=0;top<=n;++top) for(int bottom=0;bottom<=top;++bottom){
            int mask=((1<<top)-1) | (((1<<bottom)-1)<<n);
            ++a[mask];
        }
        for (int step=1;step<N;step<<=1)
            for (int base=0;base<N;base+=2*step)
                for(int i=0;i<step;++i){
                    int u=a[base+i],v=a[base+i+step];
                    a[base+i]=u+v;
                    a[base+i+step]=u-v;
                }
        long long sq=0; int zero=0,gap=numeric_limits<int>::max(),first=100;
        for(int k=0;k<N;++k){
            int v=a[k]; sq+=1LL*v*v;
            if(v==0){++zero;first=min(first,__builtin_popcount((unsigned)k));}
            else gap=min(gap,abs(v));
        }
        long long count=1LL*(n+1)*(n+2)/2;
        assert(sq==count*N);
        assert(zero==expected_zero[n]);
        assert(gap==((n%4==2 || n%4==3)?2:1));
        assert(first==((n%4==0 || n%4==1)?100:((n==2)?1:2)));
        cout<<"n="<<n<<" zeros="<<zero<<" gap="<<gap<<" first="<<(first==100?-1:first)<<"\n";
    }
    cout<<"PASS: independent complete Walsh transforms and Parseval\n";
}
