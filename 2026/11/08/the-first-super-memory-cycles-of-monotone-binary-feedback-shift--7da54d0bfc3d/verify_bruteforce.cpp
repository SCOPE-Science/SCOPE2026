// Exhaustive finite certificate for periodic binary words whose length-n
// cyclic factors form an antichain in the Boolean lattice.
// Build: c++ -std=c++17 -O2 verify_bruteforce.cpp -o verify_bruteforce
// Run:   ./verify_bruteforce
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

static int choose(int n, int k) {
    int out = 1;
    for (int j = 1; j <= k; ++j) out = out * (n - j + 1) / j;
    return out;
}
static string rotation_min(const string &s) {
    string best = s;
    for (int i = 1; i < (int)s.size(); ++i) {
        string z = s.substr(i) + s.substr(0, i);
        if (z < best) best = z;
    }
    return best;
}
static bool admissible(uint32_t bits, int n, int L) {
    uint32_t seen[20] = {0};
    for (int i = 0; i < L; ++i) {
        uint32_t window = 0;
        for (int j = 0; j < n; ++j)
            window = 2 * window + ((bits >> ((i + j) % L)) & 1u);
        for (int h = 0; h < i; ++h)
            if ((seen[h] & window) == seen[h] ||
                (seen[h] & window) == window) return false;
        seen[i] = window;
    }
    return true;
}
int main() {
    const vector<string> expected7 = {"0001011", "0001101", "0010111", "0011101"};
    const vector<string> expected9 = {"001010011", "001101011"};
    for (int n = 1; n <= 6; ++n) {
        int bound = choose(n, n / 2);
        for (int L = n + 1; L <= bound; ++L) {
            uint64_t total = 0;
            vector<string> canonical;
            for (uint32_t bits = 0; bits < (1u << L); ++bits) {
                if (!admissible(bits, n, L)) continue;
                ++total;
                string w;
                for (int j = 0; j < L; ++j)
                    w += char('0' + ((bits >> j) & 1u));
                if (w == rotation_min(w)) canonical.push_back(w);
            }
            sort(canonical.begin(), canonical.end());
            const uint64_t expected = (n == 6 && L == 7) ? 28 :
                                      (n == 6 && L == 9) ? 18 : 0;
            assert(total == expected);
            assert(total == (uint64_t)L * canonical.size());
            if (n == 6 && L == 7) assert(canonical == expected7);
            else if (n == 6 && L == 9) assert(canonical == expected9);
            else assert(canonical.empty());
            cout << "n=" << n << " L=" << L << " rooted=" << total
                 << " necklaces=" << canonical.size() << '\n';
        }
    }
    cout << "BRUTEFORCE_VERIFY_OK\n";
}
