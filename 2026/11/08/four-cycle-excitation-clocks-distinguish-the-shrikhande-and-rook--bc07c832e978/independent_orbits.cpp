#include <iostream>
#include <vector>
#include <array>
#include <map>
#include <cstdint>
#include <cassert>
#include <algorithm>
#include <chrono>
using namespace std;
constexpr uint32_t K=43046721, H=6561;
uint32_t W[16];
uint16_t one8[H],two8[H], neighbors[16], reach1[65536];
void setup(string name){
 W[0]=1;for(int i=1;i<16;i++)W[i]=W[i-1]*3;
 for(unsigned w=0;w<H;w++){
  unsigned q=w;
  for(int k=0;k<8;k++){
   unsigned a=q%3; q/=3;
   if(a==1)one8[w]|=1u<<k;
   if(a==2)two8[w]|=1u<<k;
  }
 }
 for(int v=0;v<16;v++){
  int x=v%4, y=v/4;
  for(int w=0;w<16;w++)if(v!=w){
    int dx=(w%4-x+4)%4,dy=(w/4-y+4)%4;
    bool edge = name=="shri" ?
       ((dx==0&&(dy==1||dy==3)) || (dy==0&&(dx==1||dx==3)) || (dx==dy&&(dx==1||dx==3))) :
       (dx==0 || dy==0);
    if(edge)neighbors[v]|=uint16_t(1u<<w);
  }
  assert(__builtin_popcount((unsigned)neighbors[v])==6);
 }
 for(int mask=0;mask<65536;mask++){
  unsigned a=0;
  for(int u=0;u<16;u++)if(mask&(1<<u))a|=neighbors[u];
  reach1[mask]=a;
 }
}
inline uint32_t evolve(uint32_t s){
 const uint32_t a=s%H,b=s/H;
 uint16_t one = uint16_t(one8[a] | (one8[b]<<8));
 uint16_t two = uint16_t(two8[a] | (two8[b]<<8));
 uint16_t firing = uint16_t(reach1[one] & ~(one|two));
 uint16_t advance=one|firing;
 int32_t o=s;
 while(advance){int v=__builtin_ctz((unsigned)advance);advance&=advance-1;o+=W[v];}
 while(two){int v=__builtin_ctz((unsigned)two);two&=two-1;o-=2*int32_t(W[v]);}
 assert(o>=0 && (uint32_t)o<K);
 return o;
}
int main(int argc,char**argv){
 string g=argc>1?argv[1]:"shri";setup(g);
 vector<uint8_t> state(K,0); // 0 unseen, 1 on current path, 2 done
 vector<uint32_t> depth(K,0);
 vector<uint16_t> period(K,0);
 vector<uint8_t> entry(K,0);
 vector<uint32_t> path; path.reserve(200);
 
 for(uint32_t start=0;start<K;start++){
  if(state[start])continue;
  path.clear();uint32_t x=start;
  while(state[x]==0){
    state[x]=1;depth[x]=path.size();path.push_back(x);x=evolve(x);
  }
  if(state[x]==1){
    uint32_t split=depth[x], len=uint32_t(path.size())-split;
    assert(len<=65535 && len>0);
    for(size_t i=split;i<path.size();i++){uint32_t q=path[i];state[q]=2;period[q]=(uint16_t)len;entry[q]=0;}
    path.resize(split);
  }
  for(size_t i=path.size();i>0;i--){
    uint32_t q=path[i-1], z=evolve(q);
    assert(state[z]==2 && entry[z]<255);
    state[q]=2;period[q]=period[z];entry[q]=entry[z]+1;
  }
 }
 map<pair<int,int>,uint64_t> cnt;
 for(uint32_t s=0;s<K;s++){
  assert(state[s]==2);
  cnt[{entry[s],period[s]}]++;
 }
 uint64_t sum=0;
 cout<<"GRAPH "<<g<<"\n";
 for(auto [tp,n]:cnt){cout<<"CLASS "<<tp.first<<" "<<tp.second<<" "<<n<<"\n";sum+=n;}
 assert(sum==K);
 
}
