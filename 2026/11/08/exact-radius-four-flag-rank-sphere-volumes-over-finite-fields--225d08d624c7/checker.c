/* Independent exhaustive binary radius-four flag-rank check for n=3,...,6. */
/* Build: cc -O2 -std=c11 checker.c -o checker && ./checker */
#include <stdint.h>
#include <inttypes.h>
#include <stdio.h>
static int pos[8][8];
static int rank_binary(const uint32_t *rows, int count) {
    uint32_t piv[8] = {0};
    int r = 0;
    for (int i = 0; i < count; i++) {
        uint32_t x = rows[i];
        while (x) {
            int b = 31 - __builtin_clz(x);
            if (!piv[b]) { piv[b] = x; r++; break; }
            x ^= piv[b];
        }
    }
    return r;
}
static uint64_t predicted(int n) {
    /* q=2: u=1, t=5; binomial coefficients for n-3. */
    uint64_t c2=(uint64_t)(n-3)*(n-4)/2;
    uint64_t c3=n>=6?(uint64_t)(n-3)*(n-4)*(n-5)/6:0;
    uint64_t c4=n>=7?(uint64_t)(n-3)*(n-4)*(n-5)*(n-6)/24:0;
    return (uint64_t)(n-3)*125 +3*c2*25+3*c3*5+c4+(uint64_t)(n-2)*24;
}
int main(void) {
    for (int n=3; n<=6; n++) {
        int k=0;
        for (int i=0;i<n;i++)
            for (int j=i;j<n;j++) pos[i][j]=k++;
        uint64_t count=0, total=UINT64_C(1)<<k;
        for (uint64_t mask=0;mask<total;mask++) {
            int sum=0;
            for (int cut=0;cut<n;cut++) {
                uint32_t rows[8]={0};
                for (int i=0;i<=cut;i++)
                    for (int j=cut;j<n;j++)
                        if (mask & (UINT64_C(1)<<pos[i][j]))
                            rows[i] |= (uint32_t)1 << (j-cut);
                sum += rank_binary(rows,cut+1);
                if (sum>4)break;
            }
            if(sum==4)count++;
        }
        if (count != predicted(n)) {
            fprintf(stderr,"FAIL n=%d expected=%"PRIu64" found=%"PRIu64"\n",
                    n,predicted(n),count);
            return 1;
        }
        printf("n=%d q=2 full_matrices=%"PRIu64" sphere4=%"PRIu64" PASS\n",n,total,count);
    }
    puts("ALL_CHECKS_PASSED");
    return 0;
}
