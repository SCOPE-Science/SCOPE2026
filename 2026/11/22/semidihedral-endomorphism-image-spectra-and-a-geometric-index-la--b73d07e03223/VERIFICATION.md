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

In normal form, (r^i s)^2=r^{hi}. If x=F(r)=r^i and y=F(s) is central then (h-2)i=0 modulo m, leaving four pairs. If x is a rotation and y is an outside involution, all m choices of i work for each of the m/2 possible y, and for nonzero i the image has size 2m/gcd(i,m); the order-four case is V4, and the larger proper images are dihedral since h acts trivially on their rotation subgroups. If x=r^i s with i odd, a central y cannot invert x, and an outside involution y=r^{2j}s would require 4j+2(h-1)i=0 modulo m, impossible modulo 4. For i even the involutions commuting with x are 1, r^h, x, xr^h, giving two C2 and two V4 maps per x. This exhausts and yields every coefficient, including n=4. For idempotence, any nontrivial x=c=r^h or any image containing c with F(c)=1 is excluded. A cyclic x with outside y must satisfy i^2=i modulo m, hence i=0 or 1; i=1 forces y=s. Outside x=r^{2j}s not killed by idempotence must have y=x, since with y=1 it maps to 1. The two proper families (1,t) and (t,t) have different kernel intersections with the characteristic rotation subgroup, and conjugation by r↦r, s↦r^{2w}s is transitive inside each. For the comparison families of the same order: dihedral has 2m proper projections onto reflections (two C2 characters per reflection; no other proper retract by the same rotation/idempotence test). In the quaternion presentation y^2=x^h, odd rotation x forces a surjective map, outside x is impossible since y would be central and unable to invert x, and even rotation x gives image within the central C2 which is killed by F; no proper nontrivial retract. For the index limit, the cyclic-x/outside-y block has weight (m^2/2)/(m^2/2+2m+4); its index exponent is the valuation of uniform i modulo m capped at n−1 (assign that cap to i=0). The geometric law 2^{-v-1} on v≥0 differs from this capped law in total variation by 2^{-n}. The discarded weight is O(1/m), proving total-variation convergence. The all-order derivation, not the finite recorded checker output, establishes the result.

## originality

PASS

Best-of-knowledge pass for the full rank/type census and retraction geometry, together with their index-law consequence. The group action and its structural classification are prior. A prior complete family-wide generator-image census with image data would cover the polynomial and, if it gave the action/composition data, make the further deductions largely mechanical. No such census was established in inspected prior statements. In particular, the inaccessible 2002 paper covering the relevant class leaves significant priority risk, not a negative finding about its contents.

## value

PASS

Image sizes and retracts are natural map invariants of a standard maximal-class family. The sharp absence of nontrivial retracts larger than C2, despite proper dihedral images at every nonabelian intermediate order and plentiful V4 images, is a useful distinction; the two transitive families are organized by different kernel intersections, not just a total count. The full spectrum quantifies how many maps realize each structure and directly supports the limiting index statistic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
