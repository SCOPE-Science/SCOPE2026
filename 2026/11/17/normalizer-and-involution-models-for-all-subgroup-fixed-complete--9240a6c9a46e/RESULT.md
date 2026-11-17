# Normalizer-and-involution models for all subgroup-fixed complete-graph matching spaces

## Finding
Let \(H\) be any finite group acting on a finite set \(U\), with \(|U|\ge2\), and let \(M(U)=\mathcal M(K_U)\) be the ordinary matching complex of the loopless complete graph. For each isomorphism type \(\lambda\) of transitive \(H\)-sets occurring in \(U\), choose a representative \(H/L_\lambda\), and let \(m_\lambda\ge1\) be its multiplicity. Set
\[
 w_\lambda=|N_H(L_\lambda)/L_\lambda|,\qquad
 s_\lambda=\#\{a\in N_H(L_\lambda)/L_\lambda:a^2=1,\ a\ne1\}.
\]
Construct a colored loop-matching simplicial complex \(B_{m,w,s}\) on \(m\) positions. For every unordered pair of distinct positions introduce \(w\) separate pair-vertices (each occupying both positions); at each position introduce \(s\) separate singleton-vertices (each occupying that one position). A set of these vertices is a face exactly when their occupied position-sets are pairwise disjoint. In particular, only one singleton color can be selected at a given position. All complexes include the empty face, even if they have no nonempty faces.

**Theorem.** The pointwise geometric fixed space has a natural PL description
\[
 \boxed{\ |M(U)|^H\ \cong_{\mathrm{PL}}\ \Big|\bigast_\lambda B_{m_\lambda,w_\lambda,s_\lambda}\Big|.\ }
\]
The join on the right is the *abstract simplicial join*, so a factor with no vertices acts as a join unit. If all factors have no vertices, its realization is empty. Its face-count polynomial (the empty face contributes one) is exactly
\[
 \boxed{\ F_{H,U}(z)=\prod_\lambda \sum_{j=0}^{\lfloor m_\lambda/2\rfloor}
 \frac{m_\lambda!}{2^j j!(m_\lambda-2j)!}(w_\lambda z)^j(1+s_\lambda z)^{m_\lambda-2j}.\ }
\]

**Two regular-orbit consequence.** Let an arbitrary finite group \(G\) of order \(k\) act by left regular translation on two disjoint copies of itself, and let \(s\) be its number of nonidentity involutions. Then
\[
 |M(G\sqcup G)|^G\cong_{\mathrm{PL}}
 \begin{cases}
 D_k,&s=0,\\
 (D_s*D_s)\sqcup D_k,&s\ge1,
 \end{cases}
\]
where \(D_a\) denotes \(a\) discrete points and \(*\) denotes the topological join. For \(s\ge1\), the only nonzero reduced integral homology groups are
\[
 \widetilde H_0\cong\mathbb Z^k,\qquad
 \widetilde H_1\cong\mathbb Z^{(s-1)^2}.
\]
For \(s=0\), only \(\widetilde H_0\cong\mathbb Z^{k-1}\) may be nonzero. In particular, the two groups of order four behave differently: \(C_4\) gives five contractible components, whereas \(C_2\times C_2\) gives four isolated points and a connected component homotopy equivalent to \(\bigvee^4 S^1\).

## Assumptions and scope
All groups and sets are finite. The action of \(H\) on \(U\) need not be faithful, free, transitive or cyclic. A matching is a set of undirected two-element edges with disjoint endpoints. All fixed sets refer to points in the geometric realization, not merely invariant individual edges. Distinct colors represent distinct vertices of the model complex, not multiple edges of the original complete graph. The symbol \(N_H(L)/L\) is a group since \(L\) is normal in its normalizer. All homology assertions use integral coefficients. The empty realization has no reduced homology assertion attached to it.

## Proof
**Fixed-support triangulation.** Write every point of \(|M(U)|\) uniquely in barycentric coordinates indexed by original graph edges. It is fixed by \(H\) exactly when its coordinates are constant on each orbit of graph edges. Thus its positive support is a union of entire edge-orbits and is a matching. Each usable edge-orbit contributes one vertex to an abstract orbit complex, mapped to the barycenter of that orbit. More explicitly, an orbit-barycentric coefficient \(t_O\) is sent to coefficient \(t_O/|O|\) at each edge in \(O\). The inverse sums the old coefficients over each orbit. These affine maps agree on all common faces and give a global PL homeomorphism.

**Orbit classification: two distinct ground orbits.** Let \(X,Y\) be two distinct transitive \(H\)-orbits in \(U\), and let \(O\) be an orbit of graph edges having one endpoint in each. Both projections of \(O\) cover their corresponding transitive sets. If \(O\) is a matching, both projections are injective, making \(O\) the graph of an \(H\)-equivariant bijection \(X\to Y\). Conversely, each such bijection gives one admissible edge-orbit. Such bijections exist precisely when \(X,Y\) are isomorphic transitive \(H\)-sets. If both are isomorphic to \(H/L\), there are exactly \(|N_H(L)/L|=w\) choices, as follows by choosing the image of the coset \(L\). Each admissible orbit occupies all vertices of \(X\cup Y\).

**Orbit classification: one ground orbit.** Suppose \(O\) consists of edges internal to one transitive \(H\)-orbit \(X\). If \(O\) is a matching, equivariance and transitivity imply that each ground vertex occurs exactly once, so \(O\) is an invariant perfect matching. Its partner map \(f:X\to X\) is an \(H\)-equivariant bijection, has no fixed points, and satisfies \(f^2=1\). Conversely, every nonidentity equivariant involution gives one invariant perfect matching, which is one graph-edge orbit because \(H\) acts transitively on \(X\). The equivariant bijections of \(H/L\) form the opposite of \(N_H(L)/L\); inversion does not affect involution counts. Hence precisely \(s\) admissible internal edge-orbits exist, each occupying the whole ground orbit.

**Compatibility and factorization.** Every admissible edge-orbit occupies one or two *complete* ground-vertex orbits. Two distinct admissible edge-orbits can appear in the same matching if and only if their occupied ground-vertex orbits are disjoint. Within each transitive-set isomorphism type this is exactly the colored loop/pair matching rule defining \(B_{m,w,s}\); different isomorphism types do not interact, yielding the asserted abstract simplicial join. To count \(q\)-faces, choose \(j\) pairings among \(m\) positions, color each in \(w\) ways, and independently choose or omit a singleton at each unused position, with \(s\) color choices; the displayed polynomial follows.

**Two regular orbits.** For a regular \(G\)-set the stabilizer is trivial, so \(w=k\) and \(s\) is the number of involutions of \(G\). With two positions the complex consists of \(s\) singleton choices at each position, giving the complete bipartite graph \(D_s*D_s=K_{s,s}\) for \(s\ge1\), and \(k\) isolated pair-vertices. The bipartite graph is connected and has \(s^2\) edges and \(2s\) vertices, so its first Betti number is \(s^2-2s+1=(s-1)^2\). Adding the \(k\) isolated points gives \(k+1\) components. For \(s=0\), the fixed complex is just \(k\) isolated points. All homology and group-of-order-four conclusions follow.

## Verification
The standalone `verify_orbit_matching.py` enumerates full permutation groups generated by explicitly specified transformations, all ground-vertex orbits, every original graph-edge orbit, and every admissible invariant edge-orbit. Independently it enumerates equivariant bijections and fixed-point-free equivariant involutions of each transitive orbit, builds the predicted orbit-model vertices, and compares the complete lists of admissible edge-orbits. It further enumerates all compatible orbit-subsets and matches their face counts against the normalizer/involution polynomial. Fifteen finite action cases include cyclic, Klein-four, nonabelian \(S_3\), natural transitive actions with nontrivial stabilizer, mixed orbit types, and fixed ground vertices. The recorded final output is `ALL_ORBIT_TYPE_MATCHING_CHECKS_PASS cases=15 enumerated_faces=377`.

The finite tests do not establish the universal theorem; the complete arguments above supply its proof. The two-regular-orbit homology conclusion also follows directly from the listed one-dimensional model, independently of computational homology software.

## Relationship to prior work
A published cycle-type geometric fixed-point theorem for complete-graph matching complexes gives the cyclic-subgroup case: when \(H\) is generated by one permutation, the normalizer quotient for an orbit of length \(d\) is cyclic of order \(d\), so \(s\) is zero for odd \(d\) and one for even \(d\). The present result contains that result as a special case; it is **not** claimed as new in the cyclic setting. The other published fixed-space result for arbitrary involutions is likewise covered. Neither theorem classifies arbitrary noncyclic subgroup actions; in particular neither yields the case \(s\ge2\) without an additional all-group orbit argument. The two-regular-orbit consequence exhibits this new phenomenon for \(C_2\times C_2\), whose full fixed space is different from that of any single one of its involutions.

Wachs's survey treats matching complexes, symmetric-group homology representations and *inflations* to colored multigraph matching complexes. Those established statements do not identify geometric pointwise fixed sets under arbitrary noncyclic permutation subgroups. Shareshian and Wachs provide nonequivariant connectivity and torsion results used here only as foundational context; this theorem makes no new claim about their ordinary homology calculations. The orbit-barycenter construction is standard; the contribution is the normalizer/involution structural classification and its new noncyclic topological consequences. No novelty is asserted merely for the fixed-support lemma.

## Limitations
This theorem yields exact finite PL models and face polynomials for all finite subgroup actions, not a closed integral homotopy decomposition for every model \(B_{m,w,s}\) when \(m\ge3\). It does not compute normalizer action on the fixed-space homology, and does not determine equivariant stable homotopy types. The two-regular-orbit corollary is a full homotopy classification only for that family. Earlier unindexed equivalent treatments of subgroup-fixed matching complexes remain possible. Independent validation and publication-priority review have not occurred.

## References
1. J. Shareshian and M. L. Wachs, *Torsion in the Matching Complex and Chessboard Complex*, arXiv:math/0409054, first posted 2004-09-03, https://arxiv.org/abs/math/0409054 (especially the definitions and ordinary topology in Sections 1–4).
2. M. L. Wachs, *Topology of matching, chessboard, and general bounded degree graph complexes*, *Algebra Universalis* 49 (2003), 345–385, https://www.math.miami.edu/~wachs/papers/tmc.pdf (especially Sections 1 and 8).
3. *Cycle-type geometric fixed points of complete-graph matching complexes*, publicly indexed research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-cycle-type-geometric-fixed-points-of-complete-graph-matching-com--790f558ef1ba .
4. *Geometric fixed points of complete-graph matching complexes under every involution*, publicly indexed research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-geometric-fixed-points-of-complete-graph-matching-complexes-unde--8949870375bb .
