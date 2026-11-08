#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>
using namespace std;

static unsigned reverse5(unsigned x) {
    unsigned r = 0;
    for (int i = 0; i < 5; ++i) { r = (r << 1) | ((x >> i) & 1U); }
    return r;
}
static string necklace(const string &s) {
    string ans = s;
    for (size_t i = 1; i < s.size(); ++i) ans = min(ans, s.substr(i) + s.substr(0, i));
    return ans;
}
static unsigned read5(unsigned word, int n, int i) {
    unsigned v = 0;
    for (int j = 0; j < 5; ++j) v = (v << 1) | ((word >> ((i + j) % n)) & 1U);
    return v;
}
int main() {
    map<unsigned, unsigned> class_of_representative;
    unsigned class_id[32];
    for (unsigned v = 0; v < 32; ++v) {
        unsigned representative = min(v, reverse5(v));
        auto it = class_of_representative.find(representative);
        if (it == class_of_representative.end()) {
            unsigned next = class_of_representative.size();
            class_of_representative.emplace(representative, next);
            class_id[v] = next;
        } else class_id[v] = it->second;
    }
    assert(class_of_representative.size() == 20);
    unsigned number_n = 0;
    for (int n = 5; n <= 20; ++n) {
        set<string> words;
        map<uint32_t, string> masks;
        for (unsigned x = 0; x < (1U << n); ++x) {
            uint32_t seen = 0; bool distinct = true;
            for (int i = 0; i < n; ++i) {
                unsigned v = read5(x, n, i);
                uint32_t bit = 1U << class_id[v];
                if (seen & bit) { distinct = false; break; }
                seen |= bit;
            }
            if (distinct) {
                string s; for (int i = 0; i < n; ++i) s += char('0' + ((x >> i) & 1U));
                string c = necklace(s); words.insert(c); masks[seen] = c;
            }
        }
        // A family has size at most one if all possible masks intersect.
        bool pair_conflict = true;
        for (auto a = masks.begin(); a != masks.end(); ++a)
            for (auto b = next(a); b != masks.end(); ++b)
                if (!(a->first & b->first)) pair_conflict = false;
        assert(pair_conflict);
        cout << "n=" << n << " count=" << words.size()
             << " capacity=" << (words.empty() ? 0 : 1) << '\n';
        for (const string &s : words) cout << s << '\n';
        number_n += words.size();
    }
    assert(number_n == 20);
    cout << "DIRECT_COMPLETE_OK total=" << number_n << '\n';
}
