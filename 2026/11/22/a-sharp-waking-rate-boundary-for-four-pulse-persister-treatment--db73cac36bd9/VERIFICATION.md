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

# Reproducible mathematical verification

Run `python verify.py` with Python 3, SymPy and mpmath. The script exactly expands both \(2\times2\) commutator and four-product trace identities, tests a common eigenvector and the \(z_*=\sqrt5\) exact example, and evaluates 144 strict phase cases, 36 independently composed finite switching words at the resonance, and two opposite Floquet stability examples at 65-digit working precision. Matrix exponentials are computed directly, not from precomputed package paths. Numeric traces are compared at a magnitude-relative tolerance because the examples include exponentially amplified entries; the proof does not depend on those tolerances.

The universal argument instead uses a strictly positive time-divided-difference coefficient in Cayley–Hamilton's \(2\times2\) exponential representation and the algebraic quadratic \(Q(z)\) with negative leading term and positive constant. At the unique positive zero the generators share an explicitly constructed strictly positive eigenvector, yielding all-order growth exactly. The code verifies necessary concrete algebraic identities and examples but does not purport to computationally enumerate all positive real rate tuples or to establish prior-art novelty. No independent external audit has been performed.
