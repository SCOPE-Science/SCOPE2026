# Scientific review

## Correctness — PASS

Every positive trace must be a matching. The proof establishes a residual perfect-matching lemma: with at least four unassigned vertices, deleting the restrictions of the prescribed buddy-pair matching and at most \(k-2\) arbitrary queried edges leaves minimum degree at least half the residual order and hence a perfect matching by Dirac's theorem. For the critical \(n-1\)-edge support it instead needs two deleted matchings; the four-vertex boundary follows from the three one-factors of \(K_4\), and all larger residual orders follow again from Dirac. This proves all Boolean traces and the sharp last-pair exception. The one-edge-deletion bijection gives precisely \(n p_n\) top faces, with all lower coefficients counted by inclusion-exclusion. The online upper bound is an induction after one positive edge has been fixed. All quantifiers, \(n=2\), and the empty trace are covered. Exhaustive independent finite checks verified 104,500 supports through \(n=5\), including the entire trace identity for arbitrary supports below the critical degree; finite checks are supporting evidence, not infinite proof.

## Originality — PASS, with historical-priority risk

The accessible 2022 primary paper by Johnston, Kayll and Palmer studies **the same nonbipartite graph** \(K_{2n}\setminus F\) and establishes counts of perfect matchings and asymptotics; these enumerative facts and their inclusion-exclusion formula are credited. It does not present the asserted complete coordinate-shattering criterion or facet correction. Bucić and collaborators (2019) prove intersection bounds for perfect matchings, not arbitrary Boolean edge-query traces. Lu and Yu (2018) study general prescribed-positive/negative matching extension, but their fixed-parameter large-order sufficient conditions do not cover the moving top-degree boundary uniformly or count its supports. The closest previously recorded trace polynomial is for the *bipartite* crown graph and stops at degree \(n-2\); the present nonbipartite polynomial has a nonzero degree-\((n-1)\) term. Another recorded result restricts to noncrossing perfect matchings and imposes a different geometric activity criterion. The exact implication comparisons, inspected material and residual concerns are recorded in `AUDIT.json`. No exhaustive historical novelty certification is asserted.

## Value — PASS

The classical deranged-pairing problem asks how many complete pairings avoid a prescribed pairing. The additional natural question of which *individual candidate pairings can be queried with all Boolean response patterns* is not answered by the total count. The result resolves that question on every support and for every number of original pairs, obtains the entire f-vector and a pure complex, identifies the only sharp boundary obstruction, and proves exact equality of static and adaptive learning dimensions. The comparison with derangement permutations demonstrates that the top-level behavior genuinely depends on nonbipartite pairing freedom. The full structural result, not the already-known inclusion-exclusion count alone, motivates its value.

## Prior literature and limitations

Relevant primary sources are Chase–Freitag (2018, arXiv:1801.06566), Lu–Yu (2018, arXiv:1807.11159), Bucić–Devlin–Hendon–Horne–Lund (2019, arXiv:1906.05908), and Johnston–Kayll–Palmer (2022, arXiv:2209.11319). Adjacent recorded results on bipartite derangement traces and noncrossing matching traces were read and compared. The theorem does not determine homotopy groups, teaching dimension, or arbitrary edge-deletion families. Complete bibliographic priority and independent scientific validation remain open.

Self-review: passed. Independent audit: not yet performed.
