// Exact finite enumeration of reversal-complement-closed four-base single-deletion codes.
// Build: c++ -std=c++17 -O2 census.cpp -o census
// Run: ./census > maximum_codebooks.tsv
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <set>
#include <string>
#include <vector>
using namespace std;

struct Bits {
    uint64_t lo = 0, hi = 0;
    bool any() const { return lo || hi; }
    int count() const { return __builtin_popcountll(lo) + __builtin_popcountll(hi); }
    int first() const { return lo ? __builtin_ctzll(lo) : 64 + __builtin_ctzll(hi); }
    void erase(int v) { if (v < 64) lo &= ~(1ULL << v); else hi &= ~(1ULL << (v-64)); }
    void insert(int v) { if (v < 64) lo |= (1ULL << v); else hi |= (1ULL << (v-64)); }
    friend Bits operator&(Bits a, Bits b) { return {a.lo & b.lo, a.hi & b.hi}; }
    friend Bits operator~(Bits a) { return {~a.lo, ~a.hi}; }
};

const string alphabet = "ACGT";
string complement(string s) {
    for (char &c : s) {
        if(c=='A') c='T'; else if(c=='T') c='A';
        else if(c=='C') c='G'; else if(c=='G') c='C';
        else assert(false);
    }
    return s;
}
string reverse_complement(string s) { reverse(s.begin(),s.end()); return complement(s); }
int digit(char c) { size_t p=alphabet.find(c); assert(p!=string::npos); return int(p); }
uint64_t deletion_mask(const string &s) {
    assert(s.size()==4);
    uint64_t mask=0;
    for(int omit=0;omit<4;omit++) {
        int idx=0;
        for(int pos=0;pos<4;pos++) if(pos!=omit) idx=idx*4+digit(s[pos]);
        mask|=1ULL<<idx;
    }
    return mask;
}
struct Orbit { array<string,2> words; uint64_t shadow; };
vector<Orbit> build_orbits() {
    vector<Orbit> out;
    for(char a:alphabet) for(char b:alphabet) for(char c:alphabet) for(char d:alphabet) {
        string s; s+=a;s+=b;s+=c;s+=d;
        string t=reverse_complement(s);
        if(s>=t) continue; // self-reverse-complements and duplicate representatives excluded
        uint64_t x=deletion_mask(s), y=deletion_mask(t);
        if(x&y) continue; // two different strands must not share a deletion output
        out.push_back({{s,t},x|y});
    }
    assert(out.size()==120);
    return out;
}

Bits neighbors[128];
vector<Orbit> ordered;
array<int,11> selected{};
long long solutions=0, calls=0, pruned=0; bool emit=false;

// Proper greedy coloring of the *compatibility graph* bounds clique size.
// Each constructed color class is independent; a clique takes <= one vertex per class.
// Returning `needed` early means no pruning is performed at this node.
int color_upper_bound(Bits candidates,int needed) {
    int colors=0;
    while(candidates.any() && colors<needed) {
        ++colors;
        Bits available=candidates;
        while(available.any()) {
            int v=available.first();
            available.erase(v);
            candidates.erase(v);
            available=available & ~neighbors[v];
        }
    }
    return colors;
}

void visit(Bits candidates,int remaining,int depth) {
    ++calls;
    if(remaining==0) {
        ++solutions;
        if(emit) {
            vector<string> names;
            for(int i=0;i<depth;i++) names.push_back(ordered[selected[i]].words[0]);
            sort(names.begin(),names.end());
            for(size_t k=0;k<names.size();k++) cout<<(k?"\t":"")<<names[k];
            cout<<'\n';
        }
        return;
    }
    if(candidates.count()<remaining || color_upper_bound(candidates,remaining)<remaining) {
        ++pruned;
        return;
    }
    while(candidates.any()) {
        if(candidates.count()<remaining) break;
        int v=candidates.first();
        candidates.erase(v); // all later chosen vertices must have higher indices
        selected[depth]=v;
        visit(candidates & neighbors[v],remaining-1,depth+1);
    }
}

int main() {
    vector<Orbit> originals=build_orbits();
    vector<int> index(120); iota(index.begin(),index.end(),0);
    vector<int> degree(120,0);
    for(int i=0;i<120;i++) for(int j=0;j<120;j++)
        if(i!=j && !(originals[i].shadow&originals[j].shadow)) ++degree[i];
    sort(index.begin(),index.end(),[&](int i,int j) {
        if(degree[i]!=degree[j]) return degree[i]>degree[j];
        return i<j;
    });
    for(int i:index) ordered.push_back(originals[i]);
    for(int i=0;i<120;i++) for(int j=0;j<120;j++)
        if(i!=j && !(ordered[i].shadow&ordered[j].shadow)) neighbors[i].insert(j);
    Bits all;
    for(int i=0;i<120;i++) all.insert(i);
    visit(all,12,0);
    const long long infeasible12=solutions;
    if(infeasible12!=0) { cerr<<"INFEASIBLE_12_FAILED "<<infeasible12<<'\n'; return 1; }
    solutions=0; calls=0; pruned=0; emit=true;
    visit(all,11,0);
    cerr<<"ORBIT_CANDIDATES=120; SIZE_12_SETS="<<infeasible12
        <<"; MAXIMUM_CODEBOOKS="<<solutions
        <<"; RECURSIVE_CALLS="<<calls<<"; SAFE_PRUNES="<<pruned<<'\n';
    return solutions==44 ? 0 : 1;
}
