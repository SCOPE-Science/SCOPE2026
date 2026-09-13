/* dlx3: sigma-invariant STS(21) exact cover with symmetry breaking:
 * fix pair-0's fixed block to f=18 (uses S_9 x S_3 symmetry),
 * fix pair-1's fixed block to f in {18,19} (uses residual S_2 on fixed pts),
 * order pair-0's mixed-orbit usage to break pair permutations.
 * Also dumps graph stats. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define NCOL 108
#define NROW 600
#define NNODE 3000
#define MAXDEPTH 120
#define MAXSTORE 4

static int L[NNODE], R[NNODE], U[NNODE], D[NNODE], Cx[NNODE], Rx[NNODE];
static int S[NCOL+1];
static int nnode;
static long long nodes;
static int nsol;
static int cur[MAXDEPTH];
static int stored[MAXSTORE][MAXDEPTH];
static int storedepth[MAXSTORE];
static time_t t_start; static long tlim; static int timedout;

static void cover(int c){
    L[R[c]]=L[c]; R[L[c]]=R[c];
    for(int i=D[c]; i!=c; i=D[i])
        for(int j=R[i]; j!=i; j=R[j]){ U[D[j]]=U[j]; D[U[j]]=D[j]; S[Cx[j]]--; }
}
static void uncover(int c){
    for(int i=U[c]; i!=c; i=U[i])
        for(int j=L[i]; j!=i; j=L[j]){ S[Cx[j]]++; U[D[j]]=j; D[U[j]]=j; }
    L[R[c]]=c; R[L[c]]=c;
}
static void dfs(int k){
    if(timedout) return;
    if(k>=MAXDEPTH){ timedout=1; return; }
    nodes++;
    if((nodes&0xFFFFFF)==0){
        printf("nodes=%lld depth=%d t=%lds\n",nodes,k,(long)(time(0)-t_start)); fflush(stdout);
        if(time(0)-t_start>tlim){ timedout=1; return; }
    }
    if(R[0]==0){
        if(nsol<MAXSTORE){ memcpy(stored[nsol],cur,k*sizeof(int)); storedepth[nsol]=k; }
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
        if(nsol>=MAXSTORE) break;
    }
    uncover(c);
}

/* force-cover a row: cover all its columns' other rows then record */
static int force_row(int rowid, int *rownode_of_row, int nrows_use){
    (void)nrows_use;
    int nd = rownode_of_row[rowid];
    // cover each column of the row, like choosing it
    // standard: cover primary col first... here just cover all cols of row
    // To emulate selection: cover(Cx[nd]) then for j in row cover rest, record.
    int cols[4]; int nc=0;
    cols[nc++]=Cx[nd];
    for(int j=R[nd]; j!=nd; j=R[j]) cols[nc++]=Cx[j];
    for(int t=0;t<nc;t++) cover(cols[t]);
    return nc;
}

int main(int argc,char**argv){
    tlim = argc>1? atol(argv[1]) : 60;
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
    if(ncol!=NCOL){printf("NCOL MISMATCH %d\n",ncol);return 1;}
    static int rows[600][4]; static int rncols[600];
    static char rdesc[600][64];
    int nr=0;
    int fixrow[9][3]; // [pair][q] -> row id
    for(int i=0;i<9;i++){int a=2*i,b=2*i+1;
        for(int q=0;q<3;q++){int ff=18+q;
            int u=ff<a?ff:a, v=ff<a?a:ff;
            rows[nr][0]=colof[u][v]; rows[nr][1]=usecol[i]; rncols[nr]=2;
            snprintf(rdesc[nr],64,"FIX f=%d i=%d",ff,i);
            fixrow[i][q]=nr; nr++;
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
        if(cmp==0){printf("unexpected fixed\n");return 1;}
        int c1=colof[a][b],c2=colof[a][c],c3=colof[b][c];
        if(c1==c2||c1==c3||c2==c3){printf("degenerate\n");return 1;}
        rows[nr][0]=c1;rows[nr][1]=c2;rows[nr][2]=c3;rncols[nr]=3;
        snprintf(rdesc[nr],64,"ORB (%d,%d,%d)",a,b,c); nr++;
    }
    printf("nrows=%d\n",nr); fflush(stdout);
    for(int i=0;i<=NCOL;i++){L[i]=i-1;R[i]=i+1;U[i]=D[i]=i;S[i]=0;}
    L[0]=NCOL; R[NCOL]=0;
    nnode=NCOL+1;
    static int rownode[600];
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
        rownode[r]=first;
    }
    printf("built nodes=%d\n",nnode); fflush(stdout);

    const char *mode = argc>3? argv[3] : "A";
    // symmetry breaking: force pair0 -> f=18 row; pair1 -> restrict to q in {0,1}? mode B also pre-picks pair1=18.
    // Implement by REMOVING competing rows (unlink them) before search.
    // Mode A: remove fixrow[0][1],fixrow[0][2] (pair0 must be f=18). Keep all else.
    // Mode B: additionally remove fixrow[1][2] (pair1 in {18,19}).
    // Removal: for each row to kill, unlink its nodes from column lists (cover-less delete).
    int kill[600]; int nkill=0;
    kill[nkill++]=fixrow[0][1]; kill[nkill++]=fixrow[0][2];
    if(strcmp(mode,"B")==0){ kill[nkill++]=fixrow[1][2]; }
    if(strcmp(mode,"C")==0){ kill[nkill++]=fixrow[1][2]; /* + pair2 in {18,19,20} full: no-op */ }
    for(int t=0;t<nkill;t++){
        int r=kill[t];
        int nd=rownode[r];
        if(nd<0) continue;
        // unlink all nodes of row r
        int j=nd;
        do { U[D[j]]=U[j]; D[U[j]]=D[j]; S[Cx[j]]--; j=R[j]; } while(j!=nd);
        printf("killed row %d (%s)\n",r,rdesc[r]);
    }
    fflush(stdout);
    t_start=time(0); nodes=0; nsol=0; timedout=0;
    dfs(0);
    printf("done nsol=%d nodes=%lld t=%lds timeout=%d\n",nsol,nodes,(long)(time(0)-t_start),timedout);
    if(nsol>0){
        printf("FIRST solution depth=%d rows:\n",storedepth[0]);
        for(int k=0;k<storedepth[0];k++){int r=stored[0][k]; printf("  %s\n",rdesc[r]);}
    }
    fflush(stdout);
    return 0;
}
