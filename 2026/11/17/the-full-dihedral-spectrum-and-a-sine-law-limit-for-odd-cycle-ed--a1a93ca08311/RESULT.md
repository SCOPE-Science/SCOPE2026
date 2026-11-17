# The full dihedral spectrum and a sine-law limit for odd-cycle edge simplices

## Finding
For every odd integer \(n=2k+1\ge3\), let \(e_0,\ldots,e_{n-1}\) be the standard orthonormal basis of \(\mathbb R^n\), with indices modulo \(n\), and define the **ordinary (unsigned) edge polytope** of the cycle by
\[
P_n=\operatorname{conv}\{v_i=e_i+e_{i+1}:i\in\mathbb Z/n\mathbb Z\}
\subset H_2:=\{x\in\mathbb R^n:\sum_i x_i=2\}.
\]
Use the Euclidean metric inherited from \(\mathbb R^n\). This is an \((n-1)\)-simplex. Let \(F_i\) be the facet opposite \(v_i\), and let \(\theta_{ij}\in(0,\pi)\) be the **interior**, not exterior, dihedral angle of \(F_i,F_j\). For distinct indices let \(d=\min\{|i-j|,n-|i-j|\}\), where ordinary integer representatives are used. Then
\[
\boxed{\cos\theta_{ij}=\frac{1-(-1)^d n(n-2d)}{n^2-1},
\qquad 1\le d\le k.}
\]
Every distance \(d\) supplies exactly \(n\) unordered facet pairs, and the \(k\) displayed angle values are distinct. The angles at odd \(d\) are strictly acute; those at even \(d\) are strictly obtuse, with no right angles. Their exact respective multiplicities are \(n\lceil k/2\rceil\) and \(n\lfloor k/2\rfloor\). For \(n\ge5\), the least and greatest angles are
\[
\theta_{\min}=\arccos\frac{n-1}{n+1},\qquad
\theta_{\max}=\arccos\frac{1-n(n-4)}{n^2-1}.
\]

If \(\Theta_n\) is the angle at a uniformly selected unordered pair of different facets, then along the odd integers \(n\to\infty\),
\[
\boxed{\Theta_n\ \xrightarrow{\mathrm d}\ \Theta,\qquad
\mathbb P(\Theta\le t)=\frac{1-\cos t}{2}
\quad(0\le t\le\pi).}
\]
Thus the limiting angular density on \((0,\pi)\) is \(\tfrac12\sin t\). More strongly, the cumulative distribution function of \(\cos\Theta_n\) differs uniformly from that of the uniform distribution on \([-1,1]\) by \(O(n^{-1})\).

As supporting metric identities, the simplex has unique incenter and circumcenter \(\mu=(2/n)\mathbf1\), with intrinsic Euclidean radii and volume
\[
r_n=\frac2{\sqrt{n(n^2-1)}},\qquad
R_n=\sqrt{2-\frac4n},\qquad
\operatorname{Vol}_{n-1}(P_n)=\frac{\sqrt n}{(n-1)!}.
\]
The basic lattice-volume property of odd-cycle edge polytopes was known earlier; the angle spectrum and its sine-law limit are the focus here.

## Assumptions and scope
All coordinates and distances are unscaled. For odd \(n\), the nonoriented \(0/1\) edge-incidence matrix has full rank; the even-cycle polytope is not a simplex of the same dimension, and **is not covered** by the theorem. Every \(F_i\cap F_j\) is a genuine codimension-two ridge because \(P_n\) is a simplex. Angular multiplicities count these ridges, not ordered facet pairs. The probability distribution is uniform on ridges, not weighted by their Euclidean ridge volumes. In dimension two (\(n=3\)), the dihedral convention means the interior angle between edges at their intersection.

## Proof
Let \(S\) be the cyclic coordinate-shift matrix sending \(e_i\) to \(e_{i+1}\), and put \(A=I+S\). Its columns are exactly the \(v_i\). Since \(n\) is odd, \((I+S)\sum_{h=0}^{n-1}(-S)^h=2I\); hence
\[
B=A^{-1}=\frac12\sum_{h=0}^{n-1}(-S)^h.
\]
In particular \(\det A=2\), which proves affine independence in \(H_2\). The barycentric-coordinate functions of the simplex are \(y_i(x)=(Bx)_i\), and \(F_i\) is cut out by \(y_i(x)=0\). In the tangent subspace \(H_0=\mathbf1^\perp\), the inward gradient is
\[
g_i=\left(I-\frac{\mathbf1\mathbf1^{\mathsf T}}n\right)B^{\mathsf T}e_i.
\]
Every row of \(B\) has \(n\) entries, each either \(1/2\) or \(-1/2\), and row sum \(1/2\). Therefore
\[
\lVert g_i\rVert^2=\frac{n^2-1}{4n}.
\]
For a circular separation \(d\in\{1,\ldots,k\}\), direct overlap of the two alternating sign rows gives
\[
(BB^{\mathsf T})_{ij}=\frac{(-1)^d(n-2d)}4,
\qquad
\langle g_i,g_j\rangle
=\frac{(-1)^d n(n-2d)-1}{4n}.
\]
The **interior** dihedral cosine is minus the cosine between the inward facet normals, proving the boxed formula. For odd \(d\) the cosine is positive, while for even \(d\) it is negative: since \(n-2d\ge1\), its numerator is at most \(1-n<0\). Within each parity the cosine values vary strictly with \(d\), and opposite parities have different signs. For an odd cycle every circular distance \(d\le k\) occurs at exactly \(n\) unordered facet pairs. This establishes distinctness, signs and multiplicities. The smallest angle comes from \(d=1\), and for \(n\ge5\) the largest from \(d=2\), yielding the extrema.

For the limiting law put \(u_d=1-2d/n\), \(s_d=(-1)^{d+1}\). The exact cosine formula becomes
\[
\cos\theta_d=s_d u_d+\frac{1+s_d u_d}{n^2-1}.
\]
Thus \(\lvert\cos\theta_d-s_du_d\rvert\le2/(n^2-1)\). On the odd and even subsequences separately, the values \(u_d\) form uniform arithmetic meshes of step \(4/n\) in \([0,1]\), with their endpoints within \(O(n^{-1})\) of the endpoints of this interval. The two subsequence sizes differ by at most one. Each conditional empirical distribution therefore differs from uniform \([0,1]\) by \(O(n^{-1})\) in cumulative distribution function; the displayed perturbation changes the bound by at most another \(O(n^{-1})\). Mixing the positive odd and negative even subsequences gives \(\cos\Theta_n\Rightarrow\operatorname{Unif}[-1,1]\), with uniform CDF error \(O(n^{-1})\). Applying the continuous decreasing map \(\arccos\) yields \(\mathbb P(\Theta\le t)=(1-\cos t)/2\), whose derivative is the stated density.

Finally, the centroid of the vertices is \(\mu=(2/n)\mathbf1\), and each barycentric coordinate of \(\mu\) is \(1/n\). Its distance to each facet is \(1/(n\lVert g_i\rVert)\), giving the inradius. Since the barycentric coordinates at any point of \(P_n\) sum to one, their minimum cannot exceed \(1/n\); equality forces all of them to equal \(1/n\), proving uniqueness. Every vertex has squared distance \(2-4/n\) to \(\mu\). For any putative enclosing-ball center \(c\), the mean of its squared distances to the vertices is \(2-4/n+\lVert c-\mu\rVert^2\), proving the unique circumcenter and radius. The height of \(H_2\) from the origin is \(2/\sqrt n\) and \(\lvert\det A\rvert=2\), hence the simplex's intrinsic \((n-1)\)-volume is \(\sqrt n/(n-1)!\).

## Verification
Run the standalone Python 3 file `verify_cycle_angles.py` with no external dependencies. It constructs the exact signed inverse of the \(0/1\) edge-incidence matrix, verifies inverse multiplication and all pairwise projected facet-normal Gram entries for odd orders \(3\) through \(39\) using rational arithmetic, and compares empirical angular-cosine distributions with uniform \([-1,1]\) for odd orders \(101,501,2001,10001\). In a completed execution the checker reported `ODD_CYCLE_EDGE_SIMPLEX_PASS` with \(5130\) direct normal-pair comparisons. These finite experiments are independent corroboration of, not a substitute for, the proof for all odd orders.

## Relationship to prior work
Nagaoka and Tsuchiya's 2017 public preprint defines ordinary graph edge polytopes by the same unsigned \(e_i+e_j\) embedding and establishes dimension and reflexive-lift properties, rather than Euclidean dihedral spectra. Ohsugi and Hibi's 1999 paper already identifies edge polytopes of odd cycles as having normalized lattice volume one; neither this fact nor the general statement that the polytope is a simplex is claimed as new. Numata, Takahashi and Tamaki's 2022 paper treats directed \(e_i-e_j\) edge polytopes, a different Euclidean embedding. Similarly, signed/symmetric edge polytopes, cycle Laplacian-column simplices and standard general formulas for simplex facet-normal Gram matrices do not by themselves state the displayed alternating cosine spectrum or the nonconcentrating sine-law limit. Historical priority is provisional, not certified.

## Limitations
The theorem applies only to odd cycles with the canonical **unsigned** edge-incidence realization and the standard Euclidean metric. Its limit is for uniformly sampled ridges; area-weighted ridge sampling is not addressed. It does not compute all intrinsic volumes or all face-angle measures. Earlier equivalent formulas under other names may exist, and no independent validation has yet been performed.

## References
- T. Nagaoka and A. Tsuchiya, *Reflexive polytopes arising from edge polytopes*, arXiv:1712.06078v1 (first public 2017-12-17), https://arxiv.org/abs/1712.06078 .
- H. Ohsugi and T. Hibi, *Toric Ideals Generated by Quadratic Binomials*, Journal of Algebra 218 (1999), 509–527, https://page.mi.fu-berlin.de/~chaase/lehre/ohsugiHibiQuadratic.pdf .
- Y. Numata, Y. Takahashi and D. Tamaki, *Faces of Directed Edge Polytopes*, arXiv:2203.14521v1 (first public 2022-03-28), https://arxiv.org/abs/2203.14521 .
