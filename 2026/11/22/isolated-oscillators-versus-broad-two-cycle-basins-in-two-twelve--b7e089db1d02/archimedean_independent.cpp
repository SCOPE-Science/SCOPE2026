// Reproducible exhaustive integer certificate for synchronous binary majority.
// C++17, standard library only. Independent indegree-peeling classification.
#include <algorithm>
#include <array>
#include <iostream>
#include <map>
#include <queue>
#include <stdexcept>
#include <utility>
#include <vector>
using namespace std;
using Graph=array<vector<int>,12>;
Graph triangle_truncation(){
 vector<pair<int,int>> V;
 for(int a=0;a<4;a++)for(int b=0;b<4;b++)if(a!=b)V.push_back({a,b});
 Graph G;
 for(int i=0;i<12;i++)for(int j=0;j<12;j++)if(i!=j){
  auto [a,b]=V[i]; auto [c,d]=V[j];
  if((c==a && d!=b)||(c==b && d==a)) G[i].push_back(j);
 }
 return G;
}
Graph cube_line_graph(){
 vector<pair<int,int>> E;
 for(int u=0;u<8;u++)for(int v=u+1;v<8;v++)
  if(__builtin_popcount((unsigned)(u^v))==1)E.push_back({u,v});
 Graph G;
 for(int i=0;i<12;i++)for(int j=0;j<12;j++)if(i!=j){
  auto [u,v]=E[i];auto [a,b]=E[j];
  if(u==a||u==b||v==a||v==b) G[i].push_back(j);
 }
 return G;
}
struct Data {int fixes=0,orbit2=0,basin1=0,basin2=0,consensus=0;map<int,int> first_entry, first_fixed,first_cycle;};
Data investigate(const Graph& G){
 constexpr int M=4096;
 array<int,M> to{},degree{},dist{},period{},rep{};
 for(int i=0;i<12;i++){
  for(auto j:G[i]) if(i==j||find(G[j].begin(),G[j].end(),i)==G[j].end())throw runtime_error("graph invalid");
 }
 for(int x=0;x<M;x++){
  for(int i=0;i<12;i++){
   int ones=0;
   for(int j:G[i]) ones += (x>>j)&1;
   if(2*ones>(int)G[i].size()||(2*ones==(int)G[i].size() && ((x>>i)&1)))to[x]|=(1<<i);
  }
  ++degree[to[x]];
 }
 queue<int> q;vector<int> removed;removed.reserve(M);
 for(int x=0;x<M;x++)if(degree[x]==0)q.push(x);
 while(!q.empty()){
  int x=q.front();q.pop();removed.push_back(x);
  if(--degree[to[x]]==0)q.push(to[x]);
 }
 vector<bool> seen(M,false);
 Data d;
 for(int x=0;x<M;x++)if(degree[x]>0 && !seen[x]){
  vector<int> cycle;int y=x;
  do { if(seen[y])throw runtime_error("bad cycle");cycle.push_back(y);seen[y]=true;y=to[y]; }while(y!=x);
  int anchor=*min_element(cycle.begin(),cycle.end());
  for(int s:cycle){period[s]=(int)cycle.size();dist[s]=0;rep[s]=anchor;}
  if(cycle.size()==1)d.fixes++; else if(cycle.size()==2)d.orbit2++; else throw runtime_error("unexpected period");
 }
 for(auto it=removed.rbegin();it!=removed.rend();++it){
  int x=*it;dist[x]=dist[to[x]]+1;period[x]=period[to[x]];rep[x]=rep[to[x]];
 }
 for(int x=0;x<M;x++){
  d.first_entry[dist[x]]++;
  if(period[x]==1){d.basin1++;d.first_fixed[dist[x]]++;}
  else if(period[x]==2){d.basin2++;d.first_cycle[dist[x]]++;}
  else throw runtime_error("undefined period");
  if(rep[x]==0||rep[x]==M-1)d.consensus++;
 }
 return d;
}
void print(const char* label, const Data& d){
 auto mprint=[](const map<int,int>& m){for(auto [a,b]:m)cout<<" "<<a<<":"<<b;};
 cout<<label<<" fixed="<<d.fixes<<" two_orbits="<<d.orbit2<<" fixed_basin="<<d.basin1<<" two_basin="<<d.basin2<<" consensus_basin="<<d.consensus<<"\n";
 cout<<"entry";mprint(d.first_entry);cout<<"\n";
 cout<<"fixed_by_entry";mprint(d.first_fixed);cout<<"\n";
 cout<<"two_by_entry";mprint(d.first_cycle);cout<<"\n";
}
int main(){
 try {
  Data t=investigate(triangle_truncation());Data c=investigate(cube_line_graph());
  print("truncated_tetrahedron",t);print("cuboctahedron",c);
  if(t.fixes!=16 || t.orbit2!=239 || t.basin2!=2366 || t.consensus!=1360 || t.first_entry.rbegin()->first!=5) return 1;
  if(c.fixes!=146 || c.orbit2!=20 || c.basin2!=40 || c.consensus!=2064 || c.first_entry.rbegin()->first!=4) return 2;
  if(c.first_cycle.size()!=1 || c.first_cycle.at(0)!=40) return 3;
  cout<<"INDEPENDENT_CERTIFICATE_OK\n";
  return 0;
 }catch(const exception& e){cerr<<e.what()<<"\n";return 4;}
}
