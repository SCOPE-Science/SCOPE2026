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

On a fixed fused partition and fixed signs of unfused edges, the KKT block sums make each center derivative the average on its block. The proximal map is continuous piecewise affine. At width three, a unit step can have at most two partially crossing rows; their values are at most and at least 1/2, respectively, since either outer coefficient is at most 1/2. Thus all truncated step images are monotone with variation at most 1, and summing the signed input steps and integrating along generic line segments proves the bound, including nongeneric pairs by continuity. A sufficiently steep increasing ramp and a small jump between sites 2 and 3 give equality for every N≥4; N=3 has a single output. I independently reconstructed the baseline and perturbed proximal solutions from the dual vectors and block means (python /workspace/branches/independent_frozen_checks.py 5). The two types of strict KKT slack are valid in all 12 windows, with minimum 3/20, and the center changes divided by ε are (0,1/3,0,1,2/3,1), giving ratio 7/3 exactly at N=10. Positive scaling gives all λ; continuing the step at its final value leaves the six original windows and the input variation unchanged and can only increase output variation. This is a lower bound for width five, not a sharp global modulus.

## originality

PASS

The local-filter construction is already in Louchet–Moisan. The supported distinct result is the two-input path-variation boundary for its interior 1D interval implementation: exact contraction at width three and a realized width-five amplification bound. Neither the construction itself nor the fused-block derivative formula is claimed as new.

## value

PASS

A known local smoothing construction may be monotone in each input coordinate yet amplify the spatial variation of input perturbations. The result identifies the first odd width exhibiting that effect, with an exact stable regime and an explicit amplification witness under the same normalizations and endpoints. It is useful for deciding when the usual single-signal or global-prox intuitions do not transfer.

The dated certificate retains the supplied scientific assessment, sources and limitations.
