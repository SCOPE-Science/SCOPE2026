// Exhaustive order-five binary linear universal partial-word enumerator.
// The source is distributed with its complete output and independent checks.
#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>
using namespace std;

constexpr int ORDER = 5;
constexpr int TARGETS = 1 << ORDER;
constexpr int MAX_LENGTH = TARGETS + ORDER - 1;
constexpr int POW3 = 243;
constexpr int SHORT_POW3 = 81;
array<uint32_t, POW3> masks{};
vector<string> solutions;
uint64_t visited_nodes = 0;
int length_now = 0, first_star = 0, second_star = 0;
string candidate;

void visit(int position, int trailing_ternary, uint32_t already_seen) {
    ++visited_nodes;
    if (position == length_now) {
        // There are exactly 32 target occurrences by the necessary weight sum.
        if (already_seen != UINT32_MAX) { cerr << "Invalid terminal coverage\n"; exit(3); }
        solutions.push_back(candidate);
        return;
    }
    const bool wildcard_here = position == first_star || position == second_star;
    for (int symbol = 0; symbol <= 2; ++symbol) {
        if ((symbol == 2) != wildcard_here) continue;
        int extended = trailing_ternary * 3 + symbol;
        candidate[position] = symbol == 2 ? '*' : char('0' + symbol);
        if (position < ORDER - 1) visit(position + 1, extended, already_seen);
        else {
            uint32_t new_targets = masks[extended % POW3];
            if (already_seen & new_targets) continue;
            visit(position + 1, extended % SHORT_POW3, already_seen | new_targets);
        }
    }
}

int main() {
    for (int representation = 0; representation < POW3; ++representation) {
        int x = representation;
        array<int, ORDER> symbols{};
        for (int j = ORDER - 1; j >= 0; --j) { symbols[j] = x % 3; x /= 3; }
        uint32_t mask = 0;
        for (int target = 0; target < TARGETS; ++target) {
            bool compatible = true;
            for (int j = 0; j < ORDER; ++j)
                if (symbols[j] != 2 && symbols[j] != ((target >> (ORDER - j - 1)) & 1))
                    compatible = false;
            if (compatible) mask |= uint32_t(1) << target;
        }
        masks[representation] = mask;
    }
    map<int,int> by_length;
    for (length_now = ORDER; length_now <= MAX_LENGTH; ++length_now) {
        int initial_count = solutions.size();
        for (first_star = 0; first_star < length_now; ++first_star)
            for (second_star = first_star + 1; second_star < length_now; ++second_star) {
                int total_weight = 0;
                for (int start = 0; start <= length_now - ORDER; ++start) {
                    int count_stars = (start <= first_star && first_star < start + ORDER)
                                    + (start <= second_star && second_star < start + ORDER);
                    total_weight += 1 << count_stars;
                }
                if (total_weight != TARGETS) continue;
                candidate.assign(length_now, '0');
                visit(0, 0, 0);
            }
        if (solutions.size() != size_t(initial_count)) by_length[length_now] = int(solutions.size()) - initial_count;
    }
    sort(solutions.begin(), solutions.end());
    if (unique(solutions.begin(),solutions.end()) != solutions.end()) {
        cerr << "Duplicate accepted word\n";
        return 4;
    }
    for (const string &word : solutions) cout << word << '\n';
    cerr << "EXHAUSTIVE_OK nodes=" << visited_nodes << " total=" << solutions.size() << " by_length=";
    for (auto &entry : by_length) cerr << entry.first << ':' << entry.second << ',';
    cerr << '\n';
}
