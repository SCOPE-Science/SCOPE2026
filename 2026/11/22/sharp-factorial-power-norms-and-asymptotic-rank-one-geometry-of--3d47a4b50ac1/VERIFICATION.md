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

# Reproduction and boundaries

Run `python verify.py` with Python 3.10 or later; the script uses only the Python standard library. It checks exact rational polynomial coefficient identities for three supported polynomial symbols, independently expands the iterated kernel, tests the constant-function formula, measures finite polynomial \(H^2\) boundary-Laplace ratios, and verifies support-rescaling invariance in two binomial examples. The executed checker reported 168 passing assertions and nine representative finite Laplace ratios in the range 0.998835087 to 1.000042599.

The theorem's infinite-dimensional correctness is established by the displayed analytical proof: induction for the exact iterated kernel, the Hardy-space operator-norm error bound, and the nondegenerate circle Laplace method with all maximizing angles counted. The checker is supplementary: finite tests do not establish an all-parameter operator statement and do not verify the remainder estimate for every integer or symbol. The symbolic calculations include no external datasets or unspecified dependencies.

No independent external mathematical audit has been performed. Originality is assessed against the explicitly identified primary literature and scientific search evidence, subject to unindexed-historical-work risk.
