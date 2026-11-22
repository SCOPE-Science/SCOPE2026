// Independent finite-check program: affine coordinates, explicit incidence edges,
// and a disjoint-set-union connectivity predicate. No external libraries.
// Build: c++ -std=c++17 -O2 verify_plane_census.cpp -o verify_plane_census
#include <iostream>
#include <vector>
#include <map>
#include <tuple>
#include <cassert>
#include <cstdint>
using namespace std;
struct UnionFind {
    int p[26];
    explicit UnionFind(int n) {for(int i=0;i<n;i++)p[i]=i;}
    int root(int x) {while(p[x]!=x){p[x]=p[p[x]];x=p[x];}return x;}
    void join(int x,int y) {x=root(x); y=root(y);if(x!=y)p[x]=y;}
};
struct Graph {
    int q,N;
    vector<pair<int,int>> edges;
    explicit Graph(int t):q(t),N(t*t+t+1) {
       // Point indices: q*x+y for affine (x,y); infinity points q*q+slope.
       // Line indices: q*m+b for affine y=m*x+b;
       // q*q+b for vertical x=b; N-1 for line at infinity.
       for(int x=0;x<q;x++)for(int y=0;y<q;y++) {
          int point=q*x+y;
          for(int m=0;m<q;m++) {
             int b=(y-m*x)%q;if(b<0)b+=q;
             edges.emplace_back(point, N+q*m+b);
          }
          edges.emplace_back(point,N+q*q+x);
       }
       for(int m=0;m<q;m++)for(int b=0;b<q;b++) {
          edges.emplace_back(q*q+m,N+q*m+b);
       }
       for(int b=0;b<q;b++)edges.emplace_back(q*q+q,N+q*q+b);
       for(int point=q*q;point<N;point++)edges.emplace_back(point,N+N-1);
       assert(int(edges.size())==N*(q+1));
    }
    bool weakly_connected(uint32_t s) const {
        if(!s)return false;
        UnionFind uf(2*N);
        for(auto [a,b]:edges)if((s>>a&1u)||(s>>b&1u))uf.join(a,b);
        int base=uf.root(0);
        for(int v=1;v<2*N;v++)if(uf.root(v)!=base)return false;
        return true;
    }
    int incidences(uint32_t s) const {
        int k=0;
        for(auto [a,b]:edges)k+=(s>>a&1u) && (s>>b&1u);
        return k;
    }
};
int main(){
    for(int q: {2,3}) {
        Graph g(q);
        int N=g.N,k0=2*q+1;
        map<tuple<int,int,int>,long> counts;
        for(int k=0;k<=k0;k++) {
          uint32_t s=(1u<<k)-1;
          long total=0;
          uint32_t end=(1u<<(2*N))-1;
          while(s<=end) {
             if(g.weakly_connected(s)) {
                total++;
                if(k==k0) {
                    int points=__builtin_popcount(s&((1u<<N)-1));
                    counts[{points,k-points,g.incidences(s)}]++;
                }
             }
             uint32_t smallest=s&-s, added=s+smallest;
             if(s==0||added==0)break;
             s=added|(((added^s)>>2)/smallest);
          }
          if(k<k0)assert(total==0);
          else assert(total==2*N*(q+1)*(q*q+1));
        }
        for(int p: {q,q+1}) {
            int b=k0-p;
            assert((counts[{p,b,1}]==N*(q+1)*q*q));
            assert((counts[{p,b,q}]==N*(q+1)));
        }
        assert(counts.size()==4);
        cout<<"q="<<q<<" minimum="<<k0<<" total="<<2*N*(q+1)*(q*q+1)
            <<" e=1="<<2*N*(q+1)*q*q<<" e=q="<<2*N*(q+1)<<" OK\n";
    }
}
