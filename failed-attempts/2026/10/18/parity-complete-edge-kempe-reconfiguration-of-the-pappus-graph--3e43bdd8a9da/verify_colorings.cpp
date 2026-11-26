// Exact independent direct edge-coloring enumeration of the Pappus incidence graph.
// C++17, no external packages or precomputed coloring table.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <functional>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <vector>
using namespace std;
using U=uint32_t;
using Fac=array<U,3>;
vector<pair<int,int>> E;
array<vector<int>,18> I;
array<int,27> coloring;
array<int,18> used_color;
set<Fac> factors;
int complete_named_colorings=0;

void backtrack(int left) {
 if(left==0){
  ++complete_named_colorings;
  Fac f={0,0,0};
  for(int j=0;j<27;++j){assert(coloring[j]>=0); f[coloring[j]] |= (U(1)<<j);}
  sort(f.begin(),f.end());factors.insert(f);return;
 }
 int best=-1,opts=10;
 for(int e=0;e<27;++e) if(coloring[e]<0){
  auto [u,v]=E[e];int mask=7&~(used_color[u]|used_color[v]);
  int k=__builtin_popcount((unsigned)mask);
  if(k<opts){best=e;opts=k;}
 }
 if(opts==0)return;
 auto [u,v]=E[best];
 int avail=7&~(used_color[u]|used_color[v]);
 for(int c=0;c<3;++c)if(avail&(1<<c)){
  coloring[best]=c;used_color[u] |= 1<<c;used_color[v] |= 1<<c;
  backtrack(left-1);
  used_color[u]^=1<<c;used_color[v]^=1<<c;coloring[best]=-1;
 }
}

vector<U> all_cycles(U x){
 array<vector<int>,18> adj;
 for(int e=0;e<27;++e) if(x&(U(1)<<e)){
  auto [u,v]=E[e];adj[u].push_back(v);adj[v].push_back(u);
 }
 for(int v=0;v<18;++v)assert(adj[v].size()==2);
 array<bool,18> vis={};vector<U> result;
 for(int i=0;i<18;++i)if(!vis[i]){
  queue<int> q;q.push(i);vis[i]=true;array<bool,18> inside={};
  while(!q.empty()){
   int u=q.front();q.pop();inside[u]=true;
   for(int v:adj[u])if(!vis[v]){vis[v]=true;q.push(v);}
  }
  U cycle=0;
  for(int e=0;e<27;++e){auto[u,v]=E[e];if(inside[u]&&inside[v]&&(x&(U(1)<<e))) cycle|=U(1)<<e;}
  assert(__builtin_popcount(cycle)==count(inside.begin(),inside.end(),true));
  result.push_back(cycle);
 }
 return result;
}
int sign_match(U x){
 array<int,9> perm={};
 for(int p=0;p<9;++p){int seen=0;
  for(int e:I[p])if(x&(U(1)<<e)){perm[p]=E[e].second-9;seen++;}
  assert(seen==1);
 }
 int sign=1;
 for(int i=0;i<9;++i)for(int j=i+1;j<9;++j)if(perm[i]>perm[j])sign=-sign;
 return sign;
}
int sign_factor(const Fac& f){return sign_match(f[0])*sign_match(f[1])*sign_match(f[2]);}

int main(){
 for(int x=0;x<3;++x)for(int y=0;y<3;++y)for(int m=0;m<3;++m){
  int p=3*x+y, line=9+3*m+((y-m*x+6)%3);
  E.push_back({p,line});
 }
 sort(E.begin(),E.end());assert(E.size()==27);
 for(int i=0;i<27;++i){auto[u,v]=E[i];I[u].push_back(i);I[v].push_back(i);}
 for(int v=0;v<18;++v)assert(I[v].size()==3);
 coloring.fill(-1);used_color.fill(0);
 backtrack(27);
 assert(factors.size()==20);assert(complete_named_colorings==120);
 vector<Fac> F(factors.begin(),factors.end());
 map<Fac,int> idx;for(int i=0;i<(int)F.size();++i)idx[F[i]]=i;
 vector<set<int>> neigh(F.size());
 int hubs=0,leaves=0;
 vector<int> signs;map<int,int> sign_counts;
 for(int i=0;i<(int)F.size();++i){
  auto f=F[i];int sig=sign_factor(f);signs.push_back(sig);sign_counts[sig]++;
  vector<vector<int>> profile;
  for(int a=0;a<3;++a)for(int b=a+1;b<3;++b){
   int c=3-a-b;
   auto cycles=all_cycles(f[a]|f[b]);vector<int> lens;
   for(U cycle:cycles){
    lens.push_back(__builtin_popcount(cycle)); // length in edges = vertices.
    Fac g={f[a]^cycle,f[b]^cycle,f[c]};sort(g.begin(),g.end());
    auto it=idx.find(g);assert(it!=idx.end());
    if(it->second!=i){neigh[i].insert(it->second);assert(sign_factor(g)==sig);}
   }
   sort(lens.begin(),lens.end());profile.push_back(lens);
  }
  sort(profile.begin(),profile.end());
  if(profile==vector<vector<int>>{{6,6,6},{6,6,6},{6,6,6}})hubs++;
  else if(profile==vector<vector<int>>{{6,6,6},{18},{18}})leaves++;
  else {cerr<<"unexpected bichromatic cycle profile\n";return 2;}
 }
 assert(hubs==2&&leaves==18);
 assert(sign_counts[-1]==10 && sign_counts[1]==10);
 set<pair<int,int>> edges;
 for(int i=0;i<(int)F.size();++i)for(int j:neigh[i]){assert(neigh[j].count(i));if(i<j)edges.insert({i,j});}
 assert(edges.size()==36);
 vector<int> visited(F.size(),0);
 int ccount=0;
 for(int start=0;start<(int)F.size();++start)if(!visited[start]){
  vector<int> component;queue<int> q;q.push(start);visited[start]=1;
  while(!q.empty()){
   int v=q.front();q.pop();component.push_back(v);
   for(int w:neigh[v])if(!visited[w]){visited[w]=1;q.push(w);}
  }
  assert(component.size()==10);ccount++;
  int hub=-1;
  set<int> comp(component.begin(),component.end());
  for(int v:component){assert(signs[v]==signs[start]);if(neigh[v].size()==9){assert(hub==-1);hub=v;}else assert(neigh[v].size()==3);}
  assert(hub>=0);
  set<int> peripheral=comp;peripheral.erase(hub);
  assert(neigh[hub]==peripheral);
  set<int> done;
  int triangles=0;
  for(int v:peripheral)if(!done.count(v)){
   set<int> triangle={v};triangle.insert(neigh[v].begin(),neigh[v].end());triangle.erase(hub);
   assert(triangle.size()==3);
   for(int w:triangle){set<int> local=neigh[w];local.erase(hub);assert(local.size()==2);for(int z:local)assert(triangle.count(z));}
   done.insert(triangle.begin(),triangle.end());triangles++;
  }
  assert(triangles==3 && done==peripheral);
 }
 assert(ccount==2);
 cout<<"VERIFY_DIRECT_OK vertices=18 edges=27 proper_named_3_edge_colorings="<<complete_named_colorings<<" unlabeled_factorizations="<<F.size()<<"\n";
 cout<<"VERIFY_DIRECT_OK bichromatic_hubs="<<hubs<<" leaves="<<leaves<<" Kempe_switch_edges="<<edges.size()<<"\n";
 cout<<"VERIFY_DIRECT_OK components=2x10 both_K1_join_3K3=true sign_classes=10+10\n";
}
