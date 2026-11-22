// Independent finite certificate A: enumerate all (3!)^9 local permutations.
// Compile: g++ -O2 -std=c++17 verify_orientations.cpp -o verify_orientations
// Run: ./verify_orientations
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <utility>
using namespace std;
int main() {
    constexpr array<array<int,3>,6> perms = {{{0,1,2},{0,2,1},{1,0,2},
                                               {1,2,0},{2,0,1},{2,1,0}}};
    int inv[6][3] = {};
    for (int j=0;j<6;j++) for (int a=0;a<3;a++) inv[j][perms[j][a]]=a;
    map<pair<int,int>,int64_t> table;
    int64_t accepted=0;
    constexpr int64_t count=10077696; // 6^9
    for (int64_t code=0;code<count;code++) {
        int choice[9]; int64_t x=code;
        for (int u=0;u<9;u++) {choice[u]=static_cast<int>(x%6);x/=6;}
        int pos=0;
        uint32_t seen=0;
        for (int step=0;step<27;step++) {
            if (seen & (1u<<pos)) break;
            seen |= (1u<<pos);
            const int a=pos/9;
            const int bc=pos%9;
            pos=3*bc+perms[choice[bc]][a];
        }
        if (pos!=0 || seen!=((1u<<27)-1)) continue;
        accepted++;
        int line_runs=19;
        for (int u=0;u<8;u++)
            line_runs += (inv[choice[u]][2]!=inv[choice[u+1]][0]);
        const int circular_runs = line_runs -1+
            (inv[choice[8]][2]!=inv[choice[0]][0]);
        table[{line_runs,circular_runs}]++;
    }
    const map<pair<int,int>,int64_t> expected={
        {{19,18},16}, {{19,19},58}, {{20,19},320}, {{20,20},534},
        {{21,20},1866}, {{21,21},4462}, {{22,21},7466}, {{22,22},17468},
        {{23,22},16984}, {{23,23},47150}, {{24,23},26112}, {{24,24},76186},
        {{25,24},24438}, {{25,25},77934}, {{26,25},13158}, {{26,26},44788},
        {{27,26},2952}, {{27,27},11356}
    };
    assert(accepted==373248);
    assert(table==expected);
    cout << "ORIENTATION_CERTIFICATE_OK " << accepted << "\n";
    for (const auto& item:table)
        cout << item.first.first << "," << item.first.second
             << "," << item.second << "\n";
}
