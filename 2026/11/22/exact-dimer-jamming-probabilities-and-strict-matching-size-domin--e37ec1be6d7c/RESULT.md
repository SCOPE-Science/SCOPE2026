# Strict stochastic dominance of greedy over uniform maximal matching size on the dodecahedral graph

## Finding

On the dodecahedral graph \(D=\operatorname{GP}(10,2)\), let \(J\) be the terminal size of a random greedy matching, and let \(U\) be the size of a uniformly sampled maximal matching. There are exactly \(3781\) labeled maximal matchings of \(D\), with these size counts:

| Size \(k\) | 6 | 7 | 8 | 9 | 10 |
|---|---:|---:|---:|---:|---:|
| Number of maximal matchings | 5 | 420 | 2280 | 1040 | 36 |

The greedy size strictly first-order stochastically dominates \(U\): \(\Pr(J\le k)<\Pr(U\le k)\) at every nontrivial integer threshold \(k=6,7,8,9\). The exact gaps are

| \(k\) | \(\Pr(U\le k)-\Pr(J\le k)\) |
|---:|---:|
| 6 | \(11844/11815625\) |
| 7 | \(823100515754893/10423286874000000\) |
| 8 | \(5746573892635665283/18386678045736000000\) |
| 9 | \(405901562596287/6305445146000000\) |

A perfect matching is \(155312512865429/20011992000000\), approximately \(7.761\), times as likely under the greedy process as under uniform sampling of maximal matchings.

## Assumptions and scope

Use vertices \(u_i,v_i\) with \(i\in\mathbb Z/10\mathbb Z\) and edges \(u_iu_{i+1},u_iv_i,v_iv_{i+2}\). Each edge receives an independent priority from the same continuous distribution. Processing these edges in increasing priority, accept an edge if and only if both endpoints are still unmatched. The order is a uniform permutation of the thirty edges. The terminal matching is maximal: any rejected edge already had an occupied endpoint and cannot become available. The comparison samples each individual maximal edge set with equal weight, not each automorphism class, and not each ordering of a maximal edge set.

## Proof

**Counting maximal edge sets.** Take the first unassigned vertex in a fixed vertex order. Either declare it unmatched or pair it with one of its unassigned neighbors. Mark that vertex, and also its partner if present, as assigned, then recurse. A prescribed matching determines exactly one branch at each step, and every completed branch specifies a matching. Retain the branch precisely when the vertices declared unmatched form an independent set; this is necessary and sufficient for the matching to be maximal. Exhaustive enumeration of this recursion gives the size counts in the Finding. Dividing the counts by \(3781\) gives the distribution of \(U\).

**Kinetic input and cross-check.** The separate record *Exact random dimer-jamming law on the dodecahedral graph* [1] reports the equivalent random-priority model on \(\operatorname{GP}(10,2)\) and the following law. It is used as an input to the comparison, not claimed as a distinct contribution here.

| \(k\) | \(\Pr(J=k)\) |
|---:|---:|
| 6 | \(1/3125\) |
| 7 | \(91294494167/2756754000000\) |
| 8 | \(1796566904214749/4862914056000000\) |
| 9 | \(2544405065946811/4862914056000000\) |
| 10 | \(123231298227/1667666000000\) |

For a check using the enumeration of individual maximal matchings, write \(m(A)\) for the number of edges induced by a set \(A\) of free vertices. Conditional on an ordered accepted prefix, the still-available edges have a uniform relative order: exchanging any two of them does not affect that prefix, since they were available throughout it. Thus the next accepted edge, when one exists, is uniform on the \(m(A)\) edges. If \(q(S)\) is the probability that the first \(|S|\) accepted edges form exactly the unordered matching \(S\), partition by the last edge of the prefix to obtain
\[
q(\varnothing)=1,\qquad q(S)=\sum_{e\in S}\frac{q(S\setminus\{e\})}{m(V(D)\setminus V(S\setminus\{e\}))}.
\]
The denominator is positive because \(e\) is available. For a maximal matching \(M\), its probability of being the terminal output is \(q(M)\). Summing over the enumerated maximal matchings at each size reproduces the five kinetic fractions. Recursing directly on the remaining vertex set gives the same law: if no edge is available, the number of additional accepts is zero; otherwise choose one of the \(m(A)\) edges uniformly and remove its two vertices. This is the transfer recurrence also used in [1].

**Exact comparison.** The cumulative counts for \(U\) at \(6,7,8,9\) are respectively \(5,425,2705,3745\), each divided by \(3781\). Subtracting the corresponding cumulative probabilities of \(J\) gives the four strictly positive fractions in the Finding. The distributions coincide at the trivial thresholds below 6 and at or above 10. The perfect-matching multiplier is \(\Pr(J=10)/(36/3781)\).

## Verification

The accompanying standard-library program `verify_dodeca.py` (Python 3.10 or later) exhausts the matching recursion and checks the five size counts and all four strict inequalities by exact rational arithmetic. It also reproduces the credited greedy law both by a remaining-vertex-set recurrence and by the matching-prefix recurrence. The graph is constructed directly from the modular edge rules above. No sampling or extrapolation is used.

## Relationship to prior work

The record [1], indexed on the same date, has the same five kinetic probabilities, the associated expectation and the perfect-coverage probability, as well as a geometric proof of the rare size-six probability. The date alone gives no ordering of the two records. The contribution stated here is the census of labeled maximal matchings by size and the exact comparison of the size laws under two different measures. The minimum maximal size of six was known [2]; ordinary matching counts, including the 36 perfect matchings, do not determine all the maximal-matching multiplicities. Graph dimer adsorption and random greedy matching are established models [3,4]. The analogous comparison for the Heawood graph [5] concerns a different graph.

## Limitations

The comparison is specific to the twenty-vertex dodecahedral graph. It is not a general dominance theorem, a finite-time deposition law or a physical prediction. Dominance can fail even on a connected graph: for the edge set \(\{01,12,14,15,23,24,25\}\), exactly one of the eight maximal matchings has size one, while the greedy size-one probability is \(1/7>1/8\), because it occurs exactly when \(12\) is the first edge.

## References

1. [*Exact random dimer-jamming law on the dodecahedral graph*](https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-exact-random-dimer-jamming-law-on-the-dodecahedral-graph--8e1393873ad2), Resultary, 22 November 2026.
2. V. Andova, F. Kardoš and R. Škrekovski, *Sandwiching saturation number of fullerene graphs*, [arXiv:1405.2197](https://arxiv.org/abs/1405.2197).
3. M. D. Penrose and A. Sudbury, *Exact and approximate results for deposition and annihilation processes on graphs*, [arXiv:math/0503519](https://arxiv.org/abs/math/0503519).
4. D. Gamarnik and D. A. Goldberg, *Randomized greedy algorithms for independent sets and matchings on regular graphs: Exact results and finite girth corrections*, [arXiv:0807.1277](https://arxiv.org/abs/0807.1277).
5. [*Exact random-priority dimer jamming and matching-output weights on the Heawood graph*](https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-exact-random-priority-dimer-jamming-and-matching-output-weights--538d2c590718), Resultary, 22 November 2026.
