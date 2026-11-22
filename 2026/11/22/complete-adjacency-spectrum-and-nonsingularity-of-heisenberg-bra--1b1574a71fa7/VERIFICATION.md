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

The proof follows by exact invariant-space decomposition and symbolic determinant expansion. Run `python verify_heis.py` in the same folder with NumPy and SymPy. The checker creates the full adjacency matrix directly from Brandt products and Heisenberg commutators, checks five spectral identities, and prints test summaries. Results are stored in `verification_output.txt`. Numerical finite cases are corroboration only; arbitrary finite fields and matrix indices are established by the algebraic proof. No independent audit has been performed.
