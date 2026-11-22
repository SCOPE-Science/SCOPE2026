// Independent exact checker: cyclic Fano difference-set construction.
#include <array>
#include <vector>
#include <set>
#include <unordered_map>
#include <functional>
#include <iostream>
#include <algorithm>
#include <cassert>
#include <cstdint>
using namespace std;
int main() {
    // The seven cyclic translates of {0,1,3} give the Fano lines.
    array<uint16_t,14> adj{};
    for(int j=0;j<7;j++) for(int d : {0,1,3}) {
        int i=(j+d)%7;adj[i] |= uint16_t(1u<<(7+j));adj[7+j] |= uint16_t(1u<<i);
    }
    for(int i=0;i<14;i++) assert(__builtin_popcount(unsigned(adj[i]))==3);
    vector<uint16_t> minima;
    for(int m=0;m<(1<<14);m++) {
        if(__builtin_popcount(unsigned(m))!=4) continue;
        uint16_t covered=uint16_t(m);
        for(int i=0;i<14;i++) if(m&(1<<i)) covered |= adj[i];
        if(covered==((1<<14)-1)) minima.push_back(uint16_t(m));
    }
    assert(minima.size()==21);
    for(auto m : minima) {assert(__builtin_popcount(unsigned(m&127))==2);for(int i=0;i<14;i++) if(m&(1<<i)) assert(!(m & adj[i]));}
    vector<int> coeff(15,0); set<int> shattered;
    for(int s=0;s<(1<<14);s++) {
        int k=__builtin_popcount(unsigned(s));
        set<int> traces;for(auto m : minima) traces.insert(int(m)&s);
        if(traces.size()==(size_t(1)<<k)){coeff[k]++;shattered.insert(s);}
    }
    assert(coeff[0]==1 && coeff[1]==14 && coeff[2]==70);
    for(int k=3;k<15;k++) assert(coeff[k]==0);
    for(int i=0;i<14;i++)for(int j=i+1;j<14;j++)
       assert(bool(shattered.count((1<<i)|(1<<j)))==(!(adj[i]&(1<<j))));
    // Independent recursive online-shattering verifier, no precomputed tree.
    array<uint32_t,14> contain{};
    for(int j=0;j<21;j++) for(int i=0;i<14;i++) if(minima[j]&(1<<i))contain[i]|=1u<<j;
    unordered_map<uint32_t,int> memo;
    function<int(uint32_t)> L=[&](uint32_t state)->int {
        auto it=memo.find(state);if(it!=memo.end())return it->second;
        int ans=0;
        for(auto b:contain){auto yes=state&b,no=state&(~b);
            if(yes&&no)ans=max(ans,1+min(L(yes),L(no)));
        }
        memo[state]=ans;return ans;
    };
    assert(L((1u<<21)-1)==3);
    cout << "model=cyclic_Fano_difference_set_0_1_3\n";
    cout << "minimum_dominating_sets=21 cardinality=4\n";
    cout << "shattering_polynomial=1+14z+70z^2\n";
    cout << "shattered_pairs=70 first_betti=57 VC=2 Ldim=3\n";
    cout << "PASS\n";
}
