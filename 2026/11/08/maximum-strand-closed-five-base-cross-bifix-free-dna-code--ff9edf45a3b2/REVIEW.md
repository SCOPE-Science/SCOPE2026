# Scientific review: five-base strand-closed non-overlapping codes

## Correctness — PASS

All hypotheses, quantifiers, and boundary conventions are explicit. The first/last-letter reduction holds because reverse-complement closure sends the first-letter set to the complement of the last-letter set and length-one nonoverlap forces disjointness. Complement-preserving alphabet permutations reduce all possible codebooks to the 256-word canonical domain. Every odd-length reverse-complement orbit is a two-element orbit. The 56 admissible orbits and all 412 pairwise conflicts follow from four fixed proper overlap lengths. The 18 listed cliques partition these vertices, so they bound all independent sets by 18 orbits; the 18-orbit witness meets that bound. Two distinct standard-library verification implementations independently reconstruct every finite claim, including all pair comparisons; they pass when run from the package directory.

## Originality — PASS, with residual risk

Relevant 2012 and 2013 foundational full-text results treat unconditioned q-ary cross-bifix-free codes and construction bounds; the 2024 open-access maximal-code paper provides unrestricted length-five exact results (quaternary maximum 81), not reverse-complement-closed optimization. A separate prior record reports a strand-closed four-mer value 17 for length four, and a different restricted five-mer record reports a GC-balanced value 24. Neither implies the present unrestricted-in-GC exact maximum 36; those earlier scientific statuses are not reassessed. Relevant published record searches using the phrases “strand-closed five-mer non-overlapping DNA codes exact optimum 36”, “reverse-complement closed five-letter DNA non-overlapping code maximal 36”, and “Watson-Crick self reverse complement cross bifix free code maximum” did not identify an identical 36-word constrained theorem. This is evidence of a distinct claim, not a proof that no unindexed publication exists. Historical priority remains subject to outside verification, particularly against work on self-complementary synchronization codes.

## Value — PASS

The exact optimum gives the maximum number of orientation-invariant five-base framing tokens under the stringent nonoverlap condition. It is a sharply resolved small-alphabet, finite-blocklength invariant, with a short checkable optimality certificate and a natural unconstrained benchmark of 81; its reduction to 36 quantifies the cost of strand closure. Unlike the prior four-mer problem, odd blocklength eliminates all fixed reverse-complement orbits and produces a 56-vertex, 412-conflict structural instance. It does not make claims about practical biochemical performance or higher lengths.

## Limitations

An exhaustive finite graph proof at length five is not an all-length theorem. The absence of indexed prior equality claims does not establish global historical priority. No independent scientific audit was performed.

Self-review: passed. Independent audit: not yet performed.
