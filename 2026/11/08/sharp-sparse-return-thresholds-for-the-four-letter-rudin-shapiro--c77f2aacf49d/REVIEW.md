# Scientific review: sharp sparse-return thresholds for the four-letter Rudin–Shapiro word

## Correctness — PASS

The four literal symbols, one-sided fixed point, positive shifts, and two separate optimization problems are explicitly defined. Every odd shift is impossible because the substitution sends even and odd positions to disjoint alphabets. The binary coding satisfies the standard adjacent-`11` Rudin–Shapiro recurrence; consequently Theorem 28 of Meleshko–Ochem–Shallit–Shan supplies the independent lower bound of four necessary shifts. The language-saturation lemma reduces all infinite positions and all shifts through 66 to exactly 528 length-67 factors. The standalone package code verifies the fixed-point factor stability, exhaustively tests 40,920 four-shift sets and all 1,024 subsets at horizon 10, and checks the explicit two optimum sets. Short witnesses force each of the five shifts at the smallest horizon. The direct-prefix tests and binary-projection tests provide separate consistency checks. No finite sample is mistaken for an infinite proof.

## Originality — PASS, with bibliographic risk

The nearest primary paper, *Pseudoperiodic Words and a Question of Shevelev* (arXiv:2207.10171, published in 2023), Definition 1 and Section 4.4/Theorem 28, concerns the binary-coded Rudin–Shapiro sequence. Its non-three-shift theorem is used rather than claimed as new. That binary theorem neither supplies a literal four-letter four-shift witness nor determines the 10/66 delay tradeoff or the exact two optimal four-shift sets. The four-letter substitution has been studied for factor and other complexity properties, but counts of factors or reversal pairs do not determine pseudoperiod hitting sets. Searches by word, shift parameters, coding aliases and problem terminology did not find the present explicit classification. This is best-knowledge originality only, not a demonstration that all relevant literature has been indexed; an earlier unpublished or differently formulated covering classification remains possible.

## Mathematical value — PASS

The published pseudoperiod framework motivates determining both a minimum set of return probes and the smallest return horizon. The four-state cover of a classical automatic word is canonical; its literal shift-equality invariant is not preserved by the usual two-state coding. The sharp transition from five necessary probes at horizon 10 to four probes only at horizon 66, and the exhaustive two-solution classification at that threshold, give a nontrivial structural sparse-return result. The result is for all starting positions of the infinite sequence and proves actual optimality, not a tentative computational record.

## Scientific limitations

The theorem classifies all four-shift sets only through the minimum four-shift horizon, not at larger horizons. The large binary non-three-shift computation is credited to the published source and is not reproduced. The finite exhaustive certificate is only as reliable as the specified substitution-language saturation reasoning and the supplied short verifier; all operations use exact integer arithmetic. No guarantee against an unindexed equivalent formulation is asserted.

Self-review: passed. Independent audit: not yet performed.
