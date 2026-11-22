// Exhaustive exact check of the bivariate maximal-independent-set polynomial
// of the point-line incidence graph of PG(2,4).
// Compile: g++ -std=c++17 -O2 -Wall -Wextra checks/pg4_homogeneous.cpp -o pg4_check
// Run: ./pg4_check
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <vector>
using namespace std;

// GF(4) = F_2[t]/(t^2+t+1), with bits encoding 1 and t.
static int product(int a, int b) {
    int raw=0;
    for(int i=0;i<2;i++) for(int j=0;j<2;j++)
        if ((a & (1<<i)) && (b & (1<<j))) raw ^= 1<<(i+j);
    if(raw & 4) raw ^= 7;
    return raw;
}
static int inverse(int a) {
    assert(a!=0);
    for(int b=1;b<=3;b++) if(product(a,b)==1) return b;
    assert(false); return -1;
}
static int popcount(uint32_t v){ return __builtin_popcount(v); }

int main() {
    vector<array<int,3>> representatives;
    for(int a=0;a<4;a++) for(int b=0;b<4;b++) for(int c=0;c<4;c++){
        if(!(a|b|c)) continue;
        int pivot=a?a:(b?b:c), inv=inverse(pivot);
        array<int,3> p{product(a,inv),product(b,inv),product(c,inv)};
        if(find(representatives.begin(),representatives.end(),p)==representatives.end())
            representatives.push_back(p);
    }
    assert(representatives.size()==21);
    vector<uint32_t> line_masks;
    for(auto a:representatives){
        uint32_t mask=0;
        for(int i=0;i<21;i++){
            auto b=representatives[i];
            if((product(a[0],b[0])^product(a[1],b[1])^product(a[2],b[2]))==0)
                mask |= 1u<<i;
        }
        line_masks.push_back(mask);
    }
    assert(line_masks.size()==21);
    for(int i=0;i<21;i++){
        assert(popcount(line_masks[i])==5);
        int point_degree=0;
        for(auto m:line_masks) point_degree += (m>>i)&1u;
        assert(point_degree==5);
        for(int j=0;j<i;j++) assert(popcount(line_masks[i]&line_masks[j])==1);
    }
    map<pair<int,int>,uint64_t> counts;
    const uint32_t full=(1u<<21)-1u;
    for(uint32_t selected=0;selected<=full;selected++){
        uint32_t point_coverage=selected;
        int selected_line_count=0;
        for(uint32_t line:line_masks) if((selected & line)==0){
            ++selected_line_count;
            point_coverage |= line;
        }
        if(point_coverage==full) ++counts[{popcount(selected), selected_line_count}];
    }
    const map<pair<int,int>,uint64_t> expected={
        {{0,21},1},{{1,16},21},{{2,12},210},{{3,8},210},{{3,9},1120},
        {{4,4},105},{{4,6},3360},{{4,7},2520},{{5,5},10080},
        {{6,4},3360},{{6,6},168},{{7,4},2520},{{8,3},210},
        {{9,3},1120},{{12,2},210},{{16,1},21},{{21,0},1}
    };
    assert(counts==expected);
    uint64_t total=0;
    for(auto [key,number]:counts){
        cout<<key.first<<"\t"<<key.second<<"\t"<<number<<"\n";
        total+=number;
    }
    assert(total==25237);
    cerr<<"PASS: all 2097152 point selections, 21 projective lines, 17 terms, "
        <<total<<" maximal independent sets.\n";
}
