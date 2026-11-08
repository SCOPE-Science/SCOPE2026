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

# Reproducibility

Run `python3 verify_even_graphs.py` with Python 3 and no third-party dependencies. The program constructs the binary cycle space of every complete graph with four through seven vertices, enumerates exact rational even-subgraph weights at seven rational probabilities, and separately computes the same edge-moment formulas by the \(\{\pm1\}\) character expansion. It tests adjacent and disjoint covariance identities plus the entire asserted sign table, reporting 112 passed assertions.

The all-order proof uses a polynomial Fourier identity, a Gaussian mixture for the complete-graph ferromagnetic Ising model, complementation of edge subsets, and strict positivity of variance and Cauchy--Schwarz moment determinants. Enumeration cannot certify the infinite range. The derivation applies to \(n\ge4\), \(0<p<1\) only; the \(p=1/2\) case is treated separately by cycle-space rank. No independent mathematical or publication-priority audit has been performed.
