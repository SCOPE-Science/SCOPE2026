// Complete incidence enumeration of nine-point nontrivial blocking sets in PG(2,5).
// Compile: c++ -O2 -std=c++17 verify_nine_point_blockers.cpp -o nine_blockers
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <set>
#include <vector>
using V = std::array<int, 3>;
int m5(int x) { x %= 5; return x < 0 ? x + 5 : x; }
V canonical(V v) {
    int k = 0;
    while (v[k] == 0) ++k;
    int a = 1;
    while (m5(a * v[k]) != 1) ++a;
    for (int &x : v) x = m5(a * x);
    return v;
}
int main() {
    std::set<V> all;
    for (int x=0; x<5; ++x) for (int y=0; y<5; ++y)
        all.insert(canonical({x,y,1}));
    for (int x=0; x<5; ++x) all.insert(canonical({x,1,0}));
    all.insert({1,0,0});
    std::vector<V> pts(all.begin(), all.end());
    assert(pts.size() == 31);
    std::set<uint32_t> line_set;
    for (auto a : pts) {
        uint32_t mask = 0;
        for (int i=0; i<31; ++i)
            if (m5(a[0]*pts[i][0]+a[1]*pts[i][1]+a[2]*pts[i][2]) == 0)
                mask |= uint32_t(1) << i;
        assert(__builtin_popcount(mask) == 6);
        line_set.insert(mask);
    }
    assert(line_set.size() == 31);
    std::vector<uint32_t> lines(line_set.begin(),line_set.end());
    uint32_t triangle = 0;
    for (int t : {0,1,4})
        for (V p : std::vector<V>{{0,1,-t},{1,-t,0},{-t,0,1}}) {
            p = canonical(p);
            const auto it = all.find(p);
            assert(it != all.end());
            int i = int(std::distance(all.begin(), it));
            triangle |= uint32_t(1)<<i;
        }
    assert(__builtin_popcount(triangle) == 9);
    for (uint32_t line:lines) {
        int n=__builtin_popcount(line & triangle);
        assert(1 <= n && n <= 4);
    }
    uint64_t visited=0, blocking=0, nontrivial=0, trivial=0;
    uint64_t s=(uint64_t(1)<<9)-1;
    const uint64_t limit=uint64_t(1)<<31;
    // Gosper's successor exhausts all 31-choose-9 subsets, once each.
    while (s<limit) {
        ++visited;
        bool meets=true;
        for (uint32_t line : lines) if (!(s & line)) { meets=false; break; }
        if (meets) {
            ++blocking;
            bool contains_line=false;
            for (uint32_t line : lines) if ((s&line)==line) {
                contains_line=true;
                break;
            }
            if (contains_line) ++trivial;
            else ++nontrivial;
        }
        const uint64_t bit=s&(~s+1), next=s+bit;
        s=(((next^s)>>2)/bit)|next;
    }
    assert(visited==20160075ULL && blocking==86800 &&
           nontrivial==15500 && trivial==71300);
    std::cout<<"NINE_POINT_BLOCKING_CENSUS_PASS "<<visited<<' '<<blocking
             <<' '<<nontrivial<<' '<<trivial<<' '<<__builtin_popcount(triangle)<<'\n';
}
