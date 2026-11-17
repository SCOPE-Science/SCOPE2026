# A one-third spoke law for Löwner ellipsoids of ordinary wheel edge polytopes

## Finding
Let \(m\ge3\) be an integer, and let \(W_m=K_1*C_m\) be the wheel graph on a hub \(0\) and rim \(1,\ldots,m\) with cyclic adjacency. Its **ordinary unsigned edge polytope** is
\[
E_m=\operatorname{conv}\{e_u+e_v:\{u,v\}\in E(W_m)\}\subset\mathbb R^{m+1}.
\]
It lies in the affine hyperplane \(\sum_{i=0}^m x_i=2\), with the inherited Euclidean metric and intrinsic dimension \(m\). Let the \(m\) spoke vertices be \(s_i=e_0+e_i\) and the \(m\) rim vertices be \(r_i=e_i+e_{i+1}\). For \(1\le k\le m-1\), put
\[
c_k=4\cos^2\!\left(\frac{\pi k}{m}\right),\qquad D_k(a)=a+(1-a)c_k.
\]
There exists exactly one \(a_m\in(0,1)\) satisfying
\[
\boxed{\frac1{a_m}-\frac1{1-a_m}+\sum_{k=1}^{m-1}\frac{1-c_k}{D_k(a_m)}=0.}
\]
Define
\[
\mu_m=a_m e_0+\frac{2-a_m}{m}\sum_{i=1}^m e_i,
\]
and the positive-definite covariance operator on \(H=\{v:\sum_i v_i=0\}\),
\[
C_m=\frac{a_m}{m}\sum_{i=1}^m(s_i-\mu_m)(s_i-\mu_m)^{\mathsf T}
 +\frac{1-a_m}{m}\sum_{i=1}^m(r_i-\mu_m)(r_i-\mu_m)^{\mathsf T}.
\]
Then the **unique** intrinsic minimum-volume enclosing (Löwner) ellipsoid is
\[
\boxed{\mathcal L_m=\{\mu_m+v:v\in H,\ v^{\mathsf T}(mC_m|_H)^{-1}v\le1\}.}
\]
All \(2m\) edge vertices are contacts. The squared principal semiaxes are
\[
(m+1)a_m(1-a_m)\quad\text{(once)},\qquad
D_k(a_m)\quad (1\le k\le m-1),
\]
and its intrinsic volume is
\[
\operatorname{vol}_m(\mathcal L_m)=\frac{\pi^{m/2}}{\Gamma(m/2+1)}
\sqrt{(m+1)a_m(1-a_m)\prod_{k=1}^{m-1}D_k(a_m)}.
\]
The weight on all spoke vertices has a sharp algebraic asymptotic:
\[
\boxed{a_m=\frac13+\frac{5}{3m}+O(m^{-2})\qquad(m\to\infty).}
\]
For instance, \(a_3=1/2\) and \(a_4=1-1/\sqrt5\). Unlike the centrally symmetric wheel root polytope, the ordinary unsigned wheel edge polytope is not centered at zero; the two constructions should not be identified.

## Assumptions and scope
The wheel is finite, simple, and unweighted. All graph-edge generators have two unit coordinates, no negative signs. The ambient affine hyperplane carries the Euclidean metric inherited from \(\mathbb R^{m+1}\). For a symmetric positive-definite operator \(Q\) on \(H\), an enclosing ellipsoid has the form \(\{z+v:v^{\mathsf T}Q^{-1}v\le1\}\), and its intrinsic volume equals the unit-ball volume times \(\sqrt{\det_H Q}\). The covariance \(C_m\) is formed using probability weights \(a_m/m\) and \((1-a_m)/m\) on individual spoke and rim vertices, respectively; it is not uniform over all \(2m\) vertices unless \(a_m=1/2\).

## Proof
**1. Fourier spectrum and the unique scalar parameter.** Give each spoke vertex mass \(a/m\) and each rim vertex mass \((1-a)/m\), where \(0<a<1\). Their mean is \(\mu(a)=a e_0+(2-a)m^{-1}\sum_i e_i\). The covariance \(C(a)\) on \(H\) has the hub-against-uniform-rim eigenvalue
\[
\lambda_0(a)=\frac{m+1}{m}a(1-a).
\]
On the rim Fourier mode of frequency \(k\), the cyclic rim generator has multiplier \(1+\exp(2\pi\mathrm ik/m)\), whose squared modulus is \(c_k\). Thus the other \(m-1\) eigenvalues are \(\lambda_k(a)=D_k(a)/m\). The determinant in the intrinsic \(m\)-space is therefore
\[
\det_H(mC(a))=(m+1)a(1-a)\prod_{k=1}^{m-1}D_k(a).
\]
Its logarithm has derivative
\[
F_m(a)=\frac1a-\frac1{1-a}+\sum_{k=1}^{m-1}\frac{1-c_k}{D_k(a)}
\]
and second derivative
\[
F'_m(a)=-\frac1{a^2}-\frac1{(1-a)^2}
 -\sum_{k=1}^{m-1}\frac{(1-c_k)^2}{D_k(a)^2}<0.
\]
Because \(F_m(a)\) tends to \(+\infty\) at zero and \(-\infty\) at one, it has exactly one zero \(a_m\), giving the unique determinant maximum within this positive orbit-weight family.

**2. Exact contact equations.** With the inverse taken on \(H\), the squared Mahalanobis distances of any spoke and any rim vertex from their common mean, measured in \(C(a)^{-1}\), are, respectively,
\[
R_s(a)=\frac{1-a}{a}+\sum_{k=1}^{m-1}\frac1{D_k(a)},\qquad
R_r(a)=\frac{a}{1-a}+\sum_{k=1}^{m-1}\frac{c_k}{D_k(a)}.
\]
The Fourier expansion proves these identities directly: the hub-mode contributions are \((1-a)/a\) and \(a/(1-a)\), while the nonconstant rim modes contribute the displayed sums. In particular \(R_s(a)-R_r(a)=F_m(a)\). Also,
\[
aR_s(a)+(1-a)R_r(a)
=\operatorname{tr}_H(C(a)^{-1}C(a))=m.
\]
At \(a=a_m\), both distances equal \(m\). Hence every spoke and every rim vertex lies on the boundary of the ellipsoid with shape operator \(mC_m\), and their convex hull \(E_m\) is contained in it.

**3. Global Löwner optimality and uniqueness.** Consider any ellipsoid containing \(E_m\), of center \(z\) in its affine hull and shape operator \(Q\succ0\) on \(H\). Averaging its \(2m\) vertex-containment inequalities with the positive probabilities defining \(\mu_m,C_m\) gives
\[
\operatorname{tr}_H(Q^{-1}C_m)+(z-\mu_m)^{\mathsf T}Q^{-1}(z-\mu_m)\le1.
\]
For the \(m\) positive eigenvalues of \(Q^{-1/2}C_mQ^{-1/2}\), arithmetic-geometric mean yields
\[
\left(\frac{\det_H C_m}{\det_H Q}\right)^{1/m}
\le\frac1m\operatorname{tr}_H(Q^{-1}C_m)\le\frac1m.
\]
Consequently \(\det_H Q\ge m^m\det_H C_m\). Our candidate attains equality; if an alternative attains equality, its center must be \(z=\mu_m\) and equality of all the eigenvalues forces \(Q=mC_m\). This establishes the asserted globally unique minimum-volume ellipsoid without assuming any symmetry of a competing ellipsoid.

**4. The one-third law and its first correction.** Write
\[
g_a(\theta)=\frac{1-4\cos^2\theta}{a+4(1-a)\cos^2\theta},\qquad
I(a)=\frac1\pi\int_0^\pi g_a(\theta)\,d\theta.
\]
Integrating the elementary identity
\(\pi^{-1}\int_0^\pi[a+4(1-a)\cos^2\theta]^{-1}d\theta=[a(4-3a)]^{-1/2}\)
shows
\[
I(a)=\frac{1}{1-a}\left(\frac1{\sqrt{a(4-3a)}}-1\right).
\]
The function \(I\) is strictly decreasing on \((0,1)\), since it is the integral of \(\partial_a g_a=-(1-4\cos^2\theta)^2/[a+4(1-a)\cos^2\theta]^2\); it has its unique zero at \(a=1/3\). For \(a\) in a fixed neighborhood of \(1/3\), the \(\pi\)-periodic function \(g_a\) extends analytically to a complex strip of uniform positive width. Its Fourier coefficients decay exponentially uniformly in \(a\); summing the Fourier series over the \(m\) equally spaced nodes thus gives
\[
\sum_{k=1}^{m-1}g_a(\pi k/m)=mI(a)-g_a(0)+O(m\rho^m),\qquad 0<\rho<1.
\]
The error and its first derivative are uniform in that neighborhood. Since \(g_a(0)=-3/(4-3a)\),
\[
F_m(a)=mI(a)+b(a)+O(m\rho^m),\qquad
b(a)=\frac1a-\frac1{1-a}+\frac3{4-3a}.
\]
For any fixed numbers \(a_-<1/3<a_+\), the normalized Riemann sums \(F_m(a_\pm)/m\) tend to \(I(a_\pm)\) with opposite signs. Strict decrease of \(F_m\) forces \(a_m\to1/3\). Finally,
\[
I(1/3)=0,\quad I'(1/3)=-3/2,\quad b(1/3)=5/2.
\]
Taylor expansion of \(F_m(a_m)=0\) gives first \(a_m-1/3=O(m^{-1})\), then
\(m(a_m-1/3)=5/3+O(m^{-1})\). This proves the stated \(O(m^{-2})\) expansion. The exact low-order examples follow by factoring the finite determinant or substituting into the strictly decreasing equation.

## Verification
The accompanying Python standard-library program `wheel_unsigned_ellipsoid_verify.py` independently builds the full edge-vertex covariance, solves finite linear systems on the sum-zero hyperplane, and checks the contact equations, Fourier eigenvalues, unique scalar zero, low-order identities, and the predicted asymptotic coefficient. Execute `python3 wheel_unsigned_ellipsoid_verify.py`. Its successful run reports `WHEEL_UNSIGNED_LOEWNER_PASS matrix_orders=3..24 orbit_checks=3..99`, with maximal absolute matrix-contact residual \(2.13\cdot10^{-14}\). Direct matrix tests through \(m=24\), orbit tests through \(m=99\), and asymptotic samples through \(m=2000\) are checks of the proof, not substitutes for the all-integer argument.

## Relationship to prior work
Ohsugi and Tsuchiya (arXiv:2103.15045v1) analyze the \(h^*\)-polynomial and lattice volumes of **PQ-type adjacency polytopes** of join graphs, including wheels. Their graph-associated polytope is different from the ordinary unsigned incidence polytope here, and the examined results do not determine this intrinsic Löwner ellipsoid. Ohsugi and Tsuchiya (arXiv:2008.08621v1) study Ehrhart and matching properties of **symmetric edge polytopes**, likewise a distinct family. Suliman and Weinstein (arXiv:2302.05966v1) give graph-Lewis-weight and enclosing-ellipsoid relations in a centered edge-root setting, but not this unsigned wheel solution. Related published results for the *same* unsigned wheel edge polytope determine its **inscribed Euclidean ball**, rather than its minimum-volume **enclosing** ellipsoid; their metric invariant and proof do not imply the unique positive orbit design or the one-third spoke law. A published exact Löwner result for *symmetric* wheel edge-root polytopes also treats a different polytope with a different Fourier symbol and exponentially rather than algebraically varying optimal weights. The general minimum-volume-enclosing-ellipsoid and D-optimal-design equivalences are classical and are not claimed as novel.

## Limitations
The result fixes an ordinary unsigned wheel edge-incidence realization, its inherited Euclidean metric, and integer rim length at least three. It makes no claim about all graph edge polytopes, other norms, or the inscribed John ellipsoid. The parameter is uniquely characterized by a finite equation and need not have a radical expression. No claim is made about monotonicity or closed formulas beyond the stated expansion. The literature survey is not a proof of historical novelty, especially if an equivalent result appears under classical experimental-design terminology. Independent mathematical audit remains outstanding.

## References
1. H. Ohsugi and A. Tsuchiya, *PQ-type adjacency polytopes of join graphs*, arXiv:2103.15045v1, publicly posted 2021-03-28, https://arxiv.org/abs/2103.15045 .
2. H. Ohsugi and A. Tsuchiya, *Symmetric edge polytopes and matching generating polynomials*, arXiv:2008.08621v1, publicly posted 2020-08-19, https://arxiv.org/abs/2008.08621 .
3. A. Suliman and O. Weinstein, *Infinite Lewis Weights in Spectral Graph Theory*, arXiv:2302.05966v1, publicly posted 2023-02-12, https://arxiv.org/abs/2302.05966 .
4. T. Tran and G. M. Ziegler, *Extremal edge polytopes*, Electronic Journal of Combinatorics 21 (2014), article P2.57, https://www.combinatorics.org/ojs/index.php/eljc/article/download/v21i2p57/pdf/ .
