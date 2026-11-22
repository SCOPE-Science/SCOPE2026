# Optimal minimum projection spacing of regular-simplex vertices

## Finding

Fix an integer \(d\ge3\). Take a regular Euclidean \(d\)-simplex with unit edge lengths and project its \(d+1\) labelled vertices orthogonally onto a line with Haar-uniform direction in the simplex's affine span. Write the ordered projected vertex coordinates as \(z_{(1)}<\cdots<z_{(d+1)}\), and define the **vertex-resolution margin**
\[
G=\min_{1\le j\le d}(z_{(j+1)}-z_{(j)}).
\]
Then
\[
\boxed{\max G=g_d=\sqrt{\frac{6}{d(d+1)(d+2)}}.}
\]
There are exactly \((d+1)!\) maximizing oriented directions, characterized by all \(d\) consecutive projected vertex gaps being equal to \(g_d\).

Write \(\sigma_{d-1}=2\pi^{d/2}/\Gamma(d/2)\) for the surface area of the unit sphere in \(\mathbb R^d\), and \(A_d=d(d+1)(d+2)/12\). The probability that a random viewing direction nearly maximizes the minimum separation satisfies
\[
\boxed{\Pr(G>g_d-\varepsilon)=C_d\varepsilon^{d-1}+O_d(\varepsilon^d),\qquad
C_d=\frac{2^{(3d-1)/2}\sqrt{d+1}\,A_d^{\,d-1/2}}
{\sigma_{d-1}(d-1)!d!}.}
\]
In particular, for the unit-edge tetrahedron, \(g_3=1/\sqrt{10}\) and \(C_3=2\cdot5^{5/2}/(3\pi)\).

There is also a conditional **joint spacing law**. Under \(G>g_d-\varepsilon\), let \(g_j=z_{(j+1)}-z_{(j)}\), \(a_j=j(d+1-j)/2\), \(h_j=g_j-(g_d-\varepsilon)\), and
\[
Q_j=\frac{a_jh_j}{\sum_{k=1}^d a_kh_k}\quad(1\le j\le d).
\]
The vector \(Q=(Q_1,\ldots,Q_d)\) converges in **total variation** to \(\operatorname{Dirichlet}(1,\ldots,1)\), uniformly distributed on the standard \((d-1)\)-simplex. The projected-vertex ordering is uniform among all \((d+1)!\) permutations and independent of \(Q\) for each admissible threshold, and hence in the limit.

A finite-threshold exact integral also holds. For \(0\le t<g_d\), put \(m=d+1\),
\[
M_{ij}=\frac{\min(i,j)[m-\max(i,j)]}{m}\quad(1\le i,j\le d),\qquad
B_t=\frac12-A_dt^2.
\]
For \(q_j\ge0\) and \(\sum_jq_j=1\), set
\[
H(q)=\sum_{i,j=1}^dM_{ij}\frac{q_iq_j}{a_ia_j},\qquad
s_t(q)=\frac{B_t}{\sqrt{t^2+B_tH(q)}+t}.
\]
Here \(dq=dq_1\cdots dq_{d-1}\), with \(q_d=1-\sum_{j<d}q_j\), is the standard simplex-coordinate measure on \(\Delta_{d-1}\). Then
\[
\boxed{\Pr(G>t)=\frac{\sqrt{d+1}\,2^{(3d-2)/2}}{\sigma_{d-1}d!}
\int_{\Delta_{d-1}}\frac{s_t(q)^{d-1}}{t+s_t(q)H(q)}\,dq.}
\]
For \(t\ge g_d\) the probability is zero. At \(t=0\) the displayed formula equals one.

## Assumptions and scope

Directions are uniformly distributed by rotationally invariant surface area on the unit sphere of the \(d\)-dimensional affine span, not by a distribution of affine offsets. The simplex has unit edge length; changing its edge length multiplies every gap and the maximizer by that scale. Tied projected coordinates have zero probability. All the small-excess and total-variation statements hold for fixed integer \(d\ge3\) as \(\varepsilon\downarrow0\), with no dimension-uniform claim. All exact formulas use ordinary Euclidean projection lengths, not support-width range alone. Conditional laws concern ordered gaps and the label permutation, not arbitrary independent point spacings.

## Proof

**1. Projection model and sorted chambers.** Identify the regular simplex with the vertices \((e_i-\mathbf1/m)/\sqrt2\) in \(H=\{u\in\mathbb R^m:\sum_i u_i=0\}\), where \(m=d+1\). A unit viewing direction \(u\in H\) yields projected coordinates \(z_i=u_i/\sqrt2\). Thus the unordered vector \(z\) is Haar-uniform on the sphere of radius \(R=1/\sqrt2\) in \(H\). Permutation symmetry gives \(m!\) equal-measure strict ordering chambers.

In an increasing-order chamber let \(g_j=z_{(j+1)}-z_{(j)}>0\). Because \(\sum_i z_i=0\), the vector \(z\) is a unique linear function of \(g\):
\[
z_{(i)}=\sum_{k<i}g_k-\frac1m\sum_{k=1}^{d}(m-k)g_k.
\]
Its Euclidean Gram matrix is \(M=(M_{ij})\) in the finding. More explicitly, \(M\) is the inverse of the tridiagonal matrix with diagonal entries two and adjacent entries minus one. Consequently \(\det M=1/m\) and the Euclidean Jacobian from \(dg_1\cdots dg_d\) to induced Lebesgue measure on \(H\) is \(m^{-1/2}\). The sphere constraint is
\[
g^{\mathsf T}Mg=\frac12.
\]
All entries of \(M\) are strictly positive. Its row sums are \((M\mathbf1)_j=a_j=j(m-j)/2\), so \(\mathbf1^{\mathsf T}M\mathbf1=A_d\).

**2. Maximum and its complete equality cases.** With \(t=\min_jg_j\) one has \(g\ge t\mathbf1\). Entrywise positivity gives \(g^{\mathsf T}Mg\ge t^2A_d\), with equality only if \(g=t\mathbf1\). Hence \(t\le1/\sqrt{2A_d}=g_d\), and equality requires an arithmetic progression of projected coordinates. Each strict ordering of the labelled vertices gives precisely one unit viewing direction, proving the exact maximizing count.

**3. Sphere coarea and exact finite-threshold integral.** The radius-\(R\) surface area of the sphere in \(H\) is \(\sigma_{d-1}R^{d-1}\), and for a measurable set in \(H\), surface area on this sphere is \(2R\int_H\mathbf1_{\mathrm{set}}\delta(\|z\|^2-R^2)\,dz\). Restrict to a gap chamber and use the constant Jacobian from Step 1, then sum over all \(m!\) chambers. Substituting \(g=t\mathbf1+h\) gives
\[
A_dt^2+2t\sum_{j=1}^{d}a_jh_j+h^{\mathsf T}Mh=\frac12.
\]
Define \(s=\sum a_jh_j>0\) and \(q_j=a_jh_j/s\). The cone-volume change of variables is
\[
dh_1\cdots dh_d=\frac{s^{d-1}}{\prod_{j=1}^{d}a_j}\,ds\,dq_1\cdots dq_{d-1},
\qquad\prod_{j=1}^da_j=\frac{(d!)^2}{2^d}.
\]
The radius equation becomes \(2ts+s^2H(q)=B_t\). Its unique positive root is the displayed \(s_t(q)\), and the derivative with respect to \(s\) is \(2[t+sH(q)]\). Integrating the delta mass in \(s\), inserting \(R=1/\sqrt2\), the \(m!\) chambers, and \(\det M=1/m\), yields precisely the stated finite-threshold formula. When \(t=0\), the chamber decomposition covers the sphere up to null sets, giving one; when \(t\ge g_d\), the quadratic constraint prevents the event.

**4. Sharp small-excess tail.** Put \(t=g_d-\varepsilon\). Since \(B_t=A_d(g_d^2-t^2)=2A_dg_d\varepsilon+O_d(\varepsilon^2)\), and \(H(q)\) is positive, bounded, and continuous on the closed compact simplex, the root formula gives uniformly in \(q\):
\[
s_t(q)=A_d\varepsilon+O_d(\varepsilon^2),\qquad
[t+s_t(q)H(q)]^{-1}=g_d^{-1}+O_d(\varepsilon).
\]
The coordinate volume of \(\Delta_{d-1}\) is \(1/(d-1)!\). Integrating the uniform expansion in the exact formula gives
\[
\Pr(G>g_d-\varepsilon)=
\frac{\sqrt{d+1}\,2^{(3d-2)/2}A_d^{d-1}}{\sigma_{d-1}d!(d-1)!g_d}
\varepsilon^{d-1}+O_d(\varepsilon^d).
\]
Using \(g_d^{-1}=\sqrt{2A_d}\) reduces the coefficient to \(C_d\).

**5. Conditional law.** The same changes of variables show that the conditional density of \(q\) on \(\Delta_{d-1}\) is proportional to \(s_t(q)^{d-1}/[t+s_t(q)H(q)]\). By Step 4, its normalized density converges uniformly to the constant \((d-1)!\) relative to standard simplex-coordinate measure; this implies convergence in total variation to \(\operatorname{Dirichlet}(1,\ldots,1)\). Each labelled ordering chamber is congruent under coordinate permutation, and the gap-coordinate density is identical in each; the ordering permutation is therefore exactly uniform and independent of the normalized slack vector for every \(0\le t<g_d\).

## Verification

The standalone Python-standard-library script `verify.py` checks the exact inverse-Cartan Gram identity and its row sums for \(3\le d\le9\), the coefficient simplification in dimension three, and independent two-dimensional numerical quadrature of the exact survival integral for the tetrahedron. In particular it reproduces \(\Pr(G>0)=1\) and tests the finite-threshold survival probabilities at three positive values near the maximum. Its output is `ALL_CHECKS_PASSED`. These are finite arithmetic and numerical checks; the general-dimensional formula and the total-variation limit follow analytically from the preceding proof, not from the numerical tests.

## Relationship to prior work

Kabluchko, Litvak and Zaporozhets (2015) derive projection-width moments for regular simplices using centered Gaussian extrema. Their width variable is the **largest minus smallest** projected vertex coordinate, whereas the present margin is the **smallest consecutive** projected coordinate difference. Gaussian-range moments neither fix the minimum adjacent spacing nor imply its maximal-orientation point set or conditional gap law. Finch's 2011 tetrahedral paper similarly treats the support width, not the resolution of all four projected vertices. General work on the minimum spacing of independent random sample points concerns a different probabilistic model: the present gaps are jointly constrained by the Euclidean sphere norm and permutational symmetry, not independent spacings.

For further comparison, published analyses of near-minimum simplex projection width and invariant affine-hyperplane sections concern, respectively, the sum of ordered gaps (projection range) and the number of edges crossed by a random offset. Neither contains a stated or derived formula for the minimum adjacent projected-vertex gap. The equality case is an arithmetic progression rather than a two-level width minimizer. The finite-threshold integral, sharp endpoint coefficient, and conditional Dirichlet limit are distinct implications not obtained by substituting a parameter in those prior results.

## Limitations

The theorem assumes a perfectly regular simplex and a Haar-uniform **direction**. It does not cover arbitrary vertex sets, random affine offsets, independently sampled projected positions, or simultaneous dimension and threshold limits. The conditional Dirichlet law concerns weighted excess gaps above a common near-optimal threshold; unweighted gaps do not have the same stated normalization. Independent mathematical review has not been performed, and complete historical priority cannot be guaranteed from a finite literature and prior-record comparison.

## References

1. Z. Kabluchko, A. E. Litvak and D. Zaporozhets, *Mean width of regular polytopes and expected maxima of correlated Gaussian variables*, arXiv:1511.08479v1, first posted November 26, 2015, https://arxiv.org/abs/1511.08479; primary classification 52A23.
2. S. R. Finch, *Width Distributions for Convex Regular Polyhedra*, arXiv:1110.0671v1, first posted October 4, 2011, https://arxiv.org/abs/1110.0671.
3. *Gaussian spacing laws and rare balanced cuts of regular simplices*, published mathematical finding, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-gaussian-spacing-laws-and-rare-balanced-cuts-of-regular-simplice--3cba4b68834c.
4. *A tangent-polytope limit for near-minimum widths of regular simplices*, published mathematical finding, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-a-tangent-polytope-limit-for-near-minimum-widths-of-regular-simp--5c40f067382e.
5. *Two sharp spherical-cap transitions in regular-simplex projection widths*, published mathematical finding, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-two-sharp-spherical-cap-transitions-in-regular-simplex-projectio--10b5ea726908.
