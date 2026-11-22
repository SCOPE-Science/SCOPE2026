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
# Reproducible verification

Run `python3 verify.py` with Python 3 and its standard library. The program builds the vertices and sides in hyperboloid coordinates and minimizes point-to-segment geodesic distance using the hyperbolic point-to-line perpendicular-foot criterion, with endpoint clamping. This is an independently implemented distance calculation, separate from the claimed closed formula. It tests polygon orders 3, 4, 5, 6, 7, 8, 11, 20, 37 at several radii, across both branches and the threshold, with 51 boundary samples per polygon, and checks the limiting coefficient.

Observed output: `PASS: 169 hyperboloid endpoint, interior projection, threshold, and limit checks`.

The proof uses exact hyperbolic trigonometric identities and a global nearest-side argument, not exhaustive numerical enumeration. Floating-point minimization at tested sizes cannot verify the universal quantifiers. No independent external mathematical audit has been performed.
