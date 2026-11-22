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

# Reproducible finite verification

Run `python3 verify_d4.py` with Python 3.10 or newer; no third-party packages or external files are required. The program exhaustively reconstructs the Coxeter group, reflection lengths, the proper-part lattice, the rank-reversing complement, all barycentric quotient cells and their oriented boundaries, and an exact CW reduction with 159 single-occurrence generator/two-cell cancellations.

The executed verifier reported `D4_KREWERAS_MOORE3_TWO_SPHERES_OK` and final attaching words `(-x)^3`, `x^3`, and the trivial loop. It checked group size 192, lattice size 50, barycentric quotient cells (72,231,162), connected one-skeleton and the complete cancellation sequence.

**Scope:** These checks establish the finite claimed model, not a theorem for other Coxeter types and not independent external validation. The full geometric homotopy statement additionally uses the standard facts that maximal-tree contraction, elementary generator/two-cell cancellation and two-cell sliding preserve CW homotopy type.
