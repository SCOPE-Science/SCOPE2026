// canon8.c v1.0 — isomorphism census of labeled (3,4)-free colorings of K8.
// Reads hex masks (one per line) from stdin.
// Canon key: lexicographic minimum over all 40320 vertex perms of the
// 28-bit vector in edge-lex order. Aut order: # perms fixing the coloring.
// Output (stdout): one line per class:
//   canon_hex count aut reddegseq
// stderr: #classes, timing.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#ifdef _OPENMP
#include <omp.h>
#endif
#define N 8
#define M 28
#define NPERM 40320

static int E_[M][2];
static unsigned char PERMS[NPERM][N];

static void gen_perms(void) {
    int p[N], i, n = 0;
    for (i = 0; i < N; i++) p[i] = i;
    for (;;) {
        for (i = 0; i < N; i++) PERMS[n][i] = (unsigned char)p[i];
        n++;
        int a = N - 2;
        while (a >= 0 && p[a] >= p[a + 1]) a--;
        if (a < 0) break;
        int b = N - 1;
        while (p[b] <= p[a]) b--;
        int t = p[a]; p[a] = p[b]; p[b] = t;
        int l = a + 1, r = N - 1;
        while (l < r) { t = p[l]; p[l] = p[r]; p[r] = t; l++; r--; }
    }
}

typedef struct { unsigned int key; int aut; int cnt; int deg[8]; } CLS;

int main(void) {
    int i, j, e;
    for (i = 0, e = 0; i < N; i++) for (j = i + 1; j < N; j++) { E_[e][0] = i; E_[e][1] = j; e++; }
    gen_perms();
    unsigned *masks = NULL; size_t cap = 0, nm = 0;
    char line[64];
    while (fgets(line, sizeof line, stdin)) {
        unsigned v = (unsigned)strtoul(line, NULL, 16);
        if (nm == cap) { cap = cap ? cap * 2 : 4096; masks = realloc(masks, cap * sizeof *masks); }
        masks[nm++] = v;
    }
    fprintf(stderr, "read %zu models\n", nm);
    CLS *cls = malloc(nm * sizeof *cls);
#pragma omp parallel for schedule(static)
    for (size_t s = 0; s < nm; s++) {
        unsigned R[N][N]; int a, b;
        memset(R, 0, sizeof R);
        for (e = 0; e < M; e++) if ((masks[s] >> e) & 1u) { a = E_[e][0]; b = E_[e][1]; R[a][b] = R[b][a] = 1; }
        unsigned best = 0xFFFFFFFu; int aut = 0;
        for (int q = 0; q < NPERM; q++) {
            unsigned key = 0;
            for (e = 0; e < M; e++) {
                int u = PERMS[q][E_[e][0]], v = PERMS[q][E_[e][1]];
                if (u > v) { int t = u; u = v; v = t; }
                if (R[u][v]) key |= (1u << e);
            }
            if (key < best) best = key;
            if (key == masks[s]) aut++;
        }
        cls[s].key = best; cls[s].aut = aut; cls[s].cnt = 1;
        int dg[N]; for (a = 0; a < N; a++) { dg[a] = 0; for (b = 0; b < N; b++) dg[a] += R[a][b]; }
        // insertion sort
        for (a = 1; a < N; a++) { int t2 = dg[a], k = a - 1; while (k >= 0 && dg[k] > t2) { dg[k + 1] = dg[k]; k--; } dg[k + 1] = t2; }
        for (a = 0; a < N; a++) cls[s].deg[a] = dg[a];
    }
    // sort by key
    int cmp(const void *A, const void *B) {
        unsigned x = ((CLS*)A)->key, y = ((CLS*)B)->key;
        return (x > y) - (x < y);
    }
    qsort(cls, nm, sizeof *cls, cmp);
    size_t nc = 0;
    for (size_t s = 0; s < nm; s++) {
        if (nc && cls[nc-1].key == cls[s].key) { cls[nc-1].cnt++; continue; }
        cls[nc++] = cls[s];
    }
    for (size_t s = 0; s < nc; s++) {
        printf("%07x %d %d %d%d%d%d%d%d%d%d\n", cls[s].key, cls[s].cnt, cls[s].aut,
            cls[s].deg[0], cls[s].deg[1], cls[s].deg[2], cls[s].deg[3],
            cls[s].deg[4], cls[s].deg[5], cls[s].deg[6], cls[s].deg[7]);
    }
    fprintf(stderr, "classes=%zu total=%zu\n", nc, nm);
    return 0;
}
