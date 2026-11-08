// Independent finite certificate checker for three-by-three Mallows markets.
// Build: c++ -O2 -std=c++17 verify_independent.cpp -o verify_independent
// Run: ./verify_independent
#include <array>
#include <algorithm>
#include <cassert>
#include <iostream>
#include <numeric>
using namespace std;
using Tri = array<int,3>;
using Histogram = array<long long,19>;

int inversions(const Tri& r) {
  int out=0;
  for(int x=0;x<3;x++) for(int y=x+1;y<3;y++) if(r[x]>r[y]) out++;
  return out;
}

bool stable(const array<array<int,3>,6>& rank,
            const Tri& matching) {
  Tri partners{-1,-1,-1};
  for(int m=0;m<3;m++) partners[matching[m]]=m;
  // Each distinct man/woman pair not assigned to one another can block.
  for(int m=0;m<3;m++) for(int w=0;w<3;w++) {
    if(w==matching[m]) continue;
    if(rank[m][w] < rank[m][matching[m]] &&
       rank[3+w][m] < rank[3+w][partners[w]]) return false;
  }
  return true;
}

int main() {
  array<Tri,6> perms{};
  array<int,6> inv{};
  Tri p{0,1,2};
  for(int i=0;i<6;i++) {
    perms[i]=p;
    inv[i]=inversions(p);
    next_permutation(p.begin(),p.end());
  }
  array<Histogram,4> hist{};
  Histogram diagonal{};
  long long checked=0;
  // Interpret all integers in [0,6^6) as six independent ranking indices.
  for(int mask=0;mask<46656;mask++) {
    int code=mask,degree=0;
    array<array<int,3>,6> rank{};
    for(int agent=0;agent<6;agent++) {
      int idx=code%6; code/=6;
      degree+=inv[idx];
      for(int pos=0;pos<3;pos++) rank[agent][perms[idx][pos]]=pos;
    }
    int count=0;
    bool diag=false;
    for(const Tri& mu:perms) {
      if(stable(rank,mu)) {
        count++;
        if(mu==Tri{0,1,2}) diag=true;
      }
    }
    assert(count>=1 && count<=3 && degree>=0 && degree<=18);
    hist[count][degree]++;
    if(diag) diagonal[degree]++;
    checked++;
  }
  const Histogram exp1{1,12,68,266,758,1642,2821,4006,4872,5188,4872,4006,2821,1642,758,266,68,12,1};
  const Histogram exp2{0,0,4,20,82,284,734,1410,2051,2314,2051,1410,734,284,82,20,4,0,0};
  const Histogram exp3{0,0,0,0,0,6,44,128,229,278,229,128,44,6,0,0,0,0,0};
  const Histogram expdiag{1,8,36,112,266,510,822,1142,1389,1482,1389,1142,822,510,266,112,36,8,1};
  assert(checked==46656);
  assert(hist[1]==exp1 && hist[2]==exp2 && hist[3]==exp3 && diagonal==expdiag);
  auto total=[](const Histogram& v) {return accumulate(v.begin(),v.end(),0LL);};
  assert(total(hist[1])==34080 && total(hist[2])==11484);
  assert(total(hist[3])==1092 && total(diagonal)==10054);
  cout<<"PASS: independent C++ enumeration of 46,656 labeled profiles and"
        <<" all 6 candidate matchings; complete integer coefficients agree."<<endl;
}
