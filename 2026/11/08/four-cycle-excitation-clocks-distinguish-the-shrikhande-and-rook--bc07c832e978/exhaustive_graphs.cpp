#include <bits/stdc++.h>
using namespace std;
constexpr uint32_t S=43046721; // 3^16
constexpr int V=16;
uint32_t p3[V];
uint16_t neighborhood[V], uniontab[65536];

void graph(const string& name){
 for(int u=0;u<V;u++){
   int a=u/4,b=u%4; uint16_t nb=0;
   if(name=="rook"){
      for(int v=0;v<V;v++)if(v!=u && (v/4==a || v%4==b))nb|=1u<<v;
   } else {
      for(auto [da,db]:vector<pair<int,int>>{{1,0},{3,0},{0,1},{0,3},{1,1},{3,3}}){int x=(a+da)%4,y=(b+db)%4;nb|=1u<<(4*x+y);}
   }
   neighborhood[u]=nb;
 }
 for(int mask=1;mask<65536;mask++){
  int lb=__builtin_ctz((unsigned)mask);
  uniontab[mask]=uniontab[mask&(mask-1)] | neighborhood[lb];
 }
 // graph assertions
 for(int u=0;u<V;u++){
  assert(__builtin_popcount((unsigned)neighborhood[u])==6);
  for(int v=0;v<V;v++){
   assert( ((neighborhood[u]>>v)&1)==((neighborhood[v]>>u)&1) );
   if(v!=u){int common=__builtin_popcount((unsigned)(neighborhood[u]&neighborhood[v]));assert(common==2);}
  }
 }
}
inline uint32_t step(uint32_t x){
 uint32_t tmp=x,output=x;uint16_t ones=0,zeros=0;
 for(int i=0;i<V;i++){
  int c=tmp%3;tmp/=3;
  if(c==0)zeros|=(1u<<i);
  else if(c==1){ones|=1u<<i;output+=p3[i];}
  else output-=2*p3[i];
 }
 uint32_t active= zeros & uniontab[ones];
 while(active){int i=__builtin_ctz((unsigned)active);active&=active-1;output+=p3[i];}
 return output;
}
int main(int argc,char**argv){
 string name= argc>1 ? argv[1]:"shri";
 p3[0]=1;for(int i=1;i<V;i++)p3[i]=p3[i-1]*3;
 graph(name);
 
 vector<uint32_t> nxt(S),indeg(S,0); vector<uint32_t> order;order.reserve(S);
 for(uint32_t x=0;x<S;x++){
  uint32_t y=step(x);
  assert(y<S);nxt[x]=y;indeg[y]++;
 }
 
 for(uint32_t x=0;x<S;x++)if(indeg[x]==0)order.push_back(x);
 for(size_t i=0;i<order.size();i++){
  uint32_t x=order[i], y=nxt[x];
  if(--indeg[y]==0)order.push_back(y);
 }
 
 vector<uint16_t> tt(S,0), pp(S,0);
 map<int,uint64_t> cycles;
 for(uint32_t x=0;x<S;x++)if(indeg[x]!=0 && pp[x]==0){
   uint32_t y=x;uint32_t len=0;
   do {len++;y=nxt[y];} while(y!=x && len<=S);
   assert(y==x && len<65536);cycles[len]++;
   y=x;do {pp[y]=len;indeg[y]=0;y=nxt[y];} while(y!=x);
 }
 for(size_t j=order.size();j>0;j--){
  uint32_t x=order[j-1],y=nxt[x];
  assert(pp[y]!=0);tt[x]=tt[y]+1;pp[x]=pp[y];
 }
 map<pair<int,int>,uint64_t> classes;
 uint64_t period_total=0;
 int tmax=0;
 for(uint32_t x=0;x<S;x++){
  assert(pp[x]>0);
  classes[{tt[x],pp[x]}]++;
  tmax=max(tmax,(int)tt[x]);
  if(tt[x]==0)period_total++;
 }
 
 cout<<"GRAPH "<<name<<"\n";cout<<"TOTAL "<<S<<"\n";
 cout<<"PERIODIC "<<period_total<<"\n";cout<<"MAX_TRANSIENT "<<tmax<<"\n";
 for(auto [len,count]:cycles)cout<<"CYCLE "<<len<<" "<<count<<"\n";
 for(auto [tp,count]:classes)cout<<"CLASS "<<tp.first<<" "<<tp.second<<" "<<count<<"\n";
}
