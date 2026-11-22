// Exhaustive seven-coordinate code search using independent bit-mask graph construction.
// Compile: g++ -O2 -std=c++17 ALTERNATE.cpp -o alternate && ./alternate
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;
vector<unsigned> word;
vector<uint64_t> adj;
int best = 0, best_count = 0, maximal_count = 0, reversal_fixed = 0;
uint64_t core = 0;
int rev7(unsigned x) { int y=0; for(int i=0;i<7;i++) {y=(y<<1)|(x&1U);x>>=1;}return y; }
int idx(unsigned x) {auto it=lower_bound(word.begin(),word.end(),x); assert(it!=word.end()&&*it==x);return int(it-word.begin());}
void visit(uint64_t R,uint64_t P,uint64_t X) {
    if(!P && !X) {
        ++maximal_count;
        int size=__builtin_popcountll(R);
        if(size>best) {best=size;best_count=0;core=R;reversal_fixed=0;}
        if(size==best) {
            ++best_count;core &= R;
            uint64_t rev=0;
            for(uint64_t z=R;z;z&=z-1) {int i=__builtin_ctzll(z); rev |= uint64_t(1)<<idx(rev7(word[i]));}
            if(rev==R) ++reversal_fixed;
        }
        return;
    }
    uint64_t union_set=P|X;
    int pivot=-1, score=-1;
    for(uint64_t z=union_set;z;z&=z-1) {
        int i=__builtin_ctzll(z), sc=__builtin_popcountll(P & adj[i]);
        if(sc>score) {score=sc;pivot=i;}
    }
    uint64_t todo = P & ~adj[pivot];
    while(todo) {
        int v=__builtin_ctzll(todo);uint64_t b=uint64_t(1)<<v;
        visit(R|b,P&adj[v],X&adj[v]);P&=~b;X|=b;todo&=~b;
    }
}
int main() {
    for(unsigned x=0;x<(1U<<7);++x) if(!(x&(x<<1))) word.push_back(x);
    assert(word.size()==34);
    adj.resize(word.size());
    for(size_t i=0;i<word.size();i++)for(size_t j=0;j<i;j++) {
        unsigned a=word[i],b=word[j];
        int down_a=__builtin_popcount(a & ~b),down_b=__builtin_popcount(b & ~a);
        if(max(down_a,down_b)>=2) {adj[i]|=uint64_t(1)<<j;adj[j]|=uint64_t(1)<<i;}
    }
    visit(0,(uint64_t(1)<<word.size())-1,0);
    assert(best==8 && best_count==10 && maximal_count==1398);
    vector<unsigned> forced={0b0010001,0b0100101,0b1000100,0b1001001,0b1010010,0b1010101};
    uint64_t expected=0;for(auto x:forced)expected|=uint64_t(1)<<idx(x);
    assert(core==expected && reversal_fixed==4);
    cout<<"n=7: size="<<best<<", optima="<<best_count<<", maximal="<<maximal_count<<", common="<<forced.size()<<"\nALTERNATE_OK\n";
}
