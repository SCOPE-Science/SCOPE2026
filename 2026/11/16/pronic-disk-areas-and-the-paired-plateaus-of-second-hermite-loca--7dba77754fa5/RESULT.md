# Pronic disk areas and the paired plateaus of second-Hermite localization

## Finding
For the normalized second-excited Hermite function \(h_2\), let \(H_s=V_{h_2}^{*}\mathbf 1_{D_s}V_{h_2}\) be the short-time Fourier transform localization operator on the origin-centered phase-space disk \(D_s=\{(x,\xi):\pi(x^2+\xi^2)\le s\}\), where \(s>0\). Write \(\lambda_j(s)=\langle H_sh_j,h_j\rangle\) for \(j=0,1,\ldots\). The Hermite functions form a complete orthonormal eigenbasis.

**Complete index-ordering theorem.** The eigenvalues are nonincreasing in Hermite index, \(\lambda_0(s)\ge\lambda_1(s)\ge\cdots\), **if and only if**
\[
s=k(k+1)\qquad\text{for some integer }k\ge1.
\]
At each such area, the exact equal-neighbor positions are
\[
 j\in\{k^2-1,k^2,(k+1)^2-1,(k+1)^2\},\qquad
 \lambda_{j+1}(s)=\lambda_j(s).
\]
Thus the ordered spectrum has precisely **two distinct triple eigenvalue plateaus**, on \(\operatorname{span}\{h_{k^2-1},h_{k^2},h_{k^2+1}\}\) and \(\operatorname{span}\{h_{(k+1)^2-1},h_{(k+1)^2},h_{(k+1)^2+1}\}\), with strictly decreasing steps everywhere else. No other Hermite mode shares either triple value. For every positive area not in this pronic sequence, some successive eigenvalues strictly increase.

In the smallest case \(s=2\), the first six levels form the two leading spectral triples,
\[
\lambda_0(2)=\lambda_1(2)=\lambda_2(2)=1-5e^{-2},\qquad
\lambda_3(2)=\lambda_4(2)=\lambda_5(2)=1-\frac{17}{3}e^{-2},
\]
and \(\lambda_5(2)>\lambda_6(2)>\lambda_7(2)>\cdots\).

## Assumptions and scope
The STFT is \(V_gf(x,\xi)=\int_{\mathbb R}f(t)\overline{g(t-x)}e^{-2\pi i\xi t}\,dt\). The \(L^2\)-normalized Hermite family is chosen with \(h_0(t)=2^{1/4}e^{-\pi t^2}\); scalar phases on higher \(h_j\) do not affect the result. The area of \(D_s\) in \((x,\xi)\)-coordinates is exactly \(s\). Every assertion holds for every real \(s>0\) and every integer Hermite index \(j\ge0\), including the boundary indices zero and one. The operator is compact, positive, and has strictly positive eigenvalues tending to zero. Eigenvalue multiplicities refer to the full Hilbert-space spectrum, not just a finite truncation.

## Proof
**1. Exact radial density.** The standard special-Hermite / Laguerre spectrogram identity is
\[
|V_{h_2}h_j(x,\xi)|^2=e^{-t}\frac{\min(2,j)!}{\max(2,j)!}
 t^{|j-2|}\left[L_{\min(2,j)}^{(|j-2|)}(t)\right]^2,
 \qquad t=\pi(x^2+\xi^2).
\]
Polar integration has radial measure \(dt\). Defining the polynomial
\[
Q_j(t)=t^2-2jt+j(j-1)=(t-j)^2-j,
\]
and evaluating the Laguerre polynomials of degrees zero, one and two gives, **uniformly for all \(j\ge0\)**,
\[
\lambda_j(s)=\int_0^s e^{-t}\frac{t^{j-2}Q_j(t)^2}{2j!}\,dt.
\tag{1}
\]
At \(j=0,1\) the apparent negative powers are removable: the corresponding integrands are \(e^{-t}t^2/2\) and \(e^{-t}t(2-t)^2/2\), respectively.

**2. Exact adjacent-gap identity.** Differentiating the claimed right side, using \(Q_{j+1}(t)=t^2-2(j+1)t+j(j+1)\), and expanding the polynomial identity
\[
(t-j+1)Q_jQ_{j+1}-t(Q'_jQ_{j+1}+Q_jQ'_{j+1})
=tQ_{j+1}^2-(j+1)Q_j^2
\]
gives the difference of the integrands in (1). Both sides of the integrated identity vanish at \(s\downarrow0\). Hence for all \(j\ge0\),
\[
\boxed{\lambda_{j+1}(s)-\lambda_j(s)
=-\frac{e^{-s}s^{j-1}}{2(j+1)!}Q_j(s)Q_{j+1}(s).}
\tag{2}
\]
For \(j=0\), cancellation of the apparent \(s^{-1}\) yields the regular expression \(-e^{-s}s^2(s-2)/2\).

**3. Necessity of pronic area.** For a fixed positive \(s\), regard \(Q_j(s)=j^2-(2s+1)j+s^2\) as a quadratic in the real variable \(j\). Its two real roots are
\[
 a_s=s+\frac12-\sqrt{s+\frac14},\qquad
 b_s=s+\frac12+\sqrt{s+\frac14}.
\]
The signs are positive before \(a_s\), negative strictly between the roots, and positive after \(b_s\). In particular \(Q_0(s)=s^2>0\) and \(Q_j(s)>0\) for all sufficiently large integers. A negative integer index always exists: for \(0<s<2\), take \(j=1\); for \(s\ge2\), take \(j=\lfloor s\rfloor\), since \(Q_j(s)=(s-j)^2-j<0\). By (2), if \(\lambda_j(s)\) is nonincreasing at every index, neither the passage from positive to negative \(Q_j\) nor the passage back can occur across a pair of nonzero opposite signs. Therefore **both** \(a_s,b_s\) must be integers.

Put \(d=b_s-a_s=\sqrt{4s+1}\). Since \(a_s,b_s\) are integers, \(d\) is an integer and
\[
 a_s=\frac{(d-1)^2}{4},\quad b_s=\frac{(d+1)^2}{4},\quad s=\frac{d^2-1}{4}.
\]
Their integrality forces \(d\) odd; because \(s>0\), write \(d=2k+1\) for \(k\ge1\), obtaining \(s=k(k+1)\), \(a_s=k^2\), and \(b_s=(k+1)^2\).

**4. Sufficiency and precise eigenspaces.** If \(s=k(k+1)\), the same quadratic factors as
\[
Q_j(s)=(j-k^2)(j-(k+1)^2).
\]
Two successive values of this polynomial have the same sign or include a zero; hence (2) is never positive. Its only zeros occur at \(j=k^2-1,k^2,(k+1)^2-1,(k+1)^2\). Since the roots are separated by \(2k+1\ge3\), these are two disjoint runs of two equality edges each, yielding exactly the two triple eigenspaces and strict inequality everywhere else. The first triple value exceeds the second by at least one intervening strict decrease. This also shows that no separated index can share a triple eigenvalue.

**5. First special disk.** Formula (1), using integer incomplete-gamma integration at \(s=2\), yields the displayed values; the ordering and all multiplicities already follow from Steps 2–4. This completes the proof.

## Verification
Run `python verify_pronic.py` in an environment with Python 3 and SymPy. The checker expands the universal polynomial identity symbolically, independently integrates the exact radial polynomial densities at 44 Hermite levels using finite gamma expansions, compares 43 adjacent-gap formulas in exact arithmetic, and tests the two triple blocks at five pronic areas plus 15 nonpronic thresholds. Expected terminal marker:

`H2_PRONIC_ORDER_PASS universal_polynomial_identity=1 exact_integral_levels=44 exact_neighbor_gaps=43 pronic_areas=5 nonpronic_radii=15 double_triplet_area=2`

The infinite theorem and the complete root classification come from the proof, not the finite test ranges.

## Relationship to prior work
Abreu–Gröchenig–Romero establish Hermite diagonalization of disk localization operators, special-Hermite integral eigenvalues, and the distinction between Hermite-index and decreasing-eigenvalue order; their explicit crossing illustration concerns the first Hermite window. Keller–Luef provide the general polyanalytic Toeplitz and Laguerre framework, without this disk-specific ordering classification. Formula (1) uses those standard facts. The new result asserted here is the all-radius **if-and-only-if** index-ordering law for the second-Hermite window and the two exact triple plateaus at every exceptional radius. These are not obtained merely by replacing the first-Hermite index in its known gap formula: the quadratic sign transitions and their coincident square-index roots are essential.

At \(s=k(k+1)\), every initial segment \(\operatorname{span}\{h_0,\ldots,h_{N-1}\}\) is a legitimate top-\(N\) spectral subspace (ties resolved within each triple). This gives a precise exceptional configuration in the comparison of finite polyanalytic and finite Weyl–Heisenberg ensembles. No assertion is made that the same property is impossible for one particular cutoff \(N\) at a nonpronic radius.

## Limitations
The claim concerns only the second-excited Hermite window, origin-centered disks, and ordering by the usual Hermite index. It does not classify every nonconsecutive eigenvalue coincidence at nonexceptional radii, the corresponding eigenvalue gaps' sizes, other window indices, or noncircular domains. Literature priority remains provisional: equivalent specialist results under Landau-level or polyanalytic-Toeplitz nomenclature may exist. The accompanying test does not establish an infinite statement independently.

## References
1. L. D. Abreu, K. Gröchenig, J. L. Romero, *Harmonic Analysis in Phase Space and Finite Weyl–Heisenberg Ensembles*, arXiv:1704.03042, first posted 2017-04-10; *Journal of Statistical Physics* 174 (2019), 1104–1136. https://arxiv.org/abs/1704.03042 ; https://doi.org/10.1007/s10955-019-02226-2 . See §4, especially Proposition 4.1, Lemma 4.2, Figure 4, and Corollary 4.6.
2. J. Keller, F. Luef, *Polyanalytic Toeplitz Operators: Isomorphisms, Symbolic Calculus and Approximation of Weyl Operators*, *Journal of Fourier Analysis and Applications* 27 (2021), article 47. https://doi.org/10.1007/s00041-021-09843-0 . See §3.1–3.2, particularly Eq. (21).
