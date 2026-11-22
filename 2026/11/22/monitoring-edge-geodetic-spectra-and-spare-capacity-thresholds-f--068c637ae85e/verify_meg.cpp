// Exact finite checker for monitoring-edge-geodetic sets in GP(5,2), GP(10,2), GP(10,3).
// C++17: g++ -O2 -std=c++17 verify_meg.cpp -o verify_meg && ./verify_meg
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <queue>
#include <stdexcept>
#include <vector>
using namespace std;
struct Graph { int n; vector<pair<int,int>> e; vector<vector<int>> adj; };
Graph gp(int n,int k){
 Graph g{2*n,{},vector<vector<int>>(2*n)};
 auto add=[&](int a,int b){ if(a>b)swap(a,b);for(auto c:g.e)if(c==make_pair(a,b))throw runtime_error("duplicate edge");g.e.push_back({a,b});g.adj[a].push_back(b);g.adj[b].push_back(a);};
 for(int i=0;i<n;i++){ add(i,(i+1)%n);add(i,i+n);add(i+n,(i+k)%n+n); }
 sort(g.e.begin(),g.e.end());return g;
}
vector<vector<int>> distances(const Graph&g,int removed=-1){
 vector<vector<int>> d(g.n,vector<int>(g.n,999));
 for(int i=0;i<g.n;i++){
  queue<int>q;d[i][i]=0;q.push(i);
  while(!q.empty()){
   int u=q.front();q.pop();for(int v:g.adj[u]){
    if(removed>=0 && (min(u,v)==g.e[removed].first && max(u,v)==g.e[removed].second))continue;
    if(d[i][v]>d[i][u]+1){d[i][v]=d[i][u]+1;q.push(v);}
   }
  }
 }
 return d;
}
struct Stats {vector<uint64_t> histogram; vector<uint64_t> minhist; int minimum; vector<uint32_t> optima; vector<uint64_t> coverage; vector<unsigned char> valid;};
Stats analyze(const Graph&g){
 int n=g.n,ec=g.e.size();if(n>20||ec>63)throw runtime_error("oversized");
 auto orig=distances(g);vector<vector<uint64_t>> uv(n,vector<uint64_t>(n,0));
 for(int i=0;i<ec;i++){
  auto after=distances(g,i);
  for(int u=0;u<n;u++)for(int v=u+1;v<n;v++)
   if(after[u][v]>orig[u][v])uv[u][v] |= 1ULL<<i,uv[v][u] |= 1ULL<<i;
 }
 int lim=1<<n;uint64_t full=(1ULL<<ec)-1;
 vector<uint64_t> cover(lim,0),hist(n+1,0),minimal(n+1,0);
 vector<unsigned char> valid(lim,0);int minsize=n+1;vector<uint32_t> optima;
 for(int m=1;m<lim;m++){
  int i=__builtin_ctz((unsigned)m),rest=m&(m-1);uint64_t c=cover[rest];
  for(int r=rest;r;r&=r-1){int j=__builtin_ctz((unsigned)r);c|=uv[i][j];}
  cover[m]=c;
  if(c==full){int k=__builtin_popcount((unsigned)m);valid[m]=1;hist[k]++;
   if(k<minsize){minsize=k;optima.clear();}if(k==minsize)optima.push_back(m);
  }
 }
 for(int m=1;m<lim;m++)if(valid[m]){
  bool min=true;
  for(int r=m;r;r&=r-1){int i=__builtin_ctz((unsigned)r);if(valid[m^(1<<i)]){min=false;break;}}
  if(min)minimal[__builtin_popcount((unsigned)m)]++;
 }
 return {hist,minimal,minsize,optima,cover,valid};
}
vector<pair<int,int>> components(const Stats&s,int n,int budget){
 int lim=1<<n;vector<unsigned char> vis(lim,0);vector<int> sizes;
 for(int m=0;m<lim;m++)if(s.valid[m]&&!vis[m]&&__builtin_popcount((unsigned)m)<=budget){
  queue<int>q;q.push(m);vis[m]=1;int size=0;
  while(!q.empty()){int u=q.front();q.pop();size++;
   for(int i=0;i<n;i++){
    int v=u^(1<<i);
    if(s.valid[v]&&!vis[v]&&__builtin_popcount((unsigned)v)<=budget){vis[v]=1;q.push(v);}
   }
  }
  sizes.push_back(size);
 }
 sort(sizes.begin(),sizes.end());vector<pair<int,int>> out;
 for(int size:sizes){if(out.empty()||out.back().first!=size)out.push_back({size,1});else out.back().second++;}
 return out;
}
int main(){
 struct Expected {int n,k,mu;vector<uint64_t> poly,minimals;int independent,matching3;vector<pair<int,vector<pair<int,int>>>> cc;};
 vector<Expected> expected={
 {5,2,6,{0,0,0,0,0,0,5,30,30,10,1},{0,0,0,0,0,0,5,10,0,0,0},0,0,{{6,{{1,5}}},{7,{{1,10},{5,5}}},{8,{{65,1}}}}},
 {10,2,8,{0,0,0,0,0,0,0,0,25,1840,13686,37020,54000,49880,31650,14392,4765,1140,190,20,1},{0,0,0,0,0,0,0,0,25,1540,2006,0,0,0,0,0,0,0,0,0,0},5,20,{{8,{{1,25}}},{9,{{1,1540},{13,25}}},{10,{{1,2006},{13545,1}}},{11,{{52571,1}}}}},
 {10,3,10,{0,0,0,0,0,0,0,0,0,0,2,20,115,480,1320,1924,1510,660,160,20,1},{0,0,0,0,0,0,0,0,0,0,2,0,25,60,100,0,0,0,0,0,0},2,0,{{10,{{1,2}}},{11,{{11,2}}},{12,{{1,25},{56,2}}},{13,{{1,60},{9,5},{256,2}}},{14,{{1,100},{1837,1}}},{15,{{3861,1}}}}}
 };
 for(auto ex:expected){
  auto g=gp(ex.n,ex.k);if(int(g.e.size())!=3*ex.n)throw runtime_error("degree");
  auto s=analyze(g);if(s.minimum!=ex.mu||s.histogram!=ex.poly||s.minhist!=ex.minimals)throw runtime_error("census mismatch");
  int indep=0,matching3=0;for(auto mask:s.optima){
   vector<int> deg(g.n,0);int ecount=0;for(auto [u,v]:g.e)if((mask>>u&1)&&(mask>>v&1))deg[u]++,deg[v]++,ecount++;
   int maxdeg=*max_element(deg.begin(),deg.end());
   if(ecount==0)indep++;
   if(ecount==3&&maxdeg==1)matching3++;
  }
  if(ex.n==10&& (indep!=ex.independent||matching3!=ex.matching3))throw runtime_error("optimum geometry mismatch");
  if(ex.n==5){auto g0=gp(5,2);for(int m:s.optima){int notm=((1<<g.n)-1)^m;for(auto [u,v]:g.e)if((notm>>u&1)&&(notm>>v&1))throw runtime_error("Petersen complement not independent");}}
  if(ex.k==3){
   uint32_t p0=0,p1=0;for(int i=0;i<10;i++){p0|=1U<<(i%2==0?i:i+10);p1|=1U<<(i%2==0?i+10:i);}
   if(find(s.optima.begin(),s.optima.end(),p0)==s.optima.end()||find(s.optima.begin(),s.optima.end(),p1)==s.optima.end())throw runtime_error("Desargues shore mismatch");
  }
  for(auto [b,expect]:ex.cc){auto actual=components(s,g.n,b);if(actual!=expect){cerr<<"components failed at "<<ex.n<<","<<ex.k<<","<<b<<"\n";for(auto [sz,cnt]:actual)cerr<<sz<<":"<<cnt<<" ";cerr<<"\n";throw runtime_error("connectivity mismatch");}}
  cout<<"GP("<<ex.n<<","<<ex.k<<") min="<<s.minimum<<" optima="<<s.optima.size()<<" total="<<accumulate(s.histogram.begin(),s.histogram.end(),0ULL)<<" verified\n";
 }
 cout<<"MEG_ALL_CHECKS_OK\n";
}
