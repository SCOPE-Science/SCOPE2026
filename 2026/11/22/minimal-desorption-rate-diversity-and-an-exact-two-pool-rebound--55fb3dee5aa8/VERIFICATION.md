---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and scope

Execute `python3 verify.py` using Python 3 and only its standard library. The script constructs the exact three-compartment rational generator and nonnegative initial state, checks initial negative air derivative, and certifies the positive derivative at \(t=1\) and negative derivative at \(t=5\) by exact rational Taylor sums and explicit absolute bounds. The complete at-most-two-stationary-points conclusion comes from the spectral proof in `RESULT.md`, not numerical scanning. There is no claimed independent external validation. The demonstration is an ideal source-free reversible adsorption model, not a measured exposure response.
