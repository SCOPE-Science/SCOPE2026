/* Independent brute-force verifier for Av(4231,3124) / Av(4231,3214) census.
 * Method: max-insertion DFS; every new perm checked by scanning EVERY index
 * quadruple and ranking values (no incremental insertion-slot lemma).
 * Permutations stored as values 1..n (census.c uses 0..n-1 + different check).
 * Parallelized over a brute-force frontier at depth K0.
 * Compile: gcc -O2 -fopenmp verify_brute.c -o verify_brute
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#ifdef _OPENMP
#include <omp.h>
#endif

static int NMAX;
static const unsigned char F4231[4]={4,2,3,1}, F3124[4]={3,1,2,4}, F3214[4]={3,2,1,4};

static inline void pat4(int v0,int v1,int v2,int v3, unsigned char r[4]) {
    int v[4]={v0,v1,v2,v3};
    for(int i=0;i<4;i++){ int k=1; for(int j=0;j<4;j++) if(v[j]<v[i]) k++; r[i]=(unsigned char)k; }
}
static inline int ispat(unsigned char r[4], const unsigned char f[4]){
    return r[0]==f[0]&&r[1]==f[1]&&r[2]==f[2]&&r[3]==f[3];
}
/* bitmask over full scan: 1=has4231 2=has3124 4=has3214 */
static int scan(unsigned char *a,int n){
    int m=0;
    unsigned char r[4];
    for(int i0=0;i0<n&&m!=7;i0++)for(int i1=i0+1;i1<n&&m!=7;i1++)
    for(int i2=i1+1;i2<n&&m!=7;i2++)for(int i3=i2+1;i3<n;i3++){
        pat4(a[i0],a[i1],a[i2],a[i3],r);
        if(ispat(r,F4231))m|=1; if(ispat(r,F3124))m|=2; if(ispat(r,F3214))m|=4;
    }
    return m;
}
static void dfs(unsigned char *a,int n,long long *lA,long long *lB){
    if(n>=1){
        int m=scan(a,n);
        /* a of length n already known live from parent; rescan asserts */
        if(m&1){ fprintf(stderr,"INCONSISTENT 4231 at n=%d\n",n); exit(9); }
        if(!(m&2)) lA[n]++;
        if(!(m&4)) lB[n]++;
    } else { lA[0]++; lB[0]++; }
    if(n==NMAX) return;
    unsigned char c[24];
    for(int p=0;p<=n;p++){
        for(int i=0;i<p;i++)c[i]=a[i];
        c[p]=(unsigned char)(n+1);
        for(int i=p;i<n;i++)c[i+1]=a[i];
        int m=scan(c,n+1);
        if(m&1) continue;
        if((m&2)&&(m&4)) continue;
        dfs(c,n+1,lA,lB);
    }
}
typedef struct { unsigned char a[24]; unsigned char n; } Node;
static Node *frontier=NULL; static long frn=0,frc=0;
static void gen(unsigned char*a,int n,int K0){
    if(n==K0){
        if(frn==frc){ frc=frc?frc*2:1024; frontier=realloc(frontier,frc*sizeof(Node)); }
        memcpy(frontier[frn].a,a,n); frontier[frn].n=n; frn++;
        return;
    }
    unsigned char c[24];
    for(int p=0;p<=n;p++){
        for(int i=0;i<p;i++)c[i]=a[i];
        c[p]=(unsigned char)(n+1);
        for(int i=p;i<n;i++)c[i+1]=a[i];
        int m=scan(c,n+1);
        if(m&1) continue;
        if((m&2)&&(m&4)) continue;
        gen(c,n+1,K0);
    }
}
int main(int argc,char**argv){
    NMAX=argc>1?atoi(argv[1]):12;
    int K0=argc>2?atoi(argv[2]):7;
    unsigned char root[24];
    gen(root,0,K0);
    fprintf(stderr,"frontier=%ld K0=%d\n",frn,K0);
    long long totA[24]={0},totB[24]={0};
    /* prefix counts n<=K0 single-threaded */
    {
        long long tA[24]={0},tB[24]={0};
        int save=NMAX; NMAX=K0;
        dfs(root,0,tA,tB);
        NMAX=save;
        for(int n=0;n<=K0;n++){ totA[n]=tA[n]; totB[n]=tB[n]; }
    }
#pragma omp parallel
    {
        long long lA[24]={0},lB[24]={0};
#pragma omp for schedule(dynamic,64)
        for(long i=0;i<frn;i++){
            unsigned char c[24]; int n=frontier[i].n;
            memcpy(c,frontier[i].a,n);
            unsigned char d[24];
            for(int p=0;p<=n;p++){
                for(int ii=0;ii<p;ii++)d[ii]=c[ii];
                d[p]=(unsigned char)(n+1);
                for(int ii=p;ii<n;ii++)d[ii+1]=c[ii];
                int m=scan(d,n+1);
                if(m&1) continue;
                if((m&2)&&(m&4)) continue;
                if(n+1<=NMAX) dfs(d,n+1,lA,lB);
            }
        }
#pragma omp critical
        for(int nn=K0+1;nn<=NMAX;nn++){ totA[nn]+=lA[nn]; totB[nn]+=lB[nn]; }
    }
    printf("n,Av4231_3124,Av4231_3214\n");
    for(int n=0;n<=NMAX;n++) printf("%d,%lld,%lld\n",n,totA[n],totB[n]);
    return 0;
}
