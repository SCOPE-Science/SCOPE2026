// sa13.c v1.0 — deterministic local search for a (3,5)-free coloring of K13.
// Red = 1, blue = 0. Cost = 10*(#red K3) + (#blue K5). Greedy single-edge
// flips with deterministic tie-break + seeded restarts (xorshift, fixed seed).
// Exhaustively evaluates all 78 flips per step; stops at cost 0.
#include <stdio.h>
#include <stdlib.h>
#define N 13
#define M 78
static int E_[M][2];
static unsigned long long rng = 0x123456789abcdefULL;
static unsigned long long xr(void) { rng ^= rng << 13; rng ^= rng >> 7; rng ^= rng << 17; return rng; }

static int R_[N][N];

static long cost(int *ntri, int *nk5) {
    int a, b, c, i, j, t = 0, k = 0;
    for (a = 0; a < N; a++) for (b = a + 1; b < N; b++) for (c = b + 1; c < N; c++)
        if (R_[a][b] == 1 && R_[a][c] == 1 && R_[b][c] == 1) t++;
    int q[5];
    for (q[0]=0;q[0]<N;q[0]++)for(q[1]=q[0]+1;q[1]<N;q[1]++)for(q[2]=q[1]+1;q[2]<N;q[2]++)
    for(q[3]=q[2]+1;q[3]<N;q[3]++)for(q[4]=q[3]+1;q[4]<N;q[4]++) {
        int ok=1;
        for(i=0;i<5&&ok;i++)for(j=i+1;j<5;j++){int u=q[i],v=q[j];int z=u<v?R_[u][v]:R_[v][u];if(z!=0){ok=0;break;}}
        if(ok) k++;
    }
    if (ntri) *ntri = t; if (nk5) *nk5 = k;
    return 10L * t + k;
}

int main(void) {
    int i, j, e;
    for (i = 0, e = 0; i < N; i++) for (j = i + 1; j < N; j++) { E_[e][0] = i; E_[e][1] = j; e++; }
    for (int restart = 0; restart < 200; restart++) {
        for (i = 0; i < N; i++) for (j = 0; j < N; j++) R_[i][j] = (i == j) ? -1 : (int)(xr() & 1);
        for (int step = 0; step < 20000; step++) {
            int t, k; long c = cost(&t, &k);
            if (c == 0) {
                printf("FOUND restart=%d step=%d\n", restart, step);
                // print mask as hex (78 bits -> 20 hex digits) + red adjacency rows
                char hex[24]; for (i = 0; i < 20; i++) hex[i] = '0'; hex[20] = 0;
                for (e = 0; e < M; e++) {
                    int u = E_[e][0], v = E_[e][1];
                    if ((u < v ? R_[u][v] : R_[v][u]) == 1) {
                        int pos = M - 1 - e; // print MSB first
                        int nib = pos / 4, bit = pos % 4;
                        hex[19 - nib] += 0; // nibble index from right
                    }
                }
                // simpler: print 78-char bitstring in edge-lex order
                char bits[M + 1];
                for (e = 0; e < M; e++) { int u=E_[e][0],v=E_[e][1]; bits[e] = (u<v?R_[u][v]:R_[v][u])==1?'1':'0'; }
                bits[M] = 0;
                printf("BITS %s\n", bits);
                for (i = 0; i < N; i++) {
                    for (j = 0; j < N; j++) printf("%c", i == j ? '.' : ((i<j?R_[i][j]:R_[j][i])==1?'1':'0'));
                    printf("\n");
                }
                printf("redtri=%d blueK5=%d\n", t, k);
                return 0;
            }
            // find best flip
            long best = c; int beste = -1;
            for (e = 0; e < M; e++) {
                int u = E_[e][0], v = E_[e][1];
                R_[u][v] = R_[v][u] = 1 - R_[u][v];
                long c2 = cost(NULL, NULL);
                R_[u][v] = R_[v][u] = 1 - R_[u][v];
                if (c2 < best) { best = c2; beste = e; }
            }
            if (beste >= 0) {
                int u = E_[beste][0], v = E_[beste][1];
                R_[u][v] = R_[v][u] = 1 - R_[u][v];
            } else {
                // sideways/random kick: flip 2 random edges
                for (int f = 0; f < 2; f++) { e = xr() % M; int u=E_[e][0],v=E_[e][1]; R_[u][v]=R_[v][u]=1-R_[u][v]; }
            }
        }
    }
    printf("NOTFOUND\n");
    return 1;
}
