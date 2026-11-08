# Arithmetic resonance dichotomy and logarithmic correction for two-orbit collision fluctuations

## Finding
Let \(a,b\ge2\) be integers, \(X,Y\) be **independent** Haar-uniform points on \(\mathbb T=\mathbb R/\mathbb Z\), and \(s>0\). For every integer \(N>2s\), let
\[
K_N=\sum_{i,j=0}^{N-1}\mathbf1_{\{\|a^iX-b^jY\|_{\mathbb T}\le s/N\}}.
\]
Then \(\mathbb EK_N=2sN\). The fluctuation law has a sharp arithmetic dichotomy.

**Multiplicatively independent bases.** If \(a^r\ne b^t\) for every pair of positive integers \(r,t\), then at every admissible finite \(N\),
\[
\boxed{\operatorname{Var}K_N=2sN-4s^2.}
\]
This is precisely the variance for the cross-collision count of two independent collections of \(N\) i.i.d. Haar points (not just a matching leading asymptotic).

**Multiplicatively dependent bases.** Otherwise let \((r,t)\) be the unique minimal positive integer solution of \(a^r=b^t=q\); then \(\gcd(r,t)=1\). Put \(\varepsilon=s/N\), and, for each positive integer \(k\), let \(u_k=\{q^k\varepsilon\}\), its fractional part. Define
\[
G_\varepsilon(u)=\min(u,\varepsilon)+\max(0,u+\varepsilon-1)-2\varepsilon u.
\]
The complete **finite-sample** variance is
\[
\boxed{\operatorname{Var}K_N=N^2(2\varepsilon)(1-2\varepsilon)
+4\sum_{\substack{k\ge1\\kr<N,\,kt<N}}
\frac{(N-kr)(N-kt)}{q^k}G_\varepsilon(u_k).}
\]
In particular, with \(a,b,s\) fixed and \(N\to\infty\),
\[
\boxed{\operatorname{Var}K_N
=2sN\frac{q+1}{q-1}-\frac{8s^2}{\log q}\log N+O_{a,b,s}(1).}
\]
The leading variance inflation is \((q+1)/(q-1)\), and the next-order correction is an explicit **negative logarithm with bounded residual**. The resonance direction \((r,t)\) affects finite-size counts, but neither displayed asymptotic coefficient.

## Assumptions and scope
The two seeds \(X,Y\) are independent; positions along each individual orbit are deterministically dependent. The distance is the circular metric \(\|z\|_{\mathbb T}=\min_{m\in\mathbb Z}|z-m|\). The statistic includes all \(N^2\) cross-index pairs, including \(i=j\); there is no distinguished diagonal between independent orbits. The threshold is strictly \(0<s/N<1/2\); the endpoint \(N=2s\) is not included. The natural logarithm occurs in the asymptotic formula. Only variance is claimed; no fluctuation-distribution or central-limit assertion is made.

## Proof
**1. Mean and rank-two orthogonality.** Write \(\chi_\varepsilon(z)=\mathbf1_{\{\|z\|_{\mathbb T}\le\varepsilon\}}\) and \(Z_{ij}=a^iX-b^jY\pmod1\). Because \(X,Y\) are independent Haar-uniform, each \(Z_{ij}\) is uniform on \(\mathbb T\), with \(\mathbb E\chi_\varepsilon(Z_{ij})=p:=2\varepsilon\). Thus \(\mathbb EK_N=N^2p=2sN\).

For two distinct index pairs \((i,j)\ne(i',j')\), consider the integer matrix
\[
A=\begin{pmatrix}a^i&-b^j\\a^{i'}&-b^{j'}\end{pmatrix}.
\]
If its determinant is nonzero, the torus endomorphism \((X,Y)\mapsto(Z_{ij},Z_{i'j'})\) is surjective; the image of Haar measure is Haar measure on \(\mathbb T^2\). Therefore its two coordinates are independent and the indicator covariance vanishes **exactly**, including for events sharing either orbit index. The determinant vanishes precisely when \(a^{i'-i}=b^{j'-j}\) (integer exponents are allowed). Since \(a,b>1\), a nontrivial equality requires both differences nonzero with the same sign. If there are no common positive powers, all off-diagonal indicator covariances vanish and the independent-bases variance follows.

**2. Resonant pairs.** If \(a^r=b^t=q\) with minimal positive solution \((r,t)\), every nonzero integer solution of \(a^u=b^v\) is \((u,v)=k(r,t)\). To see this, take logarithms: the positive ratio \(u/v=\log b/\log a\) is rational, and its numerator and denominator in lowest terms are \(r,t\). Thus the sole possible dependent indicator pairs have displacements \((\pm kr,\pm kt)\). For each \(k>0\) with \(kr,kt<N\), there are \((N-kr)(N-kt)\) **unordered** indicator pairs with positive displacement. Their two phase variables have the same joint law as \((U,q^kU)\) for one uniform \(U\in\mathbb T\).

**3. Exact single-resonance covariance.** For any integer \(Q\ge2\), put \(m=\lfloor Q\varepsilon\rfloor\) and \(u=\{Q\varepsilon\}\). By the substitution \(z=QU\), and periodicity of the indicator, the intersection of the two short circular windows has probability
\[
I_Q(\varepsilon)=\Pr\{\|U\|_{\mathbb T}\le\varepsilon,\ \|QU\|_{\mathbb T}\le\varepsilon\}
=\frac2Q\left(2\varepsilon m+\min(u,\varepsilon)+\max(0,u+\varepsilon-1)\right).
\]
Indeed, integration over \([-Q\varepsilon,Q\varepsilon]\) consists of \(m\) full unit intervals on each side, plus partial boundary intervals; the latter contribute the two displayed overlap terms. Subtracting \(p^2=4\varepsilon^2\) gives the exact covariance
\[
c_Q(\varepsilon)=I_Q(\varepsilon)-p^2=\frac2QG_\varepsilon(\{Q\varepsilon\}).
\]
The elementary bounds on the two overlap terms yield \(|G_\varepsilon(u)|\le2\varepsilon\), so
\[|c_Q(\varepsilon)|\le4\varepsilon/Q.\]
If \((Q+1)\varepsilon\le1\), then \(m=0\), \(u=Q\varepsilon\in[\varepsilon,1-\varepsilon]\); hence the sharper exact identity
\[
c_Q(\varepsilon)=\frac{2\varepsilon}{Q}-4\varepsilon^2.
\]

**4. Finite variance formula.** The \(N^2\) diagonal contributions to the variance of \(K_N\) are \(N^2p(1-p)\). Every non-resonant off-diagonal contribution is zero by Step 1. The \((N-kr)(N-kt)\) unordered resonances in Step 2 each contribute twice their covariance to the ordered covariance sum. Inserting Step 3 produces exactly the boxed finite formula. For two i.i.d. uniform point collections, distinct cross-collision indicators are likewise uncorrelated: when two events share one endpoint, conditioning on that endpoint leaves both with constant success probability \(p\). This verifies the stated independent benchmark without asserting joint independence.

**5. Sharp asymptotics including the logarithm.** Set \(\varepsilon=s/N\) and
\[
T_N=\left\lfloor\log_q\left(\frac{1-\varepsilon}{\varepsilon}\right)\right\rfloor.
\]
For sufficiently large \(N\), \(T_N<\min((N-1)/r,(N-1)/t)\), and \((q^k+1)\varepsilon\le1\) for every \(1\le k\le T_N\). Consequently the resonant contribution for these \(k\) equals
\[
\sum_{k=1}^{T_N}2(N-kr)(N-kt)\left(\frac{2\varepsilon}{q^k}-4\varepsilon^2\right).
\]
The first portion of the sum is
\[
4\varepsilon\sum_{k=1}^{T_N}\frac{(N-kr)(N-kt)}{q^k}=\frac{4sN}{q-1}+O_{a,b,s}(1),
\]
since the geometric tails satisfy \(Nq^{-T_N}=O_s(1)\), while \(\sum_{k\ge1}kq^{-k}\) and \(\sum_{k\ge1}k^2q^{-k}\) converge. The negative portion equals
\[
-8\varepsilon^2\sum_{k=1}^{T_N}(N-kr)(N-kt)
=-8s^2T_N+O_{a,b,s}(1)
=-\frac{8s^2}{\log q}\log N+O_{a,b,s}(1).
\]
Finally the covariance bound of Step 3 bounds the entire remaining resonance tail in absolute value by
\[
8\varepsilon N^2\sum_{k>T_N}q^{-k}=O_{a,b,s}(1).
\]
Adding the diagonal variance \(2sN-4s^2\) yields the asserted expansion. In particular the bounded remainder is valid along every integer \(N\to\infty\), without restricting to a subsequence of grid sizes.

## Verification
Run `python3 CHECK.py` using the standalone checker included with this result. It verifies the exact window-intersection formula by *independently constructing all inverse-image arcs* for 55 rational parameters; compares grouped resonance counting against all index-pair determinants for 90 cases covering equal bases, independent bases, and distinct but multiplicatively dependent bases; and tests the bounded-residual asymptotic for 30 larger cases. Output obtained in the packaged check environment:

`VERIFY_OK independent_arc_intersections=55 grouped_pair_covariances=90 asymptotic_residual_tests=30 independent_base_exact=True`

All calculations use `fractions.Fraction` for exact finite-variance assertions. The asymptotic finite-\(N\) residual tests use floating point only for the logarithm; they cannot certify the all-\(N\) asymptotic, which is proved above.

## Relationship to prior work
Baker and Todd (2026) establish almost-sure first-order pair-correlation laws for two independent orbits of mixing interval maps, including expanding examples; their general estimates do not imply the exact second moments or the multiplicative-dependence dichotomy here. Their June 16, 2026 arXiv submission provides the natural dynamical starting point.

The earlier public note *Sharp second-moment inflation for expanding circle-map pair correlations* (2026) proves the leading unsmoothed variance constant for **pairs within a single orbit from one seed**. Its Bernoulli-polynomial covariance kernel is a closely related calculation, but its single-seed two-frequency dependence is different from the rank-two torus-character dichotomy here. Neither its theorem nor a direct special case gives the present exact cross-orbit variance, arithmetic classification for distinct bases, or sharp logarithmic correction. The general method of Fourier/Haar covariance calculation is not asserted to be novel.

Rudnick and Zaharescu (1999/2002) and later Rudnick–Technau and Chaubey–Yesha establish metric lacunary pair-correlation laws and variance bounds; their inspected results do not determine the exact cross-orbit constants above.

## Limitations
No normal limit law, concentration inequality, or almost-sure convergence rate is proved. Distinct starting points must be independent and Haar distributed. The argument depends on integer expanding multipliers and circular, not interval, distance; arbitrary real expansion factors, dependent initial seeds and varying radii need separate analysis. The negative logarithmic correction is a statement about unnormalized cross counts \(K_N\), not automatically about within-orbit counts. Historical originality is supported by inspected primary sources and comparable published claims, but an unindexed earlier exact calculation cannot be ruled out.

## References
1. S. Baker and M. Todd, *Pair correlation statistics for dynamical systems*, arXiv:2606.17880, originally submitted June 16, 2026; Theorem A and Section 2. https://arxiv.org/abs/2606.17880
2. *Sharp second-moment inflation for expanding circle-map pair correlations* (2026), existing public single-orbit variance result. https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-sharp-second-moment-inflation-for-expanding-circle-map-pair-corr--d5c688b954c6/RESULT.md
3. Z. Rudnick and A. Zaharescu, *The distribution of spacings between fractional parts of lacunary sequences*, arXiv:math/9912103, especially Section 4. https://arxiv.org/abs/math/9912103
4. Z. Rudnick and N. Technau, *The metric theory of the pair correlation function of real-valued lacunary sequences*, arXiv:2001.08820. https://arxiv.org/abs/2001.08820
5. S. Chaubey and N. Yesha, *The distribution of spacings of real-valued lacunary sequences modulo one*, arXiv:2108.00431. https://arxiv.org/abs/2108.00431
