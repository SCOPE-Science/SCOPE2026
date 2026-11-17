---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-08.md",
      "INDEPENDENT_AUDIT_2026-11-08.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Any real projection onto specified V has form UF with FU=I. Frozen exact U,F_star give FU=I and all five absolute row sums 845/659. For perturbations H with HU=0, seven signed supporting row-sum forms L_i satisfy positive barycentric identity sum_i c_i L_i=0 and injective map of six-dimensional tangent onto that hyperplane (rank 10 after four constraints). Thus g=max L_i is positive and g<=1 is a seven-vertex simplex. Independently recreated rational system in SymPy using P_star signs: all seven vertices nondegenerate, their ||U H_i|| are 1013/104, 493257/1508, 9739/572, 2909/104, 2909/104, 493257/1508, 9739/572; max K yields global strong uniqueness modulus 1508/493257. Exact t=1/100000 perturbation at extremal vertex gives equality, so constant is sharp. This is a finite exact certificate combined with universal convexity, not sampling.

## originality

PASS

Earlier November 8 published result computes exact least norm 845/659 for the identical plane and extensions; no stability, uniqueness, or sharp six-dimensional tangent modulus is asserted there. Deregowska-Lewandowska 2014 full paper gives sharp strong uniqueness in restricted ker(f) coordinate-truncation generalized-projection families and a general criterion, not this specific codimension-three two-plane. No direct implication of 1508/493257 from the earlier 845/659 norm alone.

## value

PASS

A sharp error-bound for a natural explicit extremal plane upgrades the previously known projection constant to a quantitative stability and uniqueness statement, with an extremely small modulus revealing ill-conditioning. This is a motivated exact invariant of the optimizer, not an arbitrary small-coordinate calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
