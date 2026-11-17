---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

For a uniform permutation of [n], n>=4, with B_i=1{Π(i+1)=Π(i)+1} and C_j cycles of the same permutation, the claimed global covariance (2t-t²-t^(n-1))/[n(n-1)]+t^n/n² and the positionwise formula are correct. The two prescribed arrows Π(i)=a,Π(i+1)=a+1 are classified into two fixed loops, a length-two path, or two disjoint length-one paths. Contraction yields a uniform permutation on n-2 vertices; expectations of marked cycles give exactly the stated four support values. Independent rational complete enumeration n=4,5,6 reproduces the global covariance vectors and n=4,5 local formulas. The zeros in interior lengths express uncorrelatedness, not independence. Crucially, the 2026-10-27 prior theorem gives the same proof and all formulas.

## originality

FAIL

FAIL decisively: the complete published 2026-10-27 theorem 'Cycle-length orthogonality of ordinary successions in a uniform permutation' has the identical original-permutation B_i and C_j definition, the exact identical global four-support formula for all n>=2, and identical full positionwise formula for n>=5. Its p_i=1 at endpoints and 2 internally is exactly submitted c_i. The submitted n=4 local boundary case is a direct application of the earlier published contraction table and not a substantive original remainder. The earlier complete RESULT.md proof was inspected: its L/P/D forced-arrow contraction and cycle-marking calculation are the submitted method. Hence the final claim is already implied and cannot be accepted on originality even though correct and valuable.

## value

PASS

The exact interaction of one-line succession positions and original-permutation cycle-length counts is a natural second-moment refinement of the Diaconis–Evans–Graham marginal identity. Interior-length cancellation and boundary effects are scientifically meaningful, despite being entirely covered by the earlier complete theorem. Value does not rescue a covered claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
