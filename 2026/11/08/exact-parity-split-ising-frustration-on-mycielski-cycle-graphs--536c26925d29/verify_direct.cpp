// Independent direct enumeration of all physical spins on Mycielskian cycles.
// Run: g++ -O3 -std=c++17 verify_direct.cpp -o verify_direct && ./verify_direct
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <vector>
#include <utility>
using namespace std;
int main() {
 for(int n=4;n<=11;n++) {
  vector<pair<int,int>> edges;
  for(int i=0;i<n;i++) {
   int j=(i+1)%n;
   edges.emplace_back(i,j);
   edges.emplace_back(n+i,j);
   edges.emplace_back(n+j,i);
   edges.emplace_back(n+i,2*n);
  }
  assert((int)edges.size()==4*n);
  long long minE=1000000, ways=0;
  map<int,long long> mag;
  const uint64_t maxmask=uint64_t(1)<<(2*n+1);
  for(uint64_t mask=0;mask<maxmask;mask++) {
   int cuts=0;
   for(auto e:edges) cuts+=((mask>>e.first)^(mask>>e.second))&1ULL;
   int en=4*n-2*cuts;
   if(en>minE) continue;
   int m=2*__builtin_popcountll(mask)-(2*n+1);
   if(en<minE){minE=en;ways=0;mag.clear();}
   ways++;mag[m]++;
  }
  int expectedE = n%2 ? -3*(n-1) : -3*n;
  long long expectedWays = n%2 ? 2*n : 4;
  assert(minE==expectedE && ways==expectedWays);
  assert(mag.size()==2 && mag[-1]==expectedWays/2 && mag[1]==expectedWays/2);
  cout<<"PASS n="<<n<<" edges="<<edges.size()<<" configs="<<maxmask
      <<" min_energy="<<minE<<" ground_count="<<ways
      <<" magnetizations=-1:"<<mag[-1]<<",+1:"<<mag[1]<<'\n';
 }
}
