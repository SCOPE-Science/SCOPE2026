// Exact finite enumeration of three-state complete unary-binary tree automata.
// Build: g++ -O2 -std=c++17 verify_height_leaves.cpp -o v1 && ./v1
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
using namespace std;
int main() {
    array<array<long long, 6>, 6> counts{};
    for (int unary_code = 0; unary_code < 27; ++unary_code) {
        int u[3], v=unary_code;
        for (int i=0;i<3;++i) {u[i]=v%3; v/=3;}
        int U[8]{};
        for (int s=1;s<8;++s)
            for (int i=0;i<3;++i) if (s&(1<<i)) U[s]|=1<<u[i];
        for (int binary_code=0;binary_code<19683;++binary_code) {
            int b[9], z=binary_code;
            for (int i=0;i<9;++i) {b[i]=z%3;z/=3;}
            int B[8][8]{};
            for (int s=1;s<8;++s) for (int t=1;t<8;++t)
                for (int i=0;i<3;++i) for (int j=0;j<3;++j)
                    if ((s&(1<<i)) && (t&(1<<j))) B[s][t] |= 1<<b[3*i+j];
            // Reachable masks, with the bit at position (s-1) standing for state set s.
            uint8_t reach=uint8_t(1<<(7-1));
            int least_height=5;
            for (int h=0;h<=4;++h) {
                if (reach & 0b00001011) {least_height=h;break;}
                if (h==4) break;
                uint8_t next=reach;
                for (int s=1;s<8;++s) if (reach&(1<<(s-1))) {
                    next |= uint8_t(1<<(U[s]-1));
                    for (int t=1;t<8;++t) if (reach&(1<<(t-1)))
                        next |= uint8_t(1<<(B[s][t]-1));
                }
                reach=next;
            }
            if (least_height==5) {++counts[0][0];continue;}
            // Unrestricted leaf-count minimization; unary edges cost zero extra leaves,
            // binary nodes add the numbers of leaves in their two subterms.
            int cost[8];for (int i=0;i<8;++i) cost[i]=999;
            cost[7]=1;
            bool improved=true;
            int passes=0;
            while (improved) {
                assert(++passes<=30);
                improved=false;
                for (int s=1;s<8;++s) if (cost[s]<999 && cost[U[s]]>cost[s]) {
                    cost[U[s]]=cost[s];improved=true;
                }
                for (int s=1;s<8;++s) if (cost[s]<999)
                    for (int t=1;t<8;++t) if (cost[t]<999) {
                        int c=cost[s]+cost[t];
                        if (cost[B[s][t]]>c) {cost[B[s][t]]=c;improved=true;}
                    }
            }
            int least_leaves=min({cost[1],cost[2],cost[4]});
            assert(least_leaves>=1 && least_leaves<=4);
            ++counts[least_height][least_leaves];
        }
    }
    const long long expected[5][5] = {
        {288444,0,0,0,0},
        {0,59067,54,0,0},
        {0,118080,14088,1572,1056},
        {0,0,35448,3156,1764},
        {0,0,0,5220,3492}
    };
    long long sum=0;
    for(int h=0;h<=4;++h)for(int l=0;l<=4;++l){
        assert(counts[h][l]==expected[h][l]);sum+=counts[h][l];
    }
    assert(sum==531441);
    cout << "HEIGHT_LEAVES_OK total=531441 synchronizing=242997 height4=8712\n";
}
