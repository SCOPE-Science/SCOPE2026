# Review: First fractional-packing gap and rebound for adjacent-swap codes on Fibonacci words

## Correctness — PASS

The channel includes no error and one adjacent transposition of unequal bits, with outputs not required to obey the forbidden-factor constraint. Exactly \(\sum_{k=0}^{\lceil n/2\rceil}\lvert\mathcal F_{n,k}\rvert\) sources are generated at each \(n\le10\). Weight preservation proves the decomposition. Explicit optimal codebooks attain each integer value, while the exhaustive include/exclude recursion on the independently generated confusability graph gives exact upper bounds and counts of all maximizers. Nonnegative rational feasible primal and dual vectors for every weight have matching totals, proving the stated fractional optima with weak duality. Reversal-fixed maximizers are exhaustively counted. The shipped checker reconstructed and verified all certificate entries; a separate integer-program reconstruction matched the weight-layer maxima. These are finite proofs for precisely the stated range, not claims about larger lengths.

## Originality — PASS, with priority qualification

Sloane's published unrestricted swap counts concern a strictly larger source language and cannot determine optima of the restricted induced family; an unrestricted optimum gives only an upper bound. Gómez Soto et al.'s exact two-token result is likewise unrestricted at weight two. Kovačević's run-limited shift paper focuses on asymptotic inequalities and uses prescribed terminal markers; the later Kovačević–Kiah–Goyal paper concerns the unrestricted input alphabet and asymptotic rates. Castro et al.'s Fibonacci cube packing uses Hamming edges, while Kulkarni–Kiyavash use deletion shadows, neither equivalent to this receiver relation. Relevant published exact restricted-deletion and one-sided-swap results were compared by statement, and no implication giving the full ten-length table and optimizer census was found. Risk: a hidden appendix or unindexed computation may already contain some finite entries. The claim of originality is qualified, not certified uniqueness.

## Mathematical value — PASS

The forbidden-factor source is the standard Fibonacci/run-limited language, and a single physical bit shift is a natural channel operation. The first gap between its exact zero-error coding capacity and the standard fractional shadow relaxation, followed immediately by a return to equality, is a nontrivial finite boundary rather than an arbitrary subcase. The complete equality census and reversal counts expose symmetry and rigidity at the transition. No general theorem or asymptotic promise is asserted.

## Limits and priority risks

The calculation covers lengths one through ten only. The receiver may violate the source constraint, and rounding the fractional bound down still happens to give the correct integer sizes at all reported lengths. The finite computations are self-contained but independently published validation and exhaustive historical-priority certification are not provided.

Self-review: passed. Independent audit: not yet performed.
