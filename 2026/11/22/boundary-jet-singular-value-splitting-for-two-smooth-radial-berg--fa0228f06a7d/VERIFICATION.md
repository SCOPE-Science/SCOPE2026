---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

PASS applies to /workspace/repairs/4/RESULT.md, not to the frozen all-block canonical projection. The frozen claim has a genuine tie obstruction: with alpha=0, h1=t and h2=sqrt(15)(t²−t), Delta=2sqrt(15) but the degree-n=0 block has Gram I/6. The spectral projection for its equal pair has rank two, not rank one. The frozen proof also incorrectly counts at most one nonzero singular value at output frequency −1. The repair uses the smaller-eigenvalue Gram projection only in untied blocks and assigns zero at ties and frequency −1 for the lower-channel operator; the full row has exactly two negative-frequency singular values since their outputs bar(z) phi_i(t) are independent by Delta≠0. Both finite-block facts were checked independently by exact integrals in /workspace/branches/independent-replays.py 4. For n≥0 the normalized monomial images are centered h_i under Beta(n+1,s) times the common scalar sqrt(mu_n/mu_(n+1)). Beta moments show that X=n(1−t) has fixed-order moments (s)_k+O(n^−1). The centered Taylor remainder is O(n^−3) in L² by the sixth beta moment. The centered X and X² have limiting variance s, covariance 2s(s+1), and X² variance 2s(s+1)(2s+3). Subtracting the projection of centered X² onto centered X gives residual squared norm 2s(s+1); equivalently the centered wedge norm square is 2s²(s+1). The symbol wedge carries −Delta/(2n³), so the Gram trace is s||v||²/n²+O(n^−3), and determinant is |Delta|²s²(s+1)/(2n^6)+O(n^−7). Their quotient and positive roots give both coefficients with the stated error. Positive block rank follows because an affine dependence among 1,h1,h2 would force Delta=0. The asymptotic gap is strict, so the repaired projection omits only finitely many modes; the lower threshold, both logarithmic masses and rearranged tails are unchanged. The frozen checker was read, not executed.

## originality

PASS

Reassessed for the repaired arbitrary-complex-C³ two-input theorem. The monomial hierarchy predecessor contains a direct polynomial row special case, including both branches and their thresholds; neither the fixed polynomial moment constants nor the finite-block tie convention is claimed as original. The distinct content is the jet-dependent lower coefficient and sharp error for all fixed nondegenerate smooth radial pairs, preserved by the repair.

## value

PASS

After removing the tied-block ambiguity, the useful content remains a stable, sharp description of the hidden scale of a rank-one leading covariance in a natural two-input Hankel problem. The second coefficient detects jet directions invisible to the first, with a distinct ideal threshold and an explicit nonpolynomial benchmark. This gives more than scalar upper bounds or a fixed moment-table computation; the claim does not extend to degenerate jets.

The dated certificate retains the supplied scientific assessment, sources and limitations.
