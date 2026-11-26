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

Independent proof check: for ranks r,s a product has rank s−dim(im(right)∩ker(left)); subspaces of the prescribed dimensions realize every intersection size between max(0,s−r) and min(s,n−r), and left/right changes of basis realize the entire resulting rank classes. The units do not add conditions: |GL_n(K)|>2 even for n=2 over F₂, so each unit factors into two nonidentity units, and multiplying rank strata by any one unit preserves them bijectively. If a rank block B skips a rank k of C, take a=min B<k<b=max B. The product contains ranks a and k by using factor ranks (a,k) and (b,k). Saturation forces both b and max C into the product; the ranks are bounded above by min(b,max C), giving the impossible b=max C. For interval blocks [a,b],[u,v], any k between max(0,a+u−n) and min(b,v) occurs using max(a,k),max(u,k); both rank constraints follow directly. The right bound is already a block endpoint, so precisely the left bounds must be starts, yielding truncated-addition closure. Reflection around n converts that closure to addition below n, with all sums ≥n included and 0 adjoined. E₁₁ and E₁₂ lie in the same rank-one class but only E₁₁ is idempotent, precluding automorphism orbits. New bounded enumeration of endpoint sets and independent truncated semigroup sets reproduced 2,3,5,7,12,16,27,37 for n=2,…,9: python3 /workspace/branches/8735b8bd-3782-4f71-ad4b-8586d3962602/independent_counts.py. Frozen VERIFICATION.md and checker inspected, not executed. The proof, not the enumeration, covers all fields and n.

## originality

PASS

Credit the standard rank-product operation, Jenča's saturation criterion, the numerical-semigroup notion and the already indexed count sequence. The distinct supported claim is the exact field-uniform classification for this matrix rank-block family and the canonical identification with semigroups. No inspected prior statement covers it.

## value

PASS

The rank-block family is a natural structured quotient test for a standard monoid. The result gives a necessary-and-sufficient answer for all fields, reduces its classification to the classical numerical-semigroup object, and distinguishes it from automorphism orbit partitions. Value lies in the structural bijection, not the already known finite sequence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
