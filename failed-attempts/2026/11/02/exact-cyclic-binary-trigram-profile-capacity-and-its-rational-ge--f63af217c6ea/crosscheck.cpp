// Exhaustive independent cyclic trigram counter; C++17 standard library only.
#include <array>
#include <cstdint>
#include <iostream>
#include <unordered_set>
#include <vector>
#include <cassert>
using namespace std;

static uint64_t pack(unsigned n, uint32_t w) {
    unsigned cnt[8]={};
    for(unsigned i=0;i<n;++i) {
        unsigned k=(((w>>i)&1)<<2) |
                   (((w>>((i+1)%n))&1)<<1) |
                   ((w>>((i+2)%n))&1);
        ++cnt[k];
    }
    uint64_t key=0;
    for(unsigned j=0;j<8;++j)key|=(uint64_t)cnt[j]<<(5*j);
    return key;
}

static long formula(unsigned n) {
    long out=2+(n%2==0);
    for(unsigned b=1;b<=n;++b)
      for(unsigned d=1;d<=n;++d)
        for(unsigned c=(b>d?b-d:0);c<=n;++c) {
            int t=(int)n-(int)b-2*(int)c-3*(int)d;
            if(t>=0)out+=(t+1);
        }
    for(unsigned b=1;b<=n;++b)
      for(unsigned c=b;c<=n;++c)
        if(b+2*c<=n)++out;
    for(unsigned d=1;d<=n;++d)
      for(unsigned c=0;c<=n;++c)
        if(3*d+2*c<=n)++out;
    return out;
}
int main() {
    for(unsigned n=3;n<=21;++n) {
        unordered_set<uint64_t> seen;
        for(uint32_t w=0;w<(1u<<n);++w) seen.insert(pack(n,w));
        if((long)seen.size()!=formula(n)) {
            cerr << "Mismatch at "<<n<<"\n";return 1;
        }
    }
    cout << "CROSSCHECK_OK: all binary cyclic words length 3..21" << endl;
}
