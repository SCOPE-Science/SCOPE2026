# Exactly three Zak zeros for every unchirped dilate of the first Hermite function

## Finding
For each \(\beta>0\), define the Zak transform
\[
Z_\beta(x,\omega)=\sum_{k\in\mathbb Z}(x+k)e^{-\beta(x+k)^2}e^{-2\pi i k\omega}.
\]
Its zeros in \([0,1)^2\) are **exactly**
\[
\{(0,0),(0,\tfrac12),(\tfrac12,0)\}.
\]
Thus no additional Zak zeros appear under any positive **unchirped dilation** of the first Hermite function. This proves the zero-chirp, arbitrary-dilation subcase of the generalized first-Hermite Zak-zero conjecture stated in the 2025 paper cited below, not the case of nonzero chirp.

## Assumptions and scope
The parameter \(\beta\) is any positive real number, and the Zak convention is the indicated sum with the negative Fourier phase. Absolute, locally uniform convergence (including derivatives in both variables) follows from Gaussian tails. A first Hermite function dilated by any positive factor is a nonzero scalar multiple of \(t\exp(-\beta t^2)\) for an appropriate \(\beta>0\); nonzero constants do not affect zeros. Zeros are counted as distinct points, not with multiplicity. Zak quasi-periodicity makes \([0,1)^2\) a fundamental domain.

## Proof
**1. Positivity of the periodic Gaussian slope.** Put \(H_\beta(x)=\sum_{k\in\mathbb Z}\exp(-\beta(x+k)^2)\). For every \(\beta>0\), the Jacobi triple product and Poisson summation give
\[
H_\beta(x)=\sqrt{\pi/\beta}\prod_{j\ge1}(1-q^{2j})\bigl(1+2q^{2j-1}\cos(2\pi x)+q^{4j-2}\bigr),\quad q=e^{-\pi^2/\beta}.
\]
Each factor is strictly positive and the product is locally uniformly differentiable, so
\[
\frac{H'_\beta(x)}{H_\beta(x)}=-4\pi\sin(2\pi x)\sum_{j\ge1}\frac{q^{2j-1}}{1+2q^{2j-1}\cos(2\pi x)+q^{4j-2}}<0\quad(0<x<\tfrac12).
\]
Consequently \(Z_\beta(x,0)=-H'_\beta(x)/(2\beta)>0\) in that strip. The endpoint values \(Z_\beta(0,0)=Z_\beta(1/2,0)=0\) follow by pairing opposite lattice sites.

**2. Excluding all remaining zeros for \(\beta\ge2\).** Write \(\theta=2\pi\omega\). For \(0<x\le1/2\), and every integer \(n\ge1\), put
\[
A_n(x)=(n-x)e^{-\beta(n-x)^2}-(n+x)e^{-\beta(n+x)^2}>0.
\]
Indeed \(u e^{-\beta u^2}\) is strictly decreasing for \(u\ge1/2\) when \(\beta\ge2\), and \(n-x\ge1/2\). Pairing the terms indexed by \(n\) and \(-n\) yields
\[
\operatorname{Re}Z_\beta(x,\omega)=xe^{-\beta x^2}-\sum_{n\ge1}A_n(x)\cos(n\theta)
\ge xe^{-\beta x^2}-\sum_{n\ge1}A_n(x)=Z_\beta(x,0).
\]
For \(0<x<1/2\) the right side is strictly positive, proving zero-freeness for all \(\omega\). At \(x=1/2\), the right side vanishes, but
\[
\operatorname{Re}Z_\beta(1/2,\omega)=\sum_{n\ge1}A_n(1/2)(1-\cos(n\theta))>0\quad(0<\omega<1),
\]
since \(A_1(1/2)>0\). Hence the sole zero on this vertical line is \((1/2,0)\).

At \(x=0\), the transform is purely imaginary:
\[
Z_\beta(0,\omega)=-2i\sum_{n\ge1}ne^{-\beta n^2}\sin(n\theta).
\]
For \(0<\omega<1/2\), the inequality \(|\sin(n\theta)|\le n\sin\theta\), combined with
\[
\sum_{n\ge2}n^2e^{-\beta(n^2-1)}\le \sum_{m\ge1}(m+1)^2e^{-6m}
<\sum_{m\ge1}\frac{(m+1)^2}{400^m}
=\frac{r(4-3r+r^2)}{(1-r)^3}\bigg|_{r=1/400}<1,
\]
shows that the \(n=1\) term strictly dominates all others. Thus there is no zero on \(x=0\) with \(0<\omega<1/2\); conjugate symmetry excludes \(1/2<\omega<1\). The two endpoints \((0,0)\) and \((0,1/2)\) are zeros by sine cancellation.

For \(1/2<x<1\), the exact reflection identity
\[
Z_\beta(1-x,\omega)=-e^{2\pi i\omega}Z_\beta(x,-\omega)
\]
excludes zeros using the first open strip. This completes the proof for \(\beta\ge2\).

**3. Reduction of all smaller scales by Fourier duality.** Under \(\widehat f(\xi)=\int f(t)e^{-2\pi i t\xi}\,dt\),
\[
\widehat{t e^{-\beta t^2}}(\xi)=-i(\pi/\beta)^{3/2}\xi e^{-\pi^2\xi^2/\beta}.
\]
Poisson summation for Zak transforms therefore gives the exact identity
\[
Z_\beta(x,\omega)=-i(\pi/\beta)^{3/2}e^{2\pi i x\omega}
Z_{\pi^2/\beta}(\omega,-x).
\]
The prefactor never vanishes; for \(\beta<2\) the dual parameter \(\pi^2/\beta>\pi^2/2>2\). The induced map \((x,\omega)\mapsto(\omega,-x)\) permutes the three claimed zeros modulo the Zak fundamental lattice. The already proved large-parameter case therefore settles every \(0<\beta<2\). **QED.**

## Verification
The inequalities used in step 2 hold uniformly over the entire relevant infinite ranges, not just a numerical mesh. The Jacobi product has strictly positive factors and locally uniform differentiation at each fixed positive \(\beta\). The Fourier-duality constant and signs have been checked directly from the Gaussian Fourier transform; a standalone deterministic supplementary script verifies sampled instances of the identities and strict-sign estimates over several scales. Those finite calculations are diagnostic only, not the proof of the universal assertion.

## Relationship to prior work
Faulhuber's 2025 article, initially public as arXiv:2502.09510 on 2025-02-13, records the three parity zeros, poses the broader number-of-Zak-zeros question, and explicitly conjectures exactly three zeros for **all** generalized first-Hermite windows with both arbitrary dilation and arbitrary chirp (Conjecture 4.1). The present theorem proves that conjecture for arbitrary dilation with **chirp fixed at zero**. In the inspected article the arbitrary-dilation zero-exclusion argument is not supplied. Existing Gabor-frame classifications of Gaussian/first-Hermite mixtures concern simultaneous Zak-channel zeros and do not imply the complete zero set of the pure dilated first Hermite window. Classical Poisson summation and Jacobi theta factorization are used as tools; no novelty is claimed for either identity.

## Limitations
No nonzero quadratic chirp parameter is included. This result does not settle the full generalized first-Hermite conjecture, does not classify higher Hermite Zak zeros, and does not claim a general irregular Gabor-frame characterization. The bibliographic search cannot exclude an unindexed older derivation of the same zero-chirp zero-set assertion. Independent external validation has not occurred.

## References
1. M. Faulhuber, *Gabor systems with Hermite functions of order N and oversampling greater than N+1 which are not frames*, arXiv:2502.09510 (first posted 2025-02-13), published in *Sampling Theory, Signal Processing, and Data Analysis* 23 (2025), article 22, doi:10.1007/s43670-025-00112-5. Particularly Sections 2.3, 3 and 4, Conjecture 4.1.
2. The classical Jacobi triple-product identity for the third theta function and Poisson summation formula, in the normalization displayed in the proof.
