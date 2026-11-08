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

# Exact verification and its limits

Run `python3 check_boundary.py` in the same directory with a standard Python 3 interpreter; it has no nonstandard dependencies. The file `verification_output.txt` contains the output of the actual replay. The program enumerates all 91 points of \(\mathbb P^2(\mathbb F_9)\) with exact arithmetic, confirms the 28/63 Hermitian division and the 28 one-tangent/63 four-tangent incidence partition, checks that the four rational hyperflex tangent restrictions have nonsquare coefficient 2, and verifies surface counts over \(\mathbb F_3\), \(\mathbb F_9\), and \(\mathbb F_{27}\). It ends with `CHECK_OK` on success.

The code is *not* an exhaustive check over every extension field and does not calculate cohomology directly. The infinite extension-field formulas follow from the explicit Hermitian tangent identities, Frobenius action on components, and the known rank-eight del Pezzo Picard representation. Cohomology follows from the normalization and localization exact sequences, including the verified injectivity justified in the proof. The mathematical and historical-priority assessment is same-model only; no independent audit has occurred.
