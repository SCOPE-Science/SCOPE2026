# Sharp stage-budget phase transition for a masked cubic trace estimator on a rank-one projector

## Finding
For a Bernoulli-row incomplete-product Hutchinson estimator of the cubic trace of a constant rank-one projector, equal observation fractions at the three stages are not variance-optimal, except in dimension two. The final stage, which shares its Rademacher probe with the terminal quadratic form, receives strictly more observations than either preceding stage. The exact unique optimum exhibits a finite-budget saturation phase transition and a dimension-dependent variance improvement over equal allocation.

Specifically, put \(a=n-1\), \(b=2-2/n\), and let \(p_1+p_2+p_3=P\), where \(n\ge 2\), \(0<P<3\), and \(0<p_j\le 1\). The estimator defined below satisfies
\[
\mathbb E Z=1,\qquad
\operatorname{Var}(Z)=\frac{(a+p_1^{-1})(a+p_2^{-1})(b+p_3^{-1})}{n^2}-1.
\]
For \(n=2\) its unique variance-minimizing allocation is \(p_1=p_2=p_3=P/3\). For \(n\ge3\), set
\[
s_*=\frac{\sqrt{1+4a(1+b)}-1}{2a},\qquad P_*=1+2s_*.
\]
The unique optimal allocation is \((s,s,t)\), with \(t>s\) whenever \(P<3\). If \(P\ge P_*\), then \(t=1\), \(s=(P-1)/2\). If \(0<P<P_*\), then \(s,t\) are the unique positive solution of
\[
2s+t=P,\qquad s(1+as)=t(1+bt),\qquad t<1.
\]
For fixed \(0<P<1\) as \(n\to\infty\), \(s\sim\sqrt{P(1+2P)/n}\), \(t\to P\), the optimal variance tends to \(1+P^{-1}\), whereas equal allocation has variance tending to \(1+3P^{-1}\). These limits and the finite-budget optimization concern a single trace probe.

## Assumptions and scope
Let \(u=n^{-1/2}(1,\ldots,1)^\top\in\mathbb R^n\) and \(A=uu^\top\); thus \(A^3=A\) and \(\operatorname{tr}(A^3)=1\). Let \(x\in\{-1,1\}^n\) have independent uniform Rademacher coordinates. Independently let \(D_1,D_2,D_3\) be random diagonal matrices whose entries in stage \(j\) are independent Bernoulli variables of success probability \(p_j\); masks are mutually independent and independent of \(x\). The observed row budget is \(nP=n\sum_jp_j\), in expectation, not a deterministic number of observed rows. Define
\[
Z=\frac{x^\top D_3 A D_2 A D_1 A x}{p_1p_2p_3}.
\]
This is a stage-heterogeneous Bernoulli-row variant of incomplete-product cubic trace estimation. Its model differs from equal-rate and fixed-cardinality row schemes: no claim of an optimal allocation for arbitrary matrices, graph adjacency matrices, or general mask dependence is made.

## Proof
**Factorization and unbiasedness.** Since \(A=uu^\top\), write \(B_{ji}=(D_j)_{ii}\). Then
\[
Z=F_1F_2H,\quad F_j=\frac{\sum_i B_{ji}}{np_j}\ (j=1,2),\qquad H=\frac{(\sum_i x_i)(\sum_i B_{3i}x_i)}{np_3}.
\]
The three random factors are independent: each \(F_j\) depends only on its own mask; \(H\) depends on the third mask and the probe. Each factor has expectation one, so \(\mathbb EZ=1\).

**Second moment.** For \(j=1,2\), a binomial second-moment calculation gives \(\mathbb EF_j^2=(n-1+p_j^{-1})/n\). Let \(K=\sum_i B_{3i}\). Conditional on the third mask with \(K=k\), the fourth-moment pairing identity for independent Rademacher variables yields
\[
\mathbb E_x\!\left[(\textstyle\sum_i x_i)^2(\textstyle\sum_i B_{3i}x_i)^2\mid D_3\right]=2k^2+(n-2)k.
\]
Because \(K\sim\operatorname{Bin}(n,p_3)\), this has expectation \(n^2p_3^2(2-2/n)+n^2p_3\). Dividing by \(n^2p_3^2\) gives \(\mathbb EH^2=2-2/n+p_3^{-1}\). Multiplying the independent second moments proves the stated exact variance.

**Unique optimization and transition.** Minimizing variance is equivalent to minimizing
\[
\varphi(p_1,p_2,p_3)=\log(a+p_1^{-1})+\log(a+p_2^{-1})+\log(b+p_3^{-1}).
\]
For every \(c>0\), \(f_c(p)=\log(c+p^{-1})\) satisfies
\[
f_c'(p)=-\frac1{p(1+cp)},\qquad f_c''(p)=\frac{1+2cp}{p^2(1+cp)^2}>0.
\]
The objective is strictly convex and diverges when any \(p_j\) tends to zero, so there is a unique minimizer on the capped budget simplex. Symmetry and strict convexity imply \(p_1=p_2=s\). If \(n=2\), \(a=b=1\), so all stages are identical and \(s=t=P/3\).

For \(n\ge3\), \(a>b\). If \(t\le s\), then \(t(1+bt)<s(1+as)\), hence \(1/[t(1+bt)]>1/[s(1+as)]\): transferring a small amount of the row budget from one earlier stage to the last decreases the objective. Thus no optimum has \(t\le s\), and necessarily \(t>s\). It follows that \(s<1\), so only the upper bound \(t\le1\) can bind. In the interior, the Lagrange equations give \(s(1+as)=t(1+bt)\); the left side strictly increases in \(s\), while the right side strictly decreases when \(t=P-2s\). This gives the unique interior solution. At the boundary \(t=1\), the constrained optimum is \(s=(P-1)/2\). The inward derivative switches sign when \(s(1+as)=1+b\), i.e. at \(s=s_*\), \(P=P_*\). This proves the sharp phase transition. Since \(a>b\) when \(n>2\), \(s_*<1\), so \(1<P_*<3\).

**Large dimension.** For fixed \(0<P<1\) the cap \(t\le1\) cannot bind, and the interior equation implies \(ns^2\to P(1+2P)\), since \(s\to0\) and \(t=P-2s\to P\). Hence \(s\sim\sqrt{P(1+2P)/n}\). Substituting in the exact second moment gives \(\mathbb EZ^2\to 2+1/P\), hence \(\operatorname{Var}(Z)\to1+1/P\). Equal allocation \(p_i=P/3\) instead has \(\mathbb EZ^2\to2+3/P\), giving variance \(1+3/P\). This completes the proof.

## Verification
The accompanying standalone Python 3 program `verify.py` enumerates exact finite distributions using rational arithmetic for small dimensions and several rational probability triples. It independently computes the original matrix-product estimator from masks and probes; compares its first two moments with the derived formulas; verifies the unique optimizer conditions, the transition, and perturbation inequalities across a deterministic parameter grid; and checks the asymptotic trend. Run `python3 verify.py` from the extracted file directory. Finite calculations support the proof but do not establish all-dimensional or limiting statements.

## Relationship to prior work
Ghosh, Horesh, Kalantzis, Lu, Nowicki, and Ubaru (2026, arXiv:2606.22629, sections 2 and 3) introduce incomplete-product Hutchinson estimators with three independently drawn equal-law row masks, prove unbiasedness, and give a general second-moment expansion. The present result uses an unequal-probability Bernoulli-mask model on a constant rank-one projector, emphasizing the exact allocation optimization, its saturation boundary, and the large-dimension strict asymmetry; the general moment expansion alone does not state the allocation law. Hutch++ (Meyer et al., 2020) and improved Hutch++ variants (Persson, Cortinovis, and Kressner, 2022) allocate matrix-vector operations for low-rank trace estimation, but not the three incomplete row masks within one cubic trace probe. These broader frameworks and the older sampling-allocation literature are priority-comparison risks, not novelty certificates.

## Limitations
The rank-one projector \(A\) is a trace-estimation test matrix and is not a loopless graph adjacency matrix. Observations are Bernoulli independent with **expected** rather than deterministic row budget. The derived formula is for one probe and variance, not for tail-optimality, adaptive estimates, computation wall time, or arbitrary matrices. Results assume exact arithmetic and prescribed independent masks. Historical completeness of literature search and independent validation are not guaranteed.

## References
1. S. Ghosh, L. Horesh, V. Kalantzis, Y. Lu, T. Nowicki, S. Ubaru, *Counting Triangles of Graphs via Randomized Trace Estimation with Incomplete Matrix-Vector Products*, arXiv:2606.22629 (first public June 21, 2026), https://arxiv.org/abs/2606.22629.
2. R. A. Meyer, C. Musco, C. Musco, D. P. Woodruff, *Hutch++: Optimal Stochastic Trace Estimation*, arXiv:2010.09649 (2020), https://arxiv.org/abs/2010.09649.
3. D. Persson, A. Cortinovis, D. Kressner, *Improved Variants of the Hutch++ Algorithm for Trace Estimation*, SIAM Journal on Matrix Analysis and Applications (2022), https://doi.org/10.1137/21M1447623.
