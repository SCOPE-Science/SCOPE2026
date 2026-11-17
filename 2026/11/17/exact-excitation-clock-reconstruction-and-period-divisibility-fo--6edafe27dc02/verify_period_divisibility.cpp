// Exhaustive finite verification for the three-state CCA/GHM period relation.
// C++17 standard library only. Build: c++ -O3 -std=c++17 verify_period_divisibility.cpp -o verify_period_divisibility
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;

static vector<int> periods(const vector<int>& nxt) {
  const int total = (int)nxt.size();
  vector<int> ans(total, 0), mark(total, -1), route;
  route.reserve(total);
  for (int start = 0; start < total; ++start) {
    if (ans[start]) continue;
    route.clear();
    int y = start;
    while (ans[y] == 0 && mark[y] == -1) {
      mark[y] = (int)route.size();
      route.push_back(y);
      y = nxt[y];
    }
    const int p = ans[y] ? ans[y] : (int)route.size() - mark[y];
    for (int x : route) ans[x] = p;
    for (int x : route) mark[x] = -1;
  }
  return ans;
}

int main() {
  uint64_t graph_count = 0, state_count = 0;
  for (int n = 1; n <= 6; ++n) {
    const int edges = n * (n - 1) / 2;
    int p3[7] = {1,1,1,1,1,1,1};
    for (int i = 1; i <= n; ++i) p3[i] = 3 * p3[i - 1];
    const int total = p3[n];
    vector<int> masks[3];
    for (int j = 0; j < 3; ++j) masks[j].resize(total);
    for (int x = 0; x < total; ++x) {
      for (int i = 0; i < n; ++i)
        masks[(x / p3[i]) % 3][x] |= 1 << i;
    }
    const uint64_t graph_total = 1ULL << edges;
    for (uint64_t graph = 0; graph < graph_total; ++graph) {
      int adj[6] = {0,0,0,0,0,0};
      int e = 0;
      for (int j = 0; j < n; ++j)
        for (int i = 0; i < j; ++i, ++e)
          if (graph & (1ULL << e)) {
            adj[i] |= 1 << j;
            adj[j] |= 1 << i;
          }
      vector<int> c(total), g(total);
      for (int code = 0; code < total; ++code) {
        int cc = code, gg = code;
        int bm0 = masks[0][code], bm1 = masks[1][code], bm2 = masks[2][code];
        for (int v = 0; v < n; ++v) {
          int cur = (code / p3[v]) % 3;
          int nextc = cur;
          if (cur == 0 && (adj[v] & bm1)) nextc = 1;
          if (cur == 1 && (adj[v] & bm2)) nextc = 2;
          if (cur == 2 && (adj[v] & bm0)) nextc = 0;
          int nextg = cur == 0 ? ((adj[v] & bm1) != 0) : (cur + 1) % 3;
          cc += p3[v] * (nextc - cur);
          gg += p3[v] * (nextg - cur);
        }
        c[code] = cc;
        g[code] = gg;
      }
      auto pc = periods(c), pg = periods(g);
      for (int x = 0; x < total; ++x) {
        if (pc[x] % pg[x] != 0) {
          cerr << "FAIL n=" << n << " graph_mask=" << graph
               << " code=" << x << " cca=" << pc[x]
               << " ghm=" << pg[x] << '\n';
          return 1;
        }
        ++state_count;
      }
      ++graph_count;
    }
    cout << "PASS labelled graphs n=" << n << ": " << graph_total
         << " graphs, " << total << " colorings each" << '\n';
  }
  cout << "PASS period divisibility for " << graph_count
       << " labelled graphs and " << state_count
       << " graph-color pairs" << '\n';
}
