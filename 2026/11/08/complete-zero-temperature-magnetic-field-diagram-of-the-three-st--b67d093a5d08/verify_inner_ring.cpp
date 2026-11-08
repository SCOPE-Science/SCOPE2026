#include <array>
#include <cstdint>
#include <iostream>
#include <limits>
#include <cassert>
using namespace std;
struct State {int cost=100000;uint64_t ways=0;};
void add(State &t,int cost,uint64_t ways){if(cost<t.cost){t.cost=cost;t.ways=ways;}else if(cost==t.cost)t.ways+=ways;}
int main(){const int N=10; State out[21];
 for(int mask=0;mask<59049;mask++){
  int a[10],q=mask,ki=0,pi=0;
  for(int i=0;i<N;i++){a[i]=q%3;ki+=(a[i]==0);q/=3;}
  for(int i=0;i<N;i++)pi+=(a[i]==a[(i+2)%N]);
  for(int b0=0;b0<3;b0++){
   State curr[3][11],next[3][11]; add(curr[b0][b0==0], a[0]==b0,1);
   for(int i=1;i<N;i++){
    for(int b=0;b<3;b++)for(int k=0;k<=N;k++)next[b][k]=State();
    for(int prev=0;prev<3;prev++)for(int k=0;k<i+1;k++)if(curr[prev][k].ways)
      for(int b=0;b<3;b++)add(next[b][k+(b==0)],curr[prev][k].cost+(a[i]==b)+(prev==b),curr[prev][k].ways);
    for(int b=0;b<3;b++)for(int k=0;k<=N;k++)curr[b][k]=next[b][k];
   }
   for(int b9=0;b9<3;b9++)for(int ko=0;ko<=N;ko++) if(curr[b9][ko].ways) add(out[ki+ko],pi+curr[b9][ko].cost+(b9==b0),curr[b9][ko].ways);
  }
 }
 const int expected_cost[21] = {6,5,4,3,2,1,0,0,0,2,3,5,6,9,12,15,18,21,24,27,30};
 const uint64_t expected_ways[21] = {250,3000,13800,30400,32760,15840,2720,4160,320,57600,30720,115200,1280,40960,79360,61184,24160,5280,640,40,1};
 uint64_t tot=0;for(int k=0;k<=20;k++) {assert(out[k].cost == expected_cost[k] && out[k].ways == expected_ways[k]); cout<<k<<' '<<out[k].cost<<' '<<out[k].ways<<'\n';tot+=out[k].ways;}
 cerr<<"sum-min-per-k "<<tot<<'\n'; cout << "INNER_RING_DP_OK\n";
}
