# Self-review

## Correctness — PASS

The claim is precisely a one-deletion packing statement for length-five oriented DNA strings with nearest-integer 50% GC count and Watson–Crick strand-pair closure. The full input consists of 640 eligible words and 320 strand pairs. Direct regeneration yields 260 internally admissible pairs and 4948 inter-pair conflicts. The four branches of the upper-bound certificate are exhaustive; every quoted rational clique cover is checked for nonnegativity, true graph-clique support, vertex coverage at least one and a total bound strictly below 23. The 22-pair witness passes disjoint deletion-output checks across all 44 individual words. Finite exhaustive proof is suitable here because the claim concerns only length five. Risks are implementation errors, mitigated by the transparent definitions, small source code, and exact arithmetic.

## Originality — PASS, with residual priority uncertainty

The 2014 D'yachkov lecture provides the strand-paired deletion-similarity setup, specific length-four codes, and asymptotic lower bounds; its examples and results do not imply a sharp length-five GC count two-or-three capacity of 44. The 2015 Bennenni–Guenda–Gulliver paper develops bounded/fixed GC and edit-distance bounds but supplies no matching one-deletion finite classification. The 2009 Sun thesis advertises short-length bounds for edit codes with GC and reverse-complement constraints, yet its table and original pages were not accessible for inspection. This is the closest material unresolved risk; it could contain nearby or stronger covering information and merits independent priority review. Searches and full-text sections examined are listed in `AUDIT.json`. Search nonappearance is not treated as a novelty proof.

## Value — PASS

The exact maximum 44 is a natural finite packing invariant obtained by combining three established DNA coding constraints: nearest-half composition at an odd blocklength, mandatory use of both DNA strands, and a one-symbol synchronization error. An explicit code and a sharp upper certificate fill a design-capacity gap left by general asymptotic or different-distance bounds. The precise number matters because it is an optimal design limit for this fully specified small alphabet/length case, rather than an arbitrary enumeration of selected words.

## Prior-work and scope limits

No general formula for longer words, biochemical behavior, or edit errors with substitutions is asserted. Comparisons with classical Hamming, unconstrained deletion, or fixed-GC edit code sizes do not automatically transfer to this exact channel. The related Sun thesis requires external historical check.

Self-review: passed. Independent audit: not yet performed.
