// Direct enumeration of labeled words for the Wielandt automaton.
#include <cstdint>
#include <iostream>
#include <stdexcept>

int main() {
    for (unsigned n=2; n<=6; ++n) {
        unsigned L=n*n-3*n+3;
        std::uint64_t total=0;
        std::uint64_t expected=std::uint64_t(1) << ((n-2)*(n-3));
        for(std::uint64_t word=0; word<(std::uint64_t(1)<<L); ++word) {
            unsigned state_mask=(1u<<n)-1;
            bool matches=true;
            for(unsigned t=0;t<L;++t) {
                bool use_a = (word>>t)&1ull;
                if(t%(n-1)==0 && t/(n-1)<n-1 && !use_a) matches=false;
                for(unsigned j=0;j<n-2;++j)
                    if(t==1+j*n && use_a) matches=false;
                unsigned out=0;
                for(unsigned i=0;i<n;++i) {
                    if(!(state_mask&(1u<<i))) continue;
                    unsigned q=(i<n-1)?i+1:(use_a?1:0);
                    out|=1u<<q;
                }
                state_mask=out;
            }
            bool resets=(state_mask && !(state_mask&(state_mask-1)));
            if(resets!=matches) throw std::runtime_error("classification mismatch");
            if(resets)++total;
        }
        if(total!=expected) throw std::runtime_error("count mismatch");
        std::cout<<"n="<<n<<" length="<<L<<" reset words="<<total<<" OK\n";
    }
    std::cout<<"VERIFY_OK: exhaustive direct word enumeration\n";
}
