---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Over the stated split characteristic-two ring, U=I+N+εB satisfies U²=I exactly when N²=0 and NB=BN. In a basis of im N, a complement in ker N, and a lift of the image basis, N has only the (1,3) identity block. Its commutant has independent blocks P,Q,X,Y,Z of dimensions r²,s²,rs,r²,sr, and repeats P in the last diagonal block, where s=n-2r. Invertibility requires P and Q invertible. The q^d commuting B cancel q^d in the group centralizer, leaving |GL_n|/(Φ_rΦ_s) by the unique field Jordan orbit at rank r. This includes the identity and gives q^(n²) at r=0; empty diagonal blocks give the stated boundary convention. For N₀=m+1 ranks and b=Φ_∞^-2, the deficit D=N₀b-∑w_r is at most b C_q by bounding 1-Φ_∞/Φ_k by q^-k/(q-1) and summing the two geometric series. Comparing w_r/∑w_r to w_r/(N₀b) and then to 1/N₀ gives TV≤D/(N₀b), which proves the constant, while summing gives the total asymptotic and rescaling the uniform grid gives the weak law. Over the field alone the uncancelled exponent is r²+(n-r)², penalizing a deficit j=m-r by q^(-2j²-2(n-2m)j) up to bounded product factors, consistent with the stated contrast. The supplied checker and recorded counts were inspected, not rerun; they agree with the strata and are not the proof of the general formulas. No extension to characteristic four or nonsplit rings is inferred.

## originality

FAIL

A distinct Resultary record already states the exact residue-rank marginal, the total count asymptotic and the uniform law in a stronger square-zero dual-number Smith census. Translation by the identity gives exact equivalent coverage, not just shared terminology or matching small n. The explicit TV constant was not located verbatim, but it is a routine bound from the already established absolute summability of the rank-weight deficits and does not rescue the finding.

## value

FAIL

The uniform law is a meaningful phenomenon, but its exact enumeration and law are already available with finer structure. In the uncovered wording the only potential increment is a nonsharp explicit constant for a TV estimate that follows from the prior absolute weight-error estimate. There is no demonstrated threshold, sharp TV asymptotic, or application requiring this constant. Isolating that estimate would not leave a worthwhile repaired finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
