# Rank alone determines the Euclidean inradius of generalized snake order polytopes
## Finding
Let
\[
w=w_0w_1\cdots w_n
\]
be a generalized snake word of length
\[
n\ge0,
\]
and let
\[
P(w)
\]
be the generalized snake poset introduced by von Bell, Braun, Hanely, Serhiyenko, Vega, Vindas-Meléndez, and Yip.

The source proves that \(P(w)\) has a unique minimum, a unique maximum, and rank
\[
h=n+2.
\tag{1}
\]
Consider its standard order polytope
\[
\mathcal O(P(w))
=
\left\{
x\in[0,1]^{P(w)}:
x_p\le x_q
\text{ whenever }p<q
\right\}.
\tag{2}
\]

With the standard Euclidean metric in the source coordinates,
\[
\boxed{
r_{\mathrm{in}}\bigl(\mathcal O(P(w))\bigr)
=
\frac{1}{2+(n+2)\sqrt2}.
}
\tag{3}
\]

Thus the Euclidean inradius depends only on the rank and is completely independent of the generalized snake word. This sharply contrasts with the normalized volume: the source proves that, at fixed rank, the snake and ladder words are the two volume extremals.

There is also an explicit incenter. For each element \(p\in P(w)\), let
\[
\ell(p)
\]
be the maximum number of cover relations in a saturated chain from the unique minimum to \(p\). Put
\[
r_n=\frac{1}{2+(n+2)\sqrt2}.
\tag{4}
\]
Then
\[
\boxed{
c_p=r_n\bigl(1+\sqrt2\,\ell(p)\bigr)
}
\tag{5}
\]
defines an incenter of \(\mathcal O(P(w))\).

## Assumptions and scope
The generalized snake poset is exactly the recursive family from the cited source. The word length is \(n\), and the source rank is \(n+2\).

The metric is the ordinary Euclidean metric of the coordinate realization (2). The statement is not affine invariant.

The result determines the inradius and supplies one explicit incenter. It does not assert uniqueness of the incenter, nor does it determine the complete incenter locus, circumradius, or John ellipsoid.

## Proof
Write
\[
h=n+2
\]
and
\[
r=\frac{1}{2+h\sqrt2}.
\tag{6}
\]

The order-polytope inequalities are
\[
0\le x_p\le1
\]
for every element \(p\), together with
\[
x_p\le x_q
\]
whenever \(p<q\). It is enough to check coordinate inequalities and cover inequalities, since all other order inequalities follow by transitivity.

Let \(p_{\min}\) and \(p_{\max}\) be the unique minimum and maximum of \(P(w)\). The source rank \(h\) means that a longest saturated chain has \(h\) cover steps. Because the minimum and maximum are unique, a longest chain extends from \(p_{\min}\) to \(p_{\max}\). Hence
\[
\ell(p_{\min})=0,
\qquad
\ell(p_{\max})=h.
\tag{7}
\]

Define \(c\) by (5). For every element \(p\),
\[
0\le\ell(p)\le h,
\]
so
\[
c_p\ge r
\tag{8}
\]
and
\[
1-c_p
\ge
1-r(1+h\sqrt2)
=
r.
\tag{9}
\]
Thus the Euclidean distance from \(c\) to every coordinate hyperplane
\[
x_p=0
\quad\text{or}\quad
x_p=1
\]
is at least \(r\).

If
\[
p\lessdot q
\]
is a cover relation, any saturated chain realizing \(\ell(p)\) can be extended by this cover, so
\[
\ell(q)\ge\ell(p)+1.
\]
Therefore
\[
c_q-c_p
\ge
r\sqrt2.
\tag{10}
\]
The normal to the hyperplane
\[
x_p=x_q
\]
has Euclidean norm \(\sqrt2\), so (10) says that the distance from \(c\) to every cover hyperplane is at least \(r\).

Consequently the closed radius-\(r\) Euclidean ball centered at \(c\) is contained in every defining halfspace of the order polytope. Hence
\[
r_{\mathrm{in}}\bigl(\mathcal O(P(w))\bigr)\ge r.
\tag{11}
\]

For the reverse inequality, choose a longest saturated chain
\[
p_0\lessdot p_1\lessdot\cdots\lessdot p_h
\]
from the unique minimum to the unique maximum. Suppose a Euclidean ball of radius \(\rho\), centered at \(z\), is contained in the order polytope. Its distances to the two endpoint coordinate hyperplanes and the \(h\) cover hyperplanes along this chain give
\[
z_{p_0}\ge\rho,
\tag{12}
\]
\[
z_{p_{j+1}}-z_{p_j}\ge\rho\sqrt2
\qquad
(0\le j<h),
\tag{13}
\]
and
\[
1-z_{p_h}\ge\rho.
\tag{14}
\]
Adding (12)--(14) telescopes:
\[
1
\ge
\rho\bigl(2+h\sqrt2\bigr).
\]
Thus
\[
\rho\le\frac{1}{2+h\sqrt2}=r.
\tag{15}
\]
Together with (11), this proves (3).

## Verification
The proof is symbolic and valid for every generalized snake word.

The source-dependent structural facts were checked directly in the full text and page image: generalized snake posets are recursively constructed width-two distributive lattices with unique minimum, unique maximum, and rank \(n+2\), and the paper uses the standard order-polytope realization (2).

The accompanying `verify.py` reconstructs every generalized snake poset for all words of length at most \(8\). It verifies the source rank, computes every longest-path level \(\ell(p)\), checks every coordinate and cover distance for the center (5), and checks the telescoping upper bound on a longest chain. These finite tests are corroborative only.

## Relationship to prior work
The primary paper studies normalized volumes, circuits, triangulations, flips, and regular triangulations of order polytopes of generalized snake posets. In particular, it proves that among generalized snake posets of a fixed rank, the snake and ladder examples minimize and maximize normalized volume.

The inradius behaves in the opposite way: it does not distinguish any words at fixed rank. Formula (3) shows that the entire volume interval collapses to one Euclidean inradius value.

Stanley's classical order-polytope theory supplies the general coordinate realization and its relation to posets. The present claim is specifically about the generalized snake family introduced in 2021 and the rank rigidity that follows for its Euclidean inradius.

Targeted searches for “generalized snake poset”, “order polytope”, “inradius”, “Chebyshev center”, “rank”, “height”, and “longest chain” did not locate a statement implying (3) or the explicit center (5).

## Limitations
The formula is realization-dependent: a non-orthogonal affine image of an order polytope need not have the same Euclidean inradius.

No uniqueness statement is made for the incenter. The construction (5) gives one optimal center, while other centers may exist in posets with branching.

The metric proof uses only the chain and cover inequalities once the generalized snake rank is known. Accordingly, an equivalent observation may exist in general order-polytope folklore under Chebyshev-center terminology; this is the principal residual originality risk.

## References
1. Matias von Bell, Benjamin Braun, Derek Hanely, Khrystyna Serhiyenko, Julianne Vega, Andrés R. Vindas-Meléndez, and Martha Yip, *Triangulations, Order Polytopes, and Generalized Snake Posets*, arXiv:2102.11306, first public version 2021-02-22; Combinatorial Theory 2 (2022), no. 3, article 10, DOI 10.5070/C62359166.
2. Richard P. Stanley, *Two poset polytopes*, Discrete & Computational Geometry 1 (1986), 9--23.
