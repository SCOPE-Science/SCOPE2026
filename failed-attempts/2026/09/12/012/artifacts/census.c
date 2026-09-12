// Exact census of Av(1342,1423) vs Av(1342,1432) by DFS on shared Av(1342) tree.
// Appending value v to perm p[0..n-1] (values 1..n): new 4-patterns ending at
// last position detected in O(n^2) via rank rules:
//   1342 = (1,3,4,2): exists i<j<k: p[i]<v<p[j]<p[k]
//   1423 = (1,4,2,3): exists i<j<k: p[i]<p[k]<v<p[j]
//   1432 = (1,4,3,2): exists i<j<k: p[i]<v<p[k]<p[j]
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>
#ifdef _OPENMP
#include <omp.h>
#endif

#define MAXN 16
#define NTHREADS 64

static unsigned long long cntA[NTHREADS][MAXN+1];
static unsigned long long cntB[NTHREADS][MAXN+1];
static int witA[MAXN+1][MAXN+1];
static int witB[MAXN+1][MAXN+1];
static int haveA[MAXN+1], haveB[MAXN+1];

static inline void endings(int *p, int n, int v,
                           int *e1342, int *e1423, int *e1432) {
  int r2=0, r3=0, r4=0, pref=INT_MAX, j, k;
  for (j=0;j<n;j++) {
    if (pref < v && p[j] >= v) {
      for (k=j+1;k<n;k++) if (p[k] > p[j]) { r2=1; break; }
      for (k=j+1;k<n;k++) if (p[k] >= v && p[k] < p[j]) { r4=1; break; }
      for (k=j+1;k<n;k++) if (p[k] < v && p[k] > pref) { r3=1; break; }
      if (r2 && r3 && r4) break;
    }
    if (p[j]<pref) pref=p[j];
  }
  *e1342=r2; *e1423=r3; *e1432=r4;
}

static void dfs(int tid, int *p, int start, int h23, int h32, int nmax) {
  int vs[MAXN+1];
  int s23[MAXN+1], s32[MAXN+1];
  int d, v, e2, e3, e4;
  for (d=0;d<=start;d++) vs[d]=1;
  s23[start]=h23; s32[start]=h32;
  d = start;
  while (1) {
    if (d > nmax) { d--; if (d<=start) break;
      { int ov = p[d]; for (int i=0;i<d;i++) if (p[i]>ov) p[i]--; }
      continue; }
    v = vs[d];
    if (v > d+1) {
      vs[d]=1;
      d--; if (d<start) break;
      { int ov = p[d]; for (int i=0;i<d;i++) if (p[i]>ov) p[i]--; }
      continue;
    }
    vs[d]++;
    endings(p, d, v, &e2, &e3, &e4);
    if (e2) continue;
    for (int i=0;i<d;i++) if (p[i]>=v) p[i]++;
    p[d]=v;
    {
      int nh23 = s23[d]||e3, nh32 = s32[d]||e4;
      int nd = d+1;
      s23[nd]=nh23; s32[nd]=nh32;
      if (!nh23) cntA[tid][nd]++;
      if (!nh32) cntB[tid][nd]++;
      if ((!nh23 && nh32) || (!nh32 && nh23)) {
#pragma omp critical
        {
          if (!nh23 && nh32 && !haveA[nd] && nd>=1) {
            haveA[nd]=1;
            for (int i=0;i<nd;i++) witA[nd][i]=p[i];
          }
          if (!nh32 && nh23 && !haveB[nd] && nd>=1) {
            haveB[nd]=1;
            for (int i=0;i<nd;i++) witB[nd][i]=p[i];
          }
        }
      }
      vs[nd]=1;
      d = nd;
    }
  }
}

int main(int argc, char **argv) {
  int nmax = argc>1 ? atoi(argv[1]) : 12;
  int L = argc>2 ? atoi(argv[2]) : 6;
  static int preflist[8192][MAXN+1];
  static int pfl23[8192], pfl32[8192];
  int npref=0;
  {
    int p[MAXN+1]; int vs[MAXN+1]; int f23[MAXN+1], f32[MAXN+1];
    for (int i=0;i<=L;i++) vs[i]=1;
    f23[0]=0; f32[0]=0;
    int d=0;
    while (1) {
      if (d==L) {
        for (int i=0;i<L;i++) preflist[npref][i]=p[i];
        pfl23[npref]=f23[L]; pfl32[npref]=f32[L]; npref++;
        d--; { int ov=p[d]; for(int i=0;i<d;i++) if(p[i]>ov) p[i]--; }
        continue;
      }
      int v=vs[d];
      if (v>d+1) { vs[d]=1; d--; if(d<0) break;
        { int ov=p[d]; for(int i=0;i<d;i++) if(p[i]>ov) p[i]--; } continue; }
      vs[d]++;
      int e2,e3,e4; endings(p,d,v,&e2,&e3,&e4);
      if (e2) continue;
      for(int i=0;i<d;i++) if(p[i]>=v) p[i]++;
      p[d]=v; f23[d+1]=f23[d]||e3; f32[d+1]=f32[d]||e4; vs[d+1]=1; d++;
    }
  }
  fprintf(stderr, "prefixes(L=%d): %d\n", L, npref);
  static unsigned long long baseA[MAXN+1], baseB[MAXN+1];
  {
    int p[MAXN+1]; int vs[MAXN+1]; int f23[MAXN+1], f32[MAXN+1];
    for (int i=0;i<=L;i++) vs[i]=1;
    f23[0]=0; f32[0]=0; baseA[0]=1; baseB[0]=1;
    int d=0;
    while (1) {
      if (d==L) { d--; { int ov=p[d]; for(int i=0;i<d;i++) if(p[i]>ov) p[i]--; } continue; }
      int v=vs[d];
      if (v>d+1) { vs[d]=1; d--; if(d<0) break;
        { int ov=p[d]; for(int i=0;i<d;i++) if(p[i]>ov) p[i]--; } continue; }
      vs[d]++;
      int e2,e3,e4; endings(p,d,v,&e2,&e3,&e4);
      if (e2) continue;
      for(int i=0;i<d;i++) if(p[i]>=v) p[i]++;
      p[d]=v;
      int nh23=f23[d]||e3, nh32=f32[d]||e4;
      f23[d+1]=nh23; f32[d+1]=nh32;
      if(!nh23) baseA[d+1]++; if(!nh32) baseB[d+1]++;
      vs[d+1]=1; d++;
    }
  }
#pragma omp parallel for schedule(dynamic) num_threads(32)
  for (int i=0;i<npref;i++) {
    int tid=0;
#ifdef _OPENMP
    tid = omp_get_thread_num();
#endif
    int p[MAXN+1];
    for (int j=0;j<L;j++) p[j]=preflist[i][j];
    dfs(tid, p, L, pfl23[i], pfl32[i], nmax);
  }
  unsigned long long A[MAXN+1], B[MAXN+1];
  for (int n=0;n<=nmax;n++) {
    A[n]=baseA[n]; B[n]=baseB[n];
    for (int t=0;t<NTHREADS;t++){ A[n]+=cntA[t][n]; B[n]+=cntB[t][n]; }
  }
  printf("n Av1342_1423 Av1342_1432\n");
  for (int n=0;n<=nmax;n++) printf("%d %llu %llu%s\n", n, A[n], B[n], A[n]!=B[n]?"  <-- DIFF":"");
  for (int n=0;n<=nmax;n++) if (haveA[n]) {
    printf("witA n=%d:", n); for(int i=0;i<n;i++) printf(" %d", witA[n][i]); printf("\n"); }
  for (int n=0;n<=nmax;n++) if (haveB[n]) {
    printf("witB n=%d:", n); for(int i=0;i<n;i++) printf(" %d", witB[n][i]); printf("\n"); }
  return 0;
}
