/* staged.c: two-stage sigma-STS(21) search.
   Stage1: exact cover of M1(27)+U(9) by FIX(27)+MIX(216) rows.
   Stage2 (per stage-1 sol): exact cover of residual P2 (63 cells) by P3 rows (subset).
   Symmetry break: pair0 FIX -> f=18.
   Records full solutions; prints block lists. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

static int sig(int x){ return x<18 ? (x^1) : x; }
#define MAXC 80
#define MAXN 2500
#define MAXD 60
typedef struct { int L[MAXN],R[MAXN],U[MAXN],D[MAXN],Cx[MAXN],Rx[MAXN],S[MAXC+1],nnode,ncol; } DLX;
static void dinit(DLX*d,int ncol){ d->ncol=ncol; for(int i=0;i<=ncol;i++){d->L[i]=i-1;d->R[i]=i+1;d->U[i]=d->D[i]=i;d->S[i]=0;} d->L[0]=ncol; d->R[ncol]=0; d->nnode=ncol+1; }
static void drow(DLX*d,int r,int*cols,int n){ int first=-1; for(int k=0;k<n;k++){ int col=cols[k]+1,nd=d->nnode++; d->Cx[nd]=col; d->Rx[nd]=r; d->U[nd]=d->U[col]; d->D[nd]=col; d->D[d->U[col]]=nd; d->U[col]=nd; d->S[col]++; if(first==-1){first=nd; d->L[nd]=d->R[nd]=nd;} else { d->L[nd]=d->L[first]; d->R[nd]=first; d->R[d->L[first]]=nd; d->L[first]=nd; } } }
static void cvr(DLX*d,int c){ d->L[d->R[c]]=d->L[c]; d->R[d->L[c]]=d->R[c]; for(int i=d->D[c];i!=c;i=d->D[i]) for(int j=d->R[i];j!=i;j=d->R[j]){ d->U[d->D[j]]=d->U[j]; d->D[d->U[j]]=d->U[j]; d->S[d->Cx[j]]--; } }
static void ucv(DLX*d,int c){ for(int i=d->U[c];i!=c;i=d->U[i]) for(int j=d->L[i];j!=i;j=d->L[j]){ d->S[d->Cx[j]]++; d->U[d->D[j]]=j; d->D[d->U[j]]=j; } d->L[d->R[c]]=c; d->R[d->L[c]]=c; }

static int P2id[21][21]; static int nP2;
static int mixrep[300][3]; static int mix_p2[300]; static int mix_f[300], mix_i[300], mix_j[300]; static int nmix;
static int p3rep[400][3]; static int p3p2[400][3]; static int np3;
/* p2col_of: P2 cell -> stage2 column (only for uncovered cells) */
static int p2col[80];

static DLX d1;
static int path1[40];
static long long n1, n2nodes;
static int nfull;
static time_t t0; static long tlim; static int timedout; static int maxstore;
static int stored_full[8][64]; static int stored_n[8];
static int stage1_limit;

static long long s1nodes;

/* forward decl */
static int solve_stage2(int *mixrows, int nm, int *fixrows, int nf);

/* stage-2 DLX search (exact cover of residual P2 cells with compatible P3 rows) */
static DLX d2;
static int path2[40];
static int s2_mixrows[16]; static int s2_nm, s2_fix[16], s2_nf;
static int s2_target; // 21
static void dfs2(int k){
    if(timedout) return;
    n2nodes++;
    if((n2nodes&0xFFFFF)==0 && time(0)-t0>tlim){ timedout=1; return; }
    if(k==s2_target){
        if(d2.R[0]!=0) return; // must cover all
        if(nfull<8){
            int p=0;
            for(int t=0;t<s2_nf;t++) stored_full[nfull][p++]=s2_fix[t];       // FIX row ids (0..26)
            for(int t=0;t<s2_nm;t++) stored_full[nfull][p++]=1000+s2_mixrows[t]; // MIX idx
            for(int t=0;t<k;t++) stored_full[nfull][p++]=2000+path2[t];        // P3 idx
            stored_n[nfull]=p;
        }
        nfull++;
        printf("FULL SOLUTION %d (stage1 #%lld)\n",nfull,n1); fflush(stdout);
        return;
    }
    if(d2.R[0]==0) return;
    int c=d2.R[0],mn=d2.S[c];
    for(int j=d2.R[c];j!=0;j=d2.R[j]) if(d2.S[j]<mn){mn=d2.S[j];c=j;if(mn<2)break;}
    if(mn==0) return;
    cvr(&d2,c);
    for(int r=d2.D[c];r!=c;r=d2.D[r]){
        path2[k]=d2.Rx[r];
        for(int j=d2.R[r];j!=r;j=d2.R[j]) cvr(&d2,d2.Cx[j]);
        dfs2(k+1);
        if(timedout) break;
        for(int j=d2.L[r];j!=r;j=d2.L[j]) ucv(&d2,d2.Cx[j]);
        if(nfull>=maxstore) break;
    }
    ucv(&d2,c);
}

static int solve_stage2(int *mixrows, int nm, int *fixrows, int nf){
    int used[80]; memset(used,0,sizeof(used));
    for(int t=0;t<nm;t++) used[mix_p2[mixrows[t]]]=1;
    int ncol=0;
    for(int c=0;c<nP2;c++) p2col[c]=-1;
    for(int c=0;c<nP2;c++) if(!used[c]) p2col[c]=ncol++;
    if(ncol!=63){ printf("stage2 wrong residual %d\n",ncol); return 0; }
    dinit(&d2,ncol);
    for(int p=0;p<np3;p++){
        int a=p3p2[p][0],b=p3p2[p][1],c=p3p2[p][2];
        if(used[a]||used[b]||used[c]) continue;
        int cc[3]={p2col[a],p2col[b],p2col[c]};
        drow(&d2,p,cc,3);
    }
    for(int t=0;t<nm;t++){ s2_mixrows[t]=mixrows[t]; }
    s2_nm=nm;
    for(int t=0;t<nf;t++) s2_fix[t]=fixrows[t];
    s2_nf=nf; s2_target=21;
    dfs2(0);
    return 0;
}

static void dfs1(int k){
    if(timedout) return;
    s1nodes++;
    if((s1nodes&0xFFFFF)==0){ printf("s1 nodes=%lld stage1sols=%lld full=%d t=%lds\n",s1nodes,n1,nfull,(long)(time(0)-t0)); fflush(stdout); if(time(0)-t0>tlim){timedout=1;return;} }
    if(d1.R[0]==0){
        n1++;
        // decode: FIX rows (id<27) and MIX rows
        int mixrows[16],nm=0,fixrows[16],nf=0;
        for(int t=0;t<k;t++){ int r=path1[t]; if(r<27) fixrows[nf++]=r; else mixrows[nm++]=r-27; }
        if(n1<=5 || n1%20000==0){ printf(" stage1 sol %lld: nf=%d nm=%d t=%lds\n",n1,nf,nm,(long)(time(0)-t0)); fflush(stdout); }
        solve_stage2(mixrows,nm,fixrows,nf);
        if(nfull>=maxstore){ timedout=2; }
        return;
    }
    int c=d1.R[0],mn=d1.S[c];
    for(int j=d1.R[c];j!=0;j=d1.R[j]) if(d1.S[j]<mn){mn=d1.S[j];c=j;if(mn<2)break;}
    if(mn==0) return;
    cvr(&d1,c);
    for(int r=d1.D[c];r!=c;r=d1.D[r]){
        path1[k]=d1.Rx[r];
        for(int j=d1.R[r];j!=r;j=d1.R[j]) cvr(&d1,d1.Cx[j]);
        dfs1(k+1);
        if(timedout) break;
        for(int j=d1.L[r];j!=r;j=d1.L[j]) ucv(&d1,d1.Cx[j]);
        if(stage1_limit>0 && n1>=stage1_limit) break;
    }
    ucv(&d1,c);
}

int main(int argc,char**argv){
    tlim=argc>1?atol(argv[1]):300;
    maxstore=argc>2?atoi(argv[2]):4;
    stage1_limit=argc>3?atoi(argv[3]):0;
    const char* mode=argc>4?argv[4]:"A";
    for(int i=0;i<21;i++)for(int j=0;j<21;j++)P2id[i][j]=-1;
    nP2=0;
    for(int a=0;a<18;a++)for(int b=a+1;b<18;b++){
        if(sig(a)==b) continue;
        int e=sig(a)<sig(b)?sig(a):sig(b),f=sig(a)<sig(b)?sig(b):sig(a);
        int ra=a,rb=b; if(e<a||(e==a&&f<b)){ra=e;rb=f;}
        if(P2id[ra][rb]==-1)P2id[ra][rb]=nP2++;
        P2id[a][b]=P2id[b][a]=P2id[ra][rb];
    }
    printf("nP2=%d\n",nP2);
    nmix=0;
    for(int f=0;f<3;f++){int F=18+f;
        for(int i=0;i<9;i++)for(int j=i+1;j<9;j++)
            for(int x=2*i;x<=2*i+1;x++)for(int y=2*j;y<=2*j+1;y++){
                int t[3]={F,x,y};
                for(int p=0;p<3;p++)for(int q=p+1;q<3;q++)if(t[p]>t[q]){int z=t[p];t[p]=t[q];t[q]=z;}
                int s[3]={sig(F),sig(x),sig(y)};
                for(int p=0;p<3;p++)for(int q=p+1;q<3;q++)if(s[p]>s[q]){int z=s[p];s[p]=s[q];s[q]=z;}
                int cmp=0;for(int p=0;p<3;p++){if(t[p]<s[p]){cmp=-1;break;}if(t[p]>s[p]){cmp=1;break;}}
                if(cmp>0)continue;
                mixrep[nmix][0]=t[0];mixrep[nmix][1]=t[1];mixrep[nmix][2]=t[2];
                mix_f[nmix]=f;mix_i[nmix]=x/2;mix_j[nmix]=y/2;
                mix_p2[nmix]=P2id[x][y]; nmix++;
            }
    }
    printf("nmix=%d\n",nmix);
    np3=0;
    for(int a=0;a<18;a++)for(int b=a+1;b<18;b++)for(int c=b+1;c<18;c++){
        if(sig(a)==b)continue; if(sig(a)==c)continue; if(sig(b)==c)continue;
        int s[3]={sig(a),sig(b),sig(c)};
        for(int p=0;p<3;p++)for(int q=p+1;q<3;q++)if(s[p]>s[q]){int z=s[p];s[p]=s[q];s[q]=z;}
        int cmp=0;int t[3]={a,b,c};for(int p=0;p<3;p++){if(t[p]<s[p]){cmp=-1;break;}if(t[p]>s[p]){cmp=1;break;}}
        if(cmp>0)continue;
        if(cmp==0){printf("bad p3\n");return 1;}
        int c1=P2id[a][b],c2=P2id[a][c],c3=P2id[b][c];
        if(c1==c2||c1==c3||c2==c3){printf("deg p3\n");return 1;}
        p3rep[np3][0]=a;p3rep[np3][1]=b;p3rep[np3][2]=c;
        p3p2[np3][0]=c1;p3p2[np3][1]=c2;p3p2[np3][2]=c3; np3++;
    }
    printf("np3=%d\n",np3); fflush(stdout);
    dinit(&d1,36);
    for(int f=0;f<3;f++)for(int i=0;i<9;i++){int cc[2]={f*9+i,27+i}; drow(&d1,f*9+i,cc,2);}
    for(int m=0;m<nmix;m++){int cc[2]={mix_f[m]*9+mix_i[m],mix_f[m]*9+mix_j[m]}; drow(&d1,27+m,cc,2);}
    // symmetry break mode A: kill FIX rows pair0 f=19,20 (ids 1,2)
    if(mode[0]=='A'||mode[0]=='B'){
        for(int killid=1;killid<=2;killid++){
            // unlink row killid: find its nodes — easier: prevent by covering? Instead delete: iterate columns
            // find node: scan all nodes with Rx==killid and unlink vertically
            for(int nd=37;nd<d1.nnode;nd++) if(d1.Rx[nd]==killid){ d1.U[d1.D[nd]]=d1.U[nd]; d1.D[d1.U[nd]]=d1.D[nd]; d1.S[d1.Cx[nd]]--; d1.Rx[nd]=-999; }
            printf("killed FIX row %d\n",killid);
        }
    }
    fflush(stdout);
    t0=time(0); n1=0; nfull=0; timedout=0; s1nodes=0; n2nodes=0;
    dfs1(0);
    printf("done: stage1sols=%lld s1nodes=%lld s2nodes=%lld full=%d t=%lds timeout=%d\n",n1,s1nodes,n2nodes,nfull,(long)(time(0)-t0),timedout);
    for(int s=0;s<nfull&&s<8;s++){
        printf("FULL %d n=%d:\n",s,stored_n[s]);
        for(int k=0;k<stored_n[s];k++){
            int v=stored_full[s][k];
            if(v<27) printf("  FIX f=%d i=%d\n",v/9,v%9);
            else if(v<1000+300) printf("  MIX (%d,%d,%d)\n",mixrep[v-1000][0],mixrep[v-1000][1],mixrep[v-1000][2]);
            else printf("  P3 (%d,%d,%d)\n",p3rep[v-2000][0],p3rep[v-2000][1],p3rep[v-2000][2]);
        }
    }
    fflush(stdout);
    return 0;
}
