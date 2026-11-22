# Higher-dimensional chainlink section pairs preserve two separate Euclidean facet-area totals

## Finding
For every integer \(s\ge4\), complementary hyperplane sections of an admissible chainlink polytope have equal **Euclidean boundary area**, even when their face lattices differ. More strongly, the sums of Euclidean areas of their two defining facet classes agree separately:
\[
B(P_t)=B(P_{N-t}),\qquad R(P_t)=R(P_{N-t}).
\]
Here \(B\) totals the coordinate-boundary facets and \(R\) totals the cyclic-difference facets. All areas are intrinsic Euclidean \((s-2)\)-dimensional Hausdorff measures on the affine hyperplane of each section; they are **not** normalized lattice volumes.

A concrete four-coordinate example is \(\mathbf a=(4,5,6,7)\), \(\ell=2\), \(N=22\), \(t=9\), and \(N-t=13\). Exact facet enumeration gives
\[
B(P_9)=B(P_{13})=43\sqrt3,\qquad
R(P_9)=R(P_{13})=49\sqrt2,
\]
whereas \(P_9\) has \(16\) vertices and \(P_{13}\) has \(15\). Thus the area equivalence does not require combinatorial equivalence.

## Assumptions and scope
Fix an integer \(s\ge4\), real numbers \(a_i>0\), and \(\ell\ge0\) with \(2\ell\le\min_i a_i\). Let \(N=\sum_{i=1}^s a_i\) and take real \(0<t<N\). Indices are interpreted modulo \(s\). Define
\[
C(\mathbf a,\ell)=\{x\in\mathbb R^s:0\le x_i\le a_i,\ x_i-x_{i+1}\le a_i-\ell\},\quad
P_t=C(\mathbf a,\ell)\cap\{\textstyle\sum_i x_i=t\}.
\]
Every such \(P_t\) is full-dimensional in the affine hyperplane \(H_t\), with dimension \(d=s-1\). This follows by taking the coordinatewise proportional interior point \(x_i=(t/N)a_i\): the coordinate bounds are strict, while any positive cyclic difference is strictly smaller than \(a_i-a_{i+1}\le a_i-2\ell<a_i-\ell\) when \(\ell>0\); the \(\ell=0\) case is immediate from the box interior.

For a facet of \(P_t\), classify it as *box* if its supporting equation is \(x_i=0\) or \(x_i=a_i\), and *link* if its equation is \(x_i-x_{i+1}=a_i-\ell\). Distinct defining normal directions cannot describe the same facet for \(s\ge3\). Let \(B(P_t)\) and \(R(P_t)\) be the sums of the \((s-2)\)-dimensional Euclidean volumes of these facets; an inactive or lower-dimensional face contributes zero. When \(\ell=0\), the link inequalities are redundant and \(R=0\).

## Proof
**1. Normalize the two facet lattices.** First suppose \(a_i,\ell,t\) are integers, with \(0<t<N\). The difference lattice in the section is
\[
L=\{z\in\mathbb Z^s:\sum_i z_i=0\},\qquad \det L=\sqrt{s}.
\]
The restrictions of both linear forms \(x_i\) and \(x_i-x_{i+1}\) to \(L\) are primitive integer functionals because \(s\ge3\). Their orthogonal projections to the linear space \(H_0\) have norms \(\sqrt{(s-1)/s}\) and \(\sqrt2\), respectively. The facet-sublattice covolumes are therefore
\[
\delta_B=\sqrt{s-1},\qquad \delta_R=\sqrt{2s}.
\]
Indeed, the lattice hyperplane spacing for a primitive linear form with projected normal \(u\) is \(1/\|u\|\), and the product of this spacing with the facet lattice covolume is \(\det L\).

The 2022 chainlink Ehrhart-equivalence theorem states that \(P_t\) and \(P_{N-t}\) have identical Ehrhart quasipolynomials. Their vertices are rational (in fact half-integral for the integer data by Proposition 3.2 of that paper). Taking dilations divisible by a common vertex denominator, the ordinary lattice Ehrhart second-coefficient formula applies to both sections. Equality of those coefficients gives
\[
\frac{B(P_t)}{\sqrt{s-1}}+\frac{R(P_t)}{\sqrt{2s}}
=\frac{B(P_{N-t})}{\sqrt{s-1}}+\frac{R(P_{N-t})}{\sqrt{2s}}.\tag{1}
\]
The factor \(1/2\) common to both second coefficients has been canceled. The formula also applies to integral dilations of rational polytopes, so no unsupported claim about other quasipolynomial residue classes is used.

**2. Extract the link-facet area by moving the link parameter.** Let \(V(t;\mathbf a,\ell)\) denote the intrinsic \(d\)-volume of \(P_t\). The same source gives \(V(t;\mathbf a,\ell)=V(N-t;\mathbf a,\ell)\) for admissible integer data. Homogeneity and clearing denominators extend this identity to rational data, and continuity extends it to **all real** admissible data and heights. For fixed \(\mathbf a,t\), vary \(\ell\) in \(0<\ell<\min_i a_i/2\). Each link inequality has projected Euclidean normal norm \(\sqrt2\), and its right-hand side moves with derivative \(-1\). The standard moving-facet volume formula thus gives
\[
\frac{\partial}{\partial\ell}V(t;\mathbf a,\ell)
=-\frac1{\sqrt2}R(P_t).
\]
The intersections of distinct facet hyperplanes have lower dimension; this formula can also be justified by summing the first-order volumes of the thin slabs removed along the link facets. Differentiating the complementary-volume identity therefore yields
\[
R(P_t)=R(P_{N-t}).\tag{2}
\]
At nongeneric parameter walls the identity follows by continuity of polytope facet areas with fixed, noncoincident defining normals; it also extends to \(\ell=0\) and \(2\ell=\min_i a_i\) by one-sided limits.

**3. Recover the box-facet area and pass to real data.** For integer parameters, subtract (2) from the Ehrhart relation (1) to obtain \(B(P_t)=B(P_{N-t})\). Scaling from rational parameters and taking limits extends this identity to all real parameters and real heights satisfying the stated inequalities. The total Euclidean boundary area is \(B+R\), so its complementary-height symmetry follows.

**4. Nonisomorphic witness.** In the four-coordinate example, exact rational vertex enumeration gives \(|\operatorname{Vert}(P_9)|=16\) and \(|\operatorname{Vert}(P_{13})|=15\). Facets of the box class have sublattice covolume \(\sqrt3\), and link facets covolume \(\sqrt8\). The exact enumerator computes respectively normalized facet-volume totals \(43\) and \(49/2\) for both sections; multiplying by their covolumes yields the displayed Euclidean totals. Different vertex numbers preclude a combinatorial isomorphism.

## Verification
Run `python3 check.py` with Python 3. The checker enumerates vertices as exact rational intersections of active constraints, verifies every inequality, reconstructs each facet polygon using exact two-dimensional convex hulls, and computes its Euclidean area as an exact rational multiple of the relevant facet-lattice covolume. It checks six parameter instances, including the \(16\)-versus-\(15\) witness; the expected last line is `CHAINLINK_FACET_CLASS_EXACT_PASS cases=6`. These finite checks are independent consistency tests, not an exhaustive proof for every \(s\).

## Relationship to prior work
Kantarcı Oğuz, Özel and Ravichandran introduced chainlink polytopes and proved equality of the Ehrhart quasipolynomials and volumes of complementary sections in every admissible dimension [1]. These facts are central inputs here, not new claims. An earlier public result [2] already proves the corresponding Euclidean perimeter and separated edge-length laws for **three-coordinate** chainlink polygons, and is explicitly excluded from this theorem's dimensional claim. The present result concerns all sections in **four or more** coordinates: a boundary-area symmetry in Euclidean dimension at least three, derived using the distinct facet-sublattice covolumes and the link-parameter shape derivative. The nonisomorphic four-coordinate witness exhibits the additional geometric content.

## Limitations
The statement requires the admissibility threshold \(2\ell\le\min_i a_i\), sections strictly between the extreme heights, and canonical Euclidean coordinates. It does not assert equality of individual facets, isometry, width distributions, diameter, or higher intrinsic volumes. The four-coordinate calculation checks only six finite cases; the all-dimensional assertion follows from the proof above. Priority remains provisional because equivalent unindexed geometric deductions from the 2022 theorem may exist, and the full text of the closest three-coordinate result was not accessible during this comparison. Independent mathematical validation has not been performed.

## References
[1] E. Kantarcı Oğuz, C. Y. Özel, M. Ravichandran, *Chainlink Polytopes and Ehrhart-Equivalence*, arXiv:2211.08382v1 (2022-11-15), https://arxiv.org/abs/2211.08382 ; Annals of Combinatorics 28 (2024), DOI:10.1007/s00026-023-00683-x. Relevant statements: definition in Section 3, Theorem 4.8, Proposition 3.2.

[2] *Complementary three-chainlink sections preserve Euclidean perimeter and separate facet-length totals*, published research record (2026-11-08), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-complementary-three-chainlink-sections-preserve-euclidean-perime--26d25037b662 . Accessible summary explicitly restricts to three coordinates; full text could not be inspected.
