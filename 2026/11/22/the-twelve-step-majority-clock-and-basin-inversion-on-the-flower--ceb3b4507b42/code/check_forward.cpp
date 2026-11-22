// Exhaustive direct trajectory check on the 20-vertex flower snark J_5.
// Standard C++17, independent vertex-edge construction and forward tracking.
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <vector>
using namespace std;
int main(){
 constexpr int n=5,V=20,L=1<<V;
 array<array<int,3>,V> nb{};
 array<int,V> d{};
 auto add=[&](int u,int v){assert(d[u]<3&&d[v]<3);nb[u][d[u]++]=v;nb[v][d[v]++]=u;};
 // Labels are central a=0..4, outer b=5..9, c=10..14, d=15..19.
 for(int i=0;i<5;i++){add(i,5+i);add(i,10+i);add(i,15+i);}
 for(int i=0;i<5;i++)add(5+i,5+(i+1)%5);
 for(int i=0;i<4;i++){add(10+i,11+i);add(15+i,16+i);}
 add(14,15);add(19,10);
 for(int k:d) assert(k==3);
 vector<uint32_t> f(L);
 for(int x=0;x<L;x++){
  uint32_t y=0;
  for(int v=0;v<V;v++){
   int a=(x>>nb[v][0])&1,b=(x>>nb[v][1])&1,c=(x>>nb[v][2])&1;
   y|=((a&b)|(a&c)|(b&c))<<v;
  }
  f[x]=y;
 }
 map<pair<int,int>,long long> cells;
 vector<int> bas(L,0),period(L,0);
 int max_depth=0,max_count=0;
 for(int x=0;x<L;x++){
  int z=x,t=0;
  while(f[f[z]]!=(uint32_t)z){z=f[z];t++;assert(t<=20);}
  int p=f[z]==(uint32_t)z?1:2;
  int r=p==1?z:min(z,(int)f[z]);
  cells[{t,p}]++;bas[r]++;period[r]=p;
  if(t>max_depth){max_depth=t;max_count=1;}
  else if(t==max_depth)max_count++;
 }
 map<pair<int,int>,int> spectrum;
 int fixed=0,twos=0,twobasin=0;
 for(int r=0;r<L;r++)if(bas[r]){
  spectrum[{period[r],bas[r]}]++;
  if(period[r]==1)fixed++;else{twos++;twobasin+=bas[r];}
 }
 assert(fixed==154&&twos==7397&&max_depth==12&&max_count==240);
 assert(bas[0]==85522&&bas[L-1]==85522&&twobasin==874268);
 assert(cells[make_pair(0,1)]==154&&cells[make_pair(0,2)]==14794&&cells[make_pair(12,2)]==240);
 cout<<"STATES="<<L<<" FIXED="<<fixed<<" TWO_CYCLES="<<twos<<" MAX_DEPTH="<<max_depth<<" MAX_STATES="<<max_count<<" TWO_BASIN="<<twobasin<<" CONSENSUS_PER_COLOR="<<bas[0]<<"\n";
 cout<<"ENTRY_PERIOD";for(auto [key,val]:cells)cout<<" ("<<key.first<<","<<key.second<<","<<val<<")";cout<<"\n";
 cout<<"BASIN_SPECTRUM";for(auto [key,val]:spectrum)cout<<" ("<<key.first<<","<<key.second<<","<<val<<")";cout<<"\n";
}
