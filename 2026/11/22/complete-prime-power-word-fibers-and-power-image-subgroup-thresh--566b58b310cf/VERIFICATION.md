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

Model the regular module as F_q[u]/(u^n), with T=1+u. The base part of the p^b-power is multiplication by ((1+u)^i-1)^(p^b-1), using the geometric-sum identity in characteristic p. For i nonzero the factor in parentheses has valuation p^v_p(i) and unit leading coefficient, so the image is the corresponding principal ideal and kernel size is q to that valuation, capped at n. For admissible nonzero j, each of the p^b top preimages of j has valuation v_p(j)-b; for zero j, p^b-p^(b-1) preimages have valuation a-b and the remaining p^(b-1) base maps vanish. This derives all three fiber rules and their supports. The top-zero and top-p^b supports for b<a have ratio q^((p^b-1)(p^(a-b)-1)) taking the latter over the former, which is impossible for subgroup cosets. At b=a the support is the fixed line, attained nontrivially by a single-coordinate vector with i=1. At b>a all power maps vanish. Dividing the image formula by the group order and setting t=s-b gives truncations of the stated positive convergent series plus a vanishing zero-top term. A separate coordinate enumeration checked every target at depths 1 through a+1 for (p,q,a)=(2,2,3),(2,4,2),(3,9,1),(3,3,2),(5,5,1). It summed the shifted coordinate vectors directly and built the claimed ideals by repeated shift differences. Image sizes in the first case were 336,36,2,1; in the fourth were 4401,3,1.

## originality

PASS

Credit the Hall power formula and regular-module structure, the known C_p wr C_p order/identity-fiber case, and the established study of power membership and proportions for symmetric wreath products. The inspected results do not establish a uniform target-by-target cyclic-top classification with its exact non-subgroup interval and fixed-depth density series. The credited scope is this combined theorem, not the norm formula or central terminal image in isolation.

## value

PASS

The classification addresses a canonical power word on a natural family, gives target counts rather than just an identity fiber or membership criterion, and answers the consequential question of when the image stops failing closure. The positive fixed-depth density is an exact population statistic across the family, not an isolated small calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
