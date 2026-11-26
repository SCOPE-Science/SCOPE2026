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

The marked exponentials and censor atom exhaust the record. Each positive-length labelled density identifies slope and intercept even at equal rates; any zero-information tangent must annihilate both the constant and linear coefficients in both event scores and is zero. In intensity coordinates a_j=p_j lambda_j, the nuisance block is B diag(1/a_j)+O(B^2), the cross vector has entries -v_j B^2/2+O(B^3), and the target information starts at (B^3/3) sum a_j v_j^2, with v_j the p derivatives at fixed intensities. The censor atom contributes at order B^4 to the last block. Projection gives 1/3-1/4=1/12. Independent replay in the original rate coordinates recovered the same coefficient, with Fisher ratios 1.00300, 1.00040 and 1.00350 at B=.001 for the three frozen cases. Known-rate scores give the linear coefficient; at large B the event integrals converge by exponential tails and the censor contribution is bounded by a polynomial in B times an exponentially decaying probability, so complete-data orthogonality applies. The matched-intensity root-density difference is linear in t and integrates to the stated B^3/12 constant; the squared atom difference is O(B^4). Independent integration gave ratios .99759 and .99879 at B=.001. Tensorized affinity gives a positive lower bound along any bounded-MB^3 subsequence, and fixed MB makes total variation tend to zero. The theorem is a necessary bound on consistent discrimination, not literal nonidentifiability at any positive B or an estimator guarantee. Frozen checker was inspected, not executed.

## originality

PASS

Best of examined literature. The motivating paper gives precisely this marked likelihood and warns that heavily censoring unknown rates impedes estimation. The singular efficient-information coefficient and tested fixed-intensity alternatives quantify, rather than rename, that warning. No earlier covering theorem was found in the inspected material.

## value

PASS

Resolves a concrete observability question raised for trajectory filtering: estimating outcome proportions with uncalibrated durations costs two additional powers of short observation time, even when one retains exact times and labels. The matched-pair result shows that this is not merely a large standard error of one estimator; at a fixed total allocation some distinct models become indistinguishable. The advantages are specific to the posited parametric experiment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
