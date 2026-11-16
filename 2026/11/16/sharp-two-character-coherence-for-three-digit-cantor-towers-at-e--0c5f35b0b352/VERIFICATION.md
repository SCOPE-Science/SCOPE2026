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

# Verification of the stated formula
The proof is analytic and covers every integer base \(b\ge4\), every level \(n\ge1\), and all integer frequency gaps. Its key facts are (a) exact Fourier-mask factorization, (b) the complete individual mask minimization from a strictly concave trigonometric comparison or a strictly decreasing auxiliary sum, (c) compatibility of modular inverse residues across every level, and (d) convergence of the asymptotic normalization product.

Run `python CHECK.py` with `mpmath>=1.3`. It recomputes finitely many high-precision mask minima and minimizing congruence classes (including divisible-by-three zero cases). Numerical evidence cannot establish the all-base inequality; that follows solely from the analytic argument. No independent audit has been performed.
