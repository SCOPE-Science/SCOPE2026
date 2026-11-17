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

# Verification and proof dependency notes

The proved domain is every fixed integer \(d\ge4\) with strictly positive limiting box facet weights. The proof uses Cauchy's projection formula, exact sphere charts, an elementary weighted simplex volume calculation, a uniform radial-root expansion, and \(L^1\) convergence of conditional densities. These are independently reconstructible from the statement and do not use simulation.

Run `python3 check_brightness.py` with the packages in `requirements.txt`. The program samples Haar normals and tests the exact projection identity, local rare-event integrals for four-dimensional anisotropic examples, the second-order fixed-shape coefficient, and the non-smooth coalescing-facet coefficient in dimension four. The empirical checks use fixed seeds and specified tolerances; they do **not** verify statements for arbitrary inputs or settle scientific originality. All inputs and predicted numbers are computed inside the script; no external log, missing file or remote service is required.

Residual proof limits: the \(O_K(t^2)\) relative remainder in (1) is not uniform across varying facet gaps. The general moving-family assumption only promises an \(o(t)\) error, so no unconditional quantitative convergence rate in total variation is asserted. Independent mathematical audit has not been performed.
