// Independent full-state check: binary phase planes, on-the-fly walk classification.
#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <map>
#include <numeric>
#include <vector>
using namespace std;
constexpr int M=15;constexpr uint32_t N=14348907;
uint32_t power3[15];
// Independent presentation of the Petersen graph as KG(5,2): vertices are two-subsets.
// The edge set of its line graph is generated from intersecting endpoints of disjoint pairs.
int main(int argc,char**argv){
 int theta=(argc>1)?atoi(argv[1]):1;
 vector<pair<int,int>> subsets;
 for(int i=0;i<5;i++)for(int j=i+1;j<5;j++)subsets.emplace_back(i,j);
 vector<pair<int,int>> edges;
 for(int i=0;i<10;i++)for(int j=i+1;j<10;j++){
   auto a=subsets[i],b=subsets[j];
   if(a.first!=b.first&&a.first!=b.second&&a.second!=b.first&&a.second!=b.second)edges.push_back({i,j});
 }
 if(edges.size()!=15){cerr<<"bad Petersen construction";return 2;}
 array<uint16_t,M> neighbors{};
 for(int i=0;i<M;i++)for(int j=0;j<M;j++)if(i!=j){
   auto a=edges[i],b=edges[j];
   if(a.first==b.first||a.first==b.second||a.second==b.first||a.second==b.second) neighbors[i] |= uint16_t(1)<<j;
 }
 for(int i=0;i<M;i++)if(__builtin_popcount((unsigned)neighbors[i])!=4){cerr<<"bad degree";return 3;}
 power3[0]=1;for(int i=1;i<M;i++)power3[i]=3*power3[i-1];
 vector<uint32_t> next(N);
 for(uint32_t state=0;state<N;state++){
   uint32_t z=state;uint16_t b1=0,b2=0;
   for(int i=0;i<M;i++){int r=z%3;z/=3;if(r==1)b1|=uint16_t(1)<<i;else if(r==2)b2|=uint16_t(1)<<i;}
   uint16_t new1=0,new2=b1;
   uint16_t rest=uint16_t(~(b1|b2))&0x7fff;
   for(int i=0;i<M;i++)if((rest>>i)&1){
     if(__builtin_popcount((unsigned)(neighbors[i]&b1))>=theta)new1|=uint16_t(1)<<i;
   }
   uint32_t out=0;
   for(int i=0;i<M;i++)out+=power3[i]*((new1>>i&1)+2*(new2>>i&1));
   next[state]=out;
 }
 // Find directed cycles by explicit trajectory tracing from every unvisited state.
 vector<uint8_t> mark(N,0),depth(N,0);
 vector<uint32_t> root(N,0);
 vector<int> periods;vector<uint32_t> basins;
 vector<uint32_t> path;path.reserve(100);
 for(uint32_t start=0;start<N;start++){
   if(mark[start])continue;
   path.clear();uint32_t u=start;
   while(mark[u]==0){mark[u]=1;path.push_back(u);u=next[u];}
   if(mark[u]==1){
     size_t k=0;while(k<path.size()&&path[k]!=u)k++;
     if(k==path.size()){cerr<<"nonlocal recursion";return 5;}
     int id=periods.size();
     periods.push_back(int(path.size()-k));basins.push_back(int(path.size()-k));
     for(size_t j=k;j<path.size();j++){auto x=path[j];root[x]=id;depth[x]=0;mark[x]=2;}
     path.resize(k);
   }
   for(auto it=path.rbegin();it!=path.rend();it++){
      auto x=*it,y=next[x];if(mark[y]!=2){cerr<<"bad suffix";return 6;}
      root[x]=root[y];depth[x]=depth[y]+1;basins[root[x]]++;mark[x]=2;
   }
 }
 map<int,uint64_t> orbit_counts,basin_totals,depth_counts;
 map<pair<int,int>,uint64_t> cross,basin_counts;
 uint32_t maxdepth=0,witness=0;
 for(size_t i=0;i<periods.size();i++){
   orbit_counts[periods[i]]++;basin_totals[periods[i]]+=basins[i];basin_counts[{periods[i],(int)basins[i]}]++;
 }
 for(uint32_t i=0;i<N;i++){
   uint32_t d=depth[i];int p=periods[root[i]];
   depth_counts[d]++;cross[{d,p}]++;
   if(d>maxdepth){maxdepth=d;witness=i;}
 }
 cout<<"n_states "<<N<<" n_attractors "<<periods.size()<<" max_depth "<<maxdepth<<" sharp_witness "<<witness<<"\n";
 cout<<"cycles_by_period\n";for(auto [p,n]:orbit_counts)cout<<p<<" "<<n<<" states "<<p*n<<" basin_total "<<basin_totals[p]<<"\n";
 cout<<"by_depth\n";for(auto [d,n]:depth_counts)cout<<d<<" "<<n<<"\n";
 cout<<"depth_by_period\n";for(auto [dp,n]:cross)cout<<dp.first<<" "<<dp.second<<" "<<n<<"\n";
 cout<<"basin_hist_by_period\n";for(auto [pb,n]:basin_counts)cout<<pb.first<<" "<<pb.second<<" "<<n<<"\n";
 // A mask witness in this alternate labeling; deliberately not the same as the first source.
 cout<<"witness_sequence "<<witness;uint32_t v=witness;for(int t=0;t<maxdepth+2;t++){v=next[v];cout<<" "<<v;}cout<<"\n";
}
