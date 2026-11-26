# Determinant and permanent Fano schemes have the same Euler characteristic
## Finding
Let
\[
2\le r\le m\le n
\]
and let
\[
1\le k\le mn-1.
\]
Write
\[
D^r_{m,n}\subset\mathbb P^{mn-1}
\]
for the determinantal variety defined by the \(r\times r\) minors of a generic \(m\times n\) matrix, and write
\[
P^r_{m,n}\subset\mathbb P^{mn-1}
\]
for the variety defined by its \(r\times r\) permanents.

Let
\[
F_k(D^r_{m,n})
\quad\text{and}\quad
F_k(P^r_{m,n})
\]
be their Fano schemes of projective \(k\)-planes. For \(q\ge0\), let
\[
B_{m,n,r}(q)
\]
denote the number of labeled \(q\)-edge subgraphs of the complete bipartite graph \(K_{m,n}\) having matching number less than \(r\).

Then
\[
\boxed{
\chi_{\mathrm{top}}\!\left(F_k(D^r_{m,n})\right)
=
\chi_{\mathrm{top}}\!\left(F_k(P^r_{m,n})\right)
=
B_{m,n,r}(k+1).
}
\]

Thus the determinantal and permanental Fano schemes have identical ordinary Euler characteristic for every parameter choice, even though their scheme geometry can differ substantially.

The extremal matching bound gives
\[
B_{m,n,r}(q)=0
\qquad\text{for}\qquad
q>(r-1)n,
\]
so in particular
\[
\boxed{
\chi_{\mathrm{top}}\!\left(F_k(D^r_{m,n})\right)
=
\chi_{\mathrm{top}}\!\left(F_k(P^r_{m,n})\right)=0
\quad\text{if}\quad
k\ge(r-1)n.
}
\]

For \(r=2\) and \(k\ge1\), every admissible edge set is a star with a unique center. Hence
\[
\boxed{
\chi_{\mathrm{top}}
=
m\binom{n}{k+1}+n\binom{m}{k+1}.
}
\]
Here binomial coefficients outside their usual range are interpreted as zero.

## Assumptions and scope
The base field is \(\mathbb C\). Ordinary topological Euler characteristic means the Euler characteristic of the underlying complex-analytic topological space, so nilpotent scheme structure does not affect the invariant.

The theorem concerns positive-dimensional linear spaces, namely \(k\ge1\). This separates it from the base determinantal and permanental varieties themselves.

The graph \(K_{m,n}\) is labeled by the row and column indices of the generic matrix. A coordinate \(k\)-plane in \(\mathbb P^{mn-1}\) therefore corresponds to a set of exactly \(k+1\) matrix entries, equivalently an edge set of cardinality \(k+1\).

## Proof
Let
\[
T=(\mathbb C^*)^m\times(\mathbb C^*)^n
\]
act on the generic matrix by independent row and column rescaling. Both the determinantal and permanental ideals are stable under this action.

Choose a generic one-parameter subgroup
\[
\lambda:\mathbb C^*\longrightarrow T
\]
so that all \(mn\) matrix-coordinate weights are distinct. The induced fixed points on the ambient Grassmannian
\[
\operatorname{Gr}(k+1,mn)
\]
are then precisely its coordinate points, that is, the \((k+1)\)-dimensional coordinate subspaces of the matrix-coordinate vector space.

Associate to such a coordinate subspace \(Q\) its bipartite graph
\[
G_Q\subset K_{m,n},
\]
whose edges are the selected matrix entries. Chan and Ilten prove that the following are equivalent for a coordinate point \(Q\):

\[
Q\in F_k(D^r_{m,n}),
\]
\[
Q\in F_k(P^r_{m,n}),
\]
and
\[
G_Q\text{ has no matching of size }r.
\]

The equivalence can also be seen directly at the coordinate level. An \(r\times r\) determinant or permanent restricts nontrivially to a coordinate subspace exactly when its selected entries contain the support of a permutation monomial, which is exactly a matching of size \(r\).

Therefore the two Fano schemes have exactly the same finite \(\mathbb C^*\)-fixed set, and its cardinality is
\[
B_{m,n,r}(k+1).
\]

For any complex algebraic variety \(X\) with an algebraic \(\mathbb C^*\)-action,
\[
\chi_c(X)=\chi_c(X^{\mathbb C^*}).
\]
Both Fano schemes are projective, so
\[
\chi_{\mathrm{top}}(X)=\chi_c(X).
\]
Their fixed loci are finite, hence their Euler characteristics equal the common fixed-point count. This proves the main formula.

Finally, a bipartite graph on parts of sizes \(m\le n\) with matching number at most \(r-1\) has at most
\[
(r-1)n
\]
edges. This gives the vanishing range.

When \(r=2\), a graph with at least two edges and matching number one must have all its edges incident to one common vertex. For \(q=k+1\ge2\), stars centered on the \(m\)-side contribute
\[
m\binom nq,
\]
while stars centered on the \(n\)-side contribute
\[
n\binom mq.
\]
Their centers are unique, so the two families are disjoint and the displayed closed formula follows.

## Verification
The bundled checker independently enumerates edge subsets of small complete bipartite graphs.

For every tested edge set, it computes the bipartite matching number by exhaustive dynamic programming. Independently, it searches every \(r\)-row and \(r\)-column block for a permutation support contained in the selected entries. The two predicates agree in every tested case.

The checker then groups the surviving edge sets by cardinality and verifies:

\[
\#\{E:|E|=k+1,\ \nu(E)<r\}
=
B_{m,n,r}(k+1),
\]
the extremal vanishing threshold, and the explicit star formula when \(r=2\).

These finite computations are regression evidence only. The theorem for arbitrary parameters follows from the torus-fixed-point classification and Euler localization above.

## Relationship to prior work
Chan and Ilten introduce and study the Fano schemes of determinantal and permanental varieties. Their paper analyzes compression spaces, irreducible components, dimensions, smoothness, connectedness, and torus-fixed coordinate points. Proposition 2.3 gives the decisive shared fixed-point criterion: a coordinate point belongs to either Fano scheme exactly when its bipartite graph has no matching of size \(r\).

The inspected full text does not state the resulting ordinary Euler-characteristic equality, and targeted searches found no Poincaré-polynomial, Betti-number, or topological Euler formula for these Fano schemes.

The common fixed-point set is stronger than a superficial analogy between determinant and permanent equations. It shows that one coarse global topological invariant is exactly preserved across the two families for all \((m,n,r,k)\), and identifies that invariant with a classical finite matching-avoidance count.

Earlier determinantal geometry gives rich information about rank loci and their resolutions, but that does not imply the Euler characteristic of the parameter space of contained projective linear spaces. Likewise, the known component descriptions of these Fano schemes do not by themselves force the determinant and permanent families to have equal Euler characteristic.

## Limitations
Euler characteristic is coarse. Equality of Euler characteristics does not imply isomorphism, equal numbers of components, equal Betti numbers, equal motives, reducedness, or equal singularity structure.

The formula reduces the invariant to the finite number \(B_{m,n,r}(k+1)\), but no closed expression for that graph count is claimed for general \(r\). The case \(r=2\) is included because it simplifies uniformly to a star count.

The proof is short once the common torus-fixed-point description is combined with Euler localization, so an equivalent unindexed or folklore observation remains a residual originality risk.

## References
Melody Chan and Nathan Ilten, *Fano schemes of determinants and permanents*, arXiv:1312.2577, first submitted 9 December 2013; *Algebra & Number Theory* 9 (2015), no. 3, 629--679, DOI 10.2140/ant.2015.9.629.
