// Independent bottom-up computation of the graph-pegging reach polynomial.
// C++17, no third-party libraries. 14 labelled vertices are 7 points and 7 dual lines.
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;
struct Move { int a,b,c; };
int main() {
    constexpr int n=14, limit=1<<n, all=limit-1;
    array<uint16_t,n> adj{};
    for(int a=0;a<7;a++) for(int b=0;b<7;b++) {
        int parity=__builtin_popcount((a+1)&(b+1))%2;
        if(!parity) { adj[a] |= (1u<<(7+b)); adj[7+b] |= (1u<<a); }
    }
    vector<Move> moves;
    for(int b=0;b<n;b++) for(int a=0;a<n;a++) if(adj[b]&(1u<<a))
        for(int c=0;c<n;c++) if(c!=a && (adj[b]&(1u<<c)))
            moves.push_back({a,b,c});
    assert(moves.size()==84);
    vector<uint16_t> reach(limit);
    // Every move removes exactly one peg, hence the recursion is acyclic by size.
    for(int k=0;k<=n;k++) for(int s=0;s<limit;s++) if(__builtin_popcount((unsigned)s)==k) {
        uint16_t r=s;
        for(auto [a,b,c]: moves) {
            uint16_t ba=1u<<a,bb=1u<<b,bc=1u<<c;
            if((s&ba)&&(s&bb)&&!(s&bc)) r |= reach[s^ba^bb^bc];
        }
        reach[s]=r;
    }
    vector<int> num(n+1), min_num(n+1);
    for(int s=0;s<limit;s++) if(reach[s]==all) {
        int k=__builtin_popcount((unsigned)s); num[k]++;
        bool mini=true;
        for(int a=0;a<n;a++) if((s>>a)&1) if(reach[s^(1<<a)]==all) mini=false;
        if(mini) min_num[k]++;
    }
    const vector<int> expected{0,0,0,0,336,1862,2989,3430,3003,2002,1001,364,91,14,1};
    assert(num==expected);
    assert(min_num[4]==336 && min_num[5]==434);
    for(int k=0;k<=n;k++) if(k!=4 && k!=5) assert(min_num[k]==0);
    // Derive the geometric criterion independently for every 4-subset.
    for(int s=0;s<limit;s++) if(__builtin_popcount((unsigned)s)==4) {
        bool criterion=false;
        if(__builtin_popcount((unsigned)(s&127))==2) {
            int a[2],b[2],i=0,j=0;
            for(int v=0;v<7;v++) if(s>>v&1) a[i++]=v;
            for(int v=7;v<14;v++) if(s>>v&1) b[j++]=v;
            if(j==2) {
                int es=0,d0=0,d1=0;
                for(int x=0;x<2;x++) for(int y=0;y<2;y++) if(adj[a[x]]&(1u<<b[y])) {
                    es++; if(x==0)d0++; if(y==0)d1++;
                }
                criterion=(es==1 || es==3 || (es==2 && d0==1 && d1==1));
            }
        }
        assert((reach[s]==all)==criterion);
    }
    cout<<"full_counts:";
    for(int x:num)cout<<" "<<x;
    cout<<"\nminimal_counts:";
    for(int x:min_num)cout<<" "<<x;
    cout<<"\nPASS\n";
}
