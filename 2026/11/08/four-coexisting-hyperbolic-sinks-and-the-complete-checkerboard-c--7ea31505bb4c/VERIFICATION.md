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

# Reproducibility and scope

Execute `python verify.py` from the directory containing `verify.py`. Requirements: Python 3, SymPy, and NumPy. The program has no network dependencies.

The exact-arithmetic checks include the rational reduction of the alternating fixed-point equation to the quartic polynomial, the root-bracketing sign tests, derivative identity, rational envelopes of the Fourier trace and determinant, and the homogeneous stability inequalities. Numerical replay also evaluates the original simultaneous network update on even rings of lengths 2, 4, 6, 10, and 50 at both signs of the two checkerboard roots and at each of the two homogeneous states; it checks the Fourier eigenvalues at each mode. Execution returned:

`VERIFY_OK polynomial_identity=1 exact_root_brackets=4 stability_rational_bounds=12 ring_sizes=5 states_checked=20 Fourier_modes_checked=288`

The infinite family of ring lengths is established analytically by mode reduction and bounds applying to every real Fourier cosine parameter in \([-1,1]\). These finite checks do not constitute a complete computational enumeration of all ring lengths or all spatial equilibria. The eigenvalue tests certify local linear stability for selected states, not global attraction or basin size. Independent scientific validation has not been performed.
