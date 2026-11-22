# Scientific review: parity-refined derangement shattering

## Correctness — PASS

For every integer \(n\ge4\), the proof applies to even fixed-point-free permutations, with indexed, distinct, off-diagonal row–image queries. A partial permutation's directed graph decomposes uniquely into directed paths and cycles; the number of path components is \(n-k\) at support size \(k\). Every completion acts as a permutation of path components. Its parity is \((-1)^{n-c-t}\), where \(c\) counts established cycles and \(t\) counts new cycles, and a singleton path cannot be fixed. These assertions hold for every boundary case in the domain.

For at least four unassigned rows, the proof obtains both signs of permissible residual matchings. The four-row bound uses all three even double transpositions and all six odd four-cycles; the five-row case is exhaustively checked across all \(120\) second forbidden matchings; the at-least-six-row case uses a two-by-two switch and Hall's theorem, with residual minimum degree at least half its order. At three or two remaining path components, enumerating permitted endpoint-joining permutations proves respectively the singleton triple parity exception and the exact two-path criterion. Size \(n-1\) is obstructed already without a sign constraint. The top coefficient's factorial sum counts unordered path pairs once, and the exponential generating expression is the same filtered cycle/path enumeration.

A clean standalone executable checked direct actual shattering against all even derangements for \(52,160\) partial-permutation supports across orders four through seven, plus every small matching-parity boundary and coefficients through order fourteen. The code and output are included. Finite checks corroborate, rather than prove, universal quantifiers.

## Originality — PASS, with residual priority uncertainty

The published unrestricted-derangement trace theorem gives an upper bound but does not establish which supports remain shattered by the strictly smaller even-permutation subclass. Previously analyzed parity effects on **permutation comparison queries** have a different instance space and entail no current support criterion. A preceding all-order near-top theorem already established every rank up to \(n-3\), its parity exception and the dimension for \(n\ge5\); a separate earlier finite six-letter polynomial is also covered. Both are explicitly credited. **Only the previously unclassified size-\(n-2\) two-path criterion and its exact top coefficient are assessed as new.** The foundational model-theoretic framework of Chase and Freitag (2018) supplies the 03-series classification background, without any even-derangement incidence theorem. The primary articles by Bucić et al. (2019), Alexandersson and Kebede (2021), and Plantholt et al. (2022) address matching intersections, signed derangement counts, and forbidden-functional assignments, respectively, not the present exact Boolean trace problem.

A search is not a proof of historical novelty. Alternative terminology in signed permanents and partial-permutation completion may conceal earlier equivalents; no independent priority certification is asserted. Source-specific inspections, queries and implication comparisons are itemized in `AUDIT.json`.

## Value — PASS

Parity constraints are a standard natural refinement of the fixed-point-free permutation family, while edge-incidence shattering is a natural information-theoretic invariant of that family. The new result supplies a previously missing top-rank characterization for every order and its exact coefficient, thereby completing a polynomial whose lower-rank terms were already known. It isolates the nonuniform path-length and parity obstruction at this final rank; this is not a mere reformulation of the unconditional rook polynomial, the known near-top classification, or the previously settled finite six-letter case. It provides a structural bridge between signed derangement cycle enumeration and Boolean trace realizability, with a reproducible finite test of the boundary analysis.

## Scope and limitations

All results are static rather than online, for the full off-diagonal board and orders at least four. The detailed two-path criterion is not claimed for general forbidden bipartite boards or arbitrary permutation subgroups. External historical coverage is necessarily incomplete; independent audit remains outstanding.

Self-review: passed. Independent audit: not yet performed.
