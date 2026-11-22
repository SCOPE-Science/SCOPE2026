// Standalone C++17 bitmask verification of the Heawood powerful-alliance count and mobility.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <queue>
#include <set>
#include <vector>
using namespace std;
int main() {
    array<int,14> neighbors{};
    for (int i=0;i<7;++i) for (int delta: {0,1,3}) {
        int p=(i+delta)%7, l=i+7;
        neighbors[p]|=1<<l;
        neighbors[l]|=1<<p;
    }
    vector<int> good;
    array<int,15> counts{};
    for (int s=0;s<(1<<14);++s) {
        bool okay=true;
        for (int v=0;v<14;++v) {
            int have=__builtin_popcount(unsigned(neighbors[v]&s));
            int need=(s&(1<<v))?1:2;
            if (have<need) {okay=false;break;}
        }
        if (!okay) continue;
        ++counts[__builtin_popcount(unsigned(s))];
        if (__builtin_popcount(unsigned(s))==8) good.push_back(s);
    }
    const array<int,15> expected={0,0,0,0,0,0,0,0,84,350,511,308,91,14,1};
    assert(counts==expected);
    assert(good.size()==84);
    for (int s: good) {
        assert(__builtin_popcount(unsigned(s&127))==4);
        assert(__builtin_popcount(unsigned((s>>7)&127))==4);
    }
    vector<vector<int>> edges(good.size());
    int slides=0;
    for (size_t i=0;i<good.size();++i) for (size_t j=i+1;j<good.size();++j) {
        if (__builtin_popcount(unsigned(good[i]^good[j])) != 2) continue;
        edges[i].push_back(int(j));edges[j].push_back(int(i));
        int a=good[i]&~good[j], b=good[j]&~good[i];
        if (neighbors[__builtin_ctz(unsigned(a))] & b) ++slides;
    }
    assert(slides==0);
    int edge_total=0;
    for (auto &es: edges) { assert(es.size()==4);edge_total+=int(es.size()); }
    assert(edge_total==336);
    const vector<int> profile={1,4,8,16,28,22,4,1};
    for (size_t root=0;root<good.size();++root) {
        vector<int> dist(good.size(),-1);
        queue<int> q;dist[root]=0;q.push(int(root));
        while(!q.empty()) {
            int u=q.front();q.pop();
            for(int v:edges[u]) if(dist[v]<0) {dist[v]=dist[u]+1;q.push(v);}
        }
        vector<int> hist(profile.size(),0);
        for (int d:dist) {assert(d>=0 && d<int(profile.size()));++hist[d];}
        assert(hist==profile);
    }
    cout << "C++17 checker PASS: 84 minimum sets of weight 8, 168 jump edges, 0 slide edges, diameter 7; all 16384 subsets checked\n";
}
