# Fixed-point singularity saturation in fence Hibi toric varieties
## Finding
For an integer \(n\ge1\), let \(F_n\) be the fence poset on \(x_1,\ldots,x_n\) with cover relations
\[
x_i<x_{i+1}\quad\text{for odd }i,
\qquad
x_i>x_{i+1}\quad\text{for even }i.
\]
Let \(X_n\) be the projective toric variety of the order polytope \(\mathcal O(F_n)\); equivalently, \(X_n\) is the projective Hibi toric variety associated with the distributive lattice of order ideals of \(F_n\).

Write \(E_n\) for the Euler zigzag number, normalized by
\[
\sec z+\tan z=\sum_{n\ge0}E_n\frac{z^n}{n!},
\]
and write \(F_j^{\mathrm{Fib}}\) for Fibonacci numbers with
\[
F_1^{\mathrm{Fib}}=F_2^{\mathrm{Fib}}=1.
\]
Then
\[
\boxed{\deg X_n=E_n}
\]
and
\[
\boxed{\chi_{\mathrm{top}}(X_n)=F_{n+2}^{\mathrm{Fib}}.}
\]

The fixed-point singularities have a strikingly rigid form. For \(n=1,2\), every torus fixed point is smooth. For every \(n\ge3\), exactly four torus fixed points are smooth. Under the lattice-affine identification with the chain polytope, these four points are indexed by
\[
\varnothing,\qquad \{1\},\qquad \{n\},\qquad \{1,n\}.
\]
Consequently, for \(n\ge3\),
\[
\boxed{\#\{\text{singular torus fixed points of }X_n\}=F_{n+2}^{\mathrm{Fib}}-4.}
\]
In particular, the proportion of torus fixed points that are smooth tends to zero.

There is also an exact degree--Euler crossover:
\[
\deg X_n<\chi_{\mathrm{top}}(X_n)
\quad(1\le n\le4),
\]
while
\[
\boxed{\deg X_n>\chi_{\mathrm{top}}(X_n)\quad(n\ge5).}
\]
Equality never occurs.

## Assumptions and scope
The base field for the algebraic variety is \(\mathbb C\). The projective toric variety is taken with the lattice polarization coming from the order polytope. The claim concerns ordinary topological Euler characteristic and smoothness of torus fixed points; it does not assert that the singular locus itself is zero-dimensional.

The fence has height one: there is no chain of three distinct elements. Therefore its comparability graph is the path on \(n\) vertices.

## Proof
Stanley's order-polytope triangulation gives normalized volume equal to the number of linear extensions of the poset. For the fence, a linear extension is equivalent to an alternating permutation, so the normalized volume is the Euler zigzag number \(E_n\). The projective degree of the toric variety of a lattice polytope is its normalized lattice volume. Hence
\[
\deg X_n=E_n.
\]

A complete projective toric variety decomposes into torus orbits. Every positive-dimensional orbit is isomorphic to a product containing \(\mathbb C^*\), hence has compactly supported Euler characteristic zero. Thus its Euler characteristic is the number of zero-dimensional torus orbits, equivalently the number of vertices of the defining polytope.

Vertices of an order polytope are indicator functions of order filters, and filters are equinumerous with order ideals. In any finite poset an ideal is determined by its maximal antichain. For a fence, because its comparability graph is a path, antichains are exactly independent sets of that path. The number of independent sets of a path on \(n\) vertices is \(F_{n+2}^{\mathrm{Fib}}\). Therefore
\[
\chi_{\mathrm{top}}(X_n)=F_{n+2}^{\mathrm{Fib}}.
\]

To analyze fixed-point smoothness, use Stanley's lattice-affine equivalence between the order polytope and chain polytope for posets of length at most one. For the fence the chain polytope is the stable-set polytope of the path:
\[
\mathcal C(F_n)=\left\{y\in\mathbb R^n:
 y_i\ge0,\ y_i+y_{i+1}\le1\ (1\le i<n)\right\}.
\]
Its vertices are the incidence vectors \(v_S\) of independent sets \(S\subseteq\{1,\ldots,n\}\).

At \(v_S\), the active facets are the coordinate facets \(y_j=0\) for \(j\notin S\), together with one edge facet \(y_i+y_{i+1}=1\) for every path edge incident to a vertex in \(S\). Since \(S\) is independent, their number is
\[
n-|S|+\sum_{i\in S}\deg_{P_n}(i)
=n+\sum_{i\in S}(\deg_{P_n}(i)-1).
\]
A selected interior vertex has degree two and therefore forces more than \(n\) active facets, so the polytope is not simple there and the corresponding toric fixed point is singular.

If \(S\) contains no interior vertex, then for \(n\ge3\) it is one of
\[
\varnothing,\ \{1\},\ \{n\},\ \{1,n\}.
\]
At each of these vertices exactly \(n\) facets are active. Their primitive facet normals form a unimodular basis: for \(S=\varnothing\) they are the coordinate basis; for \(S=\{1\}\) or \(\{n\}\) one endpoint coordinate normal is replaced by \(e_1+e_2\) or \(e_{n-1}+e_n\); and for \(S=\{1,n\}\) both replacements occur. Elementary column subtraction reduces each matrix to the identity. Thus precisely these fixed points are smooth. The low cases \(n=1,2\) are respectively a segment and a triangle, so all fixed points are smooth.

For the degree--Euler comparison, the first values are
\[
(E_1,E_2,E_3,E_4,E_5,E_6)=(1,1,2,5,16,61)
\]
and
\[
(F_3^{\mathrm{Fib}},F_4^{\mathrm{Fib}},F_5^{\mathrm{Fib}},F_6^{\mathrm{Fib}},F_7^{\mathrm{Fib}},F_8^{\mathrm{Fib}})=(2,3,5,8,13,21).
\]
Hence the crossover occurs between \(n=4\) and \(n=5\).

It remains to propagate the strict inequality. From
\[
A(z)=\sec z+\tan z
\]
one has
\[
A'(z)=\frac{A(z)^2+1}{2}.
\]
For \(n\ge2\), taking the coefficient of \(z^{n+1}\) gives the lower bound
\[
E_{n+2}\ge(n+1)E_n.
\]
Also
\[
F_{n+4}^{\mathrm{Fib}}
=2F_{n+2}^{\mathrm{Fib}}+F_{n+1}^{\mathrm{Fib}}
<3F_{n+2}^{\mathrm{Fib}}.
\]
Thus if \(n\ge5\) and \(E_n>F_{n+2}^{\mathrm{Fib}}\), then
\[
E_{n+2}\ge(n+1)E_n
>6F_{n+2}^{\mathrm{Fib}}
>F_{n+4}^{\mathrm{Fib}}.
\]
The bases \(n=5,6\) prove the claim for both parities.

## Verification
The bundled checker constructs the fence relation directly. For \(1\le n\le9\) it exhaustively enumerates permutations to count linear extensions and subsets to count ideals, independently confirming the Euler-zigzag and Fibonacci formulas.

It also enumerates every independent-set vertex of the chain polytope for \(1\le n\le16\), counts its active facets, and checks the asserted smooth fixed-point classification. For the four smooth families it computes the determinant of the active primitive-normal matrix and verifies absolute determinant one.

Finally, it generates Euler zigzag and Fibonacci numbers through \(n=100\), checks the degree--Euler crossover, and verifies the two-step inequality used in the proof. These finite computations are regression evidence only.

## Relationship to prior work
Lakshmibai and Mukherjee study singular loci of Hibi toric varieties and explicitly define them as toric varieties associated to finite distributive lattices. Their archival record is classified primarily under MSC \(14M15\). Their paper does not specialize to the fence family and targeted full-text searches found no occurrence of the fence, Euler characteristic, or linear-extension comparison used here.

Stanley's *Two Poset Polytopes* proves that order-polytope vertices are filters, normalized volume is the number of linear extensions divided by \(n!\), and specifically identifies linear extensions of the \(n\)-element fence with alternating permutations. It does not formulate the associated projective toric fixed-point smoothness classification or the degree--Euler crossover.

The accepted statement combines the order-polytope/Hibi correspondence with a local unimodularity analysis of every path stable-set vertex. Targeted literature and semantic searches for fence Hibi varieties, order-polytope toric singularities, smooth fixed points, and the Fibonacci/Euler-zigzag comparison did not locate an equivalent theorem.

## Limitations
The theorem classifies smoothness only at torus fixed points. Positive-dimensional torus orbits can also lie in the singular locus, and no complete decomposition of the singular locus into irreducible components is claimed.

The fence is the alternating path poset. More general fences with longer monotone segments, arbitrary tree posets, and cyclic analogues can have different local cones.

The global degree and Euler formulas individually follow from classical order-polytope facts; the new content assessed here is the uniform fixed-point smoothness classification together with the exact infinite-family crossover. Because that local argument is elementary once the chain-polytope model is chosen, an unindexed folklore observation remains a residual originality risk.

## References
V. Lakshmibai and H. Mukherjee, *Singular Loci of Hibi toric varieties*, arXiv:0706.2686, first submitted 18 June 2007; *Journal of the Ramanujan Mathematical Society* 26 (2011), 1--29.

Richard P. Stanley, *Two Poset Polytopes*, *Discrete & Computational Geometry* 1 (1986), 9--23, DOI 10.1007/BF02187680.
