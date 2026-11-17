// Independent direct enumeration of temporally returning Rule 54 states.
// Compile: c++ -O3 -std=c++17 direct_enumeration.cpp -o direct_enumeration
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <limits>
#include <stdexcept>

static inline uint32_t evolve(uint32_t x, int n) {
    uint32_t y = 0;
    for (int i = 0; i < n; ++i) {
        int l = (x >> ((i+n-1)%n)) & 1;
        int c = (x >> i) & 1;
        int r = (x >> ((i+1)%n)) & 1;
        y |= ((54U >> (4*l+2*c+r)) & 1U) << i;
    }
    return y;
}
int main(int argc, char **argv) {
    int maxn = argc > 1 ? std::atoi(argv[1]) : 20;
    if (maxn < 3 || maxn > 23) return 2;
    for (int n = 3; n <= maxn; ++n) {
        uint64_t fix1=0,fix2=0,fix3=0,fix4=0;
        const uint32_t sz=1U<<n;
        for (uint32_t x=0;x<sz;++x) {
            uint32_t x1=evolve(x,n), x2=evolve(x1,n), x3=evolve(x2,n), x4=evolve(x3,n);
            fix1+=(x1==x);fix2+=(x2==x);fix3+=(x3==x);fix4+=(x4==x);
        }
        if (fix1!=1 || fix3!=1 || fix2 != uint64_t(1+4*(n%4==0)) || (fix4-fix2)%4) return 3;
        std::cout << "n="<<n<<" fix1="<<fix1<<" fix2="<<fix2<<" fix3="<<fix3
                  <<" fix4="<<fix4<<" primitive_4_orbits="<<(fix4-fix2)/4<<"\n";
    }
    std::cout << "PASS: direct independent temporal-return enumeration\n";
}
