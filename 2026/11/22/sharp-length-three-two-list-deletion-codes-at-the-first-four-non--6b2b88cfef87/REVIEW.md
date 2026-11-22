# Scientific review

## Correctness (C): PASS

The claimed domain is exact one-deletion decoding from length-three words over a labeled alphabet. Deletion histories that yield the same word are identified, and decoding lists consist of distinct codewords. The universal bound follows from a complete classification of shadow cardinalities one, two and three, the diagonal incidence restriction, and exact double counting. The four explicit constructions are tested against **all** possible received words by a standalone deterministic Python checker. The checker also tests the cyclic action, the conflict triangles, and the precise receiver-list histograms. No solver optimality assertion is used in the proof. Boundary values \(q=4,5,6,8\) are fully covered; no conclusion is made for unlisted alphabet sizes.

## Originality (O): PASS against the inspected literature, with residual risk

The precise claim is four exact **list-two** capacities, cyclic perfect two-list saturation at six symbols, and two nondecomposable optimal code examples. Chee–Ge–Ling (2010), arXiv:1008.1343, Section 6, treats perfect **list-one** deletion codes, and its single-coverage size spectrum does not establish these distinct double-coverage claims. Kiah–Wei–Zeng (2026), arXiv:2609.21395, treats fixed-list asymptotic bounds, and its Theorem 28 at length three and list size two is weaker. Song–Cai–Nguyen (2022), arXiv:2201.02013, treats binary codes under the stronger combined deletion–substitution channel. Dawson–Seberry–Skillicorn (1984) studies directed packings with different block and incidence conditions. Direct equivalent-formulation, broader-result, exact small-table, and implication comparisons are detailed in `AUDIT.json`. Previously recorded Steiner-class examples settle other alphabet congruences only. The residual possibility of a hidden two-fold directed-packing result or an unindexed finite table is real, not resolved by a failed search.

## Mathematical value (V): PASS

The four chosen sizes are not arbitrary consecutive parameter increments: they are the *first* alphabet sizes in each of the four residue classes modulo six omitted by classical Steiner triple-system existence conditions (after excluding the trivial two-symbol boundary). The theorem resolves the exact finite-block channel ambiguity capacity in each first case, rather than offering a mere lower bound. The six-symbol case is a cyclic two-fold perfect covering, while five- and eight-symbol **optimal** codes exhibit a conflict-triangle obstruction to decomposition into two unique-decodable codes. These structural differences make the small benchmarks relevant to future design constructions in non-Steiner alphabet classes. The work does not claim a uniform formula for all alphabet sizes, a classification of all optimal codebooks, or downstream asymptotic improvements.

## Limitations and external verification

The checked assertions are finite and exact; the universal upper bound is symbolic. External literature access and indexing cannot rule out unindexed equivalent statements. The code and proof have been reviewed in the same scientific-review channel; no independent audit or independent validation has been performed.

Self-review: passed. Independent audit: not yet performed.
