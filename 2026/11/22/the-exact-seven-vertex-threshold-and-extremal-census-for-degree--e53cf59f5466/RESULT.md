# The exact seven-vertex threshold and extremal census for degree-two cut immunity

## Finding

A **degree-two cut** (or **2-cut**) of a finite simple graph is a partition of its vertex set into two nonempty shores such that every vertex has at most two neighbors on the opposite shore. A graph is **2-immune** if no 2-cut exists. Write \(\mu_2(7)\) for the minimum number of edges of a 2-immune simple graph on seven vertices.

**Theorem (complete seven-vertex extremal census).**
\[
\mu_2(7)=14.
\]
More precisely, on a fixed labelled vertex set of seven elements, there are exactly \(15{,}015\) 2-immune graphs with fourteen edges; they fall into exactly ten classes under vertex relabeling. The class representatives and their orbit sizes are explicitly given in `representatives.tsv`. Their orbit sizes in that order are
\[
105,2520,2520,1260,2520,1260,630,2520,1260,420,
\]
whose sum is \(15{,}015\). Every graph with at most thirteen edges admits a 2-cut.

## Assumptions and scope

Graphs are simple, undirected, loopless, without parallel edges; the vertex set is exactly \(\{0,1,2,3,4,5,6\}\) for the labelled count, and isolated vertices are allowed in the search. There are exactly \(\binom72=21\) possible edges. The fourteen-edge minimizers are understood up to all \(7!\) vertex permutations. The cut parameter is \(d=2\); **not** the ordinary matching-cut parameter \(d=1\). No statement is made about extremal orders eight or higher, or about the general asymptotic edge-density conjecture.

A representative is encoded by the integer bitmask \(m\in\{0,\ldots,2^{21}-1\}\) with bit \(i(13-i)/2+(j-i-1)\) indicating edge \(\{i,j\}\), for \(0\le i<j\le6\). The accompanying `graph6` strings give a redundant customary graph encoding; the proof uses the integer masks only.

## Proof

We give a finite exhaustive **exact** proof with a complete, independently reproducible certificate `verify.cpp`. The following reasoning specifies why the finite search covers **all** cases.

1. **Enumerating the universe.** Every labelled seven-vertex simple graph is uniquely described by a 21-bit integer from \(0\) through \(2^{21}-1\). The verifier iterates all \(2^{21}=2{,}097{,}152\) such integers, selecting those with at most fourteen set bits. Hence no graph with at most fourteen edges is omitted; the test uses neither random sampling nor a graphical atlas.

2. **Enumerating cuts.** Every unordered nonempty proper bipartition has a unique shore \(A\) not containing vertex \(6\). Such shores are precisely the \(2^6-1=63\) nonempty subsets of \(\{0,\ldots,5\}\). For each, `has_two_cut` computes the number of neighbors on the opposite shore for **every** one of the seven vertices, and returns true if and only if all seven counts are at most two. Thus negating this predicate is precisely 2-immunity. This establishes correctness of the decision procedure directly from the definition.

3. **The finite lower bound and witness census.** Complete execution gives zero 2-immune graphs for each edge count from zero through thirteen, and exactly \(15{,}015\) such graphs for fourteen edges. The latter number is positive, so the former establishes \(\mu_2(7)=14\), and the entire set of labelled extremizers is certified.

4. **Isomorphism classes.** Each of the ten explicit masks in `representatives.tsv` has fourteen bits and is 2-immune, as rechecked from its edges. The verifier permutes every representative through all \(7!\) permutations, collects each orbit as a set of 21-bit masks, checks that every member belongs to the independently enumerated complete extremal set, and checks that the ten orbits are pairwise disjoint. Their sizes are respectively the ten numbers displayed above and their union has \(15{,}015\) elements, equal to the complete enumerated set. Therefore these ten distinct classes account for **all** fourteen-edge 2-immune seven-vertex graphs. The counts of automorphisms, \(7!\) divided by these orbit sizes, are also provided in the table.

All assertions are exact finite mathematical consequences of the specified loops and integer operations, with assertions in the certificate checking each conclusion. This is a proof by completely specified exhaustive enumeration, not inference from partial enumeration. No trusted graph database or external solver is used by the certificate.

## Verification

From a C++17 compiler:

```sh
c++ -std=c++17 -O2 -Wall -Wextra verify.cpp -o verify
./verify
```

Expected successful checks:

```text
EXHAUSTIVE_LABELLED_7_VERTEX_2_CUT_CHECK_PASS
NO_IMMUNE_GRAPHS_AT_0_THROUGH_13_EDGES_PASS
MINIMUM_14_EDGE_IMMUNE_COUNT_15015_PASS
TEN_DISJOINT_ISOMORPHISM_ORBITS_PASS
ORBIT_SIZES 105 2520 2520 1260 2520 1260 630 2520 1260 420
VERIFY_OK
```

The predicate, edge-index formula, entire 21-bit loop range, and complete 63-cut loop are visible in source. A second local check against a 7-vertex graph atlas independently recovered ten unlabeled fourteen-edge 2-immune graphs and the same orbit total; this optional corroboration is not a logical dependency of the standalone certificate.

## Relationship to prior work

Neopryatnaya, Verdenko and Voronov (public preprint dated 2026-11-19) prove that every graph with at most \(2n-2\) edges has a 2-cut, identify the sharp orders five, six and eight, and report computational values \(\mu_2(n)=2n\) for orders nine through fourteen. Their article does **not** state the seven-vertex threshold, the ten extremal isomorphism types, or the labelled census. Its general theorem gives only the weaker lower bound of thirteen edges at order seven. The present result supplies the missing order-seven optimum and complete extremal classification; it does **not** imply the authors' open all-order conjecture.

Gomes and Sau (2019) define the general degree-bounded cut decision problem and establish complexity and algorithmic results, rather than the fixed seven-vertex extremal classification. Bonsma, Farley and Proskurowski study the different, degree-one matching-cut immunity threshold. A targeted published-results comparison of seven-vertex 2-cut immunity and extremal counts and searches of the accessible primary literature found no result covering the displayed full statement. Since unindexed older databases or alternative terminology are possible, historical priority is provisional pending independent literature review.

## Limitations

This is an exact finite-order classification, not an infinite-family theorem or an improvement in the conjectured limiting density. The main computational certificate must be compiled and run to repeat the complete enumeration; the provided source allows an independent reader to inspect the loops without relying on execution logs. The proof is exhaustive at seven vertices and makes no inference from that finite boundary to higher orders. The present review is not an independent mathematical audit.

## References

1. A. Neopryatnaya, V. Verdenko, V. Voronov, *Edge cuts of bounded degree in sparse graphs*, arXiv:2611.26556, first submitted 2026-11-19. https://arxiv.org/html/2611.26556v1
2. G. C. M. Gomes, I. Sau, *Finding Cuts of Bounded Degree: Complexity, FPT and Exact Algorithms, and Kernelization*, IPEC 2019, article 19, https://doi.org/10.4230/LIPIcs.IPEC.2019.19 ; open text https://drops.dagstuhl.de/storage/00lipics/lipics-vol148-ipec2019/LIPIcs.IPEC.2019.19/LIPIcs.IPEC.2019.19.pdf
3. P. Bonsma, A. M. Farley, A. Proskurowski, *Extremal graphs having no matching cuts*, Journal of Graph Theory 69 (2012), 206–222, https://doi.org/10.1002/jgt.20576
