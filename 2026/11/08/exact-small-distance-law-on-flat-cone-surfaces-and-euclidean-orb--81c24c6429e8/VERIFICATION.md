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

# Reproducibility and checks

Run `python3 verify_flat_cone.py` from this directory. It uses only Python 3 standard libraries and prints the independent angle-integral, radial-ball-integral and closed expressions for each of four orbifold cone orders, three further angle-integral checks, three overlap-convolution checks and the five strictly ordered signature values. An exact square-pillowcase convolution calculation and the analytic Fubini argument are given in `RESULT.md`.

Expected successful final line:

`FLAT_CONE_CHECK_OK angular=7 radial=4 pillowcase_convolutions=3 signatures=5`

For each order the angular calculation is a numerical quadrature of the auxiliary angular integral, while the radial calculation integrates the actual area of individual balls in polar coordinates. The difference between these computations is small, and both agree with the symbolic closed coefficient. The pillowcase integral checks that the overlap of two Euclidean disks integrates to the square of disk area, giving the independent exact check \(F(r)=2\pi r^2-\pi^2r^4\) near zero.

These are finite numerical validations and a special-case identity. They do not prove the formula for all cone angles or all compact flat cone surfaces; that proof is in `RESULT.md`. The whole result has no independent audit.
