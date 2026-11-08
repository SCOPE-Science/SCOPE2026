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

# Reproducible checks and limits

The included `verify_cayley.py` is a standalone Python 3 program using NumPy and SciPy. Running `python verify_cayley.py` is sufficient. Its independently assembled linear programs optimize the radius in the original polytope's exact halfspace geometry: the decision variables are the fiber coordinates, base coordinates and radius. They are not fitted to the proposed explicit center box. For 1,120 random nonnegative matrices with \(1\le d,m\le4\), the LP optimum matched the saturation/no-saturation criterion. For the sparse two-parameter family, the radical identity, strict positivity exception and center-interval length were additionally checked through dimension \(31\), with each of \(\alpha,\beta\) between \(1\) and \(11\). The script printed:

`PASS: 1120 independent LPs, 19865 assertions; sparse parameter formula checked through d=31.`

Floating-point linear programming is not an exact algebraic certificate. The unrestricted proof is provided in RESULT.md and uses only projection of balls, normal lengths of explicit halfspaces, and a rationalized square-difference identity. Numerical tests cannot settle historical originality or the inradius when the sharp projection criterion fails. Independent mathematical validation has not been performed.
