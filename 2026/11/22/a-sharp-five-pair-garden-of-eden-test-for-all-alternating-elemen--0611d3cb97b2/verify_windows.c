/* Independent direct-window checker, deliberately avoiding the subset graph.
   Each pair of rules is evaluated on all 4096 possible twelve-bit inputs.
   This certifies direct reachability through five adjacent output pairs;
   the separate subset construction certifies the all-length theorem.
   Compile: cc -O2 -std=c11 -Wall -Wextra verify_windows.c -o verify_windows
   Run: ./verify_windows
 */
#include <stdint.h>
#include <stdio.h>
static uint16_t even_outputs[256][4096], odd_outputs[256][4096];
int main(void) {
  for(int x=0;x<4096;x++){
    unsigned window[10];
    for(int i=0;i<10;i++) window[i]=((unsigned)x>>i)&7u;
    for(int r=0;r<256;r++){
      unsigned ev=0,od=0;
      for(int j=0;j<5;j++) {
        ev|= (((unsigned)r>>window[2*j])&1u)<<(2*j);
        od|= (((unsigned)r>>window[2*j+1])&1u)<<(2*j+1);
      }
      even_outputs[r][x]=(uint16_t)ev;
      odd_outputs[r][x]=(uint16_t)od;
    }
  }
  unsigned long histogram[6]={0};
  static uint8_t lengths[256][256];
  for(int f=0;f<256;f++)for(int g=0;g<256;g++){
    uint64_t outputs[16]={0};
    unsigned found=0;
    for(int x=0;x<4096;x++){
      unsigned y=even_outputs[f][x]|odd_outputs[g][x];
      if(((outputs[y>>6]>>(y&63u))&1u)==0) {
        outputs[y>>6]|=1ULL<<(y&63u);
        if(++found==1024) break;
      }
    }
    unsigned shortest=0;
    for(unsigned k=1;k<=5;k++) {
      uint64_t prefixes[16]={0}; unsigned count=0,mask=(1u<<(2*k))-1;
      for(unsigned w=0;w<1024;w++) if((outputs[w>>6]>>(w&63u))&1u) {
        unsigned z=w&mask;
        if(((prefixes[z>>6]>>(z&63u))&1u)==0) {
          prefixes[z>>6]|=1ULL<<(z&63u);
          count++;
        }
      }
      if(count!=(1u<<(2*k))) { shortest=k;break; }
    }
    histogram[shortest]++; lengths[f][g]=(uint8_t)shortest;
  }
  printf("Direct-window length histogram [no missing through 5,1,2,3,4,5]:");
  for(int k=0;k<=5;k++)printf(" %lu",histogram[k]);
  printf("\n");
  unsigned long classes[3][6]={{0}};
  for(int f=0;f<256;f++)for(int g=0;g<256;g++){
    unsigned c=(lengths[f][f]==0)+(lengths[g][g]==0);
    classes[c][lengths[f][g]]++;
  }
  for(int c=0;c<3;c++){
    printf("number of homogeneous onto constituents %d:",c);
    for(int d=0;d<=5;d++)printf(" %lu",classes[c][d]);
    printf("\n");
  }
  if(classes[0][0]!=0||classes[1][0]!=96||classes[2][0]!=612)return 1;
  const unsigned long expected[6]={708,8552,38436,15920,1776,144};
  for(int k=0;k<=5;k++)if(histogram[k]!=expected[k])return 1;
  return 0;
}
