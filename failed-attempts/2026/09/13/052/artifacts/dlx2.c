/* Clean DLX (Knuth) exact cover for sigma-invariant STS(21).
 * Cols 0..NCOL-1 (header 1..NCOL), root 0. Depth-guarded, records solutions. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define NCOL 108
#define NROW 600
#define NNODE 3000
#define MAXSOL 16
#define MAXDEPTH 120

static int L[NNODE], R[NNODE], U[NNODE], D[NNODE], Cx[NNODE], Rx[NNODE];
static int S[NCOL+1];
static int nnode;
static long long nodes;
static int nsol;
static int sol_rows[MAXSOL][MAXDEPTH];
static int sol_depth[MAXSOL];
static int cur[MAXDEPTH];
static time_t t_start; static long tlim; static int timedout;

static void cover(int c){
    L[R[c]]=L[c]; R[L[c]]=R[c];
    for(int i=D[c]; i!=c; i=D[i])
        for(int j=R[i]; j!=i; j=R[j]){
            U[D[j]]=U[j]; D[U[j]]=D[j]; S[Cx[j]]--;
        }
}
static void uncover(int c){
    for(int i=U[c]; i!=c; i=U[i])
        for(int j=L[i]; j!=i; j=L[j]){
            S[Cx[j]]++; U[D[j]]=j; D[U[j]]=j;
        }
    L[R[c]]=c; R[L[c]]=c;
}

static void dfs(int k){
    if(timedout) return;
    if(k>=MAXDEPTH){ printf("DEPTH OVERFLOW\n"); timedout=1; return; }
    nodes++;
    if((nodes&0xFFFFFF)==0){
        printf("nodes=%lld depth=%d t=%lds\n",nodes,k,(long)(time(0)-t_start)); fflush(stdout);
        if(time(0)-t_start>tlim){ timedout=1; return; }
    }
    if(R[0]==0){
        if(nsol<MAXSOL){
            memcpy(sol_rows[nsol],cur,k*sizeof(int));
            sol_depth[nsol]=k;
        }
        nsol++;
        printf("SOLUTION %d depth %d\n",nsol,k); fflush(stdout);
        return;
    }
    int c=R[0], mn=S[c];
    for(int j=R[c]; j!=0; j=R[j]) if(S[j]<mn){mn=S[j]; c=j; if(mn<2)break;}
    if(mn==0) return;
    cover(c);
    for(int r=D[c]; r!=c; r=D[r]){
        cur[k]=Rx[r];
        for(int j=R[r]; j!=r; j=R[j]) cover(Cx[j]);
        dfs(k+1);
        if(timedout) break;
        for(int j=L[r]; j!=r; j=L[j]) uncover(Cx[j]);
        if(nsol>=MAXSOL) break;
    }
    uncover(c);
}

int main(int argc,char**argv){
    tlim = argc>1? atol(argv[1]) : 60;
    int want = argc>2? atoi(argv[2]) : 1;
    if(want>MAXSOL) want=MAXSOL;
    int sig[21]; for(int x=0;x<21;x++) sig[x]=(x<18)?(x^1):x;
    static int colof[21][21]; for(int i=0;i<21;i++)for(int j=0;j<21;j++)colof[i][j]=-1;
    int ncol=0;
    for(int a=0;a<21;a++)for(int b=a+1;b<21;b++){
        int sa=sig[a],sb=sig[b];
        if(((sa==a&&sb==b)||(sa==b&&sb==a))) continue;
        int e=sig[a]<sig[b]?sig[a]:sig[b], f=sig[a]<sig[b]?sig[b]:sig[a];
        int ra=a,rb=b;
        if(e<a||(e==a&&f<b)){ra=e;rb=f;}
        if(colof[ra][rb]==-1) colof[ra][rb]=ncol++;
        colof[a][b]=colof[b][a]=colof[ra][rb];
    }
    int usecol[9]; for(int i=0;i<9;i++) usecol[i]=ncol++;
    printf("ncol=%d\n",ncol); fflush(stdout);
    if(ncol!=NCOL){printf("NCOL MISMATCH\n");return 1;}
    static int rows[600][4]; static int rncols[600];
    static char rdesc[600][64];
    int nr=0;
    for(int i=0;i<9;i++){int a=2*i,b=2*i+1;
        for(int q=0;q<3;q++){int ff=18+q;
            int u=ff<a?ff:a, v=ff<a?a:ff;
            rows[nr][0]=colof[u][v]; rows[nr][1]=usecol[i]; rncols[nr]=2;
            snprintf(rdesc[nr],64,"FIX f=%d i=%d",ff,i); nr++;
        }
    }
    for(int a=0;a<21;a++)for(int b=a+1;b<21;b++)for(int c=b+1;c<21;c++){
        int sa=sig[a],sb=sig[b],sc=sig[c];
        if(((sa==a&&sb==b)||(sa==b&&sb==a))) continue;
        if(((sa==a&&sc==c)||(sa==c&&sc==a))) continue;
        if(((sb==b&&sc==c)||(sb==c&&sc==b))) continue;
        int s[3]={sa,sb,sc};
        for(int i=0;i<3;i++)for(int j=i+1;j<3;j++)if(s[i]>s[j]){int z=s[i];s[i]=s[j];s[j]=z;}
        int cmp=0; for(int i=0;i<3;i++){int t=(i==0?a:(i==1?b:c)); if(t<s[i]){cmp=-1;break;} if(t>s[i]){cmp=1;break;}}
        if(cmp>0) continue;
        if(cmp==0){printf("unexpected fixed triple\n");return 1;}
        int c1=colof[a][b],c2=colof[a][c],c3=colof[b][c];
        if(c1==c2||c1==c3||c2==c3){printf("degenerate\n");return 1;}
        rows[nr][0]=c1;rows[nr][1]=c2;rows[nr][2]=c3;rncols[nr]=3;
        snprintf(rdesc[nr],64,"ORB (%d,%d,%d)",a,b,c); nr++;
    }
    printf("nrows=%d\n",nr); fflush(stdout);
    for(int i=0;i<=NCOL;i++){L[i]=i-1;R[i]=i+1;U[i]=D[i]=i;S[i]=0;}
    L[0]=NCOL; R[NCOL]=0;
    nnode=NCOL+1;
    for(int r=0;r<nr;r++){
        int first=-1;
        for(int k=0;k<rncols[r];k++){
            int col=rows[r][k]+1;
            int nd=nnode++;
            Cx[nd]=col; Rx[nd]=r;
            U[nd]=U[col]; D[nd]=col; D[U[col]]=nd; U[col]=nd; S[col]++;
            if(first==-1){first=nd; L[nd]=R[nd]=nd;}
            else { L[nd]=L[first]; R[nd]=first; R[L[first]]=nd; L[first]=nd; }
        }
    }
    printf("built nodes=%d\n",nnode); fflush(stdout);
    t_start=time(0); nodes=0; nsol=0; timedout=0;
    // maxsol enforcement: use global limit
    dfs(0);
    printf("done nsol=%d nodes=%lld t=%lds timeout=%d\n",nsol,nodes,(long)(time(0)-t_start),timedout);
    // print first solution rows
    if(nsol>0){
        printf("FIRST solution depth=%d rows:\n",sol_depth[0]);
        for(int k=0;k<sol_depth[0];k++){int r=sol_rows[0][k]; printf("  %s\n",rdesc[r]);}
    }
    fflush(stdout);
    return 0;
}
