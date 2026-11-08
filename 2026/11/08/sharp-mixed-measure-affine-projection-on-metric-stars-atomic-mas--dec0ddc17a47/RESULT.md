# Sharp mixed-measure affine projection on metric stars: atomic-mass thresholds and vanishing-arm instability

## Finding

Let a finite metric star have \(d\ge2\) edges with positive lengths \(\ell_i\), positive constant arclength densities \(\rho_i\), and an additional positive mass \(w\) at its common vertex. Let \(P\) be orthogonal projection in real \(L^2(\mu)\) onto the continuous functions affine on each edge. Define the edge masses and their total by
\[
a_i=\rho_i\ell_i,\qquad A=\sum_{i=1}^d a_i,\qquad r=\frac{\min_i a_i}{A},\qquad z=1+\frac{4w}{A}.
\]
Then \(z>1\), \(0<r\le1/2\), and the exact endpoint norm is
\[
\boxed{\|P\|_{L^\infty(\mu)\to L^\infty(\mu)}=2+\frac{1}{3z}-\frac{4r}{3(z+r)}.}
\]
The maximizing evaluation locations are **precisely the outer endpoints of edges of minimum arclength mass**. The central vertex and all open-edge points have strictly smaller evaluation norm.

The exact threshold for amplification beyond two is
\[
\|P\|>2\quad\Longleftrightarrow\quad z(1-4r)+r>0.
\]
Consequently, if \(r\le1/4\) the norm exceeds two for every \(w>0\); if \(1/4<r<1/3\), it exceeds two precisely when
\[
0<\frac{w}{A}<\frac{1-3r}{4(4r-1)},
\]
with equality to two at the endpoint; and if \(r\ge1/3\), it is strictly below two for all positive \(w\). In the intermediate regime the inequality reverses after the stated threshold.

The effect of a vanishing-mass **new** arm is discontinuous. Fix any original star and \(w>0\), and attach an additional arm with positive mass \(\varepsilon\). Holding all original edge masses fixed, as \(\varepsilon\downarrow0\) the norm of the enlarged star tends to
\[
2+\frac{1}{3z},
\]
strictly exceeding the norm of the original star by exactly \(4r/[3(z+r)]\). This is an operator-norm phenomenon involving an additional \(L^\infty\) direction, not a claim of strong convergence on a fixed domain.

## Assumptions and scope

The metric star is the quotient of \(d\) intervals \([0,\ell_i]\) with all left endpoints identified as \(o\). The measure on an edge is \(\rho_i\,ds\) and \(\mu(\{o\})=w\), where \(\ell_i,\rho_i,w>0\). There are no other atoms. Each class in \(L^2(\mu)\) has a well-defined value at the atom, while its edge representatives are defined almost everywhere; projection values are continuous piecewise affine functions. The norm \(\|P\|_{\infty\to\infty}\) is the essential supremum relative to this mixed measure, equal to the maximum of the continuous projected output over the star. Real functions are used. The number of edges \(d\) is any finite integer at least two; equal or unequal lengths/densities are allowed.

## Proof

Use the nodal basis \(\phi_0,\phi_1,\ldots,\phi_d\): on edge \(i\) at normalized coordinate \(t=s/\ell_i\), \(\phi_0=1-t\), \(\phi_i=t\), while all other leaf functions vanish. The Gram matrix \(G_{jk}=\int\phi_j\phi_k\,d\mu\) has
\[
G_{00}=w+A/3,\qquad G_{0i}=a_i/6,\qquad G_{ii}=a_i/3,\qquad G_{ij}=0\;(i\ne j,\ i,j\ge1).
\]
Set \(h=w+A/4>0\). Its leaf-block Schur complement is exactly \(h\), so direct block inversion gives
\[
(G^{-1})_{00}=h^{-1},\qquad (G^{-1})_{0i}=-\frac{1}{2h},\qquad (G^{-1})_{ij}=\frac{3\mathbf1_{i=j}}{a_i}+\frac{1}{4h}.
\]
For a vertex \(v\), the projected evaluation functional is integration against the signed kernel \(K_v(y)=\sum_{j,k}\phi_j(v)(G^{-1})_{jk}\phi_k(y)\), and its exact \(L^\infty\) norm is \(\int|K_v|\,d\mu\). Equality is realized by the measurable sign of \(K_v\).

At the central vertex, the atom contributes \(w/h\). Each edge has kernel \((1-3t/2)/h\). Integration of its absolute value over \([0,1]\) gives \(5/12\), hence
\[
R_o=\frac{w+5A/12}{h}=1+\frac{2}{3z}.
\]
At the outer endpoint of edge \(i\), the kernel is \(-1/(2h)\) at the atom, and on edge \(j\) it equals
\[
K_i(j,t)=-\frac{1}{2h}+\left(\frac{3\mathbf1_{i=j}}{a_i}+\frac{3}{4h}\right)t.
\]
Split the absolute-value integral at its unique zero on each edge. On edge \(i\), the zero is \(2a_i/[3(4h+a_i)]\), and on any other edge it is \(2/3\). Summing the atom and the resulting triangular integrals simplifies to
\[
R_i=2+\frac{A}{12h}-\frac{4a_i}{3(4h+a_i)}
=2+\frac1{3z}-\frac{4r_i}{3(z+r_i)},\qquad r_i=a_i/A.
\]
Because \(dR_i/dr_i=-4z/[3(z+r_i)^2]<0\), these endpoint norms are largest precisely for edges of minimum mass. Moreover, for \(0<r_i\le1\) and \(z\ge1\),
\[
R_i-R_o=1-\frac1{3z}-\frac{4r_i}{3(z+r_i)}>0.
\]
Indeed the right side is decreasing in \(r_i\) and equals \(0\) at the excluded corner \(r_i=z=1\). At an interior point of an edge the evaluation kernel is a strict convex combination of the two endpoint kernels; by the triangle inequality, its norm is at most the corresponding strict convex combination of endpoint norms, hence strictly smaller than the maximum leaf norm. This also proves there are no other norming points, including the atom.

The sign of the explicit difference from two has numerator \(z(1-4r)+r\) and denominator \(3z(z+r)>0\). Substituting \(z=1+4w/A\) and solving the linear inequality gives the asserted three regimes and the exact transition threshold.

Finally attach a fresh edge of mass \(\varepsilon\). The new total edge mass is \(A+\varepsilon\), the new parameter \(z_\varepsilon=1+4w/(A+\varepsilon)\to z\), and for all sufficiently small \(\varepsilon\) the new minimum edge mass is \(\varepsilon\). Thus \(r_\varepsilon=\varepsilon/(A+\varepsilon)\to0\). Substitution into the exact formula gives the limiting value and the strictly positive difference, completing the proof.

## Verification

A standalone standard-library exact-rational checker, `verify_atom_star_projection.py`, constructs and inverts the Gram matrix independently, integrates absolute affine kernels by their zeros, and compares their norms with the closed formula for 1,440 cases with two to five edges. It separately checks the phase-sign identity and the vanishing-arm jump. The observed successful terminal markers are `INDEPENDENT_EXACT_MASS_MATRIX_AND_KERNEL_NORMS_OK 1440`, `EXACT_PHASE_SIGN_IDENTITY_OK 25`, `EXACT_COLLAPSING_BRANCH_JUMP_IDENTITY_OK 3`, and `ALL_ATOMIC_STAR_LINEAR_SPLINE_CHECKS_OK`. Run from the file's own directory with `python verify_atom_star_projection.py`. The universal theorem follows from the displayed exact algebra and integral computations; finite tests are corroborative only.

## Relationship to prior work

Classical work on \(L^2\) spline projectors establishes interval bounds and stability under different measures or discretizations, not this mixed-measure metric-star endpoint formula. De Boor (1976) studies approximation by interval splines; Grigorieff and Sloan (1998) study discrete orthogonal projections for interval splines; Kayumov (2004) gives mesh-independent estimates for second-order interval \(L\)-splines. The already-derived **atom-free weighted-star formula** \((7+3r)/[3(1+r)]\) is recovered when \(w\downarrow0\) and is not claimed as new. The present theorem applies only to **positive hub mass**, and its additional exact amplification threshold and disappearing-arm jump are the subject of the claim. Boman's (2006) general continuous finite-element projection estimates are relevant context; a comparison with its full text was not completed.

## Limitations

This theorem requires constant positive edge densities, one positive atom exactly at the junction, finite degree, and continuous affine finite elements. The result is not a classification for general trees, interior atoms, variable edge densities, higher-degree elements or arbitrary discrete quadrature. The vanishing-arm statement compares differing function spaces and does not assert failure of strong operator convergence. No general lower bound for all mixed measures or independent validation is claimed. An equivalent exact weighted-star expression under other terminology in unindexed literature remains possible; one relevant paper could be compared only at abstract level.

## References

1. Carl de Boor, *A bound on the \(L^\infty\)-norm of \(L^2\)-approximation by splines in terms of a global mesh ratio*, Mathematics of Computation **30** (1976), 765–771, DOI 10.1090/S0025-5718-1976-0425432-1.
2. R. D. Grigorieff and I. H. Sloan, *Stability of discrete orthogonal projections for continuous splines*, Bulletin of the Australian Mathematical Society **58** (1998), 307–332, DOI 10.1017/S0004972700032263.
3. Alexander Kayumov, *Least-squares approximation by second-order L-splines*, arXiv:math/0408418, public version posted 2004-08-30.
4. Mats Boman, *Estimates for the \(L^2\)-projection onto continuous finite element spaces in a weighted \(L^p\)-norm*, BIT Numerical Mathematics **46** (2006), 249–260, DOI 10.1007/s10543-006-0062-3.
