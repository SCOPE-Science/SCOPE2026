# The integral equivariant homology of dicyclic abelian-coset complexes

## Finding

For every integer \(n\ge2\), let \(G=\operatorname{Dic}_n\) be the dicyclic group of order \(4n\). Let \(\mathcal P(G)\) be the poset of left cosets of all abelian subgroups of \(G\), ordered by inclusion, and let \(X_n=|\mathcal P(G)|\), with its canonical left-translation action. Put \(A=\langle x\rangle\), let \(\varepsilon:G\to\{\pm1\}\) equal \(+1\) on \(A\) and \(-1\) outside \(A\), and let
\[
\mathcal E_n=\coprod_{i=0}^{n-1}G/\langle x^iy\rangle.
\]
There is a \(G\)-equivariant homotopy equivalence from \(X_n\) to the complete bipartite graph \(K_{2,n^2}\), where the two vertices on one side form \(G/A\), and the other side is \(\mathcal E_n\); all possible edges occur. In particular, as an **integral \(\mathbb Z[G]\)-module**, there is an isomorphism
\[
\boxed{H_1(X_n;\mathbb Z)\cong\mathbb Z_\varepsilon\otimes\ker\bigl(\mathbb Z[\mathcal E_n]\xrightarrow{\sum}\mathbb Z\bigr).}
\]
Here \(\mathbb Z_\varepsilon\) denotes the sign lattice, and the tensor factor uses the diagonal action. All reduced homology outside degree one vanishes. The resulting ordinary character is
\[
\chi(g)=\begin{cases}
 n^2-1,&g\in\{1,x^n\},\\
 -1,&g\in A\setminus\{1,x^n\},\\
 1-n,&g\notin A.
\end{cases}
\]
Further, the ordinary orbit space \(X_n/G\) is contractible. The rank \(n^2-1\) of first homology was established previously; the assertion here is the full integral equivariant structure, explicit graph model with its action, resulting complete character and quotient conclusion.

## Assumptions and scope

The presentation is
\[
G=\langle x,y\mid x^{2n}=1,\ y^2=x^n,\ yxy^{-1}=x^{-1}\rangle,\qquad n\in\mathbb Z,\ n\ge2.
\]
Its center is \(Z=\{1,x^n\}\). The space is the *ordinary geometric realization of the poset*, not a homotopy-orbit or Borel construction. The action is left multiplication on each coset. The cohomological results are integral, not merely rational. No extension to arbitrary finite groups is claimed.

## Proof

**Maximal abelian cosets.** Every element outside \(A\) is \(x^iy\) and has square \(x^n\). Its centralizer is its order-four subgroup \(B_i=\langle x^iy\rangle\). The distinct subgroups are indexed by \(i\) modulo \(n\). Each meets \(A\) in \(Z\), and distinct \(B_i\) also meet in \(Z\). These and \(A\) are all the maximal abelian subgroups. There are two left cosets of \(A\), named \(U,V\), and exactly \(n\) left cosets of each \(B_i\), giving the \(n^2\)-element set \(\mathcal E_n\).

**Equivariant nerve.** Cover the order complex of \(\mathcal P(G)\) by the principal downsets of these maximal cosets. Any nonempty intersection of the downsets is the principal downset of their set intersection, a coset of an abelian subgroup, so it has a terminal object. Moreover its stabilizer fixes that terminal coset. The finite equivariant nerve theorem therefore identifies \(X_n\), up to \(G\)-homotopy, with the nerve \(N\) of the maximal-coset intersection cover. (The stabilizer condition is necessary, and holds here.)

Each small coset \(e\in\mathcal E_n\) meets one central coset in \(U\) and one in \(V\), and these pairs exhaust the \(n\)-by-\(n\) choices of central cosets. The nerve is the union of \(n\) simplices of dimension \(n\) consisting of \(U\) and all small cosets in one fixed row, together with \(n\) analogous simplices consisting of \(V\) and all small cosets in one fixed column. Two such simplices on the same side meet only at their common apex; one on each side meets in one small-coset vertex. Thus the two halves are cones with respective apices \(U,V\), intersecting at precisely the \(n^2\) isolated small-coset vertices.

**Equivariant graph reduction.** For each of the row and column simplices, retain the star from its apex to its other vertices. This is an equivariant *strong deformation retraction of the nerve* onto \(\Gamma=K_{2,n^2}\). Explicitly, in a simplex write barycentric coordinates as \((t_a,t_1,\ldots,t_n)\), where \(a\) is its distinguished apex. Let \(s\) be the second-largest of \(t_1,\ldots,t_n\), and put \(t'_i=\max(t_i-s,0)\), \(t'_a=1-\sum_i t'_i\). The straight-line homotopy to the primed coordinates fixes all the retained star spokes and agrees on shared vertices. The formula is invariant under permutations of the nonapex vertices, and also under exchanging the two families of simplices, hence is \(G\)-equivariant.

**Integral module and character.** Orient every edge of \(\Gamma\) from \(U\) or \(V\) toward its small-coset vertex. The first-cycle group is identified with the collections of integer coefficients \((a_e)_{e\in\mathcal E_n}\) summing to zero, using the cycle having coefficient \(+a_e\) on the \(U\)-to-\(e\) edge and \(-a_e\) on the \(V\)-to-\(e\) edge. Translation in \(A\) preserves \(U,V\), whereas translation outside \(A\) interchanges them, producing precisely the sign twist \(\varepsilon\). The rank and vanishing of other reduced homology follow from the graph.

For an element \(g\in Z\), all \(n^2\) small cosets are fixed. For \(g\in A\setminus Z\), none is fixed, because their stabilizers are conjugates of some \(B_i\), whose intersection with \(A\) is \(Z\). If \(g\notin A\), it fixes exactly \(n\) small cosets: its centralizer has order four, and for each of the \(n\) relevant order-four subgroup types the coset stabilizer calculation gives the stated total (alternatively use the row-column involution on the \(n\)-by-\(n\) small-coset grid). Thus the trace of the sign-twisted augmentation lattice is \(\varepsilon(g)(|\mathcal E_n^g|-1)\), which is the displayed character.

**Orbit space.** The group is transitive on \(\{U,V\}\). For each \(i\), its action on \(G/B_i\subset\mathcal E_n\) is transitive; the \(n\) different subgroup labels remain distinct. The stabilizer of each small coset includes an element outside \(A\), hence interchanges \(U\) and \(V\). It therefore identifies the two corresponding edges of \(\Gamma\). The quotient \(\Gamma/G\) is a star with \(n\) leaves and hence is contractible. The equivariant homotopy equivalence implies \(X_n/G\simeq\Gamma/G\), proving the last assertion.

## Verification

The accompanying executable `verify.py` exhaustively constructs the group law, the maximal abelian cosets, the center-coset intersection nerve, all faces and the Euler characteristic for every \(2\le n\le7\). It independently tests the complete left action on maximal-coset vertices, the three character cases, and the \(n\) orbits of small cosets. All assertions passed in the provided `verify_output.txt`. These are finite cross-checks, not an induction proof; the proof above establishes arbitrary \(n\ge2\).

## Relationship to prior work

Okay's 2016 work introduced the abelian-coset poset framework and its relevance to the classifying space for commutativity, with emphasis on extraspecial groups. Antolín-Camarena, García-Hernández and Sánchez-Saldaña subsequently proved in Theorem 5.1 of their 2023 preprint that the **nonequivariant** homotopy type for this precise dicyclic family is already a wedge of \(n^2-1\) circles, and explicitly counted the associated maximal-coset graph. Accordingly neither that count nor the nonequivariant wedge classification is claimed as new. The additional assertion concerns the **explicit integral module under left translation**, a compatible equivariant graph model, its full character, and the ordinary symmetry-quotient homotopy type. The inspected earlier theorem does not state these equivariant conclusions.

## Limitations

The equivalence is equivariant for the canonical **left regular action**, not automatically for the full automorphism group. It is not asserted to be a literal simplicial collapse of the original poset. The 2023 nonequivariant theorem is a particularly close predecessor and further equivalent descriptions in unindexed literature remain a possible priority risk. No independent mathematical audit has been performed.

## References

- C. Okay, *Spherical posets from commuting elements*, preprint posted 2016-08-04, arXiv:1608.01685, https://arxiv.org/abs/1608.01685 .
- O. Antolín-Camarena, A. García-Hernández and L. J. Sánchez-Saldaña, *The classifying space for commutativity of geometric orientable 3-manifold groups*, preprint 2023, Theorem 5.1, arXiv:2307.04997, https://arxiv.org/abs/2307.04997 .
