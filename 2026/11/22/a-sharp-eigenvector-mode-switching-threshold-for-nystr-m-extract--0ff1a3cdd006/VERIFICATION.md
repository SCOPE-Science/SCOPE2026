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

# Verification and limits

The theorem is proved by exact, two-block spectral elimination in `RESULT.md`. In particular, the diagonal Rayleigh--Ritz entries are \(1-(1-a)u\) and \((1-\delta)(1-u)\), while the two nonzero Nyström eigenvalues are \(1-\delta_c(a,u)\) and \(1-\delta\). Their difference gives the exact separating threshold; no numerical root-finding is involved.

Run `python verify.py` to reproduce exact rational identities and branch checks. The verifier checks 874 admissible rational parameter sets, including the equality threshold, the fourfold example, and one fully reconstructed rational four-by-four Nyström operator. All checks passed when the files were packaged. The finite checks do not prove the all-real-parameter theorem; its proof is the algebra in `RESULT.md`.

The top eigenvector is uniquely defined only away from the stated Nyström tie surface. The construction is exact-arithmetic and positive semidefinite; no claim about finite-precision eigenvector computation is made. Historical originality has been compared against available published sources, but independent audit and a comprehensive priority guarantee have not been performed.
