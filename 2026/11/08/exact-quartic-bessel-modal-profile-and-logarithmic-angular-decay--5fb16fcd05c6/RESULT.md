# Exact quartic Bessel modal profile and logarithmic angular decay in dimension three

## Finding
For every integer \(k\geq0\), let \(J_\nu\) be the first-kind Bessel function and \(P_k\) the Legendre polynomial normalized by \(P_k(1)=1\). Define the quartic modal moment
\[
I_k=\int_0^\infty J_{k+1/2}(r)^4\,dr.
\]
Then the **entire** sequence has the exact finite-interval and rational representations
\[
\boxed{I_k=\frac1{2\pi}\int_0^2 P_k(1-u^2/2)^2\,du
=\frac1\pi\sum_{a,b=0}^{k}\frac{(-1)^{a+b}\binom{k}{a}\binom{k+a}{a}\binom{k}{b}\binom{k+b}{b}}{2(a+b)+1}.}
\]
In particular, \(\pi I_k\) is a positive rational number, and
\[
\boxed{\lim_{k\to\infty}\frac{2\pi^2 k}{\log k}\,I_k=1.}
\]
The initial values are \(\pi I_0=1\), \(\pi I_1=7/15\), \(\pi I_2=11/35\), and \(\pi I_3=3607/15015\). The asymptotic is for positive integers \(k\to\infty\); it does not assert an error-term expansion.

## Assumptions and scope
We use the normalization \(j_k(r)=\sqrt{\pi/(2r)}J_{k+1/2}(r)\), with its continuous interpretation at \(r=0\), for the spherical Bessel function. The ordinary Fourier transform of surface measure on \(S^2\subset\mathbb R^3\) uses the phase \(e^{-ix\cdot\omega}\) and **unnormalized** surface measure \(d\sigma\). In the radial-angular mixed fourth-norm extension problem, the degree-\(k\) coefficient is precisely \(I_k\) as defined above (with the standard factor \((2\pi)^{3/2}\) outside the fourth root). No distributional interpretation of the improper integral is necessary: it converges absolutely for every fixed nonnegative integer \(k\).

## Proof
**1. Radial addition and Parseval.** The spherical Bessel addition theorem, with equal radial arguments, states
\[
j_0(r\sqrt{2-2t})=\sum_{m=0}^{\infty}(2m+1)j_m(r)^2P_m(t),\quad -1\le t\le1.
\]
Orthogonality of the Legendre polynomials gives
\[
j_k(r)^2=\frac12\int_{-1}^1j_0(r\sqrt{2-2t})P_k(t)\,dt
=\frac12\int_0^2uP_k(1-u^2/2)j_0(ur)\,du.
\]
Under the three-dimensional radial Fourier--Bessel transform, the spherical Bessel closure relation is
\[
\int_0^\infty r^2j_0(ur)j_0(vr)\,dr=\frac{\pi}{2u^2}\,\delta(u-v),
\]
understood through its Plancherel extension, not by multiplying distributions pointwise. Applying that unitary identity to the compactly supported spectral profile \(P_k(1-u^2/2)/(2u)\), which is square integrable against \(u^2du\), yields
\[
\int_0^\infty r^2j_k(r)^4\,dr=\frac\pi8\int_0^2P_k(1-u^2/2)^2\,du.
\]
Since \(J_{k+1/2}(r)^4=(2r/\pi)^2j_k(r)^4\), multiplication by \(4/\pi^2\) gives the first boxed identity. This also verifies the boundary at \(u=0\): the profile behaves like \(1/(2u)\), which remains in the stated weighted \(L^2\) space.

**2. Exact arithmetic.** The terminating hypergeometric expansion is
\[
P_k(1-u^2/2)=\sum_{a=0}^k(-1)^a\binom{k}{a}\binom{k+a}{a}(u^2/4)^a.
\]
Squaring and integrating each of the finitely many terms over \(0\leq u\leq2\) gives the second boxed formula. Strict positivity follows independently from the square-integral representation.

**3. Logarithmic high-degree asymptotic.** Substitute \(u=2\sin(\theta/2)\). Then
\[
I_k=\frac1{2\pi}\int_0^\pi P_k(\cos\theta)^2\cos(\theta/2)\,d\theta.
\]
Fix \(\varepsilon\in(0,1)\) and write \(K=k+1/2\). On \(k^{-1+\varepsilon}\leq\theta\leq\pi/2\), the classical uniform Darboux estimate (equivalently the large-argument form of Hilb's Legendre asymptotic) gives
\[
P_k(\cos\theta)=\left(\frac2{\pi K\sin\theta}\right)^{1/2}
\big(\cos(K\theta-\pi/4)+O((k\sin\theta)^{-1})\big).
\]
The squared main term, with \(\cos^2=(1+\cos(2K\theta-\pi/2))/2\), has a nonoscillatory contribution
\[
\frac1{2\pi^2K}\int_{k^{-1+\varepsilon}}^{\pi/2}\frac{\cos(\theta/2)}{\sin\theta}\,d\theta
=\frac{(1-\varepsilon)\log k+O(1)}{2\pi^2k}.
\]
Integration by parts bounds the oscillatory contribution by \(O(k^{-1-\varepsilon})\), while the Darboux remainder contributes \(o(k^{-1})\) in this interval. On \(0\leq\theta\leq k^{-1+\varepsilon}\), use \(|P_k(\cos\theta)|\leq1\) for \(\theta\leq1/k\) and the Bernstein bound \(|P_k(\cos\theta)|\leq C(k\sin\theta)^{-1/2}\) thereafter. The resulting integral is between zero and \(O((1+\varepsilon\log k)/k)\). On \([\pi/2,\pi]\), the same Bernstein estimate and the vanishing factor \(\cos(\theta/2)\) give \(O(1/k)\). Thus the \(\liminf\) of \(2\pi^2kI_k/\log k\) is at least \(1-\varepsilon\), and its \(\limsup\) is at most \(1+C'\varepsilon\), with an absolute constant \(C'\). Sending \(\varepsilon\downarrow0\) proves the limiting formula.

## Verification
The bundled `CHECK.py` computes the first four \(\pi I_k\) as exact rational numbers by the finite double sum, independently evaluates the Legendre form using Gaussian quadrature, and compares it to truncated direct Bessel integrations. It also samples the positive high-degree moments for several \(k\), without interpreting those samples as a proof of the asymptotic. Run `python CHECK.py` with Python 3, NumPy, and SciPy. The analytic addition formula, Plancherel normalization, finite binomial expansion, and uniform Legendre estimates above supply the proof for all \(k\).

## Relationship to prior work
Carneiro--Oliveira e Silva--Sousa (arXiv:1710.10365, 2018; journal 2019) introduced these weighted Bessel modal integrals in sharp mixed-norm spherical Fourier restriction and established extremality for even exponents. Xu (arXiv:2610.19648, first submitted 2026-10-14) developed strict all-degree modal ordering and a sharp stability coefficient. Their stated general modal integral representation and comparison theorems are essential background. The specific claim here is the independent exact **all-mode** Legendre-square rational evaluation together with its \(\log k/k\) leading asymptotic, not a new general extremizer classification. In particular, for the three-dimensional quartic problem, these evaluations give computable high-degree modal constants and their sharp rate of decay. The claim of novelty is limited to this evaluated profile, subject to possible equivalent special-function representations in unindexed literature.

## Limitations
The theorem treats dimension three, fourth radial exponent, integer harmonic degree, and unnormalized surface measure only. It does not give second-order asymptotic corrections, establish a new modal ordering theorem, or independently reprove general restriction bounds. The cited 2026 manuscript was available for inspection of its statement/introduction, but not all later sections; identical evaluations outside the inspected material remain a literature risk.

## References
1. Z. Xu, *Sharp radial--angular mixed norm Fourier extension and global stability on spheres*, arXiv:2610.19648v1 (2026-10-14), https://arxiv.org/abs/2610.19648.
2. E. Carneiro, D. Oliveira e Silva, M. Sousa, *Sharp mixed norm spherical restriction*, arXiv:1710.10365v3 (2018), https://arxiv.org/abs/1710.10365.
3. NIST Digital Library of Mathematical Functions, Chapter 18, Section 18.15(iii), Legendre asymptotics, https://dlmf.nist.gov/18.15.iii.
4. G. Szegő, *Orthogonal Polynomials*, fourth edition, Chapter VIII (classical Hilb/Darboux and Bernstein estimates).
