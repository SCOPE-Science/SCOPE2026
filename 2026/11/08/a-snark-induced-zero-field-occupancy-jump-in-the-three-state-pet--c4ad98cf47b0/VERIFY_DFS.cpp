// Exact full ternary enumeration of the three-state Potts model on L(Petersen).
// Build: c++ -std=c++17 -O2 VERIFY_DFS.cpp -o verify_dfs && ./verify_dfs
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <limits>
#include <string>
using namespace std;
int main() {
    array<array<int,2>,15> edges{};
    int ne=0;
    auto add=[&](int a,int b) {edges[ne++]={a,b};};
    for (int i=0;i<5;++i) {
        add(i,(i+1)%5);                 // outside pentagon
        add(i,5+i);                     // spokes
        add(5+i,5+(i+2)%5);             // inside pentagram
    }
    if(ne!=15) return 1;
    array<array<unsigned char,15>,15> adjacent{};
    int link_count=0;
    for(int i=0;i<15;++i) for(int j=i+1;j<15;++j) {
        auto a=edges[i], b=edges[j];
        if(a[0]==b[0] || a[0]==b[1] || a[1]==b[0] || a[1]==b[1]) {
            adjacent[i][j]=adjacent[j][i]=1;
            ++link_count;
        }
    }
    if(link_count!=30) return 2;
    array<int,16> best;
    best.fill(numeric_limits<int>::max());
    array<uint64_t,16> ways{};
    array<string,16> witness{};
    array<int,15> col{};
    uint64_t visited=0;
    auto dfs=[&](auto&& self,int pos,int equal_edges,int fav)->void {
        if(pos==15) {
            ++visited;
            if(equal_edges<best[fav]) {
                best[fav]=equal_edges;ways[fav]=0;
                witness[fav].clear();
                for(int c:col) witness[fav]+=char('0'+c);
            }
            if(equal_edges==best[fav]) ++ways[fav];
            return;
        }
        for(int c=0;c<3;++c) {
            col[pos]=c;
            int incr=0;
            for(int j=0;j<pos;++j)
                if(adjacent[pos][j] && col[j]==c) ++incr;
            self(self,pos+1,equal_edges+incr,fav+(c==0));
        }
    };
    dfs(dfs,0,0,0);
    constexpr array<int,16> expected_min={10,8,6,4,2,2,2,4,6,8,10,14,18,22,26,30};
    constexpr array<uint64_t,16> expected_ways={1782,5880,6420,2640,300,1200,300,2520,5520,3120,192,1440,1160,300,30,1};
    if(visited!=14348907ULL || best!=expected_min || ways!=expected_ways) return 3;
    cout<<"visited "<<visited<<"  line_edges "<<link_count<<"\n";
    for(int k=0;k<=15;++k) {
        if(witness[k].size()!=15) return 4;
        cout<<k<<" "<<best[k]<<" "<<ways[k]<<" "<<witness[k]<<"\n";
    }
    cout<<"VERIFY_DFS_OK\n";
}
