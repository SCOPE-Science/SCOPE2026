# Apex-weighted Hamming two-shells: an exact Gabor rank discriminant and a universal two-atom spectral law

## Finding
For every integer \(n\ge4\), let \(G=\mathbb F_2^n\), \(N=2^n\), and let \(g_z:G\to\mathbb C\) be the **unnormalized** window
\[
g_z(x)=\begin{cases}z,&x=0,\\1,&\operatorname{wt}(x)=2,\\0,&\text{otherwise},\end{cases}\qquad z\in\mathbb C.
\]
For every translation \(a\in G\) and Walsh modulation \(b\in G\), let \(P_{a,b}\) be the rank-one projector *matrix* \(\lvert M_bT_ag_z\rangle\langle M_bT_ag_z\rvert\) (not rescaled to an idempotent). Define the complex-linear intensity-lifting map \(\mathcal L_z:H\mapsto(\operatorname{tr}(HP_{a,b}))_{a,b\in G}\) on \(M_N(\mathbb C)\), equipped with Hilbert--Schmidt norm. The rank \(R_n(z)\) is its complex-linear rank.

Define the second binary Krawtchouk value
\[
K_{n,2}(w)=\frac{(n-2w)^2-n}{2},\quad 0\le w\le n,
\]
and the exact nonnegative integers
\[
\begin{aligned}
Z_0(n,z)&=\sum_{w=0}^n\binom nw\,\mathbf1_{\{|z|^2+K_{n,2}(w)=0\}},\\
Z_2(n,z)&=2^{n-1}\mathbf1_{\{\operatorname{Im}z=0\}}
+2\sum_{j=0}^{n-2}\binom{n-2}{j}\mathbf1_{\{\operatorname{Re}z=n-2-2j\}}.
\end{aligned}
\]
Then the **exact rank for every complex parameter** is
\[
\boxed{R_n(z)=N-Z_0(n,z)+\binom n2\bigl(N-Z_2(n,z)\bigr)+\binom n4\frac N2.}
\]
In particular, the sharp maximum over all complex \(z\) is
\[
\boxed{R_n^{\max}=N\left(1+\binom n2+\frac12\binom n4\right).}
\]
It is attained **exactly** when \(\operatorname{Im}z\ne0\), \(\operatorname{Re}z\notin\{n-2,n-4,\ldots,-(n-2)\}\), and \(\lvert z\rvert^2\notin\{-K_{n,2}(w):0\le w\le n\}\). The explicit choice \(z=n+i\) attains it for every \(n\ge4\). The complete lower-rank locus is the union of the real axis, finitely many vertical arithmetic lines, and finitely many concentric circles (including a possible radius-zero point); defects **add** at intersections as given by the displayed formula. Purely imaginary parameters can attain the maximum when \(n\) is odd, but never when \(n\) is even.

Moreover, all singular values of \(\mathcal L_z\), including zeros and multiplicities, are given explicitly in the proof. Let \(\mu_{n,z}\) be the empirical probability measure of its *positive* singular values after division by \(\sqrt N\). For **every** sequence \(z=z_n\in\mathbb C\), without a boundedness assumption,
\[
\boxed{\mu_{n,z_n}\ \Longrightarrow\ \tfrac34\delta_2+\tfrac14\delta_6\quad\text{as }n\to\infty.}
\]
Thus the entire finite-parameter rank discriminant coexists with a parameter-independent two-atom bulk spectral law.

## Assumptions and scope
The group is the elementary Boolean group, **not** a cyclic group of the same cardinality. Characters are \(\chi_b(x)=(-1)^{b\cdot x}\). Translation and modulation are \((T_af)(x)=f(x+a)\), \((M_bf)(x)=\chi_b(x)f(x)\). The window is not divided by \(\sqrt{|z|^2+\binom n2}\); for unit-normalized windows all singular values stated here must additionally be divided by \(|z|^2+\binom n2\), while ranks are unchanged. A projective measurement matrix \(P_{a,b}\) is defined as an outer product, regardless of whether it is idempotent. The rank concerns **linear recovery of arbitrary complex matrices** from lifted intensity functionals; it is neither a claim of pure-state phase retrieval nor a stability estimate. The sampling family consists of all \(N^2\) time-frequency shifts, with no missing shifts.

## Proof
**1. Weyl diagonalization and normalization.** The Weyl matrices \(W_{u,v}=M_vT_u\), indexed by \(u,v\in G\), are an orthogonal Hilbert--Schmidt basis with \(\|W_{u,v}\|_{HS}^2=N\). Conjugation by any \(M_bT_a\) multiplies \(W_{u,v}\) by a sign character in \((a,b)\). Therefore the \(N^2\) measurements of any fixed Weyl matrix all have the same modulus, namely
\[
|A_z(u,v)|,\qquad A_z(u,v)=\sum_{x\in G}\overline{g_z(x)}g_z(x+u)\chi_v(x).
\]
Orthogonality of sign characters makes \(\mathcal L_z^*\mathcal L_z\) diagonal in the Weyl basis, with eigenvalue \(N|A_z(u,v)|^2\). Hence **every** singular value of \(\mathcal L_z\) is \(\sqrt N|A_z(u,v)|\), counted once per \((u,v)\). This identity also explicitly identifies the kernel as the span of Weyl matrices with \(A_z(u,v)=0\).

**2. Enumerating all autocorrelation shifts.** The support of \(g_z\) lies in Hamming weights zero and two. A difference between two support points has weight only zero, two, or four. For a zero shift, the Walsh character sum over weight-two vectors is the elementary degree-two Krawtchouk expression:
\[
A_z(0,v)=|z|^2+\sum_{i<j}(-1)^{v_i+v_j}=|z|^2+K_{n,2}(\operatorname{wt}v).
\]
For a shift \(u=e_i+e_j\), the support intersection consists of \(0\), \(u\), and the two points \(e_i+e_k,e_j+e_k\) for every \(k\notin\{i,j\}\). Thus
\[
A_z(u,v)=\overline z+z(-1)^{v_i+v_j}+
\bigl((-1)^{v_i}+(-1)^{v_j}\bigr)
\sum_{k\notin\{i,j\}}(-1)^{v_k}.
\]
If the two Walsh signs are unequal, this is \(-2i\operatorname{Im}z\). If they are equal to \(\epsilon\in\{-1,1\}\) and precisely \(j\) of the other \(n-2\) Walsh bits are one, it is \(2(\operatorname{Re}z+\epsilon(n-2-2j))\). These cases have, for **each** weight-two shift, multiplicities \(N/2\) and \(\binom{n-2}{j}\) for each sign \(\epsilon\), respectively.

For a shift of weight four, its six overlapping support points are exactly the weight-two subsets of its four active coordinates. If \(r\) of those coordinates have Walsh bit one, the correlation equals
\[
A_z(u,v)=K_{4,2}(r)=\begin{cases}6,&r=0,4,\\0,&r=1,3,\\-2,&r=2.\end{cases}
\]
For every such shift the correlation magnitudes \(6\), \(2\), and \(0\) have respective multiplicities \(N/8\), \(3N/8\), and \(N/2\), independently of \(z\). Every shift of any other Hamming weight has identically zero ambiguity coefficients.

**3. Exact finite singular spectrum and rank.** The preceding cases specify the complete multiset of ambiguity *magnitudes* as follows (values from different rows must be combined if they coincide):

- for zero shift: \(\lvert |z|^2+K_{n,2}(w)\rvert\), multiplicity \(\binom nw\), for every \(w=0,\ldots,n\);
- for the \(\binom n2\) shifts of weight two: \(2|\operatorname{Im}z|\), multiplicity \(\binom n2 N/2\), and \(2|\operatorname{Re}z+\epsilon(n-2-2j)|\), multiplicity \(\binom n2\binom{n-2}{j}\) for each \(\epsilon\in\{-1,1\}\), \(0\le j\le n-2\);
- for the \(\binom n4\) shifts of weight four: \(6\) with multiplicity \(\binom n4 N/8\), \(2\) with multiplicity \(\binom n4 3N/8\), and \(0\) with multiplicity \(\binom n4 N/2\);
- for the remaining \(N-1-\binom n2-\binom n4\) shifts: \(0\), each with multiplicity \(N\).

Multiply each listed magnitude by \(\sqrt N\) to obtain the singular spectrum. All multiplicities sum to \(N^2\). The zero-shift zeros are counted by \(Z_0(n,z)\). The unequal-sign weight-two cases contribute \(N/2\) zeros exactly when \(\operatorname{Im}z=0\). In the equal-sign cases, replace \(j\) by \(n-2-j\) in one of the two sign sums to get exactly the second term of \(Z_2(n,z)\). Weight-four shifts always contribute precisely \(N/2\) positive directions each, independently of \(z\). Adding all positive counts proves the boxed rank formula without cancellation or unjustified independence assumptions.

**4. The entire discriminant and sharp optimization.** All subtracted terms \(Z_0,Z_2\) are nonnegative. They vanish simultaneously exactly under the three stated parameter restrictions; hence those restrictions are necessary and sufficient for attaining the maximum. The explicit seed \(z=n+i\) lies off the real axis and outside all vertical lines because \(n>n-2\); also \(|z|^2=n^2+1>n/2\ge-K_{n,2}(w)\) for every \(w\). For odd \(n\), every element of \(\{n-2,n-4,\ldots,-(n-2)\}\) is odd, so \(\operatorname{Re}z=0\) avoids those lines. For even \(n\), zero belongs to the set and pure-imaginary windows lose exactly \(2\binom{n-2}{(n-2)/2}\) weight-two frequencies per shift, even when the radius avoids every circle. The zero sets for shifts of differing Hamming weights are disjoint, proving the additive multiplicities at every intersection.

**5. The universal positive-spectrum limit.** There are exactly \(\binom n4N/2\) positive Weyl modes at shift-weight four; among them the magnitudes \(2\) and \(6\) occur with relative frequencies \(3/4\) and \(1/4\). All other shifts together contribute at most \((1+\binom n2)N\) positive modes, independently of \(z\). This is an \(O(n^{-2})\) fraction of the weight-four positive modes as \(n\to\infty\). Consequently, for any bounded continuous test function, its positive-spectrum empirical average differs from \(3f(2)/4+f(6)/4\) by \(O(\|f\|_\infty n^{-2})\), uniformly over arbitrary parameter sequences \(z_n\). This establishes the asserted weak limit without assuming bounded amplitudes or tightness of the non-bulk modes.

## Verification
The standalone Python 3 checker `verify.py` performs **separately implemented exact Gaussian-integer autocorrelation** of the actual windows at seven rational parameters in every dimension \(4\le n\le7\), comparing all \(N^2\) squared ambiguity magnitudes and each rank against the full formulas; it uses no floating-point arithmetic for these tests. It also directly builds the \(256\times256\) Hilbert--Schmidt projector Gram matrix at \(n=4\) and checks its complete eigenvalue spectrum numerically at three substantially different parameters, verifying the predicted factor \(N\) in the squared singular values. Successful execution prints `APEX_WEIGHT_TWO_HAMMING_GABOR_EXACT_CHECKS_PASS`. The finite tests corroborate, but do not replace, the preceding proof for every dimension and complex parameter.

## Relationship to prior work
Bojarovska and Flinth (2015) establish finite Gabor phase-retrieval criteria and linear lifting bounds. Goldberger, Kang, and Okoudjou (2021) establish the general fact that the eigenvalues of a finite cyclic Gabor-projector Gramian are group-size times squared ambiguity magnitudes. Those are acknowledged as the spectral mechanism: **the general criterion by itself contains neither the Boolean two-shell correlation classification nor the full complex apex-parameter discriminant and uniform two-atom law**. The present theorem derives these properties explicitly for a family on the elementary Boolean group, with additive rank losses along real lines, integer-spaced vertical lines, and circles.

Published studies of Walsh concentration on Hamming shells concern restricting specified Walsh frequency bands to a shell, rather than the full nonlinear orbit of rank-one Gabor projectors and its Weyl-basis linearization. A previously published exact rank discriminant for a one-coordinate perturbation of a *cyclic, almost constant* Gabor window has a different support and ambient group; its divisor-controlled phases do not imply the Boolean Hamming-shell formulas. A published positive-definite Turán classification for support \(\{0\}\cup\{x:\operatorname{wt}(x)=2\}\) uses the same support geometry but a different positivity optimization; it does not count cross-correlations of the apex-perturbed window or characterize the full Gabor operator span. Classical Krawtchouk identities used in the proof are not claimed as new.

## Limitations
The result is restricted to the Boolean Hamming weight-two shell plus a single arbitrary complex apex coefficient. It does **not** solve pure-state phase retrieval: all window translates live entirely within one parity class, so changing the relative phase of two parity components of a general signal preserves every measurement. The rank is consequently always strictly smaller than \(N^2\). The singular spectrum is for unnormalized projectors and the stated complex Hilbert--Schmidt map; other normalizations rescale the singular values. No quantitative lower positive singular-value bound, algorithm for noisy recovery, or result for shell radii greater than two is asserted. A general prior theorem on Weyl ambiguity supplies the diagonalization framework, and the elementary Krawtchouk identity supplies one axis; an implicit prior specialization of those methods remains an originality risk. The work has undergone no independent mathematical audit.

## References
1. I. Bojarovska and A. Flinth, *Phase Retrieval from Gabor Measurements*, arXiv:1503.05800v1, first public 2015-03-19; especially Section 2 and Theorem 2.3. https://arxiv.org/abs/1503.05800
2. A. Goldberger, S. Kang and K. A. Okoudjou, *Towards a classification of incomplete Gabor POVMs in* \(\mathbb C^d\), arXiv:2106.01509v1, first public 2021-06-02; especially Theorems 1--2. https://arxiv.org/abs/2106.01509
