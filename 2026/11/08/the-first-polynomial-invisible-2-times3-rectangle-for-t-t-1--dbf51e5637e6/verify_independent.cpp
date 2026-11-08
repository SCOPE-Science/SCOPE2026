// Independent exact enumeration of the smallest polynomial-invisible 2-by-3 rectangle.
// Compile: c++ -O2 -std=c++17 verify_independent.cpp -o verify_independent
#include <algorithm>
#include <cassert>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;
using ll = long long;

static vector<ll> moduli(int x) {
    const ll f = 1LL * x * (x + 1);
    vector<ll> d;
    for (ll t = 1; t < x; ++t) d.push_back(f / gcd(f, t * (t + 1)));
    sort(d.begin(), d.end());
    d.erase(unique(d.begin(), d.end()), d.end());
    vector<ll> minimal;
    for (ll q : d) {
        bool dominated = false;
        for (ll z : minimal) if (q % z == 0) dominated = true;
        if (!dominated) minimal.push_back(q);
    }
    return minimal;
}
static vector<ll> combined(int x) {
    auto left = moduli(x), right = moduli(x + 1);
    vector<ll> all;
    for (ll p : left) for (ll q : right) {
        const ll m = lcm(p, q);
        if (find(all.begin(), all.end(), m) == all.end()) all.push_back(m);
    }
    return all;
}
static vector<vector<ll>> compatible(int x) {
    auto all = combined(x);
    vector<vector<ll>> answer;
    for (ll m0 : all) for (ll m1 : all) {
        if (gcd(m0, m1) != 1) continue;
        for (ll m2 : all) {
            if (gcd(m1, m2) == 1 && gcd(m0, m2) <= 2) {
                answer.push_back({m0, m1, m2});
            }
        }
    }
    return answer;
}
int main() {
    for (int x = 1; x < 230; ++x) assert(compatible(x).empty());
    auto answers = compatible(230);
    assert(answers.size() == 2);
    sort(answers.begin(), answers.end());
    assert(answers[0] == vector<ll>({22, 105, 1334}));
    assert(answers[1] == vector<ll>({1334, 105, 22}));
    for (ll b : {759044LL, 781724LL}) {
        for (int x : {230, 231}) for (ll y : {b, b+1, b+2}) {
            bool invisible = false;
            for (ll t = 1; t < x; ++t)
                if ((y * t * (t + 1)) % (1LL*x*(x+1)) == 0) invisible = true;
            assert(invisible);
        }
    }
    cout << "INDEPENDENT_VERIFY_OK first_x=230 compatible_triples=2" << '\n';
}
