// Exhaustive independent fixed-identity exact-cover checker for the cyclic
// adjacent-position-swap metric on permutations of {0,1,2,3,4}.
// C++17 standard library only.  The two-word masks cover all 120 vertices.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <vector>
using namespace std;
using Word = uint64_t;
using Perm = array<int, 5>;

array<array<Word, 2>, 120> balls{};
array<vector<int>, 120> by_vertex{};
uint64_t nodes = 0, dead_ends = 0, solutions = 0;
int bit_count(Word bits) {
  int k = 0;
  while (bits) { bits &= bits - 1; ++k; }
  return k;
}
vector<int> one_solution;

bool collides(int center, Word lo, Word hi) {
  return (balls[center][0] & lo) || (balls[center][1] & hi);
}
void recurse(Word lo, Word hi, vector<int> &selected) {
  ++nodes;
  const int count = bit_count(lo) + bit_count(hi);
  if (count == 120) {
    assert(selected.size() == 20);
    ++solutions;
    one_solution = selected;
    return;
  }
  vector<int> best;
  bool have = false;
  for (int vertex = 0; vertex < 120; ++vertex) {
    if ((vertex < 64 ? lo : hi) & (Word(1) << (vertex % 64))) continue;
    vector<int> eligible;
    for (int center : by_vertex[vertex])
      if (!collides(center, lo, hi)) eligible.push_back(center);
    if (eligible.empty()) { ++dead_ends; return; }
    if (!have || eligible.size() < best.size()) {
      best = eligible;
      have = true;
      if (best.size() == 1) break;
    }
  }
  assert(have);
  for (int center : best) {
    selected.push_back(center);
    recurse(lo | balls[center][0], hi | balls[center][1], selected);
    selected.pop_back();
  }
}

int main() {
  vector<Perm> P;
  Perm cur{0, 1, 2, 3, 4};
  do { P.push_back(cur); } while (next_permutation(cur.begin(), cur.end()));
  assert(P.size() == 120);
  map<Perm, int> index;
  for (int i = 0; i < 120; ++i) index[P[i]] = i;
  for (int i = 0; i < 120; ++i) {
    auto add = [&](int j) { balls[i][j / 64] |= Word(1) << (j % 64); };
    add(i);
    for (int j = 0; j < 5; ++j) {
      Perm changed = P[i];
      swap(changed[j], changed[(j + 1) % 5]);
      add(index.at(changed));
    }
    assert(bit_count(balls[i][0]) +
           bit_count(balls[i][1]) == 6);
    for (int j = 0; j < 120; ++j)
      if (balls[i][j / 64] & (Word(1) << (j % 64)))
        by_vertex[j].push_back(i);
  }
  for (const auto &v : by_vertex) assert(v.size() == 6);
  vector<int> selected{0};
  recurse(balls[0][0], balls[0][1], selected);
  assert(nodes == 41 && dead_ends == 4 && solutions == 1);
  vector<Perm> result;
  for (int j : one_solution) result.push_back(P[j]);
  sort(result.begin(), result.end());
  vector<Perm> affine;
  for (int a = 1; a < 5; ++a)
    for (int b = 0; b < 5; ++b) {
      Perm w{};
      for (int i = 0; i < 5; ++i) w[i] = (a * i + b) % 5;
      affine.push_back(w);
    }
  sort(affine.begin(), affine.end());
  assert(result == affine);
  cout << "n_permutations=120; balls_size=6; nodes=" << nodes
       << "; dead_ends=" << dead_ends << "; normalized_solutions="
       << solutions << "; affine_solution=TRUE; PASS\n";
}
