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

# Reproduction and limitations

Use Python with NumPy and SciPy as declared in `requirements.txt`, then execute `python3 checker.py`. The program calculates border polynomials, their dominant positive zeros, and the associated denominator derivatives. Independently it constructs the complete forbidden-edge de Bruijn matrix for each target, computes left and right Perron eigenvectors, and compares their symbol transition marginals with the border predictions. It checks all ternary forbidden words through length five and quaternary forbidden words through length four; it also checks direct finite avoidance enumeration in 135 cases. The replay yielded 703 targets and 3,129 pairwise signs with no failures.

The proof of the infinite statement is analytic and combinatorial, in `RESULT.md`. A finite numerical sweep cannot by itself certify all alphabet sizes or forbidden lengths, cannot establish priority, and is not an independent mathematical audit. The root calculation assumes the stated primitive presentation and the strict interval established in the proof; the code implements these relationships separately from the left/right eigenvector calculation.
