// Independent explicit trace checker for even-length circular intervals.
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <set>
#include <vector>
using namespace std;

int main() {
  for (int n = 4; n <= 20; n += 2) {
    set<uint64_t> hs = {0ULL, (1ULL << n) - 1};
    for (int length = 2; length < n; length += 2)
      for (int start = 0; start < n; ++start) {
        uint64_t h = 0;
        for (int j = 0; j < length; ++j) h |= 1ULL << ((start + j) % n);
        hs.insert(h);
      }
    long long face[5] = {1,0,0,0,0};
    for (int k = 1; k <= 4; ++k) {
      vector<int> s(k);
      for (int j = 0; j < k; ++j) s[j] = j;
      while (true) {
        uint64_t mask = 0;
        for (int x : s) mask |= 1ULL << x;
        set<uint64_t> traces;
        for (uint64_t h : hs) traces.insert(h & mask);
        bool shattered = traces.size() == (1u << k);
        bool triple_consec = false;
        if (k == 3) {
          for (int j = 0; j < n; ++j) {
            int cnt = 0;
            for (int x : s) if (x == j || x == (j + 1)%n || x == (j+2)%n) ++cnt;
            if (cnt == 3) triple_consec = true;
          }
        }
        bool predicted = k <= 2 || (k == 3 && !triple_consec);
        assert(predicted == shattered);
        if (shattered) ++face[k];
        int j = k - 1;
        while (j >= 0 && s[j] == n-k+j) --j;
        if (j < 0) break;
        ++s[j];
        for (int l = j+1; l < k; ++l) s[l] = s[l-1]+1;
      }
    }
    auto c2 = n * (n-1) / 2;
    auto c3 = n * (n-1) * (n-2) / 6;
    assert(face[1] == n && face[2] == c2 && face[3] == c3-n && face[4] == 0);
    assert((int)hs.size() == 2+n*(n/2-1));
    cout << "n=" << n << " hypotheses=" << hs.size() << " face=";
    for (int i=0;i<5;++i) cout << (i?",":"") << face[i];
    cout << "\n";
  }
  cout << "CPP_FINITE_CHECKS_PASS\n";
}
