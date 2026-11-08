# Exact greedy maximal-independent-set laws for dense bipartite complements of \(C_4\)-free regular graphs

## Finding

Let \(H=(A\sqcup B,E_H)\) be a finite simple bipartite graph with \(|A|=|B|=n\), regular degree \(d\), \(2\le d<n\), and no four-cycle. Form \(G=K_{n,n}\setminus E_H\) on the same bipartition. Assign the \(2n\) vertices independent continuous uniform priorities, scan in increasing order, and accept a vertex if none of its previously accepted neighbors was accepted. Denote the resulting maximal independent set by \(I\).

Define the mixed maximal independent sets
\[
S_a=\{a\}\cup N_H(a)\quad(a\in A),\qquad
S_b=\{b\}\cup N_H(b)\quad(b\in B),
\]
and put
\[
q_{n,d}=\frac{dn}{n^2-(d-1)^2}.
\]

**Theorem.** The \(2n+2\) maximal independent sets of \(G\) are exactly \(A,B\), and the \(2n\) distinct sets \(S_a,S_b\). Their *entire random-greedy probability law* is
\[
\Pr(I=A)=\Pr(I=B)=\frac{1-q_{n,d}}2,
\qquad
\Pr(I=S_v)=\frac{q_{n,d}}{2n}
\quad(v\in A\sqcup B).
\]
Consequently, if \(U\) is uniform over all maximal independent sets of \(G\), then
\[
d_{\rm TV}(\mathcal L(I),\mathcal L(U))
=\frac{n}{n+1}-q_{n,d}.
\]
In particular \(\Pr(|I|=d+1)=q_{n,d}\) and \(\Pr(|I|=n)=1-q_{n,d}\) when \(d+1<n\); if \(d+1=n\), the two sizes coincide and the set-level probabilities above still apply.

For every fixed \(d\ge2\), along every feasible sequence with \(n\to\infty\),
\[
q_{n,d}=\frac dn+O_d(n^{-3}),\qquad
 d_{\rm TV}(\mathcal L(I),\mathcal L(U))\longrightarrow1.
\]
The expected sizes are exactly
\[
\mathbb E|I|=n-(n-d-1)q_{n,d},\qquad
\mathbb E|U|=\frac{n(d+2)}{n+1},
\]
so the first is asymptotic to \(n\) while the second tends to \(d+2\). For the explicit infinite family \(H=C_{2n}\), \(d=2\), the mixed-set probability is \(2n/(n^2-1)\).

## Assumptions and scope

All graphs are finite, simple and undirected. The missing-edge graph \(H\) may be disconnected and need not be vertex-transitive. The four-cycle-free condition means two distinct vertices on either side have at most one common neighbor. The random greedy algorithm is the uniform-priority, nonadaptive independent-set process, *not* uniform sampling from the collection of all maximal independent sets. The comparison law \(U\) is the latter uniform distribution.

The assumptions force \(n\ge1+d(d-1)\), by considering the disjoint sets \(N_H(b)\setminus\{a\}\) for \(b\in N_H(a)\). The borderline \(d=2,n=3\) is included: there \(G\) is a three-edge matching and the greedy and uniform laws coincide, despite all maximal independent sets having the same size.

## Proof

**1. All terminal sets.** Any independent set meeting both sides of \(G\) is a complete bipartite subgraph of \(H\) across its two nonempty parts. If it contained at least two vertices on each side, \(H\) would have a four-cycle. Hence every mixed maximal independent set has exactly one vertex on one side and all its \(d\) neighbors on the other side; these are precisely the \(S_v\). The only unmixed maximal sets are the full sides \(A,B\), since \(n>d\) gives each vertex a neighbor in \(G\). As \(d\ge2\), all \(2n+2\) sets are distinct.

**2. Probability of a mixed terminal set.** Condition on the first vertex of the global priority order being a fixed \(a\in A\). This vertex is accepted. For \(b\in N_H(a)\), let \(E_b\) be the event that \(b\) occurs before every vertex of \(A\setminus N_H(b)\). A mixed vertex from \(B\) is accepted if and only if at least one event \(E_b\) holds. Indeed, before the first accepted vertex from \(B\), every encountered \(A\)-vertex was accepted; thus such an accepted \(b\) must precede every \(A\)-vertex not adjacent to it in \(H\). Conversely, if \(E_b\) holds, either an earlier accepted \(B\)-vertex has already made the result mixed, or \(b\) itself is accepted. Vertices outside \(N_H(a)\) cannot be accepted after \(a\).

For any distinct \(b_1,\ldots,b_t\in N_H(a)\), write \(P_t=\Pr(\cap_{j=1}^t E_{b_j}\mid a\text{ first})\). Remaining relative priorities are uniformly distributed. When \(t=1\), \(P_1=1/(n-d+1)\). For \(t\ge2\), let \(x\) and \(y\) be the largest and second-largest of these \(t\) priorities. If the last of these vertices is \(b_*\), all \(n-d\) vertices outside \(N_H(b_*)\) must occur after \(x\). The other \(d-1\) vertices of \(N_H(b_*)\setminus\{a\}\) must occur after \(y\): the four-cycle-free condition ensures that none belongs to any other \(N_H(b_j)\). These conditions are also sufficient. Their joint order-statistic density therefore gives
\[
\begin{aligned}
P_t
&=t(t-1)\int_0^1\!\int_y^1
 y^{t-2}(1-x)^{n-d}(1-y)^{d-1}\,dx\,dy\\
&=\frac{t!\,n!}{(n-d+1)(n+t-1)!}
=\frac{n}{n-d+1}\int_0^1 t z^{t-1}(1-z)^{n-1}\,dz.
\end{aligned}
\]
The last representation holds for \(t=1\) as well. Inclusion-exclusion and the binomial derivative identity yield
\[
\begin{aligned}
\Pr\left(\bigcup_{b\in N_H(a)}E_b\mid a\text{ first}\right)
&=\sum_{t=1}^d(-1)^{t+1}\binom dt P_t\\
&=\frac{n}{n-d+1}\int_0^1 d(1-z)^{n+d-2}\,dz\\
&=\frac{dn}{(n-d+1)(n+d-1)}=q_{n,d}.
\end{aligned}
\]
This calculation uses only \(n,d\), not the detailed incidence pattern. The identical argument holds when the first vertex is in \(B\). Therefore the total probability of a mixed terminal set is \(q_{n,d}\), and each full side occurs with probability \((1-q_{n,d})/2\).

**3. Equality of the mixed-set probabilities.** For any maximal independent set \(S\), the greedy algorithm returns exactly \(S\) if and only if every vertex outside \(S\) occurs after at least one of its neighbors in \(S\). Necessity follows because rejected vertices have earlier accepted neighbors; sufficiency follows by considering the earliest hypothetically accepted vertex outside \(S\).

Apply this order certificate to \(S_a=\{a\}\cup N_H(a)\). Every one of the \(n-d\) outside vertices of \(B\) must appear after \(a\). Among the \(n-1\) outside vertices of \(A\), exactly \(d(d-1)\) share precisely one neighbor with \(a\) in \(H\), with exactly \(d-1\) assigned to each of the \(d\) neighbors of \(a\); all other outside \(A\)-vertices share no neighbor with \(a\) in \(H\). Their order certificates require them to follow, respectively, the earliest of all but one of the \(d\) vertices of \(N_H(a)\), or the earliest of all \(d\). Conditional on the priorities of \(S_a\), the remaining constraints are independent, so the integrated probability depends only on \(n,d\), not on which \(a\) was chosen. The same count with sides interchanged applies to every \(S_b\). Thus all \(2n\) mixed maximal sets are equiprobable, each with probability \(q_{n,d}/(2n)\).

**4. Uniform comparison and sign.** The flat law gives probability \(1/(2n+2)\) to each maximal set. Since \(n\ge1+d(d-1)\), one has \(q_{n,d}\le n/(n+1)\). For \(d=2\), check \(n\ge3\) directly, with equality only at \(n=3\). For \(d\ge3\), \(n\ge2d\), and
\[
n^2-(d-1)^2\ge4d^2-(d-1)^2>d(2d+1),
\]
which implies the desired inequality because the difference between \(n^2-(d-1)^2\) and \(d(n+1)\) increases with \(n\ge2d\). Therefore the two large sets have excess greedy mass and the \(2n\) mixed sets have deficient greedy mass. Summing either positive discrepancy gives
\[
d_{\rm TV}=1-q_{n,d}-\frac1{n+1}=\frac n{n+1}-q_{n,d}.
\]
The expected-size and fixed-degree limits follow immediately from the complete law.

## Verification

Run `python3 check.py` in the directory containing this document and that script. It uses only the Python standard library and checks the exact **individual terminal-set probability law** and total variation formula via a separate recursive greedy-state calculation. It independently enumerates every maximal independent set for the tested graphs, checks complete vertex-permutation outcomes for the six- and eight-vertex examples, verifies disjoint and connected two-regular missing-edge graphs, and checks the degree-three incidence graph of the Fano plane. It also verifies the inclusion-exclusion formula with exact fractions for 853 parameter/model cases. Finite computations check the examples and algebraic formulas, not the universal graph theorem; the arbitrary-\(n\) conclusion is proved above.

## Relationship to prior work

Krivelevich, Mészáros, Michaeli, and Shikhelman introduced the same priority-order greedy independent-set observable and developed asymptotic local-limit methods, primarily on sparse graph sequences. The graphs \(G\) here have degree \(n-d\), which diverges for fixed \(d\), and our theorem concerns the exact terminal-set distribution and comparison with a flat maximal-set ensemble. Dall'Asta, Pin, and Ramezanpour distinguished dynamic generation from uniform blocked-state sampling in a statistical-mechanics setting; no new claim is made for that distinction alone. More recent results on exact greedy-uniformity obstructions on trees and iterative sampling under regularity conditions address different graph families and do not give this probability law. Related exact laws on threshold graphs, chain graphs, and complete multipartite graphs likewise impose different structural hypotheses; a dense bipartite graph obtained by deleting a regular \(C_4\)-free edge set is not covered by those stated families in the nondegenerate cases.

The contribution is the exact, graph-independent probability for *every* maximal output on the full regular four-cycle-free deleted-edge family and the resulting sharp total-variation separation. Existing general first-arrival recurrences, maximal-biclique descriptions, and the idea of comparing dynamical and flat laws are background, not claimed new.

## Limitations

This theorem requires regularity on both parts, equal part sizes, simple bipartite missing edges, absence of four-cycles, and independent continuous uniform priorities. It does not classify irregular missing-edge graphs, graphs whose missing-edge structure has four-cycles, other greedy algorithms, or the distribution of partial (nonmaximal) greedy configurations. The historical-priority comparison is bounded by accessible texts and indexes; absence from searches is not an exhaustive originality certificate. No independent mathematical audit is claimed.

## References

1. M. Krivelevich, T. Mészáros, P. Michaeli and C. Shikhelman, *Greedy maximal independent sets via local limits*, initially publicly posted 2019-07-16, arXiv:1907.07216; published online 2023-12-18, DOI:10.1002/rsa.21200. Full text: https://onlinelibrary.wiley.com/doi/full/10.1002/rsa.21200.
2. L. Dall'Asta, P. Pin and A. Ramezanpour, *Statistical mechanics of maximal independent sets*, Physical Review E 80 (2009), 061136, DOI:10.1103/PhysRevE.80.061136; arXiv:0907.3309.
3. J. Fairfax-Ball, *Greedy Uniformity on Trees: Exact Obstruction and Near-Uniform Spiders*, first posted 2026-10-01, arXiv:2610.02276.
4. I. Kryven, R. Versendaal and M. de Vries, *Unified framework for asymptotically uniform iterative construction of generalised random graphs with local constraints*, first posted 2026-08-07, arXiv:2608.07239.
