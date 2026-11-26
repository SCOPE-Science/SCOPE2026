---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

For the smooth genus-three model y^3=f(x)=x^4+ax^2+bx+c, use the specified basis (dx/y^2, x dx/y^2, dx/y). The relative Cartier coefficient matrix H has a 2-by-2 block M from f^8 and a scalar d=[x^12]f^4. The fresh independent replay /workspace/replays/cartier.py verified in the full polynomial ring F_13[a,b,c] that d=6T, det M=4T Delta^2, and det H=11T^2 Delta^2, with T=a^2-8c and Delta the reduced quartic discriminant. On Delta != 0 and T=0, for c != 0 one can normalize c=1 geometrically: the bottom-left entry b(4-a^2) is nonzero for b != 0, and for b=0 the bottom-right entry is 2. When c=0, T=0 forces a=0 and smoothness forces b != 0; [x^11]f^8=8b^7 is then nonzero. Hence ranks are exactly 1 and 3 on and off T=0, and the divisor has multiplicity two with smooth reduced support. Independent gcd-based enumeration confirmed 1,884 ordinary, 144 with a-number 2, and 169 singular marked F_13 triples. Over F_169, at a^2=8,b=0,c=1, the replay gave Delta=9 and H=diag(0,2,0); 8 is nonsquare in F_13. This smooth example satisfies the stated nonzero-constant and characteristic hypotheses of Nourozi–Rahmati, Theorem 3.1(1), in both inspected preprint versions, and contradicts their conclusion. This is a first Cartier-rank calculation, not a Newton-polygon or geometric 13-rank determination. The polynomial identities and rank argument establish the geometric claim; the finite census does not substitute for them. Submitted verifiers were inspected, not run.

## originality

FAIL

The full varying-b stratification, not merely the bielliptic witness, follows mechanically from the prior Picard Cartier coefficient formula and the standard polarized de Rham identities. Complementary minors make the two partial determinants associates on the smooth coefficient ring and force equal nullities. The scalar 6(a^2-8c) then gives the entire rank stratification and the doubled divisor; grading and one evaluation fix even the full discriminant factor and constant. The remaining marked counts are elementary counts on that forced locus. This is an implication judgment, not a claim that a prior source prints the characteristic-13 table verbatim.

## value

FAIL

Checking a purported ordinarity theorem on a smooth curve is well motivated, and this independently verified counterexample is a useful correction note. But the known bielliptic coefficient already selects the witness, and the entire varying-b first-rank divisor and its multiplicity follow by split-character duality and the immediate scalar specialization. The displayed determinant constant is then a normalization, and the marked census is an elementary evaluation of the same criterion. The record supplies no nonmechanical remainder such as a finer Cartier-iterate or Newton stratification. Thus it does not meet the value bar for an independent finding as frozen. No repair was made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
