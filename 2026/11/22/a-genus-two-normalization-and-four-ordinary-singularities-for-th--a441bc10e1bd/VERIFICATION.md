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

# Exact checks and mathematical limits

Run `python CHECK.py` with Python 3.10+ and SymPy 1.12+. It reconstructs all thirteen rational projective base points, the three triple fat points, the remaining ten simple points, and \(Q_0=(2:5:1)\). It forms all homogeneous derivatives of orders less than the prescribed multiplicities (75 redundant rows), confirms interpolation-matrix rank 42 and kernel dimension 3, checks the 24-term integral octic in the kernel, computes exact tangent multiplicities and discriminants, and independently eliminates the entire affine singular locus by three rational resultants and gcds. At infinity the factored equation confirms only the two prescribed triple singularities.

A geometric-integrality witness for another parameter is provided by Malara, arXiv:2611.04564v1, Section 6.2, and is not purported to be checked by the script. The proof takes an intersection of two nonempty open conditions in the irreducible net bundle. This is a proof over complex general parameters, not a finite-field approximation or exhaustive parameter census.

The geometric genus follows for a general geometrically integral member from arithmetic genus 21 and the verified ordinary multiple-point total \(\delta=19\). It is not a claim about every member of the net or any special non-general parameter.
