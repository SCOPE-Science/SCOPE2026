# Arithmetic Fourier-zero lattices and Wiener cyclicity for two separated intervals

## Finding
Let \(a,b,d>0\), put \(\Omega=[0,a]\cup[a+d,a+d+b]\), and let \(f=\mathbf 1_\Omega\). With \(\widehat f(\xi)=\int_{\mathbb R}f(x)e^{-2\pi i x\xi}\,dx\), the **complete set of nonzero real Fourier zeros** is the union of the following three explicitly arithmetic families:
\[
\begin{aligned}
Z_0&=\{\xi\ne0: a\xi\in\mathbb Z,\ b\xi\in\mathbb Z\},\\
Z_+&=\{\xi\ne0: (a+b)\xi\in\mathbb Z,\ d\xi\in\mathbb Z\},\\
Z_-&=\{\xi\ne0: (a-b)\xi\in\mathbb Z,\ 2(d+b)\xi\in2\mathbb Z+1\}.
\end{aligned}
\]
Specifically, \(\{\xi\in\mathbb R:\widehat f(\xi)=0\}=Z_0\cup Z_+\cup Z_-\); the origin is never a zero.

Every nonzero real zero is **simple**, except when \(a=b\) and \(a\xi\in\mathbb Z\) and \(2(a+d)\xi\in2\mathbb Z+1\); these and only these exceptional zeros are **double**.

By Wiener's \(L^1(\mathbb R)\) Tauberian theorem, finite linear combinations of all real translates of \(f\) are dense in \(L^1(\mathbb R)\) precisely when **all three families are empty**. For \(a\ne b\), this holds exactly if \(a/b\notin\mathbb Q\), \(d/(a+b)\notin\mathbb Q\), and the ratio \(2(d+b)/(a-b)\) is either irrational or has an even numerator when written in lowest terms. If \(a=b\), the family is never \(L^1\)-cyclic. The cyclic triples \((a,b,d)\) have full Lebesgue measure and form a dense residual subset of the positive parameter octant, while the noncyclic triples are also dense but have measure zero. For every parameter triple, translates of \(f\) are dense in \(L^2(\mathbb R)\).

## Assumptions and scope
All three parameters are strictly positive, so the two bounded intervals are nonempty and disjoint with gap \(d\). Endpoints do not affect the indicator in \(L^1\) or \(L^2\). Frequencies are unrestricted real numbers; zero multiplicity means the complex-analytic order of the entire Fourier transform at a real zero. The \(L^1\)-cyclicity assertion concerns the closed complex linear span of all real translations, not discrete or one-sided translations.

## Proof
Set \(h=d+(a+b)/2>0\). Direct integration, for \(\xi\ne0\), yields
\[
\widehat f(\xi)=\frac{e^{-\pi i a\xi}}{\pi\xi}
\left[\sin(\pi a\xi)+e^{-2\pi i h\xi}\sin(\pi b\xi)\right].
\]
At \(\xi=0\) the Fourier transform is \(a+b>0\). Let the bracketed term be \(G(\xi)\). If both sine factors vanish, precisely \(Z_0\) occurs and \(G=0\), with no condition on \(h\).

Suppose instead that the two sines do not both vanish. A zero of \(G\) implies that neither sine vanishes, their absolute values agree, and the intervening phase \(e^{-2\pi i h\xi}\) equals either \(+1\) or \(-1\). The elementary sine identities give the two mutually exhaustive possibilities
\[
(a-b)\xi=k\in\mathbb Z,\quad
\sin(\pi a\xi)=(-1)^k\sin(\pi b\xi),
\]
or
\[
(a+b)\xi=k\in\mathbb Z,\quad
\sin(\pi a\xi)=(-1)^{k+1}\sin(\pi b\xi).
\]
In the first case cancellation requires \(2h\xi-k\in2\mathbb Z+1\), equivalent to \(2(d+b)\xi\in2\mathbb Z+1\), producing \(Z_-\). In the second, cancellation requires \(2h\xi-k\in2\mathbb Z\), equivalent to \(d\xi\in\mathbb Z\), producing \(Z_+\). Conversely, substituting either set of congruences forces cancellation, even if both sine factors happen to vanish. This proves both inclusions in the asserted union.

For multiplicities, at a zero with nonzero sine factors, the derivative
\[
G'(\xi)=\pi a\cos(\pi a\xi)+\pi b e^{-2\pi i h\xi}\cos(\pi b\xi)
-2\pi i h e^{-2\pi i h\xi}\sin(\pi b\xi)
\]
has a nonzero imaginary part, because the phase is real and \(h\sin(\pi b\xi)\ne0\). Thus the zero is simple. At a common-sine zero, \(G'(\xi)=\pi[a(-1)^m+b(-1)^n e^{-2\pi i h\xi}]\), where \(m=a\xi\) and \(n=b\xi\) are integers. If \(a\ne b\), unequal moduli make this nonzero. For \(a=b\), direct factorization gives
\[
\widehat f(\xi)=\frac{2e^{-\pi i(a+h)\xi}}{\pi\xi}
\sin(\pi a\xi)\cos(\pi h\xi).
\]
Both factors have simple real zeros, so their overlaps are exactly the double zeros \(a\xi\in\mathbb Z\), \(2h\xi=2(a+d)\xi\in2\mathbb Z+1\); no higher order is possible.

For \(a\ne b\), the family \(Z_0\) is nonempty exactly when \(a/b\in\mathbb Q\); \(Z_+\) is nonempty exactly when \(d/(a+b)\in\mathbb Q\). Put \(\rho=2(d+b)/(a-b)\). If \(\rho=P/Q\) in lowest terms, with \(Q>0\), then \(Z_-\ne\varnothing\) exactly when \(P\) is odd: choosing \(\xi=Q/(a-b)\) is sufficient, and any permitted \(\xi\) forces an odd integral multiple of \(\rho\), hence \(P\) odd. Irrational \(\rho\) forbids this family. When \(a=b\), \(Z_-\) is nonempty for all \(d>0\).

These equalities define a countable union of proper affine-linear planes in the positive parameter octant: \(a=rb\), \(d=r(a+b)\), and \(2Q(d+b)=P(a-b)\) for rational or integer parameters as specified, together with \(a=b\). Every plane is null and nowhere dense. The noncyclic set is therefore null and meagre; it is dense because planes \(a=rb\) with positive rational \(r\) are dense among the positive parameter triples. Its complement is full-measure and residual. Applying the classical Wiener Tauberian theorem gives the exact \(L^1\) classification. Finally, \(\widehat f\) is an entire function that is not identically zero (its value at zero is \(a+b\)), so its real zeros have measure zero; the \(L^2\) Wiener criterion gives universal \(L^2\) cyclicity.

## Verification
The self-contained script `check.py` tests the three arithmetic predicates against direct endpoint-exponential evaluation for 9,000 rational parameter-frequency combinations, and checks sample overlapping zeros. Its successful output is supplementary evidence only; the all-parameter proof is the phase/sine argument above. For an explicit cyclic case, take \(a=1\), \(b=\sqrt2\), \(d=\sqrt3\): all three forbidden rational dependencies fail because \(\sqrt3\notin\mathbb Q(\sqrt2)\). The noncyclic equal-length case \(a=b=1\), \(d=1/2\) has double zeros at odd integer frequencies.

## Relationship to prior work
The June 2026 study of Xia and Xu (arXiv:2606.19855) investigates uniqueness from the **full Fourier magnitude** of finite unions of intervals and supplies full-data recovery results for two intervals; it does not, in the accessible abstract and indexed description, state this complete real-zero arithmetic and Wiener-translation-cyclicity classification. The classical Wiener Tauberian theorem supplies the cyclicity criterion, not the parameter-dependent zero-set analysis. Published related studies of Fourier jet recovery and exponential Riesz bases on two intervals concern recovery or basis conditioning rather than all real zeros and their multiplicities.

## Limitations
The claim concerns exactly two unweighted indicator intervals in one dimension with a strictly positive gap; it does not classify more intervals, weighted windows, complex Fourier zeros, discrete translations, or lower bounds for the Fourier amplitude away from its zeros. Fourier zero-free transforms may approach zero arbitrarily closely, so cyclicity is not a uniform conditioning guarantee. The original full text of the motivating 2026 preprint was not accessible during the literature comparison; its abstract and indexed scientific description were inspected. An equivalent older arithmetic treatment of two-interval Fourier zeros or Wiener cyclicity may exist. Independent mathematical validation has not been performed.

## References
1. Y. Xia and Z. Xu, *Fourier Phase Retrieval for Finite Unions of Intervals*, arXiv:2606.19855 (first submitted 2026-06-18), https://arxiv.org/abs/2606.19855.
2. N. Wiener, *Tauberian theorems*, Annals of Mathematics 33 (1932), 1–100. Classical \(L^1\) and \(L^2\) translate-density criteria.
3. *Sharp finite-jet Fourier phase retrieval for two intervals*, published result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-finite-jet-fourier-phase-retrieval-for-two-intervals--361050867db3.
4. *Optimal two-coset Fourier conditioning on separated unit intervals*, published result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-optimal-two-coset-fourier-conditioning-on-separated-unit-interva--1e706b439add.
