#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <vector>
using namespace std;
struct Edge {int a,b;};
struct Model {
 int n, twist, N;
 vector<Edge> edges;
 vector<vector<pair<int,int>>> adj;
 vector<uint64_t> faces,matchings;
 map<uint64_t,int> id;
 vector<vector<int>> g;
 void put(int a,int b) {if(a>b)swap(a,b);edges.push_back({a,b});}
 int edge_id(int a,int b) const {
  if(a>b)swap(a,b);
  for (int i=0;i<(int)edges.size();i++)if(edges[i].a==a&&edges[i].b==b)return i;
  return -1;
 }
 Model(int nn,int tt):n(nn),twist(tt),N(2*nn){
  for(int i=0;i<n;i++)put(i,i+n);
  for(int i=0;i<n-1;i++)for(int layer=0;layer<2;layer++)put(i+n*layer,i+1+n*layer);
  if(twist){put(n-1,n);put(0,2*n-1);}
  else {put(n-1,0);put(2*n-1,n);}
  assert((int)edges.size()==3*n && 3*n<63);
  adj.resize(N);
  for(int i=0;i<(int)edges.size();i++){
   auto e=edges[i];adj[e.a].push_back({e.b,i});adj[e.b].push_back({e.a,i});
  }
  for(auto a:adj)assert(a.size()==3);
  for(int i=0;i<n;i++){
   int j=(i+1)%n;
   int a=i,b=j,c=j+n,d=i+n;
   if(i==n-1 && twist){a=n-1;b=n;c=0;d=2*n-1;}
   uint64_t f=0;
   for(auto [x,y]: vector<pair<int,int>>{{a,b},{b,c},{c,d},{d,a}}){
    int k=edge_id(x,y);assert(k>=0);f|=(uint64_t(1)<<k);
   }
   assert(__builtin_popcountll(f)==4);faces.push_back(f);
  }
  rec((uint64_t(1)<<N)-1,0);
  for(int i=0;i<(int)matchings.size();i++)id[matchings[i]]=i;
  assert(id.size()==matchings.size());g.resize(id.size());
  for(int i=0;i<(int)matchings.size();i++){
   auto m=matchings[i];
   for(auto f:faces){
    if(__builtin_popcountll(m&f)==2){
     auto m2=m^f;auto it=id.find(m2);
     if(it!=id.end())g[i].push_back(it->second);
    }
   }
   sort(g[i].begin(),g[i].end());g[i].erase(unique(g[i].begin(),g[i].end()),g[i].end());
  }
  for(int i=0;i<(int)g.size();i++)for(int j:g[i])assert(find(g[j].begin(),g[j].end(),i)!=g[j].end());
 }
 void rec(uint64_t rem,uint64_t m){
  if(!rem){matchings.push_back(m);return;}
  int u=__builtin_ctzll(rem);
  for(auto [v,e]:adj[u]){
   if(!(rem&(uint64_t(1)<<v)))continue;
   rec(rem^(uint64_t(1)<<u)^(uint64_t(1)<<v),m|(uint64_t(1)<<e));
  }
 }
 pair<vector<int>,pair<int,int>> summary()const {
  vector<int> cs,seen(g.size());int radius=1000000,diam=0;
  for(int i=0;i<(int)g.size();i++)if(!seen[i]){
   vector<int> component,stack={i};seen[i]=1;
   while(!stack.empty()){
    int a=stack.back();stack.pop_back();component.push_back(a);
    for(int b:g[a])if(!seen[b])seen[b]=1,stack.push_back(b);
   }
   cs.push_back(component.size());
   if(component.size()>1)for(int start:component){
    vector<int>d(g.size(),-1);queue<int>q;q.push(start);d[start]=0;
    while(!q.empty()){
     int a=q.front();q.pop();
     for(int b:g[a])if(d[b]<0){d[b]=d[a]+1;q.push(b);}
    }
    int ecc=0;for(int b:component) {assert(d[b]>=0);ecc=max(ecc,d[b]);}
    radius=min(radius,ecc);diam=max(diam,ecc);
   }
  }
  sort(cs.rbegin(),cs.rend());return {cs,{radius,diam}};
 }
};
int fib(int k){int a=0,b=1;for(int i=0;i<k;i++){int c=a+b;a=b;b=c;}return a;}
int main(){
 for(int t=0;t<=1;t++)for(int n=5;n<=13;n++){
  Model m(n,t);auto [cs,metrics]=m.summary();int lucas=fib(n-1)+fib(n+1);
  vector<int> expect={lucas};if(n%2==t){expect.push_back(1);expect.push_back(1);}
  assert(cs==expect);
  int e=0;for(auto& ns:m.g)e+=ns.size();e/=2;
  assert(e==n*fib(n-1));
  assert(metrics.first==n/2 && metrics.second==2*(n/2));
  cout<<"PASS "<<(t?"mobius":"prism")<<" n="<<n<<" states="<<m.g.size()<<" components="<<cs.size()<<" edges="<<e<<" radius="<<metrics.first<<" diameter="<<metrics.second<<"\n";
 }
 cout<<"DIRECT_ENUMERATION_PASS\n";
}
