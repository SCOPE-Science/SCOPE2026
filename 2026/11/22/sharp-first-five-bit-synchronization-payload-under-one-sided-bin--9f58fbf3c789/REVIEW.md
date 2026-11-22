# Scientific review of one-sided-run-limited synchronization codes

## Correctness — PASS

The mathematical equivalence between admissible codes and cliques of the eligible-word compatibility graph is immediate from the quantified two-direction definition. The all-vertex generator checks the forbidden factor and self-borders, and an independent bit-mask implementation tests all pair overlaps. The greedy-color branch-and-bound is exhaustive: each discarded subtree has an upper bound no larger than an already verified clique. `verify.py` replay produced `VERIFY_OK`, including 410 length-16 vertices, 308053 search nodes, one length-16 42-word witness, the sharp length-15 upper bound 30, and all smaller cases. `certificates.json` contains all witness codebooks. The test is a finite proof; nothing is inferred for larger lengths.

## Originality — PASS, with priority qualification

Closest literature: Chee et al. (2012) and Blackburn (2013) study unrestricted cross-bifix-free code sizes and marker families; Stanovnik, Moškon and Mraz (2024) compute unrestricted optimal values and (2025) give run-limited constructions and characterizations. The 2025 study explicitly notes that differing restrictions for letters can be accommodated, but does not list the asymmetric `11`-avoiding exact maxima and the five-bit boundary. General algorithms alone do not provide the evaluated numerical capacities without the special finite search. Named-source and indexed-record searches found no implication yielding \(M_{15}=30\), \(M_{16}=42\). The general 2025 characterization and unindexed historical computations remain priority risks, not disproof of the distinct stated calculation.

## Mathematical value — PASS

The exact minimum 16-bit synchronized block for a five-bit payload is an operationally meaningful cutoff in a natural finite-type constrained source. The difference between the exact 42-word optimum and 24 words in a standard marker family is substantial: it yields an additional complete payload bit at the same length under the same internal constraint. All capacities through the threshold and explicit witnesses are supplied, not merely a code example or a loose bound. No larger-length rate claim is made.

## Scope and residual risks

The rule forbidding `11` is internal to each codeword and does not protect transitions between successive frames. There is no substitution/deletion robustness. Exact capacity at length 17 or beyond and historical uniqueness are unproved. This work has not received independent mathematical audit.

Self-review: passed. Independent audit: not yet performed.
