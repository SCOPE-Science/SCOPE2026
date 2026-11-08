# Self-review

## Correctness — PASS

The proof in `RESULT.md` constructs the complete dyadic factor language from aligned blocks, identifies one primitive odd-weight cyclic orbit and one doubled odd-weight cyclic orbit, derives the precise rotation-moment identity, and uses the binary scattered-`01` count to recover that moment. The argument covers all integers \(k\ge1\), with level one handled explicitly. The independent-in-code finite diagnostic `python3 verify.py` returns `VERIFY_OK levels=0..11 windows_checked=24570 pair_checks=47 five_factor_collision=confirmed`; the infinite claim rests on the written proof, not these tests.

## Originality — PASS (with residual bibliographic risk)

The nearest source family is binomial complexity of Thue--Morse and generalized Thue--Morse (arXiv:1812.07330 and arXiv:2112.05347), as well as global reconstruction for Tribonacci (Lejeune--Rigo--Rosenfeld, 2019). The same-word 2014 study arXiv:1405.3532 treats two-abelian *contiguous* factor counts, not scattered subsequence counts. The general arXiv:2201.04603 and arXiv:2509.11172 theorems were compared by hypotheses and implication, including the explicit length-five obstruction to global reconstruction. Primary-text inspections and searches did not identify a covering dyadic statement. An unindexed equivalent is possible; this is not an independent bibliographic certification.

## Mathematical value — PASS

The theorem completely identifies binomial reconstruction order at every dyadic scale, proving an all-scale exact factor count and a sharp gap between Abelian and two-binomial information. The first-moment criterion and the two cyclic orbits explain why these scales have this rigidity. This is a substantive natural invariant of a canonical automatic word, not a finite-sample extrapolation.

## Limits and nearest literature

The claim does not determine the full non-dyadic complexity. At length five, `10001` and `01010` are distinct two-binomially equivalent factors. The source comparisons and diagnostic computations are not proof of absolute novelty. Exact sources and theorem comparisons are recorded in `AUDIT.json` and `RESULT.md`.

Self-review: passed. Independent audit: not yet performed.
