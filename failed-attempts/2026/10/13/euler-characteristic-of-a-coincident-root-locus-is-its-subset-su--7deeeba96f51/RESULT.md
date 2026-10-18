# Euler characteristic of a coincident root locus is its subset-sum count
## Finding
Let
\[
\lambda=(\lambda_1,\ldots,\lambda_e)
\]
be a partition of
\[
d\ge1,
\qquad
\lambda_i\ge1,
\qquad
\sum_{i=1}^{e}\lambda_i=d.
\]
Let
\[
\Delta_\lambda
\subset
\mathbb P(\operatorname{Sym}^d\mathbb C^2)
\]
be the projective coincident root locus consisting of binary forms that admit a factorization
\[
F=\prod_{i=1}^{e}L_i^{\lambda_i}
\]
for linear forms \(L_i\).

Define the set of distinct subset sums
\[
\Sigma(\lambda)
=
\left\{
\sum_{i\in I}\lambda_i:
I\subseteq\{1,\ldots,e\}
\right\}.
\]

Then
\[
\boxed{
\chi_{\mathrm{top}}(\Delta_\lambda)
=
|\Sigma(\lambda)|.
}
\]

In particular,
\[
\chi_{\mathrm{top}}(\Delta_\lambda)\le d+1.
\]
After sorting the parts as
\[
a_1\le a_2\le\cdots\le a_e,
\]
one has
\[
\boxed{
\chi_{\mathrm{top}}(\Delta_\lambda)=d+1
}
\]
if and only if
\[
\boxed{
a_1=1
\quad\text{and}\quad
a_j\le1+\sum_{i<j}a_i
\quad
(2\le j\le e).
}
\]

Thus a proper multiple-root locus can have exactly the same Euler characteristic as the ambient projective space. For example,
\[
\lambda=(2,1)
\]
gives the discriminant surface of binary cubics and
\[
\chi_{\mathrm{top}}(\Delta_{(2,1)})=4
=
\chi_{\mathrm{top}}(\mathbb P^3).
\]

At the opposite extreme,
\[
\lambda=(d)
\]
gives the rational normal curve and
\[
\chi_{\mathrm{top}}(\Delta_{(d)})=2.
\]

## Assumptions and scope
The base field is \(\mathbb C\).

The locus \(\Delta_\lambda\) is the closed projective image of the standard multiplication parameterization associated with the partition \(\lambda\). Repeated parts of \(\lambda\) are allowed.

The subset-sum set counts distinct integers, not subsets with multiplicity. Distinct assignments of the roots \(x\) and \(y\) may yield the same monomial fixed point when the corresponding submultisets of parts have the same total.

The theorem concerns ordinary topological Euler characteristic. Projectivity permits the use of compactly supported Euler characteristic in the localization argument without changing the invariant.

## Proof
Choose homogeneous coordinates \(x,y\) on \(\mathbb C^2\), and let
\[
\mathbb C^*
\]
act by
\[
z\cdot x=zx,
\qquad
z\cdot y=y.
\]

On
\[
\mathbb P(\operatorname{Sym}^d\mathbb C^2),
\]
the monomials
\[
x^{d-s}y^s,
\qquad
0\le s\le d,
\]
have pairwise distinct weights. Hence the ambient fixed locus consists exactly of the \(d+1\) monomial coordinate points
\[
[x^{d-s}y^s].
\]

The coincident root locus is invariant under the induced action. Suppose first that
\[
s\in\Sigma(\lambda).
\]
Choose
\[
I\subseteq\{1,\ldots,e\}
\]
such that
\[
s=\sum_{i\in I}\lambda_i.
\]
Set
\[
L_i=y
\quad(i\in I),
\qquad
L_i=x
\quad(i\notin I).
\]
Then
\[
\prod_{i=1}^{e}L_i^{\lambda_i}
=
x^{d-s}y^s,
\]
so the corresponding monomial point belongs to \(\Delta_\lambda\).

Conversely, if
\[
x^{d-s}y^s
=
c\prod_{i=1}^{e}L_i^{\lambda_i}
\]
for a nonzero scalar \(c\), unique factorization in
\[
\mathbb C[x,y]
\]
forces every \(L_i\) to be proportional to either \(x\) or \(y\). Hence \(s\) is the sum of precisely those parts attached to factors proportional to \(y\), so
\[
s\in\Sigma(\lambda).
\]

Therefore
\[
(\Delta_\lambda)^{\mathbb C^*}
=
\left\{
[x^{d-s}y^s]:
s\in\Sigma(\lambda)
\right\},
\]
a reduced finite set of cardinality
\[
|\Sigma(\lambda)|.
\]

For any complex algebraic variety \(Y\) with an algebraic \(\mathbb C^*\)-action,
\[
\chi_c(Y)=\chi_c(Y^{\mathbb C^*}).
\]
Indeed, remove the fixed locus and apply a finite Rosenlicht stratification to the complement. After refinement by stabilizer type, each nonfixed piece is a Zariski-locally-trivial bundle whose fiber is a finite quotient of \(\mathbb C^*\), hence isomorphic to \(\mathbb C^*\). Since
\[
\chi_c(\mathbb C^*)=0,
\]
all nonfixed pieces contribute zero.

Applying this to projective \(\Delta_\lambda\) yields
\[
\chi_{\mathrm{top}}(\Delta_\lambda)
=
|\Sigma(\lambda)|.
\]

Since
\[
\Sigma(\lambda)\subseteq\{0,1,\ldots,d\},
\]
the ambient value \(d+1\) occurs exactly when every integer from \(0\) through \(d\) is a subset sum.

Sort the parts:
\[
a_1\le\cdots\le a_e.
\]
If the first \(j-1\) parts generate every integer from \(0\) through
\[
S_{j-1}=\sum_{i<j}a_i,
\]
then adding \(a_j\) gives the second interval
\[
[a_j,a_j+S_{j-1}].
\]
The two intervals have no gap exactly when
\[
a_j\le S_{j-1}+1.
\]
Starting with \(a_1=1\) proves sufficiency by induction. Conversely, if \(a_1>1\), then \(1\) is missing; and if the first failed inequality is
\[
a_j>S_{j-1}+1,
\]
then \(S_{j-1}+1\) cannot be formed. This proves the equality criterion.

## Verification
The bundled checker enumerates every integer partition for
\[
1\le d\le30.
\]

For each partition it computes the distinct subset-sum set by exact dynamic programming. It independently tests every monomial exponent
\[
0\le s\le d
\]
against exhaustive subset enumeration for
\[
1\le d\le18.
\]

It also verifies the complete-sequence criterion for equality with the ambient Euler characteristic.

These finite computations are regression evidence only. The all-parameter theorem follows from unique factorization, torus fixed-point localization, and the interval-induction subset-sum criterion.

## Relationship to prior work
Coincident root loci are classical projective varieties of binary forms with prescribed root multiplicities. Chipalkatti gives a projective parameterization by products of symmetric powers and studies their equations and singularities. Fehér, Némethi, and Rimányi compute equivariant Poincaré duals and study quotient cohomology. Lee and Sturmfels study conormal varieties, duality, degree, and Euclidean-distance geometry.

Those sources provide the geometric object and substantially finer algebraic or equivariant information, but the inspected texts do not state the ordinary Euler characteristic of an arbitrary coincident root locus as the distinct subset-sum count of its partition.

The formula is qualitatively different from Hilbert's projective degree formula: projective degree depends multiplicatively on the parts and their repetition multiplicities, whereas Euler characteristic depends only on which additive subset sums collide.

## Limitations
Euler characteristic is coarse. Two partitions with the same subset-sum cardinality can define geometrically very different loci.

The theorem does not determine Betti numbers, intersection cohomology, singularity type, or the cohomology of the open exact-root-multiplicity stratum.

The proof is short after combining the classical projective multiple-root locus with torus localization, so an older or unindexed observation under discriminant-stratum terminology remains a residual novelty risk.

## References
Jaydeep V. Chipalkatti, *On equations defining coincident root loci*, arXiv:math/0110224, first submitted 19 October 2001; *Journal of Algebra* 267 (2003), 246--271.

L. M. Fehér, A. Némethi, and R. Rimányi, *Coincident root loci of binary forms*, arXiv:math/0311312, first submitted 18 November 2003; *Michigan Mathematical Journal* 54 (2006), 375--392.

Hwangrae Lee and Bernd Sturmfels, *Duality of Multiple Root Loci*, arXiv:1508.00202, first submitted 2 August 2015; *Journal of Algebra* 446 (2016), 499--526.

Alejandro González Nevado and Ettore Teixeira Turatti, *Binary forms of suprageneric rank and the multiple root loci*, arXiv:2007.03335, first submitted 7 July 2020; *Communications in Algebra* 52 (2024), 466--472.
