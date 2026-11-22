# Three isolated edge-multiset resolving layers of the Desargues graph

## Finding

Let \(D\) be the Desargues graph, realized as the inclusion graph between the ten two-subsets and ten three-subsets of \([5]\). For a vertex set \(S\) and edge \(e=uv\), let \(h_e(S)\) be the histogram of the values \(d(w,e)=\min\{d(w,u),d(w,v)\}\) for \(w\in S\), with distance levels \(0,1,2,3,4\). A set \(S\) *edge-multiset resolves* \(D\) when these five-entry histograms differ for every two of the thirty edges.

The complete cardinality polynomial of resolving sets is
\[
\boxed{R_D(z)=720z^{8}+960z^{10}+720z^{12}.}
\]
In particular, the edge-multiset dimension is \(8\); there are exactly \(720\) minimum resolving sets, and no resolving sets of odd cardinality. All resolving sets are destroyed by adding just one new vertex. The minimum sets form exactly three orbits under the full automorphism group of \(D\), each of cardinality \(240\). In the respective orbits, the selected vertices induce exactly \(4\), \(5\), and \(6\) graph edges.

## Assumptions and scope

The graph is the finite, simple, unweighted twenty-vertex graph \(D=H(5,2)\), also represented by \(GP(10,3)\). Its vertex set consists of all subsets of \([5]\) having size two or three, with adjacency between a two-set and a three-set exactly when the former is contained in the latter. Vertices and edges are labelled for enumeration; resolving subsets themselves are unordered. The empty set is not resolving. No statement is made about other generalized Petersen graphs.

## Proof

**The histogram criterion.** For the specified graph, adjacent subsets differ in exactly one of the five ground elements. A breadth-first search from every vertex gives exact graph distances. For every edge \(e=uv\), define five bitmasks \(M_{e,j}=\{w\in V(D):\min(d(w,u),d(w,v))=j\}\) for \(0\le j\le4\). For a candidate landmark mask \(S\), the edge histogram is the ordered five-tuple \((|S\cap M_{e,0}|,\ldots,|S\cap M_{e,4}|)\). Equality of these tuples is exactly equality of the corresponding edge-distance multisets, because their distance values lie in \(\{0,1,2,3,4\}\).

**Finite exhaustive count.** The file `verify_bitsets.cpp` traverses every integer mask from \(0\) to \(2^{20}-1\), constructs the thirty tuples by integer population counts, and accepts the mask if and only if the thirty tuples are distinct. Five counts are packed in disjoint five-bit fields, which is injective because every count is between zero and twenty. The complete exact tally is \(720\) at size eight, \(960\) at size ten, and \(720\) at size twelve, zero at all other sizes. This is a finite proof because every candidate subset appears exactly once; it is not an inference from a sample or a numerical extrapolation. The separately implemented program `verify_gray.cpp` uses the standard generalized-Petersen presentation and updates the thirty histograms under Gray-code traversal, independently obtaining the same exhaustive tally.

**Symmetry and orbit classification.** The natural permutations of \([5]\), together with the complement involution \(X\mapsto[5]\setminus X\), generate \(240\) automorphisms. They are all the automorphisms: a graph automorphism either preserves or exchanges the two bipartition classes; preserving automorphisms induce automorphisms of the triangular graph on the ten two-subsets, in which adjacency is equivalently the existence of a common three-subset neighbor. The five unique maximum four-cliques in that triangular graph are the stars of the five ground elements, hence its automorphism group is \(S_5\). Exchanging the parts is achieved by the complement involution.

With the vertices ordered as the ascending five-bit integers of Hamming weights two or three, the three minimum-set representatives have integer masks `3534`, `5582`, and `5933`. Their induced-edge counts are respectively \(4\), \(5\), and \(6\), so their orbits are disjoint. The exact verification in `verify_orbits.py` constructs all \(240\) group elements, obtains one orbit of size \(240\) from each representative, and checks that their disjoint union equals the explicit `min_masks.txt` list of all \(720\) minimum resolving masks. Thus these are exactly the three orbits under the full automorphism group.

**Complementary landmark duality.** Every graph edge has the same full-vertex edge-distance histogram, namely \((2,4,8,4,2)\); this also follows from edge transitivity. Hence \(h_e(V(D)\setminus S)=(2,4,8,4,2)-h_e(S)\), so \(S\) resolves exactly when its complement resolves. This explains the symmetry of the coefficient counts at sizes eight and twelve. The absence of all odd-size resolving sets is the exact finite certificate above, and proves the stated one-landmark fragility.

## Verification

Compile and run `verify_bitsets.cpp` and `verify_gray.cpp` as C++17 programs; both print the complete nonzero coefficient sequence `8:720 10:960 12:720` and terminate with an exact success marker. Run `verify_bitsets.cpp min_masks_replay.txt` to regenerate the full minimum-set certificate and compare it byte-for-byte with `min_masks.txt`. Execute `verify_orbits.py` to check all \(720\) certificate sets, the full \(240\)-element group action, and the three representative orbits. All computations are exact integer operations, without tolerances or random choices.

## Relationship to prior work

Ikhlaq, Ismail, Siddiqui and Nadeem introduced the edge-multiset dimension and studied paths, cycles, and other graph families. Their small-distance obstruction concerns graphs in which all vertex-to-edge distances are at most two, whereas \(D\) has vertex-to-edge distance four. The known ordinary edge-metric results on generalized Petersen graphs concern *ordered distance vectors*, not multisets, and do not imply the present census. Work on the edge-multiset dimension of hypercubes treats a different graph family. The nonmonotone three-layer polynomial and symmetry orbits are not recovered from these results.

## Limitations

The conclusion is an exact finite classification for one labelled graph. It depends on the fully specified and reproducible exhaustive enumeration; the code and certificates are part of the proof, not a substitute for an unstated infinite argument. No theorem about an infinite family is asserted. The literature comparison is based on accessible primary texts and relevant indexed records, and cannot rule out all unpublished or unindexed earlier computations. Independent external validation has not been performed.

## References

- H. M. Ikhlaq, R. Ismail, H. M. A. Siddiqui and M. F. Nadeem, “A New Technique to Uniquely Identify the Edges of a Graph,” *Symmetry* 15 (2023), 762, https://doi.org/10.3390/sym15030762 (public 20 March 2023).
- J. Allikvere, “The edge multiset dimension of hypercubes,” arXiv:2608.09983 (2026), https://arxiv.org/abs/2608.09983.
- V. Filipović, A. Kartelj and J. Kratica, “Edge metric dimension of some generalized Petersen graphs,” *Results in Mathematics* 74 (2019), 182, https://doi.org/10.1007/s00025-019-1105-9 (ordinary edge-metric, not multiset).
