#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <queue>
#include <vector>
// Independent direct-swap enumeration of all security conditions.
// Compile: c++ -std=c++17 -O2 independent_check.cpp -o check && ./check
using namespace std;
constexpr int N = 18, TOTAL = 1 << N;
int main() {
 array<int,N> adj{};
 auto point=[](int x,int y){return 3*x+y;};
 auto line=[](int m,int b){return 9+3*m+b;};
 for (int x=0;x<3;++x) for (int y=0;y<3;++y)
  for (int m=0;m<3;++m) {
   int b=(y-m*x+9)%3;
   int u=point(x,y),v=line(m,b);
   adj[u] |= 1<<v; adj[v] |= 1<<u;
  }
 auto dominated=[&](int s){
  for (int u=0;u<N;++u)
   if (!(s&(1<<u)) && !(adj[u]&s)) return false;
  return true;
 };
 vector<unsigned char> ok(TOTAL,0);
 map<int,int> freq;
 for (int s=0;s<TOTAL;++s) {
  if (!dominated(s)) continue;
  bool good=true;
  for (int u=0;u<N && good;++u) if (!(s&(1<<u))) {
   good=false;
   for (int v=0;v<N;++v) if ((adj[u]&(1<<v)) && (s&(1<<v))) {
     if (dominated((s&~(1<<v)) | (1<<u))) {good=true; break;}
   }
  }
  if (good) {ok[s]=1; ++freq[__builtin_popcount((unsigned)s)];}
 }
 assert((freq==map<int,int>{{8,1755},{9,13088},{10,24624},{11,24948},{12,16899},{13,8316},{14,3042},{15,816},{16,153},{17,18},{18,1}}));
 map<int,int> minimal;
 vector<int> opt;
 for (int s=0;s<TOTAL;++s) if (ok[s]) {
   bool inclusion_minimal=true;
   for (int v=0;v<N;++v) if ((s&(1<<v)) && ok[s&~(1<<v)]) {inclusion_minimal=false;break;}
   if (inclusion_minimal) ++minimal[__builtin_popcount((unsigned)s)];
   if (__builtin_popcount((unsigned)s)==8) opt.push_back(s);
 }
 assert((minimal==map<int,int>{{8,1755},{9,3224}}));
 vector<int> index(TOTAL,-1);
 for (int i=0;i<(int)opt.size();++i) index[opt[i]]=i;
 for (int slide=0;slide<=1;++slide) {
  vector<vector<int>> g(opt.size());
  for (int i=0;i<(int)opt.size();++i) {
   int s=opt[i];
   for (int u=0;u<N;++u) if (s&(1<<u))
    for (int v=0;v<N;++v) if (!(s&(1<<v)) && (!slide || (adj[u]&(1<<v)))) {
      int j=index[s^(1<<u)^(1<<v)];
      if (j>=0) g[i].push_back(j);
    }
  }
  long long edge_sum=0;
  for(auto &ns:g) edge_sum+=ns.size();
  assert(edge_sum/2==(slide?4320:12798));
  map<int,int> ecc;
  for (int start=0;start<(int)g.size();++start) {
    vector<int> d(g.size(),-1);
    queue<int> q;
    q.push(start);d[start]=0;
    while(!q.empty()) {
      int v=q.front();q.pop();
      for(int w:g[v]) if(d[w]<0) {d[w]=d[v]+1;q.push(w);}
    }
    int mx=*max_element(d.begin(),d.end());
    assert(*min_element(d.begin(),d.end())>=0);
    ++ecc[mx];
  }
  assert(slide ? (ecc==map<int,int>{{9,1539},{10,216}}) : (ecc==map<int,int>{{8,1755}}));
 }
 cout << "INDEPENDENT_DIRECT_SWAP_OK\n";
}
