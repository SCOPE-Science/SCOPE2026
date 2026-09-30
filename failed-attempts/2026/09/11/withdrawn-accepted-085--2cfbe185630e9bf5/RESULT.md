# Container-count obstruction for book-free hosts at critical density

## Context and motivation

Hypergraph containers give upper bounds on families of H-free graphs by covering
them with few almost-extremal containers. At the critical density p = 1/2 for
book graphs, a recognized question in the container-versus-induction tradeoff
relevant to R(4,t) is whether containers must explode or whether a small
explicit container family could yield a new counting route. This record pins a
fixed-parameter stall point: at order n = 4096, forbidden book B_2(64), and
defect 0.02, every valid container family is exponentially large.

## Definitions

- n = 4096, N = C(n,2) = 8386560, p = 1/2.
- B = B_2(64): 64 triangles sharing one spine edge. B contains triangles, so
  every triangle-free graph is B-free.
- A container family C is a family of graphs on vertex set [n] such that
  (covering) every B-free graph on [n] is a subgraph of some member of C, and
  (defect) each C in C has at most (p + 0.02) N = 0.52 N edges.
- Edge cap: 0.52 N = 4361011.2, hence integer cap M_cap = 4361011.
- For S subset of [n] with |S| = 2048, K_S denotes the complete bipartite graph
  with bipartition (S, [n] \ S). Then e(K_S) = 2048^2 = 4194304 <= M_cap.
- Logarithms are natural; the target threshold is exp(n^1.5 / 10^4) with
  n^1.5 / 10^4 = 262144 / 10000 = 26.2144.

## Result (headline claim)

Let n = 4096, p = 1/2, B = B_2(64). Any container family C covering all B-free
graphs on [n] with at most (p + 0.02) C(n,2) edges per container satisfies
|C| >= exp(n^1.5 / 10^4).

Proved stronger bound: |C| >= 2^2837 / 4097, i.e. ln |C| >= 1958.14, hence
|C| >= e^1958 ~= 10^850, far above the e^26.2144 ~= 2.4 x 10^11 threshold
(margin about 1931.9 nats).

## Proof / evidence

Lemma 1 (test family is B-free). Each K_S is bipartite, hence triangle-free,
hence B_2(64)-free. By the covering hypothesis every K_S is a subgraph of some
container C in C.

Lemma 2 (components pin down covered cuts). Fix a container C and let M be its
complement in K_n. Then e(M) = N - e(C) >= N - 4361011 = 4025549. If K_S is a
subgraph of C, no edge of M joins S to its complement, so S is a union of
connected components of M: every cross pair of K_S lies in C, hence outside M,
so a path in M starting in S can never take a first step out of S.

Lemma 3 (dense complement has few components). M has at most r = 1259
components. Indeed, if M has r components of sizes summing to n, convexity gives
e(M) <= C(n - r + 1, 2). For r >= 1260, e(M) <= C(2837,2) = 4022866, but exact
integers give e(M) >= 4025549 > 4022866, a contradiction.

Lemma 4 (each container covers few cuts). A fixed container covers K_S for at
most 2^1258 unordered bipartitions {S, [n] \ S} with |S| = 2048: each covered S
is a union of the r <= 1259 M-components, giving at most 2^r subsets, i.e. at
most 2^{r-1} <= 2^1258 unordered pairs; the size constraint only lowers this.

Counting. Unordered balanced bipartitions number C(4096,2048)/2, and
C(2m,m) >= 4^m/(2m+1) since 2^{2m} = sum_k C(2m,k) <= (2m+1) C(2m,m), so there
are at least 2^4095/4097 graphs K_S. Double counting pairs (S, C) with
K_S subset of C gives |C| >= (2^4095/4097) / 2^1258 = 2^2837/4097. Taking logs,
ln |C| >= 2837 ln 2 - ln 4097 ~= 1958.14 > 26.2144, proving the claim with
enormous margin.

## Limitations

The proved bound is far stronger than the stated threshold and uses only that B
contains a triangle, so it does not isolate any special property of 64-page
books beyond triangle-freeness. Tightness of 2^2837/4097 and the extremal
structure of minimal container families are not addressed.

## Reproducibility

Run `python3 output/artifacts/verify.py` (stdlib only). It replays every
integer (N, cap, missing edges, clique bound C(2837,2), component bound) and
the final log comparison, printing VERIFY_OK. All key steps except the final
log comparison are exact integer arithmetic; the margin (~1931 nats) dwarfs
float error (~1e-12).

## References

- Balogh, Morris, Samotij, Independent sets in hypergraphs (container method
  foundation; general upper-bound theory).
- Saxton-Thomason / Balogh-Morris-Samotij hypergraph container lemmas.
- Balogh-Samotij, An efficient container lemma, Discrete Analysis 2020:17
  (general upper bound |G| <= n^{C n^{3/2}}; opposite direction from this
  lower bound).
- Method of hypergraph containers survey (ICM); MIT OCW 18.226 Lecture 27.
