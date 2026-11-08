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

# Reproducibility checks

Run `python3 checker.py` using only the Python 3 standard library. The checker constructs the two undirected graphs independently from their edge definitions; builds their exact integer Laplacians; computes rational pseudoinverses using a rational Gauss–Jordan inverse of \(L+J/N\); checks row sums and \(LL^+=I-J/N\); computes reciprocal-square traces exactly; and compares both to the radical formulas at high decimal precision for each \(3\le m\le10\). It also checks the positive difference formula for \(3\le m<50\).

The finite replay printed `PRISM_MOBIUS_LAPLACIAN_SIMPLEX_CHECKS_PASSED exact_m= 8 spectral_m=47`. At \(m=3\), the exact trace difference was \(2/25\). The checker cannot prove the claim for unbounded \(m\); all-integer validity rests on the Fourier-series and simplex geometry proof in `RESULT.md`. It neither establishes historical novelty nor supplies independent audit.
