// Complete labeled three-symbol prefix search with direct character comparisons.
#include <algorithm>
#include <cassert>
#include <iostream>
#include <map>
#include <string>
#include <vector>

struct State { std::string word, trace; };

bool suffix_has_overlap(const std::string& s) {
    const int n = int(s.size());
    for (int p = 1; 2*p+1 <= n; ++p) {
        bool periodic = true;
        for (int j = 0; j <= p; ++j) {
            if (s[n-2*p-1+j] != s[n-p-1+j]) { periodic = false; break; }
        }
        if (periodic) return true;
    }
    return false;
}

char suffix_curl(const std::string& s) {
    const int n = int(s.size());
    for (int p = 1; 2*p <= n; ++p) {
        bool square = true;
        for (int j = 0; j < p; ++j) {
            if (s[n-2*p+j] != s[n-p+j]) { square = false; break; }
        }
        if (square) return '2';
    }
    return '1';
}

int main() {
    const std::string prefix = "11211221211212211221211221121221122121121221211221121221122121122112122121121221121";
    assert(prefix.size() == 83);
    std::vector<State> current(1);
    for (int n = 1; n <= 85; ++n) {
        std::vector<State> next;
        for (const auto &s: current) {
            for (char a = '0'; a <= '2'; ++a) {
                State t = s;
                t.word.push_back(a);
                if (suffix_has_overlap(t.word)) continue;
                t.trace.push_back(suffix_curl(t.word));
                if (suffix_has_overlap(t.trace)) continue;
                next.push_back(std::move(t));
            }
        }
        current.swap(next);
        if (n == 84) {
            assert(current.size() == 6048);
            std::map<std::string, int> cnt;
            for (const auto &s: current) ++cnt[s.trace];
            assert(cnt.size() == 2);
            assert(cnt[prefix + '1'] == 4032);
            assert(cnt[prefix + '2'] == 2016);
        }
        if (n == 85) assert(current.empty());
    }
    std::cout << "TERMINAL_CURL_LABELED_VERIFY_OK 6048 4032 2016\n";
}
