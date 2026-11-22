// Finite affine-cylinder enumeration for the Clebsch graph.
// Compile: g++ -O2 -std=c++17 verify_affine.cpp -o verify_affine
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <set>
#include <vector>
using namespace std;
static const int FULL = (1 << 16) - 1;

int main() {
    vector<int> words;
    for(int x=0; x<32; ++x) if(__builtin_popcount((unsigned)x)%2==0) words.push_back(x);
    assert(words.size()==16);
    int near[16]={};
    for(int i=0;i<16;++i) for(int j=0;j<16;++j)
        if(__builtin_popcount((unsigned)(words[i]^words[j]))==4) near[i]|=1<<j;

    // Independently generate every two-coordinate cylinder and its support.
    vector<pair<int,int>> planes;
    for(int a=0;a<5;++a) for(int b=a+1;b<5;++b)
        for(int val=0;val<4;++val) {
            int block=0;
            for(int i=0;i<16;++i)
                if(((words[i]>>a)&1)==(val&1) &&
                   ((words[i]>>b)&1)==((val>>1)&1)) block |=1<<i;
            assert(__builtin_popcount((unsigned)block)==4);
            for(int i=0;i<16;++i) {
                assert(!(block&(1<<i)) || !(near[i]&block));
                int d=__builtin_popcount((unsigned)(near[i]&block));
                assert(d==0 || d%2==1);
            }
            planes.push_back({block,5*a+b});
        }
    assert(planes.size()==40);
    set<int> unique;
    for(auto b: planes) unique.insert(b.first);
    assert(unique.size()==40);

    // Enumerate every disjoint family of cylinders once by increasing index.
    long long count[5]={};
    map<int,long long> directions_per_full_partition;
    auto dfs = [&](auto&& self, int start, int mask, int count_blocks, int support_mask)->void {
        count[count_blocks]++;
        if(count_blocks==4) {
            assert(mask==FULL);
            directions_per_full_partition[__builtin_popcount((unsigned)support_mask)]++;
            return;
        }
        for(int i=start;i<(int)planes.size();++i) {
            int block=planes[i].first;
            if(!(mask&block)) {
                    // Supports are assigned consecutive integer labels by pair order.
                int support_index=i/4;
                self(self,i+1,mask|block,count_blocks+1,support_mask|(1<<support_index));
            }
        }
    };
    dfs(dfs,0,0,0,0);
    assert(count[0]==1 && count[1]==40 && count[2]==300 && count[3]==360 && count[4]==70);
    assert(directions_per_full_partition[1]==10 && directions_per_full_partition[2]==60);
    assert(directions_per_full_partition.size()==2);
    cout << "affine_cylinders=" << planes.size() << " graph_edges=40\n";
    cout << "disjoint_cylinder_families_by_size=1,40,300,360,70\n";
    cout << "four_block_partition_direction_types=10_single,60_double\n";
    cout << "strong_odd_color_count_polynomial=70*z^4+360*z^7+300*z^10+40*z^13+z^16\n";
}
