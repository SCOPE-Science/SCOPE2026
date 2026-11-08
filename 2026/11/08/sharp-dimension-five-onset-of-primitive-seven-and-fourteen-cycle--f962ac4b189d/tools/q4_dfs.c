/* Exhaustive finite state classification, deterministic 3-state Greenberg-Hastings rule on 4-cube. */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <inttypes.h>
#define L 6561u
#define N (L*L)
static uint8_t exc[L], resting[L];
static uint16_t base[L], subset[256];
static uint8_t *marked,*entry,*period;
static uint32_t *path;
static size_t pathcap=0;
static uint32_t pow3[8];
static uint8_t nb[8];
static void init(void){
 pow3[0]=1;for(int i=1;i<8;++i)pow3[i]=3*pow3[i-1];
 for(unsigned k=0;k<256;k++) for(int i=0;i<8;i++) if(k&(1u<<i))subset[k]+=pow3[i];
 for(int i=0;i<8;i++)for(int j=0;j<3;j++)nb[i]|=1u<<(i^(1u<<j));
 for(unsigned x=0;x<L;x++){
  unsigned a=x;uint8_t co[8];unsigned e=0,z=0,b=0;
  for(int i=0;i<8;i++){co[i]=a%3;a/=3;if(co[i]==1)e|=1u<<i;}
  for(int i=0;i<8;i++){
   if(co[i]==1)b+=2*pow3[i];
   else if(co[i]==0){if(e&nb[i]) b+=pow3[i]; else z|=1u<<i;}
  }
  exc[x]=e;resting[x]=z;base[x]=b;
 }
}
static inline uint32_t advance(uint32_t x){
 unsigned low=x%L,high=x/L;
 unsigned q0=base[low]+subset[resting[low]&exc[high]];
 unsigned q1=base[high]+subset[resting[high]&exc[low]];
 return q0+L*q1;
}
static void push(uint32_t v, size_t *plen){
 if(*plen==pathcap){pathcap=pathcap?pathcap*2:128;path=realloc(path,pathcap*sizeof(*path));if(!path){fprintf(stderr,"Out of memory\n");exit(2);}}
 path[(*plen)++]=v;
}
int main(void){
 init();marked=calloc(N,1);entry=calloc(N,1);period=calloc(N,1);
 if(!marked||!entry||!period){fprintf(stderr,"Out of memory\n");return 1;}
 uint64_t cnt[256][256]={0};uint64_t orbits[256]={0};unsigned maxT=0,maxP=0;
 for(uint32_t seed=0;seed<N;seed++){
  if(marked[seed]==2)continue;
  size_t len=0;uint32_t v=seed;
  while(!marked[v]){marked[v]=1;push(v,&len);v=advance(v);}
  if(marked[v]==1){
   size_t j=len;while(j && path[j-1]!=v) --j;
   if(j==0){fprintf(stderr,"Cycle detect error\n");return 3;}
   size_t cyclestart=j-1;size_t p=len-cyclestart;
   if(p>255){fprintf(stderr,"Period overflow %zu\n",p);return 4;}
   orbits[p]++;
   for(size_t i=cyclestart;i<len;++i){uint32_t w=path[i];marked[w]=2;entry[w]=0;period[w]=p;}
   len=cyclestart;
  }
  while(len){uint32_t w=path[--len],z=advance(w);unsigned t=entry[z]+1;
   if(t>255){fprintf(stderr,"Transient overflow %u\n",t);return 5;}
   marked[w]=2;entry[w]=(uint8_t)t;period[w]=period[z];
  }
 }
 for(uint32_t x=0;x<N;x++){
  if(marked[x]!=2){fprintf(stderr,"Unvisited\n");return 6;}
  cnt[entry[x]][period[x]]++;if(entry[x]>maxT)maxT=entry[x];if(period[x]>maxP)maxP=period[x];
 }
 uint64_t total=0;
 printf("N=%u maxT=%u maxP=%u\n",N,maxT,maxP);
 for(unsigned p=1;p<=maxP;p++)if(orbits[p]) printf("ORBIT %u %" PRIu64 "\n",p,orbits[p]);
 for(unsigned t=0;t<=maxT;t++)for(unsigned p=1;p<=maxP;p++) if(cnt[t][p]) {printf("CLASS %u %u %" PRIu64 "\n",t,p,cnt[t][p]);total+=cnt[t][p];}
 printf("CHECK SUM %" PRIu64 "\n",total);
 free(marked);free(entry);free(period);free(path);return total!=N;
}
