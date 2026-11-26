#include <cstdint>
#include <array>
#include <vector>
#include <iostream>
#include <map>
#include <algorithm>
using namespace std;
// Vertices 0..9: doubled vertices of K5: 2*i+epsilon.
// Vertices 10..19: edge vertices (i,j) of K5, lex order.
static constexpr int N=20;
static constexpr uint32_t SIZE=1u<<N;
array<array<int,4>,N> nei;
array<int,10> ea,eb;
void build(){
 int t=0;
 for(int i=0;i<5;i++) for(int j=i+1;j<5;j++) {int v=10+t;ea[t]=i;eb[t]=j;t++;
  nei[v]={2*i,2*i+1,2*j,2*j+1};
 }
 for(int i=0;i<5;i++) for(int e=0;e<2;e++){int t=0;for(int j=0;j<5;j++)if(j!=i){int k=0;while(!(ea[k]==min(i,j)&&eb[k]==max(i,j)))k++;nei[2*i+e][t++]=10+k;}}
}
uint32_t F(uint32_t x){uint32_t y=0;for(int i=0;i<N;i++){
 int s=0;for(int j:nei[i])s+=(x>>j)&1;
 bool bit=(s>2)||((s==2)&&((x>>i)&1));
 y|=uint32_t(bit)<<i;
 }return y;}
int main(){build();
 vector<uint32_t> next(SIZE);
 for(uint32_t x=0;x<SIZE;x++)next[x]=F(x);
 vector<int16_t> dist(SIZE,-1),period(SIZE,0);
 vector<int32_t> where(SIZE,-1);
 vector<uint32_t> path;path.reserve(1000);
 for(uint32_t s=0;s<SIZE;s++) if(dist[s]==-1){
   path.clear();uint32_t z=s;
   while(dist[z]==-1 && where[z]==-1){where[z]=path.size();path.push_back(z);z=next[z];}
   if(dist[z]==-1){int start=where[z],p=path.size()-start;
     for(int k=start;k<(int)path.size();k++){dist[path[k]]=0;period[path[k]]=p;}
     for(int k=start-1;k>=0;k--){dist[path[k]]=dist[next[path[k]]]+1;period[path[k]]=p;}
   } else for(int k=(int)path.size()-1;k>=0;k--){dist[path[k]]=dist[next[path[k]]]+1;period[path[k]]=period[next[path[k]]];}
   for(auto v:path)where[v]=-1;
 }
 map<pair<int,int>,uint64_t> table;
 map<int,uint64_t> rec,basin,cyc;
 int maxdist=0;uint64_t nComplementSwap=0, nHammingEqual=0;
 for(uint32_t s=0;s<SIZE;s++){
  table[{(int)dist[s],(int)period[s]}]++;
  if(dist[s]==0){rec[period[s]]++; if(period[s]==2 && next[s]==(s^(SIZE-1)))nComplementSwap++;}
  basin[period[s]]++;maxdist=max(maxdist,(int)dist[s]);
 }
 cerr<<"N="<<N<<" count="<<SIZE<<"\n";
 for(auto [p,n]:rec)cout<<"RECURRENT period="<<p<<" states="<<n<<" orbits="<<n/p<<"\n";
 for(auto [p,n]:basin)cout<<"BASIN period="<<p<<" states="<<n<<"\n";
 cout<<"MAX="<<maxdist<<" complement_swapping_states="<<nComplementSwap<<"\n";
 for(auto [pair,n]:table)cout<<"SHELL "<<pair.first<<" "<<pair.second<<" "<<n<<"\n";
 // exact 2-step identity at max
}
