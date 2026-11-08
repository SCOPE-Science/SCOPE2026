# A sharp thirteen-vertex reversal between random-edge and random-vertex greedy matching on trees

## Finding

Let \(T=(J\sqcup D,E)\) be a finite unweighted tree with one of its two bipartition classes designated as the **job side** \(J\). The *random-edge* algorithm processes a uniform random permutation of \(E\), selecting an edge whenever neither endpoint has been matched. The *random-vertex* algorithm processes a uniform random permutation of \(J\), matching each job, if possible, to a uniformly random currently unmatched neighbor in \(D\). Write \(M_E(T,J)\) and \(M_V(T,J)\) for their respective final numbers of selected edges.

**Sharp minimum-order comparison.** For every tree on at most twelve vertices and every choice of its job side,
\[
\mathbb E[M_V(T,J)]\ge\mathbb E[M_E(T,J)].
\]
Among trees on thirteen vertices, exactly one **oriented bipartite-tree isomorphism class** violates this inequality: the four-armed spider with all arms of length three, with the central vertex and all four vertices at distance two designated as jobs. Here
\[
\mathbb E[M_V]=\frac{399}{80},\qquad
\mathbb E[M_E]=\frac{404}{81},\qquad
\mathbb E[M_E]-\mathbb E[M_V]=\frac1{6480}.
\]
The finite minimum-order and uniqueness assertions are certified by the complete exact-rational enumeration in `verify.py`.

**Infinite family and stochastic order.** For every integer \(m\ge1\), let \(T_m\) be the spider with \(m\) disjoint three-edge arms \(c-a_i-b_i-d_i\), and put \(J=\{c,b_1,\ldots,b_m\}\), \(D=\{a_1,d_1,\ldots,a_m,d_m\}\). Both algorithms produce only matchings of sizes \(m\) and \(m+1\), with exact failure probabilities
\[
\Pr(M_V(T_m,J)=m)=\frac1{(m+1)2^m},\qquad
\Pr(M_E(T_m,J)=m)=\frac1{3^m}.
\]
Consequently random-vertex strictly first-order stochastically dominates random-edge when \(1\le m\le3\), whereas random-edge strictly first-order stochastically dominates random-vertex for **all** \(m\ge4\). In particular,
\[
\mathbb E[M_E(T_m,J)]-\mathbb E[M_V(T_m,J)]
=\frac1{(m+1)2^m}-\frac1{3^m}>0\quad(m\ge4).
\]

## Assumptions and scope

All graphs are finite, simple, unweighted trees. Edge priorities are uniformly random without replacement; job priorities are uniformly random without replacement, and every job's neighbor choice is uniform among its currently free neighbors. The job side is an input, not automatically the smaller or larger bipartition class. All comparisons refer to the number of matched edges, not algorithm runtime. Distinct graph labels do not affect the laws. For the first-order stochastic statement, strictness means a strict tail-probability inequality at the nontrivial threshold.

## Proof

**1. Exact stochastic laws on the spider family.** Each \(b_i\) has the private leaf \(d_i\), so every maximal matching (and hence every random-edge output) matches \(b_i\). The random-vertex process also always matches every \(b_i\), since \(d_i\) is available whenever \(b_i\) is processed. Thus the only possible unmatched job is the center \(c\), and the output size is \(m\) if \(c\) is unmatched and \(m+1\) otherwise.

For random-vertex, the center can be unmatched only if all \(m\) arm jobs are processed before it. That event has probability \(1/(m+1)\). Conditional on that order event, each \(b_i\) independently chooses \(a_i\) rather than \(d_i\) with probability \(1/2\). If the center is not last, an unprocessed \(b_i\) leaves its corresponding \(a_i\) free when the center is processed. This establishes \(\Pr(M_V=m)=1/((m+1)2^m)\).

For random-edge, assign independent continuous uniform priorities to the three edges in each arm, processing all edges in increasing priority order. The center remains unmatched **if and only if**, in every arm, the middle edge \(a_i b_i\) has the smallest priority of that arm's three edges. Sufficiency follows since each such middle edge is accepted and occupies its center-adjacent vertex \(a_i\). For necessity, if the first edge of an arm is \(ca_i\), the center is matched there unless it has already been matched elsewhere; if the first is \(b_i d_i\), then \(a_i\) remains free and the edge \(ca_i\) is eventually accepted unless the center is matched elsewhere. The probability of the middle edge being first in each arm is \(1/3\), independently across arms, proving \(\Pr(M_E=m)=3^{-m}\).

The strict stochastic comparison is equivalent to \((3/2)^m>m+1\). It fails for \(m=1,2,3\), holds at \(m=4\), and thereafter holds by induction, since \(\tfrac32(m+1)>m+2\) for \(m>1\). The stated exact gap at \(m=4\) follows by subtraction.

**2. Exhaustive minimum-order certificate.** For a residual bipartite graph \(H=(J_H\sqcup D_H,E_H)\), let \(V(H)\) and \(R(H)\) denote expected final matching sizes under the two algorithms. Isolated jobs can be deleted without changing either expectation: deleting them preserves the uniform relative order of all still relevant jobs. After that deletion, if \(E_H\ne\varnothing\), exact first-step conditioning gives
\[
R(H)=\frac1{|E_H|}\sum_{jd\in E_H}\bigl(1+R(H-\{j,d\})\bigr),
\]
\[
V(H)=\frac1{|J_H|}\sum_{j\in J_H}\frac1{\deg_H(j)}
 \sum_{d\in N_H(j)}\bigl(1+V(H-\{j,d\})\bigr).
\]
The expectations vanish on edgeless graphs. These are terminating recurrences with positive integer denominators and are evaluated using exact rational arithmetic.

The standalone certificate builds all unlabeled trees recursively: from every representative on \(n-1\) vertices it attaches one new leaf at each vertex and deduplicates using the canonical parenthesis encoding of recursively sorted rooted subtrees at the one or two tree centers. This is exhaustive by induction: deleting any leaf from a tree of order \(n\) yields a tree of order \(n-1\). The canonical encoding classifies unrooted trees because the center is invariant and rooted subtrees are classified recursively by the sorted multiset of their child encodings. Both bipartition orientations of every representative are then evaluated by the rational recurrences above. The resulting counts are:

| Vertices | Unlabeled trees | Orientations with \(\mathbb E[M_E]>\mathbb E[M_V]\) |
|---:|---:|---:|
| 1–3 | 1 each | 0 each |
| 4 | 2 | 0 |
| 5 | 3 | 0 |
| 6 | 6 | 0 |
| 7 | 11 | 0 |
| 8 | 23 | 0 |
| 9 | 47 | 0 |
| 10 | 106 | 0 |
| 11 | 235 | 0 |
| 12 | 551 | 0 |
| 13 | 1301 | 1 |

The sole positive thirteen-vertex orientation has gap \(1/6480\), and its graph is isomorphic to \(T_4\) with the job side specified above. This proves the sharp minimum-order statement and uniqueness subject only to the elementary enumeration and recurrence algorithms provided verbatim in `verify.py`.

## Verification

Run `python3 verify.py` with a standard Python 3 interpreter; no third-party packages are required. The checker reconstructs every unlabeled tree through thirteen vertices from leaf extensions, verifies the known exact tree counts, visits both bipartition orientations, calculates both expectations using `fractions.Fraction`, asserts a unique first counterexample and its exact values, and compares the spider formulas with exact dynamic programming for \(1\le m\le6\). Independent direct enumeration of all edge priority orders for \(m\le3\) and all job/local-neighbor priority orders for \(m\le4\) also confirms the failure probabilities. The census covers 4,576 oriented-tree instances through thirteen vertices. Separate cross-checking against an independent nonisomorphic-tree generator reproduced all 1,301 isomorphism types at order thirteen, but that optional external comparison is not needed to run the packaged certificate.

## Relationship to prior work

Arnosti's *Greedy Matching in Bipartite Random Graphs* (publicly online November 2, 2021) precisely distinguishes random-edge and job-side random-vertex procedures. Its Theorem 1 shows random-vertex stochastic domination **after averaging the edge set** over random bipartite graphs with fixed job-degree sequence. Its Figure 1 contains individual deterministic graphs where this order reverses, including an eight-vertex example with cycles. Neither an averaged comparison nor a cyclic counterexample determines the first fixed-tree reversal or the exact two-point distributions here.

Dyer and Frieze study random-edge matching, and Dyer, Frieze, and Pittel analyze average performance on random labeled trees; an average-over-trees comparison does not exclude exceptional fixed trees. Aronson and collaborators analyze a vertex-selection algorithm on general graphs with both sides eligible for selection; that differs from the designated-job-side process in this theorem. Closely related publications were compared using their accessible descriptions; not every older full text could be inspected.

## Limitations

The sharp order-thirteen classification is computationally exhaustive and depends on the correctness of the short, supplied tree generator and exact recursion implementation; it is not a purely analytic classification of arbitrary trees. The infinite family is proved analytically, without extrapolation from finite computation. The tree threshold concerns the one-sided random-vertex procedure, not the variant that samples unmatched vertices from both bipartition classes, nor weighted or capacitated matching. Historical priority remains subject to further checking of inaccessible older full texts. No independent mathematical audit is claimed.

## References

1. N. Arnosti, *Greedy Matching in Bipartite Random Graphs*, Stochastic Systems 12 (2022), 133–150; first published online 2021-11-02. DOI: https://doi.org/10.1287/stsy.2021.0082 . Author-hosted April 2021 version: https://nickarnosti.com/ResearchPapers/Arnosti_GreedyMatching.pdf .
2. M. Dyer and A. Frieze, *Randomized greedy matching*, Random Structures & Algorithms 2 (1991), 29–45. DOI: https://doi.org/10.1002/rsa.3240020104 .
3. M. Dyer, A. Frieze, and B. Pittel, *The average performance of the greedy matching algorithm*, Annals of Applied Probability 3 (1993), 526–552. DOI: https://doi.org/10.1214/aoap/1177005436 .
4. J. Aronson, M. Dyer, A. Frieze, and S. Suen, *Randomized greedy matching. II*, Random Structures & Algorithms 6 (1995), 55–73. DOI: https://doi.org/10.1002/rsa.3240060107 .
5. Z. G. Tang, X. Wu, and Y. Zhang, *Toward a Better Understanding of Randomized Greedy Matching*, Journal of the ACM 70 (2023), article 39. DOI: https://doi.org/10.1145/3614318 .
