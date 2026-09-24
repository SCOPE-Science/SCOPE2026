# Independent three-axis audit — 2026-09-24

Reviewer type: separate AI audit. This document records reproducible scientific checks and literature comparison, not a transcript of private reasoning.

## Audited source

- Record: `SCOPE-20260908-059`
- Source path: `2026/09/08/059`
- Audited `RESULT.md` blob: `4efe0671e685f5efdf1e724774236f38552a61ab`
- Claim: exact maximum ordered rainbow Schur-triple counts for all 3-colorings of `[n]`, `1<=n<=12`, including optimum counts/classes and the parity/interval template comparison.

## Correctness — PASS

A fresh exhaustive enumeration with the color of 1 fixed by symmetry reproduced `R(1..12)=0,0,2,4,6,8,12,14,18,22,28,30`, labelled optimum multiplicities `3,9,6,6,12,12,6,24,30,6,6,66`, and `S_3`-orbit counts `1,2,1,1,2,2,1,4,5,1,1,11`. The stated parity/interval template gives `0,0,2,4,6,8,10,14,18,22,26,30`, confirming the finite exceptions.

## Originality — PASS, with corrected historical context

No checked source publishes this exact small-`n` table and class counts. Parczyk–Spiegel (EJC 33(1), 2026, DOI `10.37236/13554`) and Hegde–Kumar–Pratibha (arXiv `2609.18474`) address asymptotic bounds. A 2017 presentation by Thotsaporn Thanatipanonda already formulates the rainbow `x+y=z` maximization problem and gives the same parity/interval construction pattern, so historical attribution must acknowledge that antecedent.

## Scientific value — FAIL

After subtracting the prior formulation/construction, the surviving contribution is only a brute-force table for `n<=12`. It supplies no structural formula, reusable proof technique, algorithmic improvement, or new asymptotic regime. The finite exceptions are valid benchmark facts but are too narrow to meet the campaign's scientific-value standard.

## Repair attempt

Narrowing the claim to a benchmark dataset and correcting historical attribution improves accuracy but does not cure the value failure.

## Final disposition

**FAILED** on scientific value; correctness passes and the exact finite table is original relative to the checked literature.
