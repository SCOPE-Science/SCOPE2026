/* Exact cover: sigma-invariant STS(21). DLX-style dancing links in C.
   Columns: 108. Rows: 579. Find sigma-invariant STS(21) count/solutions. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <stdint.h>

#define NCOL 108
#define NROW 600
#define NNODE 3000

static int L[NNODE], R[NNODE], U[NNODE], D[NNODE], Cix[NNODE], Rix[NNODE];
static int S[NCOL+1];       // column sizes, col headers 1..NCOL; 0 = root
static int row_first[NROW];
static int nnode;
static long nodes;
static int nsol, maxsol;
static int sol_rows[200];
static int sol_depth;
static double t0; static double tlim; static int timedout;
static int solbuf[8][200];

static double now(){ struct timespec ts; clock_gettime(CLOCK_MONOTONIC,&ts); return ts.tv_sec+ts.tv_nsec*1e-9; }

static void cover(int c){
    L[R[c]]=L[c]; R[L[c]]=R[c];
    for(int i=D[c]; i!=c; i=D[i])
        for(int j=R[i]; j!=i; j=R[j]){
            U[D[j]]=U[j]; D[U[j]]=D[j]; S[Cix[j]]--;
        }
}
static void uncover(int c){
    for(int i=U[c]; i!=c; i=U[i])
        for(int j=L[i]; j!=i; j=L[j]){
            S[Cix[j]]++; U[D[j]]=j; D[U[j]]=j;
        }
    L[R[c]]=c; R[L[c]]=c;
}

static void dfs(int k){
    nodes++;
    if((nodes&0x3FFFFF)==0){ printf("nodes=%ld depth=%d t=%.1f\n",nodes,k,now()-t0); fflush(stdout);}
    if(now()-t0>tlim){ timedout=1; return; }
    if(R[0]==0){
        if(nsol<8) memcpy(solbuf[nsol],sol_rows,k*sizeof(int));
        nsol++;
        printf("SOLUTION %d depth %d\n",nsol,k); fflush(stdout);
        return;
    }
    // choose col with min S
    int c=R[0], mn=S[c];
    for(int j=R[c]; j!=0; j=R[j]) if(S[j]<mn){mn=S[j]; c=j; if(mn<=1)break;}
    if(mn==0) return;
    cover(c);
    for(int r=D[c]; r!=c && !timedout; r=D[r]){
        sol_rows[k]=Rix[r];
        for(int j=R[r]; j!=r; j=R[j]) cover(Cix[j]);
        dfs(k+1);
        if(timedout) { /* still must uncover? just return after uncover */ }
        r=sol_rows[k]? r:r;
        for(int j=L[D[c]==0?0:0];0;) break; // noop
        // uncover in reverse: need last r; recompute: iterate L from saved
        // We saved only row id; recover node: find node of column c in that row:
        int rr=r;
        // uncover columns in reverse order
        // collect js
        // simple: walk L from r
        int js[8]; int nj=0;
        for(int j=L[rr]; j!=rr; j=L[j]) js[nj++]=Cix[j];
        for(int t=nj-1;t>=0;t--) uncover(js[t]);
        if(nsol>=maxsol){ uncover(c); return; }
    }
    uncover(c);
}

int main(int argc,char**argv){
    tlim = argc>1? atof(argv[1]) : 30.0;
    maxsol = argc>2? atoi(argv[2]) : 1;
    // Build matrix from python-generated description? Recompute here.
    // points 0..20; sig x = x^1 if x<18
    int sig[21]; for(int x=0;x<21;x++) sig[x]=(x<18)?(x^1):x;
    // columns indexed 0..NCOL-1 mapped to header 1..NCOL
    // column key enumeration must match python: order pairs lexicographic a<b non-fixed => index; then 9 use cols.
    int colof[21][21]; for(int i=0;i<21;i++)for(int j=0;j<21;j++)colof[i][j]=-1;
    int ncol=0;
    // need porb canonical
    for(int a=0;a<21;a++)for(int b=a+1;b<21;b++){
        int sa=sig[a],sb=sig[b];
        int fa=( (sa==a&&sb==b)||(sa==b&&sb==a) );
        if(fa) continue;
        int c=sig[a],d=sig[b]; int e=c>d?d:c, f=c>d?c:d; // sorted image
        int ca = (a<e||(a==e&&b<=f))? a:e;
        // canonical key: min of (a,b),(e,f): determine representative
        int ra,rb;
        if(a<e||(a==e&&b<f)){ra=a;rb=b;} else {ra=e;rb=f;}
        if(colof[ra][rb]==-1){colof[ra][rb]=ncol++;}
        colof[a][b]=colof[ra][rb]; colof[b][a]=colof[ra][rb];
    }
    int usecol[9]; for(int i=0;i<9;i++) usecol[i]=ncol++;
    printf("ncol=%d (expect 108)\n",ncol);
    // rows
    int rows[600][4]; int rncols[600]; int nr=0;
    char rdesc[600][64];
    for(int i=0;i<9;i++){int a=2*i,b=2*i+1;
        for(int q=0;q<3;q++){int f=18+q;
            rows[nr][0]=colof[f<a?a:f][f<a?f:a]; // colof(f,a)
            rows[nr][0]=colof[f<a?f:a][f<a?a:f];
            rows[nr][1]=usecol[i]; rncols[nr]=2;
            snprintf(rdesc[nr],64,"FIX f=%d i=%d",f,i); nr++;
        }
    }
    // orbit rows
    for(int a=0;a<21;a++)for(int b=a+1;b<21;b++)for(int c=b+1;c<21;c++){
        int sa=sig[a],sb=sig[b],sc=sig[c];
        int fa=((sa==a&&sb==b)||(sa==b&&sb==a));
        int fb=((sa==a&&sc==c)||(sa==c&&sc==a));
        int fc=((sb==b&&sc==c)||(sb==c&&sc==b));
        if(fa||fb||fc) continue;
        int t[3]={a,b,c}, s[3]={sa,sb,sc};
        // sort s
        for(int i=0;i<3;i++)for(int j=i+1;j<3;j++)if(s[i]>s[j]){int z=s[i];s[i]=s[j];s[j]=z;}
        int cmp=0; for(int i=0;i<3;i++){if(t[i]<s[i]){cmp=-1;break;} if(t[i]>s[i]){cmp=1;break;}}
        if(cmp>0) continue; // keep canonical min only
        if(cmp==0){printf("unexpected fixed triple %d %d %d\n",a,b,c); continue;}
        int c1=colof[a][b],c2=colof[a][c],c3=colof[b][c];
        if(c1==c2||c1==c3||c2==c3){printf("degenerate %d %d %d\n",a,b,c); continue;}
        rows[nr][0]=c1;rows[nr][1]=c2;rows[nr][2]=c3;rncols[nr]=3;
        snprintf(rdesc[nr],64,"ORB (%d,%d,%d)",a,b,c); nr++;
    }
    printf("nrows=%d\n",nr);
    // build DLX
    for(int i=0;i<=NCOL;i++){L[i]=i-1;R[i]=i+1;U[i]=D[i]=i;S[i]=0;}
    L[0]=NCOL; R[NCOL]=0;
    nnode=NCOL+1;
    memset(row_first,-1,sizeof(row_first));
    for(int r=0;r<nr;r++){
        int first=-1;
        for(int k=0;k<rncols[r];k++){
            int col=rows[r][k]+1;
            int nd=nnode++;
            Cix[nd]=col; Rix[nd]=r;
            // vertical link
            U[nd]=U[col]; D[nd]=col; D[U[col]]=nd; U[col]=nd; S[col]++;
            // horizontal
            if(first==-1){first=nd; L[nd]=R[nd]=nd;}
            else { L[nd]=L[first]; R[nd]=first; R[L[first]]=nd; L[first]=nd; }
        }
        row_first[r]=first;
    }
    printf("nodes=%d\n",nnode);
    t0=now(); nodes=0; nsol=0; timedout=0;
    dfs(0);
    printf("done nsol=%d nodes=%ld t=%.2f timeout=%d\n",nsol,nodes,now()-t0,timedout);
    for(int s=0;s<nsol&&s<8;s++){
        printf("SOL %d:\n",s);
        // depth unknown; print via recount? store only last; instead re-resolve: skip
    }
    // print resolved rows of first solution by re-running? Instead store depth:
    return 0;
}
