/* Exhaustive zero-sum-free multiset enumeration for G = Z3 x Z3 x Z6.
 *
 * Theorem certified: no zero-sum-free multiset (hence no sequence) of length 10
 * exists over G, so D(G) <= 10. With the length-9 witness this gives D(G)=10.
 *
 * Method: depth-first search over sorted (nondecreasing) index sequences.
 *  - Elements indexed 0..53 as (a*3+b)*6+c, index 0 = zero.
 *  - Only nonzero elements are used (zero alone is a zero-sum).
 *  - Sorted order breaks all n! permutation symmetry: every multiset appears
 *    exactly once; zero-sum property is order-independent, so completeness over
 *    multisets implies completeness over sequences.
 *  - Pruning: maintain the set of achievable nonempty-free subsums as a 54-bit
 *    mask (bit k = subsum value k achievable, including empty 0). A prefix is
 *    zero-sum-free by invariant. Extending by g creates a zero-sum iff (-g) is
 *    already achievable (new zero-sums must use g). Pruned branches all contain
 *    the same witness zero-sum, so pruning is safe (no zero-sum-free extension
 *    is ever discarded).
 *  - Deterministic, single-threaded, no randomness, no external solver.
 *  - 64-bit mask suffices (54 bits, max shift 53).
 *
 * Compile: gcc -O2 -o enumerate enumerate.c
 * Run: ./enumerate [time_limit_seconds]
 * Expected: depth-10 count 0, COMPLETE, ~84.9M nodes in a few seconds.
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <time.h>

static int addtab[54][54];
static int negtab[54];
static int elem_a[54], elem_b[54], elem_c[54];
static int is_zero_idx;
static long long nodes_by_depth[12];
static long long found10 = 0;
static int found_example[10];
static long long node_count = 0;
static time_t t0;
static int TIME_LIMIT = 600;

static inline uint64_t extend_mask(uint64_t mask, int gi) {
    uint64_t nmask = mask;
    uint64_t m = mask;
    while (m) {
        int s = __builtin_ctzll(m);
        m &= m - 1;
        nmask |= (1ULL << addtab[s][gi]);
    }
    return nmask;
}

static void dfs(int min_idx, uint64_t mask, int depth, int *seq) {
    if (found10) return;
    node_count++;
    if (depth == 10) {
        found10 = 1;
        memcpy(found_example, seq, 10 * sizeof(int));
        return;
    }
    for (int gi = min_idx; gi < 54; gi++) {
        if (gi == is_zero_idx) continue;
        if (mask & (1ULL << negtab[gi])) continue; /* would create zero-sum */
        uint64_t nmask = extend_mask(mask, gi);
        seq[depth] = gi;
        nodes_by_depth[depth + 1]++;
        dfs(gi, nmask, depth + 1, seq);
        if (found10) return;
        if ((node_count & 0xFFFFFF) == 0) {
            if (time(0) - t0 > TIME_LIMIT) return;
        }
    }
}

int main(int argc, char **argv) {
    if (argc > 1) TIME_LIMIT = atoi(argv[1]);
    for (int a = 0; a < 3; a++) for (int b = 0; b < 3; b++) for (int c = 0; c < 6; c++) {
        int i = (a * 3 + b) * 6 + c;
        elem_a[i] = a; elem_b[i] = b; elem_c[i] = c;
    }
    is_zero_idx = 0; /* (0,0,0) */
    for (int i = 0; i < 54; i++) {
        int a = elem_a[i], b = elem_b[i], c = elem_c[i];
        int na = (3 - a) % 3, nb = (3 - b) % 3, nc = (6 - c) % 6;
        negtab[i] = (na * 3 + nb) * 6 + nc;
        for (int j = 0; j < 54; j++) {
            int a2 = elem_a[j], b2 = elem_b[j], c2 = elem_c[j];
            int s = (a + a2) % 3, t = (b + b2) % 3, u = (c + c2) % 6;
            addtab[i][j] = (s * 3 + t) * 6 + u;
        }
    }
    t0 = time(0);
    memset(nodes_by_depth, 0, sizeof(nodes_by_depth));
    nodes_by_depth[0] = 1;
    int seq[10];
    uint64_t init = (1ULL << is_zero_idx);
    dfs(1, init, 0, seq); /* min_idx=1 skips zero element */
    long elapsed = (long)(time(0) - t0);
    printf("nodes=%lld time=%ld\n", node_count, elapsed);
    for (int d = 0; d <= 10; d++) printf("depth %d: %lld\n", d, nodes_by_depth[d]);
    if (found10) {
        printf("FOUND length-10 zero-sum-free: ");
        for (int i = 0; i < 10; i++) {
            int g = found_example[i];
            printf("(%d,%d,%d) ", elem_a[g], elem_b[g], elem_c[g]);
        }
        printf("\n");
        return 10;
    } else {
        if (elapsed > TIME_LIMIT)
            printf("NO length-10 found (TIMEOUT-INCOMPLETE)\n");
        else
            printf("NO length-10 found (COMPLETE)\n");
        return 0;
    }
}
