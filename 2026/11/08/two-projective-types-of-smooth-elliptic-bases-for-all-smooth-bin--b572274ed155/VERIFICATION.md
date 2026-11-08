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

# Verification of the binary all-smooth quadric-pencil classification

Run `python verify_binary_quadric_pencils.py` (Python >= 3.10, SymPy). This is an exact, exhaustive calculation, not a statistical experiment.

The code verifies the classification by checking the Pfaffian criterion for every ten-bit quadratic form against the rank of its polar bilinear matrix; independently counting eligible polar pencils and their square-coefficient refinements; enumerating every pencil; taking all orbits under twelve transvections that generate \(\mathrm{GL}_4(\mathbb F_2)\); verifying explicit order-four stabilizer groups and their element orders; checking exact rational point counts; and computing exact Gröbner bases of all eight affine Jacobian ideals for the smooth-base representatives. Over \(\mathbb F_4\) and \(\mathbb F_8\), direct point counts match the stated genus-one Frobenius polynomials.

Successful local execution returned five orbit rows with sizes \(560,3360,5040,5040,336\), unit Gröbner bases \((1)\) in each of the eight charts, and the signature `BINARY_QUADRIC_PENCIL_SMOOTH_BASE_ORBITS_PASS 14336 5 5040 5040 10080`.

The mathematical claim is restricted to \(\mathbb F_2\) and geometrically smooth complete intersections; the computation does not establish general finite-field cases or historical priority. Independent verification and audit have not been performed.
