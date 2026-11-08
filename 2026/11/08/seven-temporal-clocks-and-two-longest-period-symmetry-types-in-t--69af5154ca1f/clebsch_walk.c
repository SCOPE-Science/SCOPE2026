// Alternative full-state check: bit-mask lookup update plus forward-walk memoization.
// 5-regular folded hypercube: vertex i adjacent to i xor 1,2,4,8,15.
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <inttypes.h>
#define N 43046721u
#define SPLIT 6561u
static uint16_t e8[6561],r8[6561], contact[65536];
static uint32_t value[65536];
static uint8_t *seen,*period,*depth;
static uint32_t stack[512];
static uint64_t tbl[256][128],cycles[128];
static uint32_t examples[128];
static uint32_t successor(uint32_t x){
 uint32_t lo=x%SPLIT,hi=x/SPLIT;
 uint16_t exc=e8[lo] | (uint16_t)(e8[hi]<<8), ref=r8[lo] | (uint16_t)(r8[hi]<<8);
 uint16_t n_exc=(uint16_t)(contact[exc]&~(exc|ref));
 return value[n_exc]+2u*value[exc];
}
int main(void){
 FILE *rep16=fopen("period16_reps.txt","w");
 FILE *rep13=fopen("period13_reps.txt","w");
 if(!rep16||!rep13)return 10;
 uint32_t p=1;
 for(int j=0;j<16;j++){uint32_t m=1u<<j;for(uint32_t x=0;x<m;x++)value[m|x]=value[x]+p;p*=3;}
 for(uint32_t x=0;x<SPLIT;x++){uint32_t y=x;for(unsigned j=0;j<8;j++,y/=3){if(y%3==1)e8[x]|=1u<<j;else if(y%3==2)r8[x]|=1u<<j;}}
 uint16_t nei[16];for(int j=0;j<16;j++)nei[j]=(1u<<(j^1))|(1u<<(j^2))|(1u<<(j^4))|(1u<<(j^8))|(1u<<(j^15));
 for(uint32_t x=1;x<65536;x++){uint32_t bit=(uint32_t)__builtin_ctz(x);contact[x]=(uint16_t)(contact[x&(x-1)] | nei[bit]);}
 seen=calloc(N,1); period=calloc(N,1);depth=calloc(N,1);
 if(!seen||!period||!depth){fprintf(stderr,"allocation failed\n");return 1;}
 for(uint32_t x0=0;x0<N;x0++){
   if(period[x0])continue;
   uint32_t x=x0;unsigned size=0;
   while(!period[x]&&!seen[x]){if(size>=512){fprintf(stderr,"unexpectedly long transient\n");return 2;}seen[x]=1;stack[size++]=x;x=successor(x);}
   unsigned cycle_begin=size;
   if(!period[x]){
      while(cycle_begin>0&&stack[cycle_begin-1]!=x)cycle_begin--;
      if(cycle_begin==0){fprintf(stderr,"broken path stack\n");return 3;}
      cycle_begin--;
      unsigned length=size-cycle_begin;
      if(length>=128){fprintf(stderr,"long cycle\n");return 4;}
      cycles[length]++;if(!examples[length])examples[length]=x;
      if(length==16||length==13){uint32_t canon=stack[cycle_begin];for(unsigned j=cycle_begin+1;j<size;j++)if(stack[j]<canon)canon=stack[j];fprintf(length==16?rep16:rep13,"%u\n",canon);}
      for(unsigned j=cycle_begin;j<size;j++){period[stack[j]]=length;depth[stack[j]]=0;}
   }
   for(unsigned j=cycle_begin;j>0;j--){uint32_t y=stack[j-1],n=successor(y);period[y]=period[n];if(depth[n]>=254){fprintf(stderr,"depth overflow guard\n");return 6;}depth[y]=depth[n]+1;}
   // If previous path joined already classified, the entire stack is transient.
   for(unsigned j=0;j<size;j++)seen[stack[j]]=0;
 }
 uint64_t sum=0;unsigned mx=0;
 for(uint32_t x=0;x<N;x++){
    unsigned a=depth[x],b=period[x];if(b==0||a>=256||b>=128){fprintf(stderr,"invalid x=%u a=%u b=%u\n",x,a,b);return 5;}
    tbl[a][b]++;sum++;if(mx<a)mx=a;
 }
 printf("N=%u max_entry=%u sum=%" PRIu64 "\n",N,mx,sum);
 for(unsigned j=1;j<128;j++)if(cycles[j])printf("CYCLE p=%u cycles=%" PRIu64 " states=%" PRIu64 " example=%u\n",j,cycles[j],cycles[j]*j,examples[j]);
 for(unsigned a=0;a<=mx;a++)for(unsigned b=1;b<128;b++)if(tbl[a][b])printf("CLASS d=%u p=%u count=%" PRIu64 "\n",a,b,tbl[a][b]);
 fclose(rep16);fclose(rep13);
 return 0;
}
