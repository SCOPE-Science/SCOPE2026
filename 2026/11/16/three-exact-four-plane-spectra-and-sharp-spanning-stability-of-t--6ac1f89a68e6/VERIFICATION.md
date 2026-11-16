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

## Reproduction

Use Python 3 and SymPy 1.14 or another compatible version. From this directory, execute `python certificate.py --all` and `python certificate.py --roots`. The first command constructs and verifies the six exact cyclotomic block-Gram polynomials using the prime-field character and checks their complete orbit partition. The second uses exact polynomial root counting over the real quadratic field to verify the three strict lower-eigenvalue intervals.

The characteristic-polynomial test is performed in \(\mathbb Q(\zeta_{55})\) using rational arithmetic. It verifies every coefficient, including the one-dimensional zero eigenspace in the twelve-column Gram matrix, and hence the positive spanning rank of the corresponding eleven-dimensional projection sum. This does not constitute an independent mathematical audit.

## Limits

The certificate is for the explicit character \(\chi(2)=e^{2\pi i/10}\), eleven planes and four-plane subsets. It does not address arbitrary EITFFs, arbitrary character generators, or spectral stability for a different number of subspaces. The root intervals are algebraic, not measurements.
