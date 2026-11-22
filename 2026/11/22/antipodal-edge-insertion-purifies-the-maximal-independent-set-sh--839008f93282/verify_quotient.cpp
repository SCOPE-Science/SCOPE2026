// Direct 5-bit quotient construction and exact enumeration; no external dependencies.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    // Representatives of antipodal 5-bit pairs are the words whose top bit is zero.
    // For representatives a,b in [0,15], quotient cube adjacency holds if
    // Hamming distance(a,b) is 1 or 4.
    array<uint32_t,16> folded{}, cube{};
    for (int a=0; a<16; ++a) for (int b=0; b<16; ++b) if (a != b) {
        int dist=__builtin_popcount(static_cast<unsigned>(a^b));
        if (dist==1) cube[a] |= 1u<<b;
        if (dist==1 || dist==4) folded[a] |= 1u<<b;
    }
    auto run = [](const array<uint32_t,16>& adj, bool isfolded) {
        vector<uint32_t> maximal;
        array<int,17> independent_counts{};
        for (uint32_t mask=0; mask<(1u<<16); ++mask) {
            bool independent=true, dominating=true;
            for (int x=0;x<16;++x) {
                if (mask&(1u<<x)) {if (mask&adj[x]) independent=false;}
                else if (!(mask&adj[x])) dominating=false;
            }
            if (independent) {
                int k=__builtin_popcount(mask);
                if (k < 17) ++independent_counts[k];
                else assert(false);
            }
            if (independent && dominating) maximal.push_back(mask);
        }
        vector<char> shattered(1u<<16,0);
        array<int,17> faces{}, facet_counts{}, mis_sizes{};
        for(uint32_t c:maximal) ++mis_sizes[__builtin_popcount(c)];
        for (uint32_t s=0;s<(1u<<16);++s) {
            int k=__builtin_popcount(s);
            if ((1u<<k)>maximal.size()) continue;
            vector<uint32_t> traces;
            for (uint32_t m:maximal) traces.push_back(m&s);
            sort(traces.begin(), traces.end());
            traces.erase(unique(traces.begin(),traces.end()),traces.end());
            if (traces.size() == (1u<<k)) {shattered[s]=1; ++faces[k];}
        }
        for (uint32_t s=0;s<(1u<<16);++s) if (shattered[s]) {
            bool facet=true;
            for(int x=0;x<16;++x) if(!(s&(1u<<x)) && shattered[s|(1u<<x)]) facet=false;
            if (facet) ++facet_counts[__builtin_popcount(s)];
        }
        if (isfolded) {
            assert(maximal.size()==56 && mis_sizes[4]==40 && mis_sizes[5]==16);
            assert((independent_counts==array<int,17>{1,16,80,160,120,16}));
            assert((faces==array<int,17>{1,16,80,160,120}));
            assert(facet_counts[4]==120);
            for(int k=0;k<17;++k) if(k!=4) assert(facet_counts[k]==0);
        } else {
            assert(maximal.size()==42 && mis_sizes[4]==24 && mis_sizes[5]==16 && mis_sizes[8]==2);
            assert((faces==array<int,17>{1,16,88,160,104}));
            assert(facet_counts[2]==8 && facet_counts[4]==104);
            for(int k=0;k<17;++k) if(k!=2 && k!=4) assert(facet_counts[k]==0);
        }
    };
    run(folded,true); run(cube,false);
    cout << "QUOTIENT_CLEBSCH_Q4_EXHAUSTIVE_PASS 65536_supports_per_graph\n";
}
