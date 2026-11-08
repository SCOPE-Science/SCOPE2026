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

# Verification

The mathematical proof is self-contained apart from standard Cayley tree enumeration and the classical factorial-moment criterion for Poisson convergence. Crucial analytic statements are the uniform \(O_k(1/d_n)\) tree-injection count, the exact incident-edge exponent, the bounded cross-set overlap correction, the all-orders factorial-moment calculation, and the \(O(p_n)\) cyclic-component exclusion. All are explicitly reconstructed in `RESULT.md`.

To reproduce the finite diagnostics, execute `python verify_regular_components.py` using Python 3.9+ without third-party dependencies. The script exhaustively checks four small hosts with rational probabilities, including one disconnected host, and compares independent tree-witness enumeration to full edge-subset enumeration. It also checks asymptotic exact formulas for complete graphs with finite-size centering; the script should print `PASS: 96 finite exact and asymptotic checks`.

Finite computations do not establish limiting probabilities. Neither independent validation nor any external correctness certification has been performed. The cited fixed-component Poisson literature concerns a different graph-generation model and may contain related implications requiring additional historical analysis.
