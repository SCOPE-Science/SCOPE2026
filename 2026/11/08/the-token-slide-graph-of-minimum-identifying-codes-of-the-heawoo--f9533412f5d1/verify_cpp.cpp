// Self-contained independent finite verification of minimum identifying-code reconfiguration.
// Compile: c++ -std=c++17 -O2 -Wall -Wextra verify_cpp.cpp -o verify_cpp
// Run with states.txt, jumps.txt, slides.txt in the current working directory.
#include <algorithm>
#include <array>
#include <cassert>
#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <string>
#include <utility>
#include <vector>
using namespace std;

static array<unsigned,14> nbr{};
static array<unsigned,14> ball{};
static int pop(unsigned x) { return __builtin_popcount(x); }
static bool valid(unsigned bits) {
    array<unsigned,14> observations{};
    for (int x=0;x<14;++x) {
        unsigned b=bits & ball[x];
        if (b==0) return false;
        observations[x]=b;
    }
    for (int i=0;i<14;++i)
        for (int j=i+1;j<14;++j)
            if (observations[i]==observations[j]) return false;
    return true;
}
static vector<int> read_states() {
    ifstream in("states.txt"); assert(in.good());
    vector<int> a; int x;
    while(in>>x) a.push_back(x);
    assert(in.eof()); return a;
}
static vector<pair<int,int>> read_edges(string path) {
    ifstream in(path); assert(in.good());
    vector<pair<int,int>> a; int x,y;
    while(in>>x>>y) a.push_back({x,y});
    assert(in.eof()); return a;
}
struct Stats {
    int size=0, edges=0;
    map<int,int> degrees, eccentricities, pair_dists;
};
static vector<Stats> compute_stats(const vector<int>& states, const vector<pair<int,int>>& edges) {
    vector<vector<int>> ad(states.size());
    map<int,int> index;
    for (size_t i=0;i<states.size();++i) index[states[i]]=int(i);
    for (auto [a,b]:edges) {
        int u=index.at(a),v=index.at(b);
        ad[u].push_back(v);ad[v].push_back(u);
    }
    vector<int> flag(states.size(),0);
    vector<Stats> result;
    for (size_t i=0;i<states.size();++i) {
        if (flag[i]) continue;
        vector<int> component{int(i)};flag[i]=1;
        for (size_t k=0;k<component.size();++k) {
            int v=component[k];
            for (int w:ad[v]) if(!flag[w]) {flag[w]=1;component.push_back(w);}
        }
        Stats st; st.size=int(component.size());
        for (int u:component) {st.degrees[int(ad[u].size())]++;st.edges+=int(ad[u].size());}
        st.edges/=2;
        for (int u:component) {
            vector<int> dist(states.size(),-1);
            queue<int> q;
            dist[u]=0;q.push(u);
            while(!q.empty()) {
                int x=q.front();q.pop();
                for(int y:ad[x]) if(dist[y]==-1){dist[y]=dist[x]+1;q.push(y);}
            }
            int eccentricity=0;
            for (int v:component) {
                assert(dist[v]>=0);
                eccentricity=max(eccentricity,dist[v]);
                if (u<v) ++st.pair_dists[dist[v]];
            }
            ++st.eccentricities[eccentricity];
        }
        result.push_back(st);
    }
    sort(result.begin(),result.end(),[](const Stats& a,const Stats& b) {
        if(a.size!=b.size)return a.size<b.size;
        return a.edges<b.edges;
    });
    return result;
}
int main() {
    // Each line j is incident with the points j, j+1, j+3 modulo seven.
    for(int line=0;line<7;++line)
        for (int step: {0,1,3}) {
            int p=(line+step)%7, l=line+7;
            nbr[p] |= 1u<<l; nbr[l] |= 1u<<p;
        }
    for(int v=0;v<14;++v) ball[v]=nbr[v]|(1u<<v);
    for(int i=0;i<7;++i)
        for(int j=i+1;j<7;++j)
            assert(pop(nbr[i]&nbr[j])==1);
    array<int,8> count{};
    vector<int> states;
    for(unsigned m=0;m<(1u<<14);++m) {
        int k=pop(m);
        if(k<=7 && valid(m)) {++count[k];if(k==7)states.push_back(int(m));}
    }
    for(int k=0;k<7;++k)assert(count[k]==0);
    assert(count[7]==268);
    assert(states==read_states());
    vector<pair<int,int>> jumps, slides;
    for(size_t i=0;i<states.size();++i)
        for(size_t j=i+1;j<states.size();++j) {
            int a=states[i],b=states[j];
            unsigned delta=unsigned(a^b);
            if(pop(delta)!=2)continue;
            jumps.push_back({a,b});
            int removed=__builtin_ctz(unsigned(a & ~b));
            int inserted=__builtin_ctz(unsigned(b & ~a));
            if((nbr[removed]>>inserted)&1u)slides.push_back({a,b});
        }
    assert(jumps.size()==658 && slides.size()==210);
    assert(jumps==read_edges("jumps.txt"));
    assert(slides==read_edges("slides.txt"));
    auto jstat=compute_stats(states,jumps);
    assert(jstat.size()==3);
    for(int k=0;k<2;++k) {
        assert(jstat[k].size==22 && jstat[k].edges==63);
        assert((jstat[k].degrees==map<int,int>{{5,21},{21,1}}));
        assert((jstat[k].eccentricities==map<int,int>{{1,1},{2,21}}));
    }
    auto large=jstat.back();
    assert(large.size==224 && large.edges==532);
    assert((large.degrees==map<int,int>{{4,56},{5,168}}));
    assert((large.eccentricities==map<int,int>{{6,224}}));
    assert((large.pair_dists==map<int,int>{{1,532},{2,1848},{3,5376},{4,10332},{5,6216},{6,672}}));
    auto sstat=compute_stats(states,slides);
    assert(sstat.size()==58);
    for(int i=0;i<56;++i) {
        assert(sstat[i].size==4 && sstat[i].edges==3);
        assert((sstat[i].degrees==map<int,int>{{1,3},{3,1}}));
    }
    for(int i=56;i<58;++i) {
        assert(sstat[i].size==22 && sstat[i].edges==21);
        assert((sstat[i].degrees==map<int,int>{{1,21},{21,1}}));
    }
    cout<<"CPP_VERIFY_OK codes=268 jumps=658 jump_components=22,22,224 slides=210 slide_components=56*K1,3+2*K1,21 main_radius=6 main_diameter=6\n";
}
