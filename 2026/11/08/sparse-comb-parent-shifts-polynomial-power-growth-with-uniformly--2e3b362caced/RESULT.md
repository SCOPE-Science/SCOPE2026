# Sparse comb parent shifts: polynomial power growth with uniformly bounded essential powers

## Finding

For every real \(0<\alpha<1\), a concrete leafless rooted tree with at most two children per vertex gives an unweighted parent shift \(S_\alpha\) on a separable complex Hilbert space satisfying all of the following statements:

\[
\begin{aligned}
\|S_\alpha\|&=\sqrt 2,\\
\sigma(S_\alpha)&=\overline{\mathbb D},\\
\|S_\alpha^n\|^2&=1+\max_{j\geq0}\#\bigl(A_\alpha\cap\{j,\ldots,j+n-1\}\bigr)
=n^\alpha+O(1),\\
\|S_\alpha^n\|_{\mathrm{ess}}&=\sqrt2\qquad(n\geq1).
\end{aligned}
\]

For every \(|\lambda|<1\), \(S_\alpha-\lambda I\) is Rota-universal. Along the positive real axis, its resolvent has the sharp growth exponent

\[
\bigl\|((1+\varepsilon)I-S_\alpha)^{-1}\bigr\|
\asymp_\alpha \varepsilon^{-1-\alpha/2}
\quad(\varepsilon\downarrow0).
\]

In particular, the image of \(S_\alpha\) in the Calkin algebra has bounded positive powers even though the ordinary power norms grow like \(n^{\alpha/2}\). Different values of \(\alpha\) yield pairwise nonsimilar operators with the same unit-disk spectrum, the same norm, and the same essential norm at every positive power.

## Assumptions and scope

Set \(\beta=1/\alpha>1\) and

\[
A_\alpha=\{\lfloor k^\beta\rfloor:k=1,2,\ldots\}\subset\mathbb N.
\]

The rooted comb tree has spine vertices \(v_0,v_1,v_2,\ldots\) with the edge from \(v_{j+1}\) to its parent \(v_j\). For each \(j\in A_\alpha\), attach a separate infinite unary tooth \(t_{j,0},t_{j,1},\ldots\), with parent of \(t_{j,0}\) equal to \(v_j\) and parent of \(t_{j,\ell+1}\) equal to \(t_{j,\ell}\). No teeth are attached elsewhere. Every vertex has one or two children, and the branching vertices lie on the same ancestral spine.

Let \(V_\alpha\) be the countable vertex set and \(H_\alpha=\ell^2(V_\alpha)\). With its canonical orthonormal basis, let the **parent shift** act by \(S_\alpha e_w=e_{\mathrm{par}(w)}\) on each nonroot vertex and \(S_\alpha e_{v_0}=0\), extended linearly and continuously. All statements concern complex \(H_\alpha\). The essential norm is the distance to compact operators, or equivalently the norm of the Calkin image. The notation \(a(\varepsilon)\asymp_\alpha b(\varepsilon)\) means both ratios are bounded above and below by positive constants depending only on \(\alpha\) for all sufficiently small positive \(\varepsilon\).

## Proof

**1. Exact descendant counts and power norms.** For an arbitrary parent shift, \((S^n)^*e_v\) is the sum of the basis vectors of the descendants of \(v\) exactly \(n\) generations below it. Descendant sets of distinct vertices at a fixed generation are disjoint. Therefore

\[
S^n(S^n)^*e_v=\kappa_n(v)e_v,
\qquad
\|S^n\|^2=\sup_{v\in V_\alpha}\kappa_n(v),
\]

where \(\kappa_n(v)\) is the number of such descendants. Every tooth vertex has exactly one descendant at each positive generation. A spine vertex \(v_j\) has its unique spine descendant and, for each branching level \(h\in A_\alpha\cap\{j,\ldots,j+n-1\}\), exactly one additional descendant down the tooth attached at level \(h\). Hence

\[
\kappa_n(v_j)=1+\#(A_\alpha\cap\{j,\ldots,j+n-1\}).
\]

For \(n=1\), a branching vertex has two children, so \(\|S_\alpha\|=\sqrt2\). For arbitrary \(n\geq1\), the displayed maximum gives the exact expression in the finding.

To estimate it, suppose an interval of \(n\) consecutive integers contains \(m\geq1\) members of \(A_\alpha\), beginning with \(\lfloor k^\beta\rfloor\). The gap to the \(m\)-th one is at least

\[
\lfloor(k+m-1)^\beta\rfloor-\lfloor k^\beta\rfloor
\geq (k+m-1)^\beta-k^\beta-1
\geq (m-1)^\beta-1.
\]

Since both endpoints are in an interval of length \(n\), \((m-1)^\beta\leq n\), hence \(m\leq n^\alpha+1\). Conversely the interval \(\{0,\ldots,n-1\}\) contains exactly \(\lceil n^\alpha\rceil-1\) branching levels: \(\lfloor k^\beta\rfloor<n\) if and only if \(k<n^\alpha\). Thus the maximal count equals \(n^\alpha+O(1)\), proving \(\|S_\alpha^n\|^2=n^\alpha+O(1)\), and \(\|S_\alpha^n\|\sim n^{\alpha/2}\).

**2. Essential norms.** Since \(\beta>1\), the successive gaps in the increasing sequence \(\lfloor k^\beta\rfloor\) tend to infinity. For each fixed \(n\), every sufficiently remote \(n\)-window in the spine contains at most one branching level; infinitely many such windows contain exactly one. Consequently the diagonal operator \(S_\alpha^n(S_\alpha^n)^*\) has diagonal values at most \(2\) outside a finite set and has value \(2\) at infinitely many spine coordinates. Its essential norm is precisely \(2\). The \(C^*\)-identity in the Calkin algebra gives

\[
\|S_\alpha^n\|_{\mathrm{ess}}^2
=\|S_\alpha^n(S_\alpha^n)^*\|_{\mathrm{ess}}=2,
\quad n\geq1.
\]

In particular, the Calkin image is power-bounded, whereas \(\|S_\alpha^n\|\to\infty\).

**3. Disk spectrum and universality.** For every vertex, the number of children is at least one. Therefore \(S_\alpha S_\alpha^*\) is diagonal with entries in \(\{1,2\}\), hence \(S_\alpha S_\alpha^*\geq I\). The bounded operator

\[
Q=S_\alpha^*(S_\alpha S_\alpha^*)^{-1}
\]

satisfies \(S_\alpha Q=I\) and \(\|Q\|\leq1\). For \(|\lambda|<1\), factor

\[
S_\alpha-\lambda I=S_\alpha(I-\lambda Q).
\]

The second factor is invertible by the Neumann series; thus \(S_\alpha-\lambda I\) is surjective. At every branching level \(j\), the vector \(e_{v_{j+1}}-e_{t_{j,0}}\) belongs to \(\ker S_\alpha\); these vectors are mutually orthogonal and nonzero for infinitely many \(j\). Consequently \(\ker S_\alpha\), and by invertible factorization also \(\ker(S_\alpha-\lambda I)\), is infinite-dimensional. The standard Caradus criterion proves Rota universality of \(S_\alpha-\lambda I\) for every \(|\lambda|<1\).

The power-norm asymptotic gives \(r(S_\alpha)=\lim_{n\to\infty}\|S_\alpha^n\|^{1/n}=1\). Since each \(|\lambda|<1\) is an eigenvalue and the spectrum is closed, \(\sigma(S_\alpha)=\overline{\mathbb D}\).

**4. Resolvent upper bound.** For \(r=1+\varepsilon>1\), the spectral-radius formula just established permits the norm-convergent series

\[
(rI-S_\alpha)^{-1}=\sum_{n=0}^\infty r^{-n-1}S_\alpha^n.
\]

The first step gives \(\|S_\alpha^n\|\leq C_\alpha(n+1)^{\alpha/2}\), including \(n=0\). Hence the integral comparison for \(\sum_{n\geq0}e^{-c\varepsilon n}(n+1)^{\alpha/2}\) yields

\[
\|(rI-S_\alpha)^{-1}\|\leq C'_\alpha\varepsilon^{-1-\alpha/2}
\]

for small positive \(\varepsilon\).

**5. Matching resolvent lower bound.** Let \(N=\lfloor\varepsilon^{-1}\rfloor\) and \(J=A_\alpha\cap\{N,\ldots,2N-1\}\). Its size \(m\) satisfies

\[
m=\bigl(2^\alpha-1\bigr)N^\alpha+O(1),
\]

so \(m\asymp_\alpha N^\alpha\). For each \(j\in J\), introduce a normalized tooth vector

\[
g_j=\sqrt{1-r^{-2}}\sum_{\ell=0}^\infty r^{-\ell}e_{t_{j,\ell}},
\qquad \|g_j\|=1.
\]

These vectors have disjoint support; therefore \(x=m^{-1/2}\sum_{j\in J}g_j\) has norm one. Positivity of all the matrix coefficients of the real resolvent shows that for each spine coordinate \(v_i\), \(0\leq i\leq N/2\),

\[
\left\langle(rI-S_\alpha)^{-1}x,e_{v_i}\right\rangle
=\frac{1}{\sqrt{m(1-r^{-2})}}
\sum_{j\in J}r^{-(j-i+2)}.
\]

Indeed, the unique path from \(t_{j,\ell}\) up to \(v_i\) has length \(j-i+\ell+1\), contributing \(r^{-(j-i+\ell+2)}\) in the resolvent series. For \(j<2N\), \(i\geq0\), and \(r=1+\varepsilon\) with \(\varepsilon N\leq1\), each factor \(r^{-(j-i+2)}\) is bounded below by an absolute positive constant; also \((1-r^{-2})^{-1/2}\asymp\sqrt N\). Thus every displayed spine coordinate is bounded below by \(c\sqrt{mN}\), and there are at least \(N/2\) mutually orthogonal such coordinates. Therefore

\[
\|(rI-S_\alpha)^{-1}x\|\geq c_\alpha N\sqrt m
\geq c'_\alpha\varepsilon^{-1-\alpha/2}.
\]

Combining steps 4 and 5 proves the sharp two-sided resolvent estimate.

**6. Nonsimilarity.** If \(S_\alpha\) and \(S_{\alpha'}\) were similar, their power norms would be comparable up to a fixed multiplicative constant for all positive integers \(n\). The proven asymptotics \(\|S_\alpha^n\|\sim n^{\alpha/2}\) rule this out whenever \(\alpha\ne\alpha'\).

## Verification

The standalone `check_comb.py` uses standard-library arithmetic to reproduce branch-window counts, compare explicit finite-tree descendant counts with the exact formula, and test finite lower resolvent witnesses against the analytical power-series upper bound. It passed **2,946** finite assertions across five sample values of \(\beta\). These tests validate examples and code arithmetic, not the infinite-dimensional or asymptotic arguments, which are proved above.

## Relationship to prior work

Buckley and Seco introduced the parent-shift framework and proved spectral-radius and universality results for trees satisfying an additional disjoint-branch hypothesis (A4) [1]. Their general descendant-count identity underlies step 1. The comb trees here have all branching vertices on one ancestral spine and **fail their assumption (A4)**. Thus the universality statement for these trees is established directly in step 3, rather than being attributed to their theorem. The exact polynomial power growth, constant essential-power norms, and sharp resolvent exponent constitute the quantitative conclusions studied here.

General weighted-shift work on directed trees [2], analytic models for left-invertible directed-tree shifts [3], and dynamics of such shifts [4] provide related operator-theoretic contexts, but their reviewed statements do not assert this combined invariant profile. In particular, the finite-branching-index assumption of the specific analytic-model results in [3] is not met by these combs.

## Limitations

The construction is specific to an unweighted, Hilbert-space parent shift on the explicitly defined comb; it does not classify shifts on arbitrary directed trees. The resolvent result gives an exact exponent and two-sided bounds, not a limiting leading constant. The conclusions do not establish universality at points on the unit circle. The priority comparison is based on the accessible cited literature and targeted searches; it does not exclude equivalent general facts under other terminology. No independent external mathematical audit has been performed.

## References

1. J. Buckley and D. Seco, *Rota universality of shifts on trees*, arXiv:2610.40089v1 (first publicly available 29 October 2026), https://arxiv.org/abs/2610.40089 .
2. Z. Jabłoński, I. B. Jung and J. Stochel, *Weighted shifts on directed trees*, arXiv:0911.3821, https://arxiv.org/abs/0911.3821 .
3. S. Chavan and S. Trivedi, *An analytic model for left-invertible weighted shifts on directed trees*, arXiv:1510.03075v2, https://arxiv.org/abs/1510.03075 .
4. K.-G. Grosse-Erdmann and D. Papathanasiou, *Dynamics of weighted shifts on directed trees*, arXiv:2012.15542v3, https://arxiv.org/abs/2012.15542 .
