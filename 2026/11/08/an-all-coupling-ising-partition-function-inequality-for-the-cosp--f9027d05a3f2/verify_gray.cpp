// Standalone exact integer verification of the two 16-vertex Ising cut distributions.
// Compile: c++ -std=c++17 -O2 verify_gray.cpp -o verify_gray && ./verify_gray
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <set>
#include <utility>
#include <vector>

using namespace std;
using Edge = pair<int,int>;

vector<Edge> make_edges(bool shrikhande) {
    set<Edge> e;
    auto add=[&](int a,int b) {
        if(a>b) swap(a,b);
        assert(a!=b);
        e.insert({a,b});
    };
    for(int x=0;x<4;x++) for(int y=0;y<4;y++) {
        const int a=4*x+y;
        if(shrikhande) {
            for(const auto [dx,dy]: vector<pair<int,int>>{{1,0},{0,1},{1,1}})
                add(a,4*((x+dx)%4)+(y+dy)%4);
        } else {
            for(int u=0;u<4;u++) if(u!=x) add(a,4*u+y);
            for(int v=0;v<4;v++) if(v!=y) add(a,4*x+v);
        }
    }
    assert(e.size()==48);
    return {e.begin(), e.end()};
}

array<int,49> count_cuts(const vector<Edge>& edges) {
    array<vector<int>,16> adj;
    for(auto [a,b]:edges) { adj[a].push_back(b); adj[b].push_back(a); }
    for(auto &neighbors:adj) assert(neighbors.size()==6);
    for(int a=0;a<16;a++) for(int b=a+1;b<16;b++) {
        bool linked=false; int cn=0;
        for(int u:adj[a]) if(u==b) linked=true;
        for(int u:adj[a]) for(int v:adj[b]) if(u==v) ++cn;
        assert(cn==2); // parameters (16,6,2,2)
    }
    array<int,49> histogram{};
    uint32_t mask=0;
    int cut=0;
    histogram[0]=1;
    for(uint32_t s=1;s<65536;s++) {
        // Gray code g(s)=s^(s>>1): from g(s-1), flip least-significant set bit of s.
        const int v=__builtin_ctz(s);
        const bool prior=(mask>>v)&1U;
        for(int u:adj[v]) {
            const bool same=(prior==bool((mask>>u)&1U));
            cut+=same?1:-1;
        }
        mask^=(1U<<v);
        assert(mask==(s^(s>>1)) && cut>=0 && cut<=48);
        histogram[cut]++;
    }
    int total=0;
    for(int c=0;c<=48;c++) { total+=histogram[c]; assert(c%2==0 || histogram[c]==0); }
    assert(total==65536);
    return histogram;
}

int main() {
    const auto r=count_cuts(make_edges(false));
    const auto s=count_cuts(make_edges(true));
    const array<int,11> expected_d{{16,-96,240,-384,672,-1344,2016,-1920,1104,-352,48}};
    for(int c=0;c<=48;c++) {
        const int delta=r[c]-s[c];
        if(c>=12 && c<=32 && c%2==0) assert(delta==expected_d[(c-12)/2]);
        else assert(delta==0);
    }
    assert(r[32]==90 && s[32]==42);
    for(int c=33;c<=48;c++) assert(r[c]==0 && s[c]==0);
    for(int c=0;c<=48;c++) if(r[c]||s[c])
        cout<<c<<' '<<r[c]<<' '<<s[c]<<'\n';
    cout<<"VERIFY_GRAY_OK configurations_per_graph=65536 maxcut=32\n";
}
