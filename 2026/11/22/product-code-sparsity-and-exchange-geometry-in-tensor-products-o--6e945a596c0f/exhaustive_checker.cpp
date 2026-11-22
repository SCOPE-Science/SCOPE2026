// Reproducible exhaustive verification of total-perfect-code assertions.
// Compile: g++ -O2 -std=c++17 exhaustive_checker.cpp -o exhaustive_checker
// Run: ./exhaustive_checker
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <tuple>
#include <vector>
using namespace std;
struct Vertex {int x,y,s,t;};
void test(int a,int b,int c,int d) {
 vector<Vertex> vs;
 for(int s=0;s<2;s++) for(int x=0;x<(s?b:a);x++)
 for(int t=0;t<2;t++) for(int y=0;y<(t?d:c);y++)vs.push_back({x,y,s,t});
 int n=vs.size(); assert(n<=20);
 vector<uint64_t> adj(n,0);
 for(int i=0;i<n;i++)for(int j=0;j<n;j++)if(i!=j)
  if(vs[i].s!=vs[j].s && vs[i].t!=vs[j].t) adj[i]|=(uint64_t(1)<<j);
 vector<uint64_t> codes;
 for(uint64_t mask=0;mask<(uint64_t(1)<<n);mask++) {
  bool ok=true;
  for(auto neighbors:adj)if(__builtin_popcountll(mask&neighbors)!=1){ok=false;break;}
  if(ok)codes.push_back(mask);
 }
 const int B=a*b*c*d;
 assert((int)codes.size()==B*B);
 map<uint64_t,int> idx; for(int i=0;i<(int)codes.size();i++){
  idx[codes[i]]=i; assert(__builtin_popcountll(codes[i])==4);
 }
 // Every single replacement must preserve cardinality and the code property.
 vector<vector<int>> ng(codes.size());
 for(int i=0;i<(int)codes.size();i++) {
  auto S=codes[i];
  for(int u=0;u<n;u++)if((S>>u)&1)
   for(int v=0;v<n;v++)if(!((S>>v)&1)){
    uint64_t T=S^(uint64_t(1)<<u)^(uint64_t(1)<<v);
    auto it=idx.find(T);if(it!=idx.end())ng[i].push_back(it->second);
   }
  sort(ng[i].begin(),ng[i].end());
  ng[i].erase(unique(ng[i].begin(),ng[i].end()),ng[i].end());
  assert((int)ng[i].size()==(a+b)*(c+d)-4);
 }
 // Distances in the full one-vertex-replacement graph.
 int diameter=0;
 for(int j=0;j<(int)codes.size();j++) {
  vector<int> ds(codes.size(),-1);queue<int> q;q.push(j);ds[j]=0;
  while(!q.empty()) {int u=q.front();q.pop();for(int v:ng[u])if(ds[v]<0){ds[v]=ds[u]+1;q.push(v);}}
  for(int i=0;i<(int)codes.size();i++) {assert(ds[i]>=0);diameter=max(diameter,ds[i]);
   assert(ds[i] == 4-__builtin_popcountll(codes[i]&codes[j]));}
 }
 assert(diameter==4);
 // Direct construction of factorwise products, and distance distribution.
 vector<uint64_t> products;
 for(int x=0;x<a;x++)for(int z=0;z<b;z++)
 for(int y=0;y<c;y++)for(int w=0;w<d;w++){
  uint64_t S=0;
  for(int i=0;i<n;i++){
   const auto &v=vs[i];
   if(v.x==(v.s?z:x) && v.y==(v.t?w:y)) S|=uint64_t(1)<<i;
  }
  assert(__builtin_popcountll(S)==4);assert(idx.count(S)); products.push_back(S);
 }
 assert((int)products.size()==B);
 set<uint64_t> distinct(products.begin(),products.end());assert((int)distinct.size()==B);
 map<int,int> hist;
 for(auto T:products)hist[4-__builtin_popcountll(T&products[0])]++;
 assert(hist[0]==1);
 assert(hist[2]==(a+b-2)+(c+d-2));
 assert(hist[3]==(a+b-2)*(c+d-2));
 assert(hist[4]== B-(a+b-1)*(c+d-1));
 assert((int)hist.size()==4);
 int radius=0; map<int,int> coverage;
 for(auto S:codes){int best=4;for(auto P:products)
  best=min(best,4-__builtin_popcountll(S&P));
  coverage[best]++;radius=max(radius,best);
 }
 assert(radius==2);
 cout<<"K_("<<a<<","<<b<<") tensor K_("<<c<<","<<d<<")"
 <<" vertices="<<n<<" codes="<<codes.size()<<" product="<<products.size()
 <<" degree="<<ng.front().size()<<" diameter="<<diameter<<" cover_radius="<<radius<<" product_dist=";
 for(auto p:hist)cout<<p.first<<":"<<p.second<<" ";cout<<"PASS\n";
}
int main(){test(2,2,2,2);test(2,3,2,2);}
