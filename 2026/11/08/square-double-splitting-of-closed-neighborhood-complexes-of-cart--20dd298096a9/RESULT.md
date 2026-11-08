# Square-double splitting of closed-neighborhood complexes of Cartesian graph products

## Finding

Let \(H\) and \(J\) be finite, connected simple graphs, each with at least one edge and with no cycles of length three or four. Write \(e_H=|E(H)|\), \(e_J=|E(J)|\), and let \(G=H\square J\) be their Cartesian graph product. Define the closed-neighborhood complex \(\mathcal N[G]\) to have as faces precisely those subsets of \(V(G)\) contained in \(N_G[v]=\{v\}\cup\{w:vw\in E(G)\}\) for some vertex \(v\).

**Theorem.** There is an explicit sequence of elementary simplicial collapses from \(\mathcal N[G]\) to a two-dimensional complex consisting of the graph \(G\) together with two separately triangulated discs spanning each Cartesian square. Consequently,

\[
\boxed{\ |\mathcal N[H\square J]|\simeq (|H|\times|J|)\vee\bigvee^{e_He_J} S^2.\ }
\]

Here \(|H|\) and \(|J|\) mean the one-dimensional CW realizations of the graphs, not discrete vertex sets. If \(b_H=e_H-|V(H)|+1\) and \(b_J=e_J-|V(J)|+1\), then

\[
\pi_1(\mathcal N[G])\cong\pi_1(H)\times\pi_1(J),\qquad
\widetilde H_i(\mathcal N[G];\mathbb Z)\cong
\begin{cases}
\mathbb Z^{b_H+b_J},&i=1,\\
\mathbb Z^{b_Hb_J+e_He_J},&i=2,\\
0,&\text{otherwise}.
\end{cases}
\]

In particular, for all integers \(m,n\ge5\),

\[
|\mathcal N[C_m\square C_n]|\simeq (S^1\times S^1)\vee\bigvee^{mn}S^2.
\]

This is an integral homotopy classification of a natural infinite family. It is not merely a computation of Betti numbers.

## Assumptions and scope

The graph product has vertices \((u,x)\in V(H)\times V(J)\), with an edge when exactly one coordinate changes along a graph edge. Graphs may be trees; no bipartiteness, regularity, or planarity assumptions are made. The hypothesis excludes simple three-cycles and four-cycles **inside either factor**; the product itself contains many four-cycles. Its square faces are indexed by pairs \((uv,xy)\in E(H)\times E(J)\).

For graph edges realized metrically as unit intervals, the complex is also the finite-vertex graph Čech nerve at scale two (closed balls of radius one). This differs from the Lovász **open**-neighborhood complex and from the Vietoris–Rips complex. All complexes here are finite and unweighted.

## Proof

**1. Structure of common neighbors.** A Cartesian product of triangle-free graphs is triangle-free. For distinct nonadjacent vertices \(a,b\in G\), common neighbors are midpoints of length-two walks. There are at most two. Indeed, two different common neighbors give a four-cycle. Because neither factor has a four-cycle, every product four-cycle changes one coordinate in each factor; it is exactly the square associated with some pair of factor edges. Thus \(a,b\) have two common neighbors precisely when they are opposite corners of a product square, and otherwise at most one. Any two neighbors of a vertex \(v=(u,x)\) which change the *same* factor coordinate have \(v\) as their unique common neighbor: a second would create a four-cycle in that factor. Since there are just two coordinate directions, any set of at least three distinct neighbors of \(v\) has a pair of the same direction and therefore cannot be contained in the closed neighborhood of another center. In particular, every face comprising at least three vertices from \(N_G(v)\) belongs to the single generating simplex \(\Delta(N_G[v])\). The vertices in that face are pairwise nonadjacent because \(G\) is triangle-free.

**2. Collapse high-dimensional neighborhood faces.** For each \(v\in V(G)\) and each subset \(A\subseteq N_G(v)\) with \(|A|\ge3\), delete the pair \((A,A\cup\{v\})\), processing pairs in decreasing order of \(|A|\) (and choosing any order within a cardinality). By the unique-center property, different pairs do not overlap and every proper coface of \(A\), other than \(A\cup\{v\}\), has already disappeared when \(A\) is processed. More explicitly, any such coface belongs to the same generating simplex, and either has a larger neighbor subset and was deleted earlier as a lower face or contains \(v\) and was deleted earlier as an upper face. Therefore each removal is an elementary simplicial collapse. The survivors are the graph vertices, all graph edges and all distance-two edges, and triangles \(\{v,a,b\}\) for each pair \(a,b\in N_G(v)\).

**3. Delete unique-midpoint diagonals.** For every pair of distance-two vertices \(a,b\) having exactly one common neighbor \(v\), the surviving diagonal edge \(\{a,b\}\) occurs in exactly one triangle, \(\{v,a,b\}\). Delete this free edge and its triangle. Distinct pairs are disjoint because the diagonal determines its endpoints and unique common neighbor. What remains is a two-dimensional simplicial complex \(L\) with the original graph \(G\), and for every product square with corners \(p,q,r,s\), both diagonals and their four incident triangles. This is exactly the boundary of a tetrahedron on the four square vertices. A diagonal belongs to only one product square, and distinct square boundaries meet in subsets of the original graph \(G\).

**4. Identify the product and sphere summands.** For each product square select one of the two possible triangulated discs spanning its four-edge boundary, namely the two triangles using the same diagonal. Their union, together with \(G\), is a simplicial subdivision of the standard square CW decomposition of the topological product \(|H|\times|J|\). The other two triangles form a second disc with the same boundary loop, attached along a loop already filled by the first disc. Its attaching map is nullhomotopic, and adjoining it wedges on one \(S^2\). Different additional discs have distinct interior diagonals and meet previously attached cells only along the square boundaries. Attach these second discs one at a time. The homotopy pushout for a nullhomotopic attaching circle gives one new two-sphere each time, independently of prior attachments. There are exactly \(e_He_J\) product squares, yielding the asserted integral homotopy equivalence.

**5. Homology and fundamental group.** The product of connected graphs has fundamental group \(\pi_1(H)\times\pi_1(J)\) and first Betti rank \(b_H+b_J\); its second integral homology is the Künneth product \(H_1(H;\mathbb Z)\otimes H_1(J;\mathbb Z)\cong\mathbb Z^{b_Hb_J}\). All higher homology vanishes. Each additional sphere contributes a free \(\mathbb Z\) summand in degree two without changing the fundamental group. This proves the stated formulas, including the torus case.

The number of elementary collapses in Steps 2 and 3 is, with \(d_H(u)=\deg_H(u)\) and \(d_J(x)=\deg_J(x)\), exactly

\[
\sum_{u\in V(H),\,x\in V(J)}\ \sum_{j=3}^{d_H(u)+d_J(x)}\binom{d_H(u)+d_J(x)}{j}
+|V(J)|\sum_{u\in V(H)}\binom{d_H(u)}2
+|V(H)|\sum_{x\in V(J)}\binom{d_J(x)}2.
\]

For the final two-dimensional residue the face vector is
\[
(f_0,f_1,f_2)=\bigl(|V(H)||V(J)|,\ e_H|V(J)|+e_J|V(H)|+2e_He_J,\ 4e_He_J\bigr).
\]

## Verification

Run `python3 verify.py` using only the Python standard library. It directly constructs the original complex by enumerating subsets of every closed graph neighborhood, tests the freeness of **every individual proposed elementary collapse** against the current face set, and compares the remaining face set with an independently generated two-triangulations-per-square complex. It also computes boundary ranks over \(\mathbb F_2\) of the full residual complex, comparing with the predicted homology in degrees one and two. The ten tested products of paths, stars, and cycles include \(C_5\square C_5\) and \(C_5\square C_6\). All ten passed, as recorded in `verify_output.txt` (last line `ALL_VERIFY_OK`). For \(C_5\square C_5\), the execution verified 575 nonempty original faces and 175 actual elementary collapses, leaving face vector \((25,100,100)\) with mod-two Betti ranks \((2,26)\).

The finite tests corroborate, rather than prove, the theorem for arbitrary factor sizes. Its universal validity rests on the unique-common-neighbor argument and the explicit per-face collapse proof above. No independent external validation or equivariant classification is asserted.

## Relationship to prior work

Matsushita, *Closed neighborhood complexes of graphs* (first public version November 16, 2025), introduces the general perspective and proves connections with independence complexes and graph fundamental groups. Its Example 3.5 determines a different Cartesian-product family, \(K_m\square K_n\), whose factors possess triangles and do not satisfy the present hypotheses. A fundamental-group isomorphism alone does not determine the two-dimensional sphere summands here.

Adams, Shukla, and Singh, *Čech complexes of hypercube graphs* (arXiv:2212.05871), determine the scale-two Čech homotopy type of binary hypercubes; those are products of edges, with trivial first fundamental group. Their theorem does not cover products of two high-girth factors with cycles, for which the resulting fundamental group can be \(\mathbb Z^2\) or a product of nonabelian free groups.

The earlier result *A high-girth prism Čech collapse and its integral symmetry modules* determines \(H\square K_2\), a special case of this statement, and is **not claimed as new** here. The separate result *Clique-fiber Čech nerves over graphs of girth at least five* concerns \(H\square K_m\) for \(m\ge3\), where the complete-graph factor contains triangles. The known toroidal-grid **open**-neighborhood theorem concerns a different complex; even for \(C_m\square C_n\) its space is not the closed-neighborhood nerve classified here.

The novel claim is the uniform *two-factor, four-cycle-free* product splitting with non-free direct-product fundamental groups and precisely \(e_He_J\) extra integral two-spheres. No uniqueness-of-prior-work assertion is made.

## Limitations

The theorem assumes both factors are finite connected graphs of girth at least five (with forests allowed). Factors with three- or four-cycles can have additional overlapping neighborhood simplices and are not classified by this proof. The splitting is nonequivariant: it does not specify natural automorphism actions on homology, persistent maps at other Čech scales, or higher-dimensional graph products. Potential unindexed general results for arbitrary graph-square completions remain an originality risk.

## References

1. T. Matsushita, *Closed neighborhood complexes of graphs*, arXiv:2511.12608, first posted November 16, 2025. https://arxiv.org/abs/2511.12608
2. H. Adams, S. Shukla, and A. Singh, *Čech complexes of hypercube graphs*, arXiv:2212.05871, first posted December 12, 2022. https://arxiv.org/abs/2212.05871
3. *A high-girth prism Čech collapse and its integral symmetry modules*, publicly indexed mathematical research record, 2026. https://github.com/published-finding corpus/2026
4. *Clique-fiber Čech nerves over graphs of girth at least five*, publicly indexed mathematical research record, 2026. https://github.com/published-finding corpus/2026
5. *Toroidal grid neighborhood complexes collapse to one or two tori*, publicly indexed mathematical research record, 2026. https://github.com/published-finding corpus/2026
