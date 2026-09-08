// check13.c v1.0 — STANDALONE brute-force checker for the K13 (3,5) witness.
// Reads the 78-char BITS line from witness13.txt. Enumerates all C(13,3)=286
// triples (red-K3 test) and all C(13,5)=1287 quintuples (blue-K5 test).
// No solver calls. Exit 0 iff red triangle-free AND blue K5-free.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define N 13
#define M 78
int main(int argc, char **argv) {
    if (argc < 2) { fprintf(stderr, "usage: check13 BITS78\n"); return 2; }
    char *b = argv[1];
    if ((int)strlen(b) != M) { fprintf(stderr, "need 78 bits, got %zu\n", strlen(b)); return 2; }
    int E_[M][2], e, i, j;
    for (i = 0, e = 0; i < N; i++) for (j = i + 1; j < N; j++) { E_[e][0] = i; E_[e][1] = j; e++; }
    int R[N][N];
    for (i = 0; i < N; i++) for (j = 0; j < N; j++) R[i][j] = 0;
    for (e = 0; e < M; e++) {
        if (b[e] != '0' && b[e] != '1') { fprintf(stderr, "bad char\n"); return 2; }
        int u = E_[e][0], v = E_[e][1], r = b[e] - '0';
        R[u][v] = R[v][u] = r;
    }
    int a, c2, d, k, l, ntri = 0, nk5 = 0;
    for (a = 0; a < N; a++) for (c2 = a + 1; c2 < N; c2++) for (d = c2 + 1; d < N; d++)
        if (R[a][c2] && R[a][d] && R[c2][d]) { printf("RED-TRIANGLE %d %d %d\n", a, c2, d); ntri++; }
    int q[5], x, y;
    for (q[0]=0;q[0]<N;q[0]++)for(q[1]=q[0]+1;q[1]<N;q[1]++)for(q[2]=q[1]+1;q[2]<N;q[2]++)
    for(q[3]=q[2]+1;q[3]<N;q[3]++)for(q[4]=q[3]+1;q[4]<N;q[4]++) {
        int ok = 1;
        for (x = 0; x < 5 && ok; x++) for (y = x + 1; y < 5; y++) {
            int u = q[x], v = q[y];
            if (R[u < v ? u : v][u < v ? v : u] != 0) { ok = 0; break; }
        }
        if (ok) { printf("BLUE-K5 %d %d %d %d %d\n", q[0],q[1],q[2],q[3],q[4]); nk5++; }
    }
    printf("triples_checked=286 red_triangles=%d quintuples_checked=1287 blue_K5s=%d\n", ntri, nk5);
    if (ntri == 0 && nk5 == 0) { printf("WITNESS_OK\n"); return 0; }
    return 1;
}
