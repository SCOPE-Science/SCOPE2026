# Sharp local volume stability of the ten-vertex inscribed four-polytope

## Finding

Let \(\theta=2\pi/5\), and consider the ordered vertices
\[
a_i=(\cos i\theta,\sin i\theta,0,0),\qquad
b_j=(0,0,\cos j\theta,\sin j\theta),\quad i,j\in\mathbb Z/5\mathbb Z.
\]
Write \(p_*=(a_0,\ldots,a_4,b_0,\ldots,b_4)\), \(V_*=25(10+2\sqrt5)/384\), and \(\mathcal M=O(4)\cdot p_*\). For \(p=(p_1,\ldots,p_{10})\in(\mathbb S^3)^{10}\), let
\[
D(p)=\min_{R\in O(4)}\sum_{i=0}^4\bigl(\|p_{i+1}-Ra_i\|^2+\|p_{i+6}-Rb_i\|^2\bigr).
\]
For every \(\varepsilon>0\) there exists \(\delta>0\) such that
\[
0<D(p)<\delta\quad\Longrightarrow\quad
V_*-\operatorname{vol}_4\operatorname{conv}(p_1,\ldots,p_{10})
\geq\left(\frac{25}{192}-\varepsilon\right)D(p).
\]
The constant \(25/192\) is asymptotically optimal: there are configurations with \(D(p)\downarrow0\) for which the deficit-to-\(D\) ratio converges to \(25/192\).

More precisely, let \(\mathcal Q\) be the coefficient of \(t^2\) in the volume loss along the normalized straight-line sphere chart at \(p_*\). Relative to the squared Euclidean norm of its ten tangent velocities, the complete real spectrum of this quadratic form is
\[
\begin{array}{c|ccccc}
\text{eigenvalue}&0&\frac{25}{192}&\frac{5(5+\sqrt5)}{192}&
\frac{25(3+\sqrt5)}{384}&\frac{5(5+\sqrt5)}{96}\\
\text{multiplicity}&6&4&12&4&4.
\end{array}
\]
The six-dimensional kernel is exactly tangent to the orthogonal orbit \(\mathcal M\). Here \(\mathcal Q\) is the *half-Hessian*: the usual Hessian has twice these eigenvalues.

## Assumptions and scope

All ten labelled points lie on the Euclidean unit three-sphere, and \(p\) is close to the displayed ordered maximizing configuration up to a common orthogonal transformation. The nearest-orbit squared distance \(D\), rather than a Hausdorff or unlabeled distance, is the normalization used throughout. The theorem is local; global maximization and classification of equality were established earlier in the cited paper of Medgyes. No claim is made concerning a sharp uniform constant for configurations far from the optimizer.

## Proof

**1. A smooth local determinant formula.** The displayed polytope is the free sum of the two regular pentagons in orthogonal two-planes. Its 25 facets are the tetrahedra with vertices \((a_i,a_{i+1},b_j,b_{j+1})\). Each unlisted vertex lies strictly inside the corresponding supporting halfspace, so the same labelled facets and their orientations persist in a neighborhood. In that neighborhood,
\[
24\operatorname{vol}_4(P(p))=
\sum_{i,j\in\mathbb Z/5\mathbb Z}
\det(p_{i+1},p_{i+2},p_{j+6},p_{(j+1)\bmod5+6}),
\]
with indices in the first block interpreted modulo five. In particular \(\operatorname{vol}_4(P(p_*))=25\sin^2\theta/24=V_*\). This is the local form of the join-cycle determinant identity in the cited literature.

**2. Tangent coordinates.** Let \(E=\mathbb R^2\oplus0\) and \(F=0\oplus\mathbb R^2\). Write \(J\) for a positive quarter-turn in either plane and use \(e_i=a_i\in E\), \(f_j=b_j\in F\). Every tangent velocity has a unique decomposition
\[
\dot a_i=\alpha_iJe_i+u_i,\quad u_i\in F;
\qquad\dot b_j=\beta_jJf_j+v_j,\quad v_j\in E.
\]
Choose the unit-sphere chart \(a_i(t)=(a_i+t\dot a_i)/\sqrt{1+t^2\|\dot a_i\|^2}\), and likewise for \(b_j(t)\). Define linear maps \(U:E\to F\) and \(W:F\to E\) by
\[
U=\frac25\sum_i u_i e_i^{\mathsf T},\qquad
W=\frac25\sum_j v_j f_j^{\mathsf T},
\]
where vectors are written in orthonormal bases of their respective two-planes. Set \(u_i^\perp=u_i-Ue_i\), \(v_j^\perp=v_j-Wf_j\). The identities \(\sum_i e_ie_i^{\mathsf T}=\sum_j f_jf_j^{\mathsf T}=\frac52 I\) imply that these residuals are orthogonal to all first-harmonic in-plane coefficients and that
\[
\sum_i\|u_i\|^2=\frac52\|U\|_{F}^2+\sum_i\|u_i^\perp\|^2,
\qquad
\sum_j\|v_j\|^2=\frac52\|W\|_{F}^2+\sum_j\|v_j^\perp\|^2.
\]

**3. Second variation.** Let \(A(t)=\sum_i a_i(t)\wedge a_{i+1}(t)\) and \(B(t)=\sum_j b_j(t)\wedge b_{j+1}(t)\). The determinant sum equals \(A(t)\wedge B(t)\) in oriented four-volume coordinates. Put \(s=\sin\theta\). The component of \(A(t)\) along \(e_1\wedge e_2\) has the expansion
\[
5s-st^2\left(\frac12\sum_i(\alpha_i-\alpha_{i+1})^2+\sum_i\|u_i\|^2\right)+O(t^3),
\]
and the analogous statement holds for \(B(t)\) along \(e_3\wedge e_4\). The in-plane first derivatives telescope. Directly expanding their remaining mixed two-form components gives the cross coefficient \(-25s^2\operatorname{tr}(UW)\) in \(A(t)\wedge B(t)\). Hence, writing \(V_*-\operatorname{vol}_4(P(p(t)))=\mathcal Q(\dot p)t^2+O(t^3)\),
\[
\begin{aligned}
\mathcal Q={5s^2\over24}\left[\frac12\sum_i(\alpha_i-\alpha_{i+1})^2+
\frac12\sum_j(\beta_j-\beta_{j+1})^2+
\sum_i\|u_i\|^2+\sum_j\|v_j\|^2\right]
+{25s^2\over24}\operatorname{tr}(UW).
\end{aligned}
\]
The cross term is a matrix trace, not a Frobenius norm. In particular the off-plane contribution completes the square as
\[
\mathcal Q_{\rm off}={25s^2\over48}\|U+W^{\mathsf T}\|_F^2+
{5s^2\over24}\left(\sum_i\|u_i^\perp\|^2+
\sum_j\|v_j^\perp\|^2\right).
\]

**4. Complete spectrum and kernel.** The angular first-derivative terms are two independent five-cycle Laplacians. Their eigenvalues are \(0\) once and \((5-\sqrt5)/2\), \((5+\sqrt5)/2\) twice each. The angular quadratic-form eigenvalues are therefore \(0\) (twice), \(25/192\) (four times) and \(25(3+\sqrt5)/384\) (four times), using \(s^2=(5+\sqrt5)/8\). For off-plane velocities, \(U=-W^{\mathsf T}\) describes four zero directions of mixing the two orthogonal planes; \(U=W^{\mathsf T}\) describes four eigenvectors of eigenvalue \(5s^2/12=5(5+\sqrt5)/96\). The residual orthogonal space has dimension 12 and eigenvalue \(5s^2/24=5(5+\sqrt5)/192\). These subspaces are mutually orthogonal for the full tangent velocity norm, and their dimensions sum to 30. The six zero directions are precisely the dimension-six infinitesimal action of \(O(4)\). The least strictly positive eigenvalue is \(25/192\).

**5. Local stability and sharpness.** The orbit \(\mathcal M\) is a compact smooth six-dimensional embedded submanifold of the 30-dimensional product of spheres, since a continuous orthogonal map fixing all ten vertices fixes four spanning directions and must be the identity. In a uniform tubular neighborhood, choose a nearest orbit point and its normal tangent displacement \(\xi\). Smoothness of the volume and of normal coordinates gives uniformly
\[
V_*-\operatorname{vol}_4(P(p))=\mathcal Q(\xi)+o(\|\xi\|^2),
\qquad D(p)=\|\xi\|^2+o(\|\xi\|^2).
\]
Positivity of \(\mathcal Q\) on the normal space yields the asserted inequality for every \(\varepsilon>0\). For sharpness, take \(\alpha_i=\cos(i\theta)\), \(\beta_j=0\), \(u_i=v_j=0\) in the normalized chart. This is a nonzero normal vector in the least-eigenvalue subspace, and its ratio tends to \(25/192\).

## Verification

The accompanying executable `verify_pentagon_hessian.py` independently forms all 25 oriented facet determinants, builds the 30-by-30 constrained half-Hessian in unit-sphere tangent charts, computes its numerical spectrum, verifies the four distinct positive bands against exact symbolic expressions, and checks 20 random symmetric finite differences. On execution it passed: maximum numerical spectral deviation below \(3.1\times10^{-16}\), maximum normalized finite-difference deviation below \(3.5\times10^{-8}\), and sharp-harmonic quotient \(25/192\) to numerical precision. The infinite-dimensional-neighborhood assertion and the eigenvalue multiplicities are proved analytically above; floating-point checks are supporting evidence only.

To reproduce from this package, save the embedded script as `verify_pentagon_hessian.py` and execute `python verify_pentagon_hessian.py` with Python 3, NumPy and SymPy. No external data files are needed.

## Relationship to prior work

Medgyes (2026, arXiv:2611.14674v1), Theorem 4.5, determines the **global** maximum \(V_*\), its unique orthogonal orbit, and the 25-facet join construction. Medgyes (2026, arXiv:2611.10078v1), Sections 3–5, supplies the signed-volume exterior-square identity and Fourier area-vector inequalities that prove qualitative optimality on join-cycle types. The present calculation does not claim those results anew. It isolates the complete **local constrained volume Hessian**, identifies the rotational kernel, and obtains a sharp numerical quadratic deficit constant for the ten-point problem. These explicit local stability and spectral statements were not located in the primary texts inspected; priority against any uninspected equivalent treatment remains provisional.

## Limitations

The stability statement is local for *labelled* ten-tuples on \(\mathbb S^3\), with the sum-of-squared-vertex-displacements metric modulo common orthogonal motions. Its sharpness does not transfer without renormalization to Hausdorff distance, arbitrary point labels, other vertex counts, or a global linear deficit bound. The numerical checker is not a computer-assisted proof of the smooth local inequality. The global equality theorem is prior work. No independent mathematical audit has been performed.

## References

1. Csaba Medgyes, *The inscribed 4-polytope of maximal volume with ten vertices*, arXiv:2611.14674v1 (first posted 2026-11-10), https://arxiv.org/html/2611.14674v1 .
2. Csaba Medgyes, *The inscribed 4-polytope of maximal volume with nine vertices*, arXiv:2611.10078v1 (first posted 2026-11-06), https://arxiv.org/html/2611.10078v1 .
