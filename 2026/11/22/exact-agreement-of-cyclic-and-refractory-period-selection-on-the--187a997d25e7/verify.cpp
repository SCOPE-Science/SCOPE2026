// Complete finite-state certificate for three-state synchronous contact dynamics
// on the canonical 12-vertex Chvatal graph. No external libraries.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <deque>
#include <iostream>
#include <map>
#include <set>
#include <utility>
#include <vector>
using namespace std;
constexpr int V=12, N=531441;
constexpr pair<int,int> E[]={
 {0,1},{0,4},{0,6},{0,9},{1,2},{1,5},{1,7},
 {2,3},{2,6},{2,8},{3,4},{3,7},{3,9},{4,5},{4,8},
 {5,10},{5,11},{6,10},{6,11},{7,8},{7,11},
 {8,10},{9,10},{9,11}
};
using Neighbors=array<vector<int>,V>;
Neighbors graph(){Neighbors g{};for(auto [a,b]:E){g[a].push_back(b);g[b].push_back(a);}for(auto n:g)assert(n.size()==4);return g;}
int next_state(int x,const Neighbors &g,bool cca){
 int a[V];int y=x;
 for(int i=0;i<V;i++){a[i]=y%3;y/=3;}
 int pow=1,z=0;
 for(int v=0;v<V;v++){
   int out=a[v];
   if(cca){for(int w:g[v])if(a[w]==(a[v]+1)%3){out=(a[v]+1)%3;break;}}
   else if(a[v]!=0)out=(a[v]+1)%3;
   else {for(int w:g[v])if(a[w]==1){out=1;break;}}
   z+=pow*out; pow*=3;
 }
 return z;
}
struct Result{vector<int> entry,period;map<int,int> orbit_counts;int maxdepth=0;long long shell=0;};
Result analyze(bool cca){
 auto g=graph();vector<int> f(N),indeg(N,0),order;order.reserve(N);
 for(int i=0;i<N;i++){f[i]=next_state(i,g,cca);++indeg[f[i]];}
 deque<int> q;for(int i=0;i<N;i++)if(!indeg[i])q.push_back(i);
 while(!q.empty()){int x=q.front();q.pop_front();order.push_back(x);if(--indeg[f[x]]==0)q.push_back(f[x]);}
 Result ans;ans.entry.assign(N,-1);ans.period.assign(N,-1);
 for(int i=0;i<N;i++)if(indeg[i]&&ans.period[i]<0){
  int x=i,p=0;do{++p;x=f[x];}while(x!=i);
  x=i;do{ans.entry[x]=0;ans.period[x]=p;x=f[x];}while(x!=i);
  ++ans.orbit_counts[p];
 }
 for(int j=(int)order.size()-1;j>=0;--j){int x=order[j];
  ans.entry[x]=ans.entry[f[x]]+1;ans.period[x]=ans.period[f[x]];}
 for(int x=0;x<N;x++){
  assert(ans.entry[x]>=0&&ans.period[x]>=1);
  ans.maxdepth=max(ans.maxdepth,ans.entry[x]);
 }
 for(int x=0;x<N;x++)if(ans.entry[x]==ans.maxdepth)++ans.shell;
 return ans;
}
int main(){auto c=analyze(true),h=analyze(false);map<pair<int,int>,int> cross;
 for(int x=0;x<N;x++)++cross[{c.period[x],h.period[x]}];
 assert((c.orbit_counts==map<int,int>{{1,3},{3,4768},{4,882},{7,3036},{10,1512},{11,48}}));
 assert((h.orbit_counts==map<int,int>{{1,1},{3,4768},{4,294},{7,1012},{10,504},{11,8}}));
 assert(c.maxdepth==8&&h.maxdepth==10&&c.shell==192&&h.shell==64);
 assert((cross==map<pair<int,int>,int>{{{1,1},24249},{{3,3},134184},{{4,4},183108},{{7,7},159876},{{10,10},28344},{{11,11},1680}}));
 cout<<"PASS: "<<N<<" initial states; matched least period for every state.\n";
 cout<<"CCA depth "<<c.maxdepth<<" terminal shell "<<c.shell<<"; GHM depth "<<h.maxdepth<<" terminal shell "<<h.shell<<".\n";
 for(auto [key,num]:cross)cout<<"period "<<key.first<<": "<<num<<" initial states\n";
}
