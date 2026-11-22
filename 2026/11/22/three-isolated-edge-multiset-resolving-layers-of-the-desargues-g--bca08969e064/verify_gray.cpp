#include <array>
#include <cstdint>
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int main() {
    // Independent generalized-Petersen presentation GP(10,3).
    // Vertices 0..9 are outer, 10..19 are inner.
    vector<vector<int>> neighbors(20);
    vector<pair<int,int>> edges;
    auto add_edge=[&](int a,int b) {
        neighbors[a].push_back(b); neighbors[b].push_back(a);
        if(a>b) swap(a,b);
        edges.emplace_back(a,b);
    };
    for(int i=0;i<10;++i) {
        add_edge(i,(i+1)%10);
        add_edge(10+i,10+(i+3)%10);
        add_edge(i,10+i);
    }
    if(edges.size()!=30) return 2;
    array<array<int,20>,20> d{};
    for(int a=0;a<20;++a){
        d[a].fill(100); d[a][a]=0;
        queue<int> q;q.push(a);
        while(!q.empty()){
            int x=q.front();q.pop();
            for(int y:neighbors[x]) if(d[a][y]==100){d[a][y]=d[a][x]+1;q.push(y);}
        }
    }
    array<array<int,20>,30> levels{};
    for(int e=0;e<30;++e){
        auto [a,b]=edges[e];
        for(int t=0;t<20;++t){
            levels[e][t]=min(d[t][a],d[t][b]);
            if(levels[e][t]<0 || levels[e][t]>4) return 3;
        }
    }
    array<array<int,5>,30> hist{};
    uint32_t prev=0;
    uint64_t tally[21]{};
    for(uint32_t step=0;step<(1u<<20);++step){
        uint32_t mask=step^(step>>1);
        if(step){
            uint32_t diff=mask^prev;
            int t=__builtin_ctz(diff), delta=(mask&(1u<<t))?1:-1;
            for(int e=0;e<30;++e) hist[e][levels[e][t]]+=delta;
        }
        prev=mask;
        uint64_t codes[30];bool unique=true;
        for(int e=0;e<30 && unique;++e){
            uint64_t code=0;
            for(int h=0;h<5;++h) {
                if(hist[e][h]<0 || hist[e][h]>20) return 4;
                code |= ((uint64_t)hist[e][h])<<(5*h);
            }
            for(int j=0;j<e;++j) if(codes[j]==code){unique=false;break;}
            codes[e]=code;
        }
        if(unique) ++tally[__builtin_popcount(mask)];
    }
    for(int k=0;k<=20;++k) if(tally[k]) cout<<k<<":"<<tally[k]<<" ";
    cout<<"\n";
    if(tally[8]!=720 || tally[10]!=960 || tally[12]!=720) return 5;
    for(int k=0;k<=20;++k) if(k!=8 && k!=10 && k!=12 && tally[k]) return 6;
    cout<<"GRAY_EXHAUSTIVE_OK\n";
}
