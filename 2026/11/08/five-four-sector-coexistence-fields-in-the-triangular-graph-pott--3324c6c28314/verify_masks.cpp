// Independent enumeration: first choose edges of favored color, then a subset for color 1.
// The remaining edges have color 2. Uses edge masks and vertex degree counts.
// Compile: c++ -O3 -std=c++17 verify_masks.cpp -o verify_masks && ./verify_masks
#include <array>
#include <cstdlib>
#include <iostream>
using namespace std;
constexpr int M=15,N=6, ALL=(1<<M)-1;
constexpr int expectedE[16]={24,20,16,12,12,12,12,14,16,18,24,30,36,44,52,60};
constexpr long long expectedG[16]={1760,4680,2520,300,5580,19530,6180,15480,3420,120,900,1080,120,180,30,1};
int main(){int incident[N]{};int e=0;for(int u=0;u<N;u++)for(int v=u+1;v<N;v++){incident[u]|=1<<e;incident[v]|=1<<e;e++;}
 int B[1<<M][N];for(int mask=0;mask<=ALL;mask++)for(int v=0;v<N;v++)B[mask][v]=__builtin_popcount((unsigned)(mask&incident[v]));
 array<int,16> best;array<long long,16> ways{};best.fill(999);
 for(int red=0;red<=ALL;red++){
  int occupancy=__builtin_popcount((unsigned)red),rest=ALL^red;
  int blue=rest;
  while(true){int green=rest^blue,E=0;
   for(int v=0;v<N;v++){
    int a=B[red][v],b=B[blue][v],c=B[green][v];
    E+=(a*(a-1)+b*(b-1)+c*(c-1))/2;
   }
   if(E<best[occupancy]){best[occupancy]=E;ways[occupancy]=1;}
   else if(E==best[occupancy])ways[occupancy]++;
   if(blue==0)break;blue=(blue-1)&rest;
  }
 }
 for(int i=0;i<=15;i++){
   cout<<i<<" "<<best[i]<<" "<<ways[i]<<"\n";
   if(best[i]!=expectedE[i]||ways[i]!=expectedG[i]){cerr<<"MISMATCH\n";return 1;}
 }
 cout<<"VERIFY_MASKS_OK\n";
}
