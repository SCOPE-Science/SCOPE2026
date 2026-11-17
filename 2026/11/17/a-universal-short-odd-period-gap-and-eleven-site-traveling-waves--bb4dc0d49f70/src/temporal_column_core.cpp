#include <algorithm>
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <vector>
#include <deque>
using namespace std;
struct A { vector<uint32_t> offset, destination; };
struct Summary {int t;uint32_t vertices; uint64_t edges;uint32_t core_vertices;uint64_t core_edges;vector<int> core_cycles;};
Summary classify(int t){
 const uint32_t m=uint32_t(1)<<t, mask=m-1,N=m*m;
 vector<uint32_t> odegree(N,0),idegree(N,0);
 auto for_edges=[&](auto visit){
  for(uint32_t a=0;a<m;a++)for(uint32_t b=0;b<m;b++){
   const uint32_t forward=((b>>1)|(b<<(t-1)))&mask;
   if((a&(b^forward))!=a)continue;
   const uint32_t forced=(b^forward)&(mask^a);
   uint32_t u=a*m+b,subset=a;
   do{
    uint32_t v=b*m+(forced|subset);
    visit(u,v);
    if(subset==0)break;
    subset=(subset-1)&a;
   }while(true);
  }
 };
 uint64_t E=0;
 for_edges([&](uint32_t u,uint32_t v){++odegree[u];++idegree[v];++E;});
 A out,in;out.offset.resize(N+1);in.offset.resize(N+1);
 for(uint32_t i=0;i<N;i++){out.offset[i+1]=out.offset[i]+odegree[i];in.offset[i+1]=in.offset[i]+idegree[i];}
 out.destination.resize(E);in.destination.resize(E);
 vector<uint32_t> oc=out.offset,ic=in.offset;
 for_edges([&](uint32_t u,uint32_t v){out.destination[oc[u]++]=v;in.destination[ic[v]++]=u;});
 vector<uint8_t> active(N,1);
 deque<uint32_t> q;
 for(uint32_t i=0;i<N;i++)if(!odegree[i]||!idegree[i])q.push_back(i);
 while(!q.empty()){
  uint32_t v=q.front();q.pop_front();
  if(!active[v])continue;
  active[v]=0;
  for(uint32_t j=out.offset[v];j<out.offset[v+1];j++){
   uint32_t w=out.destination[j];
   if(active[w] && --idegree[w]==0)q.push_back(w);
  }
  for(uint32_t j=in.offset[v];j<in.offset[v+1];j++){
   uint32_t w=in.destination[j];
   if(active[w] && --odegree[w]==0)q.push_back(w);
  }
 }
 uint32_t core=0;uint64_t core_e=0;vector<uint8_t> visited(N,0);vector<int> cycles;
 for(uint32_t i=0;i<N;i++)if(active[i]){
  ++core;core_e+=odegree[i];
  if(idegree[i]!=1||odegree[i]!=1)throw runtime_error("A surviving vertex lacks degree one");
 }
 for(uint32_t i=0;i<N;i++)if(active[i]&&!visited[i]){
  uint32_t v=i;int len=0;
  do{
   if(visited[v])throw runtime_error("Non-cycle in residual core");
   visited[v]=1;++len;
   uint32_t next=N;
   for(uint32_t e=out.offset[v];e<out.offset[v+1];e++){
    auto w=out.destination[e]; if(active[w]){next=w;break;}
   }
   if(next==N)throw runtime_error("Residual edge missing");
   v=next;
  }while(v!=i);
  cycles.push_back(len);
 }
 sort(cycles.begin(),cycles.end());
 return {t,N,E,core,core_e,cycles};
}
int main(){
 for(int t:{1,3,5,7,9,11}){
  auto a=classify(t);
  cout<<"t="<<a.t<<" vertices="<<a.vertices<<" edges="<<a.edges<<" core_vertices="<<a.core_vertices<<" core_edges="<<a.core_edges<<" cycles=";
  for(size_t i=0;i<a.core_cycles.size();i++){if(i)cout<<",";cout<<a.core_cycles[i];}
  cout<<'\n';
 }
}
