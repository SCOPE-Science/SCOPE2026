# An isolated cubic-harmonic sampling resonance on regular-simplex edge midpoints

## Finding
Fix an integer \(m\ge5\) and let
\[
V_m=\{x\in\mathbb R^m:\textstyle\sum_{i=1}^m x_i=0\},\qquad
x_{ij}=\frac{e_i+e_j-(2/m)\mathbf1}{\sqrt{2(m-2)/m}}\quad(1\le i<j\le m).
\]
The \(\binom m2\) nodes lie on the unit sphere in \(V_m\), and are the normalized edge midpoints of a regular \((m-1)\)-simplex. Let \(\mathcal H_3(V_m)\) be the complex-valued degree-three homogeneous harmonic polynomials restricted to this sphere, and let \(E_m:\mathcal H_3(V_m)\to\mathbb C^{\binom m2}\) evaluate at these nodes. Write \(D_m=\dim\mathcal H_3(V_m)=\binom{m+1}{3}-(m-1)\). Equip harmonics with normalized spherical \(L^2\) inner product and \(\mathbb C^{\binom m2}\) with its unnormalized Euclidean inner product.

For any spherical-\(L^2\)-orthonormal basis of \(\mathcal H_3(V_m)\), the normalized evaluation Gram matrix \(K_m=D_m^{-1}E_mE_m^*\) has **exactly three eigenvalue sectors**, with values and multiplicities
\[
\begin{array}{c|c}
\text{eigenvalue}&\text{multiplicity}\\\hline
\displaystyle\lambda_0=\frac{m(m-4)^2(m+1)}{4(m-2)^3}&1\\[4pt]
\displaystyle\lambda_1=\frac{m^2(m-8)^2(m-3)}{8(m-2)^4}&m-1\\[4pt]
\displaystyle\lambda_2=\frac{3m^2(m-4)(m+1)}{4(m-2)^4}&\frac{m(m-3)}2.
\end{array}
\]
All three sectors are positive for every integer \(m\ge5\) except \(m=8\), where \(\lambda_1=0\). Consequently **every assignment of complex values to the simplex edge-midpoint nodes can be interpolated by one cubic spherical harmonic if and only if \(m\ne8\)**. At \(m=8\), evaluation has rank \(21\), not \(28\), and all seven independent relations are
\[
\sum_{j\ne i}h(x_{\min(i,j),\max(i,j)})
\ \text{is independent of}\ i\in\{1,\dots,8\}.
\]
At this unique singular parameter the remaining Gram spectrum is flat:
\[
K_8=\tfrac43P,\qquad P^2=P=P^*,\quad\operatorname{rank}P=21.
\]
Thus the cubic evaluation system is tight after quotienting out its seven blind incidence-contrast modes. For any feasible samples \(y=(y_{ij})\) (equal vertex incident sums), an explicit minimal-\(L^2\)-norm harmonic interpolant is
\[
h_y(z)=\frac34\sum_{i<j}y_{ij}\,P_3^{(7)}(\langle z,x_{ij}\rangle),
\qquad \|h_y\|_{L^2}^2=\frac{3}{308}\sum_{i<j}|y_{ij}|^2,
\]
where \(P_3^{(7)}(t)=(9t^3-3t)/6\) is normalized by \(P_3^{(7)}(1)=1\). The failure of surjectivity and quotient-tightness at \(m=8\) are the unique events of these respective types in this family.

## Assumptions and scope
All integers \(m\ge5\) are covered. The vectors \(e_i\) are the standard coordinate vectors of \(\mathbb R^m\). Complex harmonic polynomials here mean the complexifications of real harmonic cubics under the Laplacian on the \((m-1)\)-dimensional Euclidean space \(V_m\). The inner product on the sphere is normalized to total mass one. The Gram matrix is normalized by \(D_m\), so every diagonal entry equals one; it is not the unnormalized reproducing-kernel Gram matrix. The edges are unordered distinct pairs; no antipodal partners are added.

## Proof
**(1) Reproducing-kernel reduction.** For ambient Euclidean dimension \(d=m-1\), the degree-three normalized Gegenbauer polynomial and the spherical addition theorem give
\[
P_3^{(d)}(t)=\frac{(d+2)t^3-3t}{d-1},\qquad
\frac1{D_m}\sum_{\nu=1}^{D_m}Y_\nu(x)\overline{Y_\nu(z)}=P_3^{(d)}(\langle x,z\rangle).
\]
The node inner products are \(1\) on the diagonal, \(\alpha_m=(m-4)/(2(m-2))\) for distinct edges meeting in one vertex, and \(\beta_m=-2/(m-2)\) for disjoint edges. Hence, writing \(A\) for adjacency of the triangular graph on pairs and \(C\) for disjointness adjacency,
\[
K_m=I+u_m A+v_m C,\quad
u_m=P_3^{(m-1)}(\alpha_m),\quad v_m=P_3^{(m-1)}(\beta_m).
\]
**(2) Three invariant spaces.** Let \(B\) be the \(m\times\binom m2\) unsigned vertex-edge incidence matrix of the complete graph: \(B_{i,\{j,k\}}=1\) exactly when \(i\in\{j,k\}\). Then, with each \(J\) the all-ones matrix of the displayed size,
\[
BB^*=(m-2)I+J,\qquad A=B^*B-2I,\qquad C=J-I-A.
\]
Because \(BB^*\) is invertible for \(m\ge5\), edge-data space is the orthogonal direct sum of constants, \(B^*(\mathbf1^\perp)\), and \(\ker B\), of dimensions \(1,m-1,m(m-3)/2\). The respective eigenvalues of \(A\) on these spaces are \(2(m-2),m-4,-2\); the respective eigenvalues of \(C\) are \((m-2)(m-3)/2,-(m-3),1\). This follows directly by applying \(B^*B-2I\) and \(BB^*=(m-2)I+J\), and then \(C=J-I-A\).

**(3) Exact eigenvalues.** Substitute the preceding pairs into \(I+u_m A+v_m C\):
\[
\begin{aligned}
\lambda_0&=1+2(m-2)u_m+\tfrac12(m-2)(m-3)v_m,\\
\lambda_1&=1+(m-4)u_m-(m-3)v_m,\\
\lambda_2&=1-2u_m+v_m.
\end{aligned}
\]
Substituting \(u_m=((m+1)\alpha_m^3-3\alpha_m)/(m-2)\) and the analogous expression for \(v_m\), then collecting numerators, gives the three factorizations in the Finding. For \(m\ge5\), \(\lambda_0\) and \(\lambda_2\) are strictly positive, and \(\lambda_1\) vanishes exactly at \(m=8\). Since \(K_m=D_m^{-1}E_mE_m^*\), the rank conclusions follow for arbitrary complex sample values; neither a genericity hypothesis nor a finite-grid approximation is used.

**(4) Exact exceptional image and tightness.** At \(m=8\), the eigenvalues are \(4/3,0,4/3\). Therefore \(K_8=(4/3)P\), where \(P\) is the orthogonal projector onto \(\mathbb C\mathbf1\oplus\ker B\). The annihilated space \(B^*(\mathbf1^\perp)\) consists precisely of the seven independent vertex-incidence contrasts \(w_{ij}=a_i+a_j\) for \(\sum_i a_i=0\). Orthogonality to this space is equivalent to \(By\) being a constant vector, which is the displayed characterization of cubic sample data. The reconstruction expression in the Finding belongs to \(\mathcal H_3(V_8)\) by the reproducing property and satisfies \(E_8h_y=(3/4)K_8y=y\) for feasible \(y\). Its norm is computed from the Gram identity:
\[
\|h_y\|_{L^2}^2=\left(\frac{3}{4D_8}\right)^2 D_8\langle K_8y,y\rangle
=\frac{3}{4D_8}\|y\|_2^2=\frac{3}{308}\|y\|_2^2.
\]
It is minimal-norm because it lies in the span of evaluation representers, the orthogonal complement of \(\ker E_8\). Finally,
\[
\lambda_0-\lambda_2=
\frac{m(m+1)(m-4)(m-1)(m-8)}{4(m-2)^4},
\]
so only \(m=8\) can make these two nonzero sectors coincide. For any \(m\ne8\), all three sectors are positive, and hence this rank-deficient quotient-tight phenomenon cannot recur.

## Verification
The standalone standard-library script `check_cubic_simplex.py` constructs the complete rational zonal Gram matrix, tests representatives from all three invariant spaces, the derived eigenvalues and trace, positivity, and the unique singular parameter. At \(m=8\) it additionally verifies entrywise \(K^2=(4/3)K\) and annihilation of an incidence-contrast vector. The invocation `python check_cubic_simplex.py` passed all 19 tested integers \(m\in\{5,6,\ldots,19,24,28,32,40\}\), using exact rational arithmetic. The infinite-family theorem rests on the symbolic argument above; finite tests do not prove it.

## Relationship to prior work
The addition theorem, degree-three Gegenbauer polynomial, spherical-design principles, and the 28-line configuration in dimension seven are classical and are not asserted new. Seidel's *Spherical Harmonics and Combinatorics* (1981) supplies these tools and separately discusses a 28-line configuration and discrete-sphere Hahn polynomials. The Delsarte–Goethals–Seidel design theory predates these techniques. Dette–Melas–Pepelyshev study optimal spherical-harmonic regression designs in dimension three, and Roy–Suda study complex spherical designs and their association schemes. The assertion here is narrower and different: explicit all-parameter degree-three **real-spherical** evaluation spectra on the normalized edge midpoints of **every** regular simplex, together with the isolated seven-dimensional rank-loss and its exact tight reconstruction formula. No matching equality/spectrum result was identified in the inspected primary text or relevant research searches; this is evidence-bounded, not a claim of exhaustive priority proof.

## Limitations
Only homogeneous harmonic degree three is treated; the result does not classify arbitrary harmonic bands or perturbed node configurations. It asserts surjectivity of the evaluation map, not injectivity on the full harmonic polynomial space, whose dimension exceeds the node count. The exceptional rank is \(21\) and does not mean all 28 sample values are independently recoverable. Earlier foundational design literature may contain an implicit equivalent specialization; in particular the full text of the 1977 Delsarte–Goethals–Seidel article was unavailable for direct comparison, although Seidel's later expository full text was inspected. This same-author mathematical review does not constitute an independent assessment.

## References
- J. J. Seidel, *Spherical Harmonics and Combinatorics*, Eindhoven memorandum 1981-07 (June 1981), especially Sections 2–6. Public PDF: https://pure.tue.nl/ws/files/4294066/696891.pdf
- P. Delsarte, J. M. Goethals, and J. J. Seidel, *Spherical codes and designs*, *Geometriae Dedicata* 6 (1977), 363–388, DOI: 10.1007/BF03187604 (full text not consulted).
- H. Dette, V. B. Melas, and A. Pepelyshev, *Optimal designs for three-dimensional shape analysis with spherical harmonic descriptors*, arXiv:math/0603075, first version 2006-03-03 (abstract read).
- A. Roy and S. Suda, *Complex spherical designs and codes*, arXiv:1104.4692, first version 2011-04-25 (relevant full-text sections inspected).
