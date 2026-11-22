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

The all-size derivation is in `RESULT.md`, using an explicit five-dimensional invariant quotient and a determinant identity. Execute `python3 verify_capture.py` with Python 3 and no third-party dependencies. It independently constructs the complete Laplacian and its exact-rational Krylov projector for 100 graph/weight choices, including both sides of the balance resonance; it checks the rank and every site-localized capture probability. The successful run returned `PASS: 100 independent exact-rational full-graph cases; ranks and all site capture probabilities agree.` This finite computation is not substituted for the symbolic proof.

The model assumes positive bridge and trap strengths, no decoherence, the combinatorial Laplacian Hamiltonian, and eventual rather than finite-time capture. Self-review only; independent audit has not been performed.
