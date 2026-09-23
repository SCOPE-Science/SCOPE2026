# Independent three-axis audit — 2026-09-23

Source: `2026/09/08/032`; audited source-tree SHA `8893e4cf8b4c62ac94a313448fdb80dd37f33f65`; `RESULT.md` blob `d10a505fb81f4b4bd388512207c66d7c72e4f11d`.

## Claim checked
The record defines the simultaneous Knödel-membership set `K(n)` for composites, derives `m(n)=floor((n-1)/lambda(n))`, and reports an exhaustive census through five million including a 13,509-value multiplicity histogram, the unique maximizer `n=4,935,060` with `m=137,084`, least members of `C_1,...,C_10`, and `C_1/C_3` slice counts.

## Correctness — passed
The reduction to Carmichael's exponent is valid: all units satisfy `a^(n-k)=1 mod n` exactly when `lambda(n)|(n-k)`, so admissible `k` are `n-j lambda(n)` and `m(n)=floor((n-1)/lambda(n))`. I independently wrote and compiled a fresh C sieve/factorization program, not using the record's artifacts, and exhaustively checked every composite `n<=5,000,000`. It reproduced all headline data exactly: `4,651,486` composites, `13,509` distinct multiplicities, unique maximizer `4,935,060` with `m=137,084`, `C_1` count 74, `C_3` count 126,029, 131,805 composites with `m>=1000`, 407 with `m=1`, and least `C_1,...,C_10` members `561,4,9,6,25,8,15,12,21,12`.

## Originality — passed only in the narrow evidence-relative sense
MathWorld/Makowski/Ribenboim and OEIS sources establish the Knödel classes and tabulate individual `C_k` sequences; searches for the joint multiplicity histogram and the specific maximizer did not locate a prior publication. The headline reduction itself is immediate from the definition and the Carmichael function, so it is not an original structural theorem. The finite joint census may be new as a dataset, but this is not a guarantee of priority.

## Scientific value — failed
After the one-line reduction, the reported quantity is simply the quotient `floor((n-1)/lambda(n))`. The rest is an arbitrary-cutoff brute-force histogram and extremal scan to five million. It gives no asymptotic theorem, structural characterization of maximizers, nontrivial algorithmic advance, or connection extracting new behavior of the Carmichael function. The least-`C_k` and slice heads are already standard sequence data. Under the audit standard, a modest finite census of a tautologically reduced statistic is insufficient as a validated scientific finding.

## Repair attempt
A bounded wording repair cannot supply the missing scientific content without changing the work's identity. A legitimate retry should add a nontrivial structural or asymptotic result about `n/lambda(n)`, a theorem explaining extremizers, or a substantially justified reusable dataset/algorithmic advance beyond the five-million cutoff.

Searches included Knödel/Carmichael-function equivalents, Makowski classes, the exact maximizer and multiplicity, and OEIS/MathWorld sequence references. No inaccessible source was decisive. This is an independent AI audit, not human/expert or Lean verification.
