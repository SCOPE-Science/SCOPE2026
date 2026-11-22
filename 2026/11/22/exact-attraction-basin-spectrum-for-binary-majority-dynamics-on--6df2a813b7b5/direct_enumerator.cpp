// Direct graph-level majority enumeration on two explicitly presented graphs.
// Build: c++ -std=c++17 -O2 -Wall -Wextra direct_enumerator.cpp -o check && ./check
#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <map>
#include <stdexcept>
#include <utility>
#include <vector>
using namespace std;
using Edge=pair<int,int>;

static const vector<Edge> PETERSEN={
 {0,1},{0,4},{0,5},{1,2},{1,6},{2,3},{2,7},{3,4},{3,8},{4,9},
 {5,7},{5,8},{6,8},{6,9},{7,9}};
static const vector<Edge> DESARGUES={
 {0,1},{0,19},{0,5},{1,2},{1,16},{2,3},{2,11},{3,4},{3,14},
 {4,5},{4,9},{5,6},{6,7},{6,15},{7,8},{7,18},{8,9},{8,13},
 {9,10},{10,11},{10,19},{11,12},{12,13},{12,17},{13,14},
 {14,15},{15,16},{16,17},{17,18},{18,19}};

void census(const char* name, int n, const vector<Edge>& edges) {
 vector<uint32_t> neigh(n,0);
 for(auto [a,b]:edges){
  if(a<0||b<0||a>=n||b>=n||a==b)throw runtime_error("edge");
  neigh[a] |= (1u<<b); neigh[b] |= (1u<<a);
 }
 for(int i=0;i<n;i++) if(__builtin_popcount(neigh[i])!=3) throw runtime_error("not cubic");
 auto F=[&](uint32_t x)->uint32_t{
  uint32_t y=0;
  for(int i=0;i<n;i++) if(__builtin_popcount(x&neigh[i])>=2) y |= (1u<<i);
  return y;
 };
 map<pair<int,int>,uint64_t> counts;
 map<pair<int,uint32_t>,uint64_t> basin;
 for(uint32_t x=0;x<(1u<<n);++x){
  uint32_t y=x;
  int entry=0;
  while(F(F(y))!=y){
    y=F(y);
    ++entry;
    if(entry>n*n+2)throw runtime_error("entry bound exceeded");
  }
  int period=(F(y)==y?1:2);
  ++counts[{entry,period}];
  ++basin[{period, (period==1? y: min(y,F(y)))}];
 }
 cout<<name<<" vertices="<<n<<" states="<<(1u<<n)<<"\n";
 for(auto [key,v]:counts) cout<<"entry="<<key.first<<" period="<<key.second<<" count="<<v<<"\n";
 map<pair<int,uint64_t>,int> hist;
 for(auto [key,v]:basin) ++hist[{key.first,v}];
 for(auto [key,v]:hist) cout<<"period="<<key.first<<" basin_size="<<key.second<<" orbit_count="<<v<<"\n";
}
int main(){census("Petersen",10,PETERSEN);census("Desargues",20,DESARGUES);}
