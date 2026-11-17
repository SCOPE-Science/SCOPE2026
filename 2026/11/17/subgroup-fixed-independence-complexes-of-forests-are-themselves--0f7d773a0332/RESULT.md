# Subgroup-fixed independence complexes of forests are themselves forest complexes

## Finding

Let \(F\) be any finite simple forest, possibly disconnected, and let \(H\leq\operatorname{Aut}(F)\) be any finite subgroup. Let \(\mathcal O_H\) be the vertex-orbit set. Delete every orbit that contains an edge of \(F\); on the remaining orbits put an edge when at least one original edge joins them. Denote this simple *orbit-conflict graph* by \(Q_H(F)\).

**Theorem.** The graph \(Q_H(F)\) is a forest, and the geometric fixed-point space has a canonical piecewise-linear homeomorphism
\[
|\operatorname{Ind}(F)|^H\ \cong_{\mathrm{PL}}\ |\operatorname{Ind}(Q_H(F))|.
\]
Consequently **every** subgroup-fixed space is empty, contractible, or homotopy equivalent to one integral sphere, and the exact case and dimension follow from the leaf algorithm below.

**Orientation-character consequence.** Suppose \(|\operatorname{Ind}(F)|\simeq S^d\) for \(d\geq0\). For each \(g\in\operatorname{Aut}(F)\), the graph \(Q_{\langle g\rangle}(F)\) cannot have contractible independence complex. Put \(e_g=-1\) if this fixed space is empty, and otherwise put \(e_g\geq0\) for its sphere dimension. Then the induced automorphism of the rank-one integral homology \(\widetilde H_d(\operatorname{Ind}(F);\mathbb Z)\) is multiplication by
\[
\operatorname{deg}(g)=(-1)^{e_g-d}.
\]
In particular this gives the full integral orientation character for every forest whose independence complex is a homotopy sphere.

## Assumptions and scope

All graphs are finite, undirected and simple. The independence complex includes the empty face. Its realization is empty for a graph with no vertices; in the leaf algorithm only, this is denoted formally by \(S^{-1}\). Automorphisms act by permuting original graph vertices, and fixed means **geometric** fixed points, not the subcomplex on individually fixed vertices. No transitivity, freeness, connectivity or abelian group hypothesis is imposed.

For a forest \(Q\), the following deterministic classification algorithm is valid with **any** choice of leaf. Initialize \(s=-1\). If the **initial** forest is empty, return `empty` (formal dimension \(-1\)). Otherwise repeat: if the current forest has an isolated vertex, return `contractible`; if it is empty, return \(S^s\); in the remaining case choose a leaf \(v\), let \(u\) be its neighbor, delete \(N_Q[u]\), and increase \(s\) by one. Every nonempty forest with no isolated vertices has such a leaf.

## Proof

**1. Geometric orbit coordinates.** Give each vertex \(v\) of the independence complex a barycentric coordinate \(x_v\). A point is fixed by \(H\) exactly when \(x_v\) is constant over every \(H\)-orbit. Since a simplex is an independent vertex set, a positive-weight orbit must contain no graph edge. A collection of admissible orbits can simultaneously receive positive weight precisely when no edge joins any two of them. Thus the admissible collections are exactly the faces of \(\operatorname{Ind}(Q_H(F))\). The map sending its orbit-coordinate \(y_O\) to \(x_v=y_O/|O|\) for \(v\in O\), with zero coordinates on forbidden orbits, is affine on simplices and has inverse \(y_O=\sum_{v\in O}x_v\). Both maps agree on common faces. They give the asserted global PL homeomorphism, including when there are no eligible orbits.

**2. Why the orbit-conflict graph is a forest.** First suppose \(F\) is one tree. Subdivide every edge once. A finite group of tree automorphisms fixes the center (a vertex or an edge midpoint) of the subdivided tree. Root the subdivision there. The unique-parent map from every other vertex to its predecessor on the root path commutes with the group action. Consequently each nonroot vertex orbit has one parent orbit, and the quotient of the subdivided tree by \(H\) is a rooted tree. An original edge orbit produces a subdividing vertex of degree two in this quotient if its two endpoint orbits are distinct, and degree one if they coincide (the inverted-edge case). Suppress the degree-two subdividing vertices and discard the latter pendant subdividing vertices. What remains is the simple graph on all original vertex orbits with edges only between distinct orbits; it is a tree or forest since these operations do not create cycles. Finally deleting the original vertex orbits that contain internal edges gives \(Q_H(F)\), an induced subforest.

If \(F\) has many components, partition its components into \(H\)-orbits. Fix a representative component in each class and restrict to its setwise stabilizer. Vertex and edge orbits in that class correspond to stabilizer orbits in the representative tree. The previous argument applies independently in each class, proving the forest assertion in general.

**3. Leaf recursion.** For a forest \(Q\), an isolated vertex is an apex of \(\operatorname{Ind}(Q)\), so its realization is contractible. If no isolated vertex exists, choose a leaf \(v\) with neighbor \(u\). The decomposition
\[
\operatorname{Ind}(Q)=\operatorname{Ind}(Q\setminus u)\cup\bigl(u*\operatorname{Ind}(Q\setminus N_Q[u])\bigr)
\]
has a contractible first term because \(v\) is isolated in \(Q\setminus u\); the second is a cone, and their intersection is \(\operatorname{Ind}(Q\setminus N_Q[u])\). Its realization is therefore homotopy equivalent to the unreduced suspension of the intersection. The convention \(\Sigma\varnothing=S^0\) handles an empty residual graph. Every step decreases the number of vertices, proving the algorithm and all boundary cases by induction.

**4. Orientation character.** The reduced Lefschetz number of a simplicial automorphism \(g\) equals the reduced Euler characteristic of its geometric fixed-point set (apply barycentric subdivision so fixed simplices have no inversions). If \(|\operatorname{Ind}(F)|\simeq S^d\), reduced homology is a single rank-one group in degree \(d\), on which \(g\) acts by \(+1\) or \(-1\). Its reduced Lefschetz number is thus nonzero. The fixed locus cannot be contractible by the first three steps. For a sphere \(S^{e_g}\) its reduced Euler characteristic is \((-1)^{e_g}\); for the empty locus it equals \(-1=(-1)^{-1}\). Equating this with \((-1)^d\operatorname{deg}(g)\) yields exactly \(\operatorname{deg}(g)=(-1)^{e_g-d}\). No finite computation is used to establish the universal statement.

## Verification

The standalone `forest_fixed_verify.py` constructs vertex orbits of generated automorphism groups and checks them against a **separate** enumeration of original invariant independent subsets. It confirms acyclicity of the quotient graph, the exact fixed-face correspondence, reduced mod-two boundary-matrix homology and the reduced Lefschetz/orientation formula. The included `forest_fixed_verify.out` is the recorded output from executing that exact file.

It tests 282 cyclic-subgroup cases across nonisomorphic trees with two through eight vertices (discarding trees with more than 48 automorphisms for tractability), and seven additional generated-group cases, including noncyclic arm permutations and symmetry of four disjoint edges: 289 cases total and 6269 matched orbit faces. These finite checks support but do not prove the infinite theorem.

For example, in the tree formed from a central vertex and three two-edge arms, the original independence complex is \(S^2\) up to homotopy. The full arm-permuting \(S_3\) fixes a space of homotopy type \(S^0\); a transposition fixes \(S^1\), and a three-cycle fixes \(S^0\). More generally the subgroup-fixed sphere dimension is one less than the number of orbits of arms under the subgroup.

## Relationship to prior work

Ehrenborg and Hetyei proved in 2005 that the **ordinary** independence complex of every forest is simple-homotopy equivalent to a point or sphere; their §6 supplies ordinary reduction procedures. Adamaszek's 2015 chordal-graph theorem characterizes contractible ordinary independence complexes by strong collapsibility and spherical ones by cross-polytopal cores. These results are used and not claimed as new. The result here concerns the actual geometric fixed-point space for **every subgroup** together with the explicit orbit-forest PL model and the complete integral orientation character. Neither inspected work contains the orbit-action classification.

Kawamura's 2010 paper gives an ordinary forest-type algorithm. Its abstract was checked, but the hosted PDF did not load, so no whole-paper noncoverage claim is made for it. An equivariant overlap in unindexed or inaccessible literature remains possible.

## Limitations

The theorem is specific to forests. A general graph's orbit-conflict graph may have cycles, so its fixed spaces need not be spheres or contractible. The theorem does not assert that the full action is equivariantly a linear representation sphere, nor classify its orbit-space homotopy. The PL identification is exact, but the spherical or contractible homotopy simplification need not be a PL homeomorphism to a standard sphere or ball. Publication priority and independent validation have not been established.

## References

1. R. Ehrenborg and G. Hetyei, *The topology of the independence complex*, European Journal of Combinatorics 27 (2006), 906–923. First publicly online 2005-11-28, DOI: 10.1016/j.ejc.2005.04.010. Author-posted full text: https://www.ms.uky.edu/~jrge/Papers/Independence.pdf (especially §§5–6).
2. M. Adamaszek, *A note on independence complexes of chordal graphs and dismantling*, arXiv:1508.02426v1 (2015-08-10), https://arxiv.org/html/1508.02426v1 (especially Theorem 1 and Lemma 5).
3. K. Kawamura, *Homotopy types of independence complexes of forests*, Contributions to Discrete Mathematics 5 (2010), 67–75, DOI: 10.55016/ojs/cdm.v5i2.62064. Abstract at https://cdm.ucalgary.ca/article/view/62064; full text unavailable in this check.
