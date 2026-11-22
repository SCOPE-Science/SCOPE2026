// Self-contained independent exhaustive verifier of Frucht k-metric bases.
// Compile: c++ -O2 -std=c++17 verify_cpp.cpp -o verify_cpp && ./verify_cpp
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <queue>
#include <set>
#include <tuple>
#include <vector>
using namespace std;
constexpr int N=12, INF=10000;
using Entry=tuple<int,int,int>;
using Components=vector<Entry>;
int edges[N][N]={};
int distances[N][N];
int pop(int x){return __builtin_popcount((unsigned)x);}

pair<int, Components> explore(const vector<int>& states,bool sliding){
 vector<int> state_present(1<<N,0);
 for(int s:states) state_present[s]=1;
 vector<vector<int>> adj(1<<N);
 int E=0;
 for(int s:states){
  for(int u=0;u<N;u++) if(s&(1<<u))
   for(int v=0;v<N;v++) if(!(s&(1<<v))&&(!sliding||edges[u][v])){
    int t=s^(1<<u)^(1<<v);
    if(state_present[t]){adj[s].push_back(t); E++;}
   }
 }
 assert((E%2)==0); E/=2;
 vector<char> seen(1<<N,0);
 Components info;
 for(int source:states){
  if(seen[source])continue;
  vector<int> cc;
  queue<int> q; q.push(source);seen[source]=1;
  while(!q.empty()){
   int u=q.front();q.pop();cc.push_back(u);
   for(int v:adj[u]) if(!seen[v]){seen[v]=1;q.push(v);}
  }
  int low=INF,high=0;
  for(int root:cc){
   vector<int> d(1<<N,-1); d[root]=0;queue<int> que;que.push(root);
   while(!que.empty()){
    int u=que.front();que.pop();
    for(int v:adj[u])if(d[v]<0){d[v]=d[u]+1;que.push(v);}
   }
   int ecc=0; for(int u:cc){assert(d[u]>=0);ecc=max(ecc,d[u]);}
   low=min(low,ecc);high=max(high,ecc);
  }
  info.emplace_back((int)cc.size(),low,high);
 }
 sort(info.rbegin(),info.rend());
 return {E,info};
}
void print_components(const Components& c){
 cout << '[';
 for(int i=0;i<(int)c.size();i++){
  auto [s,r,d]=c[i];
  if(i)cout<<", ";
  cout<<'('<<s<<", "<<r<<", "<<d<<')';
 }
 cout<<']';
}
int main(){
 const int LCF[N]={-5,-2,-4,2,5,-2,2,5,-2,-5,4,2};
 for(int u=0;u<N;u++){
  int v=(u+1)%N;
  edges[u][v]=edges[v][u]=1;
  v=(u+LCF[u]+N)%N;
  edges[u][v]=edges[v][u]=1;
 }
 for(int u=0;u<N;u++){
  int deg=0;for(int v=0;v<N;v++){
   deg+=edges[u][v]; distances[u][v]=(u==v?0:(edges[u][v]?1:INF));
  }
  assert(deg==3);
 }
 for(int m=0;m<N;m++)for(int u=0;u<N;u++)for(int v=0;v<N;v++)
  distances[u][v]=min(distances[u][v],distances[u][m]+distances[m][v]);
 vector<int> cuts;
 for(int u=0;u<N;u++)for(int v=u+1;v<N;v++){
  int mask=0;
  for(int w=0;w<N;w++)if(distances[u][w]!=distances[v][w])mask|=1<<w;
  cuts.push_back(mask);
 }
 assert(cuts.size()==66);
 int mincut=12;for(int x:cuts)mincut=min(mincut,pop(x));assert(mincut==6);
 for(int k=1;k<=6;k++){
  int minimum=N+1;
  vector<int> bases;
  for(int mask=0;mask<(1<<N);mask++){
   if(pop(mask)>minimum)continue;
   bool valid=true;
   for(int cut:cuts)if(pop(mask&cut)<k){valid=false;break;}
   if(!valid)continue;
   int m=pop(mask);
   if(m<minimum){minimum=m;bases.clear();}
   bases.push_back(mask);
  }
  auto [je,jc]=explore(bases,false);
  auto [se,sc]=explore(bases,true);
  cout<<"k="<<k<<" min="<<minimum<<" bases="<<bases.size()<<" jump_edges="<<je<<" jump_components=";
  print_components(jc);
  cout<<" slide_edges="<<se<<" slide_components=";print_components(sc);cout<<'\n';
 }
}
