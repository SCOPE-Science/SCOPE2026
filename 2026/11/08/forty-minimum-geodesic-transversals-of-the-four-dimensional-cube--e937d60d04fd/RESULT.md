# Forty minimum geodesic transversals of the four-dimensional cube

## Finding
Let \(Q_4\) have vertex set \(\{0,1\}^4\), with edges joining binary words differing in one coordinate. A *geodesic transversal* meets every inclusion-maximal shortest path. There are **exactly 40** six-vertex geodesic transversals of \(Q_4\). Every such set belongs to one of the following two explicitly described families, and both families consist entirely of minimum transversals:

1. **Eight middle-sphere sets:** for \(a\in\{0,1\}^4\), take \(A_a=\{x:d_H(x,a)=2\}\). Each has six vertices, with \(A_a=A_{\overline a}\), giving eight distinct sets.
2. **Thirty-two lifted-neighborhood sets:** choose a free coordinate \(i\in\{1,2,3,4\}\) and a word \(b\in\{0,1\}^3\) on the remaining coordinates; take \(B_{i,b}=\{x:d_H(x_{\widehat i},b)=1\}\). There are \(4\cdot8=32\) distinct sets, each inducing three disjoint edges.

Under the full automorphism group of \(Q_4\) (order \(384\)), the 40 sets form exactly two orbits, of sizes \(8\) and \(32\). Their induced subgraphs distinguish the orbits: the first is independent, and the second is a three-edge matching. The known minimum size \(\operatorname{gt}(Q_4)=6\) is not claimed as new; the complete count and orbit/structural classification are the subject of this result.

## Assumptions and scope
All vertices are labelled by their four binary coordinates. Hamming distance \(d_H\) is the number of unequal positions. A maximal geodesic is a shortest path that is not a proper subpath of any longer shortest path in \(Q_4\). The count \(40\) treats two sets with different labelled vertex subsets as distinct, and the two-orbit statement identifies them under coordinate permutations and independent bit flips. No assertion is made for higher-dimensional cubes.

## Proof
**1. Maximal paths.** Along any shortest path in the cube, each coordinate changes at most once. A shortest path of length less than four leaves at least one coordinate unchanged and can be extended by flipping an unused coordinate at an endpoint. Consequently every maximal geodesic has four edges and connects two antipodal words. Conversely, a path obtained by flipping all four coordinates in any order is a maximal geodesic. There are exactly \(16\cdot4!/2=192\) undirected maximal geodesics: each ordered path is paired with its reverse and each undirected path has this unique pair of orderings.

**2. Two constructive families.** Fix a center \(a\). Along an antipodal geodesic, the distance to \(a\) changes by one at every step, while the endpoint distances are \(r\) and \(4-r\) for some integer \(0\le r\le4\). Thus some vertex has distance two from \(a\), proving that every \(A_a\) meets every maximal geodesic. Likewise, project any antipodal geodesic in \(Q_4\) onto the three coordinates other than \(i\). Erasing the one step that changes the free coordinate gives an antipodal geodesic in \(Q_3\). Its successive distances to any fixed \(b\in\{0,1\}^3\) move by one, with endpoints at distances \(r\) and \(3-r\); at least one projected vertex therefore has distance one from \(b\). So every \(B_{i,b}\) is a transversal.

The sets \(A_a\) each have \(\binom42=6\) vertices and satisfy \(A_a=A_{\overline a}\). For distinct centers not related by complementation, their distance-two layers differ. There are exactly eight sets. Each \(B_{i,b}\) consists of the three neighbors of \(b\) in \(Q_3\), each lifted to both values of coordinate \(i\). This gives six vertices inducing three disjoint edges in direction \(i\), so the free coordinate is recovered from the induced matching. Distinct three-bit centers have distinct neighbor sets, giving eight choices per coordinate and 32 in all. Each \(A_a\) is independent by the parity of Hamming weight relative to \(a\); hence the two families are disjoint and yield 40 distinct candidates.

**3. Minimum size.** The established bound of Chen–Ma–Wu [2, Theorem 3.1] gives \(\operatorname{gt}(Q_4)\ge\lceil16/3\rceil=6\), while part 2 gives a six-element construction. Independently of that published bound, the exact finite checker in `artifacts/verify.py` examines all \(\binom{16}{5}=4368\) five-vertex subsets and finds that none meets all 192 maximal geodesics. By upward closure of the hitting property, this excludes all sets of at most five vertices.

**4. Exact exhaustion and orbits.** The exhaustive certificate `artifacts/orbit_certificate.tsv` contains one row for each of the 50 orbits of six-element subsets of \(\{0,1\}^4\) under coordinate permutations and bit flips. Each row records a 16-bit subset mask, the size of its orbit, and either a valid maximal-geodesic bitmask that misses the representative or a zero indicating that the representative hits all 192 maximal geodesics. `artifacts/verify.py` constructs all 384 coordinate/bit-flip automorphisms, expands every recorded orbit, verifies the listed sizes and disjointness, and checks that their disjoint union contains all \(\binom{16}{6}=8008\) candidate subsets. It also independently checks every six-element subset against every maximal geodesic. Precisely two orbits pass, of sizes 8 and 32, and their representatives occur in the families constructed in part 2. As the hitting property is automorphism-invariant, those orbits are exactly the 40 claimed sets. Every failing orbit has a verifiable disjoint maximal-geodesic witness. This proves exhaustiveness without relying on untested sampling or numerical extrapolation.

## Verification
Use Python 3 and no third-party packages. In a directory containing the embedded `artifacts` folder run:

`python3 artifacts/verify.py`

The script reconstructs the 192 paths and 384 automorphisms, checks the two constructive families, enumerates all 4,368 five-subsets and 8,008 six-subsets, and independently replays the 50-orbit certificate with 48 disjoint-path witnesses. Expected final lines:

```
TWO_CONSTRUCTIVE_FAMILIES_OK sphere8=8 prism32=32
NO_FIVE_VERTEX_TRANSVERSALS_OK tested=4368
ALL_SIX_VERTEX_SETS_EXHAUSTED_OK tested=8008 hits=40
FIFTY_AUTOMORPHISM_ORBIT_CERTIFICATE_OK all=8008 accepted_orbits=8,32 rejected=48
VERIFY_OK
```

The proof of this finite classification is exhaustive because the actual program enumerates every subset and certifies full orbit coverage; the result does not extrapolate to larger cubes.

## Relationship to prior work
Manuel–Brešar–Klavžar [1] introduced geodesic-transversal optimization and its equivalent hitting-set perspective. Chen–Ma–Wu [2, 2026-10-29 first public version] study hypercubes, characterize maximal geodesics by antipodal coordinate-flip paths in Remark 2.1, and establish the sharp scalar value \(\operatorname{gt}(Q_4)=6\) in Remark 3.4. Their inspected hypercube section supplies bounds and the scalar value but not a six-element extremizer census or orbit classification. Prabha–Sandhiya–Manuel [3, 2026-11-04 first public version] study geodesic-transversal numbers of hypercube and butterfly networks, not the 40-set classification. The alternative term *maximal shortest paths cover number* is also used in the literature. The new result concerns the enumeration and structural classification of every minimizer, not the scalar value or known middle-layer construction.

## Limitations
This is a finite classification for the labelled four-dimensional hypercube only. It gives no formula for all dimensions and no independent mathematical audit has been performed. A differently formulated extremizer census in unindexed literature cannot be excluded merely because no covering result was found in the searches. The exact finite certificate is independently replayable but was reviewed only at the same-model level.

## References
[1] P. Manuel, B. Brešar, S. Klavžar, *The geodesic-transversal problem*, arXiv:2101.08042v1 (2021-01-20), https://arxiv.org/abs/2101.08042.

[2] S. Chen, X. Ma, T. Wu, *On two problems concerning the geodesic transversal number of graphs*, arXiv:2610.39298v1 (2026-10-29), https://arxiv.org/html/2610.39298v1.

[3] R. Prabha, B. Sandhiya, P. Manuel, *Geodesic Transversal of Hypercube and Butterfly networks*, arXiv:2611.06107v1 (2026-11-04), https://arxiv.org/abs/2611.06107.
