#include <array>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <unordered_map>
#include <vector>
using Row = std::array<std::uint64_t,16>;
static std::uint32_t key(int mask, int a, int b) {
    return (std::uint32_t(mask)<<8)|(std::uint32_t(a)<<4)|std::uint32_t(b);
}
static Row compute(int second) {
    constexpr int n=15, all=(1<<n)-1;
    std::unordered_map<std::uint32_t,Row> states, next;
    Row seed{};
    seed[0]=1;
    states[key(1|(1<<(second-1)),1,second)] = seed;
    for (int depth=2;depth<n;++depth) {
        next.clear();
        for (const auto &kv:states) {
            int mask=int(kv.first>>8),a=int((kv.first>>4)&15),b=int(kv.first&15);
            int rem=all^mask;
            while(rem) {
                int bit=rem&-rem;
                rem-=bit;
                int c=__builtin_ctz(static_cast<unsigned>(bit))+1;
                Row &dest=next[key(mask|bit,b,c)];
                int shift=((a^b)==c);
                for (int j=0;j<16-shift;++j) dest[j+shift]+=kv.second[j];
            }
        }
        states.swap(next);
    }
    Row result{};
    for (const auto &kv:states) {
        int a=int((kv.first>>4)&15),b=int(kv.first&15);
        int shift=((a^b)==1)+((b^1)==second);
        for(int j=0;j<16-shift;++j)result[j+shift]+=kv.second[j];
    }
    return result;
}
int main() {
    Row expected{1642251264ULL,2567162880ULL,1512023040ULL,
      434319360ULL,65617920ULL,5492736ULL,153600ULL};
    for (int second: {2,3}) {
        Row got=compute(second);
        if(got!=expected) {std::cerr<<"MISMATCH\n";return 1;}
        if(std::accumulate(got.begin(),got.end(),std::uint64_t(0))!=6227020800ULL)
            return 2;
    }
    std::cout<<"FORWARD_VERIFY_OK";
    for(auto value:expected)std::cout<<" "<<value/96;
    std::cout<<"\n";
}
