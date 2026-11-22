// Exact standard C++17 checker for the maximal-independent-set shattering
// complex of the Hamming graph K_3 square K_3 square K_3.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <unordered_set>
#include <vector>
using namespace std;
using U = uint32_t;
static const U ALL = (U(1)<<27)-1;
U adjacent[27]{};
vector<U> independent_sets, concepts;

// Every independent set occurs once, by choosing vertices in ascending order.
void enumerate(U chosen, U available) {
    independent_sets.push_back(chosen);
    while (available) {
        int v = __builtin_ctz(available);
        available &= available-1;
        enumerate(chosen | (U(1)<<v), available & ~adjacent[v]);
    }
}

bool shattered(U support) {
    int k = __builtin_popcount(support);
    if (k >= 9) return false;  // 390 concepts < 2^9 traces.
    uint64_t seen[4]{};
    int distinct = 0;
    for (U concept : concepts) {
        unsigned trace = 0, bit = 0;
        U remaining = support;
        while (remaining) {
            unsigned v = __builtin_ctz(remaining);
            remaining &= remaining - 1;
            trace |= ((concept >> v) & 1u) << bit++;
        }
        uint64_t flag = uint64_t(1) << (trace%64);
        if (!(seen[trace/64] & flag)) {
            seen[trace/64] |= flag;
            if (++distinct == (1<<k)) return true;
        }
    }
    return false;
}

int main() {
    for (int i=0;i<27;++i) for(int j=0;j<27;++j) if(i!=j) {
        int d=0;
        for(int t=1;t<=9;t*=3) d += ((i/t)%3 != (j/t)%3);
        if (d==1) adjacent[i] |= U(1)<<j;
    }
    enumerate(0, ALL);
    assert(independent_sets.size()==11776);
    int concept_sizes[28]{};
    for (U s : independent_sets) {
        U dominated=s;
        for (U t=s; t; t &= t-1) dominated |= adjacent[__builtin_ctz(t)];
        if (dominated==ALL) {
            concepts.push_back(s);
            ++concept_sizes[__builtin_popcount(s)];
        }
    }
    assert(concepts.size()==390);
    assert(concept_sizes[5]==54 && concept_sizes[7]==324 && concept_sizes[9]==12);
    int independent_counts[28]{}, coefficients[28]{}, facet_counts[28]{};
    unordered_set<U> good;
    for (U s : independent_sets) {
        ++independent_counts[__builtin_popcount(s)];
        if (shattered(s)) {
            ++coefficients[__builtin_popcount(s)];
            good.insert(s);
        }
    }
    for (U s : good) {
        bool facet=true;
        for(int v=0;v<27;++v) if(!(s & (U(1)<<v))) {
            if (good.count(s | (U(1)<<v))) {facet=false;break;}
        }
        if (facet) ++facet_counts[__builtin_popcount(s)];
    }
    const array<int,10> want_ind={1,27,270,1278,3078,3834,2412,756,108,12};
    const array<int,10> want_shattered={1,27,270,1278,2862,2322,0,0,0,0};
    for(int k=0;k<10;++k) {
        assert(independent_counts[k]==want_ind[k]);
        assert(coefficients[k]==want_shattered[k]);
    }
    assert(facet_counts[3]==36 && facet_counts[5]==2322);
    for(int k=0;k<28;++k) if(k!=3 && k!=5)assert(facet_counts[k]==0);
    cout << "TERNARY_HAMMING_MIS_CPP_PASS\n";
    cout << "independent=11776 concepts=390\n";
    cout << "shattering=1,27,270,1278,2862,2322\n";
    cout << "facets: 36 size-three and 2322 size-five\n";
}
