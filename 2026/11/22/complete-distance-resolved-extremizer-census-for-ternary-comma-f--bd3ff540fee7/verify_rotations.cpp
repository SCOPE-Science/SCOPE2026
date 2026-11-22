// Independent exact census by length-three rotation orbits.
// Compile: c++ -O2 -std=c++17 verify_rotations.cpp -o verify_rotations
// Run: ./verify_rotations
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <set>
#include <string>
#include <vector>
using namespace std;

static bool valid(const vector<string>& code, int d) {
    for (size_t i = 0; i < code.size(); ++i) {
        for (size_t j = i + 1; j < code.size(); ++j) {
            int distance = 0;
            for (int k = 0; k < 3; ++k) distance += code[i][k] != code[j][k];
            if (distance < d) return false;
        }
    }
    set<string> chosen(code.begin(), code.end());
    for (const string& a : code) for (const string& b : code) {
        if (chosen.count(a.substr(1, 2) + b.substr(0, 1))) return false;
        if (chosen.count(a.substr(2, 1) + b.substr(0, 2))) return false;
    }
    return true;
}

int main() {
    set<string> seen;
    vector<array<string, 3>> orbit;
    for (char a = '0'; a <= '2'; ++a)
        for (char b = '0'; b <= '2'; ++b)
            for (char c = '0'; c <= '2'; ++c) {
                string w = string(1, a) + b + c;
                if (seen.count(w)) continue;
                string r = w.substr(1) + w[0];
                string s = r.substr(1) + r[0];
                seen.insert(w); seen.insert(r); seen.insert(s);
                if (w != r && r != s && s != w) orbit.push_back({w, r, s});
            }
    assert(orbit.size() == 8);
    const int assignments = 65536; // 4^8: omit or choose one of three rotations
    array<int, 9> count2{}, count3{};
    for (int index = 0; index < assignments; ++index) {
        int value = index;
        vector<string> code;
        for (const auto& o : orbit) {
            int digit = value % 4;
            value /= 4;
            if (digit) code.push_back(o[digit - 1]);
        }
        if (valid(code, 2)) ++count2[code.size()];
        if (valid(code, 3)) ++count3[code.size()];
    }
    const array<int, 9> expect2{1, 24, 174, 336, 132, 0, 0, 0, 0};
    const array<int, 9> expect3{1, 24, 66, 12, 0, 0, 0, 0, 0};
    assert(count2 == expect2 && count3 == expect3);
    for (int d = 2; d <= 3; ++d) {
        const auto& counts = d == 2 ? count2 : count3;
        cout << "distance " << d << ": ";
        for (int k = 0; k < 9; ++k) cout << k << '=' << counts[k] << ' ';
        cout << '\n';
    }
    cout << "ALL CHECKS PASSED\n";
}
