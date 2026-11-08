# Exhaustive-community optimal leaders on balanced multipartite networks

## Finding

Let \(r\ge3\) and \(n\ge2\) be integers and let \(G=K_{n,\ldots,n}\) be the unweighted complete \(r\)-partite graph with \(r\) parts, each of size \(n\). For every integer \(1\le k<rn\), choose exactly \(k\) **noise-free leaders**, delete their rows and columns from the combinatorial Laplacian \(L\), and minimize
\[
J(S)=\operatorname{tr}(L_{V\setminus S,V\setminus S}^{-1})
\]
over all \(k\)-element leader sets \(S\).

**Theorem.** Write \(k=an+b\) with \(0\le b<n\). Every optimal leader set comprises all vertices of \(a\) whole parts, together with \(b\) vertices of one further part (when \(b>0\)); conversely, every set with this form is optimal. The optimal-part count pattern is unique up to permuting the parts. Thus a globally optimal leader set is constructible in \(O(k)\) output operations after specifying the parts, and its objective is evaluated using \(O(r)\) rational arithmetic operations. No search over vertex subsets or integer allocation patterns is needed.

More precisely, put \(d=(r-1)n\), \(F=rn-k\), \(q=\lfloor F/n\rfloor\), and \(t=F-qn\) (so \(0\le t<n\)). The optimal follower counts are the permutations of
\[
(f_1,\ldots,f_r)=(\underbrace{n,\ldots,n}_{q},t,\underbrace{0,\ldots,0}_{r-q-1}).
\]
Set
\[
S_*=\frac qr+\frac{t}{d+t},\qquad
G_*=\frac{q}{r^2n}+\frac{t}{(d+t)^2}.
\]
Then the exact minimum is
\[
\boxed{J_{\min}=\frac{F-q-1}{d}+\frac{q}{rn}+\frac1{d+t}+\frac{G_*}{1-S_*}.}
\]
For example, on \(K_{3,3,3}\) with \(k=3\), the optimum places all three leaders in one part, giving \(J_{\min}=10/9\). Putting one leader in each part instead gives \(5/4\), strictly worse.

## Assumptions and scope

All edges have conductance \(1\), every part contains exactly \(n\) vertices, the graph has at least three parts, and exactly \(k\) leaders are completely noise-free. Disturbances affect all followers uniformly; the objective is the **unscaled trace of the grounded inverse**, not a smallest-eigenvalue criterion or a noisy-leader objective. The common physical steady-state variance convention multiplies this trace by \(1/2\), which does not change the minimizing sets. The case \(k=rn\) has the empty follower matrix and is excluded. Every grounded matrix considered below is positive definite because the connected graph has at least one leader.

We also prove a strictly stronger analytic comparison: for a fixed total follower count \(F\in(0,rn)\), the rational objective is *strictly Schur-concave* as a function of the vector of follower counts in the closed cube \([0,n]^r\), on the hyperplane of sum \(F\). This is meant in the concrete sense that an unequalizing transfer from one positive smaller coordinate to a larger coordinate, without exceeding \(n\), strictly decreases the objective. The optimization statement needs this comparison only for integer follower counts.

## Proof

**1. Reduction to counts.** Let \(f_i\in\{0,\ldots,n\}\) be the number of followers in part \(i\), and \(F=\sum_i f_i\). Every original graph vertex has Laplacian diagonal \(d=(r-1)n\); distinct followers are adjacent precisely when they belong to different parts. After reordering followers, the grounded matrix has within-part constant-vector modes of eigenvalue \(d\) and an \(r\)-dimensional part-constant representation. Writing \(u_i=\sqrt{f_i}\), with zero entries permitted, the latter is the matrix
\[
B=\operatorname{diag}(d+f_1,\ldots,d+f_r)-uu^{\mathsf T}.
\]
For \(f_i=0\), the corresponding one-dimensional mode is artificial and has eigenvalue \(d\); subtracting its reciprocal exactly cancels this contribution. Hence, for all \(f_i\ge0\), including zero, the trace is
\[
J(f)=\frac{F-r}{d}+\operatorname{tr}(B^{-1}). \tag{1}
\]
For positive \(f_i\), there are \(f_i-1\) genuine within-part modes; for zero \(f_i\), the same formal expression gives \(-1\) and cancels the artificial mode. This justifies (1) uniformly.

**2. Exact rational formula and positivity of the denominator.** Put
\[
S(f)=\sum_{i=1}^r\frac{f_i}{d+f_i},\qquad
G(f)=\sum_{i=1}^r\frac{f_i}{(d+f_i)^2}.
\]
Since \(0\le f_i\le n\) and \(d+n=rn\), each fraction \(f_i/(d+f_i)\le1/r\). At least one part has a leader, so at least one inequality is strict. Thus \(S(f)<1\). The Sherman–Morrison rank-one inverse identity applied to \(B\) yields
\[
\boxed{J(f)=\frac{F-r}{d}+\sum_{i=1}^r\frac1{d+f_i}+\frac{G(f)}{1-S(f)}.}\tag{2}
\]
This also shows why the rational extension of the objective to \([0,n]^r\), with \(0<F<rn\), is well defined.

**3. Strict pairwise concentration lemma.** Fix all follower counts except \(x=f_i\) and \(y=f_j\), fix their sum \(s=x+y\), and let
\[
S_0=\sum_{\ell\notin\{i,j\}}\frac{f_\ell}{d+f_\ell},\quad
G_0=\sum_{\ell\notin\{i,j\}}\frac{f_\ell}{(d+f_\ell)^2},\quad
c=1+S_0.
\]
Write \(T=2d+s\), \(U=4d+s\), and \(B_0=(d+x)(d+y)=d^2+ds+xy\). By combining the two terms of the sum in (2) with the rank-one correction, the portion that depends on \(x,y\) is exactly
\[
R(B_0)=\frac{U-cT+G_0B_0}{dT-cB_0}. \tag{3}
\]
The other contributions are independent of \(x,y\). The denominator is positive: it equals \(B_0(1-S(f))\). Direct differentiation, at fixed \(s\), gives
\[
\frac{dR}{dB_0}
=\frac{G_0dT+c(U-cT)}{(dT-cB_0)^2}.\tag{4}
\]
Here \(G_0\ge0\), \(c\ge1\), and, because each other count is at most \(n\),
\[
S_0\le\frac{r-2}{r},\qquad T\le2(d+n)=2rn.
\]
Consequently,
\[
U-cT=2d-S_0T\ge2(r-1)n-2(r-2)n=2n>0.\tag{5}
\]
Equations (4)–(5) show \(dR/dB_0>0\). With \(s\) fixed, \(B_0=d^2+ds+xy\), so **the objective strictly increases with \(xy\)**. If \(0<y\le x<n\), moving any \(0<\varepsilon\le\min\{y,n-x\}\) from \(y\) to \(x\) changes \(xy\) to \((x+\varepsilon)(y-\varepsilon)<xy\), and strictly decreases \(J\). This establishes the claimed Schur-concavity comparison without a dimension-dependent exception.

**4. Global necessity and sufficiency.** If two coordinates of a feasible follower-count vector are both strictly between \(0\) and \(n\), a transfer as in step 3 reaches a boundary and strictly improves the objective. Repeating this finite process leaves **at most one** coordinate strictly between \(0\) and \(n\). Since the sum \(F\) is fixed, every such boundary vector must be a permutation of \((n,\ldots,n,t,0,\ldots,0)\), with \(q=\lfloor F/n\rfloor\). All these vectors give the same objective by part symmetry; every other vector admits a strict improvement. Thus these and only these are optimal follower patterns. Complementing the followers gives the stated leader patterns.

**5. Exact minimum.** Substitution of the canonical follower vector into (2) gives \(S=S_*\), \(G=G_*\), and
\[
\sum_i\frac1{d+f_i}=\frac q{rn}+\frac1{d+t}+\frac{r-q-1}{d}.
\]
The claimed expression follows by combining the last term with \((F-r)/d\). This proves all assertions. The formulas remain valid when \(t=0\): the displayed zero-count coordinate then contributes exactly \(1/d\).

## Verification

The accompanying standalone `verify.py` uses Python's exact `fractions.Fraction` arithmetic and an independently implemented rational Gauss–Jordan inverse. It exhausts all nontrivial follower-count allocations for nine parameter pairs \((r,n)\): \((2,2),(2,3),(2,4),(3,2),(3,3),(3,4),(4,2),(4,3),(5,2)\). The two-part runs are an auxiliary boundary crosscheck, not the novel theorem's scope. It checks the derived formula against full grounded inversions, every allowed budget against all allocations (including equality classification), and the positive expression (4) for all pairs. The actual replay yields 828 exact inverse identities, 66 complete budget comparisons, and 5,082 pair-derivative tests. The global theorem is certified by the algebraic proof above, not by finite enumeration.

Run the checker from a directory containing this manuscript and `verify.py` with `python3 verify.py`; it needs only Python's standard library.

## Relationship to prior work

The noise-free leader objective is the grounded inverse trace studied by Lin, Fardad and Jovanović (2013). Fitch and Leonard (2014) derived joint-centrality formulas for leader performance and treated cycles and paths explicitly. Patterson, McGlohon and Dyagilev (2014) gave polynomial-time optimal selection on weighted paths and rings. Patterson, Yi and Zhang (2017) treated resistance-based coherence, paths/cycles, and certain two-leader tree problems. Their inspected formulations do not state or imply the all-budget balanced-multipartite concentration law: the proof here supplies the decisive strict pair-transfer comparison (3)–(5) for any number of communities. A two-community count reduction by itself does not prove the multi-community comparison. Searches for alternative terminology (balanced Turán graphs, partition-majorization, grounded inverse traces, noise-free leader allocation) did not locate an equivalent result in the accessible material. These searches are evidence of coverage attempted, not a proof of worldwide priority.

## Limitations

The conclusion assumes **equal part sizes**, **unit undirected cross-edges**, and **noise-free leaders**. It does not classify unequal multipartite graphs, unequal edge conductances, noisy leaders, other coherence criteria, or optimal actuator sets for controllability. The exact formula scales the physical variance by a fixed factor, as noted above. The source literature inspection cannot rule out an unindexed or differently named earlier statement. The current package has been checked for mathematical consistency and computational reproducibility but has not undergone an independent mathematical audit.

## References

1. F. Lin, M. Fardad, M. R. Jovanović, *Algorithms for Leader Selection in Stochastically Forced Consensus Networks*; initially public February 3, 2013, arXiv:1302.0450, https://arxiv.org/abs/1302.0450.
2. K. E. Fitch, N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*; initially public July 7, 2014, arXiv:1407.1569, https://arxiv.org/abs/1407.1569.
3. S. Patterson, N. McGlohon, K. Dyagilev, *Efficient, Optimal k-Leader Selection for Coherent, One-Dimensional Formations*; initially public December 20, 2014, arXiv:1412.6595, https://arxiv.org/abs/1412.6595.
4. S. Patterson, Y. Yi, Z. Zhang, *A Resistance Distance-Based Approach for Optimal Leader Selection in Noisy Consensus Networks*; initially public August 23, 2017, arXiv:1708.06873, https://arxiv.org/abs/1708.06873.
