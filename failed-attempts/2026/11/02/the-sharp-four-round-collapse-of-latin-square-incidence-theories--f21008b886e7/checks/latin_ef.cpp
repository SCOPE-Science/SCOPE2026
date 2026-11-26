// Finite Ehrenfeucht--Fraisse type computation for two three-sorted Latin incidences.
// The two order-four squares are addition modulo four and bitwise XOR on two bits.
// No algebraic-library dependencies: C++17 standard library only.
#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

struct VHash {
    size_t operator()(const vector<int>& v) const {
        uint64_t x = 1469598103934665603ULL;
        for (int k : v) { x ^= uint64_t(k + 3); x *= 1099511628211ULL; }
        return size_t(x);
    }
};

// The 12 elements are rows [0,4), columns [4,8), symbols [8,12).
// Pack unary sorts, pairwise equality, and every admissible ordered M-atom.
uint64_t atom(int index, int length, int square) {
    int x[6] = {};
    for (int i = length - 1; i >= 0; --i) { x[i] = index % 12; index /= 12; }
    uint64_t out = 0; int bit = 0;
    for (int i = 0; i < length; ++i) {
        out |= (uint64_t(x[i] / 4) << bit); bit += 2;
    }
    for (int i = 0; i < length; ++i)
        for (int j = i + 1; j < length; ++j) {
            if (x[i] == x[j]) out |= (uint64_t(1) << bit);
            ++bit;
        }
    for (int i = 0; i < length; ++i) if (x[i] < 4)
        for (int j = 0; j < length; ++j) if (4 <= x[j] && x[j] < 8)
            for (int k = 0; k < length; ++k) if (8 <= x[k]) {
                int r = x[i], c = x[j] - 4, s = x[k] - 8;
                bool yes = square == 0 ? (r + c) % 4 == s : (r ^ c) == s;
                if (yes) out |= (uint64_t(1) << bit);
                ++bit;
            }
    return out;
}

bool equivalent(int q) {
    int size = 1;
    for (int j = 0; j < q; ++j) size *= 12;
    vector<int> current[2] = {vector<int>(size), vector<int>(size)};
    unordered_map<uint64_t, int> atomic_ids;
    int types = 0;
    for (int i = 0; i < size; ++i)
        for (int s = 0; s != 2; ++s) {
            uint64_t v = atom(i, q, s);
            auto ins = atomic_ids.emplace(v, types);
            if (ins.second) ++types;
            current[s][i] = ins.first->second;
        }
    // A tuple with remaining rank r>0 is classified by the SET of
    // (r-1)-types of all its one-point extensions, in a common codebook.
    // Its own atomic type is recovered by restricting any extension type.
    for (int k = q - 1; k >= 0; --k) {
        int count = int(current[0].size()) / 12;
        vector<int> next[2] = {vector<int>(count), vector<int>(count)};
        unordered_map<vector<int>, int, VHash> codes;
        int new_types = 0;
        for (int i = 0; i < count; ++i)
            for (int s = 0; s < 2; ++s) {
                vector<int> ext;
                for (int z = 0; z < 12; ++z) ext.push_back(current[s][12*i + z]);
                sort(ext.begin(), ext.end());
                ext.erase(unique(ext.begin(), ext.end()), ext.end());
                auto ins = codes.emplace(ext, new_types);
                if (ins.second) ++new_types;
                next[s][i] = ins.first->second;
            }
        current[0].swap(next[0]); current[1].swap(next[1]);
    }
    return current[0][0] == current[1][0];
}

int main() {
    for (int q = 1; q <= 5; ++q) {
        bool eq = equivalent(q);
        bool expected = q <= 4;
        cout << "rank=" << q << " C4_vs_V4=" << (eq ? "EQUIVALENT" : "DISTINGUISHABLE") << '\n';
        if (eq != expected) return 1;
    }
    cout << "all_expected_outcomes=PASS\n";
    return 0;
}
