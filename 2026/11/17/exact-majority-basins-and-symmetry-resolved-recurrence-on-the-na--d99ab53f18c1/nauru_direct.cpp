// Exhaustive state update for synchronous open-neighbour majority on GP(12,5).
// Uses two independently constructed shore transition tables, then iterates all 2^24 full states.
#include <array>
#include <cstdint>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;
int main(){
 constexpr int n=12, V=24, Q=1<<12;
 array<vector<int>,V> adj;
 auto edge=[&](int x,int y){adj[x].push_back(y);adj[y].push_back(x);};
 for(int i=0;i<n;i++){edge(i,(i+1)%n);edge(i,n+i);edge(n+i,n+(i+5)%n);}
 array<int,V> part; part.fill(-1);part[0]=0;queue<int> qq;qq.push(0);
 while(!qq.empty()){int v=qq.front();qq.pop();for(int w:adj[v])if(part[w]==-1){part[w]=1-part[v];qq.push(w);}}
 vector<int> shore[2];
 for(int v=0;v<V;v++)shore[part[v]].push_back(v);
 if(shore[0].size()!=12 || shore[1].size()!=12)return 2;
 int pos[24];for(int k=0;k<2;k++)for(int i=0;i<12;i++)pos[shore[k][i]]=i;
 array<uint16_t,Q> h[2];
 for(int k=0;k<2;k++)for(int mask=0;mask<Q;mask++){
  unsigned result=0;
  for(int i=0;i<12;i++){
   int ones=0;
   for(int nb:adj[shore[k][i]])ones += (mask>>pos[nb])&1;
   if(ones>=2)result |= 1u<<i;
  }
  h[k][mask]=result;
 }
 auto update=[&](uint32_t x)->uint32_t{
  return uint32_t(h[0][x>>12]) | (uint32_t(h[1][x&4095])<<12);
 };
 uint64_t period1=0,period2=0, fixed[8]={}, oscillating[8]={};
 for(uint32_t x=0;x<(1u<<24);x++){
  uint32_t a=x,b=update(a),c=update(b);
  for(int t=0;t<=7;t++){
   if(a==c){if(a==b){fixed[t]++;if(t==0)period1++;}else{oscillating[t]++;if(t==0)period2++;}break;}
   a=b;b=c;c=update(b);
   if(t==7)return 3;
  }
 }
 uint64_t cum=0;
 cout<<"period1="<<period1<<" period2_phases="<<period2<<"\n";
 for(int t=0;t<=7;t++){
  cum+=fixed[t]+oscillating[t];
  cout<<"t="<<t<<" fixed="<<fixed[t]<<" two="<<oscillating[t]<<" cum="<<cum<<"\n";
 }
 return cum==(1u<<24)?0:4;
}
