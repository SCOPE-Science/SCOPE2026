// Exhaustive temporal census of 3-state Greenberg-Hastings on folded 5-cube, 16 vertices.
// Vertices: F_2^4, edges differ by a vector of Hamming weight one or by 1111.
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <inttypes.h>
#include <string.h>
#include <time.h>
#define V 16
#define N 43046721u
static const uint32_t p3[16]={1,3,9,27,81,243,729,2187,6561,19683,59049,177147,531441,1594323,4782969,14348907};
static uint16_t nb[16];
static uint32_t *nx,*deg,*queue;
static uint16_t *entry,*per;
static uint64_t tbl[1024][128], cycles[128];
static uint32_t succ(uint32_t x){
    uint32_t y=x; uint16_t exc=0,ref=0;
    for(int i=0;i<V;++i){uint32_t z=y%3; y/=3; exc|=(uint16_t)(z==1)<<i;ref|=(uint16_t)(z==2)<<i;}
    uint32_t out=0;
    for(int i=0;i<V;++i){
       uint32_t z= ((exc>>i)&1) ? 2u : ((ref>>i)&1) ? 0u : ((exc&nb[i]) ? 1u : 0u);
       out += z*p3[i];
    }
    return out;
}
int main(void){
 for(int i=0;i<V;i++) nb[i]=(1u<<(i^1))|(1u<<(i^2))|(1u<<(i^4))|(1u<<(i^8))|(1u<<(i^15));
 fprintf(stderr,"start N=%u\n",N);
 nx=malloc((size_t)N*sizeof(uint32_t));deg=calloc(N,sizeof(uint32_t));queue=malloc((size_t)N*sizeof(uint32_t));entry=calloc(N,sizeof(uint16_t));per=calloc(N,sizeof(uint16_t));
 if(!nx||!deg||!queue||!entry||!per) {fprintf(stderr,"allocation failure\n");return 1;}
 for(uint32_t x=0;x<N;x++){uint32_t y=succ(x);nx[x]=y;deg[y]++;}
 fprintf(stderr,"successors ready\n");
 uint32_t head=0, tail=0;
 for(uint32_t i=0;i<N;++i)if(!deg[i])queue[tail++]=i;
 while(head<tail){uint32_t x=queue[head++],y=nx[x];if(--deg[y]==0)queue[tail++]=y;}
 fprintf(stderr,"peeled=%u periodic=%u\n",tail,N-tail);
 uint32_t max_cycle=0;
 for(uint32_t x=0;x<N;x++)if(deg[x]){
    uint32_t y=x;unsigned len=0;
    do{deg[y]=0;len++;y=nx[y];}while(y!=x);
    if(len>=128){fprintf(stderr,"long period %u\n",len);return 2;}
    if(len>max_cycle)max_cycle=len;
    cycles[len]++;
    y=x;do{per[y]=(uint16_t)len;y=nx[y];}while(y!=x);
 }
 uint32_t max_entry=0;
 for(uint32_t i=tail;i>0;i--){uint32_t x=queue[i-1];uint32_t y=nx[x];per[x]=per[y];if(entry[y]>=65534){fprintf(stderr,"entry overflow guard\n");return 7;}entry[x]=entry[y]+1; if(entry[x]>max_entry)max_entry=entry[x];}
 fprintf(stderr,"all classified max_entry=%u max_cycle=%u\n",max_entry,max_cycle);
 if(max_entry>=1024) return 3;
 uint64_t sum=0;
 for(uint32_t x=0;x<N;++x){unsigned d=entry[x],p=per[x];if(!p||p>=128){fprintf(stderr,"invalid at %u d=%u p=%u\n",x,d,p);return 4;}tbl[d][p]++;sum++;}
 printf("N=%u periodic=%u transient=%u max_entry=%u max_cycle=%u sum=%" PRIu64 "\n",N,N-tail,tail,max_entry,max_cycle,sum);
 for(unsigned p=1;p<128;p++)if(cycles[p])printf("CYCLE p=%u cycles=%" PRIu64 " states=%" PRIu64 "\n",p,cycles[p],cycles[p]*p);
 for(unsigned d=0;d<=max_entry;d++)for(unsigned p=1;p<128;p++)if(tbl[d][p])printf("CLASS d=%u p=%u count=%" PRIu64 "\n",d,p,tbl[d][p]);
 return 0;
}
