// Exhaustive integer certificate for the six-variable monotone-support Walsh census.
// Requires a C++17 compiler.  The two Fourier computations use distinct algorithms:
// direct 64-entry butterfly and character sums of two 32-entry cofactors.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <vector>
using namespace std;
using U = uint64_t;
int main() {
  vector<U> mon = {0,1}; int half = 1;
  // Verify the first exceptional dimension: no even-support invertible
  // convolution occurs for dimensions one through five.
  vector<U> small = {0,1}; int small_width=1;
  for (int d=1;d<=5;d++) {
    vector<U> next;
    for(U a:small)for(U b:small)if((a&~b)==0)
      next.push_back(a|(b<<small_width));
    small.swap(next);small_width*=2;
    U even_nonsingular=0;
    for(U mask:small) if ((__builtin_popcountll(mask)&1)==0) {
      vector<int> w(small_width);
      for(int x=0;x<small_width;x++)w[x]=(mask>>x)&1;
      for(int k=0;k<d;k++)for(int x=0;x<small_width;x++)
        if(!(x&(1<<k))) {
          int y=x|(1<<k),a=w[x],b=w[y];w[x]=a+b;w[y]=a-b;
        }
      if(all_of(w.begin(),w.end(),[](int z){return z!=0;}))
        even_nonsingular++;
    }
    if(even_nonsingular!=0) return 6;
  }
  if (small.size()!=7581) return 7;
  for (int d=1; d<=5; ++d) {
    vector<U> next;
    for (U a:mon) for (U b:mon) if ((a&~b)==0) next.push_back(a|(b<<half));
    mon.swap(next); half*=2;
  }
  if (mon.size()!=7581 || half!=32) return 1;
  vector<array<int,32>> char5(mon.size());
  vector<int> size5(mon.size());
  for (size_t i=0; i<mon.size(); ++i) {
    size5[i]=__builtin_popcountll(mon[i]);
    for (int u=0;u<32;u++) {
      int s=0;
      for (int x=0;x<32;x++) if ((mon[i]>>x)&1)
        s+=__builtin_parity((unsigned)(x&u)) ? -1:1;
      char5[i][u]=s;
    }
  }
  U total=0, odd=0, even=0, even_invertible=0;
  map<int,U> even_invertible_weights,even_invertible_gaps;
  for (size_t ia=0;ia<mon.size();ia++) for (size_t ib=0;ib<mon.size();ib++) {
    if ((mon[ia]&~mon[ib])!=0) continue;
    ++total;
    const U truth=mon[ia]|(mon[ib]<<32);
    const int support_size=size5[ia]+size5[ib];
    array<int,64> direct{};
    for (int x=0;x<64;x++) direct[x]=(truth>>x)&1;
    for (int k=0;k<6;k++) for (int x=0;x<64;x++) if (!(x&(1<<k))) {
      const int j=x|(1<<k), a=direct[x], b=direct[j];
      direct[x]=a+b;direct[j]=a-b;
    }
    int gap=65, zeros=0;
    for (int u=0;u<32;u++) {
      // Cofactor recursion independently evaluates the 6-variable character sum.
      if (direct[u]!=char5[ia][u]+char5[ib][u]) return 2;
      if (direct[u+32]!=char5[ia][u]-char5[ib][u]) return 3;
    }
    for (int val:direct) {
      if (val==0) zeros++;
      else gap=min(gap,abs(val));
    }
    if (support_size&1) {
      ++odd;
      // This exact gap-one assertion is part of the finite certificate.
      if (zeros!=0||gap!=1) return 4;
    } else {
      ++even;
      if (!zeros) {
        ++even_invertible;
        ++even_invertible_weights[support_size];
        ++even_invertible_gaps[gap];
      }
    }
  }
  const map<int,U> expected_weights={{10,15},{14,195},{18,225},
    {22,886},{26,4275},{30,6270},{34,6270},{38,4275},
    {42,886},{46,225},{50,195},{54,15}};
  if (total!=7828354||odd!=3913460||even!=3914894||
      even_invertible!=23732||even_invertible_weights!=expected_weights||
      even_invertible_gaps!=map<int,U>{{2,23732}}) return 5;
  cout<<"MONOTONE_SIX_EXACT_WALSH_CENSUS_PASS\n";
  cout<<"functions="<<total<<" odd="<<odd<<" even="<<even
      <<" even_invertible="<<even_invertible<<" total_invertible="
      <<odd+even_invertible<<"\n";
  for (auto [w,num]:even_invertible_weights)
    cout<<"weight="<<w<<" count="<<num<<"\n";
  return 0;
}
