# Exact local volume spectrum of the maximal ten-vertex spherical four-polytope

## Finding
Let \(p_*\) be the labelled ten-point configuration in \(\mathbb S^3\) consisting of two regular pentagons in mutually orthogonal planes, and let \(V(p)\) be the four-dimensional volume of their convex hull. The positive-semidefinite Hessian of \(V(p_*)-V\), taken on the 30-dimensional product-sphere tangent space with the ordinary sum-of-vertex Euclidean inner product, has **exactly** the following eigenvalues and multiplicities:

| Hessian eigenvalue | Multiplicity |
|---|---:|
| \(0\) | 6 |
| \(25/96\) | 4 |
| \((25+5\sqrt5)/96\) | 12 |
| \(25(3+\sqrt5)/192\) | 4 |
| \((25+5\sqrt5)/48\) | 4 |

The zero eigenspace is precisely the six-dimensional tangent space to the orthogonal orbit. In particular, if \(\mathcal O=SO(4)\cdot p_*\) and \(d(p,\mathcal O)^2=\min_{R\in SO(4)}\sum_{i=1}^{10}\|p_i-R(p_*)_i\|^2\), then the **sharp local quadratic stability constant** is

\[
\liminf_{p\to\mathcal O,\ p\notin\mathcal O}
\frac{V(p_*)-V(p)}{d(p,\mathcal O)^2}=\frac{25}{192}.
\]

The lower limiting ratio is attained along infinitesimal first Fourier modes that change the angular spacing of either pentagon. This result concerns labelled configurations in a neighborhood of the regular-pentagon pair, not a global quantitative stability estimate for all ten-vertex polytopes.

## Assumptions and scope
Let \(a_i=(\cos(2\pi i/5),\sin(2\pi i/5),0,0)\) and \(b_j=(0,0,\cos(2\pi j/5),\sin(2\pi j/5))\), for \(i,j\in\mathbb Z/5\mathbb Z\). Put \(p_*=(a_0,\dots,a_4,b_0,\dots,b_4)\). We work in a sufficiently small neighborhood of \(p_*\) in \((\mathbb S^3)^{10}\), where the facets remain precisely the twenty-five tetrahedra \([a_i,a_{i+1},b_j,b_{j+1}]\). The labelled configuration has no collisions; the norm on tangent vectors is \(\sum_i\|\dot p_i\|^2\). For the global maximizer and its unique orbit, we rely on Medgyes [1]; only its *local second variation* and its exact spectrum are established here.

Define \(\theta=2\pi/5\), \(s=\sin\theta\), and \(c=5s/2\), so \(s^2=(5+\sqrt5)/8\). The maximal volume, already established in [1], is \(V_*=c^2/6=25(10+2\sqrt5)/384\). The Hessian here is \(\operatorname{Hess}(V_*-V)\), **not** the Hessian of \(V\); eigenvalues are for the unscaled product-sphere Riemannian metric.

## Proof
**1. Signed volume and tangent coordinates.** Let \(A=(1/2)\sum_i a_i\wedge a_{i+1}\) and \(B=(1/2)\sum_j b_j\wedge b_{j+1}\). In the stable facet chamber, oriented volume satisfies the determinant identity
\[
24V=\sum_{i,j}\det(a_i,a_{i+1},b_j,b_{j+1}),\qquad
6V=\langle A,*B\rangle.
\]
This is also the area-bivector factorization used for polygon joins in [2].

Write \(z_i=(\cos(i\theta),\sin(i\theta))\) and \(J(x,y)=(-y,x)\). Every sphere-tangent velocity has unique coordinates
\[
\dot a_i=(\alpha_iJz_i,u_i),\qquad
\dot b_j=(v_j,\beta_jJz_j),
\]
where the scalar sequences \(\alpha,\beta\) are real and \(u_i,v_j\in\mathbb R^2\). For a second-variation calculation choose the normalized paths
\[
a_i(t)=\frac{(z_i+t\alpha_iJz_i,\,tu_i)}{\sqrt{1+t^2(\alpha_i^2+\|u_i\|^2)}},\qquad
b_j(t)=\frac{(tv_j,\,z_j+t\beta_jJz_j)}{\sqrt{1+t^2(\beta_j^2+\|v_j\|^2)}}.
\]
At a critical point, their quadratic volume coefficient is independent of the chosen paths with these initial velocities.

**2. Exact second variation.** Orthogonal projection in the first Fourier harmonic gives unique matrices \(M,N\in\mathbb R^{2\times2}\) and residual vectors \(\widetilde u_i,\widetilde v_j\) with
\[
M=\frac25\sum_i u_i z_i^{\mathsf T},\quad
N=\frac25\sum_j v_j z_j^{\mathsf T},\quad
u_i=Mz_i+\widetilde u_i,\quad
v_j=Nz_j+\widetilde v_j,
\]
and \(\sum_i\widetilde u_i z_i^{\mathsf T}=\sum_j\widetilde v_j z_j^{\mathsf T}=0\). 

The component of \(A(t)\) along the first-plane oriented area form is
\[
c-t^2\left(\frac s4\sum_i(\alpha_{i+1}-\alpha_i)^2+\frac s2\sum_i\|u_i\|^2\right)+O(t^3).
\]
The corresponding second-plane component of \(B(t)\) is obtained by replacing \(\alpha,u\) with \(\beta,v\). The first-order mixed bivectors are
\[
A_{\rm mix}'(0)=-s\sum_i(Jz_i)\wedge u_i,\qquad
B_{\rm mix}'(0)=-s\sum_j(Jz_j)\wedge v_j,
\]
with the first formula interpreted as first-plane \(\wedge\) second-plane and the second as second-plane \(\wedge\) first-plane. Using \(\sum_i z_i z_i^{\mathsf T}=(5/2)I_2\) and the four-dimensional Hodge-star rule on mixed bivectors yields
\[
\langle A_{\rm mix}'(0),*B_{\rm mix}'(0)\rangle=-\frac{25s^2}{4}\operatorname{tr}(MN).
\]
Combining these coefficients, and completing the square, gives the full tangent-space identity
\[
\begin{aligned}
V_*-V(p(t))=t^2\,\mathcal Q+O(t^3),\qquad
\mathcal Q={}&\frac{5s^2}{48}\sum_i\big[(\alpha_{i+1}-\alpha_i)^2+(\beta_{i+1}-\beta_i)^2\big]\\
&+\frac{25s^2}{48}\|M+N^{\mathsf T}\|_F^2
+\frac{5s^2}{24}\sum_i\big(\|\widetilde u_i\|^2+\|\widetilde v_i\|^2\big).
\end{aligned}
\]
Here \(\mathcal Q=(1/2)\langle \dot p,\operatorname{Hess}(V_*-V)\dot p\rangle\). In particular there are no omitted angular–cross mixed terms: the area-bivector components involved lie in orthogonal exterior-power sectors.

**3. Diagonalization.** On each of the two cyclic five-point scalar sequences, the difference operator has eigenvalues \(0\) once, \((5-\sqrt5)/2\) twice, and \((5+\sqrt5)/2\) twice. The resulting positive Hessian eigenvalues, each repeated four times across the two pentagons, are
\[
\frac{5s^2}{24}\frac{5-\sqrt5}{2}=\frac{25}{96},\quad
\frac{5s^2}{24}\frac{5+\sqrt5}{2}=\frac{25(3+\sqrt5)}{192}.
\]
For cross velocities, \(\sum_i\|Mz_i\|^2=(5/2)\|M\|_F^2\); the residual spaces have dimension \(6+6=12\) and Hessian eigenvalue \(5s^2/12=(25+5\sqrt5)/96\). The eight matrix dimensions \((M,N)\) split orthogonally into the four-dimensional kernel \(N=-M^{\mathsf T}\) and the four-dimensional space \(N=M^{\mathsf T}\), on which the Hessian eigenvalue is \(5s^2/6=(25+5\sqrt5)/48\). The two constant angular modes and four skew block rotations account for precisely six zero eigenvalues. All remaining eigenvalues are positive, and the smallest is \(25/96\). Their multiplicities sum to \(30\).

**4. Sharp orbit-distance coefficient.** Near \(p_*\), the compact orthogonal orbit has a smooth metric normal tubular neighborhood. Its tangent space is exactly the just-identified six-dimensional Hessian kernel. For a transverse displacement \(w\), Taylor expansion gives \(V_*-V=(1/2)\langle w,Hw\rangle+O(\|w\|^3)\), while squared distance to the orbit is \(\|w\|^2+o(\|w\|^2)\). Therefore the sharp lower limiting ratio is half of the least positive eigenvalue, namely \(25/192\). A first angular Fourier mode attains the limiting ratio.

## Verification
Run `python checker.py` (standard library) and, for the independently assembled complete numerical Hessian, `python full_hessian_check.py` (NumPy). The first script directly reconstructs the twenty-five oriented facet determinants under independently normalized spherical vertex motions. Six deterministic deformations (two angular Fourier modes, a higher-harmonic cross motion, symmetric cross motion, an infinitesimal rotation and a generic mixed direction) agree with the analytic quadratic form to finite-difference precision. It also checks the displayed eigenvalue ordering, the total tangent-space multiplicity \(30\), and the rational identity for the least eigenvalue. The second script constructs all 900 Hessian entries from direct facet determinants and finds the predicted five eigenvalue clusters within \(3\cdot10^{-6}\). Numerical finite differences are **supplementary**; the all-directions proof is the symbolic second-variation identity and harmonic decomposition above.

## Relationship to prior work
Medgyes [1], the first public source dated November 10, 2026, proves that this regular-pentagon pair is the unique ten-vertex global volume maximizer and gives its volume, but does not compute the local Hessian or sharp orbit-distance stability constant. Medgyes [2] provides the oriented polygon-join volume factorization and finite Fourier area bounds; these imply the extremum but do not specify this 30-dimensional second-variation spectrum. Earlier quantitative-stability work on seven-vertex maximal inscribed four-polytopes [3] concerns a different configuration (a triangle joined with two diameters) and does not imply the pentagon-pair spectrum. Targeted mathematical-record and literature searches found no stronger exact statement for this ten-vertex family; this is a priority assessment, not a uniqueness certification.

## Limitations
This is a local, labelled, fixed-ten-vertex statement. It gives neither a global explicit stability inequality over all configurations nor a stability bound for combinatorial types far from the maximizing orbit. The external global maximality theorem is credited to [1], not reproved here. The coefficient is sensitive to the chosen normalization (unit circumsphere and the *sum* of squared labelled Euclidean vertex displacements). No independent audit has been performed, and unindexed literature under different terminology may contain a predecessor.

## References
[1] C. Medgyes, *The inscribed 4-polytope of maximal volume with ten vertices*, arXiv:2611.14674v1 (November 10, 2026), https://arxiv.org/html/2611.14674v1 .

[2] C. Medgyes, *The inscribed 4-polytope of maximal volume with nine vertices*, arXiv:2611.10078v1 (November 6, 2026), https://arxiv.org/abs/2611.10078 .

[3] *Sharp quadratic stability of the seven-vertex maximal-volume inscribed four-polytope*, published-finding corpus research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-sharp-quadratic-stability-of-the-seven-vertex-maximal-volume-ins--713bd690255d .
