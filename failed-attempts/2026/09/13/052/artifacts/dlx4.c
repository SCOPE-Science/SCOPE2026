/* dlx4: two-stage decomposition.
   Stage 1: enumerate (FIX + MIXED) subsystem covers of M1+U cols (36 cols):
     FIX rows 27 (cover 1 M1 + 1 U), MIX orbits 216 (cover 2 M1 same-fix-row).
   For each stage-1 solution, stage 2: exact cover of residual P2 demand with P3 orbits.
   P2 columns: 72 pair-orbit cols of moved-moved pairs. Each MIX orbit covers one P2 cell
   (the (i,j,flavor)); P3 orbits cover 3.
   Print progress; record first full solutions with block lists. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

static int sig(int x){ return x<18 ? (x^1) : x; }

/* ---------- generic tiny DLX ---------- */
#define MAXC 80
#define MAXR 400
#define MAXN 2000
#define MAXD 60
typedef struct { int L[MAXN],R[MAXN],U[MAXN],D[MAXN],Cx[MAXN],Rx[MAXN],S[MAXC+1],nnode,ncol;
                 int cur[MAXD]; } DLX;
static void dlx_init(DLX*d,int ncol){
    d->ncol=ncol;
    for(int i=0;i<=ncol;i++){d->L[i]=i-1;d->R[i]=i+1;d->U[i]=d->D[i]=i;d->S[i]=0;}
    d->L[0]=ncol; d->R[ncol]=0; d->nnode=ncol+1;
}
static void dlx_row(DLX*d,int r,int*cols,int n){
    int first=-1;
    for(int k=0;k<n;k++){ int col=cols[k]+1, nd=d->nnode++;
        d->Cx[nd]=col; d->Rx[nd]=r;
        d->U[nd]=d->U[col]; d->D[nd]=col; d->D[d->U[col]]=nd; d->U[col]=nd; d->S[col]++;
        if(first==-1){first=nd; d->L[nd]=d->R[nd]=nd;}
        else { d->L[nd]=d->L[first]; d->R[nd]=first; d->R[d->L[first]]=nd; d->L[first]=nd; }
    }
}
static void cover(DLX*d,int c){
    d->L[d->R[c]]=d->L[c]; d->R[d->L[c]]=d->R[c];
    for(int i=d->D[c];i!=c;i=d->D[i]) for(int j=d->R[i];j!=i;j=d->R[j]){ d->U[d->D[j]]=d->U[j]; d->D[d->U[j]]=d->U[j]; d->S[d->Cx[j]]--; }
}
static void uncover(DLX*d,int c){
    for(int i=d->U[c];i!=c;i=d->U[i]) for(int j=d->L[i];j!=i;j=d->L[j]){ d->S[d->Cx[j]]++; d->U[d->D[j]]=j; d->D[d->U[j]]=j; }
    d->L[d->R[c]]=c; d->R[d->L[c]]=c;
}

/* ---------- problem data ---------- */
static int colof[21][21];
static int P2id[21][21];   // canonical moved-moved pair-orbit -> 0..71
static int M1id[3][9];     // (f,i) -> 0..26
static int Uid[9];         // 27..35
static int nP2;

static int mixrep[300][3]; static int nmix;       // representative triples
static int mix_p2[300];                           // P2 cell covered
static int p3rep[400][3]; static int np3;
static int p3_p2[400][3];

static int p2key(int a,int b){ // canonical moved-moved pair orbit id (a,b moved pts, a!=b, not vertical pair)
    int sa=sig(a),sb=sig(b);
    int e=sa<sb?sa:sb, f=sa<sb?sb:sa;
    int ra=a,rb=b; if(a>b){ra=b;rb=a;}
    // canonical = min of sorted (a,b) and sorted image
    int ia=ra,ib=rb;
    if(e<ia||(e==ia&&f<ib)){ra=e;rb=f;}
    return P2id[ra][rb];
}

int main(int argc,char**argv){
    long tlim = argc>1?atol(argv[1]):120;
    time_t t0=time(0);
    for(int i=0;i<21;i++)for(int j=0;j<21;j++){colof[i][j]=-1;P2id[i][j]=-1;}
    // M1 ids
    for(int f=0;f<3;f++)for(int i=0;i<9;i++)M1id[f][i]=f*9+i;
    for(int i=0;i<9;i++)Uid[i]=27+i;
    // P2 ids: canonical moved-moved pair orbits
    nP2=0;
    for(int a=0;a<18;a++)for(int b=a+1;b<18;b++){
        int sa=sig(a),sb=sig(b);
        if((sa==b&&sb==a)) continue; // vertical pair
        int e=sa<sb?sa:sb,f=sa<sb?sb:sa;
        int ra=a,rb=b;
        if(e<a||(e==a&&f<b)){ra=e;rb=f;}
        if(P2id[ra][rb]==-1)P2id[ra][rb]=nP2++;
        P2id[a][b]=P2id[b][a]=P2id[ra][rb];
    }
    printf("nP2=%d (expect 72)\n",nP2);
    // mixed reps
    nmix=0;
    for(int f=0;f<3;f++){int F=18+f;
        for(int i=0;i<9;i++)for(int j=i+1;j<9;j++)
            for(int x=2*i;x<=2*i+1;x++)for(int y=2*j;y<=2*j+1;y++){
                int t[3]={F,x,y}; // sort
                for(int p=0;p<3;p++)for(int q=p+1;q<3;q++)if(t[p]>t[q]){int z=t[p];t[p]=t[q];t[q]=z;}
                int s[3]={sig(F),sig(x),sig(y)};
                for(int p=0;p<3;p++)for(int q=p+1;q<3;q++)if(s[p]>s[q]){int z=s[p];s[p]=s[q];s[q]=z;}
                int cmp=0;for(int p=0;p<3;p++){if(t[p]<s[p]){cmp=-1;break;}if(t[p]>s[p]){cmp=1;break;}}
                if(cmp>0)continue;
                mixrep[nmix][0]=t[0];mixrep[nmix][1]=t[1];mixrep[nmix][2]=t[2];
                // P2 cell: pair (x,y)
                mix_p2[nmix]=P2id[x][y];
                nmix++;
            }
    }
    printf("nmix=%d (expect 216)\n",nmix);
    // P3 reps
    np3=0;
    for(int a=0;a<18;a++)for(int b=a+1;b<18;b++)for(int c=b+1;c<18;c++){
        int sa=sig(a),sb=sig(b),sc=sig(c);
        if(sa==b&&sb==a)continue; if(sa==c&&sc==a)continue; if(sb==c&&sc==b)continue;
        int s[3]={sa,sb,sc};
        for(int p=0;p<3;p++)for(int q=p+1;q<3;q++)if(s[p]>s[q]){int z=s[p];s[p]=s[q];s[q]=z;}
        int cmp=0;int t[3]={a,b,c};for(int p=0;p<3;p++){if(t[p]<s[p]){cmp=-1;break;}if(t[p]>s[p]){cmp=1;break;}}
        if(cmp>0)continue;
        if(cmp==0){printf("fixed p3?\n");return 1;}
        // check pairs distinct orbits
        int c1=P2id[a][b],c2=P2id[a][c],c3=P2id[b][c];
        if(c1==c2||c1==c3||c2==c3){printf("degenerate p3 %d %d %d\n",a,b,c);return 1;}
        p3rep[np3][0]=a;p3rep[np3][1]=b;p3rep[np3][2]=c;
        p3_p2[np3][0]=c1;p3_p2[np3][1]=c2;p3_p2[np3][2]=c3;
        np3++;
    }
    printf("np3=%d\n",np3);
    fflush(stdout);

    /* Stage 1 DLX: 36 cols; rows: FIX 27 (id 0..26), MIX 216 (id 27..242) */
    static DLX d1;
    dlx_init(&d1,36);
    // FIX rows: f,i -> cols M1id,Uid
    for(int f=0;f<3;f++)for(int i=0;i<9;i++){int cc[2]={M1id[f][i],Uid[i]}; dlx_row(&d1,f*9+i,cc,2);}
    for(int m=0;m<nmix;m++){
        int F=mixrep[m][0]; // sorted so F is max (18..20)? F>=18 yes since moved<18
        int f=F-18, x=mixrep[m][1], y=mixrep[m][2];
        int cc[2]={M1id[f][x/2],M1id[f][y/2]};
        dlx_row(&d1,27+m,cc,2);
    }
    printf("stage1 built nodes=%d\n",d1.nnode); fflush(stdout);
    // enumerate stage-1 solutions iteratively via explicit DLX search with callback:
    // We'll do manual recursive search with solution processing (stage-2 check).
    // Implement recursion here (needs access to locals) — write as nested via statics.
    extern void run_search(void);
    // Instead: implement inline stack-based search
    long long n1=0; int depth=0;
    // path rows
    static int path[40];
    // recursive function via C function pointer with statics
    // Use explicit recursion:
    // (define as static function operating on d1 + globals)
    // To keep it simple, use iterative deepening with function:
    // We'll write search1(k) as a real function below using globals.
    printf("starting stage-1 enumeration...\n"); fflush(stdout);
    // hand off to function
    {
        // globals for search
        // Use file-static approach: store in static vars through a struct — simplest: recursion inline with goto-free C:
        // Implement recursive search as a separate function using global DLX pointer.
        extern int g_maxstage1; extern long long *g_n1; extern int *g_path; extern time_t g_t0; extern long g_tlim;
        // (declared below)
    }
    return 0;
}
