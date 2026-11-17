#include <iostream>
#include <cstdint>
using namespace std;

// Independent enumeration of all binary majority equilibria on GP(n,k).
uint64_t count(int n,int k) {
  uint64_t ans=0, total=1ULL<<(2*n);
  for (uint64_t m=0;m<total;++m) {
    bool stable=true;
    for (int i=0;i<n && stable;++i) {
      int a=(m>>i)&1, b=(m>>(n+i))&1;
      int across_outer=((m>>((i+n-1)%n))&1)+((m>>((i+1)%n))&1)+b;
      int across_inner=((m>>(n+(i+n-k)%n))&1)+((m>>(n+(i+k)%n))&1)+a;
      if ((across_outer>=2)!=bool(a) || (across_inner>=2)!=bool(b)) stable=false;
    }
    ans+=stable;
  }
  return ans;
}
int main() {
  const uint64_t expected[5][3]={
     {32,32,32}, {48,48,72}, {76,76,52}, {124,118,124}, {202,158,224}
  };
  for (int n=7;n<=11;++n) {
    cout << "n=" << n;
    for (int k=1;k<=3;++k) {
      uint64_t got=count(n,k);
      cout << " k=" << k << ":" << got;
      if(got!=expected[n-7][k-1]) {cerr << "Mismatch\n"; return 1;}
    }
    cout << "\n";
  }
  cout << "All independent exhaustive majority checks passed.\n";
}
