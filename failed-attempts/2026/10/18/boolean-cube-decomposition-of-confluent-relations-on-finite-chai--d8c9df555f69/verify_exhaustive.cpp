// Independent all-binary-matrix census for square sizes 1 through 5.
// Compile: c++ -O3 -std=c++17 verify_exhaustive.cpp -o verify_exhaustive
// Run: ./verify_exhaustive
#include <cstdint>
#include <cstdio>
int main() {
  const long long expected[] = {2,9,118,4849,697066};
  for (int n=1; n<=5; ++n) {
    long long count=0;
    std::uint64_t bound=1ULL << (n*n);
    for (std::uint64_t mask=0; mask<bound; ++mask) {
      bool ok=true; int previous=-1;
      for (int i=0; i<n; ++i) {
        unsigned row=(mask >> (i*n)) & ((1u<<n)-1);
        int last=row?31-__builtin_clz(row):-1;
        if (last<previous) {ok=false; break;}
        previous=last;
      }
      if (!ok) continue;
      previous=-1;
      for (int j=0; j<n; ++j) {
        unsigned col=0;
        for (int i=0; i<n; ++i)
          col |= ((mask>>(i*n+j)) & 1u) << i;
        int last=col?31-__builtin_clz(col):-1;
        if (last<previous) {ok=false; break;}
        previous=last;
      }
      if (ok) ++count;
    }
    std::printf("n=%d count=%lld expected=%lld\n",n,count,expected[n-1]);
    if (count!=expected[n-1]) return 1;
  }
  std::puts("EXHAUSTIVE_OK");
  return 0;
}
