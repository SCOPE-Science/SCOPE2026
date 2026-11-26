# A derangement classification of the six-dimer Heawood orbits

## Finding

Let \(M\) be a maximal matching of size six in the Heawood graph, viewed as the point–line incidence graph of the Fano plane. Its unmatched vertices are a point \(p\) and a nonincident line \(\ell\). Define
\[
d(M)=\#\{xy\in M:x\in N(\ell),\ y\in N(p)\},
\]
where \(x\) is a point, \(y\) is a line, and \(N\) denotes graph neighbors. The integer \(d(M)\) takes precisely the values \(0,2,3\) and is a **complete invariant** under the full graph automorphism group. For each fixed nonincident pair \((p,\ell)\), the matching is determined by a subset \(D\) of the three points of \(\ell\) and a derangement on \(D\); here \(|D|=d(M)\). The three orbits are:

| \(d(M)\) | Matchings for each fixed unmatched pair | Orbit size | Probability of each labelled matching under i.i.d. edge-priority adsorption |
|---:|---:|---:|---:|
| 0 | 1 | 28 | \(261/98560\) |
| 2 | 3 | 84 | \(91723/23950080\) |
| 3 | 2 | 56 | \(8257/1995840\) |

Thus a local incidence count distinguishes the three weight classes of six-dimer outcomes. The numerical output weights are taken from the separate exact matching-output census [1]; the result here explains their symmetry classes and gives an invariant to recognize them without listing the matchings or computing any probabilities.

## Assumptions and scope

Points are the nonzero vectors of \(V=\mathbb F_2^3\); lines are kernels of nonzero linear forms on \(V\). Incidence means that a form vanishes on a vector. The structural result concerns inclusion-maximal matchings of size six, not arbitrary matchings of size six or maximum matchings. The probability column refers to a single irreversible run in which the edges are processed in ascending order of i.i.d. continuous priorities and an edge is accepted if both endpoints remain vacant. No orbit assertion about other terminal sizes is needed.

## Proof

**The unmatched pair and coordinates.** A size-six matching leaves one point and one line uncovered. It is maximal exactly when they are nonincident, since their connecting edge would otherwise be the only available addition. Fix such a pair and write \(\lambda\) for the form defining \(\ell\). Since \(\lambda(p)=1\), we have \(V=U\oplus\langle p\rangle\) for \(U=\ker\lambda\). Let \(x_1,x_2,x_3\) be the nonzero vectors of \(U\). The six remaining points are the \(x_i\) and \(p+x_i\). Let \(y_i\) be the unique nonzero linear form with \(y_i(p)=0\) and \(y_i(x_i)=0\); the restriction of \(y_i\) to \(U\) takes value one on the other two nonzero vectors. The six remaining lines are represented by \(y_i\) and \(y_i+\lambda\) for \(i=1,2,3\). Here \(N(p)\) consists of the three \(y_i\), and \(N(\ell)\) of the three \(x_i\).

**Derangement description.** In the graph with \(p,\ell\) removed, point \(x_i\) is adjacent precisely to the lines represented by \(y_i\) and \(y_i+\lambda\). Point \(p+x_i\) is adjacent to \(y_i\) and the lines \(y_j+\lambda\) for \(j\ne i\). These assertions follow using \(\lambda(x_i)=0\), \(\lambda(p)=1\), and the values of \(y_i\) above. Let \(D\) be the set of \(x_i\) matched to \(y_i\). If \(x_i\notin D\), then \(x_i\) is matched to \(y_i+\lambda\) and \(p+x_i\) must be matched to \(y_i\), because no other remaining point is adjacent to the unused \(y_i\). For \(x_i\in D\), the remaining point \(p+x_i\) must be matched to \(y_j+\lambda\) with \(x_j\in D\) and \(j\ne i\). These choices define exactly a fixed-point-free permutation of \(D\), and every such pair \((D,\pi)\) reconstructs a matching. The empty set gives one matching, a two-element set gives one transposition (three choices of subset), and the three-element set gives two three-cycles. A singleton has no derangement. The edges from \(N(\ell)\) to \(N(p)\) in the matching are precisely the edges from \(x_i\in D\) to \(y_i\), so \(d(M)=|D|\).

**Orbits.** Linear isomorphisms of \(V\) act by graph automorphisms and are transitive on nonincident point–line pairs: map a basis of one kernel and its complementary vector \(p\) to the corresponding vectors for another pair. For a fixed pair, every linear automorphism of \(U\) extends fixing \(p\), so its action on the three nonzero vectors of \(U\) gives all of \(S_3\): an ordered pair of distinct nonzero vectors is a basis and determines the third by addition. It permutes the choices of \(D\) and conjugates their derangements. This is transitive on each of the three types, including the two three-cycles. No graph automorphism can merge different types: \(d(M)\) counts matching edges between the neighborhoods of the two uncovered vertices and is unchanged even when their roles are interchanged. Each point is nonincident with four lines, giving \(7\cdot4=28\) pairs and hence orbit sizes \(28,84,56\).

**Connection to the known weights.** The priority law is invariant under each graph automorphism, so a labelled matching probability is constant within an orbit. The exact census [1, Finding and Proof] establishes three distinct weights at size six; their multiplicities are \(28,84,56\). Since there are exactly three orbits and three weights, no weight class can combine two of the orbits, and their distinct multiplicities identify the probability column. It is the geometric identification of the classes, rather than the weights themselves, that is asserted here.

## Verification

`python3 check_six_orbits.py` enumerates all bijections of the remaining vertices for each of the 28 nonincident pairs in the binary model, confirms their derangement description and stabilizer transitivity, and independently checks the three weights for representatives by exact rational summation over accepted edge orders. The analytic argument above proves completeness and invariance under the full graph automorphism group without relying on the exhaustive calculation.

## Relationship to prior work and limitations

The exact Heawood output distribution in [1] lists the same six-edge weight-class multiplicities and probabilities. A list of weights need not distinguish graph automorphism orbits: several orbits could have a single weight. The derangement model and the invariant \(d(M)\) supply the structural comparison. The separate records share a catalogue date, from which no order of publication is inferred. General greedy matching and random sequential adsorption frameworks [2,3] give the underlying selection process and do not identify the three local incidence types. This classification applies to the Fano incidence graph only, and the probability identification does not extend to non-invariant priority laws. Historical priority for the structural lemma is not established beyond the inspected evidence.

## References

1. *Exact random-priority dimer jamming and matching-output weights on the Heawood graph*, Resultary, record `538d2c590718`, https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-exact-random-priority-dimer-jamming-and-matching-output-weights--538d2c590718/RESULT.md.
2. M. D. Penrose and A. Sudbury, *Exact and approximate results for deposition and annihilation processes on graphs*, Ann. Appl. Probab. 15 (2005), 853–889, https://arxiv.org/abs/math/0503519.
3. D. Gamarnik and D. A. Goldberg, *Randomized greedy algorithms for independent sets and matchings in regular graphs: Exact results and finite girth corrections*, https://arxiv.org/abs/0807.1277.
