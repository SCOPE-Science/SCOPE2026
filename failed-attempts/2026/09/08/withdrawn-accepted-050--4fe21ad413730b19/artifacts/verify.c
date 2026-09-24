/* verify.c — standalone checker for binary 2-abelian-cube-freeness.
 * Usage: ./verify WORDFILE [MAXLEN]
 * Reads {0,1} characters ignoring whitespace. Checks every end position e and arm m.
 * Reports first cube found or OK. O(n^2/6) comparisons with O(1) prefix-sum + early exit.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(int argc,char**argv){
    if(argc<2){fprintf(stderr,"usage: %s WORDFILE [MAXLEN]\n",argv[0]);return 2;}
    FILE*f=fopen(argv[1],"r"); if(!f){perror("fopen");return 1;}
    size_t cap=1<<20, n=0; unsigned char *w=malloc(cap);
    int c; while((c=fgetc(f))!=EOF){ if(c=='0'||c=='1'){ if(n>=cap){cap*=2;w=realloc(w,cap);} w[n++]=c-'0'; } }
    fclose(f);
    long maxlen = argc>2?atol(argv[2]):(long)n;
    if((long)n>maxlen) n=maxlen;
    int *P[4]; for(int k=0;k<4;k++){P[k]=calloc(n+1,sizeof(int));}
    /* NOTE (repair 2026-09-08): a dead first prefix loop formerly stood here
       (it copied columns without adding any pair counts and was fully
       overwritten by the clean rebuild below); removed so only the audited
       Q-build remains. */
    /* Rebuild cleanly: Q[i] = #pairs starting at j<i */
    for(int k=0;k<4;k++) P[k][0]=0;
    for(size_t i=0;i<n;i++){
        for(int k=0;k<4;k++) P[k][i+1]=P[k][i];
        if(i+1<n){ /* pair starting at i known once w[i],w[i+1] read; add to column i+1 */
            int code=(w[i]<<1)|w[i+1];
            P[code][i+1]++;
        }
    }
    /* Now pairs in [l,r) = Q[r-1]-Q[l] for r-l>=2; for m==1 handle separately */
    long checks=0;
    for(size_t e=3;e<=n;e++){
        for(size_t m=1;m*3<=e;m++){
            size_t s=e-3*m;
            checks++;
            if(!(w[s]==w[s+m]&&w[s+m]==w[s+2*m])) continue;
            if(!(w[s+m-1]==w[s+2*m-1]&&w[s+2*m-1]==w[e-1])) continue;
            if(m==1){printf("CUBE at s=%zu m=%zu (000/111)\n",s,m);return 3;}
            int ok=1;
            for(int k=0;k<4;k++){
                int ca=P[k][s+m-1]-P[k][s];
                int cb=P[k][s+2*m-1]-P[k][s+m];
                if(ca!=cb){ok=0;break;}
                int cc=P[k][e-1]-P[k][s+2*m];
                if(cb!=cc){ok=0;break;}
            }
            if(ok){printf("CUBE at s=%zu m=%zu\n",s,m);return 3;}
        }
        if(e%50000==0) fprintf(stderr,"checked prefix %zu / %zu\n",e,n);
    }
    printf("OK: length %zu 2-abelian-cube-free (checks %ld)\n",n,checks);
    return 0;
}
