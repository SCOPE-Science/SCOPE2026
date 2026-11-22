// Exact enumeration of finite tournament one-point-extension rank three.
// Build: c++ -std=c++17 -O2 -Wall -Wextra verify.cpp -o verify
// Run: ./verify
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <cstdio>
#include <map>
#include <utility>
#include <vector>

using std::array;
using std::map;
using std::pair;
using std::uint32_t;
using std::uint64_t;
using std::vector;

// Edge index e follows the lexicographic list (i,j), 0<=i<j<n.
// Bit e=1 means i->j; bit e=0 means j->i.
static bool rank_at_least_three(int n, uint32_t bits) {
    uint32_t out[7] = {0};
    int e = 0;
    for (int i=0; i<n; ++i)
        for (int j=i+1; j<n; ++j, ++e)
            if ((bits>>e)&1u) out[i] |= 1u<<j;
            else out[j] |= 1u<<i;
    // This is precisely the three-round one-point-extension recursion:
    // an anchor a must have an outgoing and an incoming candidate b,
    // each admitting all four two-point extension types.
    for (int a=0; a<n; ++a) {
        bool out_good=false, in_good=false;
        for (int b=0; b<n; ++b) if (a!=b) {
            unsigned types=0;
            for (int w=0; w<n; ++w) if (w!=a && w!=b) {
                unsigned t=(((out[w]>>a)&1u)<<1)|((out[w]>>b)&1u);
                types|=1u<<t;
            }
            if (types==15u) {
                if ((out[a]>>b)&1u) out_good=true;
                else in_good=true;
                if (out_good && in_good) return true;
            }
        }
    }
    return false;
}

struct Permutation {
    array<uint8_t,21> source_index, reverse;
};

int main() {
    // Exhaustive labelled test at every smaller order and at order seven.
    const uint32_t expected[8]={0,0,0,0,0,0,0,1503216};
    uint32_t first_witness=0;
    for (int n=1; n<=7; ++n) {
        uint32_t hits=0;
        uint32_t total=1u<<(n*(n-1)/2);
        for (uint32_t x=0; x<total; ++x) {
            if (rank_at_least_three(n,x)) {
                ++hits;
                if (n==7 && !first_witness) first_witness=x;
            }
        }
        assert(hits==expected[n]);
        std::printf("order=%d labeled_rank_at_least_three=%u\n",n,hits);
    }
    assert(first_witness==17u);

    // Independently quotient all labelled seven-vertex masks by S_7.
    const int n=7;
    int index[n][n] = {{0}};
    int e=0;
    for (int i=0;i<n;++i) for (int j=i+1;j<n;++j)
        index[i][j]=index[j][i]=e++;
    vector<Permutation> perms;
    array<int,n> permutation={0,1,2,3,4,5,6};
    do {
        Permutation p{};
        int k=0;
        for (int i=0;i<n;++i)
            for (int j=i+1;j<n;++j,++k) {
                p.source_index[k]=index[permutation[i]][permutation[j]];
                p.reverse[k]=permutation[i]>permutation[j];
            }
        perms.push_back(p);
    } while (std::next_permutation(permutation.begin(), permutation.end()));
    assert(perms.size()==5040);

    vector<uint8_t> seen(1u<<21,0);
    map<pair<int,bool>,int> histogram;
    uint64_t labelled_good=0;
    int unlabelled_good=0, unlabelled_bad=0;
    uint64_t total_orbit_sizes=0;
    for (uint32_t x=0;x<(1u<<21);++x) if (!seen[x]) {
        const bool good=rank_at_least_three(7,x);
        vector<uint32_t> orbit;
        orbit.reserve(5040);
        for (const auto &p:perms) {
            uint32_t v=0;
            for (int k=0;k<21;++k)
                if (((x>>k)&1u)^p.reverse[k])
                    v |= 1u<<p.source_index[k];
            seen[v]=1;
            orbit.push_back(v);
        }
        std::sort(orbit.begin(),orbit.end());
        orbit.erase(std::unique(orbit.begin(),orbit.end()),orbit.end());
        const int orbit_size=static_cast<int>(orbit.size());
        assert(5040 % orbit_size==0);
        const int automorphism_order=5040/orbit_size;
        histogram[{automorphism_order,good}]++;
        total_orbit_sizes+=orbit_size;
        if (good) { ++unlabelled_good; labelled_good+=orbit_size; }
        else ++unlabelled_bad;
    }
    assert(total_orbit_sizes==(1u<<21));
    assert(unlabelled_good==313 && unlabelled_bad==143);
    assert(labelled_good==1503216);
    const map<pair<int,bool>,int> reference={
        {{1,false},107},{{1,true},292},
        {{3,false},30},{{3,true},17},
        {{5,false},2},{{5,true},2},
        {{7,true},1},{{9,false},4},{{21,true},1}
    };
    assert(histogram==reference);
    std::printf("unlabelled_total=%d unlabelled_rank_three=%d\n", unlabelled_good+unlabelled_bad,unlabelled_good);
    std::printf("labelled_rank_three=%llu\n",static_cast<unsigned long long>(labelled_good));
    for (const auto &[key,value]:histogram)
        std::printf("automorphism_order=%d rank_three=%d classes=%d\n",key.first,key.second,value);
    std::puts("ALL_CHECKS_OK");
}
