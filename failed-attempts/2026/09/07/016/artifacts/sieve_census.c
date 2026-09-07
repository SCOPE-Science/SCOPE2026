#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
#include <time.h>

// Primary segmented sieve, odd-only wheel-2.
// Interval [LO, HI+16], collect p in [LO,HI] with all 6 offsets prime.
#define LO 1000000000000ULL
#define HI 1001000000000ULL
#define SEG 5000000ULL

static uint64_t *base_primes;
static int nbase;

void simple_sieve(uint64_t limit) {
    uint8_t *is = calloc(limit+1,1);
    for (uint64_t i=2;i<=limit;i++) is[i]=1;
    for (uint64_t i=2;i*i<=limit;i++) if(is[i]) for(uint64_t j=i*i;j<=limit;j+=i) is[j]=0;
    int cnt=0; for(uint64_t i=2;i<=limit;i++) if(is[i]) cnt++;
    base_primes=malloc(cnt*sizeof(uint64_t));
    nbase=0; for(uint64_t i=2;i<=limit;i++) if(is[i]) base_primes[nbase++]=i;
    free(is);
}

static inline int is_prime_seg(uint8_t *seg, uint64_t L, uint64_t x){
    // seg covers [L, L+SEGLEN), odd-only: idx=(x-L)/2 if x odd
    if((x&1)==0) return x==2;
    return seg[(x-L)>>1];
}

int main(int argc,char**argv){
    const char *outpath = (argc>1)? argv[1] : "output/artifacts/census.json";
    const char *logpath = (argc>2)? argv[2] : "output/artifacts/sieve_census.log";
    uint64_t HIEXT = HI+16;
    uint64_t lim = (uint64_t)sqrt((double)HIEXT)+1;
    simple_sieve(lim);
    FILE *log=fopen(logpath,"w");
    if(!log){perror("log");return 1;}
    struct timespec t0,t1; clock_gettime(CLOCK_MONOTONIC,&t0);
    fprintf(log,"primary odd-only segmented sieve lo=%llu hi=%llu hiext=%llu seg=%llu nbase=%d baselim=%llu\n",
        (unsigned long long)LO,(unsigned long long)HI,(unsigned long long)HIEXT,(unsigned long long)SEG,nbase,(unsigned long long)lim);
    fflush(log);
    uint64_t *surv = malloc(10000*sizeof(uint64_t));
    size_t nsurv=0, cap=10000;
    uint64_t L=LO;
    // ensure L even/odd handling: segment [L, R)
    while(L<=HIEXT){
        uint64_t R=L+SEG; if(R>HIEXT+1) R=HIEXT+1;
        uint64_t len=R-L;
        // odd-only size: count of odds in [L,R)
        uint64_t odd_start = (L&1)? L : L+1;
        size_t sz = (odd_start<R)? (size_t)((R-1-odd_start)/2+1) : 0;
        uint8_t *seg = malloc(sz?sz:1);
        if(sz) memset(seg,1,sz);
        // mark
        for(int i=0;i<nbase;i++){
            uint64_t p=base_primes[i];
            if(p==2) continue; // odd array all odd assumed prime initially except evens excluded
            uint64_t p2=p*p;
            uint64_t start = p2>L? p2 : ((L+p-1)/p)*p;
            // make start odd multiple (even multiples are not in array)
            if((start&1)==0 && (p&1)==1) start+=p; // p odd, parity flips each multiple; skip evens
            // Actually if p odd, multiples alternate parity; ensure odd:
            // if start even, start+=p (p odd -> odd)
            for(uint64_t j=start;j<R;j+=2*p){
                // j odd in [L,R)
                seg[(j-odd_start)/2]=0;
            }
            // Note: stride 2p because we skip even multiples.
            // But careful: if p2 even? p odd so p2 odd. fine.
        }
        // edge: mark 1 as composite if in range (not here, L>>1)
        // scan candidates p in [L,R) intersect [LO,HI], p%30==7
        uint64_t scan_lo = L<LO?LO:L;
        uint64_t scan_hi = R-1>HI?HI:R-1;
        // first p>=scan_lo with p%30==7
        uint64_t rem = scan_lo%30;
        uint64_t p0 = scan_lo + ((7+30-rem)%30);
        for(uint64_t p=p0;p<=scan_hi;p+=30){
            // check 6 offsets via seg array (all offsets even? p odd, +even=odd, so in array)
            // bounds: p+16 <= HIEXT, and if p near end of segment, p+16 may be in next segment!
            // Handle: only evaluate if p+16 < R, else defer to segment containing p+16? Simpler: require full tuple in current seg; if p+16>=R, lookahead by direct trial? Instead evaluate using primality via trial division for the overflowing tail (at most 16 numbers) OR just require segments overlap.
            // Easiest: if p+16>=R, test those overhanging offsets by trial division with base primes (fast, rare: ~16/5M fraction).
            int ok=1;
            uint64_t offs[6]={0,4,6,10,12,16};
            for(int k=0;k<6;k++){
                uint64_t x=p+offs[k];
                int prime;
                if(x>=L && x<R){
                    if(x&1) prime=seg[(x-odd_start)/2];
                    else prime=(x==2);
                } else {
                    // trial divide x by base primes
                    prime=1;
                    for(int i=0;i<nbase;i++){uint64_t q=base_primes[i]; if(q*q>x) break; if(x%q==0){prime=0;break;}}
                }
                if(!prime){ok=0;break;}
            }
            if(ok){
                if(nsurv>=cap){cap*=2;surv=realloc(surv,cap*sizeof(uint64_t));}
                surv[nsurv++]=p;
            }
        }
        free(seg);
        L=R;
    }
    clock_gettime(CLOCK_MONOTONIC,&t1);
    double dt=(t1.tv_sec-t0.tv_sec)+(t1.tv_nsec-t0.tv_nsec)/1e9;
    fprintf(log,"survivors=%zu elapsed=%.3f s\n",(size_t)nsurv,dt);
    for(size_t i=0;i<nsurv;i++) fprintf(log,"p=%llu\n",(unsigned long long)surv[i]);
    fclose(log);
    FILE *f=fopen(outpath,"w");
    if(!f){perror("out");return 1;}
    fprintf(f,"{\"lo\":%llu,\"hi\":%llu,\"pattern\":[0,4,6,10,12,16],\"count\":%zu,\"list\":[",
        (unsigned long long)LO,(unsigned long long)HI,nsurv);
    for(size_t i=0;i<nsurv;i++) fprintf(f,"%s%llu",(i?",":""),(unsigned long long)surv[i]);
    fprintf(f,"]}");
    fclose(f);
    printf("N=%zu time=%.2fs\n",nsurv,dt);
    free(surv); free(base_primes);
    return 0;
}
