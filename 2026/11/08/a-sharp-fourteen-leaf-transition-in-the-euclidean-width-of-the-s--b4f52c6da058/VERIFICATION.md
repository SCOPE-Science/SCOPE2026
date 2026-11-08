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

The proof is mathematical and appears in `RESULT.md`, Sections 1–3. The included `verify.py` is a self-contained corroboration using rational cut ratios, direct tube-enumeration support functions, and deterministic finite test directions. Run `python3 verify.py` after extracting files from the same record. Successful output from the extracted file was:

`STELLOHEDRON_WIDTH_CHECKS_PASSED direct=1154 exact_cut_comparisons=90983`

The cut comparison was checked for dimensions \(3\) to \(350\), and independent direct support widths were computed for dimensions \(2\) to \(8\). Nonlinear optimization over all directions was **not** delegated to numerical computation: the proof's strict centered-step-vector decomposition reduces the full sphere to finitely many rays in each dimension. Independent mathematical audit has not been performed; the historical noncoverage assessment is provisional.
