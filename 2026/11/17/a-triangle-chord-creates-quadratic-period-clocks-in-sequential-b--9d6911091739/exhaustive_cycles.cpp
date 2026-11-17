// Standalone exact finite-state check of sequential threshold dynamics.
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <vector>
using namespace std;

static uint32_t evolve(uint32_t x, const vector<uint32_t>& masks) {
    for (int i=0;i<(int)masks.size();++i) {
        int occupied=__builtin_popcount(x&masks[i]);
        uint32_t bit=1u<<i;
        if (x&bit) {
            if (occupied<3) x&=~bit;
        } else if (occupied>=1) x|=bit;
    }
    return x;
}

static vector<uint32_t> make_masks(int beta, bool chord) {
    int len=2*beta+1, n=2*len;
    vector<uint32_t> mask(n);
    for (int i=0;i<n;++i)mask[i]=1u<<i;
    auto edge=[&](int u,int v){mask[u]|=(1u<<v);mask[v]|=(1u<<u);};
    for (int i=0;i<len-1;++i){edge(i,i+1);edge(len+i,len+i+1);}
    edge(beta,len+beta);
    if (chord)edge(0,2);
    return mask;
}

static map<int,long long> census(int b,bool chord) {
    auto masks=make_masks(b,chord);
    int n=(int)masks.size();
    uint32_t N=1u<<n;
    vector<uint8_t> done(N,0);
    vector<int32_t> index(N,-1);
    map<int,long long> cycles;
    vector<uint32_t> trail;
    for(uint32_t s=0;s<N;++s) {
        if (done[s])continue;
        trail.clear();
        uint32_t x=s;
        while (!done[x] && index[x]==-1) {
            index[x]=(int32_t)trail.size();
            trail.push_back(x);
            x=evolve(x,masks);
        }
        if(!done[x]) {
            int length=(int)trail.size()-index[x];
            cycles[length]++;
        }
        for(uint32_t p:trail){done[p]=1;index[p]=-1;}
    }
    return cycles;
}

int main() {
    for(int b=2;b<=5;++b) {
        auto new_counts=census(b,true);
        auto old_counts=census(b,false);
        int expected=b*(b+4);
        assert(new_counts.count(expected) && new_counts.at(expected)==1);
        cout << "beta=" << b << " vertices=" << (4*b+2)
             << " original_period_counts=";
        for(auto [t,c]:old_counts)cout << t << ':' << c << ',';
        cout << " chord_period_counts=";
        for(auto [t,c]:new_counts)cout << t << ':' << c << ',';
        cout << " PASS\n";
    }
}
