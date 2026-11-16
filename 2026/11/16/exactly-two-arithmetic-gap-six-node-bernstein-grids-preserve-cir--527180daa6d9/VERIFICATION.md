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

# Verification scope

Execute `python3 CHECK.py` with the Python 3 standard library. The checker performs **49 exact rational-interval sign assertions** (plus elementary algebraic interval and pi-bound assertions), prints an `EXACT_RATIONAL_INTERVAL_CHECK_OK` marker, and has no stochastic component or external dependencies. Its intervals for \(\sqrt3\), \(\sqrt5\), and \(\pi^2\) are enclosing rational intervals. The bound for \(\pi\) is derived by Machin's identity and alternating arctangent bounds.

The finite signs cover all \(m\bmod 2q\) for both \(q=5\) and \(q=6\), the first and third odd Fourier modes, the derivative monotonicity that covers every larger odd frequency, the even-frequency monotonicity, the forbidden small-gap mode, and the exact remaining rational exception. They do **not** certify the general positive-type reduction, roots-of-unity exhaustiveness, or endpoint integration formula mechanically. Those steps are proved analytically in `RESULT.md` and were checked as mathematical arguments. Numerical checks alone would not prove an all-frequency statement.

The theorem does not classify all possible six-node grids or strictly positive-definite outputs. Novelty is relative to inspected scientific evidence; independent audit and external validation have not been performed.
