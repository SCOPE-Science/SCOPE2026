// Exhaustive independent check of skew-zero-forcing enumerators and exchange data.
// Compile: c++ -std=c++17 -O2 -Wall -Wextra -pedantic verify.cpp -o verify && ./verify
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
struct Graph {int n; vector<uint32_t> adj; Graph(int n):n(n),adj(n,0){}
    void edge(int a,int b){assert(a!=b && 0<=a && a<n && 0<=b && b<n);
        adj[a]|=uint32_t(1)<<b;adj[b]|=uint32_t(1)<<a;}
};
Graph make_graph(int id){
 if(id==0){Graph g(14);for(int i=0;i<7;i++)for(int j=0;j<7;j++){
   int d=(j-i+7)%7;if(d==0||d==1||d==3)g.edge(i,7+j);}return g;}
 if(id==1){Graph g(16);for(int i=0;i<8;i++){
    g.edge(i,(i+1)%8);g.edge(i,8+i);g.edge(8+i,8+(i+3)%8);}return g;}
 if(id==2){Graph g(18);for(int x=0;x<3;x++)for(int y=0;y<3;y++){
   int u=3*x+y;g.edge(u,9+x);g.edge(u,12+y);g.edge(u,15+(y-x+3)%3);}return g;}
 Graph g(20);vector<int> p2,p3;
 for(int m=0;m<(1<<5);m++){int k=__builtin_popcount((unsigned)m);
    if(k==2)p2.push_back(m);
    if(k==3)p3.push_back(m);}
 assert(p2.size()==10&&p3.size()==10);
 for(int i=0;i<10;i++)for(int j=0;j<10;j++)
    if((p2[i]&p3[j])==p2[i])g.edge(i,j+10);
 return g;
}
bool force_closure(const Graph&g,uint32_t seed){
 const uint32_t full=(uint32_t(1)<<g.n)-1;uint32_t black=seed;
 while(true){uint32_t whites=full&~black, newbits=0;
   for(int i=0;i<g.n;i++){
     uint32_t t=g.adj[i]&whites;
     if(t && !(t&(t-1)))newbits|=t;
   }
   if(!newbits)return black==full;
   black|=newbits;
 }
}
vector<vector<int>> shores(const Graph&g){
 vector<int> c(g.n,-1);queue<int> q;q.push(0);c[0]=0;
 while(!q.empty()){
   int u=q.front();q.pop();for(int v=0;v<g.n;v++)if((g.adj[u]>>v)&1){
     if(c[v]<0){c[v]=1-c[u];q.push(v);}else assert(c[v]!=c[u]);
   }
 }
 vector<vector<int>> s(2);for(int i=0;i<g.n;i++){assert(c[i]>=0);s[c[i]].push_back(i);}
 assert(s[0].size()==s[1].size());return s;
}
uint32_t to_global(int mask,const vector<int>&shore){uint32_t out=0;
 for(int i=0;i<(int)shore.size();i++)if(mask>>i&1)out|=uint32_t(1)<<shore[i];
 return out;
}
// Independently compute one-shore closure using globally numbered forcing vertices.
bool shore_force(const Graph&g,uint32_t seed,uint32_t shore){
 uint32_t black=seed;
 while(true){uint32_t white=shore&~black, update=0;
   for(int i=0;i<g.n;i++)if(!(shore&(uint32_t(1)<<i))){
      uint32_t hit=g.adj[i]&white;
      if(hit&&!(hit&(hit-1)))update|=hit;
   }
   if(!update)return black==shore;
   black|=update;
 }
}
struct Edges {int edgeCount;map<int,int> degrees,ecc;};
Edges compute_exchanges(const vector<int>&bases){
 int n=bases.size();vector<vector<int>> nb(n);
 for(int i=0;i<n;i++)for(int j=i+1;j<n;j++){
   if(__builtin_popcount((unsigned)(bases[i]^bases[j]))==2){nb[i].push_back(j);nb[j].push_back(i);}
 }
 Edges d{};
 for(int i=0;i<n;i++){
   d.degrees[(int)nb[i].size()]++;d.edgeCount+=nb[i].size();
   vector<int> dist(n,-1);queue<int> q;dist[i]=0;q.push(i);
   while(!q.empty()){
     int a=q.front();q.pop();for(int b:nb[a])if(dist[b]<0){dist[b]=dist[a]+1;q.push(b);}
   }
   int e=0;for(int j=0;j<n;j++){
      assert(dist[j]>=0);assert(dist[j]==__builtin_popcount((unsigned)(bases[i]^bases[j]))/2);
      e=max(e,dist[j]);
   }
   d.ecc[e]++;
 }
 d.edgeCount/=2;return d;
}
int main(){
 const array<string,4> names={"Heawood","Mobius-Kantor","Pappus","Desargues"};
 const array<vector<int>,4> expect={{
    {0,0,0,28,35,21,7,1},
    {0,0,0,48,70,56,28,8,1},
    {0,0,0,72,126,126,84,36,9,1},
    {0,0,0,0,125,222,205,120,45,10,1}
 }};
 const array<int,4> minOpt={28,48,72,125}, exEdges={126,300,540,930};
 const array<map<int,int>,4> exEcc={map<int,int>{{3,28}},
   map<int,int>{{3,48}},map<int,int>{{3,72}},map<int,int>{{3,5},{4,120}}};
 const array<map<int,int>,4> exDegrees={map<int,int>{{9,28}},map<int,int>{{12,24},{13,24}},
   map<int,int>{{15,72}},map<int,int>{{12,5},{14,60},{16,60}}};
 for(int id=0;id<4;id++){
  auto g=make_graph(id);auto sides=shores(g);assert((int)sides[0].size()==7+id);
  vector<vector<int>> basePair;vector<vector<int>> allPoly;
  for(auto &side:sides){
    int m=side.size();vector<int> coeff(m+1,0),bases;uint32_t full=to_global((1<<m)-1,side);
    for(int s=0;s<(1<<m);s++){
      bool ok=shore_force(g,to_global(s,side),full);
      if(ok){int card=__builtin_popcount((unsigned)s);coeff[card]++;
         if(card==(id==3?4:3))bases.push_back(s);}
    }
    assert(coeff==expect[id]);assert((int)bases.size()==minOpt[id]);
    auto e=compute_exchanges(bases);assert(e.edgeCount==exEdges[id]);
    assert(e.degrees==exDegrees[id]);assert(e.ecc==exEcc[id]);
    basePair.push_back(bases);allPoly.push_back(coeff);
  }
  // Direct full-graph exhaustion, independent of the one-shore factorization.
  vector<int64_t> fullcounts(g.n+1,0);
  for(uint32_t s=0;s<(uint32_t(1)<<g.n);s++)if(force_closure(g,s))
       fullcounts[__builtin_popcount(s)]++;
  vector<int64_t> conv(g.n+1,0);
  for(int i=0;i<(int)allPoly[0].size();i++)for(int j=0;j<(int)allPoly[1].size();j++)
       conv[i+j]+=(int64_t)allPoly[0][i]*allPoly[1][j];
  assert(fullcounts==conv);
  int nopt=minOpt[id]*minOpt[id], nedges=2*minOpt[id]*exEdges[id];
  std::cout<<names[id]<<" min="<<(id==3?8:6)<<" optima="<<nopt
       <<" exchange_edges="<<nedges<<" full_enumerator_verified=yes\n";
 }
 cout<<"ALL C++ CHECKS PASSED\n";
}
