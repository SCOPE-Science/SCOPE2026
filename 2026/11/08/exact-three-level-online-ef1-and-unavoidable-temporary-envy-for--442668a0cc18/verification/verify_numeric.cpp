// Independent cardinal EF1 cross-check with exact integer valuations.
// 1..L represent any strictly increasing positive L-level alphabet;
// terminal four-good EF1 depends only on the ordinal order.
#include <algorithm>
#include <array>
#include <cstdio>
#include <cstdlib>
using namespace std;
int L, rule, values[4][3], owner[4];
unsigned long long calls[5];

bool terminal_failure() {
    for (int i = 0; i < 3; ++i) {
        int own = 0;
        for (int t = 0; t < 4; ++t) if (owner[t] == i) own += values[t][i];
        for (int j = 0; j < 3; ++j) if (i != j) {
            int total = 0, maximum = 0;
            for (int t = 0; t < 4; ++t) if (owner[t] == j) {
                total += values[t][i];
                maximum = max(maximum, values[t][i]);
            }
            if (own < total - maximum) return true;
        }
    }
    return false;
}

bool adversary_forces_failure(int step) {
    ++calls[step];
    if (step == 4) return terminal_failure();
    for (int code = 0; code < L*L*L; ++code) {
        int z = code;
        for (int i = 0; i < 3; ++i) { values[step][i] = 1 + z%L; z /= L; }
        bool all_actions_fail = true;
        for (int recipient = 0; recipient < 3; ++recipient) {
            if (step == 1 && rule == 1 && recipient == owner[0]) continue;
            if (step == 1 && rule == 2 && recipient != owner[0]) continue;
            owner[step] = recipient;
            if (!adversary_forces_failure(step+1)) {
                all_actions_fail = false;
                break;
            }
        }
        if (all_actions_fail) return true;
    }
    return false;
}

int main() {
    struct Case { int levels, first_two_rule, adversary_wins; };
    constexpr Case cases[] = {{3,0,0}, {3,1,1}, {3,2,1}, {4,0,1}};
    for (const auto c : cases) {
        L = c.levels; rule = c.first_two_rule;
        fill(calls,calls+5,0);
        int result = adversary_forces_failure(0);
        printf("levels=%d rule=%d adversary_wins=%d calls=%llu,%llu,%llu,%llu,%llu\n",
               L,rule,result,calls[0],calls[1],calls[2],calls[3],calls[4]);
        if (result != c.adversary_wins) return 1;
    }
    puts("ALL FOUR GAME VALUES VERIFIED");
    return 0;
}
