// Finite exact certificate for geodesic transversals of the five-cube.
// Build: c++ -O2 -std=c++17 verify.cpp -o verify
// Run: ./verify
#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdio>
#include <set>
#include <vector>
using namespace std;

static int weight(unsigned x) { int n=0;while(x){n+=x&1u;x>>=1;}return n; }
static uint32_t sphere(int center) {
  uint32_t m=0;for(int v=0;v<32;++v)if(weight((unsigned)(v^center))==2)m|=uint32_t(1)<<v;return m;
}
static bool hits(uint32_t m,const vector<uint32_t>& paths){
  for(uint32_t p:paths)if((p&m)==0)return false;
  return true;
}
static uint64_t count_normalized(int size,const vector<uint32_t>& paths,
                                 const set<uint32_t>& allowed, uint64_t expected_total,
                                 uint64_t expected_good){
  // Enumerate all sets of size `size` containing vertex zero exactly once.
  int a[10];for(int j=0;j<size-1;++j)a[j]=j+1;
  uint64_t total=0,good=0;
  while(true){
    uint32_t mask=1;
    for(int j=0;j<size-1;++j)mask|=uint32_t(1)<<a[j];
    if(hits(mask,paths)){
      if(!allowed.count(mask)){printf("UNEXPECTED_HITTING_SET size=%d mask=%u\n",size,mask);return 0;}
      ++good;
    }
    ++total;
    int j=size-2;
    while(j>=0 && a[j]==31-((size-2)-j))--j;
    if(j<0)break;
    ++a[j];for(int k=j+1;k<size-1;++k)a[k]=a[k-1]+1;
  }
  if(total!=expected_total || good!=expected_good){
    printf("BAD_ENUMERATION size=%d tested=%llu good=%llu\n",size,
      (unsigned long long)total,(unsigned long long)good);return 0;
  }
  printf("NORMALIZED_SIZE_%d tested=%llu valid=%llu PASS\n",size,
    (unsigned long long)total,(unsigned long long)good);
  return good+1;
}
int main(){
  set<uint32_t> unique;
  array<int,5> perm={0,1,2,3,4};
  do {
    for(int start=0;start<32;++start){
      int v=start;uint32_t mask=uint32_t(1)<<v;
      for(int bit:perm){v^=1<<bit;mask|=uint32_t(1)<<v;}
      if(v!=(start^31) || weight(mask)!=6){puts("INVALID_PATH");return 1;}
      unique.insert(mask);
    }
  }while(next_permutation(perm.begin(),perm.end()));
  if(unique.size()!=1920){puts("PATH_COUNT_FAILURE");return 1;}
  vector<uint32_t> relevant,all(unique.begin(),unique.end());
  for(uint32_t p:all)if((p&1)==0)relevant.push_back(p);
  if(relevant.size()!=1560){puts("NORMALIZED_PATH_COUNT_FAILURE");return 1;}
  printf("MAXIMAL_GEODESIC_SETS %zu PASS\n",all.size());

  set<uint32_t> expected;
  for(int x=0;x<32;++x){uint32_t s=sphere(x);
    if(weight(s)!=10 || !hits(s,all)){puts("SHELL_WITNESS_FAILURE");return 1;}
    expected.insert(s);
  }
  if(expected.size()!=32){puts("SHELL_UNIQUENESS_FAILURE");return 1;}
  set<uint32_t> normalized_expected;
  for(uint32_t s:expected)if(s&1)normalized_expected.insert(s);
  if(normalized_expected.size()!=10){puts("NORMALIZED_SHELL_COUNT_FAILURE");return 1;}
  printf("SHELL_CONSTRUCTIONS 32 DISTINCT ALL_HIT PASS\n");

  if(count_normalized(9,relevant,{},7888725ULL,0)!=1)return 1;
  if(count_normalized(10,relevant,normalized_expected,20160075ULL,10)!=11)return 1;
  printf("CLASSIFICATION_ALL_32_MINIMA_PASS\n");
  printf("GT_Q5_10_PASS\n");
  return 0;
}
