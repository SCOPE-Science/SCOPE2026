// Exact exhaustive certificate for bounded-degree two-cuts on seven labelled vertices.
// Build: c++ -std=c++17 -O2 -Wall -Wextra verify.cpp -o verify && ./verify
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <unordered_set>
using namespace std;
constexpr int N=7,E=21;
using Mask=uint32_t;
constexpr array<Mask,10> reps={0x1bccbb,0x61ffd,0x1bf72c,0x1f3bac,0x1b75bc,0x1f74ad,0xf1e3f,0x17f4f8,0xf3dbc,0x1a7f9c};
array<pair<int,int>,E> edges{};
int idx(int i,int j){if(i>j)swap(i,j);return i*(2*N-i-1)/2+(j-i-1);}
array<Mask,N> adjacency(Mask g){array<Mask,N> adj{};for(int e=0;e<E;e++)if((g>>e)&1){auto [a,b]=edges[e];adj[a]|=1u<<b;adj[b]|=1u<<a;}return adj;}
bool has_two_cut(Mask g){auto adj=adjacency(g);for(Mask A=1;A<(1u<<(N-1));A++){
  // Each unordered nontrivial bipartition is represented once by a nonempty
  // proper A not containing vertex six. For all vertices check crossing degree.
  bool valid=true;
  for(int v=0;v<N;v++){
    Mask opposite = (A>>v&1)? (~A)&((1u<<N)-1): A;
    if(__builtin_popcount(adj[v]&opposite)>2){valid=false;break;}
  }
  if(valid)return true;
}return false;}
Mask permute(Mask g,const array<int,N>& p){Mask out=0;for(int e=0;e<E;e++)if(g>>e&1){auto [a,b]=edges[e];out|=1u<<idx(p[a],p[b]);}return out;}
int main(){int e=0;for(int i=0;i<N;i++)for(int j=i+1;j<N;j++)edges[e++]={i,j};assert(e==E);
 array<uint64_t,E+1> immunity_counts{};unordered_set<Mask> minima;
 for(Mask graph=0;graph<(1u<<E);++graph){int ne=__builtin_popcount(graph);if(ne>14)continue;
  if(!has_two_cut(graph)){immunity_counts[ne]++;if(ne==14)minima.insert(graph);}
 }
 for(int k=0;k<=13;k++)assert(immunity_counts[k]==0);
 assert(immunity_counts[14]==15015 && minima.size()==15015);
 unordered_set<Mask> union_orbits;
 array<uint64_t,10> orbit_sizes{};
 for(int r=0;r<10;r++){
   assert(__builtin_popcount(reps[r])==14 && !has_two_cut(reps[r]));
   array<int,N> p; iota(p.begin(),p.end(),0);
   unordered_set<Mask> orbit;
   do{Mask m=permute(reps[r],p);orbit.insert(m);}while(next_permutation(p.begin(),p.end()));
   orbit_sizes[r]=orbit.size();
   for(auto m:orbit){assert(minima.count(m)==1);assert(union_orbits.insert(m).second);}
 }
 assert(union_orbits.size()==15015 && union_orbits==minima);
 constexpr array<uint64_t,10> expected_orbits={105,2520,2520,1260,2520,1260,630,2520,1260,420};
 assert(orbit_sizes==expected_orbits);
 cout<<"EXHAUSTIVE_LABELLED_7_VERTEX_2_CUT_CHECK_PASS\n";
 cout<<"NO_IMMUNE_GRAPHS_AT_0_THROUGH_13_EDGES_PASS\n";
 cout<<"MINIMUM_14_EDGE_IMMUNE_COUNT_15015_PASS\n";
 cout<<"TEN_DISJOINT_ISOMORPHISM_ORBITS_PASS\n";
 cout<<"ORBIT_SIZES";for(auto z:orbit_sizes)cout<<" "<<z;cout<<"\nVERIFY_OK\n";
}
