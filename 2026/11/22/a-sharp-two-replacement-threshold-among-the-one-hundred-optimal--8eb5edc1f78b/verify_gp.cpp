// Exact finite check for semitotal domination and exchanges on GP(10,3).
// Build: c++ -O2 -std=c++17 verify_gp.cpp -o verify_gp && ./verify_gp
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <queue>
#include <vector>
using namespace std;
int main(){
 constexpr int n=20, full=(1<<20)-1;
 array<int,n> adj{}, close{}, b2{};
 auto link=[&](int a,int b){adj[a]|=(1<<b);adj[b]|=(1<<a);};
 for(int i=0;i<10;i++){link(i,(i+1)%10);link(i,i+10);link(i+10,10+(i+3)%10);}
 for(int i=0;i<n;i++){
  assert(__builtin_popcount((unsigned)adj[i])==3);
  close[i]=adj[i]|(1<<i);b2[i]=close[i];
  for(int j=0;j<n;j++)if((adj[i]>>j)&1)b2[i]|=adj[j];
 }
 vector<int> solutions;
 int ordinary=0;
 for(int mask=0;mask<=full;mask++){
  int cardinality=__builtin_popcount((unsigned)mask);
  if(cardinality>6)continue;
  int cover=0;
  for(int i=0;i<n;i++)if((mask>>i)&1)cover|=close[i];
  if(cover!=full)continue;
  assert(cardinality==6); // no dominating smaller sets exist
  ordinary++;
  bool semi=true;
  for(int i=0;i<n;i++)if(((mask>>i)&1) && !(b2[i]&(mask^(1<<i))))semi=false;
  if(semi)solutions.push_back(mask);
 }
 assert(ordinary==130 && solutions.size()==100);
 vector<vector<int>> graph(solutions.size());
 int edges=0, one=0;
 for(size_t a=0;a<solutions.size();a++)for(size_t b=a+1;b<solutions.size();b++){
  int replace=__builtin_popcount((unsigned)(solutions[a]^solutions[b]))/2;
  assert(replace>=2);
  if(replace<=2){edges++;graph[a].push_back(b);graph[b].push_back(a);}
 }
 assert(edges==570 && one==0);
 map<int,int> degrees, profiles;
 for(size_t i=0;i<graph.size();i++){
  degrees[graph[i].size()]++;
  vector<int> dist(graph.size(),-1);queue<int>q;dist[i]=0;q.push(i);
  while(!q.empty()){
   int x=q.front();q.pop();
   for(int y:graph[x])if(dist[y]<0){dist[y]=dist[x]+1;q.push(y);}
  }
  assert(*min_element(dist.begin(),dist.end())==0);
  assert(*max_element(dist.begin(),dist.end())==4);
  assert(count(dist.begin(),dist.end(),-1)==0);
  array<int,5> shell{};
  for(int d:dist){assert(d>=0&&d<=4);shell[d]++;}
  const array<int,5> a={1,13,44,40,2}, b={1,8,46,44,1}, c={1,12,42,42,3};
  assert(shell==a||shell==b||shell==c);
  if(shell==a)profiles[13]++;else if(shell==b)profiles[8]++;else profiles[12]++;
 }
 assert((degrees==map<int,int>{{8,30},{12,10},{13,60}}));
 assert((profiles==map<int,int>{{8,30},{12,10},{13,60}}));
 cout << "GP(10,3): ordinary_6="<<ordinary<<" semitotal_6="<<solutions.size()
      <<" one_jump_edges="<<one<<" two_jump_edges="<<edges
      <<" diameter=4 degree_hist=8:30,12:10,13:60 VERIFY_OK\n";
}
