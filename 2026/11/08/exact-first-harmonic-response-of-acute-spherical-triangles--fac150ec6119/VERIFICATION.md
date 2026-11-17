---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

For normalized uniform area on S², the side separation has density sin(d)/2; the two angle-at-endpoint conditions restrict longitude to |t|<d/2, while the third-angle inequality gives the latitude cutoff and excludes d>=π/2. Integrating in the fixed domain gives M0=1/(2π)-1/8 and M1=(π-2)/64; independent nested numerical integration gave 0.0341549430918961 and 0.017837385212327146, agreeing with those exact values. Common antipodal reversal cancels odd dipole terms; rotational isotropy of the rank-2 tensor gives three M1/3 cross terms, hence the full exact dipole law p0+ε²M1 on [-1,1]. Normalization and Taylor expansion of the von Mises–Fisher likelihood give the pinned derivative 2M1=(π-2)/32 and three-iid even quadratic coefficient M1. Strictly acute intrinsic spherical angles and measure-zero degeneracies are handled; local Fisher expansions are not asserted global.

## originality

PASS

The original weighted cosine moment and all-parameter dipole probability are distinct from Maeda’s known uniform type probability and Li–Cooper–Eum’s numerically observed pinned Fisher response. No matched or dominating weighted-result theorem was established in inspected material; best-of-knowledge PASS with explicitly material literature risks.

## value

PASS

The exact initial concentration response to a previously studied pinned directional sampling model is a natural probability quantity. A single nontrivial weighted spherical moment also yields an exact whole-interval first-harmonic perturbation law, not just a numerical slope or textbook symmetry restatement. These geometric-probability and directional-statistics quantities are independently useful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
