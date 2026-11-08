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

Run `python3 verify.py` with a Python 3 standard-library interpreter. The program evaluates the sharp integral constants numerically in dimensions 2–12, checks the exact two- and three-dimensional evaluations, independently compares the trihedral solid-angle formula with gnomonic integration at the smallest-angle vertex in seven tetrahedra, checks angular ordering and volume-normalized bounds in these examples, tests the bounds in sixty additional sampled configurations in dimensions 2–6, and approaches both sharp limiting three-dimensional families. Successful execution produces `REPRODUCIBLE_CHECKS_OK 181` and prints the constants in dimensions 2–4.

The numerical integration uses composite Simpson quadrature, and the sampling tests are finite and pseudorandom with fixed seeds. Neither process certifies arbitrary dimensions or exact inequalities; Steps 1–5 of RESULT.md provide the quantified proof, equality conditions, and sharpness limits. The arXiv primary source is publicly accessible; no external validation has been carried out.
