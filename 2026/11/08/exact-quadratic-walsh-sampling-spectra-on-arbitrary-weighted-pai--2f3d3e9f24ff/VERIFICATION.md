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

# Verification evidence and boundaries

The proof uses exact rational identities: the blockwise cube-orthogonal decomposition; the identity \(c_1(u)=1-\rho_2(u)\); the pair-incidence eigenvalues \(-2\) and \(+1\) on the quadratic harmonic subspace; and the identity \(1-2\rho_2(u)+\rho_4(u)=c_2(u)\). These yield the exact spectrum for **all** integers \(n\ge5\), all \(2\le k<\ell\le n-2\), and all \(0<\vartheta<1\). The proof itself, not a numerical observation, establishes positivity and the one-dimensional kernel.

For reproducibility, execute `python checker.py` with SymPy. The code uses exact rational shell moments rather than floating-point approximations; it explicitly tests mixed pairs in dimensions 5, 6, 7, 8 and 9, and the central specialization in seven odd dimensions. The expected output ends with `TWO_HAMMING_LAYERS_EXACT_CHECKS_PASS 201 matrix directions and seven central families`.

No external, independent mathematical audit has been performed. The finite checks do not exhaust the parameter set, and literature uniqueness remains provisional. No accuracy claim is made outside the stated domain.
