# Independent three-axis audit — 2026-09-22

Review date (UTC): 2026-09-23. Reviewer: separate AI audit. Source directory tree: `dab40e4bf28d72c77653e9348452c834f343459a`, checked on current `main` before review. The central claim audited was the asserted binary-Eulerian extremal table through seven states together with a 25-reset-threshold eight-state witness described as the strongest known even-n binary Eulerian extremal.

## Correctness

The finite computations themselves are reproducible. I independently implemented power-set BFS and reproduced `E(1..7)=(0,1,2,5,10,14,22)`, the displayed eight-state witness reset threshold 25, and the 20,160 Eulerian completions of its fixed `a` spine with fiber maximum 25. Thus the computational statements are not the reason for rejection.

## Originality

The literature comparison is dispositive against the record's framing. Szykuła and Vorel, *An Extremal Series of Eulerian Synchronizing Automata* (DLT 2016; arXiv:1604.02879), Section 5, report an exhaustive search over binary Eulerian DFAs with `n <= 11`. They explicitly state that in the binary case the Martyugin bound `floor((n^2-5)/2)` is met uniquely for `n in {5,7,8,9,11}` and is not reachable for `n in {6,10}`. In particular, the published search already covers the claimed exact values at `n=5,7` and, more seriously, supplies an eight-state binary Eulerian automaton with reset threshold strictly larger than 25. This directly contradicts the record's statements that the binary Eulerian subcase had no published extremal table and that the 25-state witness is the strongest known even-`n=8` binary extremal.

## Scientific value

After removing the already-published small-state extremal information and the false eight-state novelty claim, the surviving new material is essentially the exact `n=6` value and a 20,160-element fiber maximum for one chosen spine. That is a valid finite computation but is too narrow to support the accepted record's claimed scientific contribution. The record cannot be repaired by wording alone without changing its central identity and value proposition.

## Disposition

**FAILED.** Correct finite computations do not cure the decisive originality error and overstated eight-state significance. The accepted package should be withdrawn while preserving the complete source package and this audit evidence.
