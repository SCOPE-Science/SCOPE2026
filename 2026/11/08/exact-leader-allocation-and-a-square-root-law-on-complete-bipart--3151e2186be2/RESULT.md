# Exact leader allocation and a square-root law on complete bipartite networks

## Finding

For every pair of integers \(p,q\ge2\), let \(K_{p,q}\) be the simple unweighted complete bipartite graph, with parts \(P,Q\) of sizes \(p,q\), and combinatorial Laplacian \(L\). With exactly \(k\) noise-free leaders, \(1\le k<p+q\), minimize the grounded trace \(\operatorname{tr}(L_{FF}^{-1})\), where \(F\) is the follower set. If \(a\) leaders lie in \(P\) and \(b=k-a\) lie in \(Q\), put \(x=p-a\) and \(y=q-b\). The exact objective is

\[
C_{p,q,k}(a)=\frac{x-1}{q}+\frac{y-1}{p}+\frac{p+q}{pq-xy},
\qquad \max(0,k-q)\le a\le\min(p,k).
\]

Thus the exact global optimum and an attaining leader set follow from at most \(\min(p,k)+1\) rational evaluations, and every optimal leader set is described by a minimizing integer count \(a\) together with arbitrary vertices in the respective parts.

This evaluation has three structural consequences.

1. For \(p=q=r\ge2\) and any \(1\le k<2r\), every optimal configuration puts all followers into one part as far as the part-capacity constraint allows: the minimizing follower counts are the two endpoints of their feasible interval. Equivalently, if \(k\le r\), all leaders are in one part; if \(k\ge r\), one entire part consists of leaders.

2. For each fixed \(p\ge2\) and fixed budget \(k\ge1\), as \(q\to\infty\) the number \(a\) of leaders in the \(p\)-vertex part is eventually confined to the minimizers of \(a/p+1/a\) over integers \(1\le a\le\min(p,k)\). Let \(r_p\) be the least positive integer with \(r_p(r_p+1)\ge p\). If \(p\ne r_p(r_p+1)\), the eventually unique optimal part count is \(a=\min(k,r_p)\). At equality \(p=r_p(r_p+1)\), the only possible eventual counts are \(\min(k,r_p)\) and, if feasible, \(r_p+1\). In particular \(r_p\sim\sqrt p\) as \(p\to\infty\) after the fixed-\(p\) large-\(q\) limit.

3. On \(K_{2,3}\), the unique optimal two-leader set is its two-vertex part, with trace \(3/2\), whereas the unique optimal three-leader set is its three-vertex part, with trace \(2/3\); consequently no nested sequence of optimal leader sets exists across these two budgets. Mixed allocation can be strictly necessary: on \(K_{2,9}\) at budget \(k=4\), the unique optimal counts are \(a=1\) in the two-vertex part and \(b=3\) in the nine-vertex part, with trace \(41/12\); both unmixed count alternatives have strictly larger trace.

## Assumptions and scope

All edges have unit conductance. The leader vertices are noiselessly fixed; the objective is the unnormalized trace of the inverse of the follower principal submatrix of the **original full graph Laplacian**, retaining degrees from edges to leaders. There is no optimization over edge weights, leader gains, or disturbance covariance. The budget is exactly \(k\), with at least one follower and at least one leader. The asymptotic takes \(q\to\infty\) with \(p,k\) held fixed; it is not a simultaneous uncontrolled limit.

## Proof

**Exact trace.** For any follower counts \(x,y>0\), after listing followers by part, the grounded matrix is

\[
L_{FF}=\begin{pmatrix}qI_x&-J_{x,y}\\-J_{y,x}&pI_y\end{pmatrix}.
\]

Its restriction to vectors whose coordinates sum to zero within each part acts by \(q\) and \(p\), with multiplicities \(x-1\) and \(y-1\). On the orthonormal two-dimensional span of the normalized all-ones vectors it is the matrix \(\left(\begin{smallmatrix}q&-\sqrt{xy}\\-\sqrt{xy}&p\end{smallmatrix}\right)\), whose inverse trace equals \((p+q)/(pq-xy)\). Because at least one leader is selected, \(xy<pq\) and the matrix is positive definite. Adding the traces proves the formula. If \(x=0\) or \(y=0\), the grounded matrix is diagonal; direct evaluation gives \(x/q+y/p\), which agrees with the displayed expression after cancellation. Every leader set with the same pair of part counts is isomorphic under graph automorphisms, proving the exact optimization reduction.

**Balanced parts.** For \(p=q=r\), the sum of the first two terms is constant at fixed \(x+y\), and the remaining term increases strictly with \(xy\). At fixed sum, the product \(xy=x(x+y-x)\) is strictly concave, so it is minimized at the two endpoints of the feasible integer interval. These endpoint follower counts have the claimed structural descriptions.

**Large-imbalance allocation.** Set \(b=k-a\), \(x=p-a\), \(y=q-k+a\). If \(a=0\) is feasible then \(pq-xy=pk\), hence

\[
C_{p,q,k}(0)=\frac{q}{p}+\frac{q}{pk}+O_{p,k}(1).
\]

For each fixed feasible \(a\ge1\), \(pq-xy=aq+(p-a)(k-a)\), and therefore

\[
C_{p,q,k}(a)=\frac{q}{p}+\frac{a-k-1}{p}+\frac1a+O_{p,k}(q^{-1}).
\]

There are finitely many feasible integer counts. Thus the optimal count for sufficiently large \(q\) lies among the minimizers of \(g(a)=a/p+1/a\). The exact adjacent difference

\[
g(a+1)-g(a)=\frac1p-\frac1{a(a+1)}
\]

changes sign at the least \(r_p\) with \(r_p(r_p+1)\ge p\). This proves the asserted cases, including the possible tie when \(p=r_p(r_p+1)\). From \(r_p(r_p-1)<p\le r_p(r_p+1)\) one gets \(r_p/\sqrt p\to1\).

**Strict examples.** For \(K_{2,3}\) and \(k=2\), the objectives at \(a=0,1,2\) are respectively \(19/12,7/4,3/2\); for \(k=3\) they are \(2/3,1,1\). The minimizers are strict and their leader sets are disjoint. For \(K_{2,9}\), \(k=4\), the objectives for \(a=0,1,2\) are respectively \(251/72,41/12,7/2\). Since \(41/12<251/72<7/2\), the mixed count is uniquely optimal.

## Verification

Run `python3 verify.py` using only the Python standard library. The standalone verifier performs exact-fraction Gauss-Jordan inversions of grounded matrices for every feasible part count with \(2\le p,q\le7\), independently enumerates all leader subsets for smaller graphs, checks the two strict examples, and tests the discrete asymptotic minimizer identity over a parameter grid. All tests executed successfully on the exact files embedded with this result; the verifier reported `VERIFY_OK`. Finite tests do not prove claims outside tested cases; the proof above handles all admissible integers and the asymptotic limit.

## Relationship to prior work

Lin–Fardad–Jovanović introduced general leader-selection optimization and convex relaxations for noise-free leaders, with the grounded inverse-trace criterion. Fitch–Leonard's joint-centrality formulation identifies a generic characterization and exact choices on paths and cycles. Patterson–McGlohon–Dyagilev developed exact algorithms on weighted one-dimensional paths and rings. The present result evaluates the arbitrary-budget objective on all complete bipartite graphs, proves the balanced extremizer structure, exhibits a strict change in optimal part membership between successive budgets, and establishes a fixed-small-part square-root allocation law. None of the specifically inspected primary results states these biclique assertions; general graph-level formulas alone do not supply their evaluated classification without this analysis.

## Limitations

Novelty is asserted only relative to inspected mathematical literature and accessible research records; an unindexed equivalent or stronger bipartite allocation analysis may exist. No independent mathematical audit has occurred. The asymptotic does not assert a uniform theorem when \(p\), \(k\), and \(q\) grow simultaneously. The tie case allows two possible eventual part counts and does not assert that both occur for every finite \(q\). There is no claim about controllability-optimal or gain-optimized leader placement.

## References

- F. Lin, M. Fardad and M. R. Jovanović, *Algorithms for Leader Selection in Stochastically Forced Consensus Networks*, arXiv:1302.0450, first posted 2013-02-03. https://arxiv.org/abs/1302.0450
- K. Fitch and N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569, first posted 2014-07-07. https://arxiv.org/abs/1407.1569
- S. Patterson, N. McGlohon and K. Dyagilev, *Efficient, Optimal k-Leader Selection for Coherent, One-Dimensional Formations*, arXiv:1412.6595, first posted 2014-12-20. https://arxiv.org/abs/1412.6595
