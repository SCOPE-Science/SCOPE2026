---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Re-audited /workspace/repairs/4/RESULT.md and SLOGAN.txt. The original mathematical boundary and coefficient formula are correct; the repair changes the contribution, not the underlying law or limits. The exact published PGF gives distinct numerator factors 1+bs and 1−rs and the double pole factor (1−qs)^(−2), so λ_k=(2q^k−r^k+(−1)^(k+1)b^k)/k as a formal coefficient. The positive zero atom gives n[s^k]G(s)^(1/n)→λ_k, so a negative coefficient rules out arbitrarily fine PGF roots. The b≤q case has strictly positive summable intensities even at equality; the b>q case has positive odd coefficients and eventually negative even coefficients. For fixed θ, ρ=r/q<1 and t=log(b/q)>0, even k is forbidden exactly when exp(kt)+ρ^k>2. Since each finite prefix is strictly positive at t=0, K→infinity. The first even k≥log(2)/t bounds K from above (ρ^k>0), and at K one has log(2−ρ^K)<Kt≤log 2+2t. This proves the exact limit and the finite-prefix consequence without a θ-uniform claim. Independent bounded replay: at θ=1 and b/q=1+1/n, compare the two rational powers (1+1/n)^k+(2/3)^k to 2 for even k starting at 2; n=10,100,1000 give first indices 8,70,694. Also, direct finite expansion of log(G/G(0)) from the convolved rational masses agreed with the formula through degree 11 at three θ values and b below, at, and above q. The supplied script was inspected, not executed.

## originality

PASS

Only the repaired first-negative-coefficient asymptotic is passed for originality. The original boundary and logarithmic intensities are independently covered by Proof §§1–2 of the matching-family thinning result. Its listing is dated the same day as the supplied record, so no intraday priority is inferred. The repair cites that coverage, keeps ordinary divisibility solely as background, and retains the separately motivated limit for the first detecting index. The inspected comparisons do not state or settle that limit as a criterion or table of values.

## value

PASS

The repaired claim gives a naturally defined detection index for a false compound-Poisson diagnosis, rather than just observing that some very high coefficient is negative. Above the boundary at fixed θ it shows quantitatively how long every finite sign test can misleadingly pass: the required order grows like log(2)/log(b/q), with exact leading constant and parity. This is an independently useful limitation of truncation diagnostics in a published count family. The already covered cutoff is not used as the basis of the originality or value determination.

The dated certificate retains the supplied scientific assessment, sources and limitations.
