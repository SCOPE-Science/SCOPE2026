/* Exact normalized signed-hafnian census for perfect matchings of K8.
   This uses a direct parity evaluation, independent of any Fourier transform. */
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#define EDGES 21
#define TOTAL (1u<<EDGES)
static uint32_t masks[105];
static int mask_count=0;
static int edge_bit[8][8];
static uint64_t counts[106]={0};
/* Independently specified exact 23-level histogram: all other counts must vanish. */
static const uint64_t expected[106]={
 [1]=403200,[3]=259280,[5]=256032,[7]=289680,[9]=221340,
 [11]=175560,[13]=146160,[15]=122976,[17]=90720,[19]=33600,
 [21]=23800,[23]=25200,[25]=15750,[27]=16800,[29]=5040,
 [33]=6720,[39]=3430,[41]=210,[43]=840,[45]=336,
 [57]=420,[75]=56,[105]=2
};
static void matchings(unsigned remaining,uint32_t mask) {
    if (!remaining) { if(mask_count>=105) abort(); masks[mask_count++]=mask; return; }
    int a=__builtin_ctz(remaining);
    remaining &= ~(1u<<a);
    for (int b=a+1;b<8;++b) if(remaining&(1u<<b)) {
        uint32_t mask2=mask;
        if(a!=0) mask2 ^= (1u<<edge_bit[a][b]);
        matchings(remaining & ~(1u<<b),mask2);
    }
}
int main(void){
    int k=0;
    for(int a=1;a<8;++a) for(int b=a+1;b<8;++b) edge_bit[a][b]=k++;
    if(k!=EDGES) abort();
    matchings(255u,0u);
    if(mask_count!=105) abort();
    for(uint32_t x=0;x<TOTAL;++x){
        int h=0;
        for(int i=0;i<105;++i) h+= __builtin_parity(x&masks[i]) ? -1 : 1;
        int abs_h=h<0?-h:h;
        if(abs_h>105) abort();
        counts[abs_h]++;
    }
    for(int j=0;j<=105;++j) if(counts[j]!=expected[j]) {
        fprintf(stderr,"COUNT_MISMATCH_AT_%d\n",j); return 3;
    }
    uint64_t sum=0,sq=0,quart=0;
    for(int j=0;j<=105;++j) if(counts[j]) {
       printf("%d %llu\n",j,(unsigned long long)counts[j]);
       sum+=(uint64_t)j*counts[j];
       sq+=(uint64_t)j*j*counts[j];
       quart+=(uint64_t)j*j*j*j*counts[j];
    }
    fprintf(stderr,"DIRECT_MATCHINGS=%d; TOTAL=%u; ABS_SUM=%llu; SECOND=%llu; FOURTH=%llu\n",mask_count,TOTAL,(unsigned long long)sum,(unsigned long long)sq,(unsigned long long)quart);
    if(sum!=16854180ull || sq!=220200960ull || quart!=84777369600ull) return 2;
    puts("DIRECT_HAFNIAN_CENSUS_PASS");
    return 0;
}
