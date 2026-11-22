// Finite exhaustive verification of 4-game-chromatic vertex-deletion robustness.
// Scientific content only. C++17: g++ -std=c++17 -O2 game_color_check.cpp -o game_color_check
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <unordered_map>
#include <utility>
#include <vector>
using namespace std;
using Graph = vector<vector<int>>;
Graph make_grotzsch() {
    Graph a(11);
    auto edge=[&](int x,int y){a[x].push_back(y);a[y].push_back(x);};
    for (int i=0;i<5;i++) edge(i,(i+1)%5);
    for (int i=0;i<5;i++) {
        edge(5+i,(i+4)%5);
        edge(5+i,(i+1)%5);
        edge(5+i,10);
    }
    return a;
}
Graph make_chvatal() {
    Graph a(12);
    const int e[][2]={
       {0,1},{0,4},{0,6},{0,9},
       {1,2},{1,5},{1,7},
       {2,3},{2,6},{2,8},
       {3,4},{3,7},{3,9},
       {4,5},{4,8},
       {5,10},{5,11},
       {6,10},{6,11},
       {7,8},{7,11},
       {8,10},
       {9,10},{9,11}
    };
    for (auto &p:e){a[p[0]].push_back(p[1]);a[p[1]].push_back(p[0]);}
    return a;
}
Graph deletion(const Graph &g,int omit) {
    Graph h(g.size()-(omit>=0));
    auto j=[&](int x){return x-(omit>=0&&x>omit);};
    for(int v=0;v<(int)g.size();v++) if(v!=omit)
      for(int w:g[v]) if(w!=omit) h[j(v)].push_back(j(w));
    return h;
}
struct Solver {
    Graph g;int k;unordered_map<uint64_t,uint8_t> memo;uint64_t explored=0;
    explicit Solver(Graph h,int t):g(move(h)),k(t){}
    uint64_t canonical(const vector<uint8_t>&s)const {
        int next=0;int mapping[6]={0};uint64_t code=0;
        for(int v=0;v<(int)s.size();v++){
            int c=s[v];
            if(c && !mapping[c]) mapping[c]=++next;
            code |= uint64_t(c?mapping[c]:0)<<(3*v);
        }
        return code;
    }
    bool eval(vector<uint8_t>&s,int filled){
        explored++;
        if(filled==(int)s.size()) return true;
        // A vertex with no available colours makes final completion impossible.
        vector<pair<int,int>> moves;
        for(int v=0;v<(int)s.size();v++) if(s[v]==0){
            int banned=0;
            for(int w:g[v]) if(s[w]) banned|=1<<(s[w]-1);
            int free=((1<<k)-1)&~banned;
            if(!free) return false;
            moves.emplace_back(v,free);
        }
        uint64_t code=canonical(s);
        auto hit=memo.find(code);if(hit!=memo.end())return hit->second;
        bool alice=(filled%2==0);
        bool result=!alice;
        for(auto [v,mask]:moves) for(int c=1;c<=k;c++) if(mask&(1<<(c-1))){
            s[v]=c;
            bool next=eval(s,filled+1);
            s[v]=0;
            if(alice==next){result=alice;goto done;}
        }
        done: memo.emplace(code,static_cast<uint8_t>(result));
        return result;
    }
    bool solve(){vector<uint8_t>s(g.size());return eval(s,0);}
};
bool proper_coloring_exists(const Graph &g,int k){
    vector<int> order(g.size());iota(order.begin(),order.end(),0);
    stable_sort(order.begin(),order.end(),[&](int a,int b){return g[a].size()>g[b].size();});
    vector<int> state(g.size());
    auto rec=[&](auto&&rec,int step)->bool{
        if(step==(int)g.size())return true;
        int v=order[step];
        for(int c=1;c<=k;c++){
            bool ok=true;for(int w:g[v])if(state[w]==c)ok=false;
            if(ok){state[v]=c;if(rec(rec,step+1))return true;state[v]=0;}
        }
        return false;
    };
    return rec(rec,0);
}
int main(){
    for(auto item:vector<pair<const char*,Graph>>{{"Grotzsch",make_grotzsch()},{"Chvatal",make_chvatal()}}){
       const auto &g=item.second;
       cout<<item.first<<" n="<<g.size()<<" m=";
       int es=0;for(int i=0;i<(int)g.size();i++)for(int j:g[i]){
          assert(i!=j && find(g[j].begin(),g[j].end(),i)!=g[j].end());
          if(j>i)es++;
       }
       cout<<es<<"\n";
       assert(!proper_coloring_exists(g,3));
       assert(proper_coloring_exists(g,4));
       Solver four(g,4);
       assert(four.solve());
       cout<<"whole chi=4 game_chi=4 states4="<<four.memo.size()<<"\n";
       for(int omit=0;omit<(int)g.size();omit++){
          Graph h=deletion(g,omit);
          assert(!proper_coloring_exists(h,2));
          assert(proper_coloring_exists(h,3));
          Solver three(h,3),fourh(h,4);
          bool a=three.solve(), b=fourh.solve();
          cout<<"delete "<<omit<<" chi=3 game3="<<a<<" game4="<<b
               <<" states3="<<three.memo.size()<<" states4="<<fourh.memo.size()<<"\n";
          assert(!a&&b);
       }
    }
    cout<<"ALL CHECKS PASS\n";
}
