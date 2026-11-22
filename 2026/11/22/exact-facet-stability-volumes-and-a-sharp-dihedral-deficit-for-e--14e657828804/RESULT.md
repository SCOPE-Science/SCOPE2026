# Exact facet-stability volumes and a sharp dihedral deficit for Euclidean simplices

## Finding
Let \(T=\operatorname{conv}(v_0,\ldots,v_d)\) be an arbitrary nondegenerate Euclidean simplex in \(\mathbb R^d\), \(d\ge2\). For its facet \(F_i\) opposite \(v_i\), write \(u_i\) for the outward unit normal and \(h_i>0\) for the distance from \(v_i\) to the hyperplane of \(F_i\). Define \(g_{ij}=\langle u_i,u_j\rangle\), \(s_+=\max\{s,0\}\), and
\[
 b_i=h_i\sum_{j\ne i}\frac{(g_{ij})_+}{h_j}.
\]
For a uniformly random point \(X\in T\), treated as a freely assigned center of mass, the probability that \(F_i\) is a stable supporting facet is
\[
 \Pr(F_i\text{ stable for }X)=\frac1{1+b_i}.
\]
More exactly, the closed locus of such points is a simplex \(E_i=\operatorname{conv}(F_i,w_i)\), with an explicit vertex described below. Consequently, the expected number of stable facets obeys
\[
 \mathbb E S(T,X)=\sum_{i=0}^{d}\frac1{1+b_i}.
\]
It equals \(d+1\) exactly when every interior dihedral angle is nonobtuse. Whenever a specified pair of facets has \(g=g_{ij}>0\),
\[
 d+1-\mathbb E S(T,X)\ \ge\ \frac{2g}{1+g}.
\]
This angular deficit is **sharp for every \(d\ge2\) and every \(0<g<1\)**. Equality for a given pair occurs exactly when it is the only pair with positive \(g_{k\ell}\) and \(h_i=h_j\).

## Assumptions and scope
The simplex is full-dimensional, with all altitudes nonzero. The reference point has the normalized Lebesgue distribution on \(T\), rather than a distribution induced by uniform material density: arbitrary positive mass distributions can in principle assign a chosen interior center of mass. In dimension three a stable facet equilibrium means the perpendicular from the reference point meets the relative interior of the supporting triangular face. At the boundaries of the face-active loci, feet may land on edges, but these configurations have reference-point probability zero; using closed faces causes no ambiguity in volume or expectation. For dimensions exceeding three, ``stable facet'' is the direct Euclidean supporting-hyperplane analogue.

## Proof
**1. Signed-distance and projection coordinates.** Let \(\lambda_0,\ldots,\lambda_d\) be the affine barycentric functions on \(T\). The simplex half-space representation shows
\[
 \lambda_j(x)=\frac{c_j-\langle u_j,x\rangle}{h_j},
 \qquad \nabla\lambda_j=-\frac{u_j}{h_j},
\]
where \(c_j\) is the support value of \(F_j\). The perpendicular projection of the apex \(v_i\) onto \(\operatorname{aff}(F_i)\) is \(z_i=v_i+h_i u_i\). Express it in the affine coordinate system of \(F_i\):
\[
 z_i=\sum_{j\ne i}q_{ij}v_j,\qquad
 q_{ij}=\lambda_j(z_i)=-\frac{h_i}{h_j}\langle u_i,u_j\rangle.
\]
Thus \(\sum_{j\ne i}q_{ij}=1\). Define \(c_{ij}=(-q_{ij})_+\) and \(b_i=\sum_{j\ne i}c_{ij}\); this agrees with the outward-normal formula in the finding.

**2. Entire active locus, not only a probability.** A point \(x=\sum_k\lambda_kv_k\in T\) projects onto the hyperplane \(\operatorname{aff}(F_i)\) with facet barycentric coordinates \(\lambda_j+\lambda_iq_{ij}\), indexed by \(j\ne i\). The projection belongs to \(F_i\) precisely when
\[
 \lambda_j\ge c_{ij}\lambda_i\qquad(j\ne i).
\]
Define nonnegative new barycentric coordinates
\[
 \mu_i=(1+b_i)\lambda_i,\qquad
 \mu_j=\lambda_j-c_{ij}\lambda_i\quad(j\ne i).
\]
They sum to one. Conversely, every nonnegative \(\mu\) summing to one gives the above inequalities through
\[
 \lambda_i=\frac{\mu_i}{1+b_i},\quad
 \lambda_j=\mu_j+\frac{c_{ij}\mu_i}{1+b_i}.
\]
Therefore the active locus is exactly the simplex with vertices \(v_j\) for \(j\ne i\), together with
\[
 w_i=\frac{v_i+\sum_{j\ne i}c_{ij}v_j}{1+b_i}.
\]
Its altitude over \(F_i\) is the fraction \((1+b_i)^{-1}\) of the original altitude. Taking the ratio of simplex volumes gives \(\operatorname{vol}_d(E_i)/\operatorname{vol}_d(T)=(1+b_i)^{-1}\).

**3. Mean and angle rigidity.** Linearity of expectation sums the individual facet indicators, without any assumption of independence. Each \(b_i\ge0\). Hence the maximum \(d+1\) is attained iff all \(b_i=0\), equivalently \(g_{ij}\le0\) for every pair, equivalently every interior dihedral angle is at most a right angle.

**4. Sharp angular deficit.** Fix \(g_{ij}=g\in(0,1)\), and put \(a=g h_i/h_j\), \(b=g h_j/h_i\). Then \(ab=g^2\). The total expected missing-facet count satisfies
\[
\begin{aligned}
 \Delta&=(d+1)-\mathbb ES(T,X)=\sum_k\frac{b_k}{1+b_k}\\
 &\ge \frac{a}{1+a}+\frac{b}{1+b}\\
 &=\frac{a+b+2g^2}{1+a+b+g^2}\ge\frac{2g}{1+g}.
\end{aligned}
\]
The last inequality follows from \(a+b\ge2g\), because the displayed rational function is strictly increasing in \(a+b\) for \(0<g<1\). Equality requires \(h_i=h_j\) and no other positive pairwise \(g_{k\ell}\). To realize equality for any prescribed \(d\ge2\), \(0<g<1\), choose \(a>b>0\) with \((a^2-b^2)/(a^2+b^2)=g\), take two vertices \((a,b,0),(-a,b,0)\), and let the remaining \(d-1\) vertices form an arbitrarily small regular \((d-2)\)-simplex in the orthogonal subspace \(\{(0,0,z)\}\), centered at the origin. For \(d=2\) the remaining simplex is the origin. The first two barycentric-gradient vectors are \((1/(2a),1/(2b),0)\) and \((-1/(2a),1/(2b),0)\), so their normalized inner product is \(g\), and their lengths coincide. Their inner products with all the remaining barycentric gradients are strictly negative; between remaining gradients, a sufficiently small regular equatorial simplex makes all mutual products negative. Because \(u_k=-h_k\nabla\lambda_k\), this is the required example with exactly one positive outer-normal pair.

**5. Exact tetrahedral benchmark.** For the four vertices \((-20,0,0),(-1,-1,10),(1,1,10),(20,0,0)\), the four facet probabilities, in that order, are
\[
\left(\frac14,\frac{101}{105},\frac{101}{105},\frac14\right),\qquad
 \mathbb ES(T,X)=\frac{509}{210}.
\]
These are exact rational evaluations of the preceding formula, not estimates. This example comes from the 2023 equilibrium study cited below; its specific volume probabilities are the evaluation given here.

## Verification
Run `python3 verification/check_facet_stability.py` using Python 3 and its standard library. It independently solves the facet-foot least-squares system over exact rational coordinates, constructs the predicted active simplex, and checks its determinant volume, barycentric membership inequalities, and the sharp two-apex examples in dimensions \(2\) through \(6\). It also checks the quoted tetrahedral probabilities. The embedded verifier reports **exact rational regression tests passed**. These computations test the implementation and examples; the proof of the universal theorem is the algebraic argument above.

## Relationship to prior work
Almádi, Dawson, Domokos and Regős (2023) establish qualitative criteria for weighted monostable tetrahedra, including the explicit four-vertex example, and characterize when every reference point admits a given facet equilibrium. They do not give the normalized volume or expected stable-facet count for uniformly sampled reference points. Nasonov, Panina and Siersma (2024) formulate general active regions as intersections with face-normal prisms and study the *total* average number of boundary normals. Their facet-prism observation provides a natural geometric starting point, but no simplex-specific exact volume law or sharp facetwise dihedral deficit is stated. A later published result titled *An exact ridge-normal obstruction and a quantitative mean-normal deficit for simplices* establishes a bound for normals based at a codimension-two ridge. Its pairwise rational obstruction shares the two-term coefficient appearing in the present facetwise deficit, but it concerns a **different face stratum and a different expected count**; the facet-region simplex decomposition and the all-facets exact expectation are not supplied by that result. Domokos and Lángi's earlier internal robustness measures a smallest displacement needed to change equilibrium type, rather than the volume of all centers preserving one facet equilibrium.

## Limitations
The reference point is uniform in a fixed simplex, not the fixed centroid of a homogeneous solid and not an arbitrary weighted sampling density. The theorem supplies all single-facet probabilities and the expectation; it does **not** determine joint correlations or the complete distribution of the number of stable facets, nor does it extend directly to arbitrary non-simplex polytopes. Strict boundary conventions have no effect on volumes. The mathematical review is not independent; unindexed prior equivalences remain possible.

## References
1. G. Almádi, R. J. MacG. Dawson, G. Domokos and K. Regős, *On equilibria of tetrahedra*, arXiv:2304.06984 (first posted 2023-04-14); *The Mathematical Intelligencer*, DOI: 10.1007/s00283-023-10294-2.
2. I. Nasonov, G. Panina and D. Siersma, *Concurrent normals problem for convex polytopes and Euclidean distance degree*, arXiv:2406.01773 (first posted 2024-06-03), *Acta Mathematica Hungarica* 174 (2024), 522–538.
3. G. Domokos and Z. Lángi, *The robustness of equilibria on convex solids*, arXiv:1301.4031 (first posted 2013-01-17).
4. *An exact ridge-normal obstruction and a quantitative mean-normal deficit for simplices* (published 2026-10-18), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-an-exact-ridge-normal-obstruction-and-a-quantitative-mean-normal--1b8d323e321a.
