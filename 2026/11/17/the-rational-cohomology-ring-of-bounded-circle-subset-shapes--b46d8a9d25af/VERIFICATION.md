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

# Reproducibility and limits

The result's general proof is in `RESULT.md`, Steps 1–5. The proof uses the published sphere-homotopy theorem for \(\exp_k(S^1)\), the cohomological Serre spectral sequence of a finite-isotropy rotation action, rational/large-prime Borel-to-orbit comparison, reflection-transfer invariants, and universal coefficients.

Run `python3 gap_euler_check.py` with Python 3 standard library. The program enumerates the \(2j\) dihedral actions on normalized gap coordinates for each \(1\leq j\leq100\), calculates fixed-coordinate cycle counts and exact rational compactly-supported Euler averages, and checks their equality to the closed formulas. The expected output is included in `gap_euler_output.txt`, verified by replay from the packaged script. This check does not establish integral torsion at primes at most the cardinality bound. The all-cardinality Euler identity and the cohomology-ring result are proved symbolically in `RESULT.md`.

The universal Pontryagin class and truncation exponent are pinned down in the proof; the mod-two ring and integral homotopy type remain undetermined.
