#include <bits/stdc++.h>
using namespace std;
// Heawood graph: incidence of the seven-point Fano plane, with lines i,i+1,i+3 (mod 7).
constexpr int Q=4,N=14,H=1<<14,FULL=1<<28;
uint8_t ones[H],np[128],nl[128];
uint16_t tick[H*128];
uint32_t nextstate(uint32_t x) {
 uint32_t p=x&(H-1), l=x>>14;
 return uint32_t(tick[(p<<7)|np[ones[l]]]) | (uint32_t(tick[(l<<7)|nl[ones[p]]])<<14);
}
void init(){
 for(int s=0;s<H;s++){
  uint8_t v=0;
  for(int i=0;i<7;i++)if(((s>>(2*i))&3)==1)v|=(1u<<i);
  ones[s]=v;
  for(int trigger=0;trigger<128;trigger++){
   uint16_t r=0;
   for(int i=0;i<7;i++){
    int a=(s>>(2*i))&3;
    int b = a==0 ? ((trigger>>i)&1):((a+1)&3);
    r |= (b<<(2*i));
   }
   tick[(s<<7)|trigger]=r;
  }
 }
 for(int z=0;z<128;z++){
  for(int i=0;i<7;i++){
   bool tp=0,tl=0;
   for(int d: {0,1,3}){
    if(z&(1u<<((i+d)%7)))tp=true;   // point i adjacent to line i+d
    if(z&(1u<<((i-d+7)%7)))tl=true; // line i adjacent to point i-d
   }
   if(tp)np[z]|=(1u<<i);
   if(tl)nl[z]|=(1u<<i);
  }
 }
}
int main(){
 init();
 vector<uint8_t> depth(FULL,255),period(FULL,0);
 map<pair<int,int>,uint64_t> counts;
 uint64_t computed=0, components=0, max_len=0;
 vector<uint32_t> path;path.reserve(128);
 for(uint32_t seed=0;seed<FULL;seed++){
  if(depth[seed]!=255)continue;
  components++; path.clear();uint32_t v=seed;
  int cycleStart=-1;
  while(depth[v]==255){
   auto hit=find(path.begin(),path.end(),v);
   if(hit!=path.end()){cycleStart=int(hit-path.begin());break;}
   path.push_back(v);v=nextstate(v);
  }
  max_len=max(max_len, uint64_t(path.size()));
  if(cycleStart>=0){
   int cyc=int(path.size())-cycleStart;
   if(cyc>254){cerr<<"PERIOD_TOO_LARGE "<<cyc<<endl;return 2;}
   for(int i=cycleStart;i<int(path.size());i++){
    depth[path[i]]=0;period[path[i]]=cyc;counts[{0,cyc}]++;computed++;
   }
   for(int i=cycleStart-1;i>=0;i--){
    int d=depth[path[i+1]]+1;
    if(d>254){cerr<<"DEPTH_TOO_LARGE "<<d<<endl;return 3;}
    depth[path[i]]=d;period[path[i]]=cyc;counts[{d,cyc}]++;computed++;
   }
  }else{
   int d=depth[v];int cyc=period[v];
   for(int i=int(path.size())-1;i>=0;i--){
    d++;if(d>254){cerr<<"DEPTH_TOO_LARGE "<<d<<endl;return 4;}
    depth[path[i]]=d;period[path[i]]=cyc;counts[{d,cyc}]++;computed++;
   }
  }
 }
 cout<<"Heawood four-state threshold-one GH, vertices=14, states="<<FULL<<"\n";
 cout<<"computed="<<computed<<" components="<<components<<" longest_new_path="<<max_len<<"\n";
 map<int,uint64_t> per_pop,entries;int md=0;
 for(auto [dp,c]:counts){auto [d,p]=dp;per_pop[p]+=c;entries[d]+=c;md=max(md,d);}
 cout<<"max_depth="<<md<<"\n";
 for(auto [p,c]:per_pop)cout<<"period "<<p<<" count "<<c<<"\n";
 for(auto [d,c]:entries)cout<<"entry "<<d<<" count "<<c<<"\n";
 cout<<"last depth per period:\n";
 for(auto [dp,c]:counts){auto [d,p]=dp;if(d==md)cout<<p<<" "<<c<<"\n";}
 for(auto [dp,c]:counts)cout<<"COUNT,"<<dp.first<<","<<dp.second<<","<<c<<"\n";

}
