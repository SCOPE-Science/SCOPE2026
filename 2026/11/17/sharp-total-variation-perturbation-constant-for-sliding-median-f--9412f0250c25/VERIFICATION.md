---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

Median monotonicity and translation equivariance bound output difference delta_i between min and max input perturbation in its local window. Adjacent windows lie in one 2r+2-point interval, hence |delta_(i+1)-delta_i| <= sum of the 2r+1 variations of the perturbation across its edges; each edge is charged exactly 2r+1 times. For attainment, explicit interleaving of ordered labels L_1..L_r,R_1,L_(r+1),...,R_r,L_2r,R_(r+1)..R_2r yields alternating selected sides across 2r boundary centers. Place this rank gadget and its reflection at two separated interfaces of an n-cycle with n>=8r, and let g=f+epsilon*1_(0<=i<4r) for epsilon in (0,1). The input variation is 2epsilon; output variation is 2(2r+1)epsilon; equality is attained. Independent integer sorted-median implementations reproduced exact factors 3,5,7,11 for r=1,2,3,5 at n=8r and 8r+3. Finite checks only test rank witness; combinatorial proof handles all radii.

## originality

PASS

Previously published cyclic three-point theorem covers the r=1 subfamily (indeed n>=6), and a separate five-point theorem extends r=2 to all n>=10. Those cases must not be claimed as new. The present all-radius cyclic family includes every r>=3; published all-radius result on clamped finite paths uses different boundary and noncyclic seminorm. No published stronger theorem was identified that directly establishes the periodic all-r statement. Originality of the broader-radius cyclic formula is best-of-knowledge with genuine priority risks.

## value

PASS

Sharp two-input variation stability of a classical running median is a natural filter robustness invariant; its linear growth in window radius contrasts sharply with the one-input variation-diminishing property. A uniform construction across unbounded radius on periodic data yields a useful worst-case stability benchmark; the known r<=2 subfamilies are credited and the new content is all r>=3.

The dated certificate retains the supplied scientific assessment, sources and limitations.
