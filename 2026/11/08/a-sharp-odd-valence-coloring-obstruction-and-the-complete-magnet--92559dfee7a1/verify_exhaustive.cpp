// Self-contained exhaustive integer certificate for the icosahedral 3-state Potts ground sectors.
// Compile: c++ -std=c++17 -O2 verify_exhaustive.cpp -o potts_check && ./potts_check
#include <array>
#include <cstdint>
#include <iostream>
#include <map>
#include <set>
#include <utility>
#include <vector>
using namespace std;
int main(){
 vector<pair<int,int>> e;
 for(int i=0;i<5;++i){
   int j=(i+1)%5;
   e.push_back({0,1+i}); e.push_back({11,6+i});
   e.push_back({1+i,1+j}); e.push_back({6+i,6+j});
   e.push_back({1+i,6+i}); e.push_back({1+i,6+(i+4)%5});
 }
 if(e.size()!=30){cerr<<"edge count";return 1;}
 set<pair<int,int>> unique_edges;
 array<int,12> degrees{};
 for(auto [u,v]:e){if(u==v||u<0||v<0||u>11||v>11){cerr<<"vertex";return 1;}
   if(u>v)swap(u,v);
   unique_edges.insert({u,v});++degrees[u];++degrees[v];}
 if(unique_edges.size()!=30){cerr<<"duplicate edges";return 1;}
 for(auto d:degrees)if(d!=5){cerr<<"non-icosahedral degree";return 1;}
 array<int,13> minimum;minimum.fill(100);
 array<uint64_t,13> counts{};
 map<uint32_t,int> supports;
 for(int word=0;word<531441;word++){
   int value=word,spin[12],favored=0;
   for(int v=0;v<12;v++){
     spin[v]=value%3;
     value/=3;
     favored+=(spin[v]==0);
   }
   int bad=0;uint32_t mask=0;
   for(size_t i=0;i<e.size();i++){
     auto [u,v]=e[i];
     if(spin[u]==spin[v]){++bad;mask|=(uint32_t(1)<<i);}
   }
   if(bad<minimum[favored]){minimum[favored]=bad;counts[favored]=0;}
   if(bad==minimum[favored])++counts[favored];
   if(bad==3)++supports[mask];
 }
 constexpr array<int,13> expected_min={10,8,6,4,3,4,5,8,11,15,20,25,30};
 constexpr array<uint64_t,13> expected_num={72,600,1260,360,120,360,120,480,240,160,144,24,1};
 if(minimum!=expected_min||counts!=expected_num){cerr<<"sector table mismatch\n";return 2;}
 if(supports.size()!=20){cerr<<"support count";return 3;}
 for(auto [mask,number]:supports){
   if(number!=6){cerr<<"support multiplicity";return 4;}
   if(__builtin_popcount(mask)!=3){cerr<<"support edge count";return 5;}
 }
 // Ground-state degeneracies at the six exactly rational crossing fields.
 constexpr array<int,6> crossing={-2,-1,1,3,4,5};
 constexpr array<uint64_t,6> expected_cross={2292,480,600,840,400,329};
 for(int q=0;q<6;q++){
   int x=crossing[q],bottom=100000;
   for(int k=0;k<13;k++)bottom=min(bottom,minimum[k]-x*k);
   uint64_t deg=0;
   for(int k=0;k<13;k++)if(minimum[k]-x*k==bottom)deg+=counts[k];
   if(deg!=expected_cross[q]){cerr<<"coexistence mismatch";return 6;}
 }
 // A lower convex hull certificate: every sector is on or above the
 // seven listed line vertices, and the slopes of successive edges increase.
 constexpr array<int,7> hull={0,3,4,6,8,9,12};
 constexpr array<int,6> slope={-2,-1,1,3,4,5};
 for(int t=0;t<6;t++){
   int i=hull[t], j=hull[t+1];
   if(minimum[j]-minimum[i]!=slope[t]*(j-i)){cerr<<"hull slope";return 7;}
   for(int k=i;k<=j;k++){
     if(minimum[k]<minimum[i]+slope[t]*(k-i)){cerr<<"hull violated";return 8;}
   }
 }
 cout<<"EXHAUSTIVE_OK 531441 configurations; 20 frustration supports; six coexistence counts; convex hull\n";
 return 0;
}
