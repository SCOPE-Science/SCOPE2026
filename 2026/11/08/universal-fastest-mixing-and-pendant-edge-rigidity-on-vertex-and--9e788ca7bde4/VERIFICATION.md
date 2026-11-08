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

# Reproducibility and limits

`python verify.py` uses the pinned minimum Python library requirements in `requirements.txt`. The script checks the symbolic budget identity, lifted Fiedler eigenvector identity and Rayleigh identity; exact rational eigenvalues for \(C_4\) with \(r\in\{1,2,3,4\}\); spectral attainment for 80 instances (cycles, cliques, cubes and the Petersen graph with four leaf multiplicities each); and 960 seeded feasible, non-invariant competitors plus 1680 invariant competitors.

Expected replay: `SYMBOLIC symbolic eigenvector, budget, Rayleigh identities`; `EXACT_C4 27 distinct exact eigenvalues across four independent instances`; `VERIFY_OK 80 network eigenvalue checks; 960 noninvariant random competitors; 1680 orbit competitors; C4 exact rational spectra`.

Finite numerical comparisons do **not** prove global optimality, uniqueness or the infinite family. The proof uses exact Rayleigh quotient/equality arguments and spectral block inequalities. Numerical tolerances are stated in executable assertions. Independent mathematical audit has not been performed.
