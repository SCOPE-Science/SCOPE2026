// Exact, independent finite check of zero-field spin-one folded-four-cube states.
// Build: c++ -O3 -std=c++17 verify_exhaustive.cpp -o verify_exhaustive
// Run: ./verify_exhaustive
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
using namespace std;
int main() {
    constexpr int n=4,N=1<<n;
    array<array<int,n+1>,N> neighbors{};
    for(int x=0;x<N;++x){for(int i=0;i<n;++i)neighbors[x][i]=x^(1<<i);neighbors[x][n]=x^(N-1);}
    array<int,N> spin{},digit{},direction{};
    spin.fill(-1); direction.fill(1);
    int exchange= N*(n+1)/2, occupied=N;
    long long examined=0, crit=0, full=0, half=0, empty=0, below=0, above=0;
    int best_below=99999,best_above=99999;
    while(true){
        ++examined;
        const int criterion =2*exchange+(n-1)*occupied;
        assert(criterion>=0);
        if(criterion==0){
            ++crit;
            if(occupied==0)++empty;
            else if(occupied==N/2)++half;
            else if(occupied==N)++full;
            else assert(false);
        }
        int e_below=2*exchange+2*occupied;
        if(e_below<best_below){best_below=e_below;below=0;}
        if(e_below==best_below)++below;
        int e_above=2*exchange+4*occupied;
        if(e_above<best_above){best_above=e_above;above=0;}
        if(e_above==best_above)++above;
        int i=0;
        while(i<N && (digit[i]+direction[i]<0 || digit[i]+direction[i]>2)) {
            direction[i]=-direction[i];++i;
        }
        if(i==N)break;
        int old=spin[i];digit[i]+=direction[i];int current=digit[i]-1;
        int neighbor_sum=0;for(int j=0;j<=n;++j)neighbor_sum+=spin[neighbors[i][j]];
        exchange+=(current-old)*neighbor_sum;
        occupied+=current*current-old*old;
        spin[i]=current;
    }
    assert(examined==43046721LL);
    assert(crit==51 && full==10 && half==40 && empty==1);
    assert(best_below==-16 && below==10); // 2 H with D=1: 2(-24+16)=-16
    assert(best_above==0 && above==1);
    cout<<"PASS exhaustive_states="<<examined<<" critical="<<crit
        <<" occupied_full="<<full<<" occupied_half="<<half
        <<" empty="<<empty<<" strict_below="<<below<<" strict_above="<<above<<'\n';
}
