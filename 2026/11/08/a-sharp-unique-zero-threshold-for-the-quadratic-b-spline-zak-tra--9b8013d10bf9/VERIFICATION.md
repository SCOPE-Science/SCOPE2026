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

# Mathematical verification
The only accepted claim is the unique-zero threshold in the first subunit band. The Zak normalization and five-term support truncation are explicit in RESULT.md. Independent steps of the analytical proof were checked against the exact B-spline formula: (a) the concavity of \(D_b\) on all knot chambers; (b) its strictly positive endpoint value; (c) nonnegativity of the cosine quadratic on the \(x=0\) boundary; (d) negativity of the derivative of the alternating sum for all \(x<1/2\); and (e) the known aliasing obstruction for \(b>5/3\).

Running `python3 CHECK.py` with the standard Python library checks a finite grid of 931 rational configurations. This reproducibility test is not an exhaustive proof over real values. The published source [1, Proposition 4.3] establishes the below-threshold horizontal line segment. No external independent audit or machine-checked infinite proof has been performed.
