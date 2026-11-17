// Exact labelled majority-dynamics census on the 18-vertex Pappus graph.
// All definitions, graph edges, assertions and outputs are self-contained.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <queue>
#include <utility>
#include <vector>
using namespace std;
int main() {
    constexpr int V = 18, N = 1 << V;
    array<vector<int>, V> neighbors;
    auto edge = [&](int x, int y) { neighbors[x].push_back(y); neighbors[y].push_back(x); };
    for (int i = 0; i < V; ++i) edge(i, (i+1)%V);
    constexpr pair<int,int> chords[] = {
        {0,5},{1,8},{2,13},{3,10},{4,15},{6,11},{7,14},{9,16},{12,17}
    };
    for (const auto &e : chords) edge(e.first, e.second);
    for (int v=0;v<V;++v) assert(neighbors[v].size()==3);
    vector<int> next(N), indegree(N), enter(N,-1), orbit_id(N,-1), peel;
    peel.reserve(N);
    for (int s=0;s<N;++s) {
        int z=0;
        for (int v=0;v<V;++v) {
            int votes=0;
            for (int u:neighbors[v]) votes += (s>>u)&1;
            if (votes>=2) z|=1<<v;
        }
        next[s]=z; ++indegree[z];
    }
    for (int i=0;i<N;++i) if (indegree[i]==0) peel.push_back(i);
    for (size_t i=0;i<peel.size();++i) {
        int v=next[peel[i]];
        if (--indegree[v]==0) peel.push_back(v);
    }
    vector<int> lengths,basins;
    for (int s=0;s<N;++s) if (indegree[s]>0 && orbit_id[s]<0) {
        int len=0,cur=s,id=(int)lengths.size();
        do { assert(orbit_id[cur]<0); orbit_id[cur]=id;enter[cur]=0; ++len;cur=next[cur]; } while (cur!=s);
        lengths.push_back(len);basins.push_back(len);
    }
    for (int i=(int)peel.size()-1;i>=0;--i) {
        int s=peel[i];orbit_id[s]=orbit_id[next[s]];
        enter[s]=enter[next[s]]+1;
        ++basins[orbit_id[s]];
    }
    map<int,int> periods, basin_total;
    map<pair<int,int>,int> basin_hist, enter_hist;
    int maxenter=0,periodic=0;
    for (size_t j=0;j<lengths.size();++j) {
        ++periods[lengths[j]];
        ++basin_hist[{lengths[j],basins[j]}];
        basin_total[lengths[j]] += basins[j];
    }
    for (int s=0;s<N;++s) {
        assert(enter[s]>=0);
        int t=enter[s],p=lengths[orbit_id[s]];
        ++enter_hist[{t,p}];maxenter=max(maxenter,t);
        if (t==0) ++periodic;
        // Verify each state becomes periodic by update three.
        int a=s,b=s;
        for(int i=0;i<3;++i)a=next[a];
        for(int i=0;i<5;++i)b=next[b];
        assert(a==b);
    }
    assert((periods==map<int,int>{{1,92},{2,4186}}));
    assert(periodic==8464 && maxenter==3);
    assert((basin_hist==map<pair<int,int>,int>{
        {{1,4},54},{{1,16},36},{{1,16900},2},
        {{2,8},1431},{{2,16},1944},{{2,32},630},
        {{2,520},108},{{2,1040},72},{{2,33800},1}
    }));
    assert((enter_hist==map<pair<int,int>,int>{
        {{0,1},92},{{0,2},8372},{{1,1},1668},{{1,2},77484},
        {{2,1},5760},{{2,2},42048},{{3,1},27072},{{3,2},99648}
    }));
    assert(basin_total[1]==34592 && basin_total[2]==227552);
    cout<<"Independent full-state check: all "<<N<<" states of the 18-vertex Pappus graph PASS\n";
    cout<<"Periodic orbits: fixed="<<periods[1]<<", primitive two-cycles="<<periods[2]<<"\n";
    cout<<"Periodic states="<<periodic<<", sharp maximum first-entry time="<<maxenter<<"\n";
    cout<<"Attractor basin histogram (period, basin size, number of orbits):\n";
    for(const auto &kv:basin_hist)cout<<kv.first.first<<" "<<kv.first.second<<" "<<kv.second<<"\n";
    cout<<"First-entry census (time, period, configurations):\n";
    for(const auto &kv:enter_hist)cout<<kv.first.first<<" "<<kv.first.second<<" "<<kv.second<<"\n";
    cout<<"F^5 = F^3 on all states: PASS\n";
}
