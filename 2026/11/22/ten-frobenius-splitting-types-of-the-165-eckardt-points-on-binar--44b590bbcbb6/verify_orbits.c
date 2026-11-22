/* Check the thirteen rational projective congruence orbits of invertible
   five-by-five binary matrices via elementary coordinate changes. */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
static uint32_t swap_coords(uint32_t z,int a,int b){
  uint32_t r[5];for(int i=0;i<5;i++)r[i]=(z>>(i*5))&31u;
  uint32_t t=r[a];r[a]=r[b];r[b]=t;
  for(int i=0;i<5;i++)if(((r[i]>>a)^(r[i]>>b))&1u)r[i]^=(1u<<a)|(1u<<b);
  uint32_t out=0;for(int i=0;i<5;i++)out|=r[i]<<(i*5);return out;
}
static uint32_t shear01(uint32_t z){
  uint32_t r[5];for(int i=0;i<5;i++)r[i]=(z>>(i*5))&31u;
  for(int i=0;i<5;i++)if(r[i]&1u)r[i]^=2u; /* column 1 += column 0 */
  r[1]^=r[0]; /* row 1 += row 0 */
  uint32_t out=0;for(int i=0;i<5;i++)out|=r[i]<<(i*5);return out;
}
int main(void){
 const uint32_t ids[13]={1118480,1118482,1118484,1118485,1118486,1118616,1118680,1118744,1118745,1122448,1122450,1122451,1122820};
 const uint32_t expected[13]={13888,208320,104160,104160,624960,1249920,1249920,555520,1666560,555520,833280,833280,1999872};
 unsigned char *seen=calloc(1,1u<<25);
 uint32_t *queue=malloc((size_t)3000000*sizeof(uint32_t));
 if(!seen||!queue){fputs("allocation failed\n",stderr);return 2;}
 uint64_t total=0;
 for(int k=0;k<13;k++){
   uint32_t head=0,tail=0,v=ids[k];
   if(seen[v]){fputs("overlapping seed\n",stderr);return 3;}
   seen[v]=1;queue[tail++]=v;
   while(head<tail){
     uint32_t w=queue[head++],neigh[5];
     for(int i=0;i<4;i++)neigh[i]=swap_coords(w,i,i+1);
     neigh[4]=shear01(w);
     for(int i=0;i<5;i++)if(!seen[neigh[i]]){
       if(tail>=3000000){fputs("orbit queue capacity exceeded\n",stderr);return 4;}
       seen[neigh[i]]=1;queue[tail++]=neigh[i];
     }
   }
   printf("code=%u orbit=%u\n",ids[k],tail);
   if(tail!=expected[k]){fputs("unexpected orbit size\n",stderr);return 5;}
   total+=tail;
 }
 printf("total=%llu\n",(unsigned long long)total);
 if(total!=9999360){fputs("not exhaustive\n",stderr);return 6;}
 free(queue);free(seen);
 puts("ALL_THIRTEEN_GL5_CONGRUENCE_ORBITS_VERIFIED");
 return 0;
}
