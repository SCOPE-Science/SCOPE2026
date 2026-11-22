// Exact independent verification of icosahedral synchronous majority dynamics.
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <set>
using namespace std;
constexpr int S=4096, N=12;
constexpr int graph[N][5] = {
 {1,2,3,4,5}, {0,2,5,6,10}, {0,1,3,6,7}, {0,2,4,7,8},
 {0,3,5,8,9}, {0,1,4,9,10}, {1,2,7,10,11}, {2,3,6,8,11},
 {3,4,7,9,11}, {4,5,8,10,11}, {1,5,6,9,11}, {6,7,8,9,10}
};
int next_state(int s){
 int r=0;
 for(int v=0;v<N;v++){
  int b[5]; for(int i=0;i<5;i++) b[i]=(s>>graph[v][i])&1;
  // Threshold 3 of 5 computed by exhaustive triples rather than popcount.
  bool maj=false;
  for(int i=0;i<5;i++)for(int j=i+1;j<5;j++)for(int k=j+1;k<5;k++)
     maj |= (b[i] && b[j] && b[k]);
  if(maj)r|=(1<<v);
 }
 return r;
}
int main(){
 array<int,S> f{};
 for(int s=0;s<S;s++)f[s]=next_state(s);
 for(int s=0;s<S;s++)assert(f[S-1-s]==S-1-f[s]);
 for(int v=0;v<N;v++)for(int j=0;j<5;j++){
   int w=graph[v][j],count=0;
   for(int k=0;k<5;k++)count+=(graph[w][k]==v);
   assert(count==1);
 }
 map<pair<int,int>,int> first;
 map<int,int> basins;
 map<int,int> states_per_period;
 set<int> caps;
 for(int v=0;v<N;v++){
  int m=1<<v;
  for(int i=0;i<5;i++)m|=(1<<graph[v][i]);
  caps.insert(m);
 }
 assert(caps.size()==12);
 int max_t=0,maximum_count=0;
 for(int s=0;s<S;s++){
  int x=s,t=-1;
  for(int i=0;i<6;i++){
   if(f[f[x]]==x){t=i;break;}
   x=f[x];
  }
  assert(t>=0);max_t=max(max_t,t);maximum_count+=(t==5);
  int p= f[x]==x?1:2;
  first[{t,p}]++;states_per_period[p]++;
  basins[min(x,f[x])]++;
 }
 assert(first.at({0,1})==14 && first.at({0,2})==312);
 assert(first.at({1,1})==386 && first.at({1,2})==600);
 assert(first.at({2,1})==984 && first.at({3,1})==1080);
 assert(first.at({4,1})==480 && first.at({5,1})==240);
 assert(first.size()==8 && max_t==5 && maximum_count==240);
 assert(states_per_period[1]==3184 && states_per_period[2]==912);
 assert(basins.size()==170 && basins[0]==1586 && basins[S-1]==1586);
 for(int cap:caps)assert(f[cap]==cap && basins[cap]==1);
 map<int,int> d2;
 for(auto [r,n]:basins)if(f[r]!=r)d2[n]++;
 assert((d2==map<int,int>({{2,16},{4,60},{6,60},{14,20}})));
 int twocycles=0, fixed=0;
 for(int s=0;s<S;s++){
    if(f[s]==s)fixed++;
    else if(f[f[s]]==s && s<f[s])twocycles++;
 }
 assert(fixed==14 && twocycles==156);
 cout<<"CHECK_ALL_4096_STATES=PASS\n";
 cout<<"FIXED=14 PRIMITIVE_TWO_CYCLES=156\n";
 cout<<"CONSENSUS_BASINS=1586,1586\n";
 cout<<"OTHER_FIXED_BASINS=12_singletons\n";
 cout<<"TWO_CYCLE_BASIN_SIZES=2:16,4:60,6:60,14:20\n";
 cout<<"FIRST_ENTRY=(0,1):14,(0,2):312,(1,1):386,(1,2):600,(2,1):984,(3,1):1080,(4,1):480,(5,1):240\n";
 cout<<"SHARP_MAX_ENTRY=5 EXTREMAL_STATES=240\n";
}
