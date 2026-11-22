# Lower mutual-visibility rigidity in the six-dimensional hypercube

## Finding
Let \(Q_6\) be the simple graph on all six-bit strings, adjacent exactly when their Hamming distance is one. A set \(S\) is *mutual-visible* if every two distinct vertices of \(S\) admit a shortest path whose internal vertices avoid \(S\). Such a set is *inclusion-maximal* if no additional vertex can be added while preserving mutual visibility. Then
\[
\boxed{\mu^-(Q_6)=7.}
\]
There are exactly \(64\) inclusion-maximal mutual-visible sets of minimum cardinality. They are precisely the \(64\) closed neighborhoods \(N[v]\), one for each vertex \(v\) of \(Q_6\). In particular, no inclusion-maximal mutual-visible set has at most six vertices, and there are no other seven-vertex inclusion-maximal sets.

## Assumptions and scope
All vertices are labelled by integers \(0,\ldots,63\) in binary. Bit \(j\) is coordinate \(j\), for \(0\le j\le5\). Edges change one coordinate. The parameter \(\mu^-(G)\) is the *lower ordinary mutual-visibility number* (minimum cardinality among inclusion-maximal ordinary mutual-visible sets), not the maximum mutual-visibility number \(\mu(G)\), nor a total/outer/dual variant. No assertion is made for arbitrary cube dimension.

## Proof
**Closed neighborhoods yield 64 witnesses.** Fix a vertex \(v\). Its six neighbors are obtained by flipping each of the six coordinates in turn. Two different neighbors have a length-two path through the vertex obtained by flipping both corresponding coordinates. This middle vertex lies outside \(N[v]\); all other selected vertex pairs are adjacent or satisfy this condition. Thus \(N[v]\) is mutual-visible. Any vertex outside \(N[v]\) is at distance at least two from \(v\), and every shortest path from \(v\) to it starts through a vertex in \(N(v)\), already selected. Therefore adding the outside vertex destroys mutual visibility. Hence every \(N[v]\) is inclusion-maximal, of size seven. Since the induced graph on \(N[v]\) is a six-leaf star with unique center \(v\), all \(64\) are distinct.

**Exact finite lower bound and uniqueness.** Encode \(S\) by the unsigned 64-bit integer \(m(S)=\sum_{v\in S}2^v\). For any pair \(a<b\), write \(D(a,b)\) for their differing coordinate positions. Every shortest \(a,b\)-path flips each member of \(D(a,b)\) exactly once, in an arbitrary permutation. Thus a pair is \(S\)-visible if and only if at least one of those permutation paths has its entire internal-vertex mask disjoint from \(m(S)\). Apply this test to each pair in \(S\) to decide mutual visibility. Given a feasible \(S\), maximality is equivalent to failure of the same test for \(S\cup\{w\}\) for *each* \(w\notin S\), because mutual visibility is hereditary under taking subsets.

For any chosen \(u\in S\), coordinatewise XOR translation by \(u\) is a graph automorphism taking \(u\) to the all-zero vertex. It preserves the two predicates. Consequently it is exhaustive to enumerate all \(k\)-vertex sets containing zero. Their number is \(\binom{63}{k-1}\). The standalone `verify_permutations.cpp` enumerates all of these for each \(2\le k\le7\) without sampling, enumerates *all* shortest paths for each tested pair, and checks every possible one-vertex extension. Its exact output is:

| \(k\) | Sets containing zero | Mutual-visible sets | Inclusion-maximal sets |
|---:|---:|---:|---:|
| 2 | 63 | 63 | 0 |
| 3 | 1,953 | 1,953 | 0 |
| 4 | 39,711 | 39,696 | 0 |
| 5 | 595,665 | 594,440 | 0 |
| 6 | 7,028,847 | 6,982,332 | 0 |
| 7 | 67,945,521 | 66,836,889 | 7 |

The exact seven maximal seven-subsets containing zero are all checked, by the executable, to equal \(N[v]\) for one of the seven centers \(v\in N[0]\). Empty and singleton sets plainly extend in this connected nontrivial graph. Hence no maximal set has cardinality below seven. Conversely every minimum maximal set can be translated to one of the seven just listed, so every such set is a closed neighborhood. Together with the first paragraph this proves the theorem and the count \(64\).

**Why the enumeration is exhaustive.** In the C++ checker, Gosper's fixed-cardinality successor enumerates each \((k-1)\)-subset of the remaining 63 vertices exactly once, starting from the least such subset and terminating at the first mask outside those 63 bits. A shortest hypercube path cannot flip any coordinate twice, since its length must equal Hamming distance; hence the permutations exhaust all shortest paths. The code's `mutual` and `inclusion_maximal` predicates therefore implement the mathematical definitions exactly. This is an exhaustive finite proof, not a sample extrapolation.

## Verification
Reproduce with a C++17 compiler in the directory containing the two supplied source files:

```sh
g++ -std=c++17 -O3 verify_permutations.cpp -o verify_permutations
./verify_permutations
g++ -std=c++17 -O3 verify_lattice.cpp -o verify_lattice
./verify_lattice
```

The first program must end with `PERMUTATION_VERIFY_OK`; it exhaustively handles every cardinality through seven after translation normalization, including 67,945,521 seven-subsets containing zero. The second program must end with `LATTICE_VERIFY_OK`; it independently checks the absence of smaller maximal sets using monotone-lattice dynamic programming, verifies every closed-neighborhood witness, and obtains the same exact counts through cardinality six. Source code and the expected terminal output for the first program are included. No unproved infinite-dimensional claim depends on these computations.

## Relationship to prior work
Brešar and Yero, *Lower (total) mutual-visibility number in graphs* (first arXiv public version 2023-07-06), introduce the lower ordinary parameter, prove a neighborhood criterion yielding the *upper bound* \(\mu^-(Q_6)\le7\), and pose the determination of lower visibility for hypercubes as a problem. Their lemma does not give the matching lower bound, the exact number, or the rigidity classification here. Korže and Vesel, *Variety of mutual-visibility problems in hypercubes* (arXiv 2024-05-09), give \(\mu(Q_6)=32\) and other *maximum-size* variants. These concern different optimization quantifiers and do not imply the lower *inclusion-maximal* result. Related records about total mutual visibility on \(Q_7,Q_8\) and distance-limited upper visibility likewise do not cover ordinary lower visibility on \(Q_6\).

## Limitations
The theorem is a rigorously finite result specifically for the six-dimensional binary cube; it is not an all-dimension theorem, and the equality \(\mu^-(Q_n)=n+1\) for arbitrary \(n\) is not claimed. The decisive exclusion is exhaustive computer-assisted enumeration, whose trust requires C++17 implementation and ordinary finite arithmetic. Publication priority remains subject to further bibliographic review and independent expert validation.

## References
1. Boštjan Brešar and Ismael G. Yero, *Lower (total) mutual-visibility number in graphs*, arXiv:2307.02951, first public 2023-07-06, https://arxiv.org/abs/2307.02951.
2. Danilo Korže and Aleksander Vesel, *Variety of mutual-visibility problems in hypercubes*, arXiv:2405.05650, first public 2024-05-09, https://arxiv.org/abs/2405.05650.
