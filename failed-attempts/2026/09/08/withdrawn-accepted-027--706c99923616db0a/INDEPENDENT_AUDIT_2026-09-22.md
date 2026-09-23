# Independent three-axis audit — 2026-09-22 campaign

## Record and source identity

- Source path: `2026/09/08/027`
- Audited repository: `SCOPE-Science/SCOPE2026`
- Audited source tree: `84c4a3666703dc10ba2ccc07f955040d4548beb9`
- `RESULT.md` blob: `db43392468120d679cc54ac3c7f649184e088f3f`
- `VERIFICATION.md` blob: `83b03a7f246da30fad50fa39962dbb6d7f0519f0`
- Review date (UTC): 2026-09-23
- Review type: separate AI independent audit; not human/expert attestation and not Lean/formal verification.

## Claim audited

For a uniformly random skew-symmetric binary sequence of odd length `n=2m-1`, the record claims:

1. all odd-lag aperiodic autocorrelations vanish;
2. for even lag `k`, `E[C_k^2] = 2(n-k)-1`;
3. mean energy `E[E]=(m-1)(2m-3)` and mean demerit factor `(m-1)(2m-3)/(2m-1)^2`;
4. this mean is lower than the unrestricted mean by `2(m-1)/n^2`;
5. a finite variance table for `n=3,...,21`.

The record states that no prior source gives the skew-conditional mean/variance.

## Correctness — PASS

I independently reconstructed the skew ensemble using free Rademacher variables. For each `m=2,...,11` I exhaustively enumerated all `2^m` free sign choices, constructed the full length-`2m-1` skew sequence, computed every aperiodic autocorrelation, and accumulated exact integer/rational moments.

The exhaustive checks reproduced:
- odd-lag autocorrelations identically zero;
- for every tested even lag `k`, the exact second moment `E[C_k^2]=2(n-k)-1`;
- mean energies `1,6,15,28,45,66,91,120,153,190` for `n=3,5,...,21`;
- energy variances `0,16,144,480,1248,2544,4464,7232,10816,15696`, exactly matching the record.

The mean formula also follows algebraically by summing the even-lag second moments. No correctness defect was found in the stated formulas or finite table.

## Originality — FAIL

The central novelty claim is directly contradicted by prior literature.

Jonathan Jedwab, *The mean and variance of the reciprocal merit factor of four classes of binary sequences*, arXiv:1911.11246 (first submitted 25 Nov 2019; revised 2024), gives exact mean and variance formulas for uniformly random skew-symmetric binary sequences. Full text:
https://arxiv.org/html/1911.11246v2

The paper defines the same aperiodic autocorrelation and standard merit factor `F(A)=n^2/(2 sum_{u=1}^{n-1} C_A(u)^2)`. Its skew-symmetric class `SS_n` is the same class up to indexing convention. Theorem 2 states, for odd `n`, `n^2 E[1/F(A)] = n^2 - 3n + 2` and gives a closed exact formula for `n^4 Var(1/F(A))`.

The record's demerit factor is `D = (sum C_k^2)/n^2 = 1/(2F)`. Therefore Jedwab's mean formula gives `E[D]=(n^2-3n+2)/(2n^2)=(m-1)(2m-3)/(2m-1)^2`, exactly the record's claimed mean. This is not merely asymptotic or adjacent coverage; it is the same quantity for the same probability ensemble.

The variance coverage is even stronger. Since `1/F=2D=2E/n^2`, `Var(E) = (n^4/4) Var(1/F)`. Substituting Jedwab's Theorem 2 formula yields, for `n=3,5,...,21`, exactly `0,16,144,480,1248,2544,4464,7232,10816,15696`, which is the record's entire variance table. The prior work gives a closed formula for all odd `n`, while the record explicitly claims only a finite table.

Jedwab's introduction also says that the expected reciprocal merit factor for the skew-symmetric class had already been calculated in earlier work, while the 2019 preprint supplied the exact skew variance formula. Thus the record's statement that no prior source gives the skew-conditional mean/variance is false.

The odd-lag vanishing property is classical and appears throughout the skew-symmetric LABS literature; it is part of the standard reason the skew class is used. The per-even-lag second-moment identity is a concise decomposition of the known mean, but it does not rescue the record's claimed novelty of the mean/variance result, and no evidence was found that this decomposition by itself constitutes a distinct substantial theorem beyond the prior exact distributional calculation.

Searches used included “skew-symmetric binary sequences mean variance reciprocal merit factor”, “skew symmetric sequences autocorrelation odd lag zero”, and direct follow-up of the record's merit-factor terminology. The decisive source was openly available in full on arXiv, so no institutional-download fallback was required.

## Scientific value — FAIL

After subtracting prior-art coverage, the record retains an elementary proof of a per-lag second-moment identity and a finite verification table. The headline mean is exactly known, and the finite variance table is strictly weaker than Jedwab's all-length exact variance formula.

The short per-lag derivation may be pedagogically useful, but it does not establish a new asymptotic regime, improve the known exact variance result, produce new higher moments, classify extremal skew sequences, or yield an algorithmic improvement. Under the campaign's stated standard, the surviving material is not enough to support a validated scientific finding.

## Bounded repair considered

A bounded repair can:
- cite Jedwab's 2019/2024 exact skew mean and variance theorem;
- remove the false novelty claim;
- present the even-lag second-moment derivation as an alternative elementary proof/decomposition of the already-known mean.

That repair would be accurate, but it would not create a sufficiently original and substantial result. A legitimate retry would need a genuinely new distributional theorem (for example new higher skew moments, a nontrivial conditional law, or a structural/extremal consequence not covered by existing exact formulas) and a literature comparison that explicitly includes Jedwab.

## Final disposition

- Correctness: **PASS**
- Originality: **FAIL**
- Scientific value: **FAIL**
- Disposition: **failed / withdraw from validated findings**

The computations are preserved as reproducible evidence, but the record does not pass the independent three-axis gate because its central mean/variance contribution was already known in stronger form.
