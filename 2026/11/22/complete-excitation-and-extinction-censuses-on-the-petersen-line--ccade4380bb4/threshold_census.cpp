// Exact finite-state enumeration of three-state threshold-one refractory dynamics on the Petersen line graph.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <vector>
using namespace std;
constexpr int NV=15;
constexpr uint32_t N=14348907; // 3^15
int main(int argc,char**argv){ int threshold=argc>1?atoi(argv[1]):1; assert(threshold>=1&&threshold<=4);
 vector<pair<int,int>> E;
 for(int i=0;i<5;i++){E.push_back(minmax(i,(i+1)%5)); E.push_back(minmax(i,5+i)); E.push_back(minmax(5+i,5+(i+2)%5));}
 sort(E.begin(),E.end());assert(E.size()==15);
 array<array<int,4>,15> adj{};array<int,15> deg{};
 for(int i=0;i<15;i++)for(int j=0;j<15;j++)if(i!=j&&(E[i].first==E[j].first||E[i].first==E[j].second||E[i].second==E[j].first||E[i].second==E[j].second)){assert(deg[i]<4);adj[i][deg[i]++]=j;}
 for(int i=0;i<15;i++)assert(deg[i]==4);
 uint32_t pow3[NV];pow3[0]=1;for(int i=1;i<NV;i++)pow3[i]=3*pow3[i-1];
 vector<uint32_t> nxt(N);
 for(uint32_t s=0;s<N;s++){
   uint32_t t=s;int a[NV];
   for(int i=0;i<NV;i++){a[i]=t%3;t/=3;}
   uint32_t out=0;
   for(int i=0;i<NV;i++){
     int v=(a[i]==1)?2:0;
     if(a[i]==0){int excited=0;for(int j:adj[i])excited+=(a[j]==1);if(excited>=threshold)v=1;}
     out+=pow3[i]*v;
   }
   nxt[s]=out;
 }
 cerr<<"graph generated, transitions done\n";
 vector<uint32_t> indeg(N,0);
 for(uint32_t t:nxt)++indeg[t];
 vector<uint32_t> order;order.reserve(N);
 for(uint32_t i=0;i<N;i++)if(indeg[i]==0)order.push_back(i);
 for(size_t k=0;k<order.size();k++){uint32_t v=order[k],w=nxt[v];if(--indeg[w]==0)order.push_back(w);}
 cerr<<"peeled "<<order.size()<<"\n";
 vector<uint32_t> root(N, UINT32_MAX);
 vector<uint16_t> depth(N,0);
 vector<uint32_t> period, basins, reps;
 for(uint32_t i=0;i<N;i++)if(indeg[i]>0&&root[i]==UINT32_MAX){
    uint32_t id=period.size(),v=i,len=0;
    do{root[v]=id;v=nxt[v];len++;}while(v!=i);
    period.push_back(len);basins.push_back(len);reps.push_back(i);
 }
 for(auto it=order.rbegin();it!=order.rend();it++){
   auto v=*it,w=nxt[v];root[v]=root[w];depth[v]=depth[w]+1;basins[root[v]]++;
 }
 map<int,uint64_t> cycles, states, attractor_basins, bydepth;
 map<pair<int,int>,uint64_t> cross, basin_hist;
 uint16_t maxdepth=0;uint32_t witness=0;
 for(size_t id=0;id<period.size();id++){
   cycles[period[id]]++; states[period[id]]+=period[id];basin_hist[{period[id],(int)basins[id]}]++;
   attractor_basins[period[id]]+=basins[id];
 }
 for(uint32_t i=0;i<N;i++){
    int p=period[root[i]],d=depth[i];cross[{d,p}]++;bydepth[d]++;
    if(d>maxdepth){maxdepth=d;witness=i;}
 }
 cout<<"graph_edge_list";for(auto e:E)cout<<" ("<<e.first<<","<<e.second<<")";cout<<"\n";
 cout<<"n_states "<<N<<" n_attractors "<<period.size()<<" max_depth "<<maxdepth<<" sharp_witness "<<witness<<"\n";
 cout<<"cycles_by_period\n";for(auto [p,n]:cycles)cout<<p<<" "<<n<<" states "<<states[p]<<" basin_total "<<attractor_basins[p]<<"\n";
 cout<<"by_depth\n";for(auto [d,n]:bydepth)cout<<d<<" "<<n<<"\n";
 cout<<"depth_by_period\n";for(auto [dp,n]:cross)cout<<dp.first<<" "<<dp.second<<" "<<n<<"\n";
 cout<<"basin_hist_by_period\n";for(auto [pb,n]:basin_hist)cout<<pb.first<<" "<<pb.second<<" "<<n<<"\n";
 cout<<"period_representatives\n";
 map<int,uint32_t> pp;
 for(size_t i=0;i<period.size();i++)if(!pp.count(period[i]))pp[period[i]]=reps[i];
 for(auto [p,v]:pp){cout<<p<<" "<<v;uint32_t z=v;for(int k=0;k<p;k++){z=nxt[z];cout<<" "<<z;}cout<<"\n";}
 cout<<"longest_trajectory "<<witness;uint32_t v=witness;for(int i=0;i<maxdepth+2;i++){v=nxt[v];cout<<" "<<v;}cout<<"\n";
}
