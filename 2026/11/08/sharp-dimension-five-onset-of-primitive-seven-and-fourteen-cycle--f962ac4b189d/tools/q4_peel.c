/* Second finite certificate: direct ternary decoding, indegree peeling and cycle discovery. */
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <inttypes.h>
#define N 43046721u
#define V 16
static uint32_t power3[V];
static uint32_t adjacent[V];
static uint32_t *out,*queue,*deg;
static uint8_t *tim,*per;
static uint32_t direct_step(uint32_t x){
 uint8_t c[V];uint32_t z=x,exc=0,ret=0;
 for(int k=0;k<V;k++){c[k]=z%3;z/=3;if(c[k]==1)exc|=1u<<k;}
 for(int k=0;k<V;k++){
  uint32_t next=c[k]==0?!!(exc&adjacent[k]):(c[k]==1?2:0);
  ret+=power3[k]*next;
 }
 return ret;
}
int main(void){
 power3[0]=1;for(int i=1;i<V;i++)power3[i]=power3[i-1]*3;
 for(int i=0;i<V;i++)for(int b=0;b<4;b++)adjacent[i]|=1u<<(i^(1u<<b));
 out=malloc((size_t)N*sizeof(*out));deg=calloc(N,sizeof(*deg));
 queue=malloc((size_t)N*sizeof(*queue));tim=calloc(N,sizeof(*tim));per=calloc(N,sizeof(*per));
 if(!out||!deg||!queue||!tim||!per){fprintf(stderr,"MEMORY FAIL\n");return 2;}
 for(uint32_t x=0;x<N;x++){uint32_t to=direct_step(x);out[x]=to;deg[to]++;}
 uint32_t start=0,end=0;
 for(uint32_t x=0;x<N;x++)if(deg[x]==0)queue[end++]=x;
 while(start<end){uint32_t x=queue[start++],y=out[x];if(--deg[y]==0)queue[end++]=y;}
 uint64_t orbits[64]={0},count[64][64]={0};uint32_t maxT=0,maxP=0;
 for(uint32_t x=0;x<N;x++)if(deg[x]&&!per[x]){
  uint32_t len=0,y=x;
  do{y=out[y];len++;}while(y!=x);
  if(len>=64){fprintf(stderr,"CYCLE OVERFLOW %u\n",len);return 3;}
  orbits[len]++;
  do{per[y]=(uint8_t)len;y=out[y];}while(y!=x);
 }
 for(uint32_t i=end;i>0;){uint32_t x=queue[--i];
  tim[x]=tim[out[x]]+1;per[x]=per[out[x]];
  if(tim[x]>=64){fprintf(stderr,"TRANSIENT OVERFLOW %u\n",tim[x]);return 4;}
 }
 for(uint32_t x=0;x<N;x++){
  if(!per[x]){fprintf(stderr,"UNMARKED %u\n",x);return 5;}
  count[tim[x]][per[x]]++;
  if(tim[x]>maxT)maxT=tim[x];
  if(per[x]>maxP)maxP=per[x];
 }
 printf("N=%u maxT=%u maxP=%u\n",N,maxT,maxP);
 uint64_t sum=0;
 for(uint32_t p=1;p<=maxP;p++)if(orbits[p])printf("ORBIT %u %" PRIu64 "\n",p,orbits[p]);
 for(uint32_t t=0;t<=maxT;t++)for(uint32_t p=1;p<=maxP;p++)if(count[t][p]){
  printf("CLASS %u %u %" PRIu64 "\n",t,p,count[t][p]);sum+=count[t][p];
 }
 printf("CHECK SUM %" PRIu64 "\n",sum);
 free(out);free(deg);free(queue);free(tim);free(per);return sum!=N;
}
