// Exhaustive Ingleton-deficit scanner for sparse-paving matroids.
// Ingleton (matroid form, Ingleton 1971):
//   D(A,B,C,D) = r(A)+r(B)+r(AUBUC)+r(AUBUD)+r(CUD)
//              - r(AUB)-r(AUC)-r(AUD)-r(BUC)-r(BUD)
// Violation iff D > 0. Reports max D over ALL ordered 4-tuples of subsets
// (full (2^n)^4 enumeration, OpenMP-parallelized), one attaining witness,
// the count of strictly-positive tuples, and the witness rank table.
// Rank function (sparse paving, rank k, nonbases = circuit-hyperplanes):
//   r(X) = min(|X|,k), except r(X) = k-1 when X is a listed nonbasis
//   (|X| = k and X in family). Sets larger than k have rank k.
// Usage: ingleton <k> <n> <nb1> <nb2> ...   (nonbasis masks in hex)
// Compile: gcc -O2 -fopenmp -o ingleton ingleton_scan.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static int *popc, *rankv;
static int N, K, NSUB;

int main(int argc, char **argv) {
  if (argc < 3) { printf("usage: ingleton <rank-k> <n-elts> [nonbasis-hex...]\n"); return 1; }
  K = atoi(argv[1]); N = atoi(argv[2]); NSUB = 1 << N;
  popc = malloc(sizeof(int) * NSUB); rankv = malloc(sizeof(int) * NSUB);
  for (int m = 0; m < NSUB; m++) popc[m] = __builtin_popcount((unsigned)m);
  char *isNB = calloc(NSUB, 1);
  for (int i = 3; i < argc; i++) {
    long m = strtol(argv[i], 0, 16);
    if (m >= 0 && m < NSUB) isNB[m] = 1;
  }
  for (int m = 0; m < NSUB; m++) {
    int s = popc[m];
    if (s < K) rankv[m] = s;
    else if (s == K) rankv[m] = isNB[m] ? K - 1 : K;
    else rankv[m] = K;
  }
  int best = -99, bA = 0, bB = 0, bC = 0, bD = 0;
  long long npos = 0;
#pragma omp parallel for schedule(static) reduction(max:best) reduction(+:npos) \
    shared(bA, bB, bC, bD)
  for (int A = 0; A < NSUB; A++) {
    for (int B = 0; B < NSUB; B++) {
      int AB = A | B, rAB = rankv[AB], rA = rankv[A], rB = rankv[B];
      for (int C = 0; C < NSUB; C++) {
        int ABC = AB | C, rABC = rankv[ABC];
        int rAC = rankv[A | C], rBC = rankv[B | C];
        for (int D = 0; D < NSUB; D++) {
          int ABD = AB | D, CD = C | D;
          int v = rA + rB + rABC + rankv[ABD] + rankv[CD]
                - rAB - rAC - rankv[A | D] - rBC - rankv[B | D];
          if (v > 0) npos++;
          if (v > best) {
#pragma omp critical
            { if (v > best) { best = v; bA = A; bB = B; bC = C; bD = D; } }
          }
        }
      }
    }
  }
  int A = bA, B = bB, C = bC, D = bD;
  printf("k=%d n=%d best=%d npos=%lld A=%#x B=%#x C=%#x D=%#x\n",
         K, N, best, npos, A, B, C, D);
  printf("LHS ranks: rA=%d rB=%d rABC=%d rABD=%d rCD=%d\n",
         rankv[A], rankv[B], rankv[A | B | C], rankv[A | B | D], rankv[C | D]);
  printf("RHS ranks: rAB=%d rAC=%d rAD=%d rBC=%d rBD=%d\n",
         rankv[A | B], rankv[A | C], rankv[A | D], rankv[B | C], rankv[B | D]);
  printf("sizes: |A|=%d |B|=%d |C|=%d |D|=%d |AB|=%d |AC|=%d |AD|=%d |BC|=%d |BD|=%d |CD|=%d |ABC|=%d |ABD|=%d\n",
         popc[A], popc[B], popc[C], popc[D], popc[A | B], popc[A | C],
         popc[A | D], popc[B | C], popc[B | D], popc[C | D],
         popc[A | B | C], popc[A | B | D]);
  free(popc); free(rankv); free(isNB);
  return 0;
}
