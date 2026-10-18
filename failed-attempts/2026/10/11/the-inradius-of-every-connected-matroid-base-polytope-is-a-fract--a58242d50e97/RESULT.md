# The inradius of every connected matroid base polytope is a fractional-partition ratio
## Finding
Let \(M\) be a connected matroid of rank \(k\) on a ground set \(E\) of size \(n\ge2\), and let
\[
B(M)=\operatorname{conv}\{\mathbf 1_B:B\text{ is a basis of }M\}
\]
be its base polytope, equipped with the intrinsic Euclidean metric of the affine hyperplane
\[
H_k=\{x\in\mathbb R^E:x(E)=k\}.
\]

For every nonempty proper subset \(S\subsetneq E\), define
\[
c(S)=
\left\|
\mathbf 1_S-\frac{|S|}{n}\mathbf 1_E
\right\|_2
=
\sqrt{\frac{|S|(n-|S|)}{n}}.
\]
Call a family
\[
\lambda=(\lambda_S)_{\varnothing\ne S\subsetneq E}
\]
a fractional partition of \(E\) when
\[
\lambda_S\ge0
\quad\text{and}\quad
\sum_{S\ni e}\lambda_S=1
\quad\text{for every }e\in E.
\]
Write \(\mathcal F(E)\) for the compact polytope of all such families. Then the intrinsic Euclidean inradius of \(B(M)\) is
\[
\boxed{
\rho(B(M))
=
\min_{\lambda\in\mathcal F(E)}
\frac{
\displaystyle
\sum_{\varnothing\ne S\subsetneq E}
\lambda_S\operatorname{rk}_M(S)-k
}{
\displaystyle
\sum_{\varnothing\ne S\subsetneq E}
\lambda_Sc(S)
}.
}
\tag{1}
\]

Moreover, the complete set of Chebyshev centers is
\[
\boxed{
\mathcal C(M)=
\left\{
x\in H_k:
x(S)\le
\operatorname{rk}_M(S)-\rho(B(M))c(S)
\text{ for every }\varnothing\ne S\subsetneq E
\right\}.
}
\tag{2}
\]

Thus the largest intrinsic Euclidean ball problem for every connected matroid base polytope is exactly a finite optimization involving only the rank function and the cardinalities of subsets.

For the uniform matroid \(U_{k,n}\), formula (1) specializes to
\[
\rho(B(U_{k,n}))
=
\frac{\min\{k,n-k\}}{\sqrt{n(n-1)}},
\]
the intrinsic inradius of the hypersimplex.

## Assumptions and scope
Connectedness is in the matroid sense. For \(n\ge2\), a connected matroid has no loops or coloops and its base polytope has intrinsic dimension \(n-1\), so its inradius in \(H_k\) is positive.

All subset sums use
\[
x(S)=\sum_{e\in S}x_e.
\]
The fractional partitions in (1) range over all nonempty proper subsets. No claim is made that an optimizer must use only flats or only facet-defining subsets, although redundant rank inequalities can be removed computationally.

The metric is intrinsic: distances are measured inside \(H_k\), not in a coordinate chart obtained by deleting one coordinate.

## Proof
Edmonds' rank-inequality description of a matroid base polytope gives
\[
B(M)=
\left\{
x\in H_k:
x(S)\le\operatorname{rk}_M(S)
\text{ for every }\varnothing\ne S\subsetneq E
\right\}.
\tag{3}
\]

Let
\[
H_0=\{y\in\mathbb R^E:y(E)=0\}
\]
be the translation space of \(H_k\). The ambient normal \(\mathbf 1_S\) of the inequality indexed by \(S\) projects orthogonally to
\[
p_S=
\mathbf 1_S-\frac{|S|}{n}\mathbf 1_E\in H_0,
\]
and therefore its intrinsic norm is
\[
\|p_S\|_2=c(S).
\tag{4}
\]

Consequently, for \(x\in H_k\) and \(t\ge0\), the intrinsic Euclidean ball of radius \(t\) centered at \(x\) lies in \(B(M)\) if and only if
\[
x(S)+t\,c(S)\le\operatorname{rk}_M(S)
\qquad
\text{for every }\varnothing\ne S\subsetneq E.
\tag{5}
\]
Indeed, \(t\,c(S)\) is exactly the maximum of the linear functional \(y\mapsto y(S)\) on the radius-\(t\) ball in \(H_0\).

Hence the inradius is the optimum of the finite linear program
\[
\begin{aligned}
\text{maximize}\quad &t\\
\text{subject to}\quad
&x(S)+t\,c(S)\le\operatorname{rk}_M(S)
&&(\varnothing\ne S\subsetneq E),\\
&x(E)=k,\\
&t\ge0.
\end{aligned}
\tag{6}
\]

Introduce nonnegative dual variables \(\mu_S\) for the inequalities and a free multiplier for \(x(E)=k\). Eliminating the free multiplier gives a scalar \(q\) such that the dual constraints are
\[
\sum_{S\ni e}\mu_S=q
\qquad(e\in E),
\tag{7}
\]
together with
\[
\sum_S\mu_Sc(S)\ge1.
\tag{8}
\]
The dual objective is
\[
\sum_S\mu_S\operatorname{rk}_M(S)-qk.
\tag{9}
\]

Any dual feasible point has \(q>0\): if \(q=0\), then (7) and nonnegativity force all \(\mu_S=0\), contradicting (8). Thus
\[
\lambda_S=\frac{\mu_S}{q}
\]
is a fractional partition of \(E\).

Conversely, every fractional partition \(\lambda\) and every \(q>0\) with
\[
q\sum_S\lambda_Sc(S)\ge1
\]
produce a dual feasible point by \(\mu_S=q\lambda_S\). For any basis \(B\) of \(M\),
\[
\sum_S\lambda_S\operatorname{rk}_M(S)
\ge
\sum_S\lambda_S|B\cap S|
=
\sum_{e\in B}\sum_{S\ni e}\lambda_S
=
k,
\tag{10}
\]
so the numerator in (1) is nonnegative. Since \(M\) is connected, \(B(M)\) is full-dimensional in \(H_k\) and has positive inradius; strong linear-programming duality therefore makes the optimal numerator strictly positive and forces (8) to be tight at an optimum.

For a fixed fractional partition \(\lambda\), the optimal scaling is consequently
\[
q=
\frac1{\sum_S\lambda_Sc(S)}.
\]
Substitution into (9), followed by strong duality between (6) and its dual, gives exactly (1).

Finally, a point \(x\in H_k\) is a center of an intrinsic ball of radius \(\rho(B(M))\) precisely when it satisfies (5) at \(t=\rho(B(M))\). This is exactly the set in (2), proving the complete center description.

For \(U_{k,n}\), the hypersimplex has the intrinsic facet pairs
\[
x_e\ge0,
\qquad
x_e\le1.
\]
At its symmetric center \(x_e=k/n\), their distances are respectively
\[
\frac{k}{\sqrt{n(n-1)}}
\quad\text{and}\quad
\frac{n-k}{\sqrt{n(n-1)}}.
\]
Their minimum gives the stated uniform-matroid specialization.

## Verification
The proof is symbolic and applies to arbitrary connected matroids; no finite enumeration is used as an infinite proof.

The critical geometric step was checked directly: after restricting to the affine hull \(H_k\), the rank-inequality normal is the orthogonal projection
\[
\mathbf 1_S-\frac{|S|}{n}\mathbf 1_E,
\]
whose squared norm is
\[
|S|-\frac{|S|^2}{n}
=
\frac{|S|(n-|S|)}{n}.
\]

The dual was independently reconstructed from (6). The free center coordinates impose the equal element-cover constraints (7), while the nonnegative radius variable imposes (8). Normalizing by their common element-cover value is what produces fractional partitions.

As boundary checks, the formula is positive exactly in the full-dimensional connected setting used here, and its uniform-matroid specialization agrees with the direct distances from the barycenter to the hypersimplex facets.

## Relationship to prior work
The modern matroid-polytope literature records two structural inputs used here: connectedness gives full intrinsic dimension \(n-1\), and matroid base polytopes admit the rank-inequality description (3). Ferroni's work on Ehrhart positivity studies connected matroid base polytopes geometrically but not their Euclidean Chebyshev radius. Joswig and Schröter give a detailed facet treatment of matroid polytopes and hypersimplices, including the connected dimension formula and rank-flat inequalities.

A separate line of matroid optimization studies strength, fractional arboricity, principal partitions, and optimization over the base polytope. That theory is related in spirit because partitions and rank deficits appear there, but its objective is different: it does not provide the intrinsic Euclidean largest-ball formula (1), the geometric weights \(c(S)\), or the complete center set (2).

Targeted searches using matroid base polytope, Chebyshev center, inradius, Euclidean radius, fractional partitions, strength, and hypersimplex formulations did not locate a theorem implying (1) or (2). This search evidence is not a formal global novelty certificate; residual literature risks are stated below.

## Limitations
Formula (1) is a finite convex-geometric characterization, not a closed form in a small number of standard matroid invariants. The number of subset variables is exponential before redundant inequalities are removed.

The theorem is stated for connected matroids. A disconnected matroid base polytope has a lower-dimensional affine hull determined by its components; applying the same method there requires projecting normals to that smaller translation space and leads to a component-dependent formula not claimed here.

The originality comparison cannot exclude an equivalent linear-programming dual hidden in general polyhedral-optimization literature or a differently normalized result in older matroid-strength literature.

## References
1. Luis Ferroni, *Matroids are not Ehrhart positive*, arXiv:2105.04465, first public version 2021-05-10; Advances in Mathematics 402 (2022), 108337, DOI 10.1016/j.aim.2022.108337.
2. Michael Joswig and Benjamin Schröter, *Matroids from hypersimplex splits*, Journal of Combinatorial Theory, Series A 151 (2017), 254–284, DOI 10.1016/j.jcta.2017.05.001.
3. Huy Truong and Pietro Poggi-Corradini, *Base Modulus for Matroid Truncation, Strength, and Fractional Arboricity*, arXiv:2604.11946.
