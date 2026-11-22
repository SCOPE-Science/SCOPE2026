// A separate monotone shortest-path dynamic-programming check of lower visibility.
// Compile: g++ -std=c++17 -O3 verify_lattice.cpp -o verify_lattice
#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
using namespace std;
constexpr int DIM=6, N=1<<DIM;
static bool reachable(uint64_t mask, int a, int b) {
    const int differences=a^b;
    int position[DIM],d=0;
    for(int bit=0;bit<DIM;++bit) if((differences>>bit)&1)position[d++]=1<<bit;
    bool dp[1<<DIM]={false}; dp[0]=true;
    const int complete=(1<<d)-1;
    for(int subset=1;subset<=complete;++subset) {
        int vertex=a;
        for(int j=0;j<d;++j)if((subset>>j)&1)vertex^=position[j];
        if(subset!=complete && ((mask>>vertex)&1))continue;
        for(int j=0;j<d;++j)if((subset>>j)&1)
            if(dp[subset^(1<<j)]){dp[subset]=true;break;}
    }
    return dp[complete];
}
static bool visible_set(uint64_t mask) {
    int members[8],n=0;
    for(int v=0;v<N;++v)if((mask>>v)&1)members[n++]=v;
    for(int i=0;i<n;++i)for(int j=i+1;j<n;++j)
        if(!reachable(mask,members[i],members[j]))return false;
    return true;
}
static bool maximal(uint64_t mask) {
    if(!visible_set(mask))return false;
    for(int v=0;v<N;++v) if(!((mask>>v)&1))
        if(visible_set(mask|(uint64_t(1)<<v)))return false;
    return true;
}
static uint64_t neighborhood(int center) {
    uint64_t mask=uint64_t(1)<<center;
    for(int j=0;j<DIM;++j)mask|=uint64_t(1)<<(center^(1<<j));
    return mask;
}
int main() {
    for(int k=2;k<=6;++k) {
        const int r=k-1;uint64_t t=(uint64_t(1)<<r)-1,feasible=0,maximal_sets=0,all=0;
        while(t<(uint64_t(1)<<63)){
            const uint64_t mask=uint64_t(1)|(t<<1);
            if(visible_set(mask)){
                ++feasible;
                if(maximal(mask))++maximal_sets;
            }
            ++all;
            const uint64_t low=t&-t,next=t+low;
            if(!low || next>=(uint64_t(1)<<63))break;
            t=(((t^next)>>2)/low)|next;
        }
        cout<<"k="<<k<<" considered="<<all<<" feasible="<<feasible<<" maximal="<<maximal_sets<<'\n';
        if(maximal_sets!=0)return 1;
    }
    int count=0;
    for(int center=0;center<N;++center){uint64_t s=neighborhood(center);
        if(!visible_set(s)||!maximal(s))return 2;
        if(s&1)++count;
    }
    cout<<"star_neighborhoods="<<N<<" containing_zero="<<count<<'\n';
    if(count!=7)return 3;
    cout<<"LATTICE_VERIFY_OK\n";
}
