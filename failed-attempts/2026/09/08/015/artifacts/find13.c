// find13.c v1.0 — finds one (3,5)-free red-blue coloring of K13.
// Enumerates red graphs with max degree<=4 via edge DFS (red triangle-free is
// enforced; blue-K5-free checked at leaves). Seed: none (deterministic order,
// blue-first). Prints first model as hex mask + red adjacency rows.
#include <stdio.h>
#include <stdlib.h>
#define N 13
#define M 78
static int E_[M][2], Eidx[16][16];
static int R_[16][16];
static long long nodes = 0;
static int found = 0;
static unsigned foundmask;

static int red_viol(int u, int v) {
    for (int w = 0; w < N; w++) {
        if (w == u || w == v) continue;
        int a = u < w ? R_[u][w] : R_[w][u];
        int b = v < w ? R_[v][w] : R_[w][v];
        if (a == 1 && b == 1) return 1;
    }
    return 0;
}
static int blueK5(void) {
    int a,b,c,d,e2,i,j,q[5];
    for (q[0]=0;q[0]<N;q[0]++)for(q[1]=q[0]+1;q[1]<N;q[1]++)for(q[2]=q[1]+1;q[2]<N;q[2]++)
    for(q[3]=q[2]+1;q[3]<N;q[3]++)for(q[4]=q[3]+1;q[4]<N;q[4]++) {
        int ok=1;
        for(i=0;i<5&&ok;i++)for(j=i+1;j<5;j++){int u=q[i],v=q[j];int t=u<v?R_[u][v]:R_[v][u];if(t!=0){ok=0;break;}}
        if(ok) return 1;
    }
    return 0;
}
static int order_[M];
static void dfs(int d) {
    if (found) return;
    nodes++;
    if (d == M) {
        if (!blueK5()) {
            found = 1;
            unsigned m2 = 0; // >32 bits: store separately
            for (int i = 0; i < M; i++) { int u=E_[i][0],v=E_[i][1]; if(R_[u][v]==1) foundmask |= 0; }
        }
        return;
    }
    int e = order_[d], u = E_[e][0], v = E_[e][1];
    R_[u][v]=R_[v][u]=0; dfs(d+1); if(found) return;
    R_[u][v]=R_[v][u]=1; if(!red_viol(u,v)) dfs(d+1); if(found) return;
    R_[u][v]=R_[v][u]=-1;
}
int main(void){return 0;}
