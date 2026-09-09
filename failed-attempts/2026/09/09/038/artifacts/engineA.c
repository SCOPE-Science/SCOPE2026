/* Engine A: insert-max generation of Av(1324) with inversion distribution.
 *
 * Theory (exact): child of pi (|pi|=m, avoids 1324) formed by inserting new
 * maximum M=m+1 at position p is a 1324-avoider iff the length-p prefix
 * avoids 132 (any 1324-occurrence using M has M as the '4', hence last, so
 * the 132-part lies fully in the prefix; occurrences not using M live in
 * the avoiding parent). Deleting the max inverts the step, so every avoider
 * is reached exactly once. inv(child)=inv(parent)+(m-p) (M exceeds the
 * m-p entries after it).
 */
#include <stdio.h>
#include <string.h>

static long long cnt[13][80];
static int a[16];

/* does a[0..p-1] avoid 132? */
static int prefix_avoids_132(int p) {
    for (int i = 0; i < p; i++)
        for (int j = i + 1; j < p; j++)
            for (int k = j + 1; k < p; k++)
                if (a[i] < a[k] && a[k] < a[j]) return 0;
    return 1;
}

static void dfs(int m, int inv) {
    cnt[m][inv]++;
    if (m == 12) return;
    for (int p = 0; p <= m; p++) {
        if (!prefix_avoids_132(p)) continue;
        /* insert M = m+1 at position p */
        memmove(&a[p + 1], &a[p], (size_t)(m - p) * sizeof(int));
        a[p] = m + 1;
        dfs(m + 1, inv + (m - p));
        memmove(&a[p], &a[p + 1], (size_t)(m - p) * sizeof(int));
    }
}

int main(void) {
    memset(cnt, 0, sizeof cnt);
    dfs(0, 0);
    for (int n = 1; n <= 12; n++) {
        long long tot = 0;
        int kmax = 0;
        for (int k = 0; k < 80; k++) { tot += cnt[n][k]; if (cnt[n][k]) kmax = k; }
        printf("n=%d total=%lld kmax=%d\n", n, tot, kmax);
        printf("row:");
        for (int k = 0; k <= kmax; k++) printf(" %lld", cnt[n][k]);
        printf("\n");
    }
    return 0;
}
