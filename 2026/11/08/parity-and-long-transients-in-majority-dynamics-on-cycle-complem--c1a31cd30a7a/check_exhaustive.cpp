#include <cassert>
#include <cstdint>
#include <iostream>
#include <string>
using namespace std;
// Independent direct neighbor enumeration, with no formula-based update shortcuts.
uint32_t step(uint32_t x,int N){
 uint32_t y=0;
 for(int v=0;v<N;v++){
  int ones=0,deg=0;
  for(int u=0;u<N;u++){
   if(u==v || u==(v+1)%N || u==(v+N-1)%N)continue;
   deg++;ones+=(x>>u)&1;
  }
  int bit=(x>>v)&1;
  if(2*ones>deg)bit=1;
  else if(2*ones<deg)bit=0;
  y|=uint32_t(bit)<<v;
 }
 return y;
}
int tau(uint32_t x,int N){
 uint32_t a=x,b=step(a,N);
 for(int t=0;t<=N+4;t++){
  uint32_t c=step(b,N);
  if(c==a)return t;
  a=b;b=c;
 }
 return -1;
}
uint32_t wordbits(const string&w){uint32_t x=0;for(int i=0;i<(int)w.size();i++)if(w[i]=='1')x|=1u<<i;return x;}
int main(){
 for(int N=7;N<=19;N+=2){
  uint32_t fixed=0,max_tau=0,bad=0;
  for(uint32_t x=0;x<(1u<<N);x++){
   uint32_t a=step(x,N),b=step(a,N),c=step(b,N);
   if(a==x)fixed++;
   if(b!=c)bad++;
   int t=(a==x?0:(b==a?1:2));
   if(t>max_tau)max_tau=t;
  }
  assert(fixed==uint32_t(2*N+2));
  assert(bad==0);
  assert(max_tau==2);
  cout<<"odd N="<<N<<" states="<<(1u<<N)<<" fixed="<<fixed<<" max_tau="<<max_tau<<" verified\n";
 }
 for(int m=4;m<=10;m++){
  const int N=2*m;
  string w="11";for(int i=0;i<m-2;i++)w+="01";w+="00";
  uint32_t x=wordbits(w);
  int t=tau(x,N);
  assert(t==m-2);
  cout<<"even N="<<N<<" witness_tau="<<t<<" verified\n";
 }
 cout<<"EXHAUSTIVE_OK\n";
}
