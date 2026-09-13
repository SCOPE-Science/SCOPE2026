/* perfix.c: for ONE canonical FIX assignment, joint MIX+P3 exact cover.
   Columns: M1 residual (27-9=18 uncovered M1 cells) + P2 (72) = 90 cols.
   Rows: MIX orbits avoiding FIX-covered M1 cells (cover 2 M1 + 1 P2) + P3 (3 P2).
   Usage: ./perfix <tlim> <maxstore> <pattern>  where pattern e.g. 7,1,1 ordering canonical:
     pairs 0..8 in order, first k0 -> f0, next k1 -> f1, rest -> f2, with (k0,k1,k2) a permutation of odd triple.
   We pass explicit assignment string of 9 digits, e.g. 000000012.
   Also applies within-block pair-symmetry lex-leader-lite: none (rely on parallelism).
   Prints solutions as orbit rep triples. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
static int sig(int x){ return x<18 ? (x^1) : x; }
#define MAXC 128
#define MAXN 3000
#define MAXD 80
typedef struct { int L[MAXN],R[MAXN],U[MAXN],D[MAXN],Cx[MAXN],Rx[MAXN],S[MAXC+1],nnode,ncol; } DLX;
static void dinit(DLX*d,int ncol){ d->ncol=ncol; for(int i=0;i<=ncol;i++){d->L[i]=i-1;d->R[i]=i+1;d->U[i]=d->D[i]=i;d->S[i]=0;} d->L[0]=ncol; d->R[ncol]=0; d->nnode=ncol+1; }
static void drow(DLX*d,int r,int*cols,int n){ int first=-1; for(int k=0;k<n;k++){ int col=cols[k]+1,nd=d->nnode++; if(nd>=MAXN){printf("NODE OVERFLOW\n");exit(1);} d->Cx[nd]=col; d->Rx[nd]=r; d->U[nd]=d->U[col]; d->D[nd]=col; d->D[d->U[col]]=nd; d->U[col]=nd; d->S[col]++; if(first==-1){first=nd; d->L[nd]=d->R[nd]=nd;} else { d->L[nd]=d->L[first]; d->R[nd]=first; d->R[d->L[first]]=nd; d->L[first]=nd; } } }
static void cvr(DLX*d,int c){ d->L[d->R[c]]=d->L[c]; d->R[d->L[c]]=d->R[c]; for(int i=d->D[c];i!=c;i=d->D[i]) for(int j=d->R[i];j!=i;j=d->R[j]){ d->U[d->D[j]]=d->U[j]; d->D[d->U[j]]=d->U[j]; d->S[d->Cx[j]]--; } }
static void ucv(DLX*d,int c){ for(int i=d->U[c];i!=c;i=d->U[i]) for(int j=d->L[i];j!=i;j=d->L[j]){ d->S[d->Cx[j]]++; d->U[d->D[j]]=j; d->D[d->U[j]]=j; } d->L[d->R[c]]=c; d->R[d->L[c]]=c; }

static DLX d;
static int cur[MAXD];
static int stored[8][MAXD]; static int sn;
static long long nodes; static int nsol, maxstore;
static time_t t0; static long tlim; static int timedout;
static char rdesc[800][64];

static void dfs(int k){
    if(timedout) return;
    nodes++;
    if((nodes&0xFFFFFF)==0){ printf("nodes=%lld depth=%d t=%lds\n",nodes,k,(long)(time(0)-t0)); fflush(stdout); if(time(0)-t0>tlim){timedout=1;return;} }
    if(d.R[0]==0){
        if(nsol<8){ memcpy(stored[nsol],cur,k*sizeof(int)); }
        nsol++;
        printf("SOLUTION %d depth %d\n",nsol,k); fflush(stdout);
        return;
    }
    int c=d.R[0],mn=d.S[c];
    for(int j=d.R[c];j!=0;j=d.R[j]) if(d.S[j]<mn){mn=d.S[j];c=j;if(mn<2)break;}
    if(mn==0) return;
    cvr(&d,c);
    for(int r=d.D[c];r!=c;r=d.D[r]){
        cur[k]=d.Rx[r];
        for(int j=d.R[r];j!=r;j=d.R[j]) cvr(&d,d.Cx[j]);
        dfs(k+1);
        if(timedout) break;
        for(int j=d.L[r];j!=r;j=d.L[j]) ucv(&d,d.Cx[j]);
        if(nsol>=maxstore) break;
    }
    ucv(&d,c);
}

int main(int argc,char**argv){
    tlim=argc>1?atol(argv[1]):120;
    maxstore=argc>2?atoi(argv[2]):2;
    const char* asg=argc>3?argv[3]:"000000012";
    int Fof[9]; for(int i=0;i<9;i++) Fof[i]=asg[i]-'0';
    printf("FIX assignment: %s\n",asg); fflush(stdout);
    int P2id[21][21]; for(int i=0;i<21;i++)for(int j=0;j<21;j++)P2id[i][j]=-1;
    int nP2=0;
    for(int a=0;a<18;a++)for(int b=a+1;b<18;b++){
        if(sig(a)==b) continue;
        int e=sig(a)<sig(b)?sig(a):sig(b),f=sig(a)<sig(b)?sig(b):sig(a);
        int ra=a,rb=b; if(e<a||(e==a&&f<b)){ra=e;rb=f;}
        if(P2id[ra][rb]==-1)P2id[ra][rb]=nP2++;
        P2id[a][b]=P2id[b][a]=P2id[ra][rb];
    }
    printf("nP2=%d\n",nP2);
    // columns: 0..71 P2 cells; 72.. M1 residual cells (only uncovered (f,i))
    int fixcell[3][9]; memset(fixcell,0,sizeof(fixcell));
    for(int i=0;i<9;i++) fixcell[Fof[i]][i]=1;
    int m1col[3][9]; for(int f=0;f<3;f++)for(int i=0;i<9;i++)m1col[f][i]=-1;
    int ncol=72;
    for(int f=0;f<3;f++)for(int i=0;i<9;i++) if(!fixcell[f][i]) m1col[f][i]=ncol++;
    printf("ncol=%d (expect 90)\n",ncol);
    dinit(&d,ncol);
    int nr=0;
    // MIX rows: rep {F,x in i,y in j}, canonical-min, with (f,i),(f,j) both uncovered
    for(int f=0;f<3;f++){int F=18+f;
        for(int i=0;i<9;i++)for(int j=i+1;j<9;j++){
            if(fixcell[f][i]||fixcell[f][j]) continue;
            for(int x=2*i;x<=2*i+1;x++)for(int y=2*j;y<=2*j+1;y++){
                int t[3]={F,x,y};
                for(int p=0;p<3;p++)for(int q=p+1;q<3;q++)if(t[p]>t[q]){int z=t[p];t[p]=t[q];t[q]=z;}
                int s[3]={sig(F),sig(x),sig(y)};
                for(int p=0;p<3;p++)for(int q=p+1;q<3;q++)if(s[p]>s[q]){int z=s[p];s[p]=s[q];s[q]=z;}
                int cmp=0;for(int p=0;p<3;p++){if(t[p]<s[p]){cmp=-1;break;}if(t[p]>s[p]){cmp=1;break;}}
                if(cmp>0)continue;
                if(cmp==0){printf("weird\n");return 1;}
                int cc[3]={P2id[x][y],m1col[f][i],m1col[f][j]};
                drow(&d,nr,cc,3);
                snprintf(rdesc[nr],64,"MIX (%d,%d,%d)",t[0],t[1],t[2]); nr++;
            }
        }
    }
    int nmixrows=nr;
    // P3 rows
    for(int a=0;a<18;a++)for(int b=a+1;b<18;b++)for(int c=b+1;c<18;c++){
        if(sig(a)==b)continue; if(sig(a)==c)continue; if(sig(b)==c)continue;
        int s[3]={sig(a),sig(b),sig(c)};
        for(int p=0;p<3;p++)for(int q=p+1;q<3;q++)if(s[p]>s[q]){int z=s[p];s[p]=s[q];s[q]=z;}
        int cmp=0;int t[3]={a,b,c};for(int p=0;p<3;p++){if(t[p]<s[p]){cmp=-1;break;}if(t[p]>s[p]){cmp=1;break;}}
        if(cmp>0)continue;
        if(cmp==0){printf("bad p3\n");return 1;}
        int c1=P2id[a][b],c2=P2id[a][c],c3=P2id[b][c];
        if(c1==c2||c1==c3||c2==c3){printf("deg\n");return 1;}
        int cc[3]={c1,c2,c3};
        drow(&d,nr,cc,3);
        snprintf(rdesc[nr],64,"P3 (%d,%d,%d)",a,b,c); nr++;
    }
    printf("nrows=%d (mix %d + p3 %d)\n",nr,nmixrows,nr-nmixrows); fflush(stdout);
    t0=time(0); nodes=0; nsol=0; timedout=0;
    dfs(0);
    printf("done nsol=%d nodes=%lld t=%lds timeout=%d\n",nsol,nodes,(long)(time(0)-t0),timedout);
    if(nsol>0){
        printf("FIRST solution rows:\n");
        // depth = 9 mix + 21 p3 = 30
        // recover from stored[0]? need depth; recompute: print count
        for(int k=0;k<30;k++){ int r=stored[0][k]; if(r>=0&&r<nr) printf("  %s\n",rdesc[r]); else printf("  row%d\n",r); }
    }
    fflush(stdout);
    return 0;
}
