# Exact parity dichotomy for sine-product semigroup spectra

## Finding

For every integer \(m\ge 2\), choose distinct primes \(p_2,\ldots,p_m\) and put
\[
\omega_1=1,\qquad \omega_j=\sqrt{p_j}\quad(2\le j\le m),\qquad a_m=\frac12\sum_{j=1}^m\omega_j.
\]
Define
\[
\Lambda_m^+=\left\{a_m+\sum_{j=1}^m n_j\omega_j:n_j\in\mathbb Z_{\ge0}}\right\},\qquad
\Lambda_m=\Lambda_m^+\cup(-\Lambda_m^+),
\]
and use the Fourier convention
\[
\widehat{\varphi}(\xi)=\int_\mathbb R\varphi(x)e^{-2\pi i x\xi}\,dx.
\]
Let
\[
\Phi_m(z)=\prod_{j=1}^m\sin(\pi\omega_j z).
\]
Then the unit-mass counting measure \(\delta_{\Lambda_m}\) is tempered and its Fourier transform has the following exact parity dichotomy.

If \(m\) is odd, then \(\widehat{\delta_{\Lambda_m}}\) is supported on
\[
\Sigma_m=\bigcup_{j=1}^m\omega_j^{-1}\mathbb Z.
\]
At a nonzero pole \(k/\omega_j\), with \(k\in\mathbb Z\setminus\{0}\), its point-mass coefficient is
\[
c_{j,k}=
\frac{2^{1-m}i^{1-m}(-1)^k}
{\omega_j\prod_{\ell\ne j}\sin(\pi k\omega_\ell/\omega_j)}.
\]
At the origin, write the principal Laurent part as
\[
\frac1{\Phi_m(z)}=
\sum_{r=0}^{(m-1)/2} A_r z^{-(2r+1)}+O(z).
\]
Then the origin contribution is
\[
2^{1-m}\pi i^{1-m}
\sum_{r=0}^{(m-1)/2}\frac{A_r}{(2r)!}\,\delta_0^{(2r)}.
\]
The top coefficient is nonzero because
\[
A_{(m-1)/2}=\frac1{\pi^m\prod_{j=1}^m\omega_j}.
\]
Thus the highest derivative present is exactly \(\delta_0^{(m-1)}\).

If \(m\) is even, then on every open interval disjoint from \(\Sigma_m\),
\[
\widehat{\delta_{\Lambda_m}}(x)=\frac{2(2i)^{-m}}{\Phi_m(x)}
\]
as a regular distribution. The right-hand side never vanishes there, hence
\[
\operatorname{supp}\widehat{\delta_{\Lambda_m}}=\mathbb R.
\]
So oddness of the number of sine factors is exactly the condition for this symmetric semigroup construction to have discrete Fourier support.

Finally,
\[
\#(\Lambda_m\cap[-R,R])=
\frac{2R^m}{m!\prod_{j=1}^m\omega_j}+O(R^{m-1}),
\]
so the odd cases give examples with arbitrarily large odd polynomial density degree.

## Assumptions and scope

The primes \(p_2,\ldots,p_m\) are pairwise distinct. This makes \(1,\sqrt{p_2},\ldots,\sqrt{p_m}\) linearly independent over \(\mathbb Q\), so every point of \(\Lambda_m^+\) has a unique nonnegative-coordinate representation. The square-root choice is also used to obtain the quadratic Diophantine estimate needed for polynomial growth of the Fourier coefficients.

The statement concerns the specific symmetric additive-semigroup family above. It does not classify all unbounded-density counting measures with discrete distributional Fourier support, and it does not assert that arbitrary irrational generators have the required temperedness.

## Proof

For \(\operatorname{Im}z>0\), geometric expansion of each reciprocal sine gives
\[
\frac1{\sin(\pi\omega_j z)}=
-2i\sum_{n\ge0}e^{2\pi i(n+1/2)\omega_j z},
\]
while for \(\operatorname{Im}z<0\),
\[
\frac1{\sin(\pi\omega_j z)}=
2i\sum_{n\ge0}e^{-2\pi i(n+1/2)\omega_j z}.
\]
Therefore, if \(T_+\) and \(T_-\) denote the upper and lower boundary values of \(1/\Phi_m\),
\[
T_+=(-2i)^m\sum_{\lambda\in\Lambda_m^+}e^{2\pi i\lambda x},\qquad
T_-=(2i)^m\sum_{\lambda\in\Lambda_m^+}e^{-2\pi i\lambda x}.
\]
Since the Fourier transform of \(\delta_\lambda\) is \(e^{-2\pi i\lambda x}\), this yields the distributional identity
\[
\widehat{\delta_{\Lambda_m}}=(2i)^{-m}\bigl(T_-+(-1)^mT_+\bigr).
\]

When \(m\) is odd this is the jump of the two boundary values. For a simple real pole with residue \(r\), the standard boundary-value formula gives
\[
(x-a-i0)^{-1}-(x-a+i0)^{-1}=2\pi i\,\delta_a.
\]
At \(a=k/\omega_j\ne0\), the residue of \(1/\Phi_m\) is
\[
\frac{(-1)^k}
{\pi\omega_j\prod_{\ell\ne j}\sin(\pi k\omega_\ell/\omega_j)}.
\]
Multiplying by \(2\pi i(2i)^{-m}\) gives the stated \(c_{j,k}\).

At the origin, \(1/\Phi_m\) is odd when \(m\) is odd, so its principal part contains exactly the powers \(z^{-(2r+1)}\). Differentiating the one-pole boundary identity gives
\[
(x-i0)^{-(2r+1)}-(x+i0)^{-(2r+1)}=
\frac{2\pi i}{(2r)!}\delta_0^{(2r)}.
\]
This proves the stated origin formula. The leading Laurent coefficient follows by replacing every sine with its linear term, so the derivative of order \(m-1\) has a nonzero coefficient.

For even \(m\), the same master identity uses the sum \(T_-+T_+\), not the jump. On an interval avoiding all poles both boundary values are the same ordinary function \(1/\Phi_m\), which gives \(2(2i)^{-m}/\Phi_m\). Since \(\Phi_m\) has no zeros off \(\Sigma_m\), this regular part is nonzero on every such interval; every interval in \(\mathbb R\) therefore meets the distributional support, and the support is all of \(\mathbb R\).

It remains to justify temperedness in the odd case. Every ratio \(\alpha=\omega_\ell/\omega_j\) satisfies \(\alpha^2=A/B\) for positive integers \(A,B\) with \(\alpha\notin\mathbb Q\). Hence, for integers \(k\ne0\) and \(n\),
\[
|k\alpha-n|=
\frac{|Ak^2-Bn^2|}{B|k\alpha+n|}\ge \frac{c_\alpha}{|k|}
\]
whenever \(n\) is a nearest integer to \(k\alpha\). Thus
\[
|\sin(\pi k\alpha)|\ge \frac{c'_\alpha}{|k|},
\]
and consequently \( |c_{j,k}|=O(|k|^{m-1})\). The point-mass series therefore converges in \(\mathcal S'(\mathbb R)\).

Finally, counting \(\Lambda_m^+\cap[0,R]\) is counting lattice points in the weighted simplex \(\sum_j\omega_j n_j\le R-a_m\). Comparing unit cubes with the simplex and its fixed-thickness boundary layer gives volume plus \(O(R^{m-1})\), namely \(R^m/(m!\prod_j\omega_j)+O(R^{m-1})\). Symmetry doubles the leading term.

For \(m=3\) with \(\omega=(1,\sqrt2,\sqrt3)\), put \(P=\sqrt6\) and \(Q=6\). The Laurent expansion begins
\[
\frac1{\Phi_3(z)}=
\frac1{\pi^3P}z^{-3}+\frac{Q}{6\pi P}z^{-1}+O(z),
\]
and \(2^{-2}\pi i^{-2}=-\pi/4\). The origin coefficients are therefore exactly
\[
-\frac1{8\pi^2P}\delta_0''-\frac{Q}{24P}\delta_0,
\]
recovering the 2026 source formula.

## Verification

The proof is analytic; finite computation is not used to promote a sampled pattern to an infinite theorem. The standalone checker `verify_parity_dichotomy.py` only replays algebraic sign, coefficient, and low-dimensional sanity checks. In particular it verifies the \(m=3\) origin coefficients against the published formula and checks that the boundary-value prefactor cancels off the pole set exactly for odd \(m\), while it doubles for even \(m\).

The key infinite steps are proved above: the geometric-series boundary identities, the distributional jump formula, the quadratic-irrational Diophantine lower bound, and the weighted-simplex counting estimate.

## Relationship to prior work

Tselishchev, arXiv:2608.09354v1, gives the explicit \(m=3\) example with generators \(1,\sqrt2,\sqrt3\), a \(\delta_0''\) term, and three reciprocal arithmetic progressions. The present statement recovers that formula but identifies a structural parity law for the entire square-root semigroup family: every odd number of factors produces only reciprocal-lattice masses plus even derivatives at the origin, whereas every even number leaves a nonzero regular Fourier component and therefore has full Fourier support.

Olevskii and Ulanovskii classify unit-mass Fourier quasicrystals when both sides are discrete atomic measures. The odd cases here retain derivative terms at the origin, while the even cases have full Fourier support, so that theorem does not subsume the parity dichotomy. Gonçalves classifies crystalline measures under quadratic-decay hypotheses; the present odd transforms are not purely atomic measures because of their origin derivatives, and the density growth is deliberately unbounded.

A public secondary reading of arXiv:2608.09354 explicitly labels the possibility of using more than three odd factors as an editorial extension rather than a theorem of the source. That observation raises an originality risk, but it does not supply the parity classification, the even-factor obstruction, or the general coefficient and origin formulas proved here.

## Limitations

Direct retrieval of the full arXiv PDF for arXiv:2608.09354v1 was unavailable through the accessible route during this review. The primary abstract, its exact first-public timestamp, and a detailed public full-text reading were inspected. Because the inaccessible primary full text is the most plausible place for an equivalent remark, a residual risk remains that some all-factor extension is stated there under different notation; this risk is recorded rather than treated as resolved.

The proof uses quadratic irrational generators. For general irrational generators, reciprocal sine factors can grow faster than polynomially and the point-mass series need not define a tempered distribution by this argument. No claim is made about such families.

## References

1. Anton Tselishchev, *A new example of crystalline-type measure with unit masses and an application to tiling of the real line by translates of a function*, arXiv:2608.09354v1, first public 2026-08-10.
2. Alexander Olevskii and Alexander Ulanovskii, *Fourier Quasicrystals with Unit Masses*, Comptes Rendus Mathématique 358 (2020), 1207--1211, DOI 10.5802/crmath.142.
3. Felipe Gonçalves, *A Classification of Fourier Summation Formulas and Crystalline Measures*, arXiv:2312.11185v3.
