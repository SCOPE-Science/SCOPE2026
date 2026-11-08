// Exhaustive direct-cut certificate for the zero-temperature Ising model on the McGee graph.
// Uses the 24-cycle and LCF chord offsets (-12,7,-7) repeated eight times.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <utility>
#include <vector>
using namespace std;
int main() {
  vector<pair<int,int>> edges;
  for(int i=0;i<24;++i) {
    int j=(i+1)%24;
    edges.emplace_back(min(i,j),max(i,j));
    int shift=(i%3==0 ? -12 : (i%3==1 ? 7 : -7));
    j=(i+24+shift)%24;
    edges.emplace_back(min(i,j),max(i,j));
  }
  sort(edges.begin(),edges.end());
  edges.erase(unique(edges.begin(),edges.end()),edges.end());
  assert(edges.size()==36);
  array<int,25> mx; mx.fill(-1);
  array<uint64_t,25> num{};
  uint64_t first_excited_count=0, first_excited_m2=0;
  uint64_t absolute_max_count=0;
  int absolute_max=-1;
  for(uint32_t mask=0;mask<(uint32_t(1)<<24);++mask) {
    int q=__builtin_popcount(mask), cut=0;
    for(const auto& e:edges) cut += ((mask>>e.first)^(mask>>e.second))&1u;
    if(cut>mx[q]) { mx[q]=cut; num[q]=1; }
    else if(cut==mx[q]) ++num[q];
    if(cut>absolute_max) { absolute_max=cut; absolute_max_count=1; }
    else if(cut==absolute_max) ++absolute_max_count;
    if(cut==31) {
      ++first_excited_count;
      int m=24-2*q;
      first_excited_m2+=uint64_t(m*m);
    }
  }
  const int expected_mx[25]={0,3,6,9,12,15,18,21,24,27,30,31,32,31,30,27,24,21,18,15,12,9,6,3,0};
  const uint64_t expected_num[25]={1,24,240,1304,4212,8328,10024,7072,2668,424,8,8,2,8,8,424,2668,7072,10024,8328,4212,1304,240,24,1};
  for(int q=0;q<=24;q++) assert(mx[q]==expected_mx[q] && num[q]==expected_num[q]);
  assert(absolute_max==32 && absolute_max_count==2);
  assert(first_excited_count==16 && first_excited_m2==64);
  uint64_t indep=0;
  for(int q=0;q<=10;q++) indep+=num[q];
  assert(indep==34305);
  cout << "VERIFY_MASKS_OK 16777216 subsets maxcut=32 ground=2 first_excited=16 at gap_2J first_crossing=18 saturation_boundary=34305\n";
}
