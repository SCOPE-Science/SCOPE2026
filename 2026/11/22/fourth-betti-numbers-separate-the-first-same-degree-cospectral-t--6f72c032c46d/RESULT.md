# Fourth Betti numbers separate the first same-degree cospectral trees

## Finding

For every finite simple graph \(G\) let \(\mathfrak n_G\) be its Dani–Mainkar two-step nilpotent rational Lie algebra, with one generator \(X_v\) per vertex and one central generator \(Z_{uv}\) per edge, and nonzero brackets \([X_u,X_v]=Z_{uv}\) for \(u<v\) joined by an edge. Its rational structure constants permit a compact nilmanifold \(M_G\); its real de Rham Betti numbers are the dimensions of the Chevalley–Eilenberg cohomology of \(\mathfrak n_G\).

Among **all nonisomorphic trees of at most nine vertices**, the smallest size at which two trees share both their adjacency characteristic polynomial and their *sorted degree sequence* is nine. Up to tree isomorphism, **exactly two pairs** occur at that size. In each pair, the associated seventeen-dimensional nilmanifolds have identical Betti numbers in degrees zero through three, yet their fourth Betti numbers differ by one.

The four trees are specified unambiguously by the following edge lists on vertex set \(\{0,1,\ldots,8\}\), with each pair written \((u,v)\), \(u<v\):

- \(A_1\): `[(0,1),(1,2),(2,3),(3,4),(4,5),(4,7),(5,6),(5,8)]`.
- \(A_2\): `[(0,1),(1,2),(2,3),(2,5),(3,4),(5,6),(6,7),(6,8)]`.
- \(B_1\): `[(0,1),(0,8),(1,2),(2,3),(2,5),(2,6),(3,4),(3,7)]`.
- \(B_2\): `[(0,1),(1,2),(2,3),(2,5),(3,4),(5,6),(5,7),(5,8)]`.

The spectral and cohomological profiles are:

| Tree | Sorted vertex degrees | Matching numbers \((m_0,\ldots,m_4)\) | \((b_0,b_1,b_2,b_3,b_4)\) |
|---|---|---|---|
| \(A_1\) | \((1,1,1,1,2,2,2,3,3)\) | \((1,8,19,14,2)\) | \((1,9,53,201,593)\) |
| \(A_2\) | \((1,1,1,1,2,2,2,3,3)\) | \((1,8,19,14,2)\) | \((1,9,53,201,594)\) |
| \(B_1\) | \((1,1,1,1,1,2,2,3,4)\) | \((1,8,17,10,0)\) | \((1,9,55,210,632)\) |
| \(B_2\) | \((1,1,1,1,1,2,2,3,4)\) | \((1,8,17,10,0)\) | \((1,9,55,210,633)\) |

For the first pair, the adjacency characteristic polynomial is \(t(t^2-1)(t^6-7t^4+12t^2-2)\); for the second it is \(t^3(t^2-1)(t^2-2)(t^2-5)\).

## Assumptions and scope

The graph is finite, simple, undirected, and the Lie algebra uses the *unweighted* graph bracket above, with other brackets zero. The compact quotient uses any lattice of the simply connected real Lie group with this rational Lie algebra; by Nomizu's theorem, its real Betti numbers depend only on the Lie algebra. This is ordinary **de Rham** cohomology; no integral cohomology or homotopy classification is asserted. All computations use exact rational arithmetic and zero-based vertex labels only for describing concrete witnesses. The exhaustive minimality statement is within all unlabeled trees of orders one through nine, not all graphs.

## Proof

**1. Exhaustive tree and spectrum classification.** Every tree on \(k+1\) vertices is obtained by deleting a leaf from a tree on \(k\) vertices and conversely attaching a new leaf to some vertex of that smaller tree. Starting from the singleton, the included checker performs every such attachment and retains one representative per isomorphism class, identified by the standard canonical rooted-parenthesis code after repeatedly removing leaves to find tree centers. Root codes sort child codes recursively; taking the lexicographically smaller of the one or two center-rooted codes is complete for unrooted tree isomorphism. Thus induction proves no tree is omitted or counted twice. The numbers for orders one through nine are exactly \(1,1,1,2,3,6,11,23,47\).

For each tree, the checker counts every matching by scanning all subsets of its \(k-1\) edges and rejecting subsets with incident edges. The adjacency characteristic polynomial of a tree equals its matching polynomial,
\[
\chi_G(t)=\sum_{j\ge0}(-1)^j m_j(G)t^{|V(G)|-2j};
\]
this follows from the usual leaf deletion recurrence for both polynomials, initialized on the empty and singleton forests. Sorted degree lists are determined directly from the edges. Grouping the exhaustive isomorphism-class representatives by this pair of invariants produces no collisions through order eight, and exactly the two groups displayed above at order nine. This establishes the spectral/degree statements and their minimality.

**2. Cohomological differential and finite exact rank calculation.** Let \(x_v\) and \(z_{uv}\) denote the dual degree-one generators in the Chevalley–Eilenberg exterior algebra. Up to a harmless simultaneous sign convention, the coboundary is the degree-one derivation
\[
 d x_v=0,\qquad d z_{uv}=x_u\wedge x_v.
\]
There are nine vertex generators and eight edge generators, hence seventeen in all. In cochain degree \(k\), the basis comprises the \(\binom{17}{k}\) ordered exterior monomials in these generators. Replacing each edge form by its two endpoints, with the ordinary exterior Leibniz sign, completely specifies the integer differential matrices. In particular \(d^2=0\): it vanishes on generators and the derivation rule propagates this identity to every wedge monomial.

For a monomial, define its **vertex support** as the union of its vertex-form indices and all endpoints of its edge forms. The differential preserves this vertex support. Accordingly every cochain degree splits into independent vertex-support blocks, and matrix ranks add over those blocks. Within each block, the included program computes the row rank by exact Gaussian elimination with Python's `fractions.Fraction`. It computes all five coboundary ranks, through \(d:C^4\to C^5\), as

| Tree | \(\operatorname{rank}d_0\) | \(\operatorname{rank}d_1\) | \(\operatorname{rank}d_2\) | \(\operatorname{rank}d_3\) | \(\operatorname{rank}d_4\) |
|---|---:|---:|---:|---:|---:|
| \(A_1\) | 0 | 8 | 75 | 404 | 1383 |
| \(A_2\) | 0 | 8 | 75 | 404 | 1382 |
| \(B_1\) | 0 | 8 | 73 | 397 | 1351 |
| \(B_2\) | 0 | 8 | 73 | 397 | 1350 |

**3. Betti numbers.** Exactness of the cohomology definition gives, with \(\operatorname{rank}d_{-1}=0\),
\[
 b_k(M_G)=\binom{17}{k}-\operatorname{rank}d_k-\operatorname{rank}d_{k-1}.
\]
For example \(b_4(M_{A_1})=\binom{17}{4}-1383-404=593\) and \(b_4(M_{A_2})=\binom{17}{4}-1382-404=594\). Similarly the second pair gives \(632\) and \(633\). Substitution at all lower degrees yields the table in the finding. Nomizu's theorem identifies these Lie-algebra cohomology dimensions with real de Rham Betti numbers of the compact nilmanifolds. This proves the statement.

## Verification

Run `python3 check.py` using Python 3 (standard library only). The program regenerates all unlabeled trees up to nine vertices, enumerates all matching polynomials and sorted degree lists, verifies the two pair memberships and minimality, and constructs each exact support-preserving Chevalley–Eilenberg differential. It checks \(d^2=0\) explicitly on every exterior monomial of degrees zero through three, computes rational ranks, and independently compares every rank with a full-matrix modular row reduction over the prime field of order \(1000003\). The rational ranks—not the modular ranks—establish the real Betti numbers. The actual output is included in `CERTIFICATE.txt`. All checks completed successfully.

## Relationship to prior work

Aldi, Bevins, Chatzitheodoridis, Da Silva, Frias and Mejía Gómez compute and study the Poincaré polynomials of **path-graph** nilmanifolds (arXiv:2611.17014, first public version 12 November 2026). The pairs above are branching trees, not paths, so the path formulas do not determine their fourth cohomology. The preceding work of Aldi, Butler, Gardiner, Grandini, Lichtenwalner and Pan (arXiv:2402.14188) supplies the graph Lie-algebra cochain formalism, canonical decomposition, a general third-degree formula and all-degree star formulas. This calculation uses that structure, but identifies an exact same-degree cospectral separation in degree four not stated in the accessible source material. The distinction is between specific Betti invariants and graph spectra, not merely the already known fact that nonisomorphic graphs can produce nonisomorphic Lie algebras.

## Limitations

The exhaustive minimality concerns the combined adjacency characteristic polynomial and degree multiset among **trees**, not the adjacency spectrum alone or arbitrary graphs. The result separates the fourth rational/real Betti numbers, not integral cohomology or other geometric features. Exact computational enumeration is a finite proof only because every finite tree of bounded order is generated and checked; the result does not extrapolate an infinite classification. Priority against unindexed work and inaccessible portions of related literature is not certified, and no independent mathematical audit has been performed.

## References

1. Marco Aldi, Samuel Bevins, Eleftherios Chatzitheodoridis, Sergio Da Silva, Quincy Frias, Tomás Mejía Gómez, *Poincaré polynomials of nilmanifolds associated with path graphs*, arXiv:2611.17014, first submitted 2026-11-12, https://arxiv.org/abs/2611.17014.
2. Marco Aldi, Andrew Butler, Jordan Gardiner, Daniele Grandini, Monica Lichtenwalner, Kevin Pan, *On the cohomology of Lie algebras associated with graphs*, arXiv:2402.14188, https://arxiv.org/abs/2402.14188; Journal of Pure and Applied Algebra 229 (2025), 107838, https://doi.org/10.1016/j.jpaa.2024.107838.
3. Katsumi Nomizu, *On the cohomology of compact homogeneous spaces of nilpotent Lie groups*, Annals of Mathematics 59 (1954), 531–538. (For the standard identification of de Rham and Lie-algebra cohomology.)
