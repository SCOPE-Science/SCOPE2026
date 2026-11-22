/* Direct, exact, exhaustive rank distribution for every binary mask on F_5^2.
   Compile: cc -O3 -std=c11 full_direct_check.c -o full_direct_check
   Run: ./full_direct_check
   Coordinates of bit 5*x+y are (x,y) in F_5^2.
   Cyclotomic divisibility says a nonzero Fourier line vanishes iff its
   five parallel affine fibres have equal indicator sums.
*/
#include <stdint.h>
#include <stdio.h>
#include <inttypes.h>
#include <assert.h>
static uint32_t pencil[6][5];
static uint64_t count[26][26];
static void make_pencils(void) {
  for (int x=0;x<5;x++) for(int y=0;y<5;y++) {
    uint32_t bit=UINT32_C(1)<<(5*x+y);
    for (int m=0;m<5;m++) pencil[m][(y-m*x+25)%5] |= bit;
    pencil[5][x] |= bit;
  }
}
int main(void) {
  make_pencils();
  for (uint32_t s=0;s<(UINT32_C(1)<<25);s++) {
    int w=__builtin_popcount(s), rank;
    if (!w) rank=0;
    else if (w%5) rank=25;
    else {
      int zero=0;
      for(int d=0;d<6;d++) {
        int fiber=__builtin_popcount(s & pencil[d][0]);
        int balanced=1;
        for(int b=1;b<5;b++)
          if (__builtin_popcount(s & pencil[d][b])!=fiber) {balanced=0;break;}
        zero+=balanced;
      }
      rank=25-4*zero;
    }
    assert(rank>=0 && rank<=25);
    count[w][rank]++;
  }
  uint64_t sums[26]={0}, total=0;
  for(int w=0;w<=25;w++) for(int r=0;r<=25;r++) sums[r]+=count[w][r];
  for(int r=0;r<=25;r++) if(sums[r]) {printf("rank=%d count=%"PRIu64"\n",r,sums[r]);total+=sums[r];}
  printf("total=%"PRIu64"\n",total);
  assert(total== (UINT64_C(1)<<25));
  assert(sums[0]==1 && sums[1]==1 && sums[5]==180 && sums[13]==4000 &&
         sums[17]==51000 && sums[21]==1122600 && sums[25]==32376650);
  for(int r=0;r<=25;r++) if(r!=0 && r!=1 && r!=5 && r!=13 && r!=17 && r!=21 && r!=25) assert(sums[r]==0);
  for(int w=0;w<=25;w++) for(int r=0;r<=25;r++) if(count[w][r])
       printf("w=%d rank=%d count=%"PRIu64"\n",w,r,count[w][r]);
  return 0;
}
