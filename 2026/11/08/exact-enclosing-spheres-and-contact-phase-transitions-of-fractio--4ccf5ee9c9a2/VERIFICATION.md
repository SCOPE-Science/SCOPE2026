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

Run `python3 verify.py` with Python 3 and its standard library. The checker directly constructs every Boolean and one-fractional vertex for each tested truncated cube, computes the center and squared radius as exact fractions, compares the squared distance for **every** enumerated vertex, checks the full contacting-vertex count and boundary conditions, and probes competitor diagonal centers. Its exact-arithmetic run prints: `PASS 401 parameter instances, 45451 exact rational assertions; transition n=5 tau=8/5 has 25 contacts`.

The tested dimensions are \(3\) through \(8\), including integer caps, a selection of rational caps and transition values. The code explicitly asserts the special \(n=5\), \(\tau=8/5\) contact count of 25 and radius squared \(17/20\). Separately, nonsymmetric SLSQP epigraph minimizations were carried out on five illustrative cases; all matched the symmetric formula to numerical tolerance. The optional numerical calculations do not form part of the required standalone verifier.

The unrestricted correctness certificate is the derivation in `RESULT.md`: exact vertex types, strict convexity and symmetry, two competing squared-distance quadratic profiles, the global median minimizer, and strict equality-case classification. A finite exhaustive enumeration in bounded dimension is not an infinite-dimensional proof. The verification establishes nothing about historical priority beyond the references and comparisons explicitly cited.
