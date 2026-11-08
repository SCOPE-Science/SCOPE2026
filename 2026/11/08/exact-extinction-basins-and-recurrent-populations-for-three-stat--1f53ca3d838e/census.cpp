// Exact finite-state verification of three-color excitable dynamics on the graph
// obtained by deleting a perfect matching from a complete graph.
#include <cstdint>
#include <iostream>
#include <vector>
#include <map>
#include <cassert>
using namespace std;
uint32_t ipow(uint32_t a,int n){uint32_t b=1;while(n--)b*=a;return b;}
uint32_t advance(uint32_t state,int n,const vector<uint32_t>& powers){
  uint8_t x[16];
  for(int j=0;j<n;j++)x[j]=(state/powers[j])%3;
  uint32_t y=0;
  for(int j=0;j<n;j++){
    int b;
    if(x[j])b=(x[j]+1)%3;
    else {
      b=0;
      for(int i=0;i<n;i++)if(i!=j && i!=(j^1) && x[i]==1){b=1;break;}
    }
    y+=powers[j]*b;
  }
  return y;
}
int main(){
 for(int r=2;r<=7;r++){
  int n=2*r;uint32_t N=ipow(3,n);
  vector<uint32_t> powers(n);for(int j=0;j<n;j++)powers[j]=ipow(3,j);
  vector<uint32_t> next(N), degree(N,0), queue(N);
  for(uint32_t a=0;a<N;a++){next[a]=advance(a,n,powers);degree[next[a]]++;}
  uint32_t tail=0,head=0;
  for(uint32_t a=0;a<N;a++)if(degree[a]==0)queue[tail++]=a;
  while(head<tail){uint32_t a=queue[head++],b=next[a];if(--degree[b]==0)queue[tail++]=b;}
  vector<uint8_t> period(N,0), depth(N,0);
  map<int,uint64_t> cycles;
  for(uint32_t a=0;a<N;a++)if(degree[a]>0 && period[a]==0){
    uint32_t b=a;int len=0;
    do{b=next[b];len++;}while(b!=a);
    assert(len<256);cycles[len]++;
    b=a;do{period[b]=len;b=next[b];}while(b!=a);
  }
  for(uint32_t t=tail;t>0;t--){uint32_t a=queue[t-1],b=next[a];period[a]=period[b];depth[a]=depth[b]+1;}
  map<int,uint64_t> basin;int maxdepth=0;
  uint64_t permanent=0;
  for(uint32_t a=0;a<N;a++){basin[period[a]]++;permanent+=depth[a]==0;if(depth[a]>maxdepth)maxdepth=depth[a];}
  cout<<"r="<<r<<" states="<<N<<" cycles=";
  for(auto kv:cycles)cout<<kv.first<<":"<<kv.second<<",";
  cout<<" basins=";
  for(auto kv:basin)cout<<kv.first<<":"<<kv.second<<",";
  cout<<" periodic_points="<<permanent<<" max_entry="<<maxdepth<<"\n";
  if(r>=3){
    uint64_t n3=N,twon=ipow(2,n);
    uint64_t fixed_basin=3*twon-3+6*r;
    uint64_t c3=(n3-3*twon+3-3*n*(ipow(2,n-2)-1))/3;
    assert(cycles.size()==2 && cycles[1]==1 && cycles[3]==c3);
    assert(basin[1]==fixed_basin && basin[3]==N-fixed_basin);
    assert(permanent==1+3*c3);
  }else{
    assert(cycles[1]==1 && cycles[4]==2 && basin[1]==57 && basin[4]==24);
  }
 }
 cout<<"CHECKS_OK\n";
}
