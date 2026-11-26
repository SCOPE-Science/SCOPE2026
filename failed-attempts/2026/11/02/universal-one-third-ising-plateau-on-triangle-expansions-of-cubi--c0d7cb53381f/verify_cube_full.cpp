// Exhaustive gray-code enumeration of every spin configuration of the truncated cube.
// Compile: c++ -std=c++17 -O3 verify_cube_full.cpp -o verify_cube_full
// Run: ./verify_cube_full
#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;
int main(){
    vector<int> neighbors[24]; int edges=0;
    auto add=[&](int a,int b){neighbors[a].push_back(b);neighbors[b].push_back(a);edges++;};
    for(int v=0;v<8;v++) for(int a=0;a<3;a++) for(int b=a+1;b<3;b++)add(3*v+a,3*v+b);
    for(int v=0;v<8;v++) for(int a=0;a<3;a++) if(!(v&(1<<a)))add(3*v+a,3*(v^(1<<a))+a);
    if(edges!=36) return 1;
    array<int,24> spins; spins.fill(-1);
    int energy=36,mag=-24;
    array<int,25> minima; minima.fill(100000);
    array<uint64_t,25> counts{};
    minima[0]=36;counts[0]=1;
    for(uint32_t t=1;t<(1u<<24);t++){
        int v=__builtin_ctz(t),sum=0;
        for(int j:neighbors[v])sum+=spins[j];
        energy-=2*spins[v]*sum;
        mag-=2*spins[v];
        spins[v]=-spins[v];
        int k=(mag+24)/2;
        if(energy<minima[k]){minima[k]=energy;counts[k]=1;}
        else if(energy==minima[k])counts[k]++;
    }
    constexpr int expectedE[13]={36,30,24,18,12,6,0,-6,-12,-14,-16,-18,-20};
    constexpr uint64_t expectedC[13]={1,24,240,1296,4092,7632,8056,4272,828,3312,4572,2520,450};
    for(int k=0;k<25;k++){
        int j=min(k,24-k);
        if(minima[k]!=expectedE[j] || counts[k]!=expectedC[j]){
            cerr<<"FAILED k="<<k<<" E="<<minima[k]<<" c="<<counts[k]<<"\n";
            return 2;
        }
    }
    cout<<"truncated cube: 16777216 spin states exhausted; 25 minima and counts match\n";
    cout<<"ground-state counts for Q=0..12: ";
    for(int q=0;q<=12;q++)cout<<(q?",":"")<<expectedC[q];
    cout<<"\nPASS\n";
}
