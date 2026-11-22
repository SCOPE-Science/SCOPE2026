# An elementary collapse of the full Clebsch independence-complex symmetry quotient

## Finding
Let \(C\) denote the **five-regular** Clebsch graph, also called the folded five-cube. Let \(X=\operatorname{Ind}(C)\) be the ordinary independence complex and let \(G=\operatorname{Aut}(C)\). The entire geometric orbit space of this action has an explicit regular CW cellulation admitting nineteen elementary collapses to one vertex:

\[
\boxed{\lvert X\rvert/G\searrow\{\mathrm{point}\}.}
\]

In particular, the quotient is integrally contractible and has trivial simple-homotopy type, not merely vanishing rational homology. Its barycentric orbit-cell counts in dimensions zero through four are respectively \((6,13,13,6,1)\), totaling 39 cells. This statement does **not** assert that \(X\) itself is contractible; indeed, its ordinary homotopy type is previously known to be a wedge of nine three-spheres.

## Assumptions and scope
Identify the vertices of \(C\) with the sixteen even-parity vectors \(x\in\mathbb F_2^5\). Distinct vertices \(x,y\) are adjacent precisely when the Hamming weight of \(x+y\) is four. Thus \(C\) is five-regular with 40 undirected edges; it is not the ten-regular complement also sometimes called the Clebsch graph. A face of \(X\) is a nonempty set of vertices with no adjacent pair, with the empty face included only in augmented-chain conventions.

Translations by even-parity vectors, together with coordinate permutations, form the complete automorphism group
\[
G\cong(\mathbb Z/2)^4\rtimes S_5,\qquad |G|=1920.
\]
This is an action on a finite simplicial complex; \(\lvert X\rvert/G\) denotes its ordinary **geometric** orbit space, not the orbit set of unordered faces or a homotopy-orbit space. Here \(\searrow\) means a sequence of genuine elementary collapses of a regular CW complex.

## Proof
**1. Exhausting the graph and its full group.** The distance-four adjacency rule gives 40 edges, with five neighbors per vertex. Two adjacent vertices have zero common neighbors and two nonadjacent vertices have exactly two common neighbors. The ten nonneighbors of any fixed vertex are individually determined by their respective pairs of common neighbors with it. Consequently a graph automorphism is uniquely specified by the image of a fixed vertex (at most 16 choices) and a permutation of its five neighbors (at most 120 choices). The exhibited translation-permutation group contains exactly \(16\cdot120=1920\) distinct automorphisms and reaches this upper bound. The standalone checker enumerates and confirms all 1,920 maps.

**2. Building the actual quotient.** Exhaustive independent-set enumeration produces 392 nonempty faces, with dimension counts
\[
 (f_0,f_1,f_2,f_3,f_4)=(16,80,160,120,16).
\]
Barycentrically subdivide \(X\): its simplices are strict nonempty chains of faces \(F_0\subsetneq\cdots\subsetneq F_k\). There are exactly 19,992 such chains, enumerated in `verify_clebsch_quotient.py`. The group acts on these chains by applying the same graph automorphism to every face. Because automorphisms preserve face cardinalities, a group element stabilizing a chain setwise fixes every vertex of the chain: the action has no inversions. Therefore the quotient is a regular CW complex whose cells are orbits of chains. Within an individual chain, different subchains have distinct sequences of face cardinalities; hence they cannot be identified in the quotient. This ensures that the boundary of each orbit cell embeds as a union of lower-dimensional quotient cells, rather than containing folded or self-identified faces.

Four translations by the vectors \(e_1+e_i\), for \(i=2,3,4,5\), and four adjacent coordinate transpositions generate \(G\). Taking connected components of their action on all 19,992 chains yields 39 chain orbits, with cell counts \((6,13,13,6,1)\). The supplied certificate records one representative chain for each orbit, ordered deterministically by ascending integer vertex-face masks. The full cellular incidence table is reconstructed by deleting each position from these representative chains. Every codimension-one boundary face occurs at most once in a cell boundary, and the oriented cellular boundary operators satisfy \(\partial^2=0\) over \(\mathbb Z\).

**3. Explicit elementary collapse.** The accompanying `collapse_certificate.json` lists 19 ordered pairs of quotient cells, each consisting of a free codimension-one face and its unique remaining coface. The verifier independently reconstructs all 39 cells and their complete incidence lists, then checks for every pair that its lower cell has precisely one active coface, the proposed upper cell. Before and after every deletion it checks that all remaining cells are closed under taking faces. Exactly one zero-cell survives after the 19 pairs are deleted, so this is an elementary-collapse sequence of a regular CW complex, proving the boxed statement. In particular, integral torsion and nontrivial fundamental group in the quotient are ruled out without reliance on rational transfer or a homology-only calculation.

## Verification
From a directory containing the two attached artifacts, run `python3 verify_clebsch_quotient.py collapse_certificate.json` with Python 3.10 or later; no nonstandard dependencies or external input are needed. Successful output is `CLEBSCH_FULL_SYMMETRY_QUOTIENT_19_COLLAPSES_PASS`. The checker verifies the graph and group normalization, all independent faces and strict flags, the orbit count and dimension vector, the exact representative chains, quotient cellular incidences, integral boundary identities, nineteen free-face deletions, and the one-vertex survivor. A complete finite certificate is supplied; the computation does not imply any theorem for larger folded cubes or other graph complexes.

## Relationship to prior work
Engström (first posted 2005-08-08) studies combinatorial topology of graph independence complexes, supplying the historical independence-complex setting. Kozlov (first posted 2005-03-28) develops explicit simple-homotopy comparisons for other graph complexes; the latter is methodological background, not a statement about this quotient. The pre-existing precise calculations on the **same five-regular Clebsch independence complex** show that \(X\simeq\bigvee^9S^3\) and determine the 1,920-element rational homology character. These results already imply that the full quotient is rationally acyclic, but they do not imply integrally that the orbit space is contractible or supply an elementary collapse. In particular, the full Weyl-group homology-character result explicitly limits its quotient consequence to rational homology. The related Clebsch open-neighborhood complex, despite sharing a graph and symmetry group, is a distinct topological object and cannot provide the present quotient collapse. The new contribution is precisely the geometrically verified full-orbit collapse and its integral homotopy consequence.

## Limitations
The result concerns only the sixteen-vertex five-regular Clebsch graph and the full 1,920-element graph automorphism group. It does not determine orbit spaces for other subgroups, the integral representation on labeled homology, or any general folded-cube family. The elementary-collapse certificate proves an exact finite statement when its explicit definitions and reconstruction algorithm are accepted. Literature comparisons include relevant fully read prior mathematical claims but cannot eliminate unindexed or inaccessible equivalent results. No independent mathematical audit of the new finite proof has been carried out.

## References
1. A. Engström, *Complexes of Directed Trees and Independence Complexes*, arXiv:math/0508148v1, first publicly posted 2005-08-08. https://arxiv.org/abs/math/0508148
2. D. N. Kozlov, *Simple homotopy types of Hom-complexes, neighborhood complexes, Lovász complexes, and atom crosscut complexes*, arXiv:math/0503613, first publicly posted 2005-03-28. https://arxiv.org/abs/math/0503613
3. *Nine three-spheres and the \(4\oplus5\) symmetry module of the folded five-cube*, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-nine-three-spheres-and-the-4-oplus5-symmetry-module-of-the-folde--25933f5ba2c9
4. *Complete rational automorphism-homology character of the Clebsch independence complex*, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-complete-rational-automorphism-homology-character-of-the-clebsch--f1606ba6b0dd
5. *Nine three-spheres and the full Weyl-group homology character of the folded five-cube independence complex*, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-nine-three-spheres-and-the-full-weyl-group-homology-character-of--30925c4a241b
