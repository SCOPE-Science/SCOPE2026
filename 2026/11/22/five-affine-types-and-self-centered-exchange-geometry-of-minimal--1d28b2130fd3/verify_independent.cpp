// Independent exact checker using modular exponentiation and union-find connectivity.
// Build: c++ -std=c++17 -O2 check_independent.cpp -o check_independent
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <vector>
using namespace std;
constexpr int N=13, FULL=(1<<N)-1;
int modpow(int a,int e){int x=1;while(e){if(e&1)x=x*a%N;a=a*a%N;e>>=1;}return x;}
array<array<bool,N>,N> edges(){
 array<array<bool,N>,N> E{};
 for(int i=0;i<N;i++)for(int j=0;j<N;j++)if(i!=j)
   E[i][j]=modpow((i-j+N)%N,(N-1)/2)==1;
 for(int i=0;i<N;i++){
  int deg=0;for(int j=0;j<N;j++){assert(E[i][j]==E[j][i]);deg+=E[i][j];}
  assert(deg==6);
 }
 return E;
}
struct DSU{
 array<int,N>p;
 DSU(){iota(p.begin(),p.end(),0);}
 int root(int u){while(p[u]!=u)u=p[u]=p[p[u]];return u;}
 void join(int u,int v){u=root(u);v=root(v);p[u]=v;}
};
using Graph=array<array<bool,N>,N>;
bool feasible(const Graph&E,int s){
 if(!s)return false;
 DSU d;bool marked[N]={};
 for(int i=0;i<N;i++)if(s>>i&1){
   marked[i]=true;
   for(int j=0;j<N;j++)if(E[i][j]){
     marked[j]=true;
     if(s>>j&1)d.join(i,j);
   }
 }
 for(bool b:marked)if(!b)return false;
 int first=__builtin_ctz((unsigned)s);
 for(int i=0;i<N;i++)if((s>>i&1)&&d.root(i)!=d.root(first))return false;
 return true;
}
int image(int s,int m,int b){int t=0;for(int i=0;i<N;i++)if(s>>i&1)t|=1<<((m*i+b)%N);return t;}
int main(){
 auto E=edges();
 array<bool,FULL+1> valid{};
 map<int,int>counts;
 for(int s=1;s<=FULL;s++)if(feasible(E,s)){
   valid[s]=true;counts[__builtin_popcount((unsigned)s)]++;
 }
 vector<int> minimal;
 for(int s=1;s<=FULL;s++)if(valid[s]){
  bool min=true;
  for(int i=0;i<N;i++)if((s>>i&1)&&valid[s^(1<<i)])min=false;
  if(min)minimal.push_back(s);
 }
 assert(minimal.size()==260);
 for(int s:minimal)assert(__builtin_popcount((unsigned)s)==4);
 map<int,int>index;
 for(int i=0;i<(int)minimal.size();i++)index[minimal[i]]=i;
 vector<vector<int>> neigh(minimal.size());int edge_count=0;
 for(int i=0;i<(int)minimal.size();i++)for(int j=i+1;j<(int)minimal.size();j++)
   if(__builtin_popcount((unsigned)(minimal[i]^minimal[j]))==2){
     neigh[i].push_back(j);neigh[j].push_back(i);edge_count++;
   }
 cout<<"connected_count_by_size";
 for(auto[k,v]:counts)cout<<" "<<k<<":"<<v;
 cout<<"\nminimal_count "<<minimal.size()<<" edges "<<edge_count<<"\n";
 int radius=100,diameter=0;
 map<array<int,5>,int>profiles;
 vector<array<int,5>>shells(minimal.size());
 for(int st=0;st<(int)minimal.size();st++){
   vector<int>dist(minimal.size(),-1);queue<int>q;q.push(st);dist[st]=0;
   while(!q.empty()){
     int u=q.front();q.pop();
     for(int v:neigh[u])if(dist[v]<0){dist[v]=dist[u]+1;q.push(v);}
   }
   assert(find(dist.begin(),dist.end(),-1)==dist.end());
   int ecc=*max_element(dist.begin(),dist.end());
   assert(ecc==4);
   radius=min(radius,ecc);diameter=max(diameter,ecc);
   for(int z:dist)shells[st][z]++;
   profiles[shells[st]]++;
 }
 cout<<"radius "<<radius<<" diameter "<<diameter<<"\n";
 set<int>seen;
 for(int s:minimal)if(!seen.count(s)){
   set<int>orb;
   for(int mul=1;mul<N;mul++)if(modpow(mul,6)==1)
     for(int off=0;off<N;off++)orb.insert(image(s,mul,off));
   assert(all_of(orb.begin(),orb.end(),[&](int t){return index.count(t);}));
   for(int t:orb){assert(!seen.count(t));seen.insert(t);}
   int k=index[s];
   for(int t:orb)assert(shells[index[t]]==shells[k]);
   cout<<"orbit "<<hex<<s<<dec<<" size "<<orb.size()<<" degree "<<neigh[k].size()<<" shells";
   for(auto x:shells[k])cout<<" "<<x;
   cout<<"\n";
 }
 assert(seen.size()==minimal.size());assert(edge_count==1911&&radius==4&&diameter==4);
 assert(counts[4]==260&&counts[5]==975&&counts[6]==1625&&counts[7]==1703);
 cout<<"CHECKS_PASS\n";
}
