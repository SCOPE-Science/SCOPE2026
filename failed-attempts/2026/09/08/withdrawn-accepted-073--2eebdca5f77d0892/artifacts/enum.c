/* enum.c — substitution-type census of Av_n(pi), single length-4 pattern pi.
 * Usage: ./enum <pattern e.g. 1324> <outdir>
 * Loops n=8..11, backtracking with incremental avoidance pruning.
 * Classifies each avoider: simple | sum-decomposable | skew-decomposable |
 * inflation of simple quotient (min #blocks over interval partitions).
 * Writes <outdir>/results_<pi>.json, witnesses, and verifiable samples.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

static int pi4[4];
static int n;
static int p[12];
static int used[14];
static long long total, c_simple, c_sum, c_skew, c_infl, anomalies;
static long long qhist[13];
static int wit[12], wit_saved;
static FILE *fsamp;
static long long n_samp_simple, n_samp_other;
static const long long QUOTA_SIMPLE = 25, QUOTA_OTHER = 10;

static inline int match4(int a, int b, int c, int d) {
    int v[4] = {a, b, c, d};
    int r[4];
    for (int i = 0; i < 4; i++) {
        int rk = 1;
        for (int j = 0; j < 4; j++) if (v[j] < v[i]) rk++;
        r[i] = rk;
    }
    return r[0]==pi4[0] && r[1]==pi4[1] && r[2]==pi4[2] && r[3]==pi4[3];
}

/* check quotient q[0..k-1] (a permutation of 1..k) is simple */
static int qis_simple(int *q, int k) {
    for (int i = 0; i < k; i++) {
        int a = q[i], b = q[i];
        for (int j = i+1; j < k; j++) {
            if (q[j] < a) a = q[j];
            if (q[j] > b) b = q[j];
            if (b - a == j - i) {
                if (!(i == 0 && j == k-1)) return 0;
            }
        }
    }
    return 1;
}

static void save_sample(const char *type, int qlen) {
    char fname[256];
    (void)fname;
    fprintf(fsamp, "%d", p[0]);
    for (int i = 1; i < n; i++) fprintf(fsamp, " %d", p[i]);
    fprintf(fsamp, " | %s %d\n", type, qlen);
}

static void classify(void) {
    total++;
    int i, j;
    int mx = 0, mn = n + 1, is_sum = 0, is_skew = 0;
    for (int k = 0; k < n - 1; k++) {
        if (p[k] > mx) mx = p[k];
        if (p[k] < mn) mn = p[k];
        if (mx == k + 1) is_sum = 1;
        if (mn == n - k) is_skew = 1;
    }
    int simple = 1;
    for (i = 0; i < n && simple; i++) {
        int a = p[i], b = p[i];
        for (j = i + 1; j < n; j++) {
            if (p[j] < a) a = p[j];
            if (p[j] > b) b = p[j];
            if (b - a == j - i) {
                if (!(i == 0 && j == n - 1)) { simple = 0; break; }
            }
        }
    }
    if (simple) {
        c_simple++;
        if (!wit_saved) { memcpy(wit, p, sizeof(int)*n); wit_saved = 1; }
        if (n_samp_simple < QUOTA_SIMPLE) { save_sample("simple", 0); n_samp_simple++; }
        return;
    }
    if (is_sum) {
        c_sum++;
        if (n_samp_other < QUOTA_OTHER) { save_sample("sum", 0); n_samp_other++; }
        /* note: counter shared across types below; use total-sample cap instead */
        return;
    }
    if (is_skew) {
        c_skew++;
        if (n_samp_other < QUOTA_OTHER*2) { save_sample("skew", 0); n_samp_other++; }
        return;
    }
    /* inflation: min #blocks over cut masks with all blocks intervals */
    int best = n, bestmask = (1 << (n - 1)) - 1;
    for (int mask = 1; mask < (1 << (n - 1)); mask++) {
        int a = 0, ok = 1, nb = 0;
        for (int k = 0; k < n - 1; k++) {
            if (mask & (1 << k)) {
                int x = p[a], y = p[a];
                for (int t = a + 1; t <= k; t++) {
                    if (p[t] < x) x = p[t];
                    if (p[t] > y) y = p[t];
                }
                if (y - x != k - a) { ok = 0; break; }
                nb++; a = k + 1;
            }
        }
        if (!ok) continue;
        {
            int x = p[a], y = p[a];
            for (int t = a + 1; t < n; t++) {
                if (p[t] < x) x = p[t];
                if (p[t] > y) y = p[t];
            }
            if (y - x != n - 1 - a) continue;
            nb++;
        }
        if (nb < best) { best = nb; bestmask = mask; }
    }
    /* verify quotient is simple of length >= 4 */
    {
        int bs[12], bmn[12], bmx[12], nb = 0, a = 0;
        for (int k = 0; k < n - 1; k++) {
            if (bestmask & (1 << k)) {
                int x = p[a], y = p[a];
                for (int t = a + 1; t <= k; t++) {
                    if (p[t] < x) x = p[t];
                    if (p[t] > y) y = p[t];
                }
                bmn[nb] = x; bmx[nb] = y; nb++; a = k + 1;
            }
        }
        {
            int x = p[a], y = p[a];
            for (int t = a + 1; t < n; t++) {
                if (p[t] < x) x = p[t];
                if (p[t] > y) y = p[t];
            }
            bmn[nb] = x; bmx[nb] = y; nb++;
        }
        int q[12];
        for (int u = 0; u < nb; u++) {
            int rk = 1;
            for (int v = 0; v < nb; v++) if (bmn[v] < bmn[u]) rk++;
            q[u] = rk;
        }
        if (nb != best || best < 4 || !qis_simple(q, nb)) anomalies++;
        (void)bs;
    }
    qhist[best]++;
    c_infl++;
    if (n_samp_other < QUOTA_OTHER*3) { save_sample("inflation", best); n_samp_other++; }
}

static void dfs(int pos) {
    if (pos == n) { classify(); return; }
    for (int v = 1; v <= n; v++) {
        if (used[v]) continue;
        p[pos] = v; used[v] = 1;
        int bad = 0;
        for (int i = 0; i < pos && !bad; i++)
            for (int j = i + 1; j < pos && !bad; j++)
                for (int k = j + 1; k < pos && !bad; k++)
                    if (match4(p[i], p[j], p[k], v)) bad = 1;
        if (!bad) dfs(pos + 1);
        used[v] = 0;
    }
}

int main(int argc, char **argv) {
    if (argc != 3) { fprintf(stderr, "usage: enum PATTERN OUTDIR\n"); return 2; }
    const char *pat = argv[1], *outdir = argv[2];
    if (strlen(pat) != 4) return 2;
    for (int i = 0; i < 4; i++) pi4[i] = pat[i] - '0';
    char respath[256], witpath[256], sampath[256];
    snprintf(respath, sizeof respath, "%s/results_%s.json", outdir, pat);
    snprintf(witpath, sizeof witpath, "%s/witnesses_%s.txt", outdir, pat);
    FILE *fr = fopen(respath, "w");
    FILE *fw = fopen(witpath, "w");
    if (!fr || !fw) { perror("fopen"); return 1; }
    fprintf(fr, "{\"pattern\": \"%s\", \"cells\": [\n", pat);
    for (int nn = 8; nn <= 11; nn++) {
        n = nn;
        total = c_simple = c_sum = c_skew = c_infl = anomalies = 0;
        n_samp_simple = n_samp_other = 0;
        wit_saved = 0;
        memset(qhist, 0, sizeof qhist);
        memset(used, 0, sizeof used);
        snprintf(sampath, sizeof sampath, "%s/samples_%s_%d.txt", outdir, pat, n);
        fsamp = fopen(sampath, "w");
        if (!fsamp) { perror("fopen samp"); return 1; }
        clock_t t0 = clock();
        dfs(0);
        clock_t t1 = clock();
        double secs = (double)(t1 - t0) / CLOCKS_PER_SEC;
        fclose(fsamp);
        fprintf(fw, "pi=%s n=%d witness_simple:", pat, n);
        for (int i = 0; i < n; i++) fprintf(fw, " %d", wit[i]);
        fprintf(fw, "\n");
        fprintf(fr, "  {\"n\": %d, \"total\": %lld, \"simple\": %lld, \"sum\": %lld,"
                    " \"skew\": %lld, \"inflation\": %lld, \"qhist\": {",
                n, total, c_simple, c_sum, c_skew, c_infl);
        int first = 1;
        for (int q = 4; q <= n; q++) if (qhist[q]) {
            fprintf(fr, "%s\"%d\": %lld", first ? "" : ", ", q, qhist[q]);
            first = 0;
        }
        fprintf(fr, "}, \"anomalies\": %lld, \"cpu_s\": %.1f}%s\n",
                anomalies, secs, nn < 11 ? "," : "");
        fflush(fr);
    }
    fprintf(fr, "]}\n");
    fclose(fr); fclose(fw);
    return 0;
}
