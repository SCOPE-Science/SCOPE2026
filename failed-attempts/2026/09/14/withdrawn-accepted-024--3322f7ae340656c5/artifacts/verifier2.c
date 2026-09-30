// Independent verifier: union-find enumeration with different edge ordering.
// Edges listed as: horizontals row-major x-outer vs verifier1 y-outer, plus
// verticals y-outer (transposed loop order). Decision via union-find over
// open edges, then left-set vs right-set intersection. Must agree with 1550368.
#include <stdio.h>
#include <stdint.h>
#define NE 22
#define NV 15
#define NCONF (1u<<22)
static int eu[NE], ev[NE];
static int par[NV], rk[NV];
static int findr(int a){ while(par[a]!=a){par[a]=par[par[a]];a=par[a];} return a; }
static void uni(int a,int b){ a=findr(a);b=findr(b); if(a==b)return;
  if(rk[a]<rk[b])par[a]=b; else if(rk[a]>rk[b])par[b]=a; else{par[b]=a;rk[a]++;} }
int main(void){
  int k=0;
  for(int x=0;x<4;x++) for(int y=0;y<3;y++){ eu[k]=y*5+x; ev[k]=y*5+x+1; k++; }
  for(int y=0;y<2;y++) for(int x=0;x<5;x++){ eu[k]=y*5+x; ev[k]=(y+1)*5+x; k++; }
  long long count=0;
  for(uint32_t mask=0;mask<NCONF;mask++){
    for(int i=0;i<NV;i++){par[i]=i;rk[i]=0;}
    for(int e=0;e<NE;e++) if(mask&(1u<<e)) uni(eu[e],ev[e]);
    int hit=0;
    for(int yl=0;yl<3 && !hit;yl++) for(int yr=0;yr<3 && !hit;yr++)
      if(findr(0*1+yl*5)==findr(4+yr*5)) hit=1;
    // note left vids: (0,yl)->yl*5+0 ; right: (4,yr)->yr*5+4
    if(hit) count++;
  }
  printf("verifier2 count=%lld total=%u\n",count,NCONF);
  return 0;
}
