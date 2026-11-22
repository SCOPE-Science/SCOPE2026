#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <vector>
using namespace std;
struct Result {
 vector<int> dest, depth, period, cycle_index, basin;
 vector<vector<int>> cycles;
 map<pair<int,int>,int> td;
 map<int,int> periods;
};
uint16_t step(uint16_t state,bool clamp){
 uint16_t answer=clamp?1u:0u;
 for(int v=clamp?1:0;v<16;v++){
  int adjacent=0;
  for(int j=0;j<4;j++)adjacent+=(state>>(v^(1<<j)))&1u;
  int previous=(state>>v)&1u;
  if(adjacent>2||(adjacent==2&&previous))answer|=(uint16_t)(1u<<v);
 }
 return answer;
}
Result classify(bool clamp){
 int n=clamp?32768:65536;
 Result r;r.dest.resize(n);r.depth.assign(n,0);r.period.assign(n,0);r.cycle_index.assign(n,-1);
 vector<int> indeg(n,0);queue<int> q;vector<int> order;
 for(int i=0;i<n;i++){
  uint16_t full=clamp?(uint16_t)((i<<1)|1u):(uint16_t)i;
  uint16_t updated=step(full,clamp);
  int out=clamp?(int)(updated>>1):(int)updated;
  r.dest[i]=out;++indeg[out];
 }
 for(int i=0;i<n;i++)if(!indeg[i])q.push(i);
 while(!q.empty()){
  int x=q.front();q.pop();order.push_back(x);
  int y=r.dest[x];if(--indeg[y]==0)q.push(y);
 }
 vector<char> seen(n,0);
 for(int i=0;i<n;i++)if(indeg[i]&&!seen[i]){
  vector<int> cycle;
  int v=i;
  do{assert(!seen[v]);seen[v]=1;cycle.push_back(v);v=r.dest[v];}while(v!=i);
  int id=(int)r.cycles.size();int len=(int)cycle.size();assert(len<=2);
  for(int state:cycle){r.cycle_index[state]=id;r.period[state]=len;}
  r.cycles.push_back(cycle);r.periods[len]++;
 }
 r.basin.assign(r.cycles.size(),0);
 for(auto it=order.rbegin();it!=order.rend();it++){
  int x=*it,y=r.dest[x];r.depth[x]=1+r.depth[y];r.period[x]=r.period[y];r.cycle_index[x]=r.cycle_index[y];
 }
 for(int i=0;i<n;i++){
  assert(r.cycle_index[i]>=0);r.basin[r.cycle_index[i]]++;
  r.td[{r.depth[i],r.period[i]}]++;
 }
 return r;
}
int main(){
 auto p=classify(true),u=classify(false);
 long long improvement=0, losses=0, basecons=0, pincons=0;
 int idcons=-1,idlonely=-1;
 for(int i=0;i<(int)p.cycles.size();i++)if(p.cycles[i].size()==1){
  if(p.cycles[i][0]==32767)idcons=i;
  if(p.cycles[i][0]==0)idlonely=i;
 }
 assert(idcons>=0&&idlonely>=0);
 int uidcons=-1,uidzero=-1;
 for(int i=0;i<(int)u.cycles.size();i++)if(u.cycles[i].size()==1){
  if(u.cycles[i][0]==65535)uidcons=i;
  if(u.cycles[i][0]==0)uidzero=i;
 }
 assert(uidcons>=0&&uidzero>=0);
 for(int i=0;i<32768;i++){
  bool pc=p.cycle_index[i]==idcons;
  bool bc=u.cycle_index[(i<<1)|1]==uidcons;
  if(pc)pincons++;
  if(bc)basecons++;
  if(pc&&!bc)improvement++;
  if(!pc&&bc)losses++;
 }
 int maxp=0,maxu=0,witness=-1;
 for(int i=0;i<32768;i++)if(p.depth[i]>maxp){maxp=p.depth[i];witness=i;}
 for(int x:u.depth)maxu=max(maxu,x);
 cout<<"PINNED N=32768 periodic_orbits_fixed="<<p.periods[1]<<" two="<<p.periods[2]<<" sharp_entry="<<maxp<<"\n";
 cout<<"PINNED JOINT_ENTRANCE ";for(auto e:p.td)cout<<"("<<e.first.first<<","<<e.first.second<<")="<<e.second<<" ";cout<<"\n";
 cout<<"PINNED unanimous_basin="<<p.basin[idcons]<<" lone_zealot_basin="<<p.basin[idlonely]<<"\n";
 cout<<"BASELINE N=65536 fixed="<<u.periods[1]<<" two="<<u.periods[2]<<" sharp_entry="<<maxu<<"\n";
 cout<<"SAME_INITIAL_BIT_0_1 baseline_unanimous1="<<basecons<<" pinned_unanimous1="<<pincons<<" gains="<<improvement<<" losses="<<losses<<"\n";
 cout<<"WITNESS_DEPTH_6 full_state="<<((witness<<1)|1)<<" trail=";
 for(int x=witness,j=0;j<=maxp;j++,x=p.dest[x]) {cout<<((x<<1)|1)<<((j==maxp)?"":"->");}
 cout<<"\n";
 int last6=0;for(int i=0;i<32768;i++)if(p.depth[i]==6)last6++;
 cout<<"MAX_DEPTH_POPULATION="<<last6<<"\n";
 assert(p.periods[1]==425&&p.periods[2]==301);
 assert(maxp==6&&maxu==4&&last6==24);
 assert(p.basin[idcons]==9383&&p.basin[idlonely]==3696);
 assert(basecons==8229&&pincons==9383&&improvement==1154&&losses==0);
}
