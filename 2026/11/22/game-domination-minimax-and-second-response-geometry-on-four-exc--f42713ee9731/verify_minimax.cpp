// Exact finite certificate for ordinary domination-game minimax.
// C++17, no third-party libraries; independent bottom-up computation.
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <tuple>
#include <vector>
using namespace std;
struct Graph { string name; int n; vector<pair<int,int>> e; };
Graph make_graph(int which){
    Graph g;g.name=vector<string>{"heawood","mobius_kantor","pappus","desargues"}[which];
    if(which==0){
        g.n=14;
        for(int i=0;i<7;++i) for(int d: {0,1,3}) g.e.emplace_back(i,7+(i+d)%7);
    }else if(which==1){
        g.n=16;
        for(int i=0;i<8;++i){
            g.e.emplace_back(i,(i+1)%8);
            g.e.emplace_back(i,8+i);
            g.e.emplace_back(8+i,8+(i+3)%8);
        }
    }else if(which==2){
        g.n=18;
        for(int x=0;x<3;++x)for(int y=0;y<3;++y){
            int p=3*x+y;
            g.e.emplace_back(p,9+x);
            g.e.emplace_back(p,12+y);
            g.e.emplace_back(p,15+(x+y)%3);
        }
    }else{
        g.n=20;
        vector<int> pairs,triples;
        for(int m=0;m<32;++m) {
            if(__builtin_popcount((unsigned)m)==2) pairs.push_back(m);
            if(__builtin_popcount((unsigned)m)==3) triples.push_back(m);
        }
        for(int i=0;i<10;++i) for(int j=0;j<10;++j)
            if((pairs[i]&triples[j])==pairs[i]) g.e.emplace_back(i,10+j);
    }
    return g;
}
int main(){
    for(int which=0;which<4;++which){
        Graph g=make_graph(which);int n=g.n;
        vector<unsigned> hood(n);vector<vector<int>> adj(n);
        for(int u=0;u<n;++u)hood[u]=(1u<<u);
        set<pair<int,int>> unique_edges;
        for(auto [u,v]:g.e){
            if(u>v)swap(u,v);
            assert(u!=v && u>=0 && v<n);
            assert(unique_edges.insert({u,v}).second);
            adj[u].push_back(v);adj[v].push_back(u);
            hood[u]|=(1u<<v);hood[v]|=(1u<<u);
        }
        assert((int)unique_edges.size()==3*n/2);
        for(int u=0;u<n;++u)assert(adj[u].size()==3);
        // Independently compute every possible dominated-set state in decreasing-mask order.
        size_t count=1u<<n;vector<unsigned char> d(count),s(count);
        for(int m=(int)count-2;m>=0;--m){
            int bestd=100,bests=-1;
            for(unsigned h:hood){
                unsigned next=(unsigned)m|h;
                if(next==(unsigned)m)continue;
                bestd=min(bestd,1+(int)s[next]);
                bests=max(bests,1+(int)d[next]);
            }
            assert(bestd!=100 && bests>=0 && bestd<=n && bests<=n);
            d[m]=(unsigned char)bestd;s[m]=(unsigned char)bests;
        }
        vector<int> distance(n,-1);queue<int>q;distance[0]=0;q.push(0);
        while(!q.empty()){
            int v=q.front();q.pop();
            for(int w:adj[v])if(distance[w]<0){distance[w]=distance[v]+1;q.push(w);}
        }
        for(int dd:distance)assert(dd>=0);
        // Each vertex is an equivalent initial move, checked without assuming symmetry.
        for(int v=0;v<n;++v){
            assert(1+s[hood[v]]==d[0]);
            assert(1+d[hood[v]]==s[0]);
        }
        cout << g.name << " " << (int)d[0] << " " << (int)s[0] << "\n";
        for(int first=0;first<=1;++first){
            map<pair<int,int>,int> tally;
            for(int v=0;v<n;++v){
                auto next=hood[0]|hood[v];
                if(next==hood[0])continue;
                int cost=2+(first==0?(int)d[next]:(int)s[next]);
                ++tally[{distance[v],cost}];
            }
            cout << (first==0?"dominator":"staller");
            for(auto const& [key,multiplicity]:tally)
                cout<<" "<<key.first<<":"<<key.second<<"="<<multiplicity;
            cout<<"\n";
        }
    }
    cout<<"CPP_VERIFICATION_OK\n";
}
