---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

Direct size-r product weighting gives p_i=lambda_i e_{r-1}(lambda_-i)/e_r(lambda), sum p_i=r. Difference p_j-p_i=(lambda_j-lambda_i)e_{r-1}(other)/e_r gives order. With min lambda=1, the ratio e_r(rest)/e_{r-1}(rest) is nondecreasing in each positive variable by Newton inequalities; its maximum when all others K gives p_min=r/[r+(d-r)K]. For the ratio p_max/p_min, fixing h=lambda_max gives h(s+1)/(s+h) with s=e_{r-1}(middle)/e_{r-2}(middle), maximized as middle coordinates equal h; the final h maximum is K, giving (r-1+(d-r)K)/(d-1). Check all boundaries r=1,r=d,K=1 and strict equality cases. Exact independent subset enumeration checked 24,912 bounded integer-spectrum/dimension/block cases, both bounds and attainment; this corroborates but does not replace the symbolic monotonicity proof.

## originality

PASS

The complete accessible Entezari–Banerjee–Kalantari source provides the nonlinear expected-projector transform and its qualitative spectral equalization, but the inspected main theorem/section 3.2/proof gives no uniform sharp extremum under a Gram condition-number cap or exact smallest guaranteed block size. Rodomanov–Kropotov and Yu provide volume-sampling and inclusion majorization antecedents. The source theorem implies the input p_i formula but the sharp worst-case extremizer and simultaneous conditioning envelope require the nontrivial symmetric-ratio optimization; no stronger matching Resultary finding was located.

## value

PASS

The exact worst-case one-step contraction and exact smallest block size translate a spectrum cap to an algorithm-independent design guarantee, with equality spectra showing unavoidable limits. This gives a precise usable invariant not simply an ad hoc table or rearrangement of an existing numerical bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
