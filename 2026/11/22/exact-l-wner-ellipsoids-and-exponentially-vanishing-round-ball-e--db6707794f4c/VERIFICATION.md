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

## Reproducibility
Run `python3 verify.py` with Python 3 and NumPy. The script constructs the full ordinary unsigned cycle incidence coordinates, centers the exact vertices, obtains the numerical tangent basis independently, and checks eigenvalues, covariance contact identities, both sets of semiaxes, enclosing sphere radii, and the exact formula for volume ratios across \(m=2,\ldots,20\). The actual completed run printed `EVEN_CYCLE_LOEWNER_PASS orders=2..20`.

## Mathematical verification
The all-dimension argument is contained in `RESULT.md`: (i) the even-cycle incidence matrix has just the constant and alternating excluded Fourier modes, (ii) the cyclicly symmetric vertex covariance provides a positive isotropic contact certificate for the minimal enclosing ellipsoid, (iii) AM–GM proves global optimality and uniqueness including arbitrary centers, and (iv) the exact trigonometric sine product yields the volume formula. The numerical script is finite corroboration only; it neither certifies novelty nor replaces the symbolic all-integer proof.

## Limits
The proof concerns the unweighted even-cycle realization in its inherited Euclidean metric. It does not address other polytopes, weighted edges, perturbations or independent replication by an external auditor.
