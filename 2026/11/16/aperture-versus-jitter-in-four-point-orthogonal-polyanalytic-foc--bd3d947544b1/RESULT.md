# Aperture versus jitter in four-point orthogonal polyanalytic Fock designs

## Finding

Let \(\alpha>0\), and consider the **full** (not single-Landau-level) order-three polyanalytic Fock reproducing kernel on \(\mathbb C\):
\[
K_{3,\alpha}(z,w)=e^{\alpha z\overline w}L_2^{(1)}(\alpha|z-w|^2),\qquad
L_2^{(1)}(x)=3-3x+\frac{x^2}{2}.
\]
For distinct nodes \(\Lambda=(z_1,\ldots,z_m)\), write \(k_z=K_{3,\alpha}(\cdot,z)/\sqrt{K_{3,\alpha}(z,z)}\), and let \(G_\Lambda=(\langle k_{z_j},k_{z_i}\rangle)_{i,j}\) be the normalized evaluation Gram matrix. The largest number of mutually orthogonal evaluation kernels is exactly **four**.

Put \(a=3-\sqrt3\) and \(b=3+\sqrt3\). Every four-node orthogonal configuration is, up to a Euclidean rigid motion (including reflection) and node permutation, **exactly one of two forms**. In the following coordinates the factor \(\alpha^{-1/2}\) multiplies every displayed complex coordinate:
\[
\begin{aligned}
\Lambda_A:&\quad -\frac{\sqrt a}{2},\quad \frac{\sqrt a}{2},\quad
 i\frac{\sqrt{3a}}2,\quad i\left(1+\frac{\sqrt3}2\right)\sqrt a;\\
\Lambda_B:&\quad -\frac{\sqrt b}{2},\quad \frac{\sqrt b}{2},\quad
 i\frac{\sqrt{3b}}2,\quad i\frac{a-b/2}{\sqrt{3b}}.
\end{aligned}
\]
For any finite set \(\Lambda\), define its aperture \(R(\Lambda)=\inf_{c\in\mathbb C}\max_{z\in\Lambda}|z-c|\). For an orthogonal four-node configuration define **one-node first-order jitter sensitivity**
\[
J(\Lambda)=\max_{1\le j\le4}\sup_{|v|=1}
\lim_{\varepsilon\downarrow0}\frac{\|G_{\Lambda(j,\varepsilon v)}-I_4\|_{\mathrm{op}}}{\varepsilon},
\]
where only node \(z_j\) moves to \(z_j+\varepsilon v\). The limits exist, and the sharp values are
\[
\begin{array}{c|cc}
& R^2 &J^2\\\hline
\Lambda_A& a/\alpha & (10\alpha a/3)e^{-a}\\
\Lambda_B& b/(3\alpha)&(2\alpha b/3)e^{-a}.
\end{array}
\]
**There is a strict tradeoff:** \(R(\Lambda_A)<R(\Lambda_B)\) but \(J(\Lambda_B)<J(\Lambda_A)\). Therefore the aperture-minimal four-node exact orthogonal design is unique up to rigid motion, and the jitter-minimal design is the *other* unique congruence class. The equivalent order-three polyanalytic Gaussian RBF reproducing kernel has the same orthogonal node patterns after its standard nonvanishing Gaussian gauge and rescaling; jitter constants above refer specifically to the Fock normalization and its Euclidean node coordinates.

## Assumptions and scope

The Hilbert space is the full Gaussian-weighted polyanalytic Fock space of order three in **one complex variable** with Gaussian rate \(\alpha>0\). Nodes are distinct. Orthogonality refers to the canonical normalized point-evaluation vectors, not to basis functions of one true Landau level. The sensitivity is for movement of **one** node while the other three remain fixed; it measures the operator norm of the full four-by-four normalized Gram perturbation. It is not a uniform simultaneous multi-node perturbation bound. Euclidean reflection, translation and rotation preserve aperture, orthogonality and the stated sensitivity. The underlying Hilbert space is infinite-dimensional, so the four orthogonal kernels do not constitute a complete basis.

## Proof

**(1) Kernel zeros.** The normalized pairwise overlap is
\[
\langle k_w,k_z\rangle= e^{i\alpha\operatorname{Im}(z\overline w)}
 e^{-\alpha|z-w|^2/2}\frac{L_2^{(1)}(\alpha|z-w|^2)}{3}.
\]
Its nonvanishing exponential factors show that two distinct evaluation kernels are orthogonal exactly when \(\alpha|z-w|^2\in\{a,b\}\). Work first in scaled coordinates \(X=\sqrt\alpha z\). Let \(t=b/a=2+\sqrt3\) and normalize the short squared distance to one. A four-point candidate has each of its six edges colored short or long. If \(D_{ij}\) denotes its squared distance, then the anchored three-by-three Euclidean Gram matrix is \(H_{ij}=(D_{0i}+D_{0j}-D_{ij})/2\), for \(1\le i,j\le3\). Four points in a real plane require \(\det H=0\).

There are exactly eleven isomorphism classes of simple graphs on four vertices, where the graph records the **long** edges. Computing \(8\det H\) as a polynomial in the long squared-distance ratio \(t\) gives the following exhaustive list; the middle column is the nondecreasing vertex-degree sequence:

| Long edges | Degree sequence | \(8\det H\) |
|---:|---|---|
| 0 | 0,0,0,0 | \(4\) |
| 1 | 0,0,1,1 | \(-2t(t-3)\) |
| 2 | 0,1,1,2 | \(-2(t^2-4t+1)\) |
| 2 | 1,1,1,1 | \(-4t^2(t-2)\) |
| 3 | 0,2,2,2 | \(-2t^2(t-3)\) |
| 3 | 1,1,1,3 | \(2(3t-1)\) |
| 3 | 1,1,2,2 | \(-2(t+1)(t^2-3t+1)\) |
| 4 | 1,2,2,3 | \(-2t(t^2-4t+1)\) |
| 4 | 2,2,2,2 | \(4(2t-1)\) |
| 5 | 2,2,3,3 | \(2t(3t-1)\) |
| 6 | 3,3,3,3 | \(4t^3\) |

Here \(8\det H\) is computed using the Gram entries just defined; its vanishing is unchanged by the overall positive scaling. At \(t=2+\sqrt3\), only the **two-edge path with one isolated vertex** and its graph complement (**four** long edges) satisfy this necessary determinant condition. Their rank-two Euclidean Gram matrices are positive semidefinite and give one congruence class each, as established by the explicit realizations in the Finding. Thus the list of four-node orthogonal configurations is complete.

**(2) No five nodes.** Suppose five nodes existed and color each long edge in the complete five-vertex graph. Every induced four-vertex long-edge graph must have **two or four** edges, and must have one of the two just-classified shapes. Write \(E\) for the number of long edges of the five-vertex graph. Each edge appears in exactly three four-vertex deletions, hence the sum of their edge counts is \(3E\). It is even and lies between \(10\) and \(20\), forcing \(E\in\{4,6\}\). The two permissible four-vertex patterns are complementary; replacing long edges by short edges allows us to assume \(E=4\). Then the sum of the five deletion-edge counts is twelve, so precisely one deletion has four edges and the other four have two. The vertex removed by the four-edge deletion has degree zero. The remaining four-vertex graph is the complement of a two-edge path plus isolated vertex: it contains a triangle and a pendant vertex. Deleting that pendant vertex gives a four-vertex graph consisting of the triangle plus the original isolated vertex, with **three** long edges, a contradiction. Thus there are at most four points, and both displayed configurations attain four.

**(3) Minimal enclosing circles.** For type A, the three points other than \(i\sqrt{3a}/2\) form an acute isosceles triangle whose circumcenter is exactly \(i\sqrt{3a}/2\) (using scaled coordinates) and whose circumradius is \(\sqrt a\). It is the unique minimal enclosing circle. For type B, the first three points form an equilateral triangle of side \(\sqrt b\), with circumradius \(\sqrt{b/3}\). The fourth point lies strictly inside this circumcircle because its distance from the triangle circumcenter is \((b-a)/\sqrt{3b}<\sqrt{b/3}\). Rescaling by \(\alpha^{-1/2}\) gives the two asserted radii. Since \(b>3a\), type A has strictly smaller aperture.

**(4) Exact one-node differential.** When node \(z_i\) moves, every diagonal entry stays one, while the only off-diagonal derivatives are in row and column \(i\). At each allowed squared distance \(x=a,b\), one has \(|(L_2^{(1)})'(x)|=\sqrt3\), so a perturbed normalized off-diagonal entry satisfies
\[
\left|\frac{d}{d\varepsilon}\Big|_{\varepsilon=0}
\langle k_{z_j},k_{z_i+\varepsilon v}\rangle\right|
=\frac{2\alpha}{\sqrt3}e^{-\alpha|z_i-z_j|^2/2}
\left|\operatorname{Re}((z_i-z_j)\overline v)\right|.
\]
Because the Hermitian first-order Gram matrix has just one nonzero row and its adjoint column, its operator norm is the Euclidean length of that row. In scaled real coordinates \(X_j\in\mathbb R^2\), define
\[
M_i=\sum_{j\ne i}e^{-|X_i-X_j|^2}(X_i-X_j)(X_i-X_j)^\mathsf T.
\]
Then \(J(\Lambda)^2=(4\alpha/3)\max_i\lambda_{\max}(M_i)\).

For type A the maximum occurs at its central short-distance vertex. The corresponding matrix has eigenvalues \((a/2)e^{-a}\) and \((5a/2)e^{-a}\). For each other vertex the trace of \(M_i\) is either \(2ae^{-a}+be^{-b}\) or \(ae^{-a}+2be^{-b}\), both strictly below \((5a/2)e^{-a}\). These inequalities follow, for example, from \(be^{-(b-a)}<a/2\). Consequently \(J_A^2=(10\alpha a/3)e^{-a}\).

For type B the maximum occurs at the vertex incident to the two short edges. At this vertex \(M_i\) is diagonal with entries \((b/2)e^{-a}\) and \((2a-b/2)e^{-a}+be^{-b}\); the first is larger. The other vertices have trace at most \(ae^{-a}+2be^{-b}\) or \(3be^{-b}\), strictly below \((b/2)e^{-a}\). Indeed \(b-a=2\sqrt3\) gives \(e^{-(b-a)}<e^{-3}<1/20\), while \((b/2-a)/b=\sqrt3-3/2>1/10\). Thus \(J_B^2=(2\alpha b/3)e^{-a}\). Finally \(5a>b\), so \(J_B<J_A\), opposite to the aperture comparison. This proves the strict optimization tradeoff.

## Verification

The standalone standard-library `CHECK.py` constructs the anchored Gram determinants in the exact quadratic field \(\mathbb Q(\sqrt3)\), exhausts all \(64\) possible four-vertex edge colorings, verifies that exactly \(24\) labeled patterns have the permitted determinant-zero shapes, and independently exhausts all \(1024\) five-vertex colorings, finding none compatible with every four-vertex restriction. It checks the six distances for both constructions and the analytical first-order Gram sensitivities by weighted two-by-two matrix eigenvalues, supplemented by finite differences. These are exhaustive **finite** certificates for the graph-classification step; they are not substitutes for the algebraic reproducing-kernel identity or the geometric and differential arguments above.

## Relationship to prior work

The full polyanalytic Fock and Gaussian RBF kernels, including their generalized Laguerre formulas and Gaussian gauge equivalence, are established in De Bie–De Martino–Diki [1]; the Laguerre kernel and normalized evaluations are also recorded in Fulsche–Hagger [2]. **They are not new here.** Harborth–Piepmeyer [3] explicitly identify the extremal planar four-point two-distance ratio \(\sqrt{2+\sqrt3}\) and two associated geometries; the five-point regular-pentagon classification is also classical. **The planar two-distance classification is not new here.** The contribution claimed is the exact order-three *kernel-evaluation* design comparison, especially the sharp Gaussian-overlap first-order jitter constants and the reversal of the aperture preference. Published searches for equivalent coherent-kernel sensitivity optima and matching evaluations did not reveal this quantitative theorem. As a residual priority risk, a prior work could have combined these classical ingredients and calculated identical stability constants under other conventions.

## Limitations

This is a natural **four-point exact-orthogonality** optimization in one complex dimension for the full order-three Gaussian polyanalytic Fock space, not an optimization over arbitrary near-orthogonal frames or all node cardinalities and orders. The jitter norm applies to a single moving node; simultaneous perturbations, nonlinear displacement tolerances and non-Gaussian weights remain outside the theorem. The underlying two-distance classification has substantial classical precedent and the incremental contribution must not be interpreted as inventing the planar geometries. Independent publication-priority review has not been performed.

## References

[1] H. De Bie, A. De Martino and K. Diki, *Polyanalytic Gaussian Radial Basis Function Kernel and Itô-Hermite Polynomials*, arXiv:2510.14639, first posted 2025-10-16, especially §2.2 and §4. https://arxiv.org/abs/2510.14639

[2] R. Fulsche and R. Hagger, *Quantum Harmonic Analysis for Polyanalytic Fock Spaces*, Journal of Fourier Analysis and Applications (2024), §3, DOI:10.1007/s00041-024-10124-9. https://link.springer.com/article/10.1007/s00041-024-10124-9

[3] H. Harborth and L. Piepmeyer, *Two-Distance Sets and the Golden Ratio*, in *Applications of Fibonacci Numbers*, pp. 279–288 (1993), DOI:10.1007/978-94-011-2058-6_27. The publicly accessible abstract documents the extremal four-point ratio and the two geometries; the complete chapter was not inspected. https://econpapers.repec.org/bookchap/spr/sprchp/978-94-011-2058-6_5f27.htm

[4] P. Erdős and P. Fishburn, *Maximum planar sets that determine k distances*, Discrete Mathematics **160** (1996), 115–125, DOI:10.1016/0012-365X(95)00153-N (two-distance five-point regular-pentagon theorem).
