// Independent exact enumeration and reconfiguration of minimum power dominating sets in Q_5.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <queue>
#include <unordered_map>
#include <vector>
using namespace std;
static uint32_t ng[32];
static int number_vertices=32;
static bool is_pds(uint32_t S){
 uint32_t observed=0;
 for(int v=0;v<32;++v)if(S>>v&1u)observed|=ng[v]|(1u<<v);
 while(true){
  bool changed=false;
  for(int v=0;v<32;++v)if(observed>>v&1u){
   uint32_t missing=ng[v]&~observed;
   if(missing && !(missing&(missing-1))){observed|=missing;changed=true;}
  }
  if(!changed)break;
 }
 return observed == ((uint64_t(1)<<number_vertices)-1);
}
int main(){
 for(int v=0;v<32;++v)for(int j=0;j<5;++j)ng[v]|=1u<<(v^(1<<j));
 for(int a=0;a<32;++a)assert(!is_pds(1u<<a));
 for(int a=0;a<32;++a)for(int b=a+1;b<32;++b)assert(!is_pds((1u<<a)|(1u<<b)));
 for(int a=0;a<32;++a)for(int b=a+1;b<32;++b)for(int c=b+1;c<32;++c)assert(!is_pds((1u<<a)|(1u<<b)|(1u<<c)));
 vector<uint32_t> states;
 for(int a=0;a<32;++a)for(int b=a+1;b<32;++b)for(int c=b+1;c<32;++c)for(int d=c+1;d<32;++d){
  uint32_t s=(1u<<a)|(1u<<b)|(1u<<c)|(1u<<d);
  if(is_pds(s))states.push_back(s);
 }
 assert(states.size()==3600);
 unordered_map<uint32_t,int> loc;
 for(int i=0;i<(int)states.size();++i)loc[states[i]]=i;
 vector<vector<int>> g(states.size());
 long long double_count=0,slide_count=0;
 for(int i=0;i<(int)states.size();++i){
  uint32_t S=states[i];
  for(int u=0;u<32;++u)if(S>>u&1u)for(int v=0;v<32;++v)if(!(S>>v&1u)){
   uint32_t t=(S^(1u<<u))|(1u<<v);
   auto it=loc.find(t);
   if(it!=loc.end()){
    g[i].push_back(it->second);++double_count;
    if(__builtin_popcount((unsigned)(u^v))==1)++slide_count;
   }
  }
 }
 assert(double_count==70400 && slide_count==0);
 map<int,int> deg,ecc;
 for(auto &v:g)deg[(int)v.size()]++;
 assert((deg==map<int,int>{{14,320},{16,400},{18,960},{22,1920}}));
 for(int start=0;start<(int)states.size();++start){
  vector<int> dist(states.size(),-1);queue<int> q;
  dist[start]=0;q.push(start);int e=0,seen=0;
  while(!q.empty()){
   int x=q.front();q.pop();++seen;
   for(int y:g[x])if(dist[y]<0){dist[y]=dist[x]+1;e=max(e,dist[y]);q.push(y);}
  }
  assert(seen==3600);
  ecc[e]++;
 }
 assert((ecc==map<int,int>{{5,1440},{6,2160}}));
 cout<<"Q5_gamma=4 states="<<states.size()<<" TJ_edges="<<double_count/2<<" TS_edges="<<slide_count/2<<" TJ_components=1 radius=5 diameter=6\n";
 cout<<"TJ degrees: ";for(auto [x,y]:deg)cout<<x<<":"<<y<<" ";cout<<"\nTJ eccentricities: ";for(auto [x,y]:ecc)cout<<x<<":"<<y<<" ";cout<<"\n";
 // Q4 control: exactly 32 distance-three pairs, all isolated under adjacent slide.
 number_vertices=16;
 for(int v=0;v<32;++v)ng[v]=0;
 for(int v=0;v<16;++v)for(int j=0;j<4;++j)ng[v]|=1u<<(v^(1<<j));
 int q4=0;
 for(int u=0;u<16;++u)for(int v=u+1;v<16;++v)if(is_pds((1u<<u)|(1u<<v))){
  assert(__builtin_popcount((unsigned)(u^v))==3);++q4;
 }
 assert(q4==32);
 cout<<"Q4_states=32 frozen=true\nPASS\n";
}
