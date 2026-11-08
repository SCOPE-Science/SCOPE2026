#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <limits>
#include <vector>
using namespace std;
int main() {
  constexpr int N=24;
  vector<array<int,2>> edges;
  // Labels are (p,b) with p in {0,1,2}, b a 3-bit sign mask.
  // Within each b, the three p-vertices form one triangular face.
  for(int b=0;b<8;b++) for(int p=0;p<3;p++)
    for(int q=p+1;q<3;q++) edges.push_back({8*p+b,8*q+b});
  // The nontriangle edges form six independent four-cycles.
  for(int p=0;p<3;p++) for(int b=0;b<8;b++)
    for(int q=0;q<3;q++) if(q!=p) {
      int nb=b^(1<<q);
      if(b<nb) edges.push_back({8*p+b,8*p+nb});
    }
  assert(edges.size()==48);
  array<vector<int>,N> nb;
  for(auto e:edges){nb[e[0]].push_back(e[1]);nb[e[1]].push_back(e[0]);}
  for(const auto &v:nb) assert(v.size()==4);
  array<int,N+1> mn; mn.fill(numeric_limits<int>::max());
  array<uint64_t,N+1> cnt{};
  int energy=48, k=0;
  uint32_t previous=0;
  for(uint32_t t=0;t<(1u<<N);t++) {
    uint32_t mask=t^(t>>1);
    if(t) {
      int i=__builtin_ctz(mask^previous);
      bool nowDown=(mask>>i)&1u;
      int sum=0;
      for(int j:nb[i]) sum += (mask&(1u<<j))?-1:1;
      energy += 2*(nowDown?-1:1)*sum;
      k += nowDown?1:-1;
    }
    if(energy<mn[k]) {mn[k]=energy;cnt[k]=1;}
    else if(energy==mn[k]) ++cnt[k];
    previous=mask;
  }
  const array<int,N+1> expectedEnergy={48,40,32,24,16,8,0,-8,-16,-20,-24,-28,-32,-28,-24,-20,-16,-8,0,8,16,24,32,40,48};
  const array<uint64_t,N+1> expectedCount={1,24,228,1104,2940,4368,3536,1440,234,552,444,144,18,144,444,552,234,1440,3536,4368,2940,1104,228,24,1};
  for(int i=0;i<=N;i++) {
    if(mn[i]!=expectedEnergy[i] || cnt[i]!=expectedCount[i]) {
      cerr<<"mismatch at k="<<i<<": "<<mn[i]<<", "<<cnt[i]<<"\n";
      return 1;
    }
  }
  cout << "Complete 2^24 Ising enumeration: PASS (25 magnetization sectors).\n";
}
