# Magnetic-flux spectral doublets for an equilateral triple of Gaussian localization disks

## Finding

Let \(R>0\) be fixed. In the standard Bargmann–Fock space, let \(T_d\) denote the Gaussian localization operator whose mask is the union of three disks of radius \(\sqrt R\), centered at the vertices \(w_j=d\exp(2\pi i j/3)/\sqrt3\), \(j=0,1,2\), of an equilateral triangle of side \(d>2\sqrt R\). Write its decreasing nonzero eigenvalues as \(\nu_1(d)\ge\nu_2(d)\ge\cdots\). Set

\[
\ell=1-e^{-R},\qquad s_d=e^{-d^2/2},\qquad \Phi_d=\frac{\sqrt3\,d^2}{2},
\]

and let \(b_1(d)\ge b_2(d)\ge b_3(d)\) be the decreasing rearrangement of

\[
\left\{\cos\left(\frac{\Phi_d+2\pi q}{3}\right):q=0,1,2\right\}.
\]

Then, as \(d\to\infty\),

\[
\boxed{\nu_j(d)=\ell\bigl(1+2s_d b_j(d)\bigr)
  +O_R\!\left(e^{-(d-\sqrt R)^2}\right),\quad j=1,2,3.}
\]

Moreover, \(\limsup_{d\to\infty}\nu_4(d)\le 1-(1+R)e^{-R}<\ell\). Hence there are precisely three isolated eigenvalues in a fixed neighborhood of \(\ell\) for sufficiently large \(d\).

Put \(t(d)=\Phi_d/(2\pi)=\sqrt3\,d^2/(4\pi)\). Along any sequence \(d\to\infty\) for which \(t(d)\) is an integer, the normalized top gap \((\nu_1-\nu_2)/(\ell s_d)\) tends to \(3\); along any sequence for which \(t(d)\) is a half-integer, it tends to \(0\), while \((\nu_2-\nu_3)/(\ell s_d)\) tends to \(3\). The normalized leading eigenvalue correction \((\nu_1-\ell)/(\ell s_d)\) has the full cluster interval \([1,2]\).

**Exact degeneracies.** For each sufficiently large integer \(n\), there is a distance \(d_n^{\mathrm{top}}>2\sqrt R\) with

\[
 t(d_n^{\mathrm{top}})=n+\tfrac12+o(1),\qquad
 \nu_1(d_n^{\mathrm{top}})=\nu_2(d_n^{\mathrm{top}})>\nu_3(d_n^{\mathrm{top}}),
\]

and there is a distance \(d_n^{\mathrm{low}}>2\sqrt R\) with

\[
 t(d_n^{\mathrm{low}})=n+o(1),\qquad
 \nu_1(d_n^{\mathrm{low}})>\nu_2(d_n^{\mathrm{low}})=\nu_3(d_n^{\mathrm{low}}).
\]

Each equality has multiplicity **exactly two**. The theorem asserts existence, not uniqueness, of a crossing near each indicated flux.

## Assumptions and scope

The Bargmann–Fock space is

\[
\mathcal F^2=\left\{f\text{ entire}:\|f\|^2=\frac1\pi\int_{\mathbb C}|f(z)|^2e^{-|z|^2}\,dA(z)<\infty\right\}.
\]

With \(k_w(z)=\exp(z\overline w-|w|^2/2)\) the unit coherent vector, set

\[
T_{\Omega}=\frac1\pi\int_{\Omega}|k_w\rangle\langle k_w|\,dA(w)
\]

as a positive trace-class operator. The ket–bra denotes the rank-one orthogonal projection, so the expression is independent of inner-product convention. All distances and areas in this note are in the above Fock coordinate: one disk has normalized trace \(R\) and Euclidean area \(\pi R\). The side \(d\) varies, while \(R\) is fixed; the orientation is counterclockwise. Reversing it conjugates the phases but does not alter the spectrum.

## Proof

**1. A single disk and its spectral gap.** For the disk \(D(0,\sqrt R)\), the normalized monomials \(e_m(z)=z^m/\sqrt{m!}\) diagonalize the concentration operator, with eigenvalues

\[
\ell_m=\frac1{m!}\int_0^R e^{-u}u^m\,du
=1-e^{-R}\sum_{j=0}^{m}\frac{R^j}{j!}.
\]

These decrease strictly; in particular \(\ell_0=\ell\) and \(\ell_1=1-(1+R)e^{-R}\), with gap \(\ell-\ell_1=Re^{-R}>0\). Under Weyl translations of the Fock space, the disk centered at \(w_j\) has decomposition

\[
T_{D(w_j,\sqrt R)}=\ell |k_{w_j}\rangle\langle k_{w_j}|+B_j,
\]

where \(B_j\ge0\), \(B_jk_{w_j}=0\), \(B_j\) is compact, and \(\|B_j\|=\ell_1\). Write \(T_d=K_d+B_d\), with \(K_d=\ell\sum_j|k_{w_j}\rangle\langle k_{w_j}|\) and \(B_d=\sum_jB_j\).

**2. Separation of the nonleading sectors.** For any fixed compact operator \(C\), the Weyl translates of \(C\) at pairwise divergent displacements are asymptotically disjoint in the following sense: products of translates of a fixed positive compact operator, at mutually distant locations, converge to zero in operator norm. To verify this without assuming it, approximate \(C\) by its finite-rank Hermite spectral truncations. Every matrix coefficient between displaced fixed Hermite functions is a polynomial in the relative displacement and its complex conjugate times \(e^{-|h|^2/2}\) (the Weyl displacement identity); hence it vanishes as \(|h|\to\infty\). Restore the compact tails in operator norm. Consequently \(\|B_iB_j\|\to0\) for \(i\ne j\). Since \(B_j^2\le\ell_1B_j\), for \(b_d=\|B_d\|\) we obtain

\[
b_d^2=\|B_d^2\|\le \ell_1 b_d+\sum_{i\ne j}\|B_iB_j\|,
\]

so \(\|B_d\|\le\ell_1+o(1)\). As \(K_d\) has rank at most three, the min–max principle gives \(\nu_4(d)\le\ell_1+o(1)\). On the other hand, its nonzero spectrum converges to three copies of \(\ell\), and \(T_d\ge K_d\); therefore all three leading eigenvalues of \(T_d\) converge to \(\ell\).

**3. The exponentially accurate three-dimensional reduction.** Let \(P_d\) be the orthogonal projection onto \(E_d=\operatorname{span}\{k_{w_0},k_{w_1},k_{w_2}\}\) and put \(Q_d=I-P_d\). The Gram matrix on this family equals \(I+O(e^{-d^2/2})\), so its coefficient map is uniformly conditioned for large \(d\). If \(i\ne j\), the coherent state centered at \(w_i\) has spectral mass in the disk at \(w_j\) bounded by

\[
0\le\langle k_{w_i},B_jk_{w_i}\rangle
\le\langle k_{w_i},T_{D(w_j,\sqrt R)}k_{w_i}\rangle
=\frac1\pi\int_{D(w_j,\sqrt R)}e^{-|z-w_i|^2}\,dA(z)
\le R e^{-(d-\sqrt R)^2}.
\]

Using \(B_jk_{w_j}=0\), positivity, and \(B_j^2\le\ell_1B_j\), uniformly on the unit sphere of \(E_d\) this implies

\[
\|P_dB_dP_d\|=O_R(e^{-(d-\sqrt R)^2}),\qquad
\|Q_dB_dP_d\|=O_R(e^{-(d-\sqrt R)^2/2}).
\]

The \(Q_d\)-diagonal block is bounded above by \(\ell_1+o(1)\). Since the \(P_d\)-block spectrum lies near \(\ell>\ell_1\), the Schur complement at each of the three upper eigenvalues gives a self-adjoint correction of norm at most

\[
\frac{\|P_dT_dQ_d\|^2}{\ell-\ell_1-o(1)}
=O_R(e^{-(d-\sqrt R)^2}).
\]

The min–max principle or the Schur complement eigenvalue comparison therefore matches the leading three eigenvalues of \(T_d\), in order, to those of \(P_dK_dP_d\), with precisely this additive error. The three nonzero eigenvalues of \(K_d\) are \(\ell\) times the three eigenvalues of the coherent-state Gram matrix.

**4. The triangular phase and its spectrum.** Coherent overlaps satisfy

\[
\langle k_{w_i},k_{w_j}\rangle
=e^{-|w_i-w_j|^2/2}\,e^{i\operatorname{Im}(w_j\overline w_i)}.
\]

Each side has magnitude \(s_d=e^{-d^2/2}\), and the ordered product of the three overlaps around the triangle has gauge-invariant phase \(\Phi_d=\sqrt3 d^2/2\), twice its Euclidean area. Since the centers are equidistant from zero and related by a \(120^\circ\) rotation, their Gram matrix is circulant, with a directed edge entry \(s_de^{i\Phi_d/3}\). Fourier diagonalization of this \(3\times3\) matrix gives

\[
\operatorname{spec}(G_d)=\left\{1+2s_d\cos\left(\frac{\Phi_d+2\pi q}{3}\right):q=0,1,2\right\}.
\]

Combining with Step 3 proves the three-eigenvalue expansion. The remainder is \(o(s_d)\), because \(e^{-(d-\sqrt R)^2}/s_d=\exp(-d^2/2+2d\sqrt R-R)\to0\). At integer flux units \(t(d)\in\mathbb Z\), the ordered cosines are \((1,-1/2,-1/2)\). At half-integer flux units they are \((1/2,1/2,-1)\). These establish the two gap limits. As \(t(d)\) varies continuously and unboundedly, the top ordered cosine ranges over \([1/2,1]\), giving the claimed full cluster interval \([1,2]\).

**5. Genuine twofold crossings.** Let \(U\) be the unitary induced by planar rotation through \(2\pi/3\) on \(\mathcal F^2\). Since the union of disks is rotation-invariant, \(U\) commutes with \(T_d\) for every \(d\). Its three character spaces are closed, fixed subspaces. The coherent span \(E_d\) has exactly one line in each character space. By Steps 2–3, for sufficiently large \(d\) there is exactly one eigenvalue \(\alpha_q(d)\) near \(\ell\) in each character space, and the sectorwise Schur estimates give the individual cosine branches (up to relabelling that is fixed once and for all by the rotation convention). These eigenvalues are continuous in \(d\): the disk symbols vary continuously in \(L^1\), which bounds the trace-norm difference of the corresponding Toeplitz operators.

Near each sufficiently large half-integer \(t=n+1/2\), the two leading cosine branches cross *transversely* as functions of \(t\), while the third is lower by a fixed positive multiple of \(s_d\). At \(t=n+1/2\pm\epsilon\) for any fixed small \(\epsilon>0\), the corresponding two sector eigenvalues have opposite order for all sufficiently large \(n\), since the error is \(o(s_d)\). The intermediate-value theorem produces an exact sector crossing between these values, and the third eigenvalue stays below. The same argument near \(t=n\) yields an exact crossing of the two lower branches. Since the argument works for every arbitrarily small fixed \(\epsilon\), the crossing locations satisfy \(t=n+1/2+o(1)\) and \(t=n+o(1)\), respectively. The fourth eigenvalue remains a fixed amount below \(\ell\), proving that these crossing eigenvalues have multiplicity exactly two. No derivative error estimate or uniqueness claim is needed.

## Verification

The accompanying `check_triangle.py` constructs Fock-basis matrices directly by radial and angular quadrature over the **original three disks**, rather than using the three-state Gram approximation as input. At five triangle areas it compares the leading eigenvalues with the predicted flux-dependent amplitudes and checks that the next eigenvalue is close to the single-disk first excited level. It also checks distinct integer and half-integer flux patterns. Running `OPENBLAS_NUM_THREADS=1 python check_triangle.py` with Python 3, NumPy, and SciPy produced `TRIANGLE_FLUX_CHECKS_PASS 34`. The numerical truncations, quadrature and floating-point tolerances are finite checks only; the universal theorem is proved above.

## Relationship to prior work

Nicola and Tilli, *The norm of time-frequency and wavelet localization operators* (arXiv:2207.08624, first public 18 July 2022), prove sharp global norms for localization weights, including disk extremality via the Faber–Krahn bound, but no phase-sensitive three-disk asymptotic. The Weyl/coherent-state framework appears in Fulsche and Hagger, *Quantum harmonic analysis for polyanalytic Fock spaces* (arXiv:2308.11292, first public 22 August 2023); it does not calculate eigenvalue crossings for disjoint disk masks. Berceanu, *Coherent states, phases and symplectic areas of geodesic triangles* (arXiv:math/9903190, 1999), establishes the geometric meaning of a triangular coherent-state phase, which is **not** claimed as novel here. The present work derives its effect on three isolated concentration eigenvalues, plus infinitely many exact twofold eigenvalue crossings. Global norm inequalities, the coherent overlap formula, and elementary circulant diagonalization are inputs, not independent novelty claims. Earlier multiwell Toeplitz or magnetic tunneling theory may contain a reformulation; this historical-priority risk remains.

## Limitations

This is a fixed-positive-radius, large-side-length result for exactly three **equal** disjoint disks at equilateral vertices with Gaussian window. It does not treat other triangles, unequal disks, growing radii, or the complete small-eigenvalue spectrum. The crossing theorem establishes existence and exact multiplicity, not uniqueness of the crossing in each flux cell. The order term is uniform for fixed \(R\) as \(d\to\infty\), but no uniformity as \(R\) varies is claimed. No external or independent validation of the argument has been performed.

## References

1. F. Nicola and P. Tilli, *The norm of time-frequency and wavelet localization operators*, arXiv:2207.08624 (2022), https://arxiv.org/abs/2207.08624 .
2. R. Fulsche and R. Hagger, *Quantum harmonic analysis for polyanalytic Fock spaces*, arXiv:2308.11292 (2023), https://arxiv.org/abs/2308.11292 .
3. S. Berceanu, *Coherent states, phases and symplectic areas of geodesic triangles*, arXiv:math/9903190 (1999), https://arxiv.org/abs/math/9903190 .
4. I. Daubechies, *Time-frequency localization operators: a geometric phase space approach*, IEEE Trans. Inform. Theory **34** (1988), 605–612.
