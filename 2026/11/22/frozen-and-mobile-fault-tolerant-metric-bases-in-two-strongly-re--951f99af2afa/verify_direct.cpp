// Independent exhaustive verifier for fault-tolerant distance landmarks.
// Build: c++ -std=c++17 -O2 -Wall -Wextra verify_direct.cpp -o verify_direct
// Run:   ./verify_direct
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
using M=uint32_t;
constexpr int N=16;
using A=array<array<int,N>,N>;
int row(int u){return u/4;}
int col(int u){return u%4;}
A make_dist(bool rook){
 A d{};
 for(int u=0;u<N;u++)for(int v=0;v<N;v++){
  int x=(row(u)-row(v)+4)%4, y=(col(u)-col(v)+4)%4;
  bool adjacent = rook ? (u!=v && (row(u)==row(v) || col(u)==col(v)))
          : (x==1&&y==0)||(x==3&&y==0)||(x==0&&y==1)||
            (x==0&&y==3)||(x==1&&y==1)||(x==3&&y==3);
  d[u][v]=(u==v)?0:adjacent?1:2;
 }
 // Check every pair has precisely two common neighbors, and valency six.
 for(int u=0;u<N;u++){
  int deg=0;for(int w=0;w<N;w++)if(d[u][w]==1)deg++;
  assert(deg==6);
  for(int v=u+1;v<N;v++){
   int common=0;
   for(int w=0;w<N;w++)if(d[u][w]==1 && d[v][w]==1)common++;
   assert(common==2);
  }
 }
 return d;
}
bool resolving(const A& d, M set){
 for(int u=0;u<N;u++)for(int v=u+1;v<N;v++){
  bool distinct=false;
  for(int w=0;w<N;w++)if((set>>w&1U) && d[w][u]!=d[w][v]){
   distinct=true;break;
  }
  if(!distinct)return false;
 }
 return true;
}
bool tolerant(const A& d, M set){
 for(int w=0;w<N;w++)if(set>>w&1U){
  if(!resolving(d,set^(1U<<w)))return false;
 }
 return true;
}
vector<M> enumerate(const A& d){
 vector<M> bases;
 long long lower=0;
 for(M set=0;set<(1U<<N);set++){
  int sz=__builtin_popcount(set);
  if(sz==5){if(tolerant(d,set))lower++;}
  if(sz==6 && tolerant(d,set))bases.push_back(set);
 }
 assert(lower==0 && !bases.empty());
 return bases;
}
struct Stats{long long edges=0;map<int,int> degree,eccentricity;map<int,long long> distance;int components=0,rad=1000000,diam=0;};
Stats analyze(const vector<M>& bases,int exchanged){
 map<M,int> ids;for(int i=0;i<(int)bases.size();i++)ids[bases[i]]=i;
 vector<vector<int>> adj(bases.size());
 for(int i=0;i<(int)bases.size();i++)for(int j=i+1;j<(int)bases.size();j++){
  if(__builtin_popcount(bases[i]^bases[j])==2*exchanged){
   adj[i].push_back(j);adj[j].push_back(i);
  }
 }
 Stats s;
 for(auto& v:adj){s.edges+=v.size();s.degree[v.size()]++;}s.edges/=2;
 vector<int> global(bases.size(),-1);
 for(int i=0;i<(int)bases.size();i++)if(global[i]<0){
  queue<int> q;global[i]=s.components;q.push(i);
  while(!q.empty()){
   int u=q.front();q.pop();
   for(int v:adj[u])if(global[v]<0){global[v]=s.components;q.push(v);}
  }
  s.components++;
 }
 if(s.components==1)for(int i=0;i<(int)bases.size();i++){
  vector<int> dist(bases.size(),-1);queue<int> q;dist[i]=0;q.push(i);
  while(!q.empty()){
   int u=q.front();q.pop();
   for(int v:adj[u])if(dist[v]<0){dist[v]=dist[u]+1;q.push(v);}
  }
  int ecc=0;
  for(int j=0;j<(int)bases.size();j++){
   assert(dist[j]>=0);ecc=max(ecc,dist[j]);
   if(j>i)s.distance[dist[j]]++;
  }
  s.eccentricity[ecc]++;s.rad=min(s.rad,ecc);s.diam=max(s.diam,ecc);
 }
 return s;
}
void print(const string& name,const vector<M>& bases,int move){
 auto s=analyze(bases,move);
 cout<<name<<" bases="<<bases.size()<<" move="<<move<<" edges="<<s.edges
     <<" components="<<s.components<<" radius="<<(s.components==1?s.rad:-1)
     <<" diameter="<<s.diam<<"\n";
 cout<<" degrees:";for(auto [k,v]:s.degree)cout<<" "<<k<<":"<<v;cout<<"\n";
 cout<<" eccentricities:";for(auto [k,v]:s.eccentricity)cout<<" "<<k<<":"<<v;cout<<"\n";
 cout<<" unordered pair distances:";for(auto [k,v]:s.distance)cout<<" "<<k<<":"<<v;cout<<"\n";
 if(name=="Shrikhande" && move==1)assert(bases.size()==448 && s.components==448 && s.edges==0);
 if(name=="Shrikhande" && move==2)assert(s.components==1 && s.edges==10080 && s.diam==3 && s.rad==3);
 if(name=="Rook" && move==1)assert(bases.size()==1600 && s.components==1 && s.edges==12816 && s.rad==6 && s.diam==6);
}
int main(){
 auto sh=enumerate(make_dist(false)),rk=enumerate(make_dist(true));
 print("Shrikhande",sh,1);print("Shrikhande",sh,2);print("Rook",rk,1);
 cout<<"ALL ASSERTIONS PASSED\n";
}
