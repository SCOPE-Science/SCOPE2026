// Independent finite certificate B: traverse Euler tours of the ternary
// order-two overlap graph and construct BWT by sorting 27 cyclic triples.
// Compile: g++ -O2 -std=c++17 verify_euler.cpp -o verify_euler
// Run: ./verify_euler
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <utility>
using namespace std;
array<unsigned char,27> symbols{};
map<pair<int,int>,int64_t> table;
int64_t total=0;
void enumerate(int vertex,uint32_t used,int length) {
    if (length==27) {
        if (vertex!=0) return;
        array<unsigned char,27> last{};
        for (int j=0;j<27;j++) {
            const int key=9*symbols[j]+3*symbols[(j+1)%27]
                           +symbols[(j+2)%27];
            last[key]=symbols[(j+26)%27];
        }
        int linear_runs=1;
        for(int j=1;j<27;j++) linear_runs+=(last[j]!=last[j-1]);
        const int cyclic_runs=linear_runs-1+(last[26]!=last[0]);
        table[{linear_runs,cyclic_runs}]++;
        total++;
        return;
    }
    for(int letter=0;letter<3;letter++) {
        int edge=3*vertex+letter;
        if(used&(1u<<edge)) continue;
        symbols[length]=static_cast<unsigned char>(letter);
        enumerate(3*(vertex%3)+letter, used|(1u<<edge),length+1);
    }
}
int main() {
    // Every Euler tour contains 000 exactly once: put it first.
    symbols[0]=0;
    enumerate(0,1u,1);
    const map<pair<int,int>,int64_t> expected={
        {{19,18},16}, {{19,19},58}, {{20,19},320}, {{20,20},534},
        {{21,20},1866}, {{21,21},4462}, {{22,21},7466}, {{22,22},17468},
        {{23,22},16984}, {{23,23},47150}, {{24,23},26112}, {{24,24},76186},
        {{25,24},24438}, {{25,25},77934}, {{26,25},13158}, {{26,26},44788},
        {{27,26},2952}, {{27,27},11356}
    };
    assert(total==373248);
    assert(table==expected);
    cout<<"EULER_CERTIFICATE_OK "<<total<<"\n";
    for(const auto& item:table)
        cout<<item.first.first<<","<<item.first.second<<","<<item.second<<"\n";
}
