# Exact random-priority dimer jamming and matching-output weights on the Heawood graph

## Finding

For irreversible random-priority **dimer** adsorption on the Heawood graph \(H\), let \(J\) denote the terminal number of accepted edges. Its entire law is

\[
\Pr(J=5)=\frac{19}{330},\qquad
\Pr(J=6)=\frac{497}{792},\qquad
\Pr(J=7)=\frac{1247}{3960}.
\]

No other terminal size is possible, and \(\mathbb E J=24779/3960\). The complete output distribution has exactly five probability classes:

| Number of accepted edges | Number of maximal matching outputs | Probability of each particular output |
|---|---:|---:|
| 5 | 42 | \(19/13860\) |
| 6 | 28 | \(261/98560\) |
| 6 | 56 | \(8257/1995840\) |
| 6 | 84 | \(91723/23950080\) |
| 7 | 24 | \(1247/95040\) |

In particular, the probability of reaching a perfect matching is \(1247/3960\), whereas a uniformly selected maximal matching is perfect with probability \(24/234=4/39\). Thus random-priority adsorption amplifies the perfect-output probability by the exact factor \(16211/5280\).

## Assumptions and scope

Label the seven Fano-plane points by \(0,1,\ldots,6\), and the seven lines in the following order:

```
(0,1,3), (0,2,5), (0,4,6), (1,2,6),
(1,4,5), (2,3,4), (3,5,6).
```

The Heawood graph is bipartite, with point vertices \(0,\ldots,6\) and line vertices \(7,\ldots,13\). There is an edge \((i,7+j)\) precisely when point \(i\) lies on line \(j\), giving twenty-one edges. The list meets the Fano axioms: each point is on three lines and each unordered pair of points lies on a unique line. Independent continuous priorities are placed on **edges** (not vertices). Each edge is accepted in ascending priority order exactly when both endpoints are still unmatched. The terminal accepted edge set is a maximal matching. The probability measure is the pushforward of the uniform law on all \(21!\) edge orders; no claims are made for nonuniform priorities or arbitrary graphs.

## Proof

**First exact calculation (occupied-vertex recursion).** For an occupied-vertex set \(U\), let \(E(U)\) be the edges having both endpoints outside \(U\); write \(e(U)=|E(U)|\). Let \(F_U(z)\) be the probability-generating polynomial for the number of *further* successful dimers from this state. Exchangeability of the remaining edge priorities implies

\[
F_U(z)=
\begin{cases}
1,&e(U)=0,\\
\displaystyle\frac{z}{e(U)}\sum_{\{u,v\}\in E(U)}F_{U\cup\{u,v\}}(z),&e(U)>0.
\end{cases}
\]

This recursion is finite, terminating at fully jammed states. Starting at \(U=\varnothing\), its exact rational coefficients are \(19/330\), \(497/792\), \(1247/3960\) in degrees five, six and seven, respectively. It visits 2,270 distinct reachable occupied-vertex subsets. The corresponding expectation is \(24779/3960\).

**Independent calculation (individual matching integrals).** Enumerate all matchings of the specified twenty-one-edge graph. A matching \(M\) is terminal iff every edge not in \(M\) shares a vertex with an edge in \(M\). There are exactly \(42\), \(168\), and \(24\) such matchings of sizes five, six and seven, totaling \(234\). Fix a maximal matching \(M\) of size \(k\), and a permutation \(\pi\) of its edges, ordered from earliest to latest priority. Every rejected edge must arrive later than the *earliest* accepted edge sharing one of its endpoints. For each \(i=1,\ldots,k\), let \(a_i\) count rejected edges for which the first incident accepted edge is the \(i\)-th in \(\pi\). If the corresponding ordered uniform priority values are \(0<u_1<\cdots<u_k<1\), then, conditional on them, the rejection constraints have probability \(\prod_{i=1}^{k}(1-u_i)^{a_i}\). Consequently

\[
\Pr(\mathrm{output}=M)=\sum_{\pi\in S_k}
\int_{0<u_1<\cdots<u_k<1}
\prod_{i=1}^{k}(1-u_i)^{a_i(\pi)}\,du_1\cdots du_k
=\sum_{\pi\in S_k}\prod_{j=1}^k
\frac{1}{j+\sum_{i=k-j+1}^{k}a_i(\pi)}.
\]

The final identity follows by substituting \(v_i=1-u_{k+1-i}\) and successively integrating nested powers over \(0<v_1<\cdots<v_k<1\). The formula is an exact rational finite sum with at most \(7!\) terms for each of the 234 matchings. Exhaustive evaluation gives the five output classes listed above, with the three aggregate size probabilities agreeing exactly with the first calculation. All counts and rational summands can be independently regenerated using the attached code; no unexamined numerical approximation is used in the proof.

**Selection comparison.** Exactly \(24\) of the \(234\) maximal matchings are perfect. Their total priority-process mass is \(24(1247/95040)=1247/3960\), whereas uniform maximal-matching sampling gives \(24/234=4/39\). The exact ratio is \(16211/5280\).

## Verification

Run `python VERIFY.py` using Python 3.10 or later. The program specifies the Fano incidence structure, enumerates all maximal matchings by an edge-by-edge search, evaluates the independent edge-priority integrals with exact `fractions.Fraction` arithmetic, and separately computes the size law through the occupied-vertex recursion. It checks all 234 individual matching weights, their five exact classes, all size probabilities, total probability one and the mean. On replay it prints **257 passed exact-rational identities and classifications**, along with the 2,270 reachable occupied-vertex states. This is a finite exhaustive mathematical computation, not a Monte Carlo sample or an infinite-asymptotic theorem.

## Relationship to prior work

Pippenger (1989) studies random sequential adsorption of vertices and edges on graphs and develops general geometric/kinetic methods, including graph families with few short cycles. Dyer and Frieze (1991) study randomized greedy matching on fixed graphs, mainly performance bounds for graph classes. Penrose and Sudbury's openly accessible 2005 study defines the same random-priority dimer process, derives graph-wide forward equations, and studies exact quantities on Bethe lattices together with broader stochastic limits. These works establish the stochastic framework and general algorithmic methods, but the inspected material does not give the Heawood graph's five individual matching-output probability classes or the three-atom terminal-size law. The claim is a finite exact Heawood specialization and its complete output census, **not** a new general random sequential adsorption method. An already available exact Heawood *monomer* model tracks accepted vertices; it does not imply this dimer matching distribution, which selects edges under a different exclusion rule.

## Limitations

The result concerns exactly one canonical fourteen-vertex, cubic girth-six graph and unit-rate/identically distributed continuous edge priorities. It does not prove a universal cage theorem or a large-graph limit. A general finite-state recurrence implies that any fixed-graph probability can in principle be computed; the mathematical content here is the resolved nontrivial output probability-class distribution and its selection bias, not the existence of a generic algorithm. The complete 1989 Pippenger article and 1991 Dyer–Frieze article were not accessible in full; neither their accessible abstracts nor the inspected 2005 full text report this numerical census, but unindexed equivalences or unpublished tabulations remain a historical-priority risk. Historical-priority determination remains provisional; no exhaustive literature-coverage claim is made.

## References

1. N. Pippenger, *Random Sequential Adsorption on Graphs*, SIAM Journal on Discrete Mathematics 2 (1989), 393–401, https://doi.org/10.1137/0402034.
2. M. Dyer and A. Frieze, *Randomized greedy matching*, Random Structures & Algorithms 2 (1991), 29–45, https://doi.org/10.1002/rsa.3240020104.
3. M. D. Penrose and A. Sudbury, *Exact and approximate results for deposition and annihilation processes on graphs*, Annals of Applied Probability 15 (2005), 853–889. Earliest verified public arXiv posting 2005-03-24: https://arxiv.org/abs/math/0503519v1; https://doi.org/10.1214/105051604000000765.
