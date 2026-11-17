---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For A=B^T B rank-two PSD, exact untruncated Nyström recovery iff the m projected independent sign columns B eps span R², using W(W^TW)^dag W^T projector identity. A single-sign image has zero mass z<=1/4 by two independent columns; each projective line L has total mass z+p_L<=1/2 by nontrivial linear-form anti-concentration. Set c=1/2-z, total nonzero masses=2c+z and each <=c, z<=c. Convex projective occupancy is bounded by masses (c,c,z), giving F_m<=2^(1-m)+(2^m-2)z^m<=3*2^(-m)-2*4^(-m). n=3 witness B=[[1,1,0],[1,0,1]] has z=p_1=p_2=p_3=1/4 and saturates, with zero padding for n>3; n=2 every invertible B sends four signs into two equiprobable projective lines, yielding 2^(1-m). Independent exact m=2,3,4 values 5/8,11/32,23/128 corroborate.

## originality

PASS

The November 2 published 2x3 Rademacher rangefinder orientation law explicitly attains precisely the same maximum 3*2^-m-2*4^-m for n=3. This is strongly credited, so the THREE-COORDINATE witness and sharp numeric sequence are NOT novel. The evaluated current theorem additionally proves the global upper bound for every higher ambient dimension n>=3 and every rank-two B by projective convex majorization; the published 2x3 classification has no statement or implication controlling arbitrary n>3. General random sketch/Nyström literature gives subGaussian sample complexity but not this sharp dimension-free exact constant. O PASS best of knowledge for the all-n extension, not the n3 case; residual possibility of known general anti-concentration implication.

## value

PASS

Natural exact-recovery failure law for randomized linear algebra: rigorously shows a universal ambient-dimension plateau in rank-two discrete sketches, with n2 versus all n>=3 distinction. Establishing that no higher ambient dimension worsens failure is an independently useful sharp minimax fact, not merely restating a small-n witness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
