// Independent exact check via even-parity binary words of length five.
#include <algorithm>
#include <array>
#include <bitset>
#include <cassert>
#include <iostream>
#include <map>
#include <vector>
using namespace std;

int main() {
    vector<int> v;
    for (int x = 0; x < 32; ++x)
        if (__builtin_popcount((unsigned)x) % 2 == 0) v.push_back(x);
    assert(v.size() == 16);
    bool A[16][16] = {};
    for (int i = 0; i < 16; ++i)
        for (int j = 0; j < 16; ++j)
            A[i][j] = __builtin_popcount((unsigned)(v[i] ^ v[j])) == 4;
    for (int i = 0; i < 16; ++i) {
        int d = 0;
        for (int j = 0; j < 16; ++j) d += A[i][j];
        assert(d == 5 && !A[i][i]);
        for (int j = i + 1; j < 16; ++j) {
            int c = 0;
            for (int k = 0; k < 16; ++k) c += A[i][k] && A[j][k];
            assert(c == (A[i][j] ? 0 : 2));
        }
    }
    for (int closed = 0; closed <= 1; ++closed) {
        vector<vector<vector<int>>> faces(5);
        for (int mask = 0; mask < (1 << 16); ++mask) {
            vector<int> s;
            for (int i = 0; i < 16; ++i) if (mask & (1 << i)) s.push_back(i);
            int z = (int)s.size();
            if (z > 4) continue;
            vector<bool> seen(1 << z, false);
            int nseen = 0;
            for (int center = 0; center < 16; ++center) {
                int trace = 0;
                for (int t = 0; t < z; ++t)
                    if (A[center][s[t]] || (closed && center == s[t])) trace |= 1 << t;
                if (!seen[trace]) { seen[trace] = true; ++nseen; }
            }
            bool hit = nseen == (1 << z);
            if (z == 3) {
                int edges = A[s[0]][s[1]] + A[s[0]][s[2]] + A[s[1]][s[2]];
                bool common = false;
                for (int center = 0; center < 16; ++center)
                    common |= A[center][s[0]] && A[center][s[1]] && A[center][s[2]];
                assert(hit == ((edges == 0 && common) || (closed && edges == 2)));
            }
            if (hit) faces[z].push_back(s);
        }
        const vector<int> expected = closed ? vector<int>{1,16,120,320,0} : vector<int>{1,16,80,160,0};
        for (int k = 0; k <= 4; ++k) assert((int)faces[k].size() == expected[k]);
        map<pair<int,int>, int> edge_id;
        for (int i = 0; i < (int)faces[2].size(); ++i)
            edge_id[{faces[2][i][0],faces[2][i][1]}] = i;
        array<bitset<120>, 120> pivots;
        array<bool, 120> used{};
        int rank = 0;
        for (auto const &tri : faces[3]) {
            bitset<120> x;
            for (int i = 0; i < 3; ++i)
                for (int j = i + 1; j < 3; ++j)
                    x.set(edge_id.at({tri[i], tri[j]}));
            for (int j = (int)faces[2].size() - 1; j >= 0; --j) {
                if (!x[j]) continue;
                if (used[j]) x ^= pivots[j];
                else { used[j] = true; pivots[j] = x; ++rank; break; }
            }
        }
        assert(rank == (closed ? 104 : 65));
        int h1 = (int)faces[2].size() - 15 - rank;
        int h2 = (int)faces[3].size() - rank;
        assert(h1 == (closed ? 1 : 0));
        assert(h2 == (closed ? 216 : 95));
        cout << (closed ? "closed" : "open") << ": f=[";
        for (int k = 0; k <= 4; ++k) cout << (k ? "," : "") << expected[k];
        cout << "], rank_d2=" << rank << ", mod2_betti_1_2=(" << h1 << "," << h2 << ")\n";
    }
    cout << "FOLDED_VERIFY_PASS\n";
}
