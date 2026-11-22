# The first Hausdorff-moment obstruction for quadratic 3-isometric Cauchy duals has an exponential onset

## Finding

The first *finite difference* that detects failure of the Hausdorff moment condition for a natural quadratic weighted-shift Cauchy dual can be identified at every parameter, and its required order grows exponentially as the quadratic discriminant approaches zero from below. This is a finite-test localization result, not a new qualitative criterion for subnormality.

For \(a,b>0\) with \(4b>a^2\), define \(P(n)=1+an+bn^2\), \(u=a/(2b)\) and \(v=\sqrt{4b-a^2}/(2b)\). For integers \(n,k\ge0\) set
\[
 m_n=\frac1{P(n)},\qquad
 D_{n,k}=\sum_{j=0}^{k}(-1)^j\binom{k}{j}m_{n+j},\qquad
 \Theta_{n,k}=\sum_{j=0}^{k}\arctan\!\frac{v}{u+n+j}.
\]
Then the following identity is exact, including its sign:
\[
 \boxed{D_{n,k}=\frac{k!\sin\Theta_{n,k}}{bv\prod_{j=0}^{k}\sqrt{(u+n+j)^2+v^2}}.}
\]
The smallest order at which *any* Hausdorff difference is negative, allowing every starting index, is
\[
 \boxed{K(u,v)=\min\{k\in\mathbb Z_{\ge0}:\Theta_{0,k}>\pi\}.}
\]
In particular, \(D_{n,k}\ge0\) for every \(n\ge0\) and \(k<K(u,v)\), while \(D_{0,K(u,v)}<0\). The minimum exists for every \(u,v>0\).

For fixed \(u>0\) and \(v\downarrow0\), impose the normalization \(P(0)=1\) by setting \(b=(u^2+v^2)^{-1}\) and \(a=2u/(u^2+v^2)\). The precise onset law is
\[
 \boxed{\log K(u,v)=\frac\pi v+\psi(u)+\frac{v^2}{3}\zeta(3,u)+O_u(v^4).}
\]
Consequently \(K(u,v)e^{-\pi/v}\to e^{\psi(u)}\). Here \(\psi\) is the logarithmic derivative of Euler's gamma function and \(\zeta(3,u)=\sum_{j\ge0}(u+j)^{-3}\).

## Assumptions and scope

Let \(\ell^2(\mathbb Z_{\ge0})\) have its canonical orthonormal basis \((e_n)\). Let \(W\) be the unilateral positive weighted shift
\[
 We_n=\sqrt{\frac{P(n+1)}{P(n)}}\,e_{n+1},\qquad P(n)=1+an+bn^2,\quad a,b>0.
\]
Since all weights exceed one, are bounded, and have infimum at least one, \(W^*W\) is invertible. Its Cauchy dual is \(V=W(W^*W)^{-1}\). The convention is \(\Delta f(n)=f(n+1)-f(n)\), so \(D_{n,k}=(-1)^k\Delta^km_n\).

For every \(q,n\ge0\), \(\|W^ne_q\|^2=P(q+n)/P(q)\). Its third discrete difference in \(n\) is zero, and its second difference equals \(2b/P(q)>0\), proving that \(W\) is a strict 3-isometry. Its Cauchy dual has reciprocal weights, is a contraction, and \(\|V^ne_0\|^2=1/P(n)\). The result concerns the precise first failure of the complete-monotonicity tests, **not** the earliest failure of other matrix-positivity tests. All indices in the theorem are nonnegative integers. The strict condition \(4b>a^2\) is essential to the phase formula; real-rooted quadratics belong to the previously classified completely monotone regime.

## Proof

**Exact phase identity.** Since \(P(z)=b(z+u-iv)(z+u+iv)\), partial fractions give
\[
 \frac1{P(n)}=\frac1{2ibv}\left(\frac1{n+u-iv}-\frac1{n+u+iv}\right).
\]
For any complex \(c\) with positive real part, induction on \(k\) yields
\[
 (-1)^k\Delta^k\frac1{n+c}
 =\frac{k!}{\prod_{j=0}^{k}(n+c+j)}.
\]
Apply this to the conjugate pair \(c=u\pm iv\). The reciprocal product with negative imaginary parts has positive argument \(\Theta_{n,k}\) and absolute value \(\prod_{j=0}^{k}((u+n+j)^2+v^2)^{-1/2}\). Subtracting the conjugate products produces exactly the displayed sine formula. Every factor outside its sine is strictly positive.

**Minimality of the witness.** For fixed \(k\), every summand in \(\Theta_{n,k}\) decreases strictly as \(n\) grows, so \(0<\Theta_{n,k}\le\Theta_{0,k}\). The sum \(\Theta_{0,k}\) increases strictly with \(k\) and diverges, because \(\arctan(v/(u+j))\sim v/j\). Let \(K\) be its first index above \(\pi\). When \(k<K\), all phases \(\Theta_{n,k}\) lie in \((0,\pi]\); hence all associated finite differences are nonnegative. At \(k=K\), \(\pi<\Theta_{0,K}<\pi+\pi/2\) because the final angle is strictly less than \(\pi/2\). Thus \(D_{0,K}<0\). This proves both existence and global minimality across starting indices, including possible exact equality at a preceding order.

**Near-boundary asymptotics.** For fixed \(u>0\), the Taylor expansion of \(\arctan\) gives, uniformly in \(k\),
\[
 \Theta_{0,k}
 =v\sum_{j=0}^{k}\frac1{u+j}
 -\frac{v^3}{3}\sum_{j=0}^{k}\frac1{(u+j)^3}
 +O_u(v^5).
\]
The uniform remainder follows from \(\sum_{j\ge0}(u+j)^{-5}<\infty\). The defining crossing gives
\[
 0<\Theta_{0,K}-\pi\le\arctan\frac{v}{u+K}\le\frac{v}{u+K}.
\]
Use \(\sum_{j=0}^{K}(u+j)^{-1}=\psi(u+K+1)-\psi(u)\) and \(\sum_{j=0}^{K}(u+j)^{-3}=\zeta(3,u)+O_u(K^{-2})\). The inequality \(\Theta_{0,K}\le v\sum_{j=0}^K(u+j)^{-1}\), together with \(\Theta_{0,K}>\pi\), forces \(K\ge\exp(\pi/v-O_u(1))\). Hence the errors from finite \(K\) are smaller than any fixed power of \(v\). Since \(\psi(u+K+1)=\log K+O_u(K^{-1})\), division of the phase relation by \(v\) yields
\[
 \log K=\frac\pi v+\psi(u)+\frac{v^2}{3}\zeta(3,u)+O_u(v^4).
\]
This completes the proof.

## Verification

The accompanying `verify_first_failure.py` reproduces 588 finite checks using rational arithmetic for alternating differences and independent numerical evaluations of the angles. It also checks six exact first-witness indices and four near-critical scale comparisons. In particular \(K(1,1)=16\), \(K(1,1/2)=328\), and \(K(1,1/4)=164953\). The script tests finitely many instances only; the argument above proves the theorem for all admissible parameters and all orders.

To reproduce: `python verify_first_failure.py` using only Python's standard library.

## Relationship to prior work

Jabłoński, Jung, Pietrzycki and Stochel (2026), Example 6.3, explicitly construct 3-isometric unilateral shifts from degree-two polynomial orbit norms. Their concern is CPD roots and operator classes, not finite-order obstructions in the reciprocal moment sequence. Nailwal (2024), Lemma 2.2, already proves the qualitative fact that a reciprocal quadratic with positive coefficients is completely monotone precisely when its roots are real. That qualitative discriminant criterion is **prior work**, and this result does not claim it as new. Anand and Chavan (2016), in their proof of the module-tensor-product theorem, analyze conjugate poles and sign-changing representing densities for non-Hausdorff sequences; they do not determine the globally first violated order or its exponentially delayed near-critical law. The statements compared differ logically: deciding whether some test eventually fails does not determine which test fails first, nor its sharp parameter-dependent growth.

## Limitations

The exact witness order applies to scalar Hausdorff **alternating finite differences**, not arbitrary truncated Hankel-matrix or other positivity tests, which can have different detection thresholds. The asymptotic fixes \(u>0\) while \(v\to0\); no uniform estimate as \(u\to0\) or \(u\to\infty\) is asserted. The sign formula uses exact real arithmetic; direct high-order binomial sums can be numerically ill-conditioned and the phase representation is preferable. Independent external mathematical validation has not been performed. A broader unindexed formula for first sign changes in rational Hausdorff sequences could imply this result and remains a bibliographic risk.

## References

1. Z. J. Jabłoński, I. B. Jung, P. Pietrzycki, and J. Stochel, *CPD nth roots of subnormal operators are subnormal*, arXiv:2604.10810v1 (first public 12 April 2026), Example 6.3. https://arxiv.org/html/2604.10810v1
2. R. Nailwal, *A complete solution to the Cauchy dual subnormality problem for torally expansive toral 3-isometric weighted 2-shifts*, New York J. Math. 30 (2024), 1517–1533, Lemma 2.2. https://nyjm.albany.edu/j/2024/30-63v.pdf
3. A. Anand and S. Chavan, *Module tensor product of subnormal modules need not be subnormal*, arXiv:1608.08113v1 (2016), Section 2 and proof of Theorem 1.5. https://arxiv.org/pdf/1608.08113
4. M. A. Aouichaoui, M. Buchała, and S. R. Garcia, *On m-partial isometries: spectra, weighted shifts, and similarity*, arXiv:2606.12865v1 (11 June 2026), related shift framework. https://arxiv.org/abs/2606.12865v1
