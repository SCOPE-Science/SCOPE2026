# Twenty-one induced octagons govern metric-basis relocation on the Heawood graph

## Finding

The 14-vertex Heawood graph has precisely 168 minimum resolving sets, each of size five. There are 21 induced eight-cycles, and every minimum resolving set is a rotation of the binary pattern 10101101 on exactly one of these octagons. Consequently, its minimum-resolving-set token-slide graph is \(21C_8\), while its token-jump graph is connected, five-regular, of radius and diameter five. The latter has 420 edges and the former has 168 edges. The octagon indexing is intrinsic to the host graph, not an arbitrary naming of the 21 components.

## Assumptions and scope

Write the vertices as \(P_i\) and \(L_j\), with \(i,j\in\mathbb Z/7\mathbb Z\). Include exactly the 21 edges \(P_iL_j\) satisfying \(i-j\in\{0,1,3\}\). This is the point-line incidence graph of the Fano plane. A subset \(S\) resolves the graph if each of its 14 vertices has a different ordered vector of distances to the elements of \(S\). A *metric basis* is a resolving set of smallest possible cardinality. In the reconfiguration graphs, every state is an unordered five-element metric basis; a jump replaces exactly one selected vertex by any unselected vertex; a slide is a jump whose removed and added vertices are adjacent in the host. Every intermediate state must be a metric basis.

An *induced octagon* is an eight-element vertex subset whose induced subgraph is a connected cycle of length eight. For a cyclic vertex order \((v_0,\ldots,v_7)\), a rotation of pattern 10101101 selects the five positions carrying a one. The reverse cyclic order generates the same eight selected subsets in this graph; either orientation may be used.

## Proof

**The minimum size and its complete census.** In an incidence graph of a projective plane of order two, distances between two distinct vertices of the same part are two, and distances between opposite parts are one or three. Let a selected set contain \(p\) points and \(\ell\) lines. Selected vertices distinguish themselves by a zero distance. Unselected points must have pairwise different incidence signatures on the \(\ell\) selected lines; unselected lines must have pairwise different incidence signatures on the \(p\) selected points. These conditions are also sufficient because opposite-side vertices have different distance parity to any selected vertex. Therefore a necessary condition is
\[
7-p\leq2^{\ell},\qquad7-\ell\leq2^p.
\]
For every \(p+\ell\leq4\), at least one inequality fails. For five selected vertices, the only possible part counts are \((p,\ell)=(3,2)\) and \((2,3)\).

Fix any pair of selected lines. The signatures of the seven points with respect to those two lines occur with multiplicities \(1,2,2,2\): their common point has signature 11, the two exclusive pairs have signatures 10 and 01, and the two points outside their union have signature 00. To distinguish the four unselected points, the three selected points must consist of exactly one point from each size-two signature class. This yields eight possibilities. For the representative selected lines \(L_0,L_1\), the classes are: 00 = \(\{P_5,P_6\}\); 01 = \(\{P_2,P_4\}\); 10 = \(\{P_0,P_3\}\); 11 = \(\{P_1\}\). Among the eight triples, exactly
\[
\{P_5,P_2,P_0\},\quad\{P_5,P_4,P_3\},\quad\{P_6,P_2,P_3\},\quad\{P_6,P_4,P_0\}
\]
also separate all five unselected lines. This is verified directly against their three-bit incidence signatures. The collineation group of the Fano plane acts transitively on pairs of lines (equivalently, on pairs of independent nonzero dual vectors of \(\mathbb F_2^3\)), so each of the \(\binom72=21\) selected line pairs supports exactly four such three-point selections. This gives 84 bases of type three points/two lines. The duality interchanging points and lines yields 84 more bases of the opposite type, for exactly 168.

**Octagon indexing.** The reproducible finite enumeration described below exhausts all \(\binom{14}{8}=3003\) eight-vertex subsets, using the logically equivalent octagon criterion that the induced subgraph is connected and every one of its eight vertices has induced degree two. It finds precisely 21 induced octagons. On each octagon, the eight cyclic rotations of 10101101 are distinct resolving sets. The 21 families of eight are pairwise disjoint, and their union is the 168 bases just classified. This proves both that the octagon containing a given basis is unique and that every basis has the prescribed occupancy pattern. These are finite checked facts, with the complete executable tests provided as part of this result.

**Exact transition graphs.** Enumerate the 168 states using the incidence-signature test above. Two states are joined under jumping exactly when their intersection has four elements. For sliding, the corresponding two vertices in their symmetric difference must additionally be adjacent in the 21-edge host. The two independently implemented exhaustive checkers reconstruct all such pairs. Both obtain 168 slide edges and degree two at every slide state. Every slide component has eight states and their union is the vertex set of one of the 21 induced octagons. Connectedness and degree two show that each component is \(C_8\). In the jump graph, all 168 states have degree five and there are 420 edges. Breadth-first search from each of the 168 states reaches all states, with maximum distance exactly five. Thus the jump graph is connected and has radius and diameter five. These are certified finite exhaustive conclusions, not extrapolations from sampling.

## Verification

All artifacts are included with this result. From the artifact root, run:

```bash
python3 verification/check_fano.py
g++ -std=c++17 -O2 -Wall -Wextra -pedantic verification/check_fano.cpp -o check_fano
./check_fano
```

The Python checker uses breadth-first host distances and ordered distance vectors, exhausts 1,001 four-subsets and 2,002 five-subsets, enumerates induced octagons, constructs the eight rotations of each occupancy pattern, checks pairwise disjointness and equality with all metric bases, and constructs both reconfiguration graphs. The C++17 checker independently encodes vertices and states by bitmasks, checks the pairwise distance-separation condition, enumerates 8-subsets through induced-degree tests, and computes transition components and all-state eccentricities. Both produce the recorded successful output files. Integer comparisons and finite loops are exact.

## Relationship to prior work

Héger and Takáts, first publicly posted July 23, 2012, prove in Remark 2.6 that the Fano-plane incidence graph has metric dimension five. Their Proposition 2.2 gives incidence conditions for resolving sets. That minimum-cardinality fact and their general criteria are prior work, not new claims here. Their relevant inspected text does not enumerate the 168 minimum resolving sets or characterize either of the reconfiguration graphs. Their main large-order projective-plane classification applies to order at least 23, not to this 14-vertex host.

Avis and Hoang study token-slide reconfiguration for *independent sets*, which have a different feasibility condition; their general token-graph definitions do not give the resolving-set state classification on the Heawood graph. The standard Fano-plane/Heawood incidence and symmetry data are background. Published summaries and semantic research-record searches were compared under the aliases *Heawood graph*, *Fano incidence graph*, *projective plane of order two*, *resolving set exchange*, *landmark relocation*, *token jumping* and *token sliding*. No established result encountered implies the present 21-octagon, 168-state reconfiguration classification.

## Limitations

This is an exact result for one canonical finite host graph, not a statement for all projective-plane incidence graphs or all cubic bipartite graphs. The distances and component isomorphisms are verified by complete, small, deterministic enumeration; the abstract octagon correspondence beyond this particular host is not asserted. The status of inaccessible, unpublished, or unindexed equivalent historical calculations remains uncertain. The older source's minimum metric dimension is not being claimed as new. Independent scholarly audit has not been performed.

## References

1. Tamás Héger and Marcella Takáts, *Resolving sets and semi-resolving sets in finite projective planes*, first posted July 23, 2012, arXiv:1207.5469, especially Definition 1.1, Proposition 2.2, Remark 2.6. https://arxiv.org/abs/1207.5469 and full HTML https://arxiv.org/html/1207.5469v3.
2. David Avis and Duc A. Hoang, *On Reconfiguration Graphs of Independent Sets under Token Sliding*, first posted March 31, 2022, arXiv:2203.16861, especially Introduction and Definitions in Section 3. https://arxiv.org/abs/2203.16861.
3. John Baez, *Heawood Graph*, AMS Visual Insight, August 1, 2015. https://blogs.ams.org/visualinsight/2015/08/01/heawood-graph/.
