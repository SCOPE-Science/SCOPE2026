#include <bits/stdc++.h>
using namespace std;
// Icosahedral graph: apices 0,11; top ring 1..5, lower ring 6..10.
int main(){
 constexpr int N=12, Q=4, TOTAL=(1<<(2*N));
 uint16_t adj[N]{};
 auto edge=[&](int a,int b){if(a==b || (adj[a]>>b&1)) throw runtime_error("duplicate"); adj[a]|=1u<<b;adj[b]|=1u<<a;};
 for(int i=0;i<5;i++){
  int j=(i+1)%5;
  edge(0,1+i);edge(11,6+i);
  edge(1+i,1+j);edge(6+i,6+j);
  edge(1+i,6+i);edge(1+i,6+(i+4)%5);
 }
 for(int i=0;i<N;i++){ if(__builtin_popcount((unsigned)adj[i])!=5)throw runtime_error("degree"); }
 cout<<"adjacency=";for(int i=0;i<N;i++)cout<<hex<<adj[i]<<(i+1==N?'\n':',');cout<<dec;
 vector<uint32_t> nxt(TOTAL), indeg(TOTAL,0);
 for(uint32_t x=0;x<TOTAL;x++){
  uint16_t exc=0; uint32_t v=x;
  for(int i=0;i<N;i++,v>>=2) if((v&3)==1)exc|=(1u<<i);
  uint32_t y=0;v=x;
  for(int i=0;i<N;i++,v>>=2){unsigned s=v&3; unsigned ns=s?((s+1)&3):!!(adj[i]&exc); y|=ns<<(2*i);}
  nxt[x]=y; indeg[y]++;
 }
 vector<uint32_t> queue(TOTAL);
 uint32_t tail=0;
 for(uint32_t x=0;x<TOTAL;x++) if(!indeg[x]) queue[tail++]=x;
 for(uint32_t head=0;head<tail;head++){ uint32_t v=queue[head],u=nxt[v];if(--indeg[u]==0)queue[tail++]=u;}
 vector<uint16_t> depth(TOTAL,UINT16_MAX), period(TOTAL,0);
 map<int,uint64_t> orbit_count,periodic_states;
 for(uint32_t x=0;x<TOTAL;x++) if(indeg[x]&&depth[x]==UINT16_MAX){
    uint32_t y=x;uint16_t len=0;do{y=nxt[y];len++;if(len>1024)throw runtime_error("cycle longer than 1024");}while(y!=x);
    orbit_count[len]++;
    y=x;do{depth[y]=0;period[y]=len;y=nxt[y];}while(y!=x);
 }
 map<pair<int,int>,uint64_t> counts;
 for(uint32_t x=0;x<TOTAL;x++) if(indeg[x]){counts[{0,period[x]}]++;periodic_states[period[x]]++;}
 for(uint32_t j=tail;j>0;--j){uint32_t x=queue[j-1],y=nxt[x];depth[x]=depth[y]+1;period[x]=period[y];counts[{depth[x],period[x]}]++;}
 uint64_t check=0;int maxd=0;map<int,uint64_t> max_depth_types;
 for(auto [key,v]:counts){check+=v;maxd=max(maxd,key.first);} 
 for(auto [key,v]:counts)if(key.first==maxd)max_depth_types[key.second]+=v;
 cout<<"TOTAL="<<TOTAL<<";COUNT="<<check<<";MAX_DEPTH="<<maxd<<"\n";
 cout<<"PERIODIC_COUNTS\n";for(auto [p,v]:periodic_states)cout<<p<<","<<v<<","<<orbit_count[p]<<"\n";
 cout<<"MAX_DEPTH_COUNTS\n";for(auto [p,v]:max_depth_types)cout<<p<<","<<v<<"\n";
 cout<<"ALL_DEPTH_PERIOD_COUNTS\n";for(auto [tp,v]:counts)cout<<tp.first<<","<<tp.second<<","<<v<<"\n";
}
