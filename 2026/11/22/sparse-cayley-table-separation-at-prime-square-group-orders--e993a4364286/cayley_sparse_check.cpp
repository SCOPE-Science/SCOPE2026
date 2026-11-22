// Independent finite sanity checks for sparse multiplication constraints.
// This program is not the proof of the all-prime determinant bound.
// Compile: g++ -O2 -std=c++17 cayley_sparse_check.cpp -o cayley_check
#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>
using namespace std;

using Matrix = vector<vector<int>>;
long long pattern_counts[4] = {};
long long checked_differences[4] = {};

int modular_rank(Matrix a, int prime) {
    if (a.empty()) return 0;
    const int rows = (int)a.size(), cols = (int)a[0].size();
    for (auto &row : a) for (auto &x : row) x = (x % prime + prime) % prime;
    int pivot = 0;
    for (int c = 0; c < cols && pivot < rows; ++c) {
        int r = pivot;
        while (r < rows && a[r][c] == 0) ++r;
        if (r == rows) continue;
        swap(a[r], a[pivot]);
        int inv = 1;
        while (inv * a[pivot][c] % prime != 1) ++inv;
        for (int j = c; j < cols; ++j) a[pivot][j] = a[pivot][j] * inv % prime;
        for (int i = 0; i < rows; ++i) {
            if (i == pivot) continue;
            int s = a[i][c];
            for (int j = c; j < cols; ++j)
                a[i][j] = (a[i][j] - s * a[pivot][j] % prime + prime) % prime;
        }
        ++pivot;
    }
    return pivot;
}

void inspect(const vector<int> &part, int cells, const vector<int> &primes) {
    ++pattern_counts[cells];
    int labels = *max_element(part.begin(), part.end()) + 1;
    Matrix rel(cells, vector<int>(labels));
    for (int r = 0; r < cells; ++r) {
        rel[r][part[3*r]]++;
        rel[r][part[3*r+1]]++;
        rel[r][part[3*r+2]]--;
    }
    int reference = modular_rank(rel, 17);
    for (int p : primes) assert(modular_rank(rel, p) == reference);
    for (int a = 0; a < labels; ++a) for (int b = a+1; b < labels; ++b) {
        ++checked_differences[cells];
        Matrix augmented = rel;
        vector<int> d(labels);
        d[a] = 1; d[b] = -1;
        augmented.push_back(d);
        int larger = modular_rank(augmented, 17);
        for (int p : primes) assert(modular_rank(augmented, p) == larger);
    }
}

void partitions(vector<int> &part, int cells, int mx, const vector<int> &primes) {
    if ((int)part.size() == 3*cells) { inspect(part, cells, primes); return; }
    for (int x = 0; x <= mx+1; ++x) {
        part.push_back(x);
        partitions(part, cells, max(mx,x), primes);
        part.pop_back();
    }
}

void check_chain(int p, vector<int> chain) {
    assert(chain.front() == 1 && chain.back() == p+1);
    for (int i = 1; i < (int)chain.size(); ++i) {
        bool found = false;
        for (int j = 0; j < i; ++j) for (int k = 0; k < i; ++k)
            if (chain[j] + chain[k] == chain[i]) found = true;
        assert(found && chain[i] < p*p);
        assert(chain[i] > chain[i-1]);
    }
    for (int i = 0; i < (int)chain.size(); ++i)
        for (int j = i+1; j < (int)chain.size(); ++j)
            assert(chain[i] % (p*p) != chain[j] % (p*p));
    assert((chain.back() - chain.front()) % p == 0);
    cout << "p=" << p << " upper_cells=" << chain.size()-1 << '\n';
}

int main() {
    for (auto item : vector<pair<int,vector<int>>>{{1,{5,7}}, {2,{5,7}}, {3,{11,13}}}) {
        vector<int> part{0};
        partitions(part, item.first, 0, item.second);
    }
    assert(pattern_counts[1] == 5);
    assert(pattern_counts[2] == 203);
    assert(pattern_counts[3] == 21147);
    for (int k=1;k<=3;k++)
        cout << "cells=" << k << " patterns=" << pattern_counts[k]
             << " label_pairs=" << checked_differences[k] << " OK\n";
    check_chain(3, {1,2,4});
    check_chain(5, {1,2,4,6});
    check_chain(7, {1,2,4,8});
    check_chain(11, {1,2,3,6,12});
    check_chain(17, {1,2,4,8,16,18});
    check_chain(19, {1,2,4,5,10,20});
    check_chain(23, {1,2,3,6,12,24});
    check_chain(31, {1,2,4,8,16,32});
    cout << "SPARSE_CAYLEY_PRIME_SQUARE_CHECKS_OK\n";
}
