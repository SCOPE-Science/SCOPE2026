# A sharp asymmetric two-arc observability law for five consecutive Fourier modes

## Finding
On the circle \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\), let
\[
\mathcal V_4=\operatorname{span}_{\mathbb C}\{1,e^{it},e^{2it},e^{3it},e^{4it}\},\qquad
\|f\|_{\mathbb T}^2=\frac1{2\pi}\int_{\mathbb T}|f(t)|^2\,dt.
\]
For \(0<a<\pi/2\), let \(\mathcal E_a\) be the family of unions of two circular arcs of half-widths \(h_1,h_2>0\), disjoint in their interiors, with \(h_1+h_2=2a\). Set
\[
\Lambda(E)=\min_{\substack{f\in\mathcal V_4\\\|f\|_{\mathbb T}=1}}\frac1{2\pi}\int_E|f(t)|^2\,dt,
\qquad \mathcal M(a)=\sup_{E\in\mathcal E_a}\Lambda(E).
\]
Then
\[
\boxed{\lim_{a\downarrow0}\frac{\mathcal M(a)}{a^5}=\frac{1024}{135\pi}.}
\]
This is a sharp **two-arc** optimization, not an optimization over arbitrary measurable observation sets. A concrete asymptotically optimal configuration has antipodal centers and half-widths
\[
h_1=2a-a^{3/2},\qquad h_2=a^{3/2}.
\]
Conversely, any family of two-arc configurations satisfying \(\Lambda(E_a)/\mathcal M(a)\to1\) as \(a\downarrow0\) must have its shorter half-width negligible relative to \(a\), and the shorter circular distance between the two centers must tend to \(\pi\). There is no assertion of uniqueness of the finite-\(a\) maximizer or of a unique power-law decay for the shorter arc.

For comparison, two **equal** antipodal arcs of half-width \(a\) each have
\[
\Lambda(E_{\rm equal})=\frac{64}{135\pi}a^5+o(a^5).
\]
Allowing unequal widths therefore increases the sharp small-aperture worst-observation coefficient by a factor of \(16\), without changing the fifth-power exponent.

## Assumptions and scope
All Fourier modes are unweighted, consecutive integer characters, and orthonormal with respect to normalized Haar measure. An arc's half-width is half its angular length, not its Haar mass. The total observed angular length is \(4a\). Two arc centers have shorter circular separation \(\delta\in[2a,\pi]\); one may translate the first center to angle \(0\), the other to \(\delta\). The five-by-five Hermitian Gram matrix has entries
\[
G_{jk}(E)=\frac1{2\pi}\int_E e^{i(j-k)t}\,dt,\qquad 0\le j,k\le4,
\]
and \(\Lambda(E)=\lambda_{\min}(G(E))\). Arcs may touch at endpoints; that does not affect the integral. The limit concerns fixed five-mode bandwidth as \(a\downarrow0\). The constant does not describe modes or numbers of arcs varying with \(a\).

## Proof
**1. A universal trial direction.** Fix centers \(z_1=1\) and \(z_2=e^{i\delta}\) with \(0<\delta\le\pi\). Associate a Fourier polynomial \(f(t)=P(e^{it})\) with its coefficient vector. Define
\[
Q_\delta(z)=(z-z_1)^2(z-z_2)^2.
\]
It vanishes twice at each center. Parseval makes its squared coefficient norm
\[
S(\cos\delta)=\sum_{j=0}^4|[z^j]Q_\delta|^2
=34+32\cos\delta+4\cos^2\delta\ge6.
\]
At either center, the squared modulus of its quadratic Taylor coefficient with respect to the angular coordinate, after normalizing by \(\sqrt S\), is
\[
R(\delta)=\frac{|z_1-z_2|^4}{S(\cos\delta)}
=\frac{4(1-\cos\delta)^2}{34+32\cos\delta+4\cos^2\delta}.
\]
(The angular quadratic coefficient is the coefficient of \(u^2\) in \(Q_\delta(z_i e^{iu})\).)

**2. Local optimal quadratic residual, uniformly away from colliding centers.** For a prescribed complex quadratic coefficient \(C\), the minimum of
\(\int_{-h}^h|A+Bu+Cu^2|^2\,du\), over \(A,B\in\mathbb C\), equals
\[
|C|^2\int_{-h}^h\left(u^2-\frac{h^2}{3}\right)^2du
=\frac8{45}|C|^2h^5.
\]
The unique minimizing lower-order coefficients are \(B=0\), \(A=-Ch^2/3\). For two distinct centers, Hermite interpolation of the value and first angular derivative at both centers has rank four on the degree-at-most-three polynomials. Thus the normalized \(Q_\delta\) can be corrected by a degree-at-most-three polynomial of coefficient norm \(O_\varepsilon(a^2)\) to obtain **both** local monic quadratic residuals, when \(\delta\in[\varepsilon,\pi]\). Taylor expansion on each arc, uniformly for \(h_1+h_2=2a\), then gives a unit-norm trial polynomial satisfying
\[
\Lambda(E)\le
\frac4{45\pi}R(\delta)(h_1^5+h_2^5)+O_\varepsilon(a^6).
\tag{1}
\]
This is a trial-vector upper bound; it does not assume that the eigenvector already has a limiting form.

**3. Colliding centers cannot improve the fifth-power coefficient.** If \(\delta\to0\), the normalized uncorrected \(Q_\delta\) suffices. For \(t\) on the first arc with angular displacement \(|u|\le h_1\),
\(|Q_\delta(e^{iu})|\le |u|^2(|u|+\delta)^2\). The analogous estimate holds on the second arc. Since \(S\ge6\) and both half-widths are at most \(2a\),
\[
\Lambda(E)\le C a^5(a+\delta)^4=o(a^5)
\quad\text{whenever }a\downarrow0,\ \delta\to0.
\tag{2}
\]
Therefore every sequence of configurations has, after taking a subsequence of center separations, either the compact-uniform estimate (1), or the negligible bound (2).

**4. Global upper bound and necessary geometry.** On \([-1,1]\),
\[
\frac{d}{dc}\frac{4(1-c)^2}{34+32c+4c^2}
=\frac{80(c-1)(2c+5)}{(34+32c+4c^2)^2}<0
\quad(-1\le c<1).
\]
Hence \(R(\delta)\le R(\pi)=8/3\), with equality only at antipodal centers. Moreover, \(h_1^5+h_2^5\le(h_1+h_2)^5=(2a)^5\), with equality in the normalized limiting inequality only when \(\min(h_1,h_2)/a\to0\). Equations (1) and (2) imply
\[
\limsup_{a\downarrow0}\frac{\mathcal M(a)}{a^5}
\le\frac4{45\pi}\cdot\frac83\cdot 32
=\frac{1024}{135\pi}.
\]
These two strict inequalities also prove the asserted necessary center separation and asymmetry for any asymptotically optimal family, once the matching lower bound is established.

**5. Construction and matching lower bound.** Set \(h_1=2a-a^{3/2}\), \(h_2=a^{3/2}\), with centers at \(0\) and \(\pi\). Here \(Q_\pi(z)=(z^2-1)^2\) has squared coefficient norm \(6\) and its angular quadratic coefficient at either center has magnitude \(4\). The interpolation in Step 2, taking the large-arc value correction \(-Ch_1^2/3\) and zero value and first derivative at the narrow arc, gives a normalized trial polynomial with energy at most
\[
\frac1{2\pi}\cdot\frac{16}{6}\cdot\frac8{45}h_1^5+o(a^5)
=\frac{1024}{135\pi}a^5+o(a^5).
\]
This bounds the least Gram eigenvalue from above. To obtain the necessary *lower* bound, take unit coefficient-norm minimizers \(f_a\); they have observed energy \(O(a^5)\). Finite-dimensional polynomial norm equivalence on a shrinking interval and uniformly bounded higher derivatives imply
\[
f_a(0)\to0,\ f_a'(0)\to0,\qquad
f_a(\pi)\to0,\ f_a'(\pi)\to0.
\]
For completeness, rescaling the large arc and using the energy bound gives \(f_a(0)=O(a^2)\), \(f_a'(0)=O(a)\), up to Taylor remainders of higher orders. Rescaling the narrow arc of half-width \(a^{3/2}\) gives \(f_a(\pi)=O(a^{7/4})\), \(f_a'(\pi)=O(a^{1/4})\), again with smaller remainder terms. Any converging subsequence of coefficient vectors therefore lies in the one-dimensional kernel of these four value/derivative functionals: it is \(e^{i\phi}Q_\pi/\sqrt6\). In particular, the angular quadratic coefficient of \(f_a\) at the large arc converges in squared modulus to \(16/6\).

Let \(C_a=f_a''(0)/2\) (angular derivatives). Orthogonal projection of \(f_a\) on the real quadratic \(u^2-h_1^2/3\) over the large arc gives, using a uniform bounded-derivative Taylor remainder,
\[
\int_{-h_1}^{h_1}|f_a(u)|^2du
\ge \frac8{45}h_1^5|C_a|^2+o(a^5).
\]
Since \(|C_a|^2\to16/6\) and \(h_1/a\to2\), the observed large-arc energy alone is at least \(1024a^5/(135\pi)+o(a^5)\), after Haar normalization. The narrow arc contributes nonnegative energy. This matches the trial upper bound, establishes the sharp limit and completes the rigidity argument.

**6. Equal-width benchmark.** At antipodal centers with \(h_1=h_2=a\), the same two-center Hermite argument applies with equal local quadratic residuals. The one-dimensional double-zero limit gives
\[
\Lambda(E_{\rm equal})\sim \frac4{45\pi}\frac83\cdot2a^5
=\frac{64}{135\pi}a^5.
\]
The factor-sixteen gain follows by division.

## Verification
The standalone `checks/verify_five_mode.py` uses exact symbolic calculations to verify the polynomial coefficient norm \(S\), the derivative identity, the monic Legendre moment \(8/45\), and the antipodal double-zero polynomial. It independently constructs the full complex five-by-five Fourier Gram matrices and compares their entries with high-precision direct quadrature. Five widths compare unequal and equal antipodal designs, and five smaller widths test convergence of the normalized eigenvalues toward the claimed sharp constant. Execute `python checks/verify_five_mode.py` using `sympy` and `mpmath`; the tested package prints `TWO_ARC_FIVE_MODE_CHECKS_PASS 55`. Numerical convergence supports normalization, not the universal all-configurations proof.

## Relationship to prior work
Marceca, Romero and Speckbacher (arXiv:2301.11685, first public January 27, 2023) analyze Fourier concentration on nonconvex and nonsymmetric domains and obtain nonasymptotic eigenvalue-counting estimates. Their open-access article's main theorems do not optimize the smallest eigenvalue for a fixed five-character band over two shrinking arcs. Asipchuk and Drezels (arXiv:2211.03821, first public November 7, 2022) concern exponential Riesz bases for unions of intervals rather than this fixed-band minimax design. The published fixed-index low-bandwidth moment theorem for arbitrary spatial/frequency windows gives fixed-window asymptotics but expressly does not claim uniform control over degenerating windows; its theorem does not supply the asymmetric two-arc optimum or moving-window rigidity here.

The previously published sharp two-arc Fourier observability theorem treats **equal-width** arcs and derives a Legendre constant and antipodal optimality. For five modes its equal-width coefficient is \(64/(135\pi)\), the benchmark used above; it neither considers width allocations nor implies the factor-sixteen improvement for vanishing-fraction companion arcs. Related three- and four-mode results likewise restrict to equal arcs. The present result is an optimization over both component widths and their relative position, with a singularly unbalanced optimal geometry.

## Limitations
The theorem is asymptotic as total observed length tends to zero, not a formula for the finite-length optimal widths or a claim that \(a^{3/2}\) is the unique narrow-arc scale. The result fixes exactly two interval components, unit observation weight and the five consecutive characters; it does not cover arbitrary measurable masks, higher mode counts, or noise models. Historical originality is based on identified accessible comparisons and remains subject to unindexed or inaccessible specialized results. No independent mathematical validation has been performed.

## References
1. O. Asipchuk and V. Drezels, *Examples of exponential bases on union of intervals*, arXiv:2211.03821 (initial public version November 7, 2022); Canadian Mathematical Bulletin 66 (2023), 1296–1312; https://arxiv.org/abs/2211.03821.
2. F. Marceca, J. L. Romero and M. Speckbacher, *Eigenvalue estimates for Fourier concentration operators on two domains*, arXiv:2301.11685 (initial public version January 27, 2023); Archive for Rational Mechanics and Analysis 248 (2024), article 35; https://doi.org/10.1007/s00205-024-01979-9.
3. *Fixed-index low-bandwidth spectra for arbitrary two-window Fourier concentration*, published research record (October 25, 2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-fixed-index-low-bandwidth-spectra-for-arbitrary-two-window-fouri--175763578bb2.
4. *Sharp two-arc Fourier observability: a Legendre constant and asymptotic antipodal design*, published research record (November 8, 2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-two-arc-fourier-observability-a-legendre-constant-and-asym--900ee56c5370.
