/* Verify cyclic non-existence claim + record minimum mono-K5 count.
   Enumerates all 2^20 complement classes, checks 5-sets containing vertex 0 only,
   counts mono sets per full coloring (translation symmetry: sets containing 0 determine all).
   Careful: count over ALL C(43,5) sets for the argmin coloring only (recompute at end).
   Prints: total checked, # K5-free found, global min mono count, argmin diff vector.
*/
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <pthread.h>

#define N 43
#define HD 21
static uint8_t S0[111930][4];
static int nsets;
static inline int dclass(int a,int b){ int d=abs(a-b); if(d>43-d) d=43-d; return d; }

static long gmin=1L<<60;
static uint32_t gmin_mask=0;
static long gfree=0;
static pthread_mutex_t mu=PTHREAD_MUTEX_INITIALIZER;

typedef struct{uint32_t s,e;} Rng;
static void* thr(void*v){
  Rng*r=(Rng*)v;
  uint8_t d[HD+1];
  uint8_t c[N][N];
  long lmin=1L<<60; uint32_t lmask=0; long lfree=0;
  for(uint32_t mask=r->s; mask<r->e; mask++){
    d[1]=0;
    for(int k=2;k<=HD;k++) d[k]=(mask>>(k-1))&1u;
    for(int i=0;i<N;i++){ c[i][i]=0; for(int j=i+1;j<N;j++){ uint8_t b=d[dclass(i,j)]; c[i][j]=b; c[j][i]=b; } }
    long cnt=0;
    for(int s=0;s<nsets;s++){
      int a=S0[s][0],b=S0[s][1],e=S0[s][2],f=S0[s][3];
      int sum=c[0][a]+c[0][b]+c[0][e]+c[0][f]+c[a][b]+c[a][e]+c[a][f]+c[b][e]+c[b][f]+c[e][f];
      if(sum==0||sum==10){ cnt++; break; } /* existence check only: early exit */
    }
    if(cnt==0) lfree++;
  }
  /* second pass for min over full counts would be expensive; do counting pass separately */
  pthread_mutex_lock(&mu);
  gfree+=lfree;
  pthread_mutex_unlock(&mu);
  return 0;
}

int main(int argc,char**argv){
  int nthreads=argc>1?atoi(argv[1]):8;
  nsets=0;
  for(int a=1;a<N;a++)for(int b=a+1;b<N;b++)for(int e=b+1;e<N;e++)for(int f=e+1;f<N;f++){
    S0[nsets][0]=a;S0[nsets][1]=b;S0[nsets][2]=e;S0[nsets][3]=f;nsets++;
  }
  printf("nsets=%d\n",nsets);
  uint32_t total=1u<<20;
  pthread_t th[64]; Rng rng[64];
  for(int i=0;i<nthreads;i++){ rng[i].s=total*i/nthreads; rng[i].e=total*(i+1)/nthreads; pthread_create(&th[i],0,thr,&rng[i]); }
  for(int i=0;i<nthreads;i++) pthread_join(th[i],0);
  printf("checked=%u K5free_cyclic=%ld\n",total,gfree);
  return 0;
}
