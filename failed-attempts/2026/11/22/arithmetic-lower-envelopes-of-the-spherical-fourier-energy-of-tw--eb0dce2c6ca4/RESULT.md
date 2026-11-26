# Arithmetic lower envelopes of the spherical Fourier energy of two separated balls

## Finding

Fix an integer \(d\ge 2\). Let \(B(c_j,r_j)\subset\mathbb R^d\), \(j=1,2\), be two open balls with \(r_j>0\) and \(|c_1-c_2|>r_1+r_2\). Put \(\Omega=B(c_1,r_1)\cup B(c_2,r_2)\), define \(\widehat f(\xi)=\int_{\mathbb R^d}f(x)e^{-2\pi i x\cdot\xi}\,dx\), and give \(\mathbb S^{d-1}\) probability surface measure \(d\sigma\). Write

\[
E_\Omega(R)=\int_{\mathbb S^{d-1}}|\widehat{\mathbf1_\Omega}(R\omega)|^2\,d\sigma(\omega),\qquad
H_\Omega(R)=\pi^2 R^{d+1}E_\Omega(R).
\]

The following uniform high-frequency asymptotic holds as \(R\to\infty\), with constants depending on the fixed geometry:

\[
H_\Omega(R)=\sum_{j=1}^{2}r_j^{d-1}\cos^2\!\left(2\pi r_jR-\frac{\pi(d+1)}4\right)
+O_\Omega\left(R^{-\min\{1,(d-1)/2\}}\right).\tag{1}
\]

If \(r_1/r_2\notin\mathbb Q\), then
\[
\liminf_{R\to\infty}H_\Omega(R)=0,\qquad
\limsup_{R\to\infty}H_\Omega(R)=r_1^{d-1}+r_2^{d-1}.\tag{2}
\]
Moreover, the high-frequency values converge in the Cesàro-distribution sense to the sum of two independent, weighted arcsine variables: for every bounded continuous \(F\colon\mathbb R\to\mathbb R\),
\[
\lim_{T\to\infty}\frac1T\int_0^T F(H_\Omega(R))\,dR
=\frac1{\pi^2}\int_0^\pi\int_0^\pi F(r_1^{d-1}\cos^2u+r_2^{d-1}\cos^2v)\,du\,dv.\tag{3}
\]

If \(r_1/r_2=p/q\in\mathbb Q\) in lowest positive terms, then
\[
\boxed{\ \liminf_{R\to\infty}H_\Omega(R)=0\quad\Longleftrightarrow\quad4\mid(p-q)(d+3).\ }\tag{4}
\]
When this divisibility fails, there is an \(R_0>0\) and a \(c>0\), depending on the two radii and \(d\), such that \(E_\Omega(R)\ge cR^{-d-1}\) for all \(R\ge R_0\). Likewise,
\[
\limsup_{R\to\infty}H_\Omega(R)=r_1^{d-1}+r_2^{d-1}
\quad\Longleftrightarrow\quad4\mid(p-q)(d+1).\tag{5}
\]

For the particularly natural three-dimensional unequal-radius configuration \(r_1=r\), \(r_2=2r\), with arbitrary separated centers,
\[
\boxed{\ \liminf_{R\to\infty}\frac{\pi^2R^4}{r^2}E_\Omega(R)=\frac{31}{64},\qquad
\limsup_{R\to\infty}\frac{\pi^2R^4}{r^2}E_\Omega(R)=5.\ }\tag{6}
\]
Thus a separated pair of smooth balls can have a positive uniform high-frequency spherical Fourier-energy lower envelope even though each constituent ball by itself has arbitrarily small normalized energy along unbounded frequency sequences.

## Assumptions and scope

The result concerns exactly two disjoint Euclidean balls with fixed radii and centers, ambient dimension \(d\ge2\), the \(2\pi\) Fourier convention above, and normalized surface probability. It makes no claim for overlapping balls, an arbitrary union of three or more balls, general smooth connected domains, or a scale-uniform error when radii vary with frequency. The zero or positive conclusion is about the scaled *spherical mean energy*, not pointwise absence of Fourier zeros in every direction.

## Proof

**Step 1: Exact radial transform.** The Fourier transform of a centered radius-\(r\) ball is real and radial, and for \(R>0\) is
\[
A_r(R)=r^{d/2}R^{-d/2}J_{d/2}(2\pi rR).
\]
The standard fixed-order large-argument Bessel expansion (DLMF 10.17.3) gives, for each fixed positive radius,
\[
\pi R^{(d+1)/2}A_r(R)=r^{(d-1)/2}
\left[\cos\!\left(2\pi rR-\frac{\pi(d+1)}4\right)+O_r(R^{-1})\right].\tag{7}
\]
In particular both sides are uniformly bounded in \(R\) large, and squaring (7) has an \(O_r(R^{-1})\) remainder.

**Step 2: Directional averaging kills separated-center interference.** Translation gives
\[
\widehat{\mathbf1_\Omega}(R\omega)=e^{-2\pi iR\omega\cdot c_1}A_{r_1}(R)+e^{-2\pi iR\omega\cdot c_2}A_{r_2}(R).
\]
Writing \(L=|c_1-c_2|>0\), rotation invariance gives the exact identity
\[
E_\Omega(R)=A_{r_1}(R)^2+A_{r_2}(R)^2+2A_{r_1}(R)A_{r_2}(R)\,\Phi_d(2\pi RL),
\]
where
\[
\Phi_d(z)=\int_{\mathbb S^{d-1}}\cos(z\omega_1)\,d\sigma(\omega)
=\Gamma(d/2)(2/z)^{d/2-1}J_{d/2-1}(z).
\]
By the same Bessel expansion, \(\Phi_d(z)=O_d(z^{-(d-1)/2})\) for fixed dimension and \(z\to\infty\). Combining this with (7) proves (1), including its error exponent and normalization.

**Step 3: Incommensurate radii.** The linear flow
\(R\mapsto (2r_1R,2r_2R)\pmod1\) is dense and uniquely equidistributed in the two-torus when \(r_1/r_2\) is irrational: every nontrivial integer character has nonzero frequency, so its continuous-time average vanishes. The leading term in (1) is a continuous function on the torus, with minimum zero (both cosines zero) and maximum \(r_1^{d-1}+r_2^{d-1}\) (both have absolute value one). Density gives (2), and equidistribution, uniform continuity for \(F\) on the compact range, and the decaying error in (1) give (3). The displayed double integral is precisely the law of two independent squared cosines of uniform phases.

**Step 4: Commensurate radii and all boundaries.** Write \(r_1=ph\), \(r_2=qh\), \(\gcd(p,q)=1\), \(h>0\), and set \(u=2hR\). The leading expression in (1) is a continuous \(1\)-periodic function of \(u\), so its global minimum and maximum are also its limiting lower and upper envelopes as \(R\to\infty\). A zero requires both cosine factors to vanish; equivalently there must be integers \(k,\ell\) with
\[
pu=\frac{d+3}{4}+k,\qquad qu=\frac{d+3}{4}+\ell.
\]
Eliminating \(u\) gives \(qk-p\ell=(p-q)(d+3)/4\). By Bézout's theorem, the left side can be any integer; hence a simultaneous zero exists if and only if \(4\mid(p-q)(d+3)\). If not, the positive continuous leading function has a strictly positive minimum on a compact period, which remains a uniform lower bound up to a vanishing error. This proves (4). Replacing the cosine-zero target by the condition that both cosine squares equal one replaces \(d+3\) with \(d+1\), proving (5). No other boundary cases are omitted, including equal radii \(p=q=1\).

**Step 5: A closed exact positive envelope.** For \(d=3\), \(r_1=r\), \(r_2=2r\), set \(z=\cos^2(2\pi rR)\in[0,1]\). The leading expression in (1), divided by \(r^2\), becomes
\[
z+4(2z-1)^2=16\left(z-\frac{15}{32}\right)^2+\frac{31}{64}.
\]
Its minimum is \(31/64\), attained at \(z=15/32\), and its maximum is \(5\), attained at \(z=1\); all such phases recur at arbitrarily large \(R\). Equation (1) then gives (6).

## Verification

The standalone `CHECK.py` uses only the Python standard library. Running `python CHECK.py` checks the completed-square identity in exact rational arithmetic, the rational-phase divisibility condition on many examples, and direct three-dimensional Fourier-transform sequences approaching the stated sharp endpoints. Finite checks are supplementary and do not establish the universal assertions; the proof above covers all allowed dimensions, radii, and frequencies. The exact three-dimensional transform used in the code is
\[
A_r(R)=\frac{\sin(2\pi rR)-2\pi rR\cos(2\pi rR)}{2\pi^2R^3},
\]
and its angular interference coefficient is \(\sin(2\pi RL)/(2\pi RL)\).

## Relationship to prior work

Brandolini, Hofmann and Iosevich (2003) prove the sharp *upper decay exponent* of spherical Fourier means for convex bodies and sufficiently regular boundaries; their Theorems 1.1--1.2 do not provide the arithmetic high-frequency lower envelope for a disconnected pair of balls. Iosevich, Merlo and Mourgoglou (arXiv:2611.04426, publicly posted November 3, 2026) recently proved the sharp Hölder regularity threshold for the same upper decay exponent, motivating the finer question of whether the normalizing power has a uniformly positive lower envelope. The present result instead classifies the arithmetic obstruction to simultaneous Bessel-phase zeros and computes a sharp nonzero example.

Nearby results on separated frequency-sphere injectivity and Bessel zeros concern different operators and do not imply (4) or (6). The novelty comparison is made at the level of statement and implication, not terminology. The full text of the 2026 motivating paper was unavailable at inspection time; any unlocated equivalent example in that text or older literature remains a priority risk.

## Limitations

This is an exact two-ball high-frequency asymptotic and classification, not a theorem about the optimal Fourier decay exponent for arbitrary domains. No uniform-in-geometry constants or effective global frequency cutoff are asserted. No proof of global priority, and no independent external verification, is claimed. The broad recent paper's abstract, rather than its full text, was available for the closest contemporary comparison.

## References

1. A. Iosevich, A. Merlo, M. Mourgoglou, *Sharp decay of the spherical averages of the Fourier transform of open sets*, arXiv:2611.04426 (first posted 2026-11-03), https://arxiv.org/abs/2611.04426.
2. L. Brandolini, S. Hofmann, A. Iosevich, *Sharp rate of average decay of the Fourier transform of a bounded set*, arXiv:math/0303188 (2003), https://arxiv.org/pdf/math/0303188.
3. NIST Digital Library of Mathematical Functions, §10.17(i), Bessel large-argument expansion, https://dlmf.nist.gov/10.17.
