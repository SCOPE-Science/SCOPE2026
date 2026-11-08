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

# Reproducibility and boundaries

Run `python3 verify.py` with Python 3 and no third-party packages. The script uses exact rational arithmetic and a two-dimensional representation of \(\mathbb Q(\sqrt5)\). It checks the five-facet formula and constructive feasibility for \(1323\) rational floor pairs over \(m=4,5,6\), checks \(150\) explicit eigenvector equations for complete matrices, verifies strict facet witnesses, and confirms even-cycle redundancy for the tested sizes. The expected final line begins with `VERIFY_OK`.

The unbounded family and the global optimum over all symmetric stochastic transition matrices are established by the analytic averaging, Fourier, and inequality proof in `RESULT.md`, not by extrapolating a finite test grid. The script does not test publication priority or supply an independent audit.
