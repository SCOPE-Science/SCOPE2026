# Universal heat-trace and Schatten-resolvent extremizers on pinned cycles

## Finding

**Theorem.** Let \(N\ge3\), \(1\le k\le N\), and let \(E\) be any \(k\)-element subset of the cycle \(C_N\). For the grounded positive operator \(H_E\) defined below, at every mass \(\mu\ge0\), every time \(t>0\), and every exponent \(p>0\), the two objectives

\[
\mathcal H_t(E)=\operatorname{Tr}(e^{-tH_E}),\qquad
\mathcal Z_p(E)=\operatorname{Tr}(H_E^{-p})
\]

are **both minimized** precisely by cyclically balanced pinned-site gaps and **both maximized** precisely by a single nontrivial unpinned arc (the remaining gaps have length one). The optimizing configurations do not depend on \(t\), \(p\), or \(\mu\). The characterization includes exact equality cases and makes no divisibility assumption on \(N\) or \(k\).

For the inverse trace, set \(q=\lfloor N/k\rfloor\) and \(r=N-kq\). Its extreme values are

\[
\min_{|E|=k}\operatorname{Tr}(H_E^{-1})=(k-r)f_\mu(q)+rf_\mu(q+1),\qquad
\max_{|E|=k}\operatorname{Tr}(H_E^{-1})=f_\mu(N-k+1),
\]

where

\[
f_0(g)=\frac{g^2-1}{6},\qquad
f_\mu(g)=\frac{g\coth(g\theta)-\coth\theta}{2\sinh\theta},\quad
\theta=\operatorname{arcosh}(1+\mu/2)>0\quad(\mu>0).
\]

The number of labeled minimizing pin sets is \(\frac Nk\binom{k}{r}\). For \(k<N\), there are \(N\) maximizing sets; for \(k=N\), there is only the complete pin set. For \(k=1\), or \(k=N-1\), the extremal classes coincide and every allowed set is extremal.

## Assumptions and scope

The unweighted simple cycle \(C_N\) has vertices \(\mathbb Z/N\mathbb Z\), each of degree two. Its combinatorial Laplacian \(L=2I-A\) is the positive semidefinite difference operator with nearest-neighbor adjacency \(A\). Fix a set \(E\) of pinned vertices and write \(U=V\setminus E\). The grounded matrix is

\[
H_E=(L+\mu I)_{U,U},\qquad \mu\ge0.
\]

For \(U=\varnothing\) all traces are defined as zero. Otherwise, since \(E\ne\varnothing\), \(H_E\) is positive definite even at \(\mu=0\), so every real power is well-defined by ordinary finite-dimensional spectral calculus.

Read the \(k\) pinned sites cyclically. Their clockwise distances are positive integers \(g_1,\ldots,g_k\) with \(\sum_i g_i=N\). A gap of length \(g_i\) contains \(g_i-1\) unpinned vertices. The grounded matrix splits orthogonally into path blocks

\[
H_E\cong\bigoplus_{i=1}^k T_{g_i-1}(\mu),\quad
T_n(\mu)=(2+\mu)I_n-A_n,
\]

where \(A_n\) is path adjacency and \(T_0\) is the empty matrix. The special case \(k=1\) is one path of \(N-1\) vertices.

## Proof

**1. A discrete convexity lemma for every spectral parameter.** Let \(A_n\) be path adjacency, \(A_0\) empty. For an integer \(m\ge0\), a closed walk of length \(2m\) has a sequence \(w\in\{-1,+1\}^{2m}\) with zero total displacement. Put \(s_0=0\), \(s_j=\sum_{h=1}^{j}w_h\), and let \(R(w)=\max_j s_j-\min_j s_j\). There are exactly \((n-R(w))_+=\max\{n-R(w),0\}\) valid starting sites on the path with \(n\) vertices. Hence

\[
\operatorname{Tr}(A_n^{2m})
=\sum_{\substack{w\in\{-1,+1\}^{2m}\\\sum_jw_j=0}}
(n-R(w))_+,
\qquad \operatorname{Tr}(A_n^{2m+1})=0.
\]

For every integer \(R\ge0\), the map \(n\mapsto(n-R)_+\) is discretely convex: its centered difference \(F(n+1)-2F(n)+F(n-1)\) is nonnegative. It is strictly positive at \(n=R\ge1\). In particular, for each integer \(n\ge1\), the balanced word with \(n\) upward steps followed by \(n\) downward steps has range \(n\), so

\[
\Delta^2\operatorname{Tr}(A_n^{2n})>0.
\]

This proves a strict discrete second-difference witness at every path length, with no asymptotic approximation.

**2. Positive expansions.** Write \(a=2+\mu\). The trace of the heat operator is the absolutely convergent series

\[
F_t(n):=\operatorname{Tr}(e^{-tT_n(\mu)})
=e^{-at}\sum_{m\ge0}\frac{t^{2m}}{(2m)!}\operatorname{Tr}(A_n^{2m}).
\]

Every coefficient is nonnegative, and the witness at \(m=n\) makes \(\Delta^2F_t(n)>0\) for all integer \(n\ge1\), \(t>0\). Similarly, \(\|A_n\|=2\cos(\pi/(n+1))<2\le a\) for \(n\ge1\), so for any \(p>0\) the binomial series converges absolutely in operator norm and yields

\[
G_p(n):=\operatorname{Tr}(T_n(\mu)^{-p})
=a^{-p}\sum_{m\ge0}\frac{(p)_{2m}}{(2m)!a^{2m}}\operatorname{Tr}(A_n^{2m}),
\]

with \((p)_j=p(p+1)\cdots(p+j-1)\), \((p)_0=1\). Every coefficient is strictly positive. The same witness gives \(\Delta^2G_p(n)>0\) for all integer \(n\ge1\). Both functions vanish at \(n=0\).

**3. All equality cases by gap transfers.** Set \(f(g)=F_t(g-1)\) or \(f(g)=G_p(g-1)\) for integers \(g\ge1\). Strict discrete convexity means successive increments \(f(g+1)-f(g)\) strictly increase. If two positive gaps satisfy \(b-a\ge2\), replacing \((a,b)\) by \((a+1,b-1)\) strictly **decreases** \(f(a)+f(b)\). Iterating proves that the unique minimizing gap multiset consists of \(k-r\) copies of \(q\) and \(r\) copies of \(q+1\). In the opposite direction, transferring one unit from a gap of length at least two to a gap at least as long increases the sum strictly; iterating proves that the unique maximizing gap multiset has \(k-1\) copies of one and a single copy of \(N-k+1\). These gap multisets are realizable by pinned vertex sets. A cyclic ordering of the balanced lengths and a starting pinned vertex specify such a set; counting the \(N\binom{k}{r}\) anchored descriptions and dividing by the \(k\) choices of anchor proves the claimed labeled minimum count. The maximum count follows from positioning its unique long arc, with the complete-pin case handled separately.

**4. Explicit inverse-trace endpoint.** For \(\mu>0\), let \(\cosh\theta=1+\mu/2\). The standard inverse of the tridiagonal Dirichlet block \(T_n(\mu)\) has diagonal entries

\[
(T_n(\mu)^{-1})_{jj}=
\frac{\sinh(j\theta)\sinh((n+1-j)\theta)}{\sinh\theta\,\sinh((n+1)\theta)}
\quad (1\le j\le n).
\]

Summing at \(n=g-1\), use \(2\sinh(j\theta)\sinh((g-j)\theta)=\cosh(g\theta)-\cosh((2j-g)\theta)\) and \(\sum_{j=1}^{g-1}\cosh((2j-g)\theta)=\sinh((g-1)\theta)/\sinh\theta\). These exact identities give \(f_\mu(g)=[g\coth(g\theta)-\coth\theta]/(2\sinh\theta)\). At \(\mu=0\), the continuous limit or the usual discrete Green diagonal \(j(g-j)/g\) yields \(\sum_{j=1}^{g-1}j(g-j)/g=(g^2-1)/6\). The gap extremal formulas now follow from Step 3. This completes the proof.

## Verification

The accompanying `check.py` independently assembles grounded cycle matrices and enumerates every pin mask for \(3\le N\le10\), checking the minimum and maximum gap patterns at two positive heat times, three inverse-power exponents and three masses. It also checks the exact inverse-trace formula. It reports `CYCLE_SPECTRAL_EXTREMAL_CHECK_OK 67056` in the supplied environment with NumPy. This finite diagnostic supports, but does not replace, the proofs for arbitrary cycle size and real parameters.

## Relationship to prior work

Fitch and Leonard's *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks* gives a noise-free cyclic leader-placement theorem for the **unshifted inverse trace at exponent one** when the number of sites is divisible by the number of leaders (Theorem 3, Appendix B, p. 19 in the arXiv PDF). Its formula is a special case of the present explicit inverse-trace result. The substantive claim here is simultaneous exact optimality and strict equality classification **for every positive heat time, every positive inverse power, all nonnegative masses, and all integer cardinalities**, together with the opposing worst-case classification. It is not a claim to have originated the balanced-leader principle or the zero-mass inverse-trace case.

Giribet and Feldberg analyze augmented dynamical sampling with unknown forcing, Gaussian covariance and sensor geometry. Their setting motivates asking for geometry-independent optimal sensor masks but does not assert the pinned-cycle Dirichlet spectral trace theorem. Tsuzurugi studies masked stationary Gaussian reconstruction on a ring, emphasizing that posterior trace depends on mask geometry; the model uses a circulant prior with finite-noise observations and reports reference experiments, not this exact all-parameter hard-pinning optimization. Operator inequalities and spectral-graph majorization may admit alternative equivalent formulations; the literature comparison does not establish absolute priority.

## Limitations

The graph has uniform unit edge weights and a homogeneous nonnegative diagonal shift; arbitrary weighted cycles, unequal pinning strengths, noisy rather than exact pinning and general circulant covariances are not covered. The result concerns traces of the **grounded** Dirichlet semigroup and inverse powers, not traces of a full-cycle posterior under finite observational noise. Finite checks do not certify the infinite family, and no independent mathematical audit has been performed.

## References

1. J. I. Giribet and S. Feldberg, *Augmented Dynamical Sampling under unmodeled Forcing*, arXiv:2611.17137v1 (publicly posted 12 November 2026), https://arxiv.org/html/2611.17137v1.
2. K. Fitch and N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569, Appendix B, Theorem 3, https://arxiv.org/pdf/1407.1569.
3. J. Tsuzurugi, *Finite-Mask Gaussian-Process Reconstruction on a Periodic Sensor Ring: Mask-Geometry Dependence, Fourier-Mode Coupling, and Posterior Trace*, arXiv:2609.14007, https://arxiv.org/abs/2609.14007.
4. R. Wang, X. Zhou, W. Li, and Z. Zhang, *Maximizing the Smallest Eigenvalue of Grounded Laplacian Matrix*, arXiv:2110.12576, https://arxiv.org/abs/2110.12576 (a distinct extremal spectral objective).
