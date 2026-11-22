// Finite, exhaustive check of the nonzero-square neighborhood traces over F_81.
// Compile: c++ -O3 -std=c++17 verify_direct.cpp -o verify_direct && ./verify_direct
#include <array>
#include <cstdint>
#include <cstdio>
#include <functional>
#include <cassert>
using namespace std;
constexpr int q=81;
int dig[q][4], addt[q][q], negt[q], prod[q][q];
bool is_square[q], adj[q][q];
int encode(const int c[4]) {int n=0,p=1;for(int i=0;i<4;i++){n+=p*c[i];p*=3;}return n;}
void field(){
 for(int x=0;x<q;x++) {int t=x;for(int i=0;i<4;i++){dig[x][i]=t%3;t/=3;}}
 for(int x=0;x<q;x++){
  int a[4];for(int i=0;i<4;i++)a[i]=(3-dig[x][i])%3;negt[x]=encode(a);
  for(int y=0;y<q;y++){
   int b[4];for(int i=0;i<4;i++)b[i]=(dig[x][i]+dig[y][i])%3;addt[x][y]=encode(b);
   int c[7]={};for(int i=0;i<4;i++)for(int j=0;j<4;j++)c[i+j]=(c[i+j]+dig[x][i]*dig[y][j])%3;
   // x^4+x+2:  x^4 = 1+2x over F_3.
   for(int k=6;k>=4;k--){int t=c[k];c[k]=0;c[k-4]=(c[k-4]+t)%3;c[k-3]=(c[k-3]+2*t)%3;}
   prod[x][y]=encode(c);
  }
 }
 for(int x=1;x<q;x++)is_square[prod[x][x]]=true;
 int ns=0;for(int x=0;x<q;x++)ns+=is_square[x];assert(ns==40 && !is_square[0]);
 for(int v=0;v<q;v++)for(int y=0;y<q;y++)adj[v][y]=is_square[addt[y][negt[v]]];
 for(int v=0;v<q;v++){int degree=0;for(int y=0;y<q;y++)degree+=adj[v][y];assert(degree==40 && !adj[v][v]);}
}
inline bool shattered(const int s[6],int k){
 uint64_t seen=0;int cnt=0;
 for(int v=0;v<q;v++){
  unsigned pat=0;
  for(int i=0;i<k;i++)pat |= (unsigned)adj[v][s[i]]<<i;
  uint64_t b=uint64_t(1)<<pat;
  if(!(seen&b)){seen|=b;cnt++;}
  if(cnt==(1<<k))return true;
  if(cnt+q-1-v < (1<<k))return false;
 }
 return false;
}
int main(){
 field();int s[6]={0};
 const unsigned long long expected[7]={1,81,3240,85320,1658880,9515880,0};
 for(int k=0;k<=6;k++){
  if(k==0){puts("k=0 all=1");continue;}
  unsigned long long hit=0,visited=0;
  function<void(int,int)> rec=[&](int pos,int lo){
   if(pos==k){visited++; if(shattered(s,k))hit++;return;}
   for(int x=lo;x<q;x++){s[pos]=x;rec(pos+1,x+1);}
  };rec(1,1);
  assert(hit*81%k==0);
  auto count=hit*81/k;
  printf("k=%d normalized=%llu passed=%llu all=%llu\n",k,visited,hit,count);
  if(count!=expected[k])return 1;
 }
 puts("DIRECT_OK");
}
