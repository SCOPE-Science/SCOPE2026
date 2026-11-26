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

The first 2h letters of a nonunary h-periodic run contain exactly two copies of one marker: zero markers would make the run unary by periodicity, and four exceed the weight. Thus the period is one of the adjacent distances, and a three-marker run requires equal gaps. A fixed pair and period determine at most one maximal interval. Equal gaps or a unit gap have exponent sums strictly below the candidate for n>=13. For distinct gaps 2<=p<q, the potential run intervals are contained in [max(0,x-p+1),x+2p) and [x+1,min(n,x+p+2q)); the upper bounds are positive even when the corresponding run is absent. Ignoring endpoint losses yields the first bound in (1); charging combined loss at least (2p+2q-1-n)_+/q yields the second. For p<=m the first bound is optimized by q=p+1 and then p=m. For p>=m+1, the second decreases with p after setting q=p+1; n<=4m+4 and m>=3 give the stated comparison. The witness contributes n-3 from the four zero runs plus the stated maximal intervals [0,3m-1) and [m,4m+1), with least periods m and m+1. At n=12 the same bounds give at most 83/6 for p<=2 and at most 9+g(3)=167/12 for p>=3; the equal/unit-gap cases are below 167/12. Markers (2,5,9) attain 9+8/3+9/4. A separate longest-border maximality enumerator checks 2,380 weight-three words at lengths 3..16, confirming the n=12 exception and the n=13..16 formula and witness. This finite replay is supplementary to the analytic proof.

## originality

PASS

Credit the earlier weight-three run-spectrum proof for the restriction to adjacent-gap periods, which this record re-derives. The supported distinct claim is the exact optimization of the sum of lengths divided by least periods, including the sharp threshold and explicit attaining word. None of the compared statements yields that optimization.

## value

PASS

The sum of run exponents is a standard invariant distinct from run count. Weight three is the first sparse composition permitting two unequal nonunary periods. Balancing both periods and boundary losses yields a sharp length-dependent correction, a verified sharp onset, and a uniform attaining family. This is a concrete benchmark unavailable from unrestricted bounds or the known count distribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
