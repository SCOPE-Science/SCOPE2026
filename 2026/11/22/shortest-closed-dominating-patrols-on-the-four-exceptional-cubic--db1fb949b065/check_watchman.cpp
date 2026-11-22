// Exact enumerator for all closed dominating walks up to the first optimum.
// Standard C++17, no third-party libraries. Compile: c++ -O2 -std=c++17 check_watchman.cpp -o check_watchman
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <utility>
#include <vector>
using namespace std;
struct G {
    int n;
    vector<vector<int>> adj;
    explicit G(int n):n(n),adj(n){}
    void edge(int u,int v){
        assert(u!=v && u>=0 && v>=0 && u<n && v<n);
        if (find(adj[u].begin(),adj[u].end(),v)==adj[u].end()) {
            adj[u].push_back(v); adj[v].push_back(u);
        }
    }
    void finish(){for(auto &a:adj){sort(a.begin(),a.end());assert(a.size()==3);}}
};
G lcf(int n, vector<int> off) {
    G g(n);
    for(int i=0;i<n;++i){g.edge(i,(i+1)%n);int v=(i+off[i%off.size()]+n*10)%n;g.edge(i,v);}
    g.finish(); return g;
}
G gp(int n,int k){
    G g(2*n);
    for(int i=0;i<n;++i){g.edge(i,(i+1)%n);g.edge(i,i+n);g.edge(i+n,n+(i+k)%n);}
    g.finish();return g;
}
vector<int> canonical(const vector<int>& p) {
    assert(p.front()==p.back());
    vector<int> x(p.begin(),p.end()-1),best=x;
    int L=(int)x.size();
    for(int dir=0;dir<2;++dir){
      for(int k=0;k<L;++k){
        vector<int> cur;cur.reserve(L);
        for(int i=0;i<L;++i)cur.push_back(x[(i+k)%L]);
        if(cur<best)best=cur;
      }
      reverse(x.begin(),x.end());
    }
    return best;
}
struct Summary{
    vector<int> maxima;
    vector<long long> roots;
    set<vector<int>> dihedral;
    map<pair<int,int>,int> types;
};
Summary enum_walks(G const&g,int L){
    Summary R;R.maxima.assign(L+1,0);R.roots.assign(L+1,0);
    vector<uint32_t> neighborhoods(g.n,0);
    uint32_t all=(1u<<g.n)-1;
    for(int i=0;i<g.n;++i){
        uint32_t mask=(1u<<i);
        for(int j:g.adj[i])mask|=1u<<j;
        neighborhoods[i]=mask;
    }
    vector<int> p;
    auto rec=[&](auto&&self,int s,int v,int d,uint32_t seen)->void {
        if(d>0 && d%2==0 && v==s){
            R.maxima[d]=max(R.maxima[d],__builtin_popcount(seen));
            if(seen==all){
                ++R.roots[d];
                if(d==L){
                    auto ca=canonical(p);
                    if(R.dihedral.insert(ca).second){
                        set<int> vs(ca.begin(),ca.end());
                        set<pair<int,int>> es;
                        for(int t=0;t<L;++t){int a=ca[t],b=ca[(t+1)%L];if(a>b)swap(a,b);es.insert({a,b});}
                        ++R.types[{(int)vs.size(),(int)es.size()}];
                    }
                }
            }
        }
        if(d==L)return;
        for(int w:g.adj[v]){p.push_back(w);self(self,s,w,d+1,seen|neighborhoods[w]);p.pop_back();}
    };
    for(int s=0;s<g.n;++s){p={s};rec(rec,s,s,0,neighborhoods[s]);}
    return R;
}
int main(){
    struct Case{string name;G g;int L;long long rooted;int dihedral;map<pair<int,int>,int> types;};
    vector<Case> cases={
      {"Heawood",lcf(14,{5,-5}),10,10920,546,{{{6,5},42},{{8,8},420},{{10,10},84}}},
      {"Mobius-Kantor",gp(8,3),8,96,6,{{{8,8},6}}},
      {"Pappus",lcf(18,{5,7,-7,7,-7,-5}),12,5400,225,{{{10,10},108},{{12,12},117}}},
      {"Desargues",gp(10,3),10,240,12,{{{10,10},12}}},
    };
    for(auto &c:cases){
       Summary r=enum_walks(c.g,c.L);
       assert(r.roots[c.L]==c.rooted);
       assert((int)r.dihedral.size()==c.dihedral);
       assert(r.types==c.types);
       for(int d=2;d<c.L;d+=2)assert(r.roots[d]==0);
       cout<<c.name<<" n="<<c.g.n<<" optimum="<<c.L<<" rooted="<<r.roots[c.L]
           <<" dihedral="<<r.dihedral.size()<<" max_coverage=";
       for(int d=2;d<=c.L;d+=2)cout<<d<<":"<<r.maxima[d]<<" ";
       cout<<" support_types=";
       for(auto const &[p,v]:r.types)cout<<"("<<p.first<<","<<p.second<<"):"<<v<<" ";
       cout<<"\n";
    }
    cout<<"ALL PASS\n";
}
