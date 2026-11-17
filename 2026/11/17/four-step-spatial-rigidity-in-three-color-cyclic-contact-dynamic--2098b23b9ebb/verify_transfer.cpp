// Exact finite transfer certificate for four-periodic three-color successor-contact dynamics.
// Build: g++ -std=c++17 -O2 verify_transfer.cpp -o verify_transfer
// Run: ./verify_transfer
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdio>
#include <functional>
#include <set>
#include <string>
#include <vector>
using namespace std;
static constexpr int L=12, C=L*L, V=C*C;
int main() {
    array<array<int,4>,L> timeword{};
    for(int initial=0; initial<3; ++initial)
       for(int hold=0; hold<4; ++hold) {
           int k=4*initial+hold, v=initial;
           for(int t=0;t<4;++t) {timeword[k][t]=v; if(t!=hold) v=(v+1)%3;}
           assert(v==initial);
       }
    vector<vector<int>> out(V), rev(V);
    long long number_edges=0;
    for(int left=0;left<C;++left)for(int middle=0;middle<C;++middle)
    for(int right=0;right<C;++right) {
        bool valid=true;
        int a[2]={left/L,left%L}, b[2]={middle/L,middle%L}, c[2]={right/L,right%L};
        for(int row=0;row<2 && valid;++row)for(int t=0;t<4;++t) {
            int old=timeword[b[row]][t];
            int next=(old+1)%3;
            bool touched=(timeword[b[1-row]][t]==next ||
                          timeword[a[0]][t]==next || timeword[a[1]][t]==next ||
                          timeword[c[0]][t]==next || timeword[c[1]][t]==next);
            int update=touched?next:old;
            if(update != timeword[b[row]][(t+1)%4]) {valid=false;break;}
        }
        if(valid) {
            int from=left*C+middle, to=middle*C+right;
            out[from].push_back(to); rev[to].push_back(from); ++number_edges;
        }
    }
    // Kosaraju strongly connected components, including all nominal pair states.
    vector<int> used(V,0), finish;
    finish.reserve(V);
    for(int root=0;root<V;++root)if(!used[root]) {
        vector<pair<int,int>> todo{{root,0}}; used[root]=1;
        while(!todo.empty()) {
            int v=todo.back().first;
            int &i=todo.back().second;
            if(i<(int)out[v].size()) {
                int u=out[v][i++];
                if(!used[u]) {used[u]=1;todo.push_back({u,0});}
            } else {finish.push_back(v);todo.pop_back();}
        }
    }
    vector<int> comp(V,-1);
    vector<vector<int>> members;
    for(int j=V-1;j>=0;--j) {
        int root=finish[j]; if(comp[root]!=-1)continue;
        int k=members.size();members.emplace_back();
        vector<int> todo{root};comp[root]=k;
        while(!todo.empty()) {
            int v=todo.back();todo.pop_back();members.back().push_back(v);
            for(int u:rev[v])if(comp[u]==-1){comp[u]=k;todo.push_back(u);}
        }
    }
    vector<vector<int>> cyclic;
    for(auto &s:members) {
        if(s.size()>1)cyclic.push_back(s);
        else {int v=s[0];for(int w:out[v])if(w==v)cyclic.push_back(s);}
    }
    assert(number_edges==20340);
    assert(cyclic.size()==6);
    set<string> actual;
    for(auto &s:cyclic) {
        assert(s.size()==4);
        set<int> vertices(s.begin(),s.end());
        for(int v:s) {
            int indeg=0, outdeg=0;
            for(int w:out[v])if(vertices.count(w))++outdeg;
            for(int w:rev[v])if(vertices.count(w))++indeg;
            assert(indeg==1 && outdeg==1);
            string rows[2];
            int current=v;
            for(int j=0;j<4;++j) {
                int col=current/C, lo=col/L, hi=col%L;
                rows[0]+='0'+timeword[lo][0];
                rows[1]+='0'+timeword[hi][0];
                int next=-1;
                for(int z:out[current])if(vertices.count(z))next=z;
                assert(next>=0);
                current=next;
            }
            assert(current==v && rows[0]==rows[1]);
            actual.insert(rows[0]);
        }
    }
    set<string> expected;
    string base="2100";
    for(int orientation=0;orientation<2;++orientation) {
       string z=base;
       if(orientation)reverse(z.begin(),z.end());
       for(int rotation=0;rotation<4;++rotation)
       for(int phase=0;phase<3;++phase) {
           string q;
           for(int i=0;i<4;++i)q+=char('0'+(z[(i+rotation)%4]-'0'+phase)%3);
           expected.insert(q);
       }
    }
    assert(expected.size()==24 && actual==expected);
    printf("column_traces=%d column_states=%d pair_states=%d\n",L,C,V);
    printf("directed_edges=%lld strongly_connected_components=%zu\n",number_edges,members.size());
    printf("cyclic_components=%zu cyclic_component_sizes=4,4,4,4,4,4\n",cyclic.size());
    printf("cyclic_edges=24 component_internal_in_out_degree=1\n");
    printf("observed_four_column_patterns=%zu expected_oriented_patterns=%zu equality=PASS\n",actual.size(),expected.size());
    for(int n=3;n<=16;++n)printf("n=%d primitive_four_states=%d primitive_four_orbits=%d\n",n,n%4==0?24:0,n%4==0?6:0);
}
