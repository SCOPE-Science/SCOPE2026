# Five new circles per tetrahedral stacking in simplicial doubles

## Finding
Let \(X\) be a finite pure simplicial complex of dimension three, and let \(\tau=\{a,b,c,d\}\) be one of its tetrahedral facets. Let \(X'\) be obtained by a facet stellar subdivision: introduce a new vertex \(w\), delete only the three-simplex \(\tau\), retain its boundary, and insert the four tetrahedra \(\{w\}\cup(\tau\setminus\{x\})\) for \(x\in\tau\). Write \(D_2(X)\) for the simplicial double of Lesh--Schreiner--Wahl: its vertices are edges of \(X\), and two vertices are adjacent precisely if their original edges are disjoint and their union is a tetrahedral face of \(X\).

Let \(c\) and \(b\) be the number of connected components and the first integral Betti number of \(D_2(X)\). Let \(k\) be the number of connected components of \(D_2(X)\) meeting the six edge-vertices belonging to \(\tau\). Then \(1\le k\le3\), and the **exact local update** is
\[
 c(D_2(X'))=c-k+1,\qquad
 \operatorname{rank}H_1(D_2(X');\mathbb Z)=b+6-k.
\]
All first homology groups here are free abelian. In particular, if \(D_2(X)\) is connected, so is \(D_2(X')\), and facet stacking adds exactly five independent integral circle classes.

Consequently, for **every stacked simplicial four-polytope** \(P\) with \(n\ge5\) vertices, irrespective of its stacking history,
\[
 \boxed{D_2(\partial P)\simeq\bigvee^{5n-19}S^1.}
\]
This is an integral homotopy classification, not merely an Euler-characteristic computation. The same formula holds for any triangulated three-sphere obtained from \(\partial\Delta^4\) by successive tetrahedral stellar subdivisions.

## Assumptions and scope
A pure three-complex is a finite abstract simplicial complex all of whose maximal faces have four vertices. The double \(D_2\) is defined using **all** two-element faces and four-element faces, not a matching complex of the one-skeleton: pairs of disjoint edges need not be adjacent unless their union is a tetrahedron. No orientation or manifold hypothesis is required for the local rule. A stacked simplicial four-polytope is obtained from a four-simplex by repeatedly adding a vertex beyond a tetrahedral boundary facet; the boundary change is exactly the facet subdivision above.

For any finite graph \(Y\) with \(V\) vertices, \(E\) edges, and \(c\) connected components, its first integral homology is free of rank \(E-V+c\). A nonempty connected finite graph is homotopy equivalent to a wedge of that many circles. These standard graph facts are the only homotopy-theoretic tools needed.

## Proof
**1. The double is a graph.** Every simplex of \(D_2(X)\) with \(q\) vertices uses \(2q\) distinct vertices of \(X\) whose union must be a face of \(X\). As \(\dim X=3\), necessarily \(2q\le4\). Thus \(D_2(X)\) has no simplices of dimension two or greater. A tetrahedron \(\{a,b,c,d\}\) generates exactly three different edges in this graph:
\[
 ab\text{--}cd,\quad ac\text{--}bd,\quad ad\text{--}bc,
\]
where the symbols denote unordered original pairs, now vertices of the double. Different tetrahedra cannot generate the same double edge because the union of the two original pairs recovers the tetrahedron.

**2. The exact local replacement.** Subdividing \(\tau\) retains all original two-element faces and adds precisely four two-element faces \(wa,wb,wc,wd\). Hence the double gains four graph vertices. The old tetrahedron contributes the three opposite-pair edges displayed above; these three edges disappear. Each of the four new tetrahedra contributes three opposite-pair edges, all with one graph endpoint \(wx\) and the other an original pair in \(\tau\). These are twelve distinct edges. No other double edge changes. Thus
\[
 V'=V+4,\qquad E'=E-3+12=E+9.
\]

The new local subgraph on the six original pair-vertices from \(\tau\) and the four new vertices \(wx\) is precisely the incidence subdivision of the complete graph on the four labels \(a,b,c,d\): the graph vertex corresponding to the original edge \(yz\) is adjacent to \(wx\) if and only if \(x\notin\{y,z\}\). Each original pair-vertex is adjacent to exactly two new vertices; the four new vertices are each adjacent to exactly three original pair-vertices. Under the relabeling \(yz\leftrightarrow\tau\setminus\{y,z\}\), this is the usual subdivision of all six edges of \(K_4\), hence connected.

In the old double the six original pair-vertices are joined in three disjoint opposite pairs, so their vertices meet some \(k\in\{1,2,3\}\) components. Replacing their three old edges with the connected subdivided \(K_4\) merges exactly those \(k\) components into one and cannot affect any other component: none of the changed edges touches an outside vertex. Therefore \(c'=c-k+1\). Substituting in the graph-homology rank formula yields
\[
 b'-b=(E+9)-(V+4)+(c-k+1)-(E-V+c)=6-k.
\]
This proves the local rule without assuming connectivity or a particular triangulation.

**3. The stacked-sphere base case.** The boundary of the four-simplex on five vertices has all ten two-element subsets and all five four-element subsets. Its double is the Kneser graph \(KG(5,2)\): two pair-vertices are adjacent exactly if the pairs are disjoint. It has ten vertices and fifteen edges. It is connected: two intersecting pairs have the two-element complement of their three-element union as a common neighbor, and disjoint pairs are already adjacent. Therefore its first Betti number is \(15-10+1=6\) and it is homotopy equivalent to \(\bigvee^6S^1\).

**4. Induction under stacking.** Every new stacking subdivides one tetrahedral boundary facet. By step 2, connectedness persists and the first Betti number rises by five. A stacked four-polytope with \(n\) vertices is obtained after exactly \(n-5\) such moves. Therefore its double is a connected graph of rank \(6+5(n-5)=5n-19\), proving the claimed wedge of circles. Every graph involved is one-dimensional, so no higher homotopy information is lost in the graph reduction.

## Verification
Run `python verify_stacking_double.py` in the same directory. Its output must match `EXPECTED.txt` exactly. The program reconstructs double edges independently from tetrahedral facets, checks the local disappearing/appearing edges and component/rank differences, and enumerates all *labeled stacking histories as resulting distinct facet sets* through nine vertices. It also checks 1,002 additional local moves from arbitrary pure tetrahedral complexes, including disconnected examples. The finite checks are corroboration; the four proof steps above establish every asserted parameter.

## Relationship to prior work
Lesh, Schreiner and Wahl defined the simplicial double and proved a weak Cohen--Macaulay connectivity bound for its higher-dimensional generalizations [1]. Their work is the starting definition; the exact behavior under a tetrahedral facet subdivision and the stacked-sphere formula are not conclusions of their connectivity theorem. A published calculation of doubles of cyclic four-polytope boundaries [2] shows a parity-sensitive disconnection phenomenon (two components at even vertex counts). The stacked family here instead stays connected at every size. For example, two six-vertex triangulated three-spheres can consequently have doubles with different numbers of components. The cyclic calculation is prior work, not part of the claimed discovery.

## Limitations
The local theorem requires a pure three-dimensional complex and a facet (one-to-four) stellar subdivision. It does not classify two-to-three bistellar flips, non-facet subdivisions, doubles of higher-dimensional complexes, or automorphism representations. The stacked case does not assert a canonical embedding of the previous double into the next one. Exact mathematical priority remains subject to literature outside the inspected sources; no independent external audit is claimed.

## References
[1] Kathryn Lesh, Bridget Schreiner and Nathalie Wahl, *The double of a simplicial complex*, arXiv:2506.10436 (first public version 2025-06-12; version of 2026-10-27 inspected), https://arxiv.org/abs/2506.10436, Definition 2.1 and Theorem A.

[2] *Parity and dihedral homology of the doubled cyclic four-polytope boundary*, publicly available research article, 2026, published in the published-finding corpus 2026 mathematical-results repository (title and full result inspected); https://github.com/published-finding corpus/2026. This concerns cyclic rather than stacked polytope boundaries.
