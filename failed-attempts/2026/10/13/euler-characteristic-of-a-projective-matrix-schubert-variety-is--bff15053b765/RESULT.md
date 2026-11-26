# Euler characteristic of a projective matrix Schubert variety is a prefix-minimum statistic
## Finding
Let
\[
w\in S_n.
\]
Write
\[
r_w(i,j)
=
\#\{k\le j:w(k)\le i\},
\qquad
1\le i,j\le n.
\]
Let
\[
X_w
\subset
\operatorname{Mat}_{n\times n}(\mathbb C)
\]
be the matrix Schubert variety defined by the northwest rank conditions
\[
\operatorname{rank}(Z_{[1,i],[1,j]})
\le
r_w(i,j)
\]
for all \(i,j\), and let
\[
\mathbb P X_w
\subset
\mathbb P^{n^2-1}
\]
be its projectivization.

Define the prefix minima
\[
m_j
=
\min\{w(1),\ldots,w(j)\}.
\]

Then
\[
\boxed{
\chi_{\mathrm{top}}(\mathbb P X_w)
=
\sum_{j=1}^{n}(n-m_j+1).
}
\]

Equivalently,
\[
\boxed{
\chi_{\mathrm{top}}(\mathbb P X_w)
=
\#\{(i,j):r_w(i,j)>0\}.
}
\]

Thus ordinary Euler characteristic forgets almost all of the permutation and remembers only its left-to-right minima.

Moreover,
\[
\boxed{
\frac{n(n+1)}2
\le
\chi_{\mathrm{top}}(\mathbb P X_w)
\le
n^2.
}
\]
The minimum is attained uniquely by the long permutation
\[
w_0=n\cdots21,
\]
and the maximum is attained exactly by the permutations satisfying
\[
w(1)=1.
\]

For example,
\[
w=132
\]
defines the matrix Schubert variety whose northwest \(2\times2\) block is singular, yet
\[
\chi_{\mathrm{top}}(\mathbb P X_{132})=9,
\]
the Euler characteristic of the whole ambient
\[
\mathbb P^8.
\]

## Assumptions and scope
The base field is \(\mathbb C\).

The rank-matrix convention is
\[
r_w(i,j)
=
\operatorname{rank}\bigl((w^{\mathsf T})_{[1,i],[1,j]}\bigr)
=
\#\{k\le j:w(k)\le i\}.
\]

The affine matrix Schubert variety is a cone because its defining minors are homogeneous. Its projectivization is nonempty.

No smoothness assumption is used.

## Proof
Choose integers
\[
a_i=2^i,
\qquad
b_j=2^{n+j}.
\]
Let
\[
\mathbb C^*
\]
act on matrix coordinates by
\[
z\cdot Z_{ij}
=
z^{a_i+b_j}Z_{ij}.
\]

Matrix Schubert varieties are invariant under independent row and column rescaling. The weights
\[
a_i+b_j
\]
are pairwise distinct, because their binary expansions have one nonzero digit among the \(a\)-positions and one among the \(b\)-positions.

Therefore the fixed locus of the ambient projective space consists exactly of the coordinate points
\[
[E_{ij}],
\]
and the fixed locus of
\[
\mathbb P X_w
\]
is the subset of those coordinate points satisfying the Schubert rank conditions.

Fix \(E_{ij}\). Its northwest \(p\times q\) submatrix has rank zero unless
\[
p\ge i
\quad\text{and}\quad
q\ge j,
\]
and has rank one when both inequalities hold.

Since
\[
r_w(p,q)
\]
is weakly increasing in both variables, \(E_{ij}\in X_w\) if and only if
\[
r_w(i,j)\ge1.
\]
This is equivalent to the existence of some \(k\le j\) with \(w(k)\le i\), hence to
\[
m_j\le i.
\]

Thus the surviving coordinate points in column \(j\) are exactly
\[
E_{m_j,j},
E_{m_j+1,j},
\ldots,
E_{n,j},
\]
so their number is
\[
n-m_j+1.
\]

For any complex algebraic variety \(Y\) with an algebraic
\[
\mathbb C^*
\]
action,
\[
\chi_c(Y)=\chi_c(Y^{\mathbb C^*}).
\]
Applying this to the projective variety \(\mathbb P X_w\) gives
\[
\chi_{\mathrm{top}}(\mathbb P X_w)
=
\sum_{j=1}^{n}(n-m_j+1).
\]

Among the first \(j\) entries of a permutation,
\[
m_j\le n-j+1,
\]
so
\[
n-m_j+1\ge j.
\]
Summing gives the lower bound. Equality for every \(j\) forces
\[
w=n\cdots21.
\]

The upper bound follows from
\[
m_j\ge1.
\]
Equality in every summand means \(m_j=1\) for every \(j\), equivalent to
\[
w(1)=1.
\]

## Verification
The bundled checker enumerates every permutation for
\[
1\le n\le7.
\]

For each permutation it constructs the full rank matrix directly, tests every coordinate matrix against every northwest rank condition, and compares the resulting fixed-point count with the prefix-minimum formula.

It also verifies the sharp lower and upper bounds and their equality cases across the complete permutation census.

These finite computations are regression evidence only. The all-\(n\) theorem follows from the symbolic fixed-point argument and the elementary prefix-minimum inequalities.

## Relationship to prior work
Knutson and Miller study matrix Schubert varieties through their determinantal ideals, multidegrees, Hilbert series, Gröbner bases, pipe dreams, and Cohen--Macaulay degenerations. Their full text records the northwest-rank description and row-column rescaling symmetry used here.

Later work on diagonal degenerations continues to study Gröbner bases, liaison, and bumpless-pipe-dream models of the same varieties.

The inspected sources do not state the ordinary topological Euler characteristic of the projectivized matrix Schubert variety, nor the prefix-minimum formula or its extremal classification.

## Limitations
Euler characteristic is very coarse. Permutations with the same prefix-minimum sequence have the same value even when their matrix Schubert varieties have different dimensions, degrees, singularities, and Gröbner geometry.

The result concerns the projectivization of the affine matrix Schubert cone. It does not compute the Euler characteristic of the associated Schubert variety in a flag variety.

The torus-localization proof is short, so an older or unindexed observation remains a residual novelty risk.

## References
Allen Knutson and Ezra Miller, *Gröbner geometry of Schubert polynomials*, arXiv:math/0110058, first submitted 5 October 2001; *Annals of Mathematics* 161 (2005), 1245--1318.

Patricia Klein, *Diagonal degenerations of matrix Schubert varieties*, *Algebraic Combinatorics* 6 (2023), 1073--1094, DOI 10.5802/alco.296.
