// enum8b.c v1.0 — INDEPENDENT second enumerator for (3,4)-free colorings of K8.
// Differences from enum8.c: edges processed in REVERSE lexicographic order,
// blue tried before red, violation test by direct scan of all triples/quads
// containing the new edge (no precomputed Tby/Qby tables), models printed
// as hex of mask in standard edge-lex bit order (same format as enum8.c).
#include <stdio.h>
#include <stdlib.h>

static int n = 8, E_[64][2], Eidx[16][16], m;
static int R_[16][16]; // -1 unset, 1 red, 0 blue
static long long nodes = 0, models = 0;

static int viol(int u, int v, int red) {
    int w, x, y;
    if (red) {
        for (w = 0; w < n; w++) {
            if (w == u || w == v) continue;
            int a = u < w ? R_[u][w] : R_[w][u];
            int b = v < w ? R_[v][w] : R_[w][v];
            if (a == 1 && b == 1) return 1;
        }
    } else {
        // any blue K4 containing edge (u,v)? need w<x both blue-adjacent to u,v and blue edge w-x
        for (w = 0; w < n; w++) {
            if (w == u || w == v) continue;
            int a = u < w ? R_[u][w] : R_[w][u];
            int b = v < w ? R_[v][w] : R_[w][v];
            if (a != 0 || b != 0) continue;
            for (x = w + 1; x < n; x++) {
                if (x == u || x == v) continue;
                int c = u < x ? R_[u][x] : R_[x][u];
                int d = v < x ? R_[v][x] : R_[x][v];
                if (c != 0 || d != 0) continue;
                int e2 = w < x ? R_[w][x] : R_[x][w];
                if (e2 == 0) return 1;
            }
        }
    }
    return 0;
}

static int order_[64];

static void dfs(int d) {
    nodes++;
    if (d == m) {
        unsigned mask = 0;
        for (int i = 0; i < m; i++) {
            int u = E_[i][0], v = E_[i][1];
            if (R_[u][v] == 1) mask |= (1u << i);
        }
        printf("%07x\n", mask);
        models++;
        return;
    }
    int e = order_[d], u = E_[e][0], v = E_[e][1];
    R_[u][v] = R_[v][u] = 0;           // blue first
    if (!viol(u, v, 0)) dfs(d + 1);
    R_[u][v] = R_[v][u] = 1;           // then red
    if (!viol(u, v, 1)) dfs(d + 1);
    R_[u][v] = R_[v][u] = -1;
}

int main(void) {
    int i, j;
    m = 0;
    for (i = 0; i < n; i++) for (j = i + 1; j < n; j++) { E_[m][0] = i; E_[m][1] = j; Eidx[i][j] = m++; }
    for (i = 0; i < n; i++) for (j = 0; j < n; j++) R_[i][j] = -1;
    for (i = 0; i < m; i++) order_[i] = m - 1 - i; // reverse order
    dfs(0);
    fprintf(stderr, "nodes=%lld models=%lld\n", nodes, models);
    return 0;
}
