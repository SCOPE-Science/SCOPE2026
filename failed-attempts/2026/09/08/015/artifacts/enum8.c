// enum8.c v1.0 — exhaustive labeled enumeration of (3,4)-free red-blue edge
// colorings of K_8. Variable x_e = 1 means edge e red, 0 blue; edges in
// lexicographic order. Forbids red K3 (56 triples) and blue K4 (70 quads).
// DFS over edges in fixed order with forward checking: when edge d is set,
// only clauses whose maximum edge is d can become newly violated.
// Usage: ./enum8 [n]  (default n=8; n=7 supported for self-test)
// Output: stdout one line per model (hex of 28/21-bit mask, edge0 = LSB),
//         stderr node/model counts.
#include <stdio.h>
#include <stdlib.h>

static int n, m, E_[64][2], Eidx[16][16];
static int Tby[64][32][2], Tcnt[64];
static int Qby[64][32][5], Qcnt[64];
static int A[64];
static long long nodes = 0, models = 0;
static FILE *out;

static void check_add_tri(int a, int b, int c) {
    int mx = a; if (b > mx) mx = b; if (c > mx) mx = c;
    int k = Tcnt[mx]++, o = 0, oarr[2];
    if (a != mx) oarr[o++] = a;
    if (b != mx) oarr[o++] = b;
    if (c != mx) oarr[o++] = c;
    Tby[mx][k][0] = oarr[0]; Tby[mx][k][1] = oarr[1];
}
static void check_add_quad(int e[6]) {
    int mx = e[0], i;
    for (i = 1; i < 6; i++) if (e[i] > mx) mx = e[i];
    int k = Qcnt[mx]++, o = 0;
    for (i = 0; i < 6; i++) if (e[i] != mx) Qby[mx][k][o++] = e[i];
}

static void dfs(int d) {
    nodes++;
    if (d == m) {
        unsigned int mask = 0, i;
        for (i = 0; i < (unsigned)m; i++) if (A[i]) mask |= (1u << i);
        fprintf(out, "%07x\n", mask);
        models++;
        return;
    }
    int k, ok;
    // try red (1)
    ok = 1;
    for (k = 0; k < Tcnt[d]; k++)
        if (A[Tby[d][k][0]] && A[Tby[d][k][1]]) { ok = 0; break; }
    if (ok) { A[d] = 1; dfs(d + 1); }
    // try blue (0)
    ok = 1;
    for (k = 0; k < Qcnt[d]; k++)
        if (!A[Qby[d][k][0]] && !A[Qby[d][k][1]] && !A[Qby[d][k][2]] &&
            !A[Qby[d][k][3]] && !A[Qby[d][k][4]]) { ok = 0; break; }
    if (ok) { A[d] = 0; dfs(d + 1); }
    A[d] = -1;
}

int main(int argc, char **argv) {
    n = (argc > 1) ? atoi(argv[1]) : 8;
    int i, j, k;
    m = 0;
    for (i = 0; i < n; i++)
        for (j = i + 1; j < n; j++) { E_[m][0] = i; E_[m][1] = j; Eidx[i][j] = m++; }
    for (i = 0; i < m; i++) { A[i] = -1; Tcnt[i] = 0; Qcnt[i] = 0; }
    // triples
    int a, b, c;
    for (a = 0; a < n; a++) for (b = a + 1; b < n; b++) for (c = b + 1; c < n; c++)
        check_add_tri(Eidx[a][b], Eidx[a][c], Eidx[b][c]);
    // quads
    int q[4], e[6];
    for (q[0] = 0; q[0] < n; q[0]++) for (q[1] = q[0] + 1; q[1] < n; q[1]++)
        for (q[2] = q[1] + 1; q[2] < n; q[2]++) for (q[3] = q[2] + 1; q[3] < n; q[3]++) {
            e[0] = Eidx[q[0]][q[1]]; e[1] = Eidx[q[0]][q[2]]; e[2] = Eidx[q[0]][q[3]];
            e[3] = Eidx[q[1]][q[2]]; e[4] = Eidx[q[1]][q[3]]; e[5] = Eidx[q[2]][q[3]];
            check_add_quad(e);
        }
    out = stdout;
    dfs(0);
    fprintf(stderr, "n=%d m=%d nodes=%lld models=%lld\n", n, m, nodes, models);
    return 0;
}
