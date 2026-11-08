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

# Reproducibility and verification

Run `python3 verify.py` from the extracted package with standard Python 3. The expected terminal marker is `VERIFY_OK exact_assertions=110526`.

The code checks, using exact `Fraction` comparisons rather than floating point: the support inequality \(H_m(s)\le B_s\) and sharp equality cases in the saturation range for \(1\le m,n\le45\); the strict coordinate-cap obstruction for \(2\le m<n\); and an independently generated set of vertices and indicator-functional maxima for \(1\le m,n\le4\).

The universal claim is a mathematical theorem proved in RESULT.md, not a conclusion drawn from the parameter cutoff. The verifier checks formulas and boundary cases but does not formally verify the differentiability argument, the general uniqueness theorem for John ellipsoids, or literature priority. Only a self-review has been performed. Independent validation and independent audit have not been performed.
