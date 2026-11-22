// Exact exhaustive state-space census for deterministic three-opinion plurality.
// Standard C++17; no external dependencies.
#include <array>
#include <algorithm>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <string>
#include <vector>
using namespace std;
struct Census {
 int k,N,S; array<array<int,3>,10> adj{};
 vector<int> next,period,depth,orbit;
 vector<vector<int>> cycles;
 int p3[10];
 explicit Census(int step):k(step),N(10),S(59049),next(S),period(S),depth(S),orbit(S,-1){
  vector<vector<int>> list(10);
  auto edge=[&](int a,int b){list[a].push_back(b);list[b].push_back(a);};
  for(int i=0;i<5;i++){edge(i,(i+1)%5);edge(i,5+i);edge(5+i,5+(i+k)%5);}
  for(int i=0;i<10;i++){sort(list[i].begin(),list[i].end());if(list[i].size()!=3)abort();copy(list[i].begin(),list[i].end(),adj[i].begin());}
  p3[0]=1;for(int i=1;i<N;i++)p3[i]=3*p3[i-1];
 }
 int update(int state){
  int x[10],z=0;
  for(int i=0;i<10;i++)x[i]=(state/p3[i])%3;
  for(int v=0;v<10;v++){
   int a=x[adj[v][0]],b=x[adj[v][1]],c=x[adj[v][2]];
   int y=(a==b||a==c)?a:(b==c?b:x[v]);
   z+=p3[v]*y;
  }
  return z;
 }
 void execute(){
  vector<int> in(S,0);
  for(int s=0;s<S;s++){next[s]=update(s);in[next[s]]++;}
  queue<int> q;for(int s=0;s<S;s++)if(!in[s])q.push(s);
  vector<int> order;order.reserve(S);
  while(!q.empty()){int x=q.front();q.pop();order.push_back(x);int y=next[x];if(--in[y]==0)q.push(y);}
  for(int s=0;s<S;s++)if(in[s]>0&&orbit[s]<0){
    int i=cycles.size();vector<int> c;int t=s;
    do{orbit[t]=i;c.push_back(t);t=next[t];}while(t!=s);
    int p=c.size();for(int x:c){period[x]=p;depth[x]=0;}
    cycles.push_back(c);
  }
  reverse(order.begin(),order.end());
  for(int x:order){int y=next[x];orbit[x]=orbit[y];period[x]=period[y];depth[x]=depth[y]+1;}
  map<int,int> orbit_counts,basin_period,entrant_fixed,by_alphabet;
  map<pair<int,int>,int> entry;
  map<int,int> basin_size,basin_hist_fixed,basin_hist_2;
  for(auto &c:cycles)orbit_counts[c.size()]++;
  for(int s=0;s<S;s++){
   basin_period[period[s]]++;entry[{depth[s],period[s]}]++;
   basin_size[orbit[s]]++;
   if(period[s]==1)entrant_fixed[depth[s]]++;
  }
  for(auto [id,size]:basin_size){if(cycles[id].size()==1)basin_hist_fixed[size]++;else basin_hist_2[size]++;}
  int consensus_orbits=0,consensus_basin=0;
  for(int id=0;id<(int)cycles.size();id++){
   if(cycles[id].size()!=1)continue;
   int s=cycles[id][0];int a=s%3, j=0;
   for(;j<N;j++)if(s/p3[j]%3!=a)break;
   if(j==N){consensus_orbits++;consensus_basin+=basin_size[id];}
  }
  map<int,int> alph_fixed;
  for(auto &cyc:cycles){if(cyc.size()!=1)continue;int s=cyc[0];bool seen[3]={};for(int j=0;j<N;j++)seen[(s/p3[j])%3]=true;alph_fixed[int(seen[0])+int(seen[1])+int(seen[2])]++;}
  int maxDepth=*max_element(depth.begin(),depth.end());
  int witness=int(find(depth.begin(),depth.end(),maxDepth)-depth.begin());
  cout<<"graph GP(5,"<<k<<") states="<<S<<" fixed="<<orbit_counts[1]<<" primitive_two_cycles="<<orbit_counts[2]<<" max_entry="<<maxDepth<<" basin_fixed="<<basin_period[1]<<" basin_two="<<basin_period[2]<<" consensus_basin="<<consensus_basin<<"\n";
  cout<<"sharp_witness="<<witness<<" path:";int u=witness;for(int i=0;i<=maxDepth+1;i++){cout<<" "<<u;u=next[u];}cout<<"\n";
  cout<<"fixed_by_palette_support:";for(auto [a,v]:alph_fixed)cout<<" "<<a<<":"<<v;cout<<"\n";
  cout<<"entry_counts:";for(auto [key,v]:entry)cout<<" ("<<key.first<<","<<key.second<<")="<<v;cout<<"\n";
  cout<<"fixed_basin_hist:";for(auto [size,v]:basin_hist_fixed)cout<<" "<<size<<":"<<v;cout<<"\n";
  cout<<"two_basin_hist:";for(auto [size,v]:basin_hist_2)cout<<" "<<size<<":"<<v;cout<<"\n";
  if(accumulate(basin_period.begin(),basin_period.end(),0,[](int a,const auto &b){return a+b.second;})!=S)abort();
  if(orbit_counts.size()!=2)abort();
 }
};
int main(){Census(1).execute();Census(2).execute();}
