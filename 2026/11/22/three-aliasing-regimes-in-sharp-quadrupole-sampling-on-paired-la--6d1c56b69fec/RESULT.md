# Three aliasing regimes in sharp quadrupole sampling on paired latitude rings

## Finding
Two mirror-symmetric regular sensor rings can recover all five real spherical quadrupoles using only three points per ring. The exact conditioning and optimal relative ring orientation exhibit three different regimes, depending on whether each ring contains three, four, or at least five equally spaced sites.

Let \(m\ge3\) be an integer, let \(0<t<1\), and let \(\delta\in\mathbb R\). Write \(r=\sqrt{1-t}\), \(h=\sqrt t\), and define the \(2m\) distinct points
\[
p_{j,+}=(r\cos(2\pi j/m),r\sin(2\pi j/m),h),\qquad
p_{j,-}=(r\cos(\delta+2\pi j/m),r\sin(\delta+2\pi j/m),-h),
\quad 0\le j<m.
\]
Let \(\mathcal H_2(S^2)\) be the five-dimensional space of real *pure degree-two* spherical harmonics, with norm for **probability** area measure \(d\sigma=d\omega/(4\pi)\). The equally weighted observation form is
\[
Q_{m,t,\delta}(f)=\frac1{2m}\sum_{j=0}^{m-1}\left(|f(p_{j,+})|^2+|f(p_{j,-})|^2\right).
\]
Its eigenvalues relative to \(\|f\|_{L^2(\sigma)}^2\) have the following complete formulas. Set
\[
C=\frac54(3t-1)^2,\qquad A=\frac{15}2t(1-t),\qquad B=\frac{15}8(1-t)^2.
\]
For \(m=3\), define \(\lambda_\pm=\tfrac12\big(A+B\pm\sqrt{(A-B)^2+4AB\sin^2(3\delta/2)}\big)\). The eigenvalue multiset is \(\{C,\lambda_-,\lambda_-,\lambda_+,\lambda_+\}\). For \(m=4\) it is
\[
\{C,A,A,B(1-|\cos2\delta|),B(1+|\cos2\delta|)\}.
\]
For every \(m\ge5\) it is \(\{C,A,A,B,B\}\), independently of \(\delta\).

Write \(\Lambda=\min_{\|f\|=1}Q_{m,t,\delta}(f)\) and \(\kappa^2=\lambda_{\max}/\lambda_{\min}\), with \(\kappa^2=\infty\) if the observation form is singular. In **all** three regimes, both of the following sharp extremal values are the same:
\[
\boxed{\max_{t,\delta}\Lambda=\frac{11-\sqrt{21}}{10}},\qquad
\boxed{\min_{t,\delta}\kappa^2=\frac{5+\sqrt{21}}4}.
\]
Every optimizer has the **unique** squared latitude \(t_*=(6-\sqrt{21})/15\). Their orientations differ sharply:

- For three sites per ring, **both** optimum criteria hold exactly when \(\delta\equiv0\pmod{2\pi/3}\): the two triangles must be aligned.
- For four sites per ring, **conditioning** is optimized exactly when \(\delta\equiv\pi/4\pmod{\pi/2}\). However, **worst-case energy** is optimal on the entire nontrivial phase plateau \(|\cos2\delta|\le\sqrt{21}-4\).
- For five or more sites per ring, **every** relative rotation optimizes both criteria at \(t_*\).

Three sites are the smallest possible equal ring population for full recovery: two rings with at most two sites each have fewer than the five measurements required by dimension. The six-site aligned triangular-prism family therefore achieves exactly the same best *normalized* conditioning and lower frame bound as every larger paired regular-ring family, despite its azimuthal aliasing. The half-step triangular antiprism \(\delta=\pi/3\), in contrast, is singular for all heights.

## Assumptions and scope
All rings are equally populated and mirror-symmetric, their site weights are equal, the sphere has radius one, and the observed signal belongs **exactly** to \(\mathcal H_2(S^2)\), not the full polynomial band through degree two. Rotating either ring by a multiple of \(2\pi/m\) only relabels its sites. The two rings remain distinct because \(h>0\). Bounds compare only these paired-ring geometries; the theorem does not assert global optimality among arbitrary spherical point sets, unequal weights, or all-band spherical harmonic sampling grids.

## Proof
**Normalized harmonic basis.** The following real functions form an orthonormal basis for \(\mathcal H_2\) in normalized spherical area:
\[
e_0=\frac{\sqrt5}{2}(3z^2-1),\quad
e_{1c}=\sqrt{15}\,zx,\quad e_{1s}=\sqrt{15}\,zy,\quad
e_{2c}=\frac{\sqrt{15}}2(x^2-y^2),\quad e_{2s}=\sqrt{15}\,xy.
\]
For example, this follows from \(\int x_i^4\,d\sigma=1/5\), \(\int x_i^2x_j^2\,d\sigma=1/15\) for distinct indices, and odd-monomial cancellation. In latitude coordinates the last four functions are respectively
\[
\sqrt{15}\,zr\cos\phi,\quad\sqrt{15}\,zr\sin\phi,\quad
\frac{\sqrt{15}}2r^2\cos2\phi,\quad\frac{\sqrt{15}}2r^2\sin2\phi.
\]
Their first- and second-order azimuthal column norms on each ring yield the quantities \(A\) and \(B\) above; \(e_0\) yields \(C\). The trace is \(C+2A+2B=5\), as it must be from the addition theorem and the normalized \(2m\)-point average.

**Complete alias analysis.** On an equilateral ring, \(\sum_{j=0}^{m-1}e^{2\pi i kj/m}=0\) unless \(m\mid k\). For \(m\ge5\), all distinct azimuthal orders \(-2,-1,0,1,2\) are orthogonal, proving the five diagonal values. For \(m=4\), the only collision is between orders \(-2\) and \(2\). The two real order-two columns on the first ring point along \((1,0)\), and on the second along \((\cos2\delta,\sin2\delta)\). Their \(2\times2\) Gram block has eigenvalues \(B(1\pm|\cos2\delta|)\); orders \(0,\pm1\) remain orthogonal.

For \(m=3\), the collisions are \(1\equiv-2\) and \(-1\equiv2\) modulo three. There are two identical real singular-value blocks, with diagonal entries \(A,B\). The order-one term changes sign between north and south, whereas the order-two term does not. Summing both rings, the singular magnitude of their off-diagonal coupling is precisely \(\sqrt{AB}|\sin(3\delta/2)|\): the relative complex contribution is proportional to \(1-e^{3i\delta}\). The two eigenvalues of each block are exactly \(\lambda_\pm\). This establishes the full spectrum for every \(m,t,\delta\). It also proves the stated loss of rank at the triangular antiprism. Apart from \(t=1/3\), the only other singular phases are \(\delta\equiv\pi/3\pmod{2\pi/3}\) when \(m=3\), and \(\delta\equiv0\pmod{\pi/2}\) when \(m=4\).

**Universal upper bound and exact E-optimality.** In every regime, \(\Lambda\le L(t):=\min\{C,A,B\}\), by the stated block eigenvalues (or the Rayleigh principle applied to the sector diagonal). Put \(t_*=(6-\sqrt{21})/15\). The identity \(15t_*^2-12t_*+1=0\) gives \(C(t_*)=A(t_*)=(11-\sqrt{21})/10\), while \(B(t_*)>A(t_*)\). For \(0<t<t_*\), strict increase of \(A\) implies \(L(t)<L(t_*)\). For \(t_*<t<1/3\), strict decrease of \(C\) gives the same conclusion. For \(1/3\le t\le1/2\), \(C\le5/16<L(t_*)\). For \(1/2\le t<1\), \(B\le15/32<L(t_*)\). Consequently \(t_*\) is the unique optimal squared height.

At this height, \(C=A<B\). For \(m=3\), \(\lambda_-<A\) unless \(\sin(3\delta/2)=0\), proving unique aligned rotation. For \(m=4\), \(\Lambda=A\) precisely when \(B(1-|\cos2\delta|)\ge A\), equivalent to \(|\cos2\delta|\le1-A/B=\sqrt{21}-4\). For \(m\ge5\), the eigenvalues do not depend on rotation. These are all E-equality cases.

**Universal condition-number optimum.** For all \(m\ge3\) and all rotations, the spectral extremes satisfy
\[
\lambda_{\max}\ge\max\{C,A,B\},\qquad
\lambda_{\min}\le\min\{C,A,B\}.
\]
Hence \(\kappa^2\ge R(t):=\max\{C,A,B\}/\min\{C,A,B\}\). At \(t_*\), \(R(t_*)=B/A=(5+\sqrt{21})/4=:R_*\). If \(0<t<t_*\), then \(R(t)\ge B/A=(1-t)/(4t)>R_*\). If \(t_*<t<1/3\), then \(R(t)\ge B/C=\frac32((1-t)/(1-3t))^2>R_*\), since the displayed quotient increases with \(t\). At \(t=1/3\), the condition number is infinite. For \(1/3<t\le2/5\), the bounds \(A\ge5/3\) and \(C\le1/20\) give \(R(t)\ge100/3>R_*\). Finally, for \(2/5\le t<1\), \(R(t)\ge A/B=4t/(1-t)\ge8/3>R_*\). Therefore \(t_*\) is uniquely condition-optimal. At that height, every nonzero alias coupling for \(m=3\) makes the bottom eigenvalue smaller and the top larger, so only alignment attains \(R_*\). For \(m=4\), any \(|\cos2\delta|>0\) makes the top eigenvalue larger than \(B\); hence only the half-step offset attains \(R_*\). For \(m\ge5\), all phases attain it. These claims are exact, including the stated nontrivial E-plateau.

## Verification
The bundled `verify.py` independently computes the five normalized real harmonic evaluations and each full \(5\times5\) sample Gram matrix, then diagonalizes it by a standard-library Jacobi eigensolver. It checks the three predicted spectral formulas on eight heights, eight relative rotations and all ring populations from three through ten (512 complete Gram tests), including the height of extremal conditioning and both alias-induced singular orientations. It also verifies exact polynomial identities with rational arithmetic and evaluates the two sharp extremal constants and the four-ring E-optimal plateau threshold. Run `python3 verify.py` from the package directory. Numerical tests verify only the implementation and sampled cases; the preceding finite-dimensional block identities and strict inequalities prove the result for every stated parameter.

## Relationship to prior work
Zandieh, Han and Avron (arXiv:2202.12995, first submitted 2022-02-25) prove general near-dimensional random sampling results for low-pass spherical harmonic expansion; they do not optimize this deterministic exact-degree, paired-ring geometry. Khalid, Kennedy and McEwen (arXiv:1403.4661), and Khalid–Kennedy's companion latitude-placement analysis, treat optimal-dimensional whole-band transforms and numerical ring placement, rather than this two-ring five-mode spectral classification.

The published result *Sharp quadrupole conditioning on paired spherical latitude rings* (published-finding corpus, 2026-11-01, identifier ending `38d9014ee346`) proves the same sharp latitude and condition number **for \(m\ge5\)**. It explicitly uses the nonaliasing hypothesis \(m\ge5\), and its phase-independence does not cover \(m=3,4\). The present additional result is the complete **minimal-population** regime and its opposite angular-optimality laws, including a nontrivial E-optimal phase plateau. The published six-sample *two great circles* theorem (published-finding corpus, 2026-11-08, identifier ending `0de67cc2f408`) uses two plane intersections through the sphere center, not two parallel latitude circles; its optimal lower frame bound is different. Another indexed interpolation result on two \(2L\)-point latitude rings, identifier ending `35d45a63d3a2`, concerns **row-space determinant optimization for the full band through degree \(L\)**, and does not imply the present pure-degree-two spectrum or E-plateau. These are comparisons of hypotheses and mathematical implications, not uniqueness proofs.

## Limitations
The height and orientation optimizers are sharp only within equally weighted, equally populated, mirror-symmetric regular latitude rings. The global six-point E-optimal design over unrestricted point sets is not addressed, nor are unequal ring populations, arbitrary spherical harmonic bands, or robustness to geometric perturbations of individual sensor sites. Previously indexed near-neighbor results have not been independently re-audited. Historical priority remains subject to specialized spherical-array and optimal-design literature not exhaustively searchable here. Independent mathematical audit has not been performed.

## References
1. A. Zandieh, I. Han, H. Avron, *Near Optimal Reconstruction of Spherical Harmonic Expansions*, arXiv:2202.12995, first submitted 2022-02-25, https://arxiv.org/abs/2202.12995.
2. Z. Khalid, R. A. Kennedy, J. D. McEwen, *An Optimal-Dimensionality Sampling Scheme on the Sphere with Fast Spherical Harmonic Transforms*, arXiv:1403.4661, first submitted 2014-03-19, https://arxiv.org/abs/1403.4661.
3. Z. Khalid, R. A. Kennedy, *On the Placement of Latitudes in Iso-Latitude Optimal-Dimensionality Sampling Schemes on the Sphere*, IEEE conference paper (2014), https://www.zubairkhalid.org/papers/C17.pdf.
4. *Sharp quadrupole conditioning on paired spherical latitude rings*, published-finding corpus, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-sharp-quadrupole-conditioning-on-paired-spherical-latitude-rings--38d9014ee346.
5. *Sharp six-sample reconstruction of real quadratic spherical harmonics from two great circles*, published-finding corpus, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-six-sample-reconstruction-of-real-quadratic-spherical-harm--0de67cc2f408.
6. *Sharp angular-offset determinant and conditioning for two spherical latitude rings*, published-finding corpus, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-sharp-angular-offset-determinant-and-conditioning-for-two-spheri--35d45a63d3a2.
