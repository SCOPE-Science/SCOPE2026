# Young-subgroup fixed spaces of complete-graph forest complexes

## Finding

Let \(n\ge 2\) and let \(\mathcal F_n\) be the graphic-matroid independence complex of the complete graph on \([n]\): its simplicial vertices are the edges of \(K_n\), and a set of such vertices is a face exactly when those graph edges form a forest. Partition \([n]\) into \(m\ge0\) singleton blocks and \(b\ge1\) non-singleton blocks of sizes \(k_1,\ldots,k_b\ge2\). Let
\[
H=S_{k_1}\times\cdots\times S_{k_b}\le S_n
\]
act independently on the non-singleton blocks, fixing the other \(m\) labels. Write \(a=|\{i:k_i=2\}|\), and let \(D_s\) be the abstract zero-dimensional simplicial complex on \(s\) isolated vertices, with \(D_0=\{\emptyset\}\) (no geometric points). Then the **actual geometric fixed-point space** admits a canonical piecewise-linear homeomorphism
\[
\boxed{
 |\mathcal F_n|^H \cong_{\mathrm{PL}}
 \left|\mathcal F_m*D_{m+1}^{*a}*D_m^{*(b-a)}\right|.
}
\]
Here \(\mathcal F_0=\mathcal F_1=\{\emptyset\}\) and \(*\) denotes the abstract simplicial join on disjoint vertex sets. In particular, for every \(m\ge3\),
\[
\boxed{
|\mathcal F_n|^H\simeq\bigvee^{\,B_m m^a(m-1)^{b-a}}S^{m+b-2},
\qquad B_m=(m-2)H_{m-3}(m-1),
}
\]
where the polynomial \(H_j(t)\) is defined by \(\sum_{j\ge0}H_j(t)z^j/j!=\exp(tz+z^2/2)\). Thus \(B_3=1\), \(B_4=6\), \(B_5=51\), \(B_6=560\), and all these spaces have torsion-free **reduced** integral homology concentrated in the indicated dimension.

The exceptional cases are also complete: when \(m=2\) the fixed space is contractible; when \(m=1\) it is \(S^{b-1}\) if every non-singleton block has size two, and is contractible otherwise; when \(m=0\) it is contractible if some block has size two and is empty otherwise. For example, a transposition in \(S_5\) fixes a space homotopy equivalent to \(\bigvee^3S^2\), whereas any permutation subgroup \(S_3\) acting on three labels of six fixes \(\bigvee^2S^2\). More generally, enlarging an independently permuted block from size three to any larger size has no effect on the fixed-space homeomorphism type when \(m\) and the number of blocks are held fixed.

## Assumptions and scope

The group action permutes **graph vertices**, thus permuting the \(\binom n2\) simplicial vertices indexed by graph edges. The fixed set means all points \(x\) in the linear geometric realization satisfying \(hx=x\) for every \(h\in H\), not the subcomplex on graph edges individually fixed by \(H\), and not the orbit space \(|\mathcal F_n|/H\). The non-singleton blocks are permuted independently by their **full** symmetric groups. The claim does not include arbitrary subgroups transitive on those blocks. The count \(a\) is the number of blocks of size exactly two. The simplicial join with \(\{\emptyset\}\) uses the standard abstract-complex convention, so its geometric realization can be empty.

## Proof

**1. Orbit-barycenter realization of fixed points.** Let \(E\) be the set of edges of \(K_n\). A point in \(|\mathcal F_n|\) has a unique finitely supported barycentric coordinate vector \((x_e)_{e\in E}\) with nonnegative coordinates summing to one, whose positive-coordinate support is a forest. It is fixed by every \(h\in H\) if and only if its coordinates are constant on each \(H\)-orbit \(O\subseteq E\). Therefore its support is a union of entire edge orbits, each individually a forest. The vertex corresponding to an eligible edge orbit \(O\) is mapped to its barycenter \(|O|^{-1}\sum_{e\in O}e\). Mapping a simplex of eligible orbits affinely by their barycenters gives a continuous bijection from the orbit-union forest complex to the fixed set. It is a homeomorphism because its domain is compact and its target Hausdorff. The affine maps identify faces precisely, providing a PL homeomorphism.

**2. Exhaustive edge-orbit classification.** Denote the singleton labels by \(T\), \(|T|=m\), and the non-singleton blocks by \(A_i\), \(|A_i|=k_i\). Every \(H\)-orbit of graph edges belongs to exactly one of the following five kinds:

- An edge joining two labels of \(T\) is individually fixed and admissible. These vertices form \(\mathcal F_m\).
- The edges joining all labels of one \(A_i\) to one fixed label \(t\in T\) form one orbit of size \(k_i\), a star and hence an admissible forest. There are \(m\) such orbits for each \(i\).
- The edges within \(A_i\) form one orbit: when \(k_i=2\) it is a single admissible edge; when \(k_i\ge3\) it contains a triangle and is forbidden.
- For distinct blocks \(A_i,A_j\), all \(k_i k_j\) edges joining them form one orbit, containing a four-cycle since both sizes are at least two, and are forbidden.
- There are no other edges or orbits.

Within one block \(A_i\), choosing two distinct admissible star orbits produces the four-cycle \(t-u-t'-v-t\) for two different labels \(u,v\in A_i\); if \(k_i=2\), choosing its internal edge alongside any star produces a triangle. Thus at most one admissible orbit associated with a given non-singleton block can be selected. Conversely, choose any forest among edges on \(T\), and for each \(A_i\) choose at most one admissible orbit (a star at one fixed label, or its internal edge if \(k_i=2\)). Each chosen star is a pendant tree attached to the fixed-label forest at exactly one vertex, and each chosen internal two-label edge is an isolated tree. Adding these trees cannot create cycles, even if several blocks choose the same attachment label. Hence every such choice is valid. This proves the exact simplicial join in the finding, including all empty-factor boundary cases.

**3. Homotopy classification.** For \(m\ge3\), the ordinary complete-graph forest complex \(\mathcal F_m\) is the independence complex of a rank-\(m-1\) matroid and therefore is pure shellable and homotopy equivalent to a wedge of \(B_m\) spheres of dimension \(m-2\) [1,2,3]. For a discrete complex \(D_s\) with \(s\ge2\), its realization is based-homotopy equivalent to a wedge of \(s-1\) zero-spheres, and joining with it multiplies the number of wedge spheres by \(s-1\) and increases the dimension by one. Iterating over the \(b\) blocks gives dimension \(m+b-2\) and multiplicity \(B_m m^a(m-1)^{b-a}\). The known exact forest Euler-characteristic formula gives \(B_m=(m-2)H_{m-3}(m-1)\) [3, Theorem 13.3]. Equivalently, without using that closed expression,
\[
B_m=(-1)^{m-1}\sum_{F\text{ a labeled forest on }[m]}(-1)^{|E(F)|},
\]
which is directly computable by enumerating labeled forests.

When \(m=2\), \(\mathcal F_2\) is a one-vertex simplex, so the join is a cone. When \(m=1\), each size-two block contributes \(D_2\simeq S^0\), and each larger block contributes a one-vertex cone factor \(D_1\); the stated sphere/contractible dichotomy follows. When \(m=0\), every size-two block contributes one available internal edge, whereas every larger block has no eligible orbit, giving a simplex if \(a\ge1\) and no geometric points if \(a=0\). These are all cases.

## Verification

The standalone Python 3 program `verify_fixed_forests.py` independently enumerates the full product group action on complete-graph edges, constructs all edge orbits, tests admissibility by union-find, then tests **every** subset of eligible orbits against the proposed factorization for fourteen block configurations. It also computes the signed forest sums directly on \(m=3,4,5,6\) labels, recovering \((B_3,B_4,B_5,B_6)=(1,6,51,560)\). Its observed terminal output is `VERIFY_OK`. The verification is deliberately finite; the unbounded classification follows from the symbolic five-case orbit exhaustion and the established matroid shellability theorem, not from extrapolation.

## Relationship to prior work

Provan and Billera [1] prove vertex decomposability of matroid complexes. Björner [2] develops the resulting homological topology, and Jonsson [3, Chapter 13, Section 13.1] states the forest-complex sphere-wedge theorem and the exact multiplicity formula. These sources establish \(\mathcal F_m\), **not** the fixed set \(|\mathcal F_n|^H\). Related symmetry analyses of complete-graph **matching** complexes treat disjoint-edge faces rather than all cycle-free faces, while analyses of complete-graph **discrete Morse** complexes treat directed rooted-forest matchings rather than graphic matroid independent sets; their fixed-point formulas do not determine the edge-orbit factorization above. The claim adds the PL model and the complete Young-subgroup fixed-space classification, including exceptional cases. Its novelty is assessed relative to the inspected literature; unindexed equivalent work remains possible.

## Limitations

The theorem does not classify quotients, general subgroups of symmetric groups, or fixed points of arbitrary transitive block actions. It does not assert equivariant equivalences for the ambient space, and the wedge equivalence is nonequivariant. The complete PL model is more precise than the wedge statement. The external shellability and forest Euler-characteristic results used in the final homotopy and multiplicity deductions are credited rather than claimed anew. Published-source access and indexing remain incomplete, so publication priority needs independent scrutiny.

## References

[1] J. S. Provan and L. J. Billera, *Decompositions of simplicial complexes related to diameters of convex polyhedra*, Mathematics of Operations Research 5 (1980), 576–594, especially Section 3.2, Theorem 3.2.1. DOI: https://doi.org/10.1287/moor.5.4.576 (first published 1 November 1980).

[2] A. Björner, *The homology and shellability of matroids and geometric lattices*, in *Matroid Applications*, Cambridge University Press, 1992, pp. 226–283. DOI: https://doi.org/10.1017/CBO9780511662041.008 .

[3] J. Jonsson, *Simplicial Complexes of Graphs*, Lecture Notes in Mathematics 1928, Springer, 2008, Chapter 13, particularly Theorems 13.1 and 13.3. DOI: https://doi.org/10.1007/978-3-540-75859-4 .
