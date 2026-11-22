# Equidihedral ridge curvature and parity cancellation for Van Kampen–Flores polytopes

## Finding
Let \(n\ge4\) be an integer and let \(\Omega_n\) be the canonical regular-simplex symmetrization in \(\mathbb R^n\):
\[
H_n=\left\{x\in\mathbb R^n:\sum_{i=1}^n x_i=0\right\},\qquad
\delta_i=e_i-\frac1n\mathbf1,\qquad
\Omega_n=\operatorname{conv}\{\pm\delta_i:1\le i\le n\}\subset H_n.
\]
The intrinsic Euclidean dimension is \(d=n-1\). Every codimension-two face (ridge) of \(\Omega_n\) is an \((n-3)\)-simplex. **All ridges are mutually congruent and have the same exterior dihedral angle**, although the facet types and their combinatorics change with parity. Define
\[
\varepsilon_n=\begin{cases}0,&n\text{ even},\\1,&n\text{ odd},\end{cases}\qquad
r_n=\begin{cases}
\frac12\binom{n}{n/2}(n/2)^2,&n\text{ even},\\[2pt]
\frac12 n(n-1)\binom{n-1}{(n-1)/2},&n\text{ odd},
\end{cases}
\]
\[
\alpha_n=\begin{cases}
\arccos(1-4/n),&n\text{ even},\\[2pt]
\arccos(1-1/(n-1)),&n\text{ odd}.
\end{cases}
\]
Then \(r_n\) is the **exact number of ridges**, each ridge has intrinsic volume
\[
\mathcal H^{n-3}(G)=\frac1{(n-3)!}\sqrt{\frac{2(n-2)+\varepsilon_n}{n}},
\]
and its interior dihedral angle is \(\pi-\alpha_n\). Consequently the complete codimension-two Steiner invariant is
\[
\boxed{\;V_{n-3}(\Omega_n)=\frac{r_n\,\alpha_n}{2\pi(n-3)!}
\sqrt{\frac{2(n-2)+\varepsilon_n}{n}}.\;}
\]
Despite the approximately twofold difference between odd- and even-order ridge counts, and the reverse twofold difference in their small exterior angles, the leading intrinsic curvature is **parity independent**:
\[
\boxed{\quad\lim_{n\to\infty}\frac{(n-3)!\,V_{n-3}(\Omega_n)}{2^n n}
=\frac1{4\pi}\sqrt{\frac2\pi}.\quad}
\]

## Assumptions and scope
All statements are for integer \(n\ge4\), with the Euclidean inner product induced from \(\mathbb R^n\) on the zero-sum hyperplane \(H_n\). The polar is relative to \(H_n\); we use unit support offsets for the displayed generators. The intrinsic volumes are those in the classical Steiner normalization
\[
\operatorname{Vol}_{d}(K+tB_d)=\sum_{j=0}^{d}\kappa_{d-j}V_j(K)t^{d-j},\qquad t\ge0,
\]
where \(B_d\) is the intrinsic unit ball and \(\kappa_2=\pi\). Thus the asserted invariant is \(V_{d-2}\), not \(V_2\) (unless \(d=4\)). We make no assertion for nonregular generators, arbitrary Bier spheres, or affine deformations that fail to preserve this Euclidean metric.

## Proof
**1. Polar, vertices, and ridge–edge duality.** Since \(\langle x,\delta_i\rangle=x_i\) for \(x\in H_n\), polarity gives
\[
Q_n:=\Omega_n^\circ=H_n\cap[-1,1]^n.
\]
Every vertex of \(Q_n\) has at least \(n-1\) saturated cube coordinates. For \(n=2k\), the only possible vertices have exactly \(k\) entries \(+1\) and \(k\) entries \(-1\). There are \(\binom nk\) of them. Two such vertices are joined by an edge exactly when they differ by swapping one positive and one negative coordinate: that is equivalent to sharing exactly \(n-2\) saturated coordinate equations, which cut out a one-dimensional face of \(Q_n\). Each vertex has degree \(k^2\), giving \(r_n=\binom nk k^2/2\).

For \(n=2k+1\), each polar vertex has \(k\) coordinates \(+1\), \(k\) coordinates \(-1\), and one zero. There are \(n\binom{n-1}{k}\) vertices. An edge moves the unique zero to any one of the other \(n-1\) positions, changing the former zero to the opposite sign of the moved entry. Again its endpoints share exactly \(n-2\) saturated coordinates and no additional independent cube equality; the edge degree is \(n-1\). Thus there are \(r_n=n(n-1)\binom{n-1}{k}/2\) edges. As \(Q_n\) contains the origin in its interior, face polarity bijects its edges with the ridges of \(\Omega_n\), establishing the census.

**2. Uniform dihedral angles.** At a vertex \(u\in Q_n\), the corresponding primal facet has outward normal \(u\) and support height \(1\). For adjacent vertices \(u,v\in Q_n\), the exterior dihedral angle \(\alpha\) of the corresponding primal facets is therefore \(\arccos(\langle u,v\rangle/(\|u\|\|v\|))\). In even order, \(\|u\|^2=\|v\|^2=n\) and \(\|u-v\|^2=8\); their normalized inner product is \(1-4/n\). In odd order, \(\|u\|^2=\|v\|^2=n-1\) and \(\|u-v\|^2=2\); their normalized inner product is \(1-1/(n-1)\). This proves the two parity formulas for the single exterior angle.

**3. Every ridge is the same Euclidean simplex.** A polar edge is specified by \(N=n-2\) shared saturated coordinate equations. The corresponding ridge in \(\Omega_n\) is the convex hull of the \(N\) signed vertices \(s_i\delta_i\) at these indices, with \(s_i\in\{\pm1\}\). In even order the signs are balanced, with \(N/2\) of each sign; in odd order their counts differ by one. Consequently \(m=\sum_i s_i\) satisfies \(m^2=\varepsilon_n\). Any two such lists are related by a coordinate permutation and possibly reflection, proving congruence.

For a fixed list, write its \(N\times N\) vertex Gram matrix as \(G\). The centered-simplex Gram determinant identity gives
\[
((N-1)!)^2\mathcal H^{N-1}(G_{\mathrm{ridge}})^2
=\det(G)\,\mathbf1^{\mathsf T}G^{-1}\mathbf1.
\]
Because \(\langle s_i\delta_i,s_j\delta_j\rangle=\delta_{ij}-s_is_j/n\), we have \(G=I_N-ss^{\mathsf T}/n\), hence by the rank-one determinant and inversion formulas
\[
\det(G)=\frac2n,\qquad G^{-1}=I_N+\frac12ss^{\mathsf T},\qquad
\mathbf1^{\mathsf T}G^{-1}\mathbf1=N+\frac{m^2}{2}.
\]
The resulting squared volume is \([2(n-2)+\varepsilon_n]/[n((n-3)!)^2]\), strictly positive; therefore all such faces are genuine simplices of dimension \(n-3\).

**4. Intrinsic volume.** At a ridge of a Euclidean polytope, the exterior normal cone is a planar sector of aperture \(\alpha\), so its normalized external angle is \(\alpha/(2\pi)\). The classical polyhedral face formula for the intrinsic volume \(V_{d-2}\) is the sum over all ridges of their \((d-2)\)-volumes times this angle fraction. Steps 1–3 yield the displayed exact formula. At \(n=4\), \(\Omega_4\) is a cube with twelve unit-length ridges and right dihedral angles; the formula returns \(V_1=3\).

**5. The parity-canceling limit.** Stirling's central-binomial estimate gives, with relative error \(o(1)\),
\[
r_n\sim\begin{cases}
\displaystyle\frac{2^n n^{3/2}}8\sqrt{\frac2\pi},&n\text{ even},\\[3pt]
\displaystyle\frac{2^n n^{3/2}}4\sqrt{\frac2\pi},&n\text{ odd},
\end{cases}
\]
whereas the elementary expansion \(\arccos(1-x)\sim\sqrt{2x}\) gives \(\alpha_n\sim2\sqrt{2/n}\) in even order and \(\alpha_n\sim\sqrt{2/n}\) in odd order. Also \(\sqrt{[2(n-2)+\varepsilon_n]/n}\to\sqrt2\). Substitution into Step 4 yields the common displayed limit.

## Verification
The companion standalone `check.py` independently enumerates all vertices of \(Q_n\) for \(n=4,\ldots,8\). For each pair it determines edge adjacency from shared saturated cube constraints, explicitly forms the corresponding ridge points in \(H_n\), computes their volumes from coordinate-difference Gram determinants, and compares facet-normal angles with the claimed formulas. It additionally calls an independent convex-hull routine on the actual primal generators. It checks the limiting normalization at even and odd orders up to \(n=1001\) using logarithmic factorials. Run: `OPENBLAS_NUM_THREADS=1 python check.py` (Python 3 with NumPy and SciPy). Its final success marker is `VAN_KAMPEN_FLORES_RIDGE_CHECK_PASS`. These finite computations corroborate but do not replace the all-order analytic proof.

## Relationship to prior work
Jevtić and Živaljević (arXiv:2108.00618, first posted August 2, 2021), in their Sections 2–3, identify \(\Omega_n\), its maximal Bier-sphere volume setting and its polar median-hypersimplex realization, including the basic face structure. Those premises are credited, not new. Jevtić, Timotijević and Živaljević (arXiv:1812.00397) introduced closely related opposite-simplex convex hulls in their polytopal Bier-sphere constructions. A previously published exact covariance and isotropic-constant comparison for \(\Omega_n\) works with the same body, but its volume moments do not determine its ridge angle or second Steiner coefficient. An exact second-intrinsic-volume formula for ordinary hypersimplices concerns a different body: the intrinsic volumes of a polytope are not generally recovered by simply substituting those of its polar. The new statement is the complete equidihedral ridge classification, the explicit intrinsic volume, and the quantitative parity-canceling limit.

## Limitations
The result is confined to the canonical Euclidean regular-simplex symmetrization; its metric rigidity need not survive a general linear transformation. The asymptotic formula is a leading-order statement and does not give a uniform remainder over all transformations. The normal-cone face formula and cube-slice vertex census are standard premises; priority is asserted only for their new exact combination and consequence, and may be affected by historical formulas under alternative terminology such as projections of cross-polytopes or symmetric simplex hulls. No independent mathematical audit has been performed.

## References
1. F. D. Jevtić and R. T. Živaljević, *Bier spheres of extremal volume and generalized permutohedra*, arXiv:2108.00618, first public posting 2021-08-02. https://arxiv.org/abs/2108.00618
2. F. D. Jevtić, M. Timotijević and R. T. Živaljević, *Polytopal Bier spheres and Kantorovich–Rubinstein polytopes of weighted cycles*, arXiv:1812.00397, first public posting 2018-12-02. https://arxiv.org/abs/1812.00397
3. Classical Steiner formula and polyhedral external-angle intrinsic-volume face formula; see A. Colesanti, M. Ludwig, F. Mussnig, *The Hadwiger theorem on convex functions, III: Steiner formulas and mixed Monge–Ampère measures*, arXiv:2111.05648. https://arxiv.org/abs/2111.05648
4. *A parity-reversing isotropic comparison for Van Kampen–Flores polytopes* (prior covariance/volume-moment result, separate invariant). https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-a-parity-reversing-isotropic-comparison-for-van-kampen-flores-po--5bbe9fa6be5a
5. *A Gaussian rank-window curvature crossover and exact second intrinsic volumes of hypersimplices* (primal hypersimplex, not this polar). https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-a-gaussian-rank-window-curvature-crossover-and-exact-second-intr--3b7f285b6bbf
