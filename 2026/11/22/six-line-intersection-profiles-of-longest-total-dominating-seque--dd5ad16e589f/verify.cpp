// C++17 forward recurrence for legal point-line covering sequences in PG(2,4).
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <set>
#include <vector>
using namespace std;

int multiply(int a, int b) {
    int p = 0;
    for (int i=0; i<2; ++i)
        for (int j=0; j<2; ++j)
            if ((a & (1<<i)) && (b & (1<<j))) p ^= 1<<(i+j);
    if (p & 8) p ^= 14;   // subtract x*(x^2+x+1) in characteristic 2
    if (p & 4) p ^= 7;    // subtract x^2+x+1
    return p;
}
int inverse(int a) {
    for (int b=1; b<4; ++b) if (multiply(a,b)==1) return b;
    assert(false); return 0;
}
int main() {
    set<array<int,3>> representatives;
    for (int a=0; a<4; ++a) for (int b=0; b<4; ++b)
      for (int c=0; c<4; ++c) {
        if (!(a|b|c)) continue;
        array<int,3> u={a,b,c};
        int s=inverse(a?a:(b?b:c));
        for (int &v:u) v=multiply(v,s);
        representatives.insert(u);
      }
    vector<array<int,3>> p(representatives.begin(),representatives.end());
    const int n=int(p.size()); assert(n==21);
    vector<int> neighborhoods(n);
    for (int i=0; i<n; ++i) for (int j=0; j<n; ++j) {
        int dot=0;
        for (int k=0; k<3; ++k) dot^=multiply(p[i][k],p[j][k]);
        if (dot==0) neighborhoods[i]|=1<<j;
    }
    for (int i=0; i<n; ++i) {
        assert(__builtin_popcount(unsigned(neighborhoods[i]))==5);
        for (int j=0; j<i; ++j)
            assert(__builtin_popcount(unsigned(neighborhoods[i]&neighborhoods[j]))==1);
    }
    const int m=1<<n, all=m-1;
    vector<int> cover(m,0);
    for (int s=1; s<m; ++s) {
        int bit=__builtin_ctz(unsigned(s));
        cover[s]=cover[s^(1<<bit)]|neighborhoods[bit];
    }
    vector<unsigned long long> orders(m,0);
    orders[0]=1;
    for (int s=0; s<m; ++s) if (orders[s]) {
        for (int i=0; i<n; ++i) if (!(s&(1<<i))) {
            int next=cover[s]|neighborhoods[i];
            if (next!=cover[s]) orders[s|(1<<i)]+=orders[s];
        }
    }
    int best=0, supports=0, reachable=0;
    unsigned long long sequences=0;
    map<vector<int>,int> profiles;
    for (int s=0; s<m; ++s) if (orders[s]) {
        ++reachable;
        int len=__builtin_popcount(unsigned(s));
        if (len>best) {best=len; supports=0; sequences=0; profiles.clear();}
        if (len==best) {
            ++supports; sequences+=orders[s];
            if (len==10) assert(cover[s]==all);
            vector<int> h(6,0);
            for (int line=0; line<n; ++line) {
                int intersection=0;
                for (int i=0; i<n; ++i)
                    if ((s&(1<<i))&&(neighborhoods[i]&(1<<line))) ++intersection;
                ++h[intersection];
            }
            ++profiles[h];
        }
    }
    const map<vector<int>,int> expected={
      {{0,3,11,4,2,1},30240}, {{0,4,8,7,1,1},20160},
      {{0,4,9,4,4,0},20160}, {{0,5,5,10,0,1},6048},
      {{0,5,6,7,3,0},60480}, {{0,6,3,10,2,0},3360}
    };
    assert(best==10 && reachable==738840 && supports==140448);
    assert(sequences==36288000000ULL && profiles==expected);
    cout << "PASS: length=" << best << " supports=" << supports
         << " orders=" << sequences << " reachable=" << reachable << '\n';
    for (auto &[h,c]:profiles) {
        cout << "profile";
        for (int v:h) cout << ' ' << v;
        cout << " count=" << c << '\n';
    }
}
