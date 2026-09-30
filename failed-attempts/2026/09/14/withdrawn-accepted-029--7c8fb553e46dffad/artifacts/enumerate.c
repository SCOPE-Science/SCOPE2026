/* Exact length-distribution ledger for 3x3-box (4x4-vertex) critical bond percolation.
 *
 * Graph: vertices (x,y), x,y in {0,1,2,3}, id = y*4+x (16 vertices).
 * Edges: all pairs with both endpoints in the box:
 *   12 horizontal ((x,y)-(x+1,y)), 12 vertical ((x,y)-(x,y+1)) => 24 edges.
 * Enumerates all 2^24 configurations; per config, multi-source BFS from the
 * left side (x=0) over open edges; S = min distance to right side (x=3),
 * or "no crossing" if unreachable. Accumulates exact integer histogram.
 */
#include <stdio.h>
#include <stdint.h>
#include <string.h>

#ifdef _OPENMP
#include <omp.h>
#endif

#define NV 16
#define NE 24
#define NCONF ((uint32_t)1u << 24)

static int eu[NE], ev[NE];
static int deg[NV], adj[NV][4], adje[NV][4];

static void build_graph(void) {
    int id;
    for (int y = 0; y < 4; y++)
        for (int x = 0; x < 3; x++) {
            id = y * 3 + x;
            eu[id] = y * 4 + x;
            ev[id] = y * 4 + x + 1;
        }
    for (int x = 0; x < 4; x++)
        for (int y = 0; y < 2; y++) {
            /* NOTE: vertical block uses y<2 -> only 8 edges; remaining filled below */
            id = 12 + x * 3 + y;
            eu[id] = y * 4 + x;
            ev[id] = (y + 1) * 4 + x;
        }
    /* y=2 vertical edges: ids 12+x*3+2 */
    for (int x = 0; x < 4; x++) {
        id = 12 + x * 3 + 2;
        eu[id] = 2 * 4 + x;
        ev[id] = 3 * 4 + x;
    }
    memset(deg, 0, sizeof deg);
    for (int e = 0; e < NE; e++) {
        int u = eu[e], v = ev[e];
        adj[u][deg[u]] = v; adje[u][deg[u]] = e; deg[u]++;
        adj[v][deg[v]] = u; adje[v][deg[v]] = e; deg[v]++;
    }
}

/* Returns S (>=0) or -1 if no left-right crossing. */
static int shortest_crossing(uint32_t mask) {
    int dist[NV], q[NV], qh = 0, qt = 0;
    static const int src[4] = {0, 4, 8, 12};
    static const int tgt[4] = {3, 7, 11, 15};
    for (int i = 0; i < NV; i++) dist[i] = -1;
    for (int i = 0; i < 4; i++) {
        dist[src[i]] = 0;
        q[qt++] = src[i];
    }
    while (qh < qt) {
        int u = q[qh++];
        for (int k = 0; k < deg[u]; k++) {
            int e = adje[u][k];
            if (mask & ((uint32_t)1u << e)) {
                int w = adj[u][k];
                if (dist[w] == -1) {
                    dist[w] = dist[u] + 1;
                    q[qt++] = w;
                }
            }
        }
    }
    int best = -1;
    for (int i = 0; i < 4; i++) {
        int d = dist[tgt[i]];
        if (d != -1 && (best == -1 || d < best)) best = d;
    }
    return best;
}

int main(void) {
    build_graph();
    /* sanity: every vertex degree >= 2, total incidences = 48 */
    int tot = 0;
    for (int i = 0; i < NV; i++) tot += deg[i];
    if (tot != 2 * NE) { printf("GRAPH_ERROR tot=%d\n", tot); return 1; }

    uint64_t hist[NV + 1];
    memset(hist, 0, sizeof hist);
    uint64_t n_cross = 0, sum_S = 0;

#pragma omp parallel
    {
        uint64_t lh[NV + 1];
        uint64_t ln = 0, ls = 0;
        memset(lh, 0, sizeof lh);
#pragma omp for schedule(static) nowait
        for (uint32_t m = 0; m < NCONF; m++) {
            int s = shortest_crossing(m);
            if (s >= 0) {
                ln++;
                ls += (uint64_t)s;
                lh[s]++;
            }
        }
#pragma omp critical
        {
            n_cross += ln;
            sum_S += ls;
            for (int i = 0; i <= NV; i++) hist[i] += lh[i];
        }
    }

    uint64_t check = 0;
    for (int i = 0; i <= NV; i++) check += hist[i];
    printf("total_configs=%u\n", NCONF);
    printf("n_cross=%llu\n", (unsigned long long)n_cross);
    printf("n_nocross=%llu\n", (unsigned long long)(NCONF - n_cross));
    printf("sum_S=%llu\n", (unsigned long long)sum_S);
    printf("hist_check=%llu\n", (unsigned long long)check);
    for (int i = 0; i <= NV; i++)
        if (hist[i]) printf("N[S=%d]=%llu\n", i, (unsigned long long)hist[i]);
    /* Exact comparison: mean >= 3.6=18/5  <=>  5*sum_S >= 18*n_cross */
    __uint128_t L = (__uint128_t)5 * sum_S;
    __uint128_t R = (__uint128_t)18 * n_cross;
    printf("five_sum=%llu\n", (unsigned long long)L);
    printf("eighteen_ncross=%llu\n", (unsigned long long)R);
    if (L >= R) printf("VERDICT=MEAN_GE_3.6_HOLDS\n");
    else printf("VERDICT=MEAN_LT_3.6_DISPROVED\n");
    /* print exact mean as high-precision decimal via integer division */
    __uint128_t rem = sum_S;
    uint64_t ip = (uint64_t)(rem / n_cross);
    printf("mean_integer_part=%llu\n", (unsigned long long)ip);
    printf("mean_decimal_digits=");
    rem = rem % n_cross;
    for (int i = 0; i < 20; i++) {
        rem *= 10;
        int d = (int)(rem / n_cross);
        printf("%d", d);
        rem = rem % n_cross;
    }
    printf("\n");
    return 0;
}
