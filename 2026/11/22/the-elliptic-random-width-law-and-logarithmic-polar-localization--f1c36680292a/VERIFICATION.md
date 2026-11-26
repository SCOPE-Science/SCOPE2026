---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Checked the actual equal-radius orthogonal intersection and Haar-width claim. At fixed y the section is a square, giving support r sqrt(u_y^2+(|u_x|+|u_z|)^2), hence W=2r sqrt(1+S), S=2|U_x U_z|. Independently, rotation by pi/4 gives S=|P-Q| where (P,Q,1-P-Q) has Dirichlet(1/2,1/2,1/2) law. Its folded difference density is (1/pi) times the integral of [v(v+s)(1-s-2v)]^(-1/2) for 0<v<(1-s)/2. Substitution v=(1-s)sin^2(theta)/2 gives the displayed K with modulus sqrt((1-s)/(1+s)); the width Jacobian cancels sqrt(1+s). The elliptic endpoint expansion gives f_S(s)=log(8/s)/pi+O(s log(1/s)), and s=delta/r+delta^2/(4r^2) yields the stated full lower-tail constant and error. The density is smooth up to the other endpoint with limit 1/r; neither endpoint has atoms. Independent latitude/azimuth gives E S=(2/3)(2/pi). For 0<a<b<1, integrate the disk density over s^b<|x|<s^a and |z|<s/(2|x|): it is uniformly (1+o(1))/(2pi) there and the mass is (b-a)s log(1/s)/pi. Dividing by the full tail and exhausting interior intervals proves the conditional law and forces both |x| and |z| to zero in probability. Reflection gives the fair independent sign exactly for every positive threshold. Read the checker and notes without execution; the checker is a finite numerical diagnostic, not a proof of the limit.

## originality

PASS

The compound theorem adds the marked conditional localization for this bicylinder; the scalar elliptic distribution is already an exact specialization of published real numerical-shadow results, and its scalar tails and moment are not independent novelty. The marked log scale and resulting selection of the two crossings are not supplied by that scalar marginal, or by the inspected width results. No ordering is inferred from same-day catalogue dates.

## value

PASS

The mark distinguishes which parts of a nonisolated extremizing set receive the rare directions: the crossings attract all the mass, with no single algebraic approach scale. This is useful information beyond the known marginal density and unlike either a smooth isolated extremum or the strictly unequal bicylinder. The full constant gives the normalization linking that mark to the actual caliper excess.

The dated certificate retains the supplied scientific assessment, sources and limitations.
