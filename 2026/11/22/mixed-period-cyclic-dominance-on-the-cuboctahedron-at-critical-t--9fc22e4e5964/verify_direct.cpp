#include <array>
#include <vector>
#include <map>
#include <algorithm>
#include <iostream>
#include <numeric>
#include <cstdint>
using namespace std;
static constexpr int N=531441, V=12;
static constexpr array<array<int,2>,12> E={{{0,1},{0,2},{0,4},{1,3},{1,5},{2,3},{2,6},{3,7},{4,5},{4,6},{5,7},{6,7}}};
array<array<int,4>,V> adj;
void build(){
 for(int i=0;i<V;++i){int k=0;for(int j=0;j<V;++j) if(i!=j){for(int a=0;a<2;++a)for(int b=0;b<2;++b)if(E[i][a]==E[j][b]){ if(k>=4){cerr<<"degree error";exit(1);}adj[i][k++]=j;}}if(k!=4){cerr<<"degree error";exit(1);}}
}
inline int step(int x, bool gh){
 int col[V];int t=x;
 for(int i=0;i<V;++i){col[i]=t%3;t/=3;}
 int result=0,place=1;
 for(int i=0;i<V;++i){int c=col[i];int dst=(c+1)%3;int yes=0;
 if(!gh || c==0){
 for(int j:adj[i])yes+=(col[j]==dst);
 }
 int next=gh?(c==0?((yes>=2)?1:0):dst):((yes>=2)?dst:c);
 result += place*next;place*=3;
 }
 return result;
}
struct Entry{int basin=-1,period=0,depth=0;};
void census(bool gh){
 vector<Entry> dat(N);vector<int> order(N,-1);vector<int> orbit_period,orbit_rep,orbit_size;
 vector<int> path;path.reserve(300);
 for(int init=0;init<N;++init){if(dat[init].basin!=-1)continue;
  path.clear();int y=init;
  while(dat[y].basin==-1 && order[y]==-1){order[y]=(int)path.size();path.push_back(y);y=step(y,gh);}
  int tail,period,basin;
  if(order[y]>=0){int start=order[y];period=(int)path.size()-start;basin=(int)orbit_period.size();orbit_period.push_back(period);orbit_rep.push_back(y);orbit_size.push_back(0);
   for(int k=start;k<(int)path.size();k++){dat[path[k]]={basin,period,0};}tail=start-1;
  }else{basin=dat[y].basin;period=dat[y].period;tail=(int)path.size()-1;}
  for(int k=tail;k>=0;--k){int z=path[k];int nxt=step(z,gh);dat[z]={dat[nxt].basin,dat[nxt].period,dat[nxt].depth+1};}
  for(int z:path)order[z]=-1;
 }
 map<int,int> orbit_count;map<pair<int,int>,int> depth_period;
 map<int,map<int,int>> basins;
 vector<int> basin_size(orbit_period.size(),0);
 for(int i=0;i<N;++i){auto e=dat[i];++basin_size[e.basin];++depth_period[{e.depth,e.period}];}
 for(int i=0;i<(int)orbit_period.size();i++){orbit_count[orbit_period[i]]++;basins[orbit_period[i]][basin_size[i]]++;}
 cout<<(gh?"GHM":"CCA")<<" : N="<<N<<"\n";
 cout<<"orbits";for(auto [p,c]:orbit_count)cout<<" "<<p<<":"<<c;cout<<"\n";
 cout<<"basin sizes\n";for(auto [p,b]:basins){cout<<" period "<<p<<":";for(auto [sz,c]:b)cout<<" "<<sz<<"x"<<c;cout<<"\n";}
 cout<<"entry rows\n";for(auto [dp,c]:depth_period)cout<<" "<<dp.first<<","<<dp.second<<":"<<c;cout<<"\n";
 int maxdepth=0;for(auto &e:dat)maxdepth=max(maxdepth,e.depth);

 map<int,int> expected_orbits = gh ? map<int,int>{{1,1},{3,8}} :
  map<int,int>{{1,81},{3,8},{6,8},{8,36},{12,8}};
 map<int,map<int,int>> expected_basins;
 if(gh){
  expected_basins={{1,{{531417,1}}},{3,{{3,8}}}};
 }else{
  expected_basins={{1,{{116,18},{1300,36},{4989,24},{114627,3}}},
                   {3,{{3,8}}},{6,{{6,8}}},
                   {8,{{416,18},{472,18}}},{12,{{360,8}}}};
 }
 if(orbit_count!=expected_orbits || basins!=expected_basins || maxdepth!=(gh?6:8)){
  cerr<<"Exact census verification failed\n";exit(2);
 }
 int counted=0;for(auto [dp,c]:depth_period)counted+=c;
 if(counted!=N){cerr<<"Incomplete state classification\n";exit(3);}
 cout<<"max depth="<<maxdepth<<"\n";
 for(int i=0;i<N;i++){auto e=dat[i];if(e.depth==maxdepth){cout<<"max depth witness="<<i<<"\n";break;}}
}
int main(){build();census(false);census(true);}
