# Multiring polygonal Fock intensities: a sharp all-order peak bound

## Finding
For integers \(k\ge1\), \(n\ge3\), and distinct real numbers \(0<a_1<\cdots<a_k\), let
\[
P(z)=\prod_{j=1}^k(z^n-a_j),\qquad H(z)=e^{-|z|^2}|P(z)|^2.
\]
The number of distinct local maxima of \(H\) on \(\mathbb C\) is at most \(kn+1\). The origin is always a nondegenerate local maximum, and every other local maximum lies on one of the \(n\) rays \(z^n<0\). In fact, every nonzero stationary point belongs to a ray \(z^n\in\mathbb R\), and the \(kn\) zeros of \(P\) are nondegenerate minima.

The bound is **attained with every maximum nondegenerate** whenever
\[
 n\ge \left\lceil 8k\log(8k)\right\rceil.
\]
One explicit open family of sharp examples is obtained around the parameters
\[
 a_j=\bigl(n(j-\tfrac12)\bigr)^{n/2},\qquad j=1,\dots,k.
\]
At the displayed parameters, precisely \(k\) strict off-origin radial maxima occur along each negative-power ray, giving \(kn+1\) nondegenerate two-dimensional maxima in all. The strict configuration persists for sufficiently small independent perturbations of the positive parameters. No optimality of the sufficient degree threshold is asserted.

## Assumptions and scope
Complex derivatives and Hessians are taken in \(\mathbb R^2\cong\mathbb C\). A local maximum includes a degenerate isolated local maximum when the parameters are arbitrary. For the sharpness family all local maxima are nondegenerate. Natural logarithms are used, and the Gaussian factor has exponent \(-|z|^2\), without an omitted rescaling.

The analytic polynomial has \(kn\) simple zeros because the \(a_j\) are strictly positive and distinct; the polynomial is not normalized in the Bargmann–Fock norm, but multiplying it by a nonzero scalar does not affect the critical-point geometry. In quantum-optical language this is the unnormalized shape of a finite-stellar-rank Husimi intensity.

## Proof
**Angular rigidity.** Write \(z=re^{i\theta}\) and \(w=z^n=r^ne^{in\theta}\). For nonzero \(P(z)\), direct differentiation gives
\[
 \partial_\theta\log H(r e^{i\theta})
 =2n\operatorname{Im}(w)\sum_{j=1}^k
 \frac{a_j}{|w-a_j|^2}.
\]
Its sign is that of \(\sin(n\theta)\); thus all nonzero nonzero-intensity stationary points have \(z^n\in\mathbb R\). Each fixed-radius angular profile attains its strict maximum precisely when \(z^n<0\), its minimum when \(z^n>0\) except at zeros of \(P\). In particular no noncentral maximum can lie on a positive-power ray. At a negative-power ray, \(\partial_{\theta\theta}\log H=2n^2w\sum_j a_j/(w-a_j)^2<0\), so angular curvature is strictly negative. Each simple zero of \(P\) is a nondegenerate minimum of \(H\).

**Radial Descartes bound.** On any negative-power ray, the logarithm of the positive radial intensity satisfies
\[
 \frac{d}{dr}\log H=-2r+2nr^{n-1}\sum_{j=1}^k\frac1{r^n+a_j}.
\]
Let \(Q(t)=\prod_{j=1}^k(t+a_j)=\sum_{j=0}^kq_jt^j\), where every \(q_j>0\). The positive radial stationary radii are precisely the positive roots of
\[
 R(r)=Q(r^n)-nr^{n-2}Q'(r^n)
 =\sum_{j=0}^kq_jr^{nj}-n\sum_{j=1}^k j q_jr^{nj-2}.
\]
Since \(n\ge3\), the nonzero terms have strictly interlaced powers \(0,n-2,n,2n-2,2n,\ldots,kn-2,kn\) with alternating signs \(+,-,+,-,\ldots,-,+\), hence exactly \(2k\) sign changes. Descartes' rule gives at most \(2k\) positive roots counted with multiplicity. The radial derivative is negative near zero (since \(n\ge3\)) and negative for large \(r\). Each radial local maximum therefore requires an entering positive-derivative interval and an exiting negative-derivative interval, consuming at least two positive roots counted with multiplicity. Consequently each negative-power ray has at most \(k\) off-origin maxima. There are \(n\) such rays. The origin satisfies \(H(z)=H(0)(1-|z|^2+O(|z|^3))\) and is a nondegenerate local maximum. The bound \(kn+1\) follows.

**Uniform sharpness construction.** Put \(m=n/2\), \(c_j=j-\tfrac12\), and \(a_j=(nc_j)^m\). With \(x=r^2/n>0\), the radial derivative has the sign of
\[
 S(x)-x,\qquad S(x)=\sum_{j=1}^k\frac1{1+(c_j/x)^m}.
\]
Take sample locations
\[
 x_j^-=j-\tfrac34,\quad x_j^+=j-\tfrac14\ (1\le j\le k),\qquad x_{k+1}^-=k+\tfrac14.
\]
For any of these samples \(x\), every ratio \(c_i/x<1\) or \(x/c_i<1\) on the appropriate side of the step satisfies
\[
 \min(c_i/x,x/c_i)\le1-\frac1{4k}.
\]
Indeed the nearest offsets from the half-integer \(c_i\) are at least \(1/4\), and direct inspection of the nearest neighboring half-integers gives the displayed uniform estimate; more distant terms have smaller ratios. As a result, each summand of \(S(x)\) differs from its step limit \(\mathbf1_{\{c_i<x\}}\) by no more than \(e^{-n/(8k)}\). Therefore
\[
 \left|S(x)-\#\{i:c_i<x\}\right|\le k e^{-n/(8k)}\le\tfrac18
\]
under the claimed degree condition. At \(x_j^-\) the step count is \(j-1\), at \(x_j^+\) it is \(j\), and at \(x_{k+1}^-\) it is \(k\). Thus
\[
 S(x_j^-)-x_j^-\le-\tfrac18,\quad
 S(x_j^+)-x_j^+\ge\tfrac18,\quad
 S(x_{k+1}^-)-x_{k+1}^-\le-\tfrac18.
\]
In the disjoint consecutive intervals \((x_j^-,x_j^+)\) and \((x_j^+,x_{j+1}^-)\), \(1\le j\le k\), the radial derivative changes sign, giving at least \(2k\) positive roots. Descartes gives at most \(2k\) counted with multiplicity: hence all are simple, and precisely \(k\) are maxima. The angular curvature is strictly negative and the radial curvature is strictly negative at those maxima, so they are nondegenerate in two dimensions. The origin provides the additional nondegenerate maximum. Simplicity and continuity give persistence for all sufficiently small perturbations of \((a_1,\ldots,a_k)\).

## Verification
The accompanying standalone `check_multiring.py` implements the sample-value inequalities with exact rational arithmetic for \(k=1,\dots,6\) and the first tested multiples of four above the stated degree threshold. It additionally checks the coefficient-sign alternation of \(R\). The replay finishes with `MULTIRING_POLYGON_PEAK_CHECK_PASS`. The infinite-parameter theorem is established by the preceding inequalities and Descartes' rule, **not** by the six finite tests. The zero classification follows from simplicity of the polynomial roots.

## Relationship to prior work
Abreu's 2022 work develops the general Chern-critical-point framework for Gaussian-weighted entire functions and establishes statistical densities for random Gaussian spectrogram maxima. Chabaud, Markham and Grosshans (2019) establish the stellar/Husimi correspondence and the relevance of finite polynomial zero sets. Their inspected statements do not contain a deterministic all-order maximum-count theorem or its explicit uniform saturating family.

Separate elementary instances with one and two concentric polygonal zero rings already provide the sharp \(n+1\) and \(2n+1\) bounds. The present assertion is stronger in quantifiers and mechanism: \(k\) is unrestricted, with a constructive \(O(k\log k)\) degree condition guaranteeing \(k\) simultaneous, nondegenerate peak rings. The one- and two-ring statements alone do not imply such uniform arbitrary-\(k\) realization.

## Limitations
The bound is specific to equal angular order \(n\), positive real distinct \(a_j\), and the stated isotropic Gaussian weight. It is not claimed for arbitrary zero configurations, complex parameter phases, or general entire functions. The sufficient threshold \(\lceil8k\log(8k)\rceil\) is probably not optimal; the exact smallest saturating degree for a given \(k\) is not determined. The proof gives an upper bound on the number of maxima, not a complete classification of all saddles or their bifurcation surfaces.

## References
- U. Chabaud, D. Markham, F. Grosshans, *Stellar representation of non-Gaussian quantum states* (first publicly available 2019-07-25), arXiv:1907.11009. The full author HTML, including its supplementary text, was inspected for the Husimi/core-state setup.
- L. D. Abreu, *Local Maxima of White Noise Spectrograms and Gaussian Entire Functions* (arXiv first publicly available 2022-10-13), arXiv:2210.06721; *J. Fourier Anal. Appl.* **28** (2022), article 88. Full open-access HTML was inspected, especially Section 2.2, Theorem 1, Proposition 1 and its proof.
