// ext9.c v1.0 — UNSAT certificate for F_9^(3,4) by extension over the K8 census.
// For each of the 17640 K8 models (hex mask, edge-lex bits) and each of the 9
// choices of deleted vertex, the induced 8-edge-set pattern is fixed; test all
// 2^8 completions of the 8 star edges. Every completion contains a red K3 or
// blue K4. Usage: ./ext9 models8.txt
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define N 9
static int Eidx[16][16], E_[64][2], m;
static int R_[16][16];

static int bad9(void) {
    int a, b, c, d, i, j;
    for (a = 0; a < N; a++) for (b = a + 1; b < N; b++) for (c = b + 1; c < N; c++)
        if (R_[a][b] == 1 && R_[a][c] == 1 && R_[b][c] == 1) return 1;
    int q[4];
    for (q[0] = 0; q[0] < N; q[0]++) for (q[1] = q[0]+1; q[1] < N; q[1]++)
        for (q[2] = q[1]+1; q[2] < N; q[2]++) for (q[3] = q[2]+1; q[3] < N; q[3]++) {
            int all0 = 1;
            for (i = 0; i < 4; i++) for (j = i + 1; j < 4; j++)
                if (R_[q[i]][q[j]] != 0) { all0 = 0; break; }
            if (all0) return 2;
        }
    return 0;
}

int main(int argc, char **argv) {
    int i, j, e;
    m = 0;
    for (i = 0; i < N; i++) for (j = i + 1; j < N; j++) { E_[m][0] = i; E_[m][1] = j; Eidx[i][j] = m++; }
    FILE *f = fopen(argv[1], "r");
    if (!f) return 1;
    char line[64];
    long long tested = 0, ok8 = 0, nm = 0;
    while (fgets(line, sizeof line, f)) {
        unsigned mask = (unsigned)strtoul(line, NULL, 16);
        nm++;
        // K8 edge-lex order on vertices 0..7 of the model; embed into K9 minus vertex del
        for (int del = 0; del < 9; del++) {
            // map model vertices 0..7 -> K9 vertices skipping del
            int mp[8], k = 0;
            for (i = 0; i < N; i++) if (i != del) mp[k++] = i;
            // base coloring of K9 minus star of del
            for (i = 0; i < N; i++) for (j = 0; j < N; j++) R_[i][j] = -1;
            int e8 = 0;
            for (i = 0; i < 8; i++) for (j = i + 1; j < 8; j++) {
                int v = (mask >> e8) & 1u; e8++;
                R_[mp[i]][mp[j]] = R_[mp[j]][mp[i]] = v;
            }
            // star edges: del-w for w != del (8 edges)
            int star[8], t = 0;
            for (i = 0; i < N; i++) if (i != del) star[t++] = i;
            for (int pat = 0; pat < 256; pat++) {
                for (t = 0; t < 8; t++) { int v = (pat >> t) & 1; R_[del][star[t]] = R_[star[t]][del] = v; }
                tested++;
                if (!bad9()) { printf("COUNTEREXAMPLE model#%lld del=%d pat=%d\n", nm, del, pat); return 2; }
            }
            ok8++;
        }
    }
    printf("models=%lld restricted=%lld completions=%lld all_blocked=1\n", nm, ok8, tested);
    return 0;
}
