// Exact enumeration of unlabeled enemy-cycle coalition partitions.
// A coalition is an independent set of the enemy graph C_n.
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
using U64 = unsigned long long;
static U64 power(U64 a, unsigned b) { U64 v=1; for(unsigned i=0;i<b;++i) v*=a; return v; }
struct Tester {
 int n; std::vector<unsigned> groups; U64 best=0, best_count=0, valid=0;
 void dfs(int v) {
  if(v==n) {
   ++valid; U64 w=1;
   for(unsigned mask:groups) {
    int size=__builtin_popcount(mask);
    if(size==1) {w=0;break;}
    w*=power(size-1,size);
   }
   if(w>best) {best=w;best_count=0;}
   if(w==best) ++best_count;
   return;
  }
  unsigned bit=1u<<v;
  for(size_t j=0;j<groups.size();++j) {
   unsigned old=groups[j];
   if(v>0 && (old & (bit>>1))) continue;
   if(v==n-1 && (old&1u)) continue;
   groups[j]=old|bit; dfs(v+1); groups[j]=old;
  }
  groups.push_back(bit);dfs(v+1);groups.pop_back();
 }
};
int main() {
 for(int n=3;n<=13;++n) {
  Tester t; t.n=n; t.dfs(0);
  U64 w=0,c=0;
  if(n%2==0) {
   int k=n/2;
   w=power(k-1,n);c=1;
  } else if(n>=7) {
   int k=(n-1)/2;
   w=power(k-1,k)*power(k-2,k-1);
   c=(k==3)?2*n:2ULL*n*(k-1);
  } else {
   w=0; c=t.best_count;
  }
  std::cout<<"n="<<n<<" feasible_partitions="<<t.valid
           <<" Nash_product="<<t.best<<" optimizers="<<t.best_count<<"\n";
  if(t.best!=w || t.best_count!=c) return 1;
 }
 std::cout<<"EXACT_ENUMERATION_OK\n";
}
