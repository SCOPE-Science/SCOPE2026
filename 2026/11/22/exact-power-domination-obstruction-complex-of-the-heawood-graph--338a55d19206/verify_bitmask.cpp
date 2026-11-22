// Exhaustive, integer-only power propagation on the 14-vertex Fano incidence graph.
// Vertex labels 0..6 are points, 7..13 are lines.
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;
constexpr int N=14;
constexpr uint16_t ALL=(1u<<N)-1;
static inline int pop(uint16_t x){return __builtin_popcount((unsigned)x);}
int main(){
    array<uint16_t,N> nbr{};
    const int offsets[3]={0,1,3};
    for(int p=0;p<7;p++)for(int d:offsets){int ell=7+(p+d)%7;nbr[p]|=uint16_t(1u<<ell);nbr[ell]|=uint16_t(1u<<p);}
    array<uint16_t,N> star{};
    for(int v=0;v<N;v++) star[v]=nbr[v]|(1u<<v);
    array<int,15> fails{};int correct=0;
    for(uint16_t seed=0;seed<=ALL;seed++){
        uint16_t blue=seed;
        for(int u=0;u<N;u++)if(seed&(1u<<u))blue|=nbr[u];
        while(1){
            uint16_t add=0;
            for(int u=0;u<N;u++)if(blue&(1u<<u)){
                uint16_t unseen=nbr[u]&~blue;
                if(pop(unseen)==1)add|=unseen;
            }
            if(!add)break;
            blue|=add;
        }
        bool pdom=(blue==ALL),contained=false;
        for(auto s:star)if((seed&s)==seed)contained=true;
        assert(pdom==!contained);
        if(!pdom)fails[pop(seed)]++;
        if(pdom && pop(seed)==2)correct++;
    }
    assert(fails[0]==1&&fails[1]==14&&fails[2]==63&&fails[3]==56&&fails[4]==14);
    for(int k=5;k<15;k++)assert(!fails[k]);
    assert(correct==28);
    cout<<"PASS bitmask: 16384 exhaustive subsets, exact failed polynomial and 28 minimum placements\n";
}
