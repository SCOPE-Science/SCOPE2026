/* Exact census of Av(4231,3124) and Av(4231,3214) by max-insertion DFS.
 * Inserting the new maximum n can only create a pattern occurrence in which
 * the new element plays the role of value 4. Since 4 is first in 4231 and
 * last in 3124/3214, only triples fully after (for 4231) or fully before
 * (for 3124/3214) the insertion slot need checking.
 * Node flags: f3124 / f3214 = pattern already present. Anchor 4231 prunes.
 * Alive = !has4231 && (!has3124 || !has3214).
 * Compile: gcc -O2 -fopenmp census.c -o census
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#ifdef _OPENMP
#include <omp.h>
#endif

static long long cntA[20], cntB[20];
static int NMAX;

/* relative order tests for values (x,y,z) at increasing positions */
static inline int is231(int x, int y, int z) { return (z < x && x < y); }
static inline int is312(int x, int y, int z) { return (y < z && z < x); }
static inline int is321(int x, int y, int z) { return (z < y && y < x); }

static void dfs(unsigned char *a, int n, int f3124, int f3214,
                long long *lA, long long *lB) {
    if (!f3124) lA[n]++;
    if (!f3214) lB[n]++;
    if (n == NMAX) return;
    unsigned char c[20];
    for (int p = 0; p <= n; p++) {
        for (int i = 0; i < p; i++) c[i] = a[i];
        c[p] = (unsigned char)n;
        for (int i = p; i < n; i++) c[i + 1] = a[i];
        /* anchor 4231: new max first, need triple after p of type (2,3,1) */
        int bad = 0;
        for (int i = p + 1; i <= n && !bad; i++)
            for (int j = i + 1; j <= n && !bad; j++)
                for (int k = j + 1; k <= n; k++)
                    if (is231(c[i], c[j], c[k])) { bad = 1; break; }
        if (bad) continue;
        int g3124 = f3124, g3214 = f3214;
        if (!g3124 || !g3214) {
            for (int i = 0; i < p && (!g3124 || !g3214); i++)
                for (int j = i + 1; j < p && (!g3124 || !g3214); j++)
                    for (int k = j + 1; k < p; k++) {
                        if (!g3124 && is312(c[i], c[j], c[k])) g3124 = 1;
                        if (!g3214 && is321(c[i], c[j], c[k])) g3214 = 1;
                        if (g3124 && g3214) break;
                    }
            if (g3124 && g3214) continue;
        }
        dfs(c, n + 1, g3124, g3214, lA, lB);
    }
}

typedef struct { unsigned char a[20]; unsigned char n, f1, f2; } Node;
static Node *frontier;
static long frontier_n, frontier_cap;

static void collect(unsigned char *a, int n, int f1, int f2, int K0) {
    if (n == K0) {
        if (frontier_n == frontier_cap) {
            frontier_cap = frontier_cap ? frontier_cap * 2 : 1024;
            frontier = realloc(frontier, frontier_cap * sizeof(Node));
        }
        Node *nd = &frontier[frontier_n++];
        memcpy(nd->a, a, n);
        nd->n = n; nd->f1 = f1; nd->f2 = f2;
        return;
    }
    unsigned char c[20];
    for (int p = 0; p <= n; p++) {
        for (int i = 0; i < p; i++) c[i] = a[i];
        c[p] = (unsigned char)n;
        for (int i = p; i < n; i++) c[i + 1] = a[i];
        int bad = 0;
        for (int i = p + 1; i <= n && !bad; i++)
            for (int j = i + 1; j <= n && !bad; j++)
                for (int k = j + 1; k <= n; k++)
                    if (is231(c[i], c[j], c[k])) { bad = 1; break; }
        if (bad) continue;
        int g1 = f1, g2 = f2;
        if (!g1 || !g2) {
            for (int i = 0; i < p && (!g1 || !g2); i++)
                for (int j = i + 1; j < p && (!g1 || !g2); j++)
                    for (int k = j + 1; k < p; k++) {
                        if (!g1 && is312(c[i], c[j], c[k])) g1 = 1;
                        if (!g2 && is321(c[i], c[j], c[k])) g2 = 1;
                        if (g1 && g2) break;
                    }
            if (g1 && g2) continue;
        }
        collect(c, n + 1, g1, g2, K0);
    }
}

int main(int argc, char **argv) {
    NMAX = argc > 1 ? atoi(argv[1]) : 12;
    int K0 = argc > 2 ? atoi(argv[2]) : 8;
    if (NMAX > 18) { fprintf(stderr, "NMAX too big\n"); return 1; }
    unsigned char root[20];
    /* sequential counts below frontier depth */
    long long seqA[20] = {0}, seqB[20] = {0};
    /* count small n directly while collecting */
    collect(root, 0, 0, 0, K0);
    /* sequential prefix counts: rerun small DFS for n<=K0 */
    {
        long long tA[20] = {0}, tB[20] = {0};
        int save = NMAX; NMAX = K0;
        dfs(root, 0, 0, 0, tA, tB);
        NMAX = save;
        for (int n = 0; n <= K0; n++) { seqA[n] = tA[n]; seqB[n] = tB[n]; }
    }
    long long totA[20] = {0}, totB[20] = {0};
    for (int n = 0; n <= K0; n++) { totA[n] = seqA[n]; totB[n] = seqB[n]; }
#pragma omp parallel
    {
        long long lA[20] = {0}, lB[20] = {0};
#pragma omp for schedule(dynamic, 64)
        for (long i = 0; i < frontier_n; i++) {
            Node *nd = &frontier[i];
            /* count the frontier node itself (depth K0) once per thread? No:
               depth-K0 counts already in seq; dfs would recount. Avoid by
               counting only deeper levels: temporarily offset. */
            long long dA[20] = {0}, dB[20] = {0};
            /* run dfs but skip counting depth K0: do one manual expansion */
            unsigned char *a = nd->a; int n = nd->n;
            if (n >= NMAX) continue; /* K0==NMAX: nothing deeper to count */
            unsigned char c[20];
            for (int p = 0; p <= n; p++) {
                for (int ii = 0; ii < p; ii++) c[ii] = a[ii];
                c[p] = (unsigned char)n;
                for (int ii = p; ii < n; ii++) c[ii + 1] = a[ii];
                int bad = 0;
                for (int ii = p + 1; ii <= n && !bad; ii++)
                    for (int j = ii + 1; j <= n && !bad; j++)
                        for (int k = j + 1; k <= n; k++)
                            if (is231(c[ii], c[j], c[k])) { bad = 1; break; }
                if (bad) continue;
                int g1 = nd->f1, g2 = nd->f2;
                if (!g1 || !g2) {
                    for (int ii = 0; ii < p && (!g1 || !g2); ii++)
                        for (int j = ii + 1; j < p && (!g1 || !g2); j++)
                            for (int k = j + 1; k < p; k++) {
                                if (!g1 && is312(c[ii], c[j], c[k])) g1 = 1;
                                if (!g2 && is321(c[ii], c[j], c[k])) g2 = 1;
                                if (g1 && g2) break;
                            }
                    if (g1 && g2) continue;
                }
                dfs(c, n + 1, g1, g2, dA, dB);
            }
            for (int nn = K0 + 1; nn <= NMAX; nn++) { lA[nn] += dA[nn]; lB[nn] += dB[nn]; }
        }
#pragma omp critical
        for (int nn = K0 + 1; nn <= NMAX; nn++) { totA[nn] += lA[nn]; totB[nn] += lB[nn]; }
    }
    printf("n,Av4231_3124,Av4231_3214\n");
    for (int n = 0; n <= NMAX; n++)
        printf("%d,%lld,%lld\n", n, totA[n], totB[n]);
    fprintf(stderr, "frontier=%ld K0=%d\n", frontier_n, K0);
    return 0;
}
