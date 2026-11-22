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

## Actual mathematical verification
Run `python3 verify.py` using Python 3. No third-party packages or external data files are required. The checker evaluates all displayed moments by two independent exact symbolic integrations: the affine image of a unit four-simplex and an independent product-cube parametrization of a single signed-and-sorted chamber. All computations use Python `Fraction` objects and sparse integer-exponent polynomials. It checks the 24-cell vertex set, Hadamard preservation of that set, all moment constants through degree six, the exact fourth isotropy coefficient and the sixth-direction defect. A successful run prints `VERIFY_OK`.

The analytic proof separately establishes the Voronoi halfspaces, 384-chamber partition, Jacobians and all-direction tensor identities. Neither numerical sampling nor a finite list of tested directions is used to substitute for those infinite-domain arguments. The checker verifies exact integral values but cannot independently certify bibliographic priority, optimality among other lattices or external mathematical audit.
