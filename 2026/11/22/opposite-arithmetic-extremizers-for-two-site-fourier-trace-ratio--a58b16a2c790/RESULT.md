# Opposite arithmetic extremizers for two-site Fourier trace ratios on finite groups

## Finding
Let \(G\) be any finite group of order \(n\ge2\). For every nonzero function \(f:G\to\mathbb C\), write
\[
\mathcal R_G(f)=\frac{\sum_{\pi\in\widehat G}d_\pi\|\widehat f(\pi)\|_{S_1}}{\sqrt n\,\|f\|_{\ell^2(G)}},\qquad
\widehat f(\pi)=\sum_{z\in G}f(z)\pi(z)^*.
\]
Here \(\widehat G\) is a full set of irreducible unitary representations, \(d_\pi\) their dimensions, and \(\|\cdot\|_{S_1}\) the sum of singular values. This normalization gives \(\mathcal R_G(\delta_x)=\sqrt n\) and agrees with the counting-norm Fourier \(\ell^1/\ell^2\) ratio on abelian groups.

For any **exact two-site signal** \(f=a\delta_x+b\delta_y\), with \(x\ne y\), \(ab\ne0\), and \(m=\operatorname{ord}(x^{-1}y)\), the exact formula is
\[
\mathcal R_G(f)=\frac{\sqrt n}{m\sqrt{|a|^2+|b|^2}}
\sum_{j=0}^{m-1}|a+b e^{2\pi i j/m}|.
\tag{1}
\]
Consequently the sharp complex-coefficient minimum at a fixed separation order is
\[
\min_{a,b\in\mathbb C^\times}\mathcal R_G(a\delta_x+b\delta_y)
=\sqrt n\,C_m,\qquad C_m=\frac{\sqrt2}{m}\cot\left(\frac{\pi}{2m}\right).
\tag{2}
\]
Equality in (2) occurs **exactly** for equal magnitudes \(|a|=|b|\) with relative phase \(b/a\in-\mu_m\), where \(\mu_m\) is the group of complex \(m\)-th roots of unity. In particular, the real signed choice \(a=-b\ne0\) is extremal for every \(m\).

If the coefficients are required to be strictly positive real numbers, the sharp fixed-order minimum is instead
\[
\min_{a,b>0}\mathcal R_G(a\delta_x+b\delta_y)=\sqrt n\,D_m,
\qquad
D_m=\begin{cases}
\displaystyle\frac{\sqrt2}{m}\cot\left(\frac{\pi}{2m}\right),&m\text{ even},\\[5pt]
\displaystyle\frac{\sqrt2}{m}\csc\left(\frac{\pi}{2m}\right),&m\text{ odd}.
\end{cases}
\tag{3}
\]
Equality in (3) occurs exactly when \(a=b\).

Write \(p\) for the least prime divisor of \(n\), and \(M\) for the largest order of an element of \(G\) (not necessarily the exponent of \(G\)). The **unrestricted two-site** complex minimum is \(\sqrt n C_p\), attained precisely at separation order \(p\) and the phases in (2). The **positive two-site** minimum is
\[
\boxed{\begin{cases}
\sqrt{n/2},&n\text{ even},\\[2pt]
\displaystyle\sqrt n\,\frac{\sqrt2}{M}\csc\left(\frac{\pi}{2M}\right),&n\text{ odd}.
\end{cases}}
\tag{4}
\]
For even \(n\), the positive minimizers have separation order two and equal coefficients; for odd \(n\), they have separation order \(M\) and equal coefficients. Thus on every odd-order group, allowing coefficient cancellation favors **smallest-prime-order** separations, whereas positive coefficients favor **largest-realized-order** separations. Their optimal two-site Fourier ratios reveal distinct arithmetic information about the group.
For example, in the nonabelian group of order \(21\) given by \(C_7times C_3\), the signed minimum occurs at an element of order three, whereas the positive minimum occurs at an element of order seven.

## Assumptions and scope
All groups are finite, with no commutativity assumption. The signal support consists of exactly two distinct group elements. The trace norm includes representation-dimension multiplicity as written; it is not the number of nonzero Fourier blocks and it is not the rank-weighted support. Coefficient phases are arbitrary for the complex assertion, and strictly positive real for the positive assertion. All minima are attained within the specified nonzero coefficient classes.

## Proof
**1. Exact nonabelian reduction.** Left translation reduces the support to the identity and an element \(g\) of order \(m\), without changing any singular values. In the regular representation, the Fourier multiplier \(aI+b\pi(g)^*\) appears with multiplicity \(d_\pi\). The right-regular action of \(g\) consists of \(n/m\) disjoint cycles of length \(m\). The eigenvalues of each cycle are all \(m\)-th roots of unity once. Since \(g\) is represented unitarily, its spectral decomposition is normal and the singular values of \(aI+b\pi(g)^*\) are \(|a+b\zeta|\). Summing across the regular representation proves (1). Replacing \(g\) by \(g^{-1}\) only permutes roots.

**2. Coefficient balancing.** Divide by the common coefficient norm and write \(\lambda=2|ab|/(|a|^2+|b|^2)\in(0,1]\), with phase \(\phi=\arg(b/a)\). Apart from the common factor \(\sqrt n\), (1) becomes
\[
F_m(\lambda,\phi)=\frac1m\sum_{j=0}^{m-1}\sqrt{1+\lambda\cos(\phi+2\pi j/m)}.
\]
For each fixed \(\phi\), this is concave in \(\lambda\in[0,1]\), with right derivative \(F_m'(0,\phi)=0\) since the roots of unity sum to zero. Therefore \(F_m(\lambda,\phi)\ge F_m(1,\phi)\). The inequality is strict for \(\lambda<1\) whenever at least one cosine is nonzero, because at least one square-root summand is strictly concave. The only exceptional situation (the two roots at perpendicular phase when \(m=2\)) has \(F_m\equiv1\), larger than the eventual minimum \(1/\sqrt2\). Hence all minimizers have \(|a|=|b|\); the same argument with phase zero proves the positive-coefficient balance.

**3. Sharp phase.** At balanced amplitudes, let \(t=\phi/2\). Then
\[
F_m(1,\phi)=\frac{\sqrt2}{m}\sum_{j=0}^{m-1}|\cos(t+\pi j/m)|.
\]
On each open interval between its finitely many cosine zeros, the displayed sum \(S(t)\) satisfies \(S''(t)=-S(t)<0\), because the cosine signs are fixed and \(S(t)>0\). Thus an interval interior has no local minimum: all minima occur exactly at a zero of at least one summand. Periodicity and cyclic permutation show all those zero locations give the same value. They correspond precisely to \(b/a\in-\mu_m\). At such a zero, elementary geometric summation gives
\[
\sum_{j=0}^{m-1}|1-e^{2\pi ij/m}|
=2\sum_{j=1}^{m-1}\sin(\pi j/m)
=2\cot(\pi/(2m)),
\]
proving (2) and its complete equality cases.

**4. Positive coefficients.** With phase zero and balanced amplitudes, the cosine modulus sum is
\[
\sum_{j=0}^{m-1}|\cos(\pi j/m)|=
\begin{cases}
\cot(\pi/(2m)),&m\text{ even},\\
\csc(\pi/(2m)),&m\text{ odd}.
\end{cases}
\]
This follows by pairing angles around \(\pi/2\) and summing the resulting finite geometric progression. The balancing argument gives strict uniqueness of \(a=b\), and (3) follows.

**5. Optimize element orders.** Set \(x=\pi/(2m)\). The function \(x\cot x\) is strictly decreasing for \(0<x\le\pi/4\), because \(\sin x\cos x<x\). Hence \(C_m=(2\sqrt2/\pi)x\cot x\) is strictly increasing with \(m\). By Cauchy's theorem the smallest nonidentity element order in \(G\) is \(p\), so (2) gives the complex result.

For odd \(m\), \(D_m=(2\sqrt2/\pi)x\csc x\), which strictly decreases as \(m\) increases, because \(\sin x-x\cos x>0\). If \(n\) is odd, all orders are odd, so the minimizing order is the largest actual element order \(M\). If \(n\) is even, an order-two element exists and \(C_2=1/\sqrt2\). Every even \(m>2\) has \(D_m=C_m>C_2\), and every odd \(m\ge3\) has \(D_m\ge\lim_{j\to\infty}D_{2j+1}=2\sqrt2/\pi>1/\sqrt2\). Therefore order two uniquely minimizes the positive problem for even \(n\). This proves (4) and all equality classifications.

## Verification
The accompanying standard-Python checker recomputes the root-of-unity sums for orders \(2\le m\le120\), verifies exact trigonometric constants to numerical precision, tests randomized nonbalanced phases, and checks cyclic regular representations for orders up to 34. When NumPy is installed it additionally constructs the regular permutation matrices of the nonabelian group \(S_3\) and compares their singular-value sums with the formula. It reports `VERIFY_OK` (16,004 supplementary checks in the packaged environment). These finite tests do not prove the all-group classification; the analytic steps above do.

## Relationship to prior work
Iosevich–Hovhannisyan–Keyshams–Vagharshakyan (2026) study Fourier-ratio classes on cyclic groups, and Iosevich–Li–Yu (2026) connect the Fourier ratio to synthesis and Fourier-algebra norms; neither accessible manuscript states the exact nonabelian two-site trace-norm spectrum and signed-versus-positive optimization. The public result *Exact two-spike rank-support law on arbitrary finite groups* classifies zero singular values, using the same regular-representation cyclic reduction, but its rank-counting statement does not determine the sum of all singular values in (1) or the opposite order extrema. The public note *Exact two-frequency \(L^1\) concentration on every cyclic group* contains the elementary equal-sign cosine sum in (3), but solves a different fixed-idempotent point concentration problem; it does not determine the free-phase trace-norm minimum or the optimal element orders on arbitrary nonabelian groups. Thus the cyclic reduction and cosine identities themselves are not claimed new; the exact coefficient-sensitive trace-ratio optimization and arithmetic reversal are the asserted contribution.

## Limitations
The result concerns exact support two, not larger supports or arbitrary Fourier \(\ell^p\) ratios. The distinction in (4) for positive signals refers to *largest realized element order*, not group exponent; these can differ. For even group order the signed/positive optimal element orders coincide. Previously unindexed harmonic-analysis treatments may already contain an equivalent two-atom trace-norm minimization; this priority risk is not excluded. No independent mathematical audit has been carried out.

## References
1. A. Iosevich, V. Hovhannisyan, Z. Keyshams, A. Vagharshakyan, *Metric entropy of Fourier ratio classes on \(\mathbb Z_N\)*, arXiv:2606.24229, first public 2026-06-23, https://arxiv.org/abs/2606.24229.
2. A. Iosevich, Z. Li, K. Yu, *Spectral synthesis with the complexity parameter in \(\mathbb Z_N^d\)*, arXiv:2609.25404, first public 2026-09-21, https://arxiv.org/abs/2609.25404.
3. *Exact two-spike rank-support law on arbitrary finite groups*, public mathematical research record (2026-10-11), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-two-spike-rank-support-law-on-arbitrary-finite-groups--29d4924b2b7c.
4. *Exact two-frequency \(L^1\) concentration on every cyclic group*, public mathematical research record (2026-10-04), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-two-frequency-l-1-concentration-on-every-cyclic-group--aabfaa5078e3.
