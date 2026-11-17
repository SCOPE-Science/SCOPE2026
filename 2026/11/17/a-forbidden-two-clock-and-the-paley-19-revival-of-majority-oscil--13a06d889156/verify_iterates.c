/* Independent C11 direct-iterate test for majority on Paley tournaments. */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

static int res[20], nr;
static unsigned int *next_map;
static unsigned int nstates;
static int order;

static unsigned int update(unsigned int x) {
  unsigned int y = 0;
  int degree = nr;
  for (int vertex = 0; vertex < order; ++vertex) {
    int votes = 0;
    for (int t = 0; t < nr; ++t) {
      int neighbor = (vertex + res[t]) % order;
      votes += (x >> neighbor) & 1u;
    }
    if (2 * votes > degree) y |= 1u << vertex;
  }
  return y;
}

static unsigned int iterate(unsigned int x, int steps) {
  for (int i=0;i<steps;++i) x=next_map[x];
  return x;
}

static void run(int p) {
  order=p;
  int q[20]={0}; nr=0;
  for (int i=1;i<p;++i) q[(i*i)%p]=1;
  for (int i=1;i<p;++i) if(q[i])res[nr++]=i;
  if (nr!=(p-1)/2){fputs("bad degree\n",stderr);exit(2);}
  nstates=1u<<p;
  next_map=malloc((size_t)nstates*sizeof(*next_map));
  unsigned char *periodic=calloc(nstates,1);
  if(!next_map || !periodic) exit(2);
  for (unsigned int x=0;x<nstates;++x)next_map[x]=update(x);
  int exponent=(p==19?76:(p==7?7:(p==3?3:1)));
  int cutoff=(p==19?7:(p==11?5:(p==7?3:0)));
  long long period_hist[100]={0},depth_hist[30]={0};
  long long by_depth_period[30][100]={{0}};
  int maxdepth=0;
  int all_identity=1,sharp_identity=0;
  for(unsigned int x=0;x<nstates;++x){
    periodic[x]=(iterate(x,exponent)==x);
  }
  for (unsigned int x=0;x<nstates;++x) {
    unsigned int v=x;
    int depth=0;
    while(!periodic[v]){
      v=next_map[v];++depth;
      if (depth>cutoff){fprintf(stderr,"cutoff exceeded p=%d x=%u\n",p,x);exit(3);}
    }
    if(depth>maxdepth)maxdepth=depth;
    int L=1;
    unsigned int z=next_map[v];
    while(z!=v && L<=exponent){z=next_map[z];++L;}
    if (L>exponent || exponent%L){fprintf(stderr,"period invalid\n");exit(4);}
    ++depth_hist[depth];++period_hist[L];++by_depth_period[depth][L];
    if(iterate(x,cutoff+exponent)!=iterate(x,cutoff))all_identity=0;
    if(cutoff>0 && iterate(x,cutoff-1+exponent)!=iterate(x,cutoff-1))sharp_identity=1;
  }
  if(!all_identity || (cutoff>0 && !sharp_identity))exit(5);
  printf("p=%d states=%u maximum_entry=%d identity_F(%d+%d)=F(%d) verified\n",p,nstates,maxdepth,cutoff,exponent,cutoff);
  printf("recurrent_periodic_states:");
  for(int L=1;L<=exponent;++L)if(period_hist[L]) {
    long long recurrent=by_depth_period[0][L];
    printf(" %d:%lld",L,recurrent);
  }
  puts("");
  printf("period_basin_sizes:");
  for(int L=1;L<=exponent;++L)if(period_hist[L])printf(" %d:%lld",L,period_hist[L]);
  puts("");
  printf("depth_hist:");for(int d=0;d<=maxdepth;++d)printf(" %d:%lld",d,depth_hist[d]);puts("");
  printf("depth_period_hist:");
  for(int d=0;d<=maxdepth;++d)for(int L=1;L<=exponent;++L)if(by_depth_period[d][L])printf(" (%d,%d):%lld",d,L,by_depth_period[d][L]);
  puts("");
  free(periodic);free(next_map);
}

int main(void){run(3);run(7);run(11);run(19);return 0;}
