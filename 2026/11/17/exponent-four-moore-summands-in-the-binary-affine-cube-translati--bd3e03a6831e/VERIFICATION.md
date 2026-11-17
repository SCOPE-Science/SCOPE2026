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

# Reproducibility of the exact calculation

Run `python3 verify.py` with the Python standard library only. It computes and checks the \(14\) omitted affine planes, \(56\) independent tetrahedra, barycentric flags, orbit representatives and Burnside sums. It constructs the oriented integral quotient boundary matrices, verifies \(\partial^2=0\), executes precisely \(311\) algebraic unit cancellations, and checks the four determinantal divisors of the remaining four-by-four matrix. `verification_output.txt` stores the complete expected standard output from an actual run of the embedded source.

The fixed-midpoint checks are finite corroboration of the use of Armstrong's theorem. The exact matrix reduction calculates integral homology only; the arguments for the fundamental group and the Moore-space splitting are mathematical steps supplied in `RESULT.md`, not conclusions inferred solely from printed computational logs. This certificate checks one finite complex and makes no claim of independent external verification.
