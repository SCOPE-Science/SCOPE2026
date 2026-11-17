// Direct rotor-step simulation, independent of the functional-graph algorithm.
// Build: g++ -std=c++17 -O2 -Wall -Wextra check_direct.cpp -o check_direct
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;

bool is_recurrent(int n, uint32_t rotor, int chip) {
    // A rotor graph is a unicycle iff it has exactly one directed cycle,
    // the chip belongs to it, and every vertex leads into it.
    vector<int> visited(n, -1);
    int cur = chip;
    for (int t = 0; t <= n; ++t) {
        if (visited[cur] >= 0) {
            if (cur != chip) return false;
            break;
        }
        visited[cur] = t;
        int dir = (rotor & (1U << cur)) ? 1 : -1;
        cur = (cur + n + dir) % n;
    }
    for (int i = 0; i < n; ++i) {
        if (visited[i] >= 0) continue;
        vector<bool> seen(n, false);
        int p = i;
        while (visited[p] < 0 && !seen[p]) {
            seen[p] = true;
            int dir = (rotor & (1U << p)) ? 1 : -1;
            p = (p + n + dir) % n;
        }
        if (seen[p]) return false; // extra cycle
    }
    return true;
}

int predicted(int n, uint32_t rotors, int chip) {
    int k = __builtin_popcount(rotors);
    int c = (chip - k + n) % n;
    int b0 = (rotors >> c) & 1;
    int s = 0, r = 0, ell = n;
    for (int j = 1; j < n; ++j) {
        int b = (rotors >> ((c + j) % n)) & 1;
        s += j*b;
        if (b) r = j;
        else if (ell == n) ell = j;
    }
    return 2*s - k*k + (b0 ? ell : -r);
}

int main() {
    for (int n = 3; n <= 13; ++n) {
        long long total = 0, maxima = 0;
        int max_delay = -1;
        const uint32_t masks = 1U << n;
        for (uint32_t initial = 0; initial < masks; ++initial) {
            for (int start = 0; start < n; ++start) {
                int d = predicted(n, initial, start);
                assert(d >= 0 && d <= (n-1)*(n-2)/2);
                uint32_t rotor = initial;
                int chip = start;
                for (int t = 0; t < d; ++t) {
                    if (is_recurrent(n, rotor, chip)) {
                        cerr << "Premature recurrence " << n << ' ' << initial << ' ' << start << ' ' << t << '\n';
                        return 1;
                    }
                    rotor ^= 1U << chip;
                    chip = (chip + n + ((rotor >> chip) & 1 ? 1 : -1)) % n;
                }
                if (!is_recurrent(n, rotor, chip)) {
                    cerr << "No recurrence at predicted entry " << n << ' ' << initial << ' ' << start << '\n';
                    return 1;
                }
                total += d;
                if (d > max_delay) {max_delay=d;maxima=1;}
                else if (d == max_delay) ++maxima;
            }
        }
        if (max_delay != (n-1)*(n-2)/2 || maxima != 2*n) return 1;
        cout << "n=" << n << " states=" << (n*(1<<n)) << " max=" << max_delay
             << " maximizers=" << maxima << " total_delay=" << total << '\n';
    }
    cout << "PASS direct rotor simulation, n=3..13\n";
    return 0;
}
