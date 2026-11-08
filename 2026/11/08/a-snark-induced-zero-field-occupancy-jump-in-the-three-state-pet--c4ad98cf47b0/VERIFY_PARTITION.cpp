// Independent exact enumeration by an ordered partition of the fifteen edges.
// Build: c++ -std=c++17 -O2 VERIFY_PARTITION.cpp -o verify_partition && ./verify_partition
#include <array>
#include <cstdint>
#include <iostream>
#include <limits>
using namespace std;
int main(){
    // Alternate vertex ordering: outer cycle, inner pentagram, then spokes.
    array<array<int,2>,15> e{};
    for(int i=0;i<5;++i){
        e[i]={i,(i+1)%5};
        e[5+i]={5+i,5+(i+2)%5};
        e[10+i]={i,5+i};
    }
    array<unsigned,15> nbr{};
    for(int i=0;i<15;++i)for(int j=0;j<i;++j){
        auto a=e[i],b=e[j];
        if(a[0]==b[0]||a[0]==b[1]||a[1]==b[0]||a[1]==b[1]){
            nbr[i]|=1u<<j;
            nbr[j]|=1u<<i;
        }
    }
    constexpr int N=1<<15;
    array<unsigned char,N> same{};
    for(int mask=1;mask<N;++mask){
        int v=__builtin_ctz((unsigned)mask),rest=mask&(mask-1);
        same[mask]=same[rest]+__builtin_popcount(nbr[v]&(unsigned)rest);
    }
    array<int,16> best;
    best.fill(numeric_limits<int>::max());
    array<uint64_t,16> ways{};
    uint64_t visited=0;
    const int full=N-1;
    // M is the set of colour-zero edges, A the colour-one edges,
    // and B the remaining colour-two edges. This visits all 3^15 states.
    for(int M=0;M<N;++M){
        int other=full^M;
        int k=__builtin_popcount((unsigned)M);
        int A=other;
        while(true){
            int B=other^A;
            int energy=same[M]+same[A]+same[B];
            if(energy<best[k]){best[k]=energy;ways[k]=0;}
            if(energy==best[k])++ways[k];
            ++visited;
            if(A==0)break;
            A=(A-1)&other;
        }
    }
    constexpr array<int,16> expected_min={10,8,6,4,2,2,2,4,6,8,10,14,18,22,26,30};
    constexpr array<uint64_t,16> expected_ways={1782,5880,6420,2640,300,1200,300,2520,5520,3120,192,1440,1160,300,30,1};
    if(visited!=14348907ULL || best!=expected_min || ways!=expected_ways) return 1;
    cout<<"visited "<<visited<<"\n";
    for(int k=0;k<=15;++k)cout<<k<<" "<<best[k]<<" "<<ways[k]<<"\n";
    cout<<"VERIFY_PARTITION_OK\n";
}
