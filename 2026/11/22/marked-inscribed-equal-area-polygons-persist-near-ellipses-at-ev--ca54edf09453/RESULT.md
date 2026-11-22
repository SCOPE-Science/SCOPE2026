# Marked inscribed equal-area polygons persist near ellipses at every odd order

## Finding

**Local marked-inscription theorem.** Fix any odd integer \(n\geq5\). There are positive constants \(\delta_n\) and \(\eta_n\) such that, for every real \(2\pi\)-periodic \(C^2\) function \(\rho\) with \(\|\rho-1\|_{C^2}<\delta_n\), and for every prescribed angular parameter \(\alpha\in\mathbb R/(2\pi\mathbb Z)\), the strictly convex oval
\[
\Gamma_\rho(\theta)=\rho(\theta)(\cos\theta,\sin\theta)
\]
contains a unique *near-regular, cyclically ordered* inscribed \(n\)-gon \(P_0,\ldots,P_{n-1}\) of the form
\[
P_j=\Gamma_\rho(\theta_j),\qquad
\theta_0=\alpha,\quad
\left|\theta_j-\left(\alpha+\frac{2\pi j}{n}\right)\right|<\eta_n\ (1\leq j<n),
\]
whose consecutive-vertex triangles \((P_j,P_{j+1},P_{j+2})\) all have exactly the same positive oriented area (indices modulo \(n\)). The solution depends \(C^1\)-continuously on \(\rho\) in the \(C^2\) topology and on \(\alpha\). The constants can be chosen uniformly in the prescribed point; uniqueness is only within the displayed near-regular angular neighborhood.

This transfers by any nonsingular affine change of coordinates to all sufficiently \(C^2\)-nearby ovals around any fixed nondegenerate ellipse, with **any** prescribed boundary vertex. It is a local, fixed-odd-order, prescribed-point affirmative instance of the inscribed equal-area polygon question explicitly posed in Craizer–Teixeira–da Silva (2011, Section 3.3), not a solution for arbitrary ovals.

**First variation.** Let \(\rho_\varepsilon=1+\varepsilon f+o_{C^2}(\varepsilon)\), where \(f\in C^2(\mathbb S^1)\), and write
\[
\theta_j(\varepsilon)=\alpha+j\Delta+\varepsilon u_j+o(\varepsilon),\qquad
\Delta=2\pi/n,\quad u_0=0.
\]
Define \(f_j=f(\alpha+j\Delta)\),
\[
c_n=\cos\Delta-\cos(2\Delta)>0,\qquad
G_j=(\sin\Delta-\sin(2\Delta))(f_j+f_{j+2})+2\sin\Delta\,f_{j+1}.
\]
Then \(u_j\) is uniquely and constructively specified by
\[
\boxed{\quad u_{j+2}-u_j=\frac{\overline G-G_j}{c_n},\qquad
\overline G=\frac1n\sum_{k=0}^{n-1}G_k,\qquad u_0=0.\quad}
\]
The indices are cyclic. This gives a linear response to **every** oval deformation and every marked point.

**Sharp parity of the linear mechanism.** For even \(n\ge6\), the analogous marked angular linearization has a nontrivial alternating cokernel; a perturbation with \(f(\theta)=\cos(n\theta/2)\) and marked parameter \(\alpha=0\) violates its compatibility condition. Consequently, no differentiable branch through the corresponding regular \(n\)-gon with this fixed mark exists for that deformation. This **does not assert** that even-order polygons have no solutions, nor exclude branches with nondifferentiable scaling or different limiting configurations.

## Assumptions and scope

The \(C^2\) norm is \(\max_{0\le k\le2}\sup_{\theta}|\partial_\theta^k(\rho(\theta)-1)|\); \(\delta_n\) is existential, depends on the fixed odd \(n\), and is not claimed optimal or uniform in \(n\). A \(C^2\)-small positive radial graph is strictly convex because its signed curvature numerator is \(\rho^2+2(\rho')^2-\rho\rho''>0\). The marked angle \(\alpha\) is fixed before solving; the last edge uses \(\theta_n=\theta_0+2\pi\), so the polygon is cyclic rather than open. Equal areas here means equality of areas of the \(n\) triangles made by *three successive vertices*, not an equidissection of the polygon interior. All normalizations are in a fixed Euclidean coordinate system before an optional affine change of coordinates.

## Proof

1. **Exact constraint.** For arbitrary cyclically ordered parameters let \(\Gamma_j=\Gamma_\rho(\theta_j)\) and define the doubled oriented area
\[
F_j=\det(\Gamma_{j+1}-\Gamma_j,\Gamma_{j+2}-\Gamma_{j+1}).
\]
The common-area condition is \(H_j=F_j-F_{n-1}=0\) for \(0\le j\le n-2\). There are \(n-1\) unknown angular corrections because the prescribed parameter \(\theta_0=\alpha\) is fixed. This is a \(C^1\) map from a neighborhood in \(\mathbb R^{n-1}\times C^2(\mathbb S^1)\) to \(\mathbb R^{n-1}\).

2. **Circular solution and exact differential.** At \(\rho=1\) and \(\theta_j=\alpha+j\Delta\), the elementary determinant identity gives \(F_j=2\sin\Delta-\sin(2\Delta)>0\). For *any* three angular parameters with consecutive gaps \(a,b\), the circular value is \(F=\sin a+\sin b-\sin(a+b)\). Differentiating at \(a=b=\Delta\), both partial derivatives equal \(c_n=\cos\Delta-\cos(2\Delta)>0\). Therefore for corrections \(u_j\), with \(u_0=0\),
\[
\mathrm DF_j[u]=c_n(u_{j+2}-u_j),\qquad
\mathrm DH_j[u]=c_n\{u_{j+2}-u_j-u_1+u_{n-1}\}.
\]
All indices are cyclic; the formula is valid also at the wraparound because angular differences are taken with the \(2\pi\)-lift.

3. **Odd-order invertibility.** If \(\mathrm DH[u]=0\), then every \(u_{j+2}-u_j\) has the same value \(a\). Summing these differences over \(j\) gives \(na=0\), hence \(u_{j+2}=u_j\). Since \(n\) is odd, adding \(2\) repeatedly visits every vertex, so all \(u_j\) are equal. The marked condition \(u_0=0\) forces \(u=0\). Thus the square \((n-1)\times(n-1)\) Jacobian is an isomorphism. In particular the parity statement does not depend on numerical conditioning or a finite case enumeration.

4. **Parameter-dependent implicit function theorem.** Applying the Banach-parameter implicit function theorem at each circular configuration yields a unique angular correction vector depending \(C^1\) on \(\rho\) and \(\alpha\). The base Jacobian and its inverse are independent of \(\alpha\); compactness of the angular circle yields the same sufficiently small \(\delta_n\) and \(\eta_n\) for all marked angles. Taking them still smaller preserves successive angular order and strict convexity of the boundary; cyclically ordered distinct points on a strictly convex oval form a strictly convex polygon. Continuity preserves the positive sign of the common doubled triangle area. This proves the theorem for the circle and nearby ovals. Applying an affine bijection scales all oriented areas by its determinant and proves the ellipse formulation.

5. **First variation.** At the circular configuration, the exact radial representation is
\[
F_j=\rho_j\rho_{j+1}\sin(\theta_{j+1}-\theta_j)
+\rho_{j+1}\rho_{j+2}\sin(\theta_{j+2}-\theta_{j+1})
-\rho_j\rho_{j+2}\sin(\theta_{j+2}-\theta_j).
\]
Differentiating in \(\varepsilon\) gives \(\dot F_j=c_n(u_{j+2}-u_j)+G_j\), where \(G_j\) has exactly the form in the Finding. Equality of all \(\dot F_j\) and summation in \(j\) forces that common derivative to equal \(\overline G\). This gives the boxed cyclic difference equation. Since the step-two permutation has one orbit at odd \(n\), \(u_0=0\) determines its unique solution, with closure guaranteed by \(\sum_j(\overline G-G_j)=0\).

6. **Even-order linear obstruction.** At even \(n\), the step-two permutation separates even and odd vertex indices, and the alternating functional annihilates every angular variation: \(\sum_j(-1)^j\mathrm DF_j[u]=0\). The radial contribution instead satisfies
\[
\sum_j(-1)^j G_j=-2\sin(2\Delta)\sum_j(-1)^j f_j.
\]
For \(n\ge6\), \(\sin(2\Delta)\ne0\). With \(f(\theta)=\cos(n\theta/2)\), \(\alpha=0\) gives \(f_j=(-1)^j\), whence this alternating sum is nonzero. A differentiable solution branch with those limiting regular angles would have to satisfy the incompatible linearized equality equations. This proves only the explicitly stated linear obstruction.

## Verification

A standalone reproducibility script, `equal_area_local_check.py`, evaluates the exact determinant constraints, the analytic Jacobian, and nonlinear roots for \(n=5,7,9,11,15\), multiple phases, Fourier perturbations, and small radial amplitudes. It passed 278 deterministic checks, including three first-order tests of the recurrence against the nonlinear determinant formula. The mathematical existence statement for all allowed \(\rho\) is proved by the Jacobian argument and the implicit function theorem, **not** by the finite sample.

Run with `python equal_area_local_check.py` using Python, NumPy, and SciPy. Numerical residual tolerances are specified in the script. The theorem does not provide a computable optimal smallness radius \(\delta_n\).

## Relationship to prior work

Harel–Rabin (2003) study the algebraic classification of abstract equal-area polygons up to affine equivalence, but not an inscribed solution on a prescribed perturbed oval through an arbitrary marked boundary point. Craizer–Teixeira–da Silva (arXiv first public 14 March 2011; Section 3.3) give a near-curve approximation algorithm whose output need not be inscribed, and specifically ask whether an equal-area \(n\)-gon *can be inscribed* with a preassigned first vertex, predicting a positive odd-order answer. The result here proves a local version of that explicitly stated question for every fixed odd \(n\), plus local uniqueness and a deformation-response formula. It is not implied by the existence of affinely regular polygons on ellipses alone, because the deformed oval need not itself be a conic.

The proof is a direct finite-dimensional implicit-function argument, with a structural step-two parity rank calculation; no broad global inscribed-polygon theorem or general odd-order solution is claimed. Searches of related convex-curve approximation and inscribed-polygon literature found no equivalent marked near-ellipse conclusion, but this does not establish historical priority; an unlocated perturbative or degree-theoretic proof would dominate the local result.

## Limitations

This result is local in the ambient \(C^2\) oval, local in the \(n\)-gon vertices, and for fixed odd \(n\ge5\). It neither proves that all strictly convex smooth ovals admit a marked equal-area \(n\)-gon nor rules out even-order inscribed polygons. The even-order obstruction concerns differentiable branches approaching a **specified** regular configuration, not arbitrary solution branches. The neighborhood parameters are existential and not quantified. Independence and exhaustive historical priority are not certified.

## References

1. G. Harel and J. M. Rabin, “Polygons Whose Vertex Triangles Have Equal Area,” *American Mathematical Monthly* **110** (2003), 606–619. Lawful manuscript: https://mathweb.ucsd.edu/~jrabin/publications/Polygons.pdf.
2. M. Craizer, R. C. Teixeira, M. A. H. B. da Silva, “Affine Properties of Convex Equal-Area Polygons,” arXiv:1103.2722, first submitted 14 March 2011; *Discrete & Computational Geometry* **48** (2012), 580–595, https://arxiv.org/abs/1103.2722, DOI: 10.1007/s00454-012-9448-y. See Section 3.3 for the marked inscribed-polygon question.
3. R. C. Teixeira, “Convex Equal-Area Polygons,” author’s explanatory webpage: https://www.professores.uff.br/ralphteixeira/convex-equal-area-polygons-ceap/ (states the same inscribed-polygon question).
