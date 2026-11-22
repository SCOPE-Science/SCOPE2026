#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <queue>
#include <set>
#include <unordered_set>
#include <vector>
using namespace std;

// Complete and deterministic exhaustive certificate for the incidence graph
// on the two- and three-element subsets of {0,1,2,3,4}.
static int bits(uint32_t v) {return __builtin_popcount(v);}
static constexpr uint32_t FULL=(1u<<20)-1u;

int main(){
  vector<int> subsets;
  for(int x=0;x<32;++x) if(bits(x)==2 || bits(x)==3)subsets.push_back(x);
  assert(subsets.size()==20);
  array<int,32> id;id.fill(-1);
  for(int i=0;i<20;++i)id[subsets[i]]=i;
  array<uint32_t,20> closed{};
  for(int i=0;i<20;++i) {
    closed[i]|=1u<<i;
    for(int j=0;j<20;++j) if(i!=j){
      int a=subsets[i], b=subsets[j];
      if((a&b)==a || (a&b)==b)closed[i]|=1u<<j;
    }
    assert(bits(closed[i])==4);
  }
  vector<uint32_t> delta;
  for(int i=0;i<20;++i)for(int j=i+1;j<20;++j)
    delta.push_back(closed[i]^closed[j]);
  assert(delta.size()==190);

  auto valid=[&](uint32_t s){
    for(uint32_t n:closed)if(bits(n&s)<2)return false;
    for(uint32_t d:delta)if(bits(d&s)<2)return false;
    return true;
  };
  array<int,21> hist{};
  unordered_set<uint32_t> valid_sets;
  set<uint32_t> optima;
  for(uint32_t s=0;s<=FULL;++s){
    if(!valid(s))continue;
    valid_sets.insert(s);hist[bits(s)]++;
    if(bits(s)==12)optima.insert(s);
  }
  const array<int,21> expected_counts={0,0,0,0,0,0,0,0,0,0,0,0,
                                         15,120,680,1824,2155,940,190,20,1};
  assert(hist==expected_counts && valid_sets.size()==5945 && optima.size()==15);

  // Every optimum is the complement of both incidence-side copies of the
  // four edges of a 4-cycle in K5. A K4 has three 4-cycles (delete one
  // of its three disjoint-edge matchings).
  set<uint32_t> geometric;
  for(int quad=0;quad<32;++quad)if(bits(quad)==4){
    vector<int> edges;
    for(int e=0;e<32;++e)if(bits(e)==2 && (e&quad)==e)edges.push_back(e);
    for(size_t i=0;i<edges.size();++i)for(size_t j=i+1;j<edges.size();++j){
      if(edges[i]&edges[j])continue;
      uint32_t omitted=0;
      for(int e:edges)if(e!=edges[i] && e!=edges[j]) {
        assert(id[e]>=0 && id[31^e]>=0);
        omitted|=1u<<id[e];omitted|=1u<<id[31^e];
      }
      geometric.insert(FULL^omitted);
    }
  }
  assert(geometric.size()==15 && geometric==optima);

  // Natural S5 permutations are automorphisms and are transitive on 4-cycles.
  array<int,5> p={0,1,2,3,4};
  set<uint32_t> orbit;
  do {
    uint32_t transformed=0;
    for(int i=0;i<20;++i)if(*optima.begin()&(1u<<i)){
      int target=0;
      for(int b=0;b<5;++b)if(subsets[i]&(1<<b))target|=1<<p[b];
      transformed|=1u<<id[target];
    }
    orbit.insert(transformed);
  }while(next_permutation(p.begin(),p.end()));
  assert(orbit==optima);

  // TAR budget b: each intermediate code has cardinality <=b; adjacent
  // codes differ by exactly one position, and every intermediate remains
  // redundant. Measure how many of the 15 minima are reachable.
  auto reachable_minima=[&](int b) {
    unordered_set<uint32_t> seen;
    queue<uint32_t> q;
    uint32_t start=*optima.begin();
    seen.insert(start);q.push(start);
    while(!q.empty()){
      uint32_t s=q.front();q.pop();
      for(int i=0;i<20;++i){
        uint32_t t=s^(1u<<i);
        if(bits(t)>b || !valid_sets.count(t) || !seen.insert(t).second)continue;
        q.push(t);
      }
    }
    int cnt=0;for(auto s:optima)cnt+=seen.count(s);
    return cnt;
  };
  assert(reachable_minima(12)==1 && reachable_minima(13)==1 &&
         reachable_minima(14)==1 && reachable_minima(15)==15);
  cout<<"VERIFY_OK: 5945 codes; 15 four-cycle optima; TAR threshold 15\n";
}
