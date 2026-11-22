// Exact finite enumeration for distance-one to distance-three changes in
// finite integer metric spaces; all counts use integer arithmetic.
// C++17: g++ -O2 -std=c++17 artifacts/verify.cpp -o verify && ./verify
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdio>
#include <cstdlib>
using namespace std;

int main() {
  for (int n = 2; n <= 6; ++n) {
    int edge_i[15], edge_j[15], edges = 0;
    for (int i = 0; i < n; ++i)
      for (int j = i + 1; j < n; ++j) {
        edge_i[edges] = i;
        edge_j[edges] = j;
        ++edges;
      }

    int triples[20][3], ntriples = 0;
    for (int i = 0; i < n; ++i)
      for (int j = i + 1; j < n; ++j)
        for (int k = j + 1; k < n; ++k) {
          int ids[3] = {-1, -1, -1};
          for (int e = 0; e < edges; ++e) {
            if (edge_i[e] == i && edge_j[e] == j) ids[0] = e;
            if (edge_i[e] == i && edge_j[e] == k) ids[1] = e;
            if (edge_i[e] == j && edge_j[e] == k) ids[2] = e;
          }
          for (int a = 0; a < 3; ++a) assert(ids[a] >= 0);
          for (int a = 0; a < 3; ++a) triples[ntriples][a] = ids[a];
          ++ntriples;
        }

    int limit = 1;
    for (int e = 1; e < edges; ++e) limit *= 3;
    int switchable = 0, positive = 0, zero = 0, negative = 0;
    int min_delta = 100000, max_delta = -100000;
    int internal_pairs[3] = {};
    for (int serial = 0; serial < limit; ++serial) {
      int d[15], s = serial;
      d[0] = 1;                  // distinguished distance d(0,1)
      for (int e = 1; e < edges; ++e) {
        d[e] = 1 + s % 3;
        s /= 3;
      }
      assert(s == 0);
      bool metric = true;
      for (int t = 0; t < ntriples && metric; ++t) {
        int e0 = triples[t][0], e1 = triples[t][1], e2 = triples[t][2];
        int x = d[e0], y = d[e1], z = d[e2];
        if (x > y + z || y > x + z || z > x + y) {
          metric = false;
          break;
        }
        // Retest the triple after replacing just d(0,1) by 3.
        if (e0 == 0) x = 3;
        if (e1 == 0) y = 3;
        if (e2 == 0) z = 3;
        if (x > y + z || y > x + z || z > x + y) metric = false;
      }
      if (!metric) continue;
      ++switchable;

      int g1[6] = {}, g3[6] = {};
      for (int e = 0; e < edges; ++e) {
        int i = edge_i[e], j = edge_j[e];
        if (d[e] == 1) {
          g1[i] |= 1 << j;
          g1[j] |= 1 << i;
        }
        if (d[e] == 3) {
          g3[i] |= 1 << j;
          g3[j] |= 1 << i;
        }
      }

      // Independent method: choose the distance-one support L; it must
      // be independent in G_3. Every vertex outside L and its G_1-neighborhood
      // may independently receive distance three instead of two.
      auto count_types = [&]() -> int {
        int count = 0;
        for (int mask = 0; mask < (1 << n); ++mask) {
          int blocked = mask;
          bool admissible = true;
          for (int v = 0; v < n; ++v) {
            if (!(mask & (1 << v))) continue;
            if (g3[v] & mask) {
              admissible = false;
              break;
            }
            blocked |= g1[v];
          }
          if (admissible)
            count += 1 << (n - __builtin_popcount((unsigned)blocked));
        }
        return count;
      };
      int before = count_types();
      g1[0] &= ~(1 << 1);
      g1[1] &= ~1;
      g3[0] |= 1 << 1;
      g3[1] |= 1;
      int after = count_types();
      int change = after - before;
      min_delta = min(min_delta, change);
      max_delta = max(max_delta, change);
      if (change < 0) {
        ++negative;
        if (n == 6) {
          assert(change == -2);
          int group_x = 0, group_y = 0;
          for (int v = 2; v < 6; ++v) {
            int av = 0, bv = 0;
            for (int e = 1; e < edges; ++e) {
              if (edge_i[e] == 0 && edge_j[e] == v) av = d[e];
              if (edge_i[e] == 1 && edge_j[e] == v) bv = d[e];
            }
            assert((av == 1 && bv == 2) || (av == 2 && bv == 1));
            if (av == 1) group_x |= 1 << v;
            else group_y |= 1 << v;
          }
          assert(__builtin_popcount((unsigned)group_x) == 2);
          assert(__builtin_popcount((unsigned)group_y) == 2);
          int inside_twos = 0;
          for (int e = 1; e < edges; ++e) {
            int i = edge_i[e], j = edge_j[e];
            if (i < 2) continue;
            if (((group_x & (1 << i)) && (group_y & (1 << j))) ||
                ((group_y & (1 << i)) && (group_x & (1 << j)))) {
              assert(d[e] == 1);
            } else {
              assert(d[e] == 1 || d[e] == 2);
              if (d[e] == 2) ++inside_twos;
            }
          }
          assert(inside_twos >= 0 && inside_twos <= 2);
          ++internal_pairs[inside_twos];
        }
      } else if (change == 0) {
        ++zero;
      } else {
        ++positive;
      }
    }
    printf("n=%d switchable=%d positive=%d zero=%d negative=%d "
           "delta_min=%d delta_max=%d", n, switchable, positive, zero,
           negative, min_delta, max_delta);
    if (n == 6)
      printf(" internal_twos=%d,%d,%d", internal_pairs[0],
             internal_pairs[1], internal_pairs[2]);
    puts("");
    assert(switchable == positive + zero + negative);
    if (n <= 5) assert(negative == 0 && zero == 0);
    if (n == 6) assert(negative == 24 && zero == 96);
  }
  puts("VERIFY_OK");
}
