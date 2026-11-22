// Exhaustive four-state binary transformation-monoid census.
// Build: c++ -std=c++17 -O2 -o verify_transforms verify_transforms.cpp
// Run from the directory containing joint_spectrum.csv: ./verify_transforms
#include <algorithm>
#include <array>
#include <cassert>
#include <fstream>
#include <iostream>
#include <map>
#include <queue>
#include <stdexcept>
#include <string>
#include <tuple>
#include <utility>
using namespace std;
int main() {
    constexpr int T = 256;
    int next[T][T];
    for (int f = 0; f < T; ++f) for (int g = 0; g < T; ++g) {
        int h = 0;
        for (int i = 0; i < 4; ++i) {
            int j = (f >> (2*i)) & 3;
            h |= ((g >> (2*j)) & 3) << (2*i);
        }
        next[f][g] = h; // read f, then g
    }
    int identity = 0;
    for (int i = 0; i < 4; ++i) identity |= i << (2*i);
    map<pair<int,int>, int> histogram;
    int visit[T] = {0}, depth[T], queue[T];
    int serial = 0;
    for (int a = 0; a < T; ++a) for (int b = 0; b < T; ++b) {
        ++serial;
        int head = 0, tail = 0, reset = -1;
        queue[tail++] = identity;
        visit[identity] = serial; depth[identity] = 0;
        while (head != tail) {
            int f = queue[head++];
            bool constant = true;
            for (int i = 1; i < 4; ++i)
                if (((f >> (2*i)) & 3) != (f & 3)) constant = false;
            if (constant && reset == -1) reset = depth[f];
            for (int generator : {a,b}) {
                int h = next[f][generator];
                if (visit[h] != serial) {
                    visit[h] = serial;
                    depth[h] = depth[f] + 1;
                    queue[tail++] = h;
                }
            }
        }
        assert(tail <= 256);
        histogram[{reset,tail}] += 1;
    }
    ifstream input("joint_spectrum.csv");
    if (!input) throw runtime_error("joint_spectrum.csv not found");
    map<pair<int,int>,int> expected;
    string line;
    if (!getline(input,line) || line != "reset_length,monoid_size,count")
        throw runtime_error("unexpected header");
    while (getline(input,line)) {
        if (line.empty()) throw runtime_error("empty data row");
        int r,m,c; char comma1,comma2;
        size_t x = line.find(','), y = line.find(',',x+1);
        if (x==string::npos || y==string::npos) throw runtime_error("bad csv line");
        r=stoi(line.substr(0,x)); m=stoi(line.substr(x+1,y-x-1)); c=stoi(line.substr(y+1));
        if (!expected.insert({{r,m},c}).second) throw runtime_error("duplicate cell");
    }
    if (histogram != expected) throw runtime_error("transformation histogram mismatch");
    int total=0,slow=0;
    for (const auto &kv : histogram) {
        total+=kv.second;
        if (kv.first.first==9) slow+=kv.second;
    }
    if (total != 65536 || slow != 96 || histogram.size()!=179)
        throw runtime_error("unexpected census invariant");
    cout << "VERIFY_TRANSFORMS_OK: 65536 complete automata, 179 cells, 96 at threshold 9\n";
}
