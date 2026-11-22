// Independent finite-state path-tracing certificate for the Paley majority maps.
// Build: g++ -O2 -std=c++17 verify_paley_census.cpp -o verify_paley_census
#include <algorithm>
#include <cassert>
#include <iostream>
#include <map>
#include <numeric>
#include <vector>
using namespace std;
int power_mod(int a,int e,int m){int r=1;while(e){if(e&1)r=(r*a)%m;a=(a*a)%m;e>>=1;}return r;}

void run(int p){
 const int N=1<<p, deg=(p-1)/2, full=N-1;
 vector<vector<int>> nbr(p);
 for(int v=0;v<p;v++)for(int u=0;u<p;u++)if(v!=u){
   int delta=(u-v+p)%p;
   if(power_mod(delta,deg,p)==1)nbr[v].push_back(u);
 }
 for(int v=0;v<p;v++)assert((int)nbr[v].size()==deg);
 vector<int> next(N);
 for(int s=0;s<N;s++){
   int t=0;
   for(int v=0;v<p;v++){
     int sum=0;
     for(int u:nbr[v])sum += 2*((s>>u)&1)-1;
     int old=(s>>v)&1;
     int newvalue = sum>0 ? 1 : (sum<0 ? 0 : old);
     t|=newvalue<<v;
   }
   next[s]=t;
 }
 assert(next[0]==0 && next[full]==full);
 vector<int> assigned(N,-1),depth(N,-1),period(N,-1),seen(N,-1),cycle_lengths;
 for(int s=0;s<N;s++)if(assigned[s]<0){
   vector<int> path;int t=s;
   while(assigned[t]<0 && seen[t]!=s){seen[t]=s;path.push_back(t);t=next[t];}
   int prelen=(int)path.size();
   if(assigned[t]<0){
     int k=0;while(path[k]!=t)k++;
     const int orbit=(int)cycle_lengths.size(), len=prelen-k;
     cycle_lengths.push_back(len);
     for(int j=k;j<prelen;j++){
       assigned[path[j]]=orbit;depth[path[j]]=0;period[path[j]]=len;
     }
     prelen=k;
   }
   while(prelen>0){int a=path[--prelen],b=next[a];
     assigned[a]=assigned[b];depth[a]=depth[b]+1;period[a]=period[b];
   }
 }
 map<int,int> orbit_hist,depth_hist,unfixed_weight;
 map<pair<int,int>,int> basin_hist;
 vector<int> basins(cycle_lengths.size(),0);
 for(int s=0;s<N;s++){
   assert(assigned[s]>=0 && depth[s]>=0);
   depth_hist[depth[s]]++;
   basins[assigned[s]]++;
   if(next[s]==s && s!=0 && s!=full){
      unfixed_weight[__builtin_popcount((unsigned)s)]++;
   }
 }
 for(int len:cycle_lengths){assert(len==1 || len==2); orbit_hist[len]++;}
 for(int j=0;j<(int)basins.size();j++)basin_hist[{cycle_lengths[j],basins[j]}]++;
 int cons=basins[assigned[0]]+basins[assigned[full]],nonfixed=0,osc=0;
 for(int j=0;j<(int)basins.size();j++){
   if(cycle_lengths[j]==2)osc+=basins[j];
   else if(j!=assigned[0] && j!=assigned[full])nonfixed+=basins[j];
 }
 int upper=depth_hist.rbegin()->first;
 cout<<"p="<<p<<" states="<<N<<" fixed="<<orbit_hist[1]<<" two_cycles="<<orbit_hist[2]
     <<" max_entry="<<upper<<" max_entry_population="<<depth_hist[upper]
     <<" consensus_total="<<cons<<" unanimity_basin_each="<<basins[assigned[0]]
     <<" nonconsensus_fixed_basin="<<nonfixed<<" two_cycle_basin="<<osc<<"\n";
 cout<<"entry_histogram:"; for(auto [d,c]:depth_hist)cout<<" "<<d<<":"<<c;cout<<"\n";
 cout<<"basin_histogram:";for(auto [k,c]:basin_hist)cout<<" ("<<k.first<<","<<k.second<<"):"<<c;cout<<"\n";
 cout<<"nonuniform_fixed_by_weight:";for(auto [w,c]:unfixed_weight)cout<<" "<<w<<":"<<c;cout<<"\n";
 assert(cons+nonfixed+osc==N);
}
int main(){run(13);run(17);}
