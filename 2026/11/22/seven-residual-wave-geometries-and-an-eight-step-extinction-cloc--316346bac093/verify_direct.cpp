// Exact functional-graph enumeration of three-state two-contact excitable dynamics.
// Build: c++ -O2 -std=c++17 verify_direct.cpp -o verify_direct
// Run from this directory: ./verify_direct
#include <algorithm>
#include <array>
#include <cassert>
#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <vector>
using namespace std;
int main() {
 constexpr int n=12;
 int pw[n+1];pw[0]=1;for(int i=1;i<=n;i++)pw[i]=3*pw[i-1];
 const int N=pw[n];
 ifstream in("adjacency.txt");if(!in){cerr<<"Cannot open adjacency.txt\n";return 2;}
 array<array<int,5>,n> adj{};
 for(int i=0;i<n;i++)for(int j=0;j<5;j++)if(!(in>>adj[i][j]))return 3;
 // First implementation: exact base-three integer encoding and iterative graph walk.
 vector<int> F(N);
 for(int x=0;x<N;x++) {
  int d[n],a=x;
  for(int i=0;i<n;i++){d[i]=a%3;a/=3;}
  int y=0;
  for(int i=0;i<n;i++){
   int v=0;
   if(d[i]==1)v=2;
   else if(d[i]==0){int c=0;for(int j:adj[i])c+=(d[j]==1);v=(c>=2);}
   y+=pw[i]*v;
  }
  F[x]=y;
 }
 vector<int> depth(N,-1),period(N,0),which(N,-1),local(N,-1);
 vector<int> orbit_period,orbit_root,basin;
 for(int x=0;x<N;x++)if(depth[x]<0){
  vector<int> path;
  int y=x;
  while(depth[y]<0 && local[y]<0){local[y]=int(path.size());path.push_back(y);y=F[y];}
  if(depth[y]>=0){
   int d=depth[y],p=period[y],o=which[y];
   for(int j=int(path.size())-1;j>=0;j--){int v=path[j];depth[v]=++d;period[v]=p;which[v]=o;basin[o]++;}
  } else {
   int s=local[y],p=int(path.size())-s,o=int(basin.size());
   if(p!=1&&p!=3){cerr<<"Unexpected period "<<p<<"\n";return 4;}
   int root=*min_element(path.begin()+s,path.end());
   orbit_period.push_back(p);orbit_root.push_back(root);basin.push_back(0);
   for(int j=s;j<int(path.size());j++){int v=path[j];depth[v]=0;period[v]=p;which[v]=o;basin[o]++;}
   for(int j=s-1;j>=0;j--){int v=path[j];depth[v]=s-j;period[v]=p;which[v]=o;basin[o]++;}
  }
  for(int v:path)local[v]=-1;
 }
 map<pair<int,int>,long long> hist;map<int,int> b3;int count1=0,count3=0,maxdepth=0,sharp=0;
 for(int x=0;x<N;x++){
  hist[{depth[x],period[x]}]++;maxdepth=max(maxdepth,depth[x]);
  if(period[x]==1)count1++;else count3++;
  int y=x;for(int j=0;j<8;j++)y=F[y];int z=F[F[F[y]]];
  if(y!=z){cerr<<"F^11 != F^8 at "<<x<<"\n";return 5;}
 }
 int n1=0,n3=0;
 vector<pair<int,int>> roots;
 for(int k=0;k<int(basin.size());k++){
  if(orbit_period[k]==1){n1++;if(basin[k]!=count1)return 6;}
  else{n3++;b3[basin[k]]++;roots.push_back({orbit_root[k],basin[k]});}
 }
 sort(roots.begin(),roots.end());
 ofstream rout("orbit_roots.csv");rout<<"root_code,basin_size\n";
 for(auto [code,bs]:roots)rout<<code<<","<<bs<<"\n";
 cout<<"states="<<N<<"\n";
 cout<<"fixed_orbits="<<n1<<" three_orbits="<<n3<<"\n";
 cout<<"fixed_basin="<<count1<<" three_basin_total="<<count3<<"\n";
 cout<<"entry_period_counts:\n";
 for(auto [dp,c]:hist)cout<<dp.first<<","<<dp.second<<":"<<c<<"\n";
 cout<<"max_entry="<<maxdepth<<" states_at_max="<<hist[{maxdepth,1}]+hist[{maxdepth,3}]<<"\n";
 cout<<"three_basin_histogram:";for(auto [size,num]:b3)cout<<" "<<size<<":"<<num;cout<<"\n";
 int code=2824;
 cout<<"witness_code="<<code<<" witness_trajectory:";
 for(int j=0;j<=9;j++){cout<<" "<<code;code=F[code];}cout<<"\n";
 cout<<"identity_F11_eq_F8=verified\n";
 // Check sharpness of identity by existence of state with depth 8.
 if(maxdepth!=8||n3!=200||n1!=1||count3!=1260)return 7;
 return 0;
}
