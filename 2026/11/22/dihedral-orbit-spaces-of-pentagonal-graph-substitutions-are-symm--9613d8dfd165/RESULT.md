# Dihedral orbit spaces of pentagonal graph substitutions are symmetric joins

## Finding

For a finite nonempty simple graph \(H\), write \(X=|\operatorname{Ind}(H)|\) and \(G=C_5\circ H\), with the lexicographic product using five identical labelled copies of \(H\). Let \(D_5\) act by rotating and reflecting the five outer positions, without changing labels in any copy. The **actual geometric orbit space**, not a quotient obtained by simply identifying simplicial vertices, has a natural homeomorphism

\[
|\operatorname{Ind}(G)|/D_5\ \cong\ (X*X)/\langle\tau\rangle,
\qquad \tau([x,y,t])=[y,x,1-t].
\]

For every integer \(d\ge2\), take \(H=(d+1)K_2\), a disjoint union of \(d+1\) edges. Then \(X\cong S^d\), and the orbit space has the more explicit homeomorphism

\[
|\operatorname{Ind}(C_5\circ((d+1)K_2))|/D_5
\ \cong\ S^d*\mathbb{RP}^{d}
\ \simeq\ \Sigma^{d+1}\mathbb{RP}^{d}.
\]

Here \(\Sigma\) denotes suspension, and the last expression is a homotopy equivalence under the usual based-suspension convention. Its **complete reduced integral homology** is

\[
\widetilde H_k\ \cong\
\begin{cases}
\mathbb Z/2,&k=d+1+j,\quad j\text{ odd},\ 1\le j<d,\\
\mathbb Z,&k=2d+1\text{ and }d\text{ odd},\\
0,&\text{otherwise}.
\end{cases}
\]

In particular the first nontrivial torsion example, \(d=2\), is a degree-four mod-two Moore space \(M(\mathbb Z/2,4)\); it has \(\widetilde H_4\cong\mathbb Z/2\) and no other reduced integral homology. The unquotiented substituted-graph complex has torsion-free integral homology by the published sphere-wedge classification; its orbit space need not.

## Assumptions and scope

All complexes are finite, with ordinary geometric realizations. The vertices of \(C_5\) are indexed by \(\mathbb Z/5\mathbb Z\). A vertex of \(G\) is a pair \((i,h)\), with \(h\in V(H)\). Two vertices are adjacent if their outer indices are adjacent in \(C_5\), or if the indices coincide and their \(H\)-labels are adjacent. The group \(D_5\) has order ten and acts via \(i\mapsto \epsilon i+a\) for \(\epsilon\in\{1,-1\}\) and \(a\in\mathbb Z/5\mathbb Z\); it acts trivially on \(h\). The quotient is the orbit space of the full geometric realization, including points on faces inverted by symmetries.

For \(d\ge2\), the graph \((d+1)K_2\) consists of \(d+1\) pairwise disjoint edges. All homology groups use integer coefficients, and all displayed homotopy and homeomorphism statements concern the full spaces, not just homology.

## Proof

**1. Five joins.** An independent set in \(C_5\) has at most two vertices. Its two-element independent sets are exactly the five diagonals \(A_i=\{i,i+2\}\), indexed by \(i\in\mathbb Z/5\mathbb Z\). Since \(H\) is nonempty, every independent face in \(G\) has its outer support contained in at least one \(A_i\). Let \(J_i\) be the full independence subcomplex supported in the two copies over \(A_i\). Then

\[
\operatorname{Ind}(G)=\bigcup_{i=0}^{4}J_i,
\qquad |J_i|\cong X*X.
\]

If a point has positive barycentric mass on two outer indices, these are necessarily the unique pair \(A_i\) containing its support. If it has mass on exactly one index, it belongs to two such joins. These are the only overlaps.

**2. Orbit reduction, including overlaps.** Fix \(A_0=\{0,2\}\) and write \(J=J_0\). The group \(D_5\) acts transitively on the five diagonals, so every orbit meets \(|J|\). The setwise stabilizer of \(A_0\) has order two: identity and the reflection \(s(i)=2-i\pmod5\), which swaps indices \(0\) and \(2\). Hence the quotient map of \(|J|\) descends to a continuous surjection from \(|J|/\langle s\rangle\) onto \(|\operatorname{Ind}(G)|/D_5\).

To prove injectivity, suppose \(p,q\in|J|\) and \(g(p)=q\) for \(g\in D_5\). If \(p\) uses both outer positions, then so does \(q\); its outer support is exactly \(A_0\), so \(g(A_0)=A_0\) and \(g\in\langle s\rangle\). If \(p\) uses only one position, then \(q\) does as well, and the relevant positions both lie in \(A_0\). They are either equal or exchanged; since \(g\) does not change the inner \(H\)-labels, \(q=p\) in the first case and \(q=s(p)\) in the second. Thus the map is bijective. It is a homeomorphism since the domain is compact and the target is Hausdorff (a finite group quotient of a finite polyhedron). The restriction of \(s\) to \(J\cong X*X\) is precisely the factor exchange \(\tau\). This proves the general claim.

**3. Orthogonal form of the factor exchange.** For \(H=(d+1)K_2\), an independent face chooses at most one endpoint from each of \(d+1\) edges. Therefore \(\operatorname{Ind}(H)\) is the join of \(d+1\) two-point complexes, the boundary of the \((d+1)\)-crosspolytope. Its radial homeomorphism to the unit sphere \(S(V)\), with \(V=\mathbb R^{d+1}\), gives an equivariant homeomorphism \(X*X\cong S(V\oplus V)\). The factor exchange is \((u,v)\mapsto(v,u)\). The orthogonal coordinate change

\[
(p,q)=\left(\frac{u+v}{\sqrt2},\frac{u-v}{\sqrt2}\right)
\]

conjugates it to \((p,q)\mapsto(p,-q)\). The unit sphere of the direct sum is the join \(S(V)_+*S(V)_-\), and the involution is trivial on the first factor and antipodal on the second. The orbit is therefore homeomorphic to \(S^d*(S^d/\{\pm1\})=S^d*\mathbb{RP}^d\). Because \(S^d=(S^0)^{*(d+1)}\), this join is an iterated suspension of \(\mathbb{RP}^d\).

**4. Integral homology and sharp small example.** The standard CW structure on \(\mathbb{RP}^d\) has one cell in each degree \(0,1,\ldots,d\), with degree-\(j\) cellular boundary multiplication by \(2\) for positive even \(j\), and by \(0\) for odd \(j\). Its reduced integral homology has \(\mathbb Z/2\) in each odd degree \(1\le j<d\) and \(\mathbb Z\) in degree \(d\) exactly when \(d\) is odd. Suspending \(d+1\) times shifts these degrees by \(d+1\), yielding the displayed groups. For \(d=2\), \(\mathbb{RP}^2\) is the cofiber of the degree-two map \(S^1\to S^1\), hence its threefold suspension is the cofiber of the degree-two map \(S^4\to S^4\), i.e. \(M(\mathbb Z/2,4)\). No assertion of an integral sphere-wedge decomposition of the quotient is made.

## Verification

A standalone script `VERIFY.py` enumerates independent faces of the pentagon substitution for \(d=0,1,2,3\), quotients these faces by all ten dihedral permutations, and independently quotients faces supported on \(\{0,2\}\) by its two-element stabilizer. It verifies a bijection of the two orbit sets, including the single-support overlaps. Observed global face counts are \(30,360,3510,32400\), and corresponding orbit counts are \(5,44,377,3320\). The same script checks the predicted cellular integral-homology groups for \(2\le d\le8\), including \(\widetilde H_4\cong\mathbb Z/2\) at \(d=2\). These finite computations corroborate but do not substitute for the topological proof for arbitrary nonempty \(H\) and all \(d\ge2\).

Run `python3 VERIFY.py` with Python 3 and no nonstandard dependencies.

## Relationship to prior work

Carnero Bravo's *Polyhedral joins and graph complexes* establishes the nonequivariant homotopy classification for such lexicographic graph complexes via polyhedral joins. In particular its cycle graph formulas classify the unquotiented spaces up to homotopy, but do not identify these dihedral geometric orbit spaces or their integral torsion. Okura's *On the Homotopy Type of the Polyhedral Join over the Independence Complex of a Forest* gives nonequivariant polyhedral-join splitting results for forest outer graphs and states the graph-product/polyhedral-join correspondence; the outer five-cycle is not a forest. The present conclusion instead identifies the actual orbit space by a stabilizer reduction and computes its integral torsion. The theorem concerns outer dihedral symmetry alone, not the full automorphism group of the substituted graph.

## Limitations

The group action must preserve all inner labels and act through the specified outer \(D_5\); quotienting additionally by automorphisms of \(H\) is not covered. The general symmetric-join homeomorphism holds for nonempty finite \(H\), but the explicit real-projective classification relies on \(H=(d+1)K_2\). The result concerns genuine geometric group orbits, not naive simplicial vertex-orbit complexes. Finite verification does not establish the unrestricted theorem; the support/stabilizer and orthogonal-decomposition arguments do. Related results on arbitrary symmetric joins may give an alternative derivation; an exhaustive bibliographic uniqueness claim is not made.

## References

1. Kengo Okura, *On the Homotopy Type of the Polyhedral Join over the Independence Complex of a Forest*, arXiv:2303.11984 (first public version 2023-03-21), https://arxiv.org/abs/2303.11984.
2. Andrés Carnero Bravo, *Polyhedral joins and graph complexes*, arXiv:2307.14321 (first public version 2023-07-26), https://arxiv.org/abs/2307.14321.
