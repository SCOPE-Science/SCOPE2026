/* Exhaustive cyclic 2-colorings of K43 (difference colorings mod 43).
   Color of {i,j} depends only on min((j-i)%43,(i-j)%43) in 1..21.
   Fix d1=0 by complement symmetry -> 2^20 = 1048576 colorings.
   By translation symmetry, suffices to check 5-sets containing vertex 0: C(42,4)=111930.
   Early exit on first mono set. Multithreaded over high bits.
   Compile: gcc -O3 -march=native -o cyc cyc.c -lpthread
*/
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <pthread.h>

#define N 43
#define HD 21
#define NSETS 111930

static uint8_t S0[NSETS][4]; /* 5-sets {0,a,b,c,d} stored as a,b,c,d */
static int nsets;

/* difference class of unordered pair */
static inline int dclass(int a,int b){ int d=abs(a-b); if(d>43-d) d=43-d; return d; } /* 1..21 */

static volatile long long done=0;
static volatile int found=0;
static uint8_t found_d[HD+1];

static void check_range(uint32_t start,uint32_t end){
  uint8_t d[HD+1];
  uint8_t c[N][N];
  for(uint32_t mask=start; mask<end && !found; mask++){
    d[1]=0;
    for(int k=2;k<=HD;k++) d[k]=(mask>>(k-1))&1u;
    /* build matrix */
    for(int i=0;i<N;i++){ c[i][i]=0; for(int j=i+1;j<N;j++){ uint8_t b=d[dclass(i,j)]; c[i][j]=b; c[j][i]=b; } }
    int ok=1;
    for(int s=0;s<nsets;s++){
      int a=S0[s][0],b=S0[s][1],e=S0[s][2],f=S0[s][3];
      int sum=c[0][a]+c[0][b]+c[0][e]+c[0][f]+c[a][b]+c[a][e]+c[a][f]+c[b][e]+c[b][f]+c[e][f];
      if(sum==0||sum==10){ ok=0; break; }
    }
    if(ok){
      found=1;
      memcpy(found_d,d,sizeof(d));
      printf("FOUND mask=%u d:",mask);
      for(int k=1;k<=HD;k++) printf("%d",d[k]);
      printf("\n"); fflush(stdout);
      return;
    }
    if(((mask-start)&0xFFFFF)==0xFFFFF){ __sync_fetch_and_add(&done,0x100000); printf("progress: %lldM\n",done/1000000); fflush(stdout); }
  }
}

typedef struct{uint32_t s,e;} Rng;
static void* thr(void*v){ Rng*r=(Rng*)v; check_range(r->s,r->e); return 0; }

int main(int argc,char**argv){
  int nthreads = argc>1?atoi(argv[1]):8;
  /* build 5-sets containing 0 */
  nsets=0;
  for(int a=1;a<N;a++)for(int b=a+1;b<N;b++)for(int e=b+1;e<N;e++)for(int f=e+1;f<N;f++){
    S0[nsets][0]=a;S0[nsets][1]=b;S0[nsets][2]=e;S0[nsets][3]=f;nsets++;
  }
  printf("nsets=%d (expect 111930)\n",nsets);
  uint32_t total=1u<<20;
  pthread_t th[64];
  Rng rng[64];
  for(int i=0;i<nthreads;i++){ rng[i].s=total*i/nthreads; rng[i].e=total*(i+1)/nthreads; pthread_create(&th[i],0,thr,&rng[i]); }
  for(int i=0;i<nthreads;i++) pthread_join(th[i],0);
  if(found){ printf("CYCLIC WITNESS EXISTS\n"); }
  else printf("NO cyclic coloring: exhaustive 2^20 done, none K5-free\n");
  return 0;
}
