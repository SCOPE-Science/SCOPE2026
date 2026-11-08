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

# Reproduction and analytical limits

Execute `python3 check_leafpa.py` using the Python 3 standard library. No network connections, external dependencies, or datasets are required. The script obtains the complete probability distribution of small labelled growing trees from the original leaf-degree attachment weights, independently calculates the one-dimensional leaf-count Markov law, and compares them for five rational parameters through eight vertices. It additionally checks weight normalization, probability-mass conservation, polynomial differentiation, a strict critical-point bracket and numerical fixed-point/variance identities. The recorded run produced 8,919 passing assertions.

The strong law follows from the exact Bernoulli growth recurrence and a summable-noise almost-supermartingale inequality. The Gaussian limit follows from the linearized weighted martingale-array central limit theorem, using almost-sure convergence of its predictable variance and automatic Lindeberg control from bounded jumps. A fourth-moment estimate bounds the nonlinear remainder in \(L^2\). The maximization is a deterministic cubic-root sign argument. Neither finite tree enumeration nor floating-point evaluation establishes these infinite and universal claims by itself.

The result applies to each fixed \(a>0\), with a two-vertex edge as seed and leaf degree defined as the number of adjacent degree-one vertices. No separate independent audit has been performed.
