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

The formulas, universal supporting-contact construction, and global optimality proof are reconstructed in `RESULT.md`. Direct substitution checks the identities \(c-u=t\), \(v^2-u^2=dcu\), and \(c^2+v^2+cu/d=1\). The normalized regular-simplex vectors are actual supports of the affine-normalized cap and form an exact centered isotropic frame, proving unrestricted global volume maximality by the determinant/trace inequality.

The standalone `check_cap_john.py` was executed and passed 6,922 deterministic diagnostic assertions spanning eight finite dimensions, eight cut heights, angular containment, exact simplex isotropy, numerical occupied fractions, thin-cap limits, Gaussian-window convergence and monotonic sample values. These finite checks corroborate but do not prove the universal assertions. The proof of strict monotonicity of the limiting profile uses the strictly positive conditional normal variance, not numerical sampling.

Unproved limits: no general finite-dimension strict monotonicity assertion for the occupied fraction; no uniformity in moving Gaussian-window parameters; no extension to several nonparallel cuts; no independent mathematical audit or exhaustive historical priority certification.
