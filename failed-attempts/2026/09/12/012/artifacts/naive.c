// INDEPENDENT validator: naive O(n^4) direct 4-tuple pattern test on full perms.
// Shares NO code with census.c (no incremental endings, no flags, no fan-out).
#include <stdio.h>
#include <stdlib.h>
#ifdef _OPENMP
#include <omp.h>
#endif
#define MAXN 12
#define NTHREADS 64
static unsigned long long cA[NTHREADS][MAXN+1], cB[NTHREADS][MAXN+1];
static unsigned long long sA[MAXN+1], sB[MAXN+1];
static int P1342[4]={1,3,4,2}, P1423[4]={1,4,2,3}, P1432[4]={1,4,3,2};
static int contains_pat(int *p,int n,int *q){
  int i,j,k,l,a,b,s[4];
  for(i=0;i<n;i++)for(j=i+1;j<n;j++)for(k=j+1;k<n;k++)for(l=k+1;l<n;l++){
    int x0=p[i],x1=p[j],x2=p[k],x3=p[l];
    int xs[4]={x0,x1,x2,x3};
    for(a=0;a<4;a++){s[a]=1;for(b=0;b<4;b++)if(xs[b]<xs[a])s[a]++;}
    if(s[0]==q[0]&&s[1]==q[1]&&s[2]==q[2]&&s[3]==q[3])return 1;
  }
  return 0;
}
static void dfs(int tid,int *p,int n,int nmax){
  int v,i;
  if(!contains_pat(p,n,P1342)&&!contains_pat(p,n,P1423))cA[tid][n]++;
  if(!contains_pat(p,n,P1342)&&!contains_pat(p,n,P1432))cB[tid][n]++;
  if(n==nmax)return;
  for(v=1;v<=n+1;v++){
    for(i=0;i<n;i++)if(p[i]>=v)p[i]++;
    p[n]=v;
    if(!contains_pat(p,n+1,P1342)) dfs(tid,p,n+1,nmax);
    for(i=0;i<n;i++)if(p[i]>v)p[i]--;
  }
}
static int pre[5040*7]; static int np=0; static int gL=5;
static void gen(int*p,int*used,int d){
  if(d==gL){for(int i=0;i<gL;i++)pre[np*7+i]=p[i];np++;return;}
  for(int v=1;v<=gL;v++)if(!used[v]){used[v]=1;p[d]=v;gen(p,used,d+1);used[v]=0;}
}
static void gen2(int*p,int*used,int d,int n){
  if(d==n){
    if(!contains_pat(p,n,P1342)&&!contains_pat(p,n,P1423))sA[n]++;
    if(!contains_pat(p,n,P1342)&&!contains_pat(p,n,P1432))sB[n]++;
    return;}
  for(int v=1;v<=n;v++)if(!used[v]){used[v]=1;p[d]=v;gen2(p,used,d+1,n);used[v]=0;}
}
int main(int argc,char**argv){
  int nmax=argc>1?atoi(argv[1]):10, L=argc>2?atoi(argv[2]):5, n, t;
  gL=L;
  { int p[8]={0},used[9]={0}; gen(p,used,0); }
  fprintf(stderr,"naive prefixes: %d\n",np);
#pragma omp parallel for schedule(dynamic) num_threads(32)
  for(int i=0;i<np;i++){int tid=0;
#ifdef _OPENMP
    tid=omp_get_thread_num();
#endif
    int p[MAXN+1];for(int j=0;j<L;j++)p[j]=pre[i*7+j];dfs(tid,p,L,nmax);}
  unsigned long long A[MAXN+1]={0},B[MAXN+1]={0};
  sA[0]=1;sB[0]=1;
  { for(n=1;n<L;n++){int p2[8]={0},u2[9]={0};gen2(p2,u2,0,n);} }
  for(n=0;n<L;n++){A[n]=sA[n];B[n]=sB[n];}
  for(n=L;n<=nmax;n++){for(t=0;t<NTHREADS;t++){A[n]+=cA[t][n];B[n]+=cB[t][n];}}
  printf("n naiveA naiveB\n");
  for(n=0;n<=nmax;n++)printf("%d %llu %llu%s\n",n,A[n],B[n],A[n]!=B[n]?" DIFF":"");
  return 0;
}
