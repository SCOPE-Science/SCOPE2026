// Standalone exhaustive certificate for minimum locating-dominating codes in GP(12,5).
// Build: c++ -O3 -std=c++17 check_all_masks.cpp -o check_all_masks
// Run: ./check_all_masks  (expected: VERIFY_FULL_OK)
#include <array>
#include <bitset>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <set>
using namespace std;
int main(){
  constexpr int V=24;
  array<uint32_t,V> nbr{};
  auto edge=[&](int u,int v){nbr[u]|=uint32_t(1)<<v; nbr[v]|=uint32_t(1)<<u;};
  for(int i=0;i<12;i++){edge(i,(i+1)%12);edge(i,i+12);edge(i+12,12+(i+5)%12);}
  for(uint32_t x:nbr)assert(__builtin_popcount(x)==3);
  set<uint32_t> found;
  uint64_t tested=0;
  for(uint32_t x=0; x<(uint32_t(1)<<V); ++x){
    if(__builtin_popcount(x)>8)continue;
    tested++;
    // Distinct nonzero open-neighborhood signatures on the omitted vertices.
    array<uint32_t,V> seen{}; int used=0;bool good=true;
    for(int v=0;v<V;v++)if(!(x&(uint32_t(1)<<v))){
      uint32_t m=nbr[v]&x;
      if(!m){good=false;break;}
      for(int j=0;j<used;j++)if(seen[j]==m){good=false;break;}
      if(!good)break;
      seen[used++]=m;
    }
    if(good){assert(__builtin_popcount(x)==8);found.insert(x);}
  }
  auto makeA=[&](int i){uint32_t x=0;for(int j:{4,6,9,11})x|=uint32_t(1)<<((i+j)%12);for(int j=0;j<4;j++)x|=uint32_t(1)<<(12+(i+j)%12);return x;};
  auto makeB=[&](int r,int s){uint32_t x=0;for(int j=0;j<12;j++){if(j%3==r)x|=uint32_t(1)<<j;if(j%3==s)x|=uint32_t(1)<<(12+j);}return x;};
  set<uint32_t> expected;
  for(int i=0;i<12;i++)expected.insert(makeA(i));
  for(int r=0;r<3;r++)for(int s=0;s<3;s++)if(r!=s)expected.insert(makeB(r,s));
  assert(found.size()==18 && expected.size()==18 && found==expected);
  // Every subset with fewer than 8 landmarks was explicitly tested.
  cout<<"VERIFY_FULL_OK tested="<<tested<<" minima="<<found.size()<<"\n";
}
