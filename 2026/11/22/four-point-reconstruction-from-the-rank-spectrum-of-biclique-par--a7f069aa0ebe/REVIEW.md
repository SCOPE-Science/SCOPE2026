# Self-review

## Correctness — PASS
The claim is a reconstruction statement about three **cardinalities** of rank strata of the inverse monoid of partial induced-graph automorphisms of \(K_{a,b}\), for \(a,b\ge2\). The induced-subgraph stratification into independent sets and complete bicliques is exhaustive and disjoint. Its automorphism orders are respectively \(k!\), \(i!j!\) for unequal positive part sizes, and \(2(i!)^2\) for equal positive sizes. These give the exact full rank polynomial, not only an estimate.

Writing \(n=a+b\), \(m=ab\), \(K=\binom n2\), the rank-two count is \(K^2+4(m-K/2)^2\). The third coefficient is a polynomial in these data, so it leaves the only possible reflection \(m\leftrightarrow K-m\) unresolved. The computed rank-four difference is \(\frac23(n-2)(m-K/2)(8(m-K/2)^2-n(n-1))\). If both reflected products come from bipartitions of the same \(n\), their physical upper bounds imply \(|m-K/2|\le n/4\). Thus the second factor is strictly negative for \(n\ge4\), and the difference vanishes only when the products coincide. The unordered part sizes then follow as roots of a quadratic. The explicit infinite family has complementary products and satisfies the domain bounds for every \(h\ge2\), establishing sharpness.

The bundled standalone standard-library verifier directly enumerates partial induced-automorphisms on five small bicliques, independently checks the rank formula, and tests the sharpness and reconstruction predicates over finite parameter ranges. The symbolic factorization and inequality, not those tests, establish the infinite result. Nonstandard arithmetic steps were independently checked by symbolic expansion. The bundled executable additionally certifies the rank-three and rank-four polynomial identities with exact rational evaluations on grids exceeding their proven coordinate-degree bounds (respectively \(6,2\) and \(8,4\)).

## Originality — PASS with acknowledged residual risk
The motivating full 18-page arXiv preprint by Jajcay, Jajcayová, Szakács and Szendrei (arXiv:1809.04422; publicly posted 2018-09-12) studies precisely this inverse monoid and establishes reconstruction from actual partial maps of ranks at most two, not from the numbers of maps by rank. Proposition 4.3 and Theorem 5.1 were compared at the implication level; their hypotheses supply more information and do not yield the proposed low-coefficient threshold. Other sections treat algebraic structure and realization, not the proposed numerical rank-four discrimination.

A publicly indexed 2026 homogeneous-graph partial-automorphism census covers balanced homogeneous cases, but not the complete class of unbalanced bicliques, and does not assert the sharp low-rank inverse threshold in its indexed description. A 2026 multipartite square-zero partial-isometry census concerns a restricted submonoid and hence does not imply unrestricted counts. The complete texts of those two published repository entries were not accessible through the attempted page retrieval. Accordingly the coverage risk is real, and these entries were not represented as fully inspected or conclusively excluded. Searches of exact formulas, aliases, biclique class, inverse monoids, and indexed results found no decisive stronger claim. Failure to find overlap is not proof of unique priority.

## Mathematical value — PASS
This addresses a natural inverse problem for the rank-size invariant of finite inverse monoids of partial graph automorphisms. The rank-one and rank-two strata are very small, easily measured features; their rank-three redundancy and the exact rank-four threshold are structurally informative rather than a small numerical improvement. An explicit infinite collision family rules out every truncation at rank three, while the one higher coefficient distinguishes all bicliques in the stated family. The theorem also supplies a complete rank enumerator for arbitrary unequal part sizes. It does not claim the same threshold for all graphs or arbitrary multipartite graphs.

## Closest literature and limitations
- Jajcay et al., *Inverse monoids of partial graph automorphisms*, arXiv:1809.04422, https://arxiv.org/abs/1809.04422 (full primary preprint, relevant statements checked).
- *Rank spectra and Gaussian deficiency laws for finite homogeneous graph partial automorphisms*, published 2026-11-02 repository record (indexed abstract checked, full repository content inaccessible).
- *The complete square-zero rank distribution of multipartite partial-isometry monoids*, published 2026-10-26 repository record (indexed abstract checked, full repository content inaccessible).

The theorem is a mathematical proof supplemented by finite checks, not an independent certificate. General graph reconstruction, general multipartite reconstruction and exclusion of unindexed prior results are outside scope.

Self-review: passed. Independent audit: not yet performed.
