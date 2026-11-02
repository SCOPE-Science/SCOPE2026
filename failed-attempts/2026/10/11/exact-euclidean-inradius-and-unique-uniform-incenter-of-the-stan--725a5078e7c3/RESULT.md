# Exact Euclidean inradius and unique uniform incenter of the standard stellohedron
## Finding
For \(n\ge2\), let \(K_{1,n}\) be the star graph on vertices
\[
\{0,1,\ldots,n\},
\]
with center \(0\) and leaves \(1,\ldots,n\). Consider the standard stellohedron realization
\[
\operatorname{St}_n
=
\operatorname{Assoc}(K_{1,n})
=
\sum_{\emptyset\ne S\subseteq[n]}
\Delta_{\{0\}\cup S}
\subset\mathbb R^{n+1},
\tag{1}
\]
where \(\Delta_T=\operatorname{conv}\{e_i:i\in T\}\).

There are
\[
M_n=2^n-1
\]
summands in (1), so
\[
\operatorname{St}_n
\subset
H_n=
\left\{
x\in\mathbb R^{n+1}:
\sum_{i=0}^n x_i=M_n
\right\}.
\]
Equip \(H_n\) with its intrinsic Euclidean metric.

Then
\[
\boxed{
r_{\mathrm{in}}(\operatorname{St}_n)
=
\frac{2^n-1}{\sqrt{n(n+1)}}.
}
\tag{2}
\]
The incenter is unique and equals
\[
\boxed{
c_n=
\frac{2^n-1}{n+1}\mathbf1.
}
\tag{3}
\]

For \(n\ge3\), the maximal ball centered at \(c_n\) is tangent exactly to the \(n+1\) singleton-tube facets
\[
x_i=0
\qquad
(0\le i\le n).
\tag{4}
\]
For \(n=2\), \(\operatorname{St}_2\) is a pentagon and all five facets are tangent to its maximal inscribed circle.

The total number of facets is
\[
2^n+n-1,
\]
so for \(n\ge3\) the inradius is controlled by only \(n+1\) of exponentially many facets.

## Assumptions and scope
The realization in (1) is the standard graph-associahedron realization used in the cited literature. Some authors add the singleton simplices \(\Delta_{\{i\}}\) to the Minkowski sum. Doing so merely translates the polytope by \(\mathbf1\), so the inradius and tangency classification are unchanged, while the incenter is translated by the same vector.

A tube of the star is either a singleton or a subset containing the center. Proper tubes index the facets. The theorem concerns intrinsic Euclidean distance in the affine hull \(H_n\); it is not a statement about arbitrary affinely equivalent realizations.

## Proof
Every summand \(\Delta_{\{0\}\cup S}\) in (1) lies in the simplex hyperplane where its coordinate sum is \(1\). Hence every point of the Minkowski sum has total coordinate sum
\[
M_n=2^n-1.
\]

For any subset \(T\subseteq\{0,\ldots,n\}\), each summand contributes at least \(1\) to \(x(T)\) exactly when its vertex set is contained in \(T\), and contributes at least \(0\) otherwise. Thus the standard generalized-permutohedron inequalities give
\[
x(T)\ge z(T),
\tag{5}
\]
where \(z(T)\) is the number of summands in (1) contained in \(T\).

For a singleton \(T=\{i\}\),
\[
z(T)=0.
\tag{6}
\]
For a center-containing tube \(T\) of cardinality \(k\ge2\),
\[
z(T)=2^{k-1}-1,
\tag{7}
\]
because the summands contained in \(T\) are indexed by the nonempty subsets of its \(k-1\) leaves.

The published facet description of the stellohedron says that the proper center-containing subsets together with the leaf singletons are exactly the facets. In particular, all \(n+1\) singleton inequalities
\[
x_i\ge0
\tag{8}
\]
are facets.

Let a Euclidean ball of radius \(r\), centered at \(c\in H_n\), lie in \(\operatorname{St}_n\). Inside the tangent space
\[
\mathbf1^\perp,
\]
the intrinsic normal to the singleton hyperplane \(x_i=0\) is
\[
e_i-\frac1{n+1}\mathbf1,
\]
whose squared norm is
\[
\frac{n}{n+1}.
\tag{9}
\]
Therefore every singleton facet requires
\[
c_i
\ge
r\sqrt{\frac{n}{n+1}}.
\tag{10}
\]
Summing (10) over all \(n+1\) coordinates and using
\[
\sum_i c_i=M_n
\]
gives the universal bound
\[
r
\le
\frac{M_n}{\sqrt{n(n+1)}}.
\tag{11}
\]
Moreover, equality in (11) forces equality in every inequality (10), hence forces
\[
c_i=\frac{M_n}{n+1}
\]
for all \(i\). Thus any ball attaining the bound has the unique possible center \(c_n\) from (3).

It remains to prove that the ball centered at \(c_n\) with radius equal to the right-hand side of (11) satisfies every other facet inequality.

Let \(T\) be a proper center-containing tube of cardinality
\[
1\le k\le n.
\]
For \(k=1\), this is the center singleton and its distance is already the value in (2). Assume \(k\ge2\). The intrinsic projection of \(\mathbf1_T\) to \(\mathbf1^\perp\) has squared norm
\[
\frac{k(n+1-k)}{n+1}.
\tag{12}
\]
Using (7), the slack of the uniform center in the \(T\)-facet is
\[
s_{n,k}
=
\frac{k(2^n-1)}{n+1}
-
(2^{k-1}-1).
\tag{13}
\]
Hence its distance to that facet is
\[
d_{n,k}
=
\frac{s_{n,k}}
{\sqrt{k(n+1-k)/(n+1)}}.
\tag{14}
\]

Set
\[
N=n+1,
\qquad
F(j)=\frac{2^{j-1}-1}{j(j-1)}
\quad(j\ge2).
\]
A direct calculation gives
\[
F(j+1)-F(j)
=
\frac{(j-3)2^{j-1}+2}
{j(j-1)(j+1)}
\ge0.
\tag{15}
\]
Thus \(F\) is nondecreasing. For \(2\le k<N\),
\[
\frac{2^{k-1}-1}{k(k-1)}
\le
\frac{2^{N-1}-1}{N(N-1)},
\]
or equivalently
\[
N(N-1)(2^{k-1}-1)
\le
k(k-1)(2^{N-1}-1).
\tag{16}
\]
After division and rearrangement, (16) says
\[
k-
\frac{N(2^{k-1}-1)}{2^{N-1}-1}
\ge
\frac{k(N-k)}{N-1}.
\tag{17}
\]
Also
\[
\frac{k(N-k)}{N-1}\ge1,
\tag{18}
\]
because
\[
k(N-k)-(N-1)
=
(k-1)(N-k-1)\ge0.
\]
For a number at least \(1\), its value is at least its square root. Combining (17)--(18) yields
\[
k-
\frac{N(2^{k-1}-1)}{2^{N-1}-1}
\ge
\sqrt{\frac{k(N-k)}{N-1}}.
\tag{19}
\]
Equation (19) is exactly the inequality
\[
d_{n,k}
\ge
\frac{2^n-1}{\sqrt{n(n+1)}}.
\]
Thus the candidate ball is contained in every facet halfspace, proving (2)--(3).

For the equality cases, \(F(2)=F(3)\), while (15) is strict thereafter. Also equality in (18) for \(k\ge2\) occurs only at \(k=N-1\). Therefore a non-singleton proper tube can satisfy equality in (19) only when
\[
N=3,\qquad k=2.
\]
This is precisely the two-dimensional stellohedron. Hence for \(n\ge3\) only singleton facets are tangent, while for \(n=2\) the two size-\(2\) center-containing facets join the three singleton facets, giving all five facets.

## Verification
The proof is symbolic and covers every \(n\ge2\). The two nonstandard ingredients are independently visible in the cited full texts: the standard star-graph-associahedron realization as a Minkowski sum of coordinate simplices, and the exhaustive stellohedron facet indexing by proper center-containing subsets plus leaf singletons.

The accompanying `verify.py` checks, for \(2\le n\le100\), the exact integer inequality (16), the numerical facet distances (14), the inradius formula, and the exceptional equality pattern at \(n=2\). It is a corroborative replay only and does not replace the arbitrary-dimensional proof.

## Relationship to prior work
Baralić, Ivanović, and Petrić describe the facets of the \(n\)-dimensional stellohedron exactly as the proper subsets containing the star center together with the leaf singletons. Their work studies facet chromatic numbers and does not state a Euclidean inradius or Chebyshev-center theorem.

Behrend recalls the standard realization
\[
\operatorname{Assoc}(K_{1,n})
=
\sum_{\emptyset\ne S\subseteq[n]}
\Delta_{\{0\}\cup S}
\]
and notes that partial permutohedra in a certain parameter range are combinatorially equivalent to stellohedra. Combinatorial equivalence does not preserve Euclidean inradius. In particular, a previously studied partial-permutohedron realization uses different Minkowski coefficients and a different ambient realization, so its metric formula does not imply (2).

Targeted searches for “stellohedron inradius”, “star graph associahedron inradius”, “stellohedron Chebyshev center”, “largest inscribed ball”, and the characteristic closed form in (2) did not locate a covering theorem. The directly inspected stellohedron sources contain no occurrence of “inradius” or “Chebyshev”; the exact-realization source also contains no occurrence of “radius”.

## Limitations
The theorem is realization-specific. Other stellohedron realizations with the same face lattice can have different Euclidean inradii and different incenters.

The claim concerns only the inradius, incenter, and inball-contact facets. It does not determine the circumradius, John ellipsoid, or other norm-dependent invariants.

The literature comparison leaves a residual risk that the short metric consequence of the standard nestohedron inequalities appears as folklore or under a broader generalized-permutohedron Chebyshev-center theorem not exposed by the searches.

## References
1. Đorđe Baralić, Jelena S. Ivanović, and Zoran Petrić, *Chromatic numbers for facet colouring of some generalised associahedra*, arXiv:2311.05901, first public version 2023-11-10; Discrete Applied Mathematics 358 (2024), 272--284, DOI 10.1016/j.dam.2024.07.013.
2. Roger E. Behrend, *Ehrhart polynomials of partial permutohedra*, arXiv:2403.06975, first public version 2024-03-11.
