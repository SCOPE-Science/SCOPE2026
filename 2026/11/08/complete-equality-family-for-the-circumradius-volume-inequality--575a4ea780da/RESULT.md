# Complete equality family for the circumradius–volume inequality of four-generator spatial zonotopes

## Finding

Let \(Z\subset\mathbb R^3\) be full dimensional and expressible as the Minkowski sum of **at most four** line segments, and let \(R>0\) be its Euclidean circumradius. The known sharp inequality is
\[
\operatorname{Vol}_3(Z)\le 2R^3.
\]
The new statement here is the **complete equality classification**, including its nonregular three-parameter family. Define, for an arbitrary orthonormal frame \(e_1,e_2,e_3\),
\[
\begin{aligned}
q_1&=\tfrac R2(e_1+e_2+e_3),&q_2&=\tfrac R2(e_1-e_2-e_3),\\
q_3&=\tfrac R2(-e_1+e_2-e_3),&q_4&=\tfrac R2(-e_1-e_2+e_3),
\end{aligned}
\]
and put \(T_R=\operatorname{conv}\{q_1,q_2,q_3,q_4\}\). Define the explicit compact feasible region
\[
\Omega_R=\left\{v\in\mathbb R^3:\;
-v\in T_R,\quad 2\|v\|\le R,\quad
\|v-q_i\|\le R\ \text{for }i=1,2,3,4\right\}.
\]
Then \(\operatorname{Vol}_3(Z)=2R^3\) **if and only if**, up to Euclidean isometry and translation, there is a vector \(v\in\Omega_R\) such that
\[
Z=\sum_{i=1}^4[0,q_i+v].
\]
The tetrahedral constraint can be evaluated without convex-hull software: \(-v\in T_R\) is equivalent to \(\langle q_i,v\rangle\le R^2/4\) for all four indices. Consequently the displayed description consists solely of five quadratic inequalities and four linear inequalities. It is exhaustive, not merely a sufficient perturbation criterion.

In particular, for every \(v\) with
\[
0<\|v\|<R\left(1-\frac{\sqrt3}{2}\right),
\]
the resulting four-generator zonotope is a **nonregular rhombic dodecahedron** having the same volume and circumradius as the regular one. Thus regular rhombic dodecahedra are not the unique minimizers of circumradius at fixed volume, answering negatively the uniqueness question posed as Problem 1 by Joós and Lángi [1]. The existence of nearby common-shift perturbations is suggested by a related construction already in [1]; the distinct assertion here is the complete necessary-and-sufficient equality region.

## Assumptions and scope

All segments are Euclidean, the ambient dimension is exactly three, and \(Z\) has nonempty interior. A generator \(p_i\) means \(Z=\sum_{i=1}^4[0,p_i]\) up to translation; a vanishing extra generator is permitted when the minimal number is below four. Individual changes \(p_i\mapsto-p_i\) change \(Z\) only by translation. The circumradius is the radius of the unique minimum enclosing Euclidean ball. The classification includes boundary configurations where some triple determinants vanish. To require the usual generic rhombic-dodecahedral combinatorial type, use the subfamily with \(-v\in\operatorname{int}T_R\), which has all four triple determinants nonzero.

The representation of equality sets is not asserted to be one-to-one: orthogonal changes of frame, generator permutations, and sign choices can describe the same zonotope. It is, however, complete modulo these harmless redundancies. No statement is made about zonotopes requiring five or more generators.

## Proof

**1. Orient the four generators by a positive dependence.** Because the \(3\)-by-\(4\) generator matrix has a nonzero kernel vector, sign changes of the generators make the nonzero kernel coefficients nonnegative. After normalization there exist \(\lambda_i\ge0\) with \(\sum_i\lambda_i=1\) and \(\sum_i\lambda_i p_i=0\). Thus \(0\in S:=\operatorname{conv}\{p_1,p_2,p_3,p_4\}\). Since the generators span \(\mathbb R^3\), this is a nondegenerate tetrahedron, possibly with \(0\) on its boundary.

The standard zonotope volume identity [1,2], and the tetrahedron decomposition into the tetrahedra \(\operatorname{conv}\{0,p_i,p_j,p_k\}\), give
\[
\operatorname{Vol}_3(Z)
=\sum_{i<j<k}|\det(p_i,p_j,p_k)|
=|\det(p_1-p_4,p_2-p_4,p_3-p_4)|.
\]
The identity remains true if the origin is on a face, because then some component tetrahedra have zero volume.

**2. Orthogonal signed-sum factorization.** Define the three balanced signed sums
\[
\begin{aligned}
w_1&=p_1+p_2-p_3-p_4,\\
w_2&=p_1-p_2+p_3-p_4,\\
w_3&=p_1-p_2-p_3+p_4.
\end{aligned}
\]
A direct column operation gives
\[
\operatorname{Vol}_3(Z)=\frac14|\det(w_1,w_2,w_3)|.
\]
The centered translate \(Z-\tfrac12\sum_i p_i\) consists of all \(\tfrac12\sum_i t_i p_i\) with \(-1\le t_i\le1\). Its circumradius is \(\tfrac12\max_{\varepsilon_i\in\{-1,1\}}\|\sum_i\varepsilon_i p_i\|\), because central symmetry forces its circumcenter to be the origin. In particular \(\|w_j\|\le2R\) for each \(j\). Hadamard's inequality therefore yields
\[
\operatorname{Vol}_3(Z)
\le \frac14\prod_{j=1}^3\|w_j\|
\le \frac14(2R)^3=2R^3.
\]
Equality in this chain holds **exactly** when the three \(w_j\) are pairwise perpendicular and each has length \(2R\). This gives an intrinsic test for extremality after the positive-dependence orientation.

**3. Invert the equality conditions.** In an equality case, write \(w_j=2Re_j\) in an orthonormal frame (allowing an orientation-reversing frame). Let \(v=\tfrac14\sum_i p_i\). Inverting the three signed-sum definitions gives \(p_i=q_i+v\) for the displayed regular-tetrahedron vectors \(q_i\). The positivity of the kernel in step 1 is exactly \(-v\in T_R\).

All sixteen signed sums of four vectors occur in complementary pairs. Six have two plus signs and two minus signs, forming three complementary pairs; these give the three \(w_j\), each producing a zonotope half-sum of norm \(R\). The all-plus sign gives half-sum \(2v\). The four signs with exactly one negative generator give the half-sums \(v-q_i\). Consequently
\[
\operatorname{cr}\left(\sum_i[0,q_i+v]\right)
=\max\left\{R,\ 2\|v\|,\ \max_i\|v-q_i\|\right\}.
\]
Necessity of the inequalities defining \(\Omega_R\) follows. Conversely, any \(v\in\Omega_R\) has \(\operatorname{cr}(Z)=R\) by this formula; and since \(-v\in T_R\), the tetrahedral decomposition of step 1 applies. Translation of all four tetrahedral vertices by \(v\) leaves its volume unchanged, and the determinant formula gives \(\operatorname{Vol}_3(Z)=2R^3\). This proves the if-and-only-if classification for all four-generator full-dimensional zonotopes.

The four face planes of \(T_R\) have equations \(\langle q_i,x\rangle=-R^2/4\), with the tetrahedron lying on the greater-than side; substituting \(x=-v\) proves the stated linear form of its containment condition.

**4. Explicit genuinely nonregular equality bodies.** Each \(q_i\) has norm \(\sqrt3R/2\), and \(T_R\) contains the ball centered at the origin with radius \(R/(2\sqrt3)\). Hence \(\|v\|<R(1-\sqrt3/2)\) implies \(2\|v\|<R\), \(\|v-q_i\|<R\) for every \(i\), and \(-v\in\operatorname{int}T_R\); the last assertion holds because \(1-\sqrt3/2<1/(2\sqrt3)\). These are genuine rhombic dodecahedra, not combinatorial degenerations.

If all four generator lengths \(\|q_i+v\|\) were equal, subtraction of their squared norms would imply \(\langle q_i-q_j,v\rangle=0\) for every pair \(i,j\). The differences span \(\mathbb R^3\), forcing \(v=0\). Every nonzero vector in the displayed open ball therefore produces unequal edge lengths and hence a nonregular polyhedron. The equal-radius, equal-volume family has three free real parameters modulo finite tetrahedral symmetry.

## Verification

A fully rational example fixes \(R=2\) and
\[
(q_1,q_2,q_3,q_4)=((1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)),
\qquad v=(1/10,0,0).
\]
The constraints defining \(\Omega_2\) hold. The four squared generator lengths are \(321/100,321/100,281/100,281/100\); the three balanced sums are \((4,0,0),(0,4,0),(0,0,4)\). Direct determinant enumeration gives \(\operatorname{Vol}_3(Z)=16\), and the sixteen signed half-sums have maximal squared norm exactly \(4\). Thus \(R=2\) and \(V=2R^3\), although the generators have unequal lengths.

The supplied standalone standard-library Python program `verify.py` performs the exact rational witness calculations, checks the signed-minor orientation identity, and tests the inequality on 4,000 seeded rational four-generator examples. These finite checks reproduce the algebraic identities and a nonregular counterexample; the universal conclusions follow from the complete analytic proof above, not from sampling.

## Relationship to prior work

Joós and Lángi [1] proved the sharp extremal circumradius inequality for zonotopes generated by dimension-plus-one segments and explicitly posed uniqueness of the regular rhombic dodecahedron at fixed volume (Problem 1). Their Section 3.2 also makes the important related observation that a sufficiently small common translation of the generators of an odd-dimensional regular-simplex zonotope preserves its circumradius; they use this to discuss a **different**, mean-width-normalized optimization. The present argument does not claim that construction, the volume identity, or the sharp inequality as novel. It classifies *all* equality geometries in dimension three via a necessary-and-sufficient compact parameter set and shows exactly how the published uniqueness question fails.

Lángi [3] discusses the geometry and mean-width isoperimetry of spatial parallelohedra, rather than circumradius equality for arbitrary four-segment zonotopes. Bezdek [4] establishes inradius-normalized lower bounds for intrinsic volumes of four-generator zonotopes, not the present fixed-circumradius equality set. Its six-page original paper was inspected in full; an unindexed equivalent characterization elsewhere remains a historical-priority risk.

## Limitations

The classification is specific to three-dimensional zonotopes with four or fewer generators; no higher-dimensional version or stability estimate is proved. The feasible set is explicit through inequalities but is not additionally parameterized by a list of congruence-orbit fundamental domains. Sources with alternative terminology or an unindexed equality characterization could affect historical priority. No independent external validation has been performed.

## References

[1] A. Joós and Z. Lángi, *Isoperimetric problems for zonotopes*, arXiv:2206.03204 (initial public posting June 7, 2022); *Mathematika* **69** (2023), 508–534, doi:10.1112/mtk.12191, especially Sections 2, 3.1, 3.2 and 5 (Problem 1).

[2] G. C. Shephard, *Combinatorial properties of associated zonotopes*, *Canadian Journal of Mathematics* **26** (1974), 302–321. Cited for the classical volume decomposition.

[3] Z. Lángi, *An isoperimetric problem for three-dimensional parallelohedra*, arXiv:2102.11621 (initial public posting February 23, 2021); *Pacific Journal of Mathematics* **316** (2022), 169–181.

[4] K. Bezdek, *On rhombic dodecahedra*, *Beiträge zur Algebra und Geometrie* **41** (2000), 411–416. Full original six-page text inspected.
