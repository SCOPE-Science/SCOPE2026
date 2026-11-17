# The full volume-Hessian spectrum and sharp local stability of the nine-vertex spherical four-polytope

## Finding

Let \(u_i=(\cos(2\pi i/4),\sin(2\pi i/4))\) for \(i\in\mathbb Z/4\mathbb Z\), and \(v_j=(\cos(2\pi j/5),\sin(2\pi j/5))\) for \(j\in\mathbb Z/5\mathbb Z\). In \(\mathbb R^4=\mathbb R^2\oplus\mathbb R^2\), let \(p_i^*=(u_i,0)\), \(p_{4+j}^*=(0,v_j)\), and \(P_*=\operatorname{conv}\{p_0^*,\ldots,p_8^*\}\). Put \(b=\sin(2\pi/5)\), and \(V_*=5b/6=5\sqrt{10+2\sqrt5}/24\).

For labelled configurations \(p=(p_0,\ldots,p_8)\in(S^3)^9\) near \(p^*\), the volume deficit \(\Delta(p)=V_*-\operatorname{vol}_4(\operatorname{conv}\{p_0,\ldots,p_8\})\) has a positive-semidefinite quadratic Taylor term \(\mathcal Q\) on the full 27-dimensional vertex tangent space. Its complete eigenvalue spectrum, relative to the ordinary squared Euclidean norm of tangent vertex displacements, is

\[
\begin{array}{c|c}
\text{quadratic coefficient}&\text{multiplicity}\\\hline
0&6\\
\frac{b(5-\sqrt5)}{24}&2\\
\frac b6&6\\
\frac{5b}{24}&6\\
\frac{b(5+\sqrt5)}{24}&2\\
\frac{3b}{8}&4\\
\frac{5b}{12}&1
\end{array}
\]

Its kernel consists **exactly** of the six infinitesimal rigid rotations. Consequently, writing \(d(p,\mathcal O)^2=\min_{U\in O(4)}\sum_{i=0}^8\|p_i-Up_i^*\|^2\) for the squared distance to the labelled orthogonal orbit, the **sharp local quadratic coefficient** is
\[
\boxed{\mu=\frac{\sin(2\pi/5)(5-\sqrt5)}{24}=0.109527315024819\ldots}. 
\]
Precisely, for every \(\eta>0\) there is a neighbourhood of the orbit where \(\Delta(p)\ge(\mu-\eta)d(p,\mathcal O)^2\). The constant \(\mu\) cannot be increased in this asymptotic assertion; equality in the limiting ratio is approached along first Fourier-harmonic deformations of the pentagon's angles, keeping the square fixed.

## Assumptions and scope

All nine vertices remain on the unit three-sphere and keep their labels. The assertion is local in the usual topology of \((S^3)^9\); it places **no symmetry restriction** on perturbations. The convex hull is four-dimensional and retains its twenty simplicial facets for all sufficiently small perturbations of \(p^*\). The source theorem that \(P_*\) is the unique global maximiser of the ordinary four-volume is prior work [1]. The present finding concerns the previously unquantified complete constrained second-variation spectrum and its sharp local stability modulus; it neither asserts a global quadratic deficit nor re-proves the global classification.

## Proof

**1. Local volume identity.** The facets of \(P_*\) are exactly the twenty tetrahedra with vertex sets \(\{i,i+1,4+j,4+j+1\}\), where \(i\in\mathbb Z/4\mathbb Z\), \(j\in\mathbb Z/5\mathbb Z\). Their support inequalities are strict at every remaining vertex, so the facet structure persists locally. For any vectors \(w_0,\ldots,w_{n-1}\in\mathbb R^4\), write \(\mathcal A(w)=\sum_i w_i\wedge w_{i+1}\) (cyclic indices). In a neighbourhood of \(p^*\), the oriented facet determinant formula, or equivalently the Hodge-star pairing established in [1], gives
\[
24\operatorname{vol}_4(P(p))=\langle\mathcal A(p_0,\ldots,p_3),*\mathcal A(p_4,\ldots,p_8)\rangle.
\]
At the reference configuration the two area bivectors are \(4e_{12}\) and \(5b\,e_{34}\); hence \(24V_*=20b\).

**2. Normalised tangent coordinates.** Fix the quarter-turn \(J(x,y)=(-y,x)\) and let \(\alpha\in\mathbb R^4\), \(\beta\in\mathbb R^5\), \(X_i\in\mathbb R^2\) for \(0\le i<4\), \(Y_j\in\mathbb R^2\) for \(0\le j<5\). Use the exact spherical chart
\[
\begin{split}
p_i&=\bigl(\sqrt{1-\|X_i\|^2}(\cos(\pi i/2+\alpha_i),\sin(\pi i/2+\alpha_i)),X_i\bigr),\\
p_{4+j}&=\bigl(Y_j,\sqrt{1-\|Y_j\|^2}(\cos(2\pi j/5+\beta_j),\sin(2\pi j/5+\beta_j))\bigr).
\end{split}
\]
The tangent norm is exactly \(\sum_i\alpha_i^2+\sum_j\beta_j^2+\sum_i\|X_i\|^2+\sum_j\|Y_j\|^2\) at zero. All remainders in what follows are \(O(\|z\|^3)\), uniformly for small \(z=(\alpha,\beta,X,Y)\).

**3. Bivector expansion.** Set \(a=\sin(2\pi/4)=1\), \(b=\sin(2\pi/5)\), \(m=4\), \(\ell=5\). The pure first-plane coefficient of the square's area bivector is
\[
ma-a\sum_i\|X_i\|^2-\frac a2\sum_i(\alpha_{i+1}-\alpha_i)^2+O(\|z\|^3).
\]
The pure second-plane coefficient of the pentagon's area bivector is
\[
\ell b-b\sum_j\|Y_j\|^2-\frac b2\sum_j(\beta_{j+1}-\beta_j)^2+O(\|z\|^3).
\]
The first-order mixed bivectors are respectively \(-2a\sum_i(Ju_i)\wedge X_i\) and \(+2b\sum_jY_j\wedge(Jv_j)\), with each embedded in its designated orthogonal plane. Using \(\det(x_1,x_2,y_1,y_2)\) and the Hodge-star signs gives their pairing
\[
-4ab\sum_{i,j}(u_i\cdot Y_j)(v_j\cdot X_i).
\]
These identities yield the quadratic volume-deficit form
\[
\mathcal Q=\frac{ab}{24}\left[\ell\sum_i\|X_i\|^2+m\sum_j\|Y_j\|^2+4\sum_{i,j}(u_i\cdot Y_j)(v_j\cdot X_i)+\frac\ell2\sum_i(\alpha_{i+1}-\alpha_i)^2+\frac m2\sum_j(\beta_{j+1}-\beta_j)^2\right].\tag{1}
\]
The sign of the mixed term can be checked intrinsically: an infinitesimal rotation interchanging the two coordinate planes must give zero volume deficit.

**4. Exact sum-of-squares diagonalisation.** The tight-frame identities are \(\sum_i u_i u_i^{\mathsf T}=\frac m2 I_2\) and \(\sum_j v_jv_j^{\mathsf T}=\frac\ell2 I_2\). Decompose uniquely
\[
X_i=Ku_i+R_i,\quad \sum_iR_i u_i^{\mathsf T}=0,\qquad
Y_j=Lv_j+S_j,\quad \sum_jS_jv_j^{\mathsf T}=0,
\]
where \(K\) maps the first coordinate plane to the second and \(L\) maps the second plane to the first. Substitution in (1) gives the **exact quadratic identity**
\[
\boxed{\mathcal Q=\frac{ab}{24}\left[\frac{m\ell}{2}\|K+L^{\mathsf T}\|_F^2+\ell\sum_i\|R_i\|^2+m\sum_j\|S_j\|^2+\frac\ell2\sum_i(\alpha_{i+1}-\alpha_i)^2+\frac m2\sum_j(\beta_{j+1}-\beta_j)^2\right].}\tag{2}
\]
The tangent metric becomes
\[
\|z\|^2=\sum_i\alpha_i^2+\sum_j\beta_j^2+\frac m2\|K\|_F^2+\frac\ell2\|L\|_F^2+\sum_i\|R_i\|^2+\sum_j\|S_j\|^2.
\]
In each of the four matrix entries the \(K,L\) block has one zero mode \(L=-K^{\mathsf T}\) and one positive mode with quadratic coefficient \((m+\ell)ab/24=3b/8\). The residual \(R\)-space has dimension \(2m-4=4\) with coefficient \(\ell ab/24=5b/24\), and the residual \(S\)-space has dimension \(2\ell-4=6\) with coefficient \(mab/24=b/6\).

For the angle vectors, the cycle Laplacian's eigenvalues are \(2-2\cos(2\pi k/n)\). From (2) the nonzero square-angle coefficients are \(5b/24\) twice and \(5b/12\) once; the pentagon-angle coefficients are \(b(5-\sqrt5)/24\) twice and \(b(5+\sqrt5)/24\) twice. Each cyclic constant angle mode has coefficient zero. The six zero modes are exactly the two planar rotations plus four cross-plane rotations. This lists all \(27\) eigenvalues and proves the spectrum in Finding.

**5. Sharp local metric inequality.** Since the orthogonal group acts isometrically and its orbit through \(p^*\) is a smooth six-dimensional compact submanifold, the squared distance to the orbit agrees to leading order with the squared norm of the orthogonal projection onto the complement of its tangent space. By the preceding diagonalisation \(\mathcal Q\ge\mu\|z_{\perp}\|^2\), with \(\mu=b(5-\sqrt5)/24\), and the remainder is \(O(\|z\|^3)\) in a slice transverse to the orbit. This proves the asserted local inequality with arbitrary loss \(\eta>0\). Choose \(\beta_j=t\cos(2\pi j/5)\), and set every other perturbation to zero; this is a nonrotational pentagon first-mode direction and achieves \(\Delta/d^2\to\mu\). Therefore the coefficient is sharp.

## Verification

A standalone standard-library Python verifier (`verify.py`) reconstructs the twenty-facet signed volume from independent bivector coordinates, evaluates the quadratic identity (1) and its sum-of-squares version (2), and tests the second-order finite-difference remainder along deterministic tangent directions and rotation modes. Separately, an independent SciPy convex-hull computation for twenty random tangent directions at three small scales verified agreement of true hull volume and the analytic quadratic expansion, and a numerical constrained Hessian reconstructed from 27 independent tangent coordinates matched the seven predicted spectral levels to within \(5.4\times10^{-9}\) in the tested finite-difference discretisation. These computations are finite consistency checks; the proof rests on the analytical expansions and diagonalisation.

## Relationship to prior work

Medgyes [1] proves the unique global maximum-volume nine-vertex inscribed four-polytope and supplies the signed-volume factorisation and sharp polygon area-vector bound. It does not advertise a full constrained Hessian spectrum or a sharp local orbit-distance coefficient; the claim here is that complete second-order determination, not the maximum-volume theorem or the Hodge factorisation. Horváth and Lángi [2] studied maximisers at other small vertex counts. The related seven-vertex sharp-stability result addresses a different extremiser and its 21-dimensional vertex tangent space, so it does not imply the present 27-dimensional spectrum. A separate exact simplex-volume spectrum for this nine-vertex configuration concerns five-point sub-simplex volumes, not the second variation of the whole convex hull.

## Limitations

The stability inequality is local, not a global quantitative inequality. The precise Hessian is for labelled spherical vertices and Euclidean vertex-displacement distance modulo simultaneous orthogonal transformations; changing the metric changes coefficients. No independent external audit has been performed. Historical priority of a spectral computation under another formulation remains to be checked against all earlier literature; the accessible portion of [1] covers its introduction, preliminaries, and the start of its Hodge-star factorisation, while later full text was temporarily inaccessible. The source's theorem and methods are acknowledged independently of any priority assessment of this calculation.

## References

[1] Csaba Medgyes, *The inscribed 4-polytope of maximal volume with nine vertices*, arXiv:2611.10078v1 (first released 2026-11-06), https://arxiv.org/abs/2611.10078.

[2] Ákos G. Horváth and Zsolt Lángi, *Maximum volume polytopes inscribed in the unit sphere*, arXiv:1402.6496 (first released 2014-02-26), https://arxiv.org/abs/1402.6496.

[3] Csaba Medgyes, *Inscribed 4-polytopes of maximal volume with seven and eight vertices*, arXiv:2610.26886v1 (2026-10-12), https://arxiv.org/abs/2610.26886.
