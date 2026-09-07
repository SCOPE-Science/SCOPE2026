#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
#include <time.h>
// Near-miss census: for each p in [LO,HI], p%30==7, count k = #{o in Offs: p+o prime}.
// Histogram + examples of 5-of-6 by missing offset + 4-of-6 samples.
#define LO 1000000000000ULL
#define HI 1001000000000ULL
#define SEG 5000000ULL
static uint64_t *base_primes; static int nbase;
void simple_sieve(uint64_t limit){
    uint8_t *is=calloc(limit+1,1);
    for(uint64_t i=2;i<=limit;i++) is[i]=1;
    for(uint64_t i=2;i*i<=limit;i++) if(is[i]) for(uint64_t j=i*i;j<=limit;j+=i) is[j]=0;
    int cnt=0; for(uint64_t i=2;i<=limit;i++) if(is[i]) cnt++;
    base_primes=malloc(cnt*sizeof(uint64_t)); nbase=0;
    for(uint64_t i=2;i<=limit;i++) if(is[i]) base_primes[nbase++]=i;
    free(is);
}
int main(int argc,char**argv){
    const char *outpath=(argc>1)?argv[1]:"output/artifacts/miss_table.json";
    uint64_t HIEXT=HI+16;
    uint64_t lim=(uint64_t)sqrt((double)HIEXT)+1;
    simple_sieve(lim);
    uint64_t offs[6]={0,4,6,10,12,16};
    uint64_t hist[7]={0};
    uint64_t miss_by_off[6]={0};
    // store first 8 examples per missing offset for 5-of-6
    uint64_t ex5[6][8]; int nex5[6]={0};
    // store first 8 examples of 4-of-6 (any)
    uint64_t ex4[8]; int nex4=0;
    uint64_t total_cand=0;
    uint64_t L=LO;
    struct timespec t0,t1; clock_gettime(CLOCK_MONOTONIC,&t0);
    while(L<=HIEXT){
        uint64_t R=L+SEG; if(R>HIEXT+1) R=HIEXT+1;
        uint64_t odd_start=(L&1)?L:L+1;
        size_t sz=(odd_start<R)?(size_t)((R-1-odd_start)/2+1):0;
        uint8_t *seg=malloc(sz?sz:1);
        if(sz) memset(seg,1,sz);
        for(int i=0;i<nbase;i++){
            uint64_t p=base_primes[i]; if(p==2) continue;
            uint64_t start=(p*p>L)?p*p:((L+p-1)/p)*p;
            if((start&1)==0) start+=p;
            for(uint64_t j=start;j<R;j+=2*p) seg[(j-odd_start)/2]=0;
        }
        uint64_t scan_lo=L<LO?LO:L;
        uint64_t scan_hi=R-1>HI?HI:R-1;
        uint64_t rem=scan_lo%30;
        uint64_t p0=scan_lo+((7+30-rem)%30);
        for(uint64_t p=p0;p<=scan_hi;p+=30){
            total_cand++;
            int k=0; int miss_idx=-1;
            int prime[6];
            for(int kk=0;kk<6;kk++){
                uint64_t x=p+offs[kk];
                int pr;
                if(x>=L&&x<R) pr=(x&1)?seg[(x-odd_start)/2]:(x==2);
                else { pr=1; for(int i=0;i<nbase;i++){uint64_t q=base_primes[i]; if(q*q>x)break; if(x%q==0){pr=0;break;}} }
                prime[kk]=pr; if(pr) k++; else miss_idx=kk;
            }
            hist[k]++;
            if(k==5){
                miss_by_off[miss_idx]++;
                if(nex5[miss_idx]<8) ex5[miss_idx][nex5[miss_idx]++]=p;
            } else if(k==4 && nex4<8){
                ex4[nex4++]=p;
            }
        }
        free(seg);
        L=R;
    }
    clock_gettime(CLOCK_MONOTONIC,&t1);
    double dt=(t1.tv_sec-t0.tv_sec)+(t1.tv_nsec-t0.tv_nsec)/1e9;
    FILE *f=fopen(outpath,"w");
    fprintf(f,"{\"lo\":%llu,\"hi\":%llu,\"total_candidates_mod30\":%llu,\n",
        (unsigned long long)LO,(unsigned long long)HI,(unsigned long long)total_cand);
    fprintf(f,"\"hist_k_of_6\":{\"0\":%llu,\"1\":%llu,\"2\":%llu,\"3\":%llu,\"4\":%llu,\"5\":%llu,\"6\":%llu},\n",
        (unsigned long long)hist[0],(unsigned long long)hist[1],(unsigned long long)hist[2],
        (unsigned long long)hist[3],(unsigned long long)hist[4],(unsigned long long)hist[5],(unsigned long long)hist[6]);
    fprintf(f,"\"miss5_by_offset\":{\"0\":%llu,\"4\":%llu,\"6\":%llu,\"10\":%llu,\"12\":%llu,\"16\":%llu},\n",
        (unsigned long long)miss_by_off[0],(unsigned long long)miss_by_off[1],(unsigned long long)miss_by_off[2],
        (unsigned long long)miss_by_off[3],(unsigned long long)miss_by_off[4],(unsigned long long)miss_by_off[5]);
    fprintf(f,"\"examples5\":{");
    for(int k=0;k<6;k++){
        fprintf(f,"%s\"%llu\":[",k?",":"",(unsigned long long)offs[k]);
        for(int i=0;i<nex5[k];i++) fprintf(f,"%s%llu",i?",":"",(unsigned long long)ex5[k][i]);
        fprintf(f,"]");
    }
    fprintf(f,"},\"examples4\":[");
    for(int i=0;i<nex4;i++) fprintf(f,"%s%llu",i?",":"",(unsigned long long)ex4[i]);
    fprintf(f,"],\"elapsed_s\":%.3f}",dt);
    fclose(f);
    printf("hist 6=%llu 5=%llu 4=%llu total=%llu time=%.2f\n",
        (unsigned long long)hist[6],(unsigned long long)hist[5],(unsigned long long)hist[4],
        (unsigned long long)total_cand,dt);
    return 0;
}
