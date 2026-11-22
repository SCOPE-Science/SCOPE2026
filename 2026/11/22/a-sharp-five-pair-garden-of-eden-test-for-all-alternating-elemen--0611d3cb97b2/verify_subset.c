/* Exact subset-construction certificate for all 2-periodic elementary-rule pairs.
   Compile: cc -O2 -std=c11 -Wall -Wextra verify_subset.c -o verify_subset
   Run: ./verify_subset
   This is a complete enumeration of all 65,536 pairs, not a sample. */
#include <stdint.h>
#include <stdio.h>
#include <string.h>

static uint8_t edge[8][4], trans[256][4], seen[256], queue[256], depth[256];

/* Returns zero if the pair-block image is the entire four-symbol shift.
   Otherwise returns the exact length (in pairs) of a shortest missing word. */
static int first_missing(int f, int g) {
  for (unsigned u=0;u<8;u++) {
    unsigned a=u>>2, b=(u>>1)&1, c=u&1;
    for (unsigned y=0;y<4;y++) edge[u][y]=0;
    for (unsigned d=0;d<2;d++) for (unsigned e=0;e<2;e++) {
      unsigned y=(((unsigned)f>>(4*a+2*b+c))&1u)*2u
               + (((unsigned)g>>(4*b+2*c+d))&1u);
      edge[u][y] |= (uint8_t)(1u<<(4*c+2*d+e));
    }
  }
  for (unsigned s=0;s<256;s++) for (unsigned y=0;y<4;y++) {
    uint8_t out=0;
    for (unsigned u=0;u<8;u++) if ((s>>u)&1u) out|=edge[u][y];
    trans[s][y]=out;
  }
  memset(seen,0,sizeof(seen));
  unsigned head=0,tail=0;
  queue[tail++]=255;seen[255]=1;depth[255]=0;
  while(head<tail) {
    unsigned s=queue[head++];
    for (unsigned y=0;y<4;y++) {
      unsigned t=trans[s][y];
      if (t==0) return depth[s]+1;
      if (!seen[t]) {
        seen[t]=1;
        depth[t]=depth[s]+1;
        if(tail>=256) return -1;
        queue[tail++]=(uint8_t)t;
      }
    }
  }
  return 0;
}
int main(void) {
  static uint8_t result[256][256];
  unsigned long histogram[6]={0};
  unsigned long categories[3][6]={{0}};
  unsigned long homogeneous_surjective=0;
  for(int f=0;f<256;f++)for(int g=0;g<256;g++){
    int z=first_missing(f,g);
    if(z<0||z>5) { fprintf(stderr,"unexpected depth %d for (%d,%d)\n",z,f,g);return 1; }
    result[f][g]=(uint8_t)z;
    histogram[z]++;
  }
  for(int f=0;f<256;f++) if(result[f][f]==0) homogeneous_surjective++;
  for(int f=0;f<256;f++)for(int g=0;g<256;g++){
    unsigned a=result[f][f]==0, b=result[g][g]==0;
    categories[a+b][result[f][g]]++;
  }
  unsigned unequal=0;
  for(int f=0;f<256;f++) for(int g=f+1;g<256;g++) if(result[f][g]!=result[g][f]) { unequal++; if(unequal==1) printf("first phase length mismatch: (%d,%d): %u vs %u\n", f,g,result[f][g],result[g][f]);}
  printf("unequal swapped depths=%u\n", unequal);
  printf("pair_length,onto,one,two,three,four,five\n");
  printf("all,%lu,%lu,%lu,%lu,%lu,%lu\n",
    histogram[0],histogram[1],histogram[2],histogram[3],histogram[4],histogram[5]);
  for(int category=0;category<3;category++) {
    printf("%d_homogeneous_surjective",category);
    for(int k=0;k<=5;k++)printf(",%lu",categories[category][k]);
    printf("\n");
  }
  printf("surjective homogeneous elementary rules=%lu\n",homogeneous_surjective);
  printf("witness (22,105): shortest forbidden block-pair length=%u\n",result[22][105]);
  printf("witness (51,54): onto=%s; homogeneous statuses=%u,%u\n",
     result[51][54]==0?"yes":"no",result[51][51]==0,result[54][54]==0);
  if (homogeneous_surjective!=30 ||
      histogram[0]!=708 || histogram[1]!=8552 || histogram[2]!=38436 ||
      histogram[3]!=15920 || histogram[4]!=1776 || histogram[5]!=144 ||
      categories[0][0]!=0 || categories[1][0]!=96 || categories[2][0]!=612 ||
      result[22][105]!=5 || result[51][54]!=0) return 1;
  return 0;
}
