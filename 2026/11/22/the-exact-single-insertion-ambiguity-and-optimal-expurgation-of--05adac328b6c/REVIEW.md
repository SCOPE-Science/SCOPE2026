# Scientific review

## Correctness — PASS

The assertion covers all integers \(q\ge2\) and \(m\ge1\), including one-symbol roots and periodic roots. The two halves surrounding the central letter bound the inverse list by two. When the two halves differ, the first-mismatch alignment forces the deleted words to be a pair of adjacent cyclic rotations; both insertion positions exist, and a constant root is the sole coincidence. Counting distinct one-symbol insertions into each parent gives the exact inverse-list histogram. The confusability graph is then a disjoint union of rotation-orbit cycles, edges and isolated vertices; independent-set sizes and multiplicities give the sharp optimal-subcode formulas. The actual standalone checker passed exhaustive direct enumeration over the stated finite parameter ranges. The infinite proof is not based on the finite checks.

## Originality — PASS, qualified

The closest primary work inspected is Sala–Gabrys–Schoeny–Dolecek (arXiv:1604.03000, originally April 11, 2016), particularly its introduction, main general common-supersequence theorem and corollaries. Its worst-case bounds over unconstrained sequences do not imply a complete inverse-list distribution for the family \(\{UU\}\) or its induced rotation-orbit code capacity. Cheng–Guruswami–Haeupler–Li (arXiv:2007.09075) discuss coordinatewise repetition, not doubling a whole block. Targeted published-record searches found adjacent work on square subsequences, palindromic codewords, and duplication channels, but not this theorem. Full text of every possible unindexed antecedent has not been inspected; priority remains conditional rather than certified.

## Mathematical value — PASS

The whole-block duplication encoder has rate one-half yet fails one-insertion correction in a highly constrained way. The exact ambiguous-output spectrum distinguishes ordinary insertion histories from genuinely different candidate messages. More importantly, the full confusability graph yields a natural optimal expurgation problem with an exact all-length answer and a complete count of optimal subcodes. The asymptotic half-survival rate identifies the price of repairing this simple synchronization encoder. No optimality is claimed relative to unrestricted codes.

## Scientific limitations

Only a single arbitrary insertion is treated; alphabet labels and orientation are retained. Maximum-subcode claims apply inside the doubled-block family. The finite checker is corroboration, not an infinite proof. An earlier unindexed equivalent remains a material originality risk.

Self-review: passed. Independent audit: not yet performed.
