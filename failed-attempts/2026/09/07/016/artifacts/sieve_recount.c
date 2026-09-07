#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
#include <time.h>

// Independent recount: wheel-30 candidate sieve.
// Candidates p in [LO,HI], p%30==7. For each base prime q>5, forbid 6 residues p == -o (mod q).
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

// primality of x in [LO,HI+16] by trial division (for cross-check of survivors only)
int is_prime_trial(uint64_t x){
    if(x<2) return 0;
    for(int i=0;i<nbase;i++){uint64_t q=base_primes[i]; if(q*q>x) break; if(x%q==0) return x==q;}
    return 1;
}

int main(int argc,char**argv){
    const char *outpath = (argc>1)? argv[1] : "output/artifacts/recount.json";
    const char *logpath = (argc>2)? argv[2] : "output/artifacts/sieve_recount.log";
    uint64_t HIEXT=HI+16;
    uint64_t lim=(uint64_t)sqrt((double)HIEXT)+1;
    simple_sieve(lim);
    FILE *log=fopen(logpath,"w"); if(!log){perror("log");return 1;}
    struct timespec t0,t1; clock_gettime(CLOCK_MONOTONIC,&t0);
    uint64_t offs[6]={0,4,6,10,12,16};
    // To avoid missing composites where q*q > segment but q divides tuple member,
    // we must mark using ALL base primes (not just q*q<=R), since p+o ~1e12 >> q*q.
    // For candidate sieve, every q>5 can divide some p+o even if q*q << p. So loop all q.
    fprintf(log,"recount wheel-30 seg=%llu nbase=%d baselim=%llu\n",(unsigned long long)SEG,nbase,(unsigned long long)lim);
    uint64_t *surv=malloc(10000*sizeof(uint64_t)); size_t nsurv=0,cap=10000;
    uint64_t L=LO;
    while(L<=HI){
        uint64_t R=L+SEG; if(R>HI+1) R=HI+1;
        // candidate list: p in [L,R) with p%30==7
        uint64_t rem=L%30;
        uint64_t p0=L+((7+30-rem)%30);
        size_t nc=0;
        if(p0<R) nc=(size_t)((R-1-p0)/30+1);
        uint8_t *cand=malloc(nc?nc:1);
        if(nc) memset(cand,1,nc);
        for(int i=0;i<nbase;i++){
            uint64_t q=base_primes[i];
            if(q<=5) continue;
            for(int k=0;k<6;k++){
                uint64_t o=offs[k];
                // need p == -o mod q, p in [L,R), p%30==7
                // find first p>=L with p%q == (q - o%q)%q
                uint64_t need = (q - (o%q))%q;
                uint64_t rL = L%q;
                uint64_t d = (need + q - rL)%q;
                uint64_t pf = L + d;
                // advance to %30==7
                uint64_t r30 = pf%30;
                uint64_t d30 = ((7+30-r30)%30);
                // step must preserve both congruences: step = lcm(q,30) if q not dividing 30
                // Since q>5, gcd(q,30) may be >1 only if q divides 30 (i.e., 2,3,5 excluded). So gcd=1 for q>5.
                // Hence combined step = q*30, and first solution found by advancing pf by multiples of q until %30==7.
                // Instead of CRT, simply iterate: pf += q until %30==7? That could take up to 30 steps. Then stride q*30.
                // Do that:
                int guard=0;
                while(pf<R && pf%30!=7 && guard<40){ pf+=q; guard++; }
                // Actually adding q preserves mod q. Good. But initial pf may have skipped the true first combined solution? No: sequence L+d + t*q enumerates all p in [L,..) with mod q == need. First with mod30==7 is what we want.
                // However the d30 approach above is wrong when q and 30 interact; use loop.
                // Recompute correctly: start from pf0 = L+d, then find t:
                // (already done via loop)
                for(uint64_t p=pf;p<R;p+=q*30){
                    // p satisfies both; but need p%30==7 check (ensured) and index
                    // index = (p-p0)/30
                    if(p< p0) continue; // shouldn't happen since p>=L and p%30==7 implies p>=p0? if p>=L and %30==7 then p>=p0 yes.
                    size_t idx=(size_t)((p-p0)/30);
                    if(idx<nc) cand[idx]=0;
                }
            }
        }
        // survivors in this segment: verify each surviving candidate's 6-tuple by trial division (independent of sieve marking)
        for(size_t i=0;i<nc;i++) if(cand[i]){
            uint64_t p=p0+i*30;
            int ok=1;
            for(int k=0;k<6;k++){ if(!is_prime_trial(p+offs[k])){ok=0;break;} }
            if(ok){
                // only keep if sieve says survivor AND trial confirms (trial is ground truth for these)
                if(nsurv>=cap){cap*=2;surv=realloc(surv,cap*sizeof(uint64_t));}
                surv[nsurv++]=p;
            } else {
                // sieve false positive? log
                // (should not happen since marking is complete; but if it happens, trial corrects)
            }
            // Note: sieve false negatives impossible? If marking missed a composite, trial catches (we require trial). If marking wrongly cleared a true tuple, we'd lose it. To detect, we'd need full trial scan; but marking logic is exact, and primary sieve cross-checks.
        }
        free(cand);
        L=R;
    }
    clock_gettime(CLOCK_MONOTONIC,&t1);
    double dt=(t1.tv_sec-t0.tv_sec)+(t1.tv_nsec-t0.tv_nsec)/1e9;
    fprintf(log,"survivors=%zu elapsed=%.3f s\n",nsurv,dt);
    for(size_t i=0;i<nsurv;i++) fprintf(log,"p=%llu\n",(unsigned long long)surv[i]);
    fclose(log);
    FILE *f=fopen(outpath,"w"); if(!f){perror("out");return 1;}
    fprintf(f,"{\"lo\":%llu,\"hi\":%llu,\"pattern\":[0,4,6,10,12,16],\"count\":%zu,\"list\":[",
        (unsigned long long)LO,(unsigned long long)HI,nsurv);
    for(size_t i=0;i<nsurv;i++) fprintf(f,"%s%llu",(i?",":""),(unsigned long long)surv[i]);
    fprintf(f,"]}");
    fclose(f);
    printf("N=%zu time=%.2fs\n",nsurv,dt);
    free(surv); free(base_primes);
    return 0;
}
