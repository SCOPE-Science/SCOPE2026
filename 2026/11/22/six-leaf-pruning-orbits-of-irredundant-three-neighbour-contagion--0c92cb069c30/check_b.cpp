// Standalone exact integer verification, C++17.
#include <array>
#include <algorithm>
#include <cassert>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <vector>
using namespace std;

int main() {
    constexpr int N = 16, LIMIT = 1 << N, FULL = LIMIT-1;
    array<int,N> adj{};
    for(int v=0;v<N;++v)for(int i=0;i<4;++i) adj[v]|=1<<(v^(1<<i));
    // Bitwise implementation of synchronous closure. -1 means not percolating.
    vector<int> time(LIMIT,-1);
    for(int m=0;m<LIMIT;++m) {
        int a=m, rounds=0;
        for(;;) {
            int b=a;
            for(int v=0;v<N;++v) {
                if(!(a&(1<<v)) && __builtin_popcount((unsigned)(a&adj[v]))>=3) b|=1<<v;
            }
            if(b==a)break;
            a=b;
            rounds++;
        }
        if(a==FULL)time[m]=rounds;
    }
    map<pair<int,int>,int> hist;
    set<int> minimal;
    for(int m=0;m<LIMIT;++m) if(time[m]>=0) {
        bool remove_one_kills=true;
        for(int v=0;v<N;++v)if((m>>v)&1) {
            if(time[m^(1<<v)]>=0){remove_one_kills=false;break;}
        }
        if(remove_one_kills) {
            minimal.insert(m);
            hist[{__builtin_popcount((unsigned)m),time[m]}]++;
        }
    }
    assert((hist==map<pair<int,int>,int>{{{6,2},8},{{7,3},160},{{7,4},768}}));
    assert(minimal.size()==936);
    const array<array<int,4>,6> specs{{{{5736,6,2,8}},{{5782,7,3,64}},
        {{5801,7,3,96}},{{5785,7,4,192}},{{5804,7,4,192}},{{5786,7,4,384}}}};
    set<int> accumulated;
    array<int,4> perm{{0,1,2,3}};
    for(auto spec:specs) {
        auto [rep,weight,delay,expected]=spec;
        set<int> orbit;
        perm={{0,1,2,3}};
        do {
            array<int,N> table{};
            for(int v=0;v<N;++v){
                for(int i=0;i<4;++i) if((v>>i)&1)table[v]|=1<<perm[i];
            }
            for(int shift=0;shift<N;++shift) {
                int image=0;
                for(int v=0;v<N;++v)if((rep>>v)&1)image|=1<<(table[v]^shift);
                orbit.insert(image);
                assert(minimal.count(image)==1);
                assert(__builtin_popcount((unsigned)image)==weight);
                assert(time[image]==delay);
            }
        } while(next_permutation(perm.begin(),perm.end()));
        assert((int)orbit.size()==expected);
        for(int image:orbit) assert(accumulated.insert(image).second);
    }
    assert(accumulated==minimal);
    set<int> parity;
    for(int p=0;p<=1;++p)for(int a=0;a<N;++a){
        if((__builtin_popcount((unsigned)a)&1)!=p)continue;
        int s=0;
        for(int v=0;v<N;++v)if((__builtin_popcount((unsigned)v)&1)==p && v!=a && v!=(a^15))s|=1<<v;
        parity.insert(s);
    }
    assert(parity.size()==8);
    for(int s:parity)assert(time[s]==2 && minimal.count(s));
    for(int s:minimal)if(__builtin_popcount((unsigned)s)==6)assert(parity.count(s));
    cout << "PASS: all " << LIMIT << " subsets; " << minimal.size() << " minimal; six orbits\n";
    for(auto [key,num]:hist)cout << key.first << ' ' << key.second << ' ' << num << '\n';
}
