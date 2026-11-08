#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;

// Check the exact joint law of baseline-pivotal swaps and matching survival
// in a complete market with common strict priorities on one side.
// Full rankings and all independent adjacent-swap locations are enumerated.
int main() {
  for (int n = 2; n <= 4; ++n) {
    vector<array<int, 4>> permutations;
    array<int, 4> p = {0, 1, 2, 3};
    do { permutations.push_back(p); }
    while (next_permutation(p.begin(), p.begin() + n));
    const int P = static_cast<int>(permutations.size());
    const int S = n - 1;
    uint64_t total = 0, survived = 0;
    vector<uint64_t> pivotal_counts(n + 1, 0);
    uint64_t num_profiles = 1, num_swaps = 1;
    for (int i = 0; i < n; ++i) { num_profiles *= P; num_swaps *= S; }
    for (uint64_t profile = 0; profile < num_profiles; ++profile) {
      array<array<int, 4>, 4> lists{};
      uint64_t code = profile;
      for (int i = 0; i < n; ++i) {
        lists[i] = permutations[code % P];
        code /= P;
      }
      int remaining = (1 << n) - 1;
      vector<int> baseline(n);
      for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
          int v = lists[i][j];
          if (remaining & (1 << v)) {
            baseline[i] = v;
            remaining ^= (1 << v);
            break;
          }
        }
      }
      for (uint64_t swaps = 0; swaps < num_swaps; ++swaps) {
        uint64_t code2 = swaps;
        int perturbed_remaining = (1 << n) - 1;
        int pivots = 0;
        bool unchanged = true;
        for (int i = 0; i < n; ++i) {
          const int s = static_cast<int>(code2 % S);
          code2 /= S;
          int chosen = -1;
          for (int j = 0; j < n; ++j) {
            const int idx = j == s ? s + 1 : (j == s + 1 ? s : j);
            const int v = lists[i][idx];
            if (perturbed_remaining & (1 << v)) { chosen = v; break; }
          }
          assert(chosen >= 0);
          if (chosen != baseline[i]) unchanged = false;
          int original_remaining = 0;
          for (int j = i; j < n; ++j) original_remaining |= 1 << baseline[j];
          const int a = lists[i][s], z = lists[i][s + 1];
          if ((original_remaining & (1 << a)) && (original_remaining & (1 << z))) {
            bool none_earlier = true;
            for (int j = 0; j < s; ++j)
              if (original_remaining & (1 << lists[i][j])) none_earlier = false;
            if (none_earlier) ++pivots;
          }
          perturbed_remaining ^= (1 << chosen);
        }
        survived += unchanged;
        ++pivotal_counts[pivots];
        ++total;
      }
    }
    cout << "n=" << n << " permutations=" << P << " total=" << total
         << " unchanged=" << survived << " pivotal_counts=";
    for (int i = 0; i <= n; ++i)
      cout << pivotal_counts[i] << (i == n ? "" : " ");
    cout << "\n";
    assert(total == num_profiles * num_swaps);
    assert(pivotal_counts[0] == survived);
    if (n == 2) assert(survived == 0 && pivotal_counts[1] == total);
    if (n == 3) {
      assert(survived * 3 == total);
      assert(pivotal_counts[1] * 2 == total);
      assert(pivotal_counts[2] * 6 == total);
    }
    if (n == 4) {
      assert(survived * 12 == total * 5);
      assert(pivotal_counts[1] * 72 == total * 31);
      assert(pivotal_counts[2] * 36 == total * 5);
      assert(pivotal_counts[3] * 72 == total);
    }
  }
}
