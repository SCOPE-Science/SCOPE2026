// Independent exhaustive incidence check for six-dimensional binary symplectic quadratic refinements.
#include <array>
#include <algorithm>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
using namespace std;
int q(unsigned v){return (((v&1u)&&((v>>3)&1u)) ^ (((v>>1)&1u)&&((v>>4)&1u)) ^ (((v>>2)&1u)&&((v>>5)&1u)))&1u;}
int b(unsigned a,unsigned v){ unsigned x=(a&7u),y=(a>>3),p=(v&7u),t=(v>>3); return (__builtin_popcount(x&t)+__builtin_popcount(y&p))&1u;}
int main(){
  unsigned char ev[64][64]{}; for(unsigned a=0;a<64;a++)for(unsigned v=1;v<64;v++)ev[a][v]=q(v)^b(a,v);
  unsigned long long counts[2][5]{};
  for(int k=0;k<=4;k++){
     int S[5]{};
     auto traverse=[&](auto&& self,int dep,int start)->void{
        if(dep<k){for(int v=start;v<=63-(k-dep)+1;v++){S[dep]=v;self(self,dep+1,v+1);} return;}
        uint32_t mask[2]={0,0};
        for(int a=0;a<64;a++){
           unsigned t=0;for(int j=0;j<k;j++)t|=(unsigned(ev[a][S[j]])<<j);
           mask[q(a)] |= (1u<<t);
        }
        uint32_t target=(1u<<(1u<<k))-1u;
        for(int e=0;e<2;e++)if(mask[e]==target)counts[e][k]++;
     };
     traverse(traverse,0,1);
  }
  unsigned long long expected[2][5]={{1,63,1953,39060,282240},{1,63,1953,35280,282240}};
  for(int e=0;e<2;e++){
    printf("parity %d:",e);for(int k=0;k<=4;k++){printf(" %llu",counts[e][k]);if(counts[e][k]!=expected[e][k])return 3;} puts("");
  }
  puts("DIM6_ALL_SUPPORTS_K_LE4_PASS");
}
