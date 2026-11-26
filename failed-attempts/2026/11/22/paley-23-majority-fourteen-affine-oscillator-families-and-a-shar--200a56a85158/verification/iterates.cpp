#include <cstdint>
#include <cstdio>
#include <vector>
#include <cassert>
using namespace std;
static constexpr int p=23;
static constexpr uint32_t N=1u<<p;
int modpow(int a,int k){int v=1;while(k){if(k&1)v=v*a%p;a=a*a%p;k>>=1;}return v;}
int main(){
 uint32_t mask[23]={};
 for(int i=0;i<23;i++)for(int j=0;j<23;j++){
  int d=(j+23-i)%23;
  if(d && modpow(d,11)==1)mask[i]|=(1u<<j);
 }
 for(int i=0;i<p;i++)assert(__builtin_popcount(mask[i])==11);
 vector<uint32_t> f(N);
 for(uint32_t s=0;s<N;s++){
  uint32_t out=0;
  for(int i=0;i<23;i++) if(__builtin_popcount(s & mask[i])>5)out|=1u<<i;
  f[s]=out;
 }
 vector<uint32_t> f2(N),f4(N);
 for(uint32_t s=0;s<N;s++)f2[s]=f[f[s]];
 for(uint32_t s=0;s<N;s++)f4[s]=f2[f2[s]];
 vector<uint32_t> img(N);
 for(uint32_t s=0;s<N;s++)img[s]=s;
 uint64_t last1=0,last4=0;
 printf("INDEPENDENT_ENTRY_HISTOGRAM\n");
 for(int t=0;t<=10;t++){
  uint64_t c1=0,c4=0;
  for(uint32_t s=0;s<N;s++){
   uint32_t y=img[s];
   if(f4[y]==y){
     if(f[y]==y)c1++;
     else {assert(f2[y]!=y);c4++;}
   }
  }
  assert(c1>=last1 && c4>=last4);
  printf("%d %llu %llu\n",t,(unsigned long long)(c1-last1),(unsigned long long)(c4-last4));
  if(t==0)assert(c1==2 && c4==14168);
  if(t==9)assert(c1+c4<N);
  if(t==10)assert(c1+c4==N);
  last1=c1;last4=c4;
  if(t<10)for(uint32_t s=0;s<N;s++)img[s]=f[img[s]];
 }
 // At t=10 every state is fixed under four more updates; no other least period is possible.
 // This independently certifies the global identity F^14 = F^10 and the sharp cutoff 10.
 printf("TOTAL %llu\n",(unsigned long long)(last1+last4));
 printf("INDEPENDENT_ITERATES_OK\n");
}
