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

For each target, killed matrices A,B of the two lazy Metropolis kernels satisfy a=1+Ab, b=1+Ba, equivalently (I-AB)a=1+A1. Connectedness and self-loops >=1/2 ensure absorption and invertibility. Frozen witness C4/paw has rational phase hitting vector (5538,3876,4236)/607 and static vectors (8,6,6) and (15,6,9); start 1 target 3 yields (3876/607)/6=646/607. The complete finite census enumerates every connected labeled graph n=2,3,4 (1,4,38), each unordered pair, all starts, targets and two phases: 4,120,17784 tests, best ratios 1,1,646/607; 168 four-state strict slowdowns and 24 extremal phase cases. I independently reimplemented exact rational killed-matrix elimination and reran this entire finite census. This is exhaustive for n<=4 and does not assert any n>4 case.

## originality

PASS

Best-of-knowledge originality: established general criteria and overlapping special cases are explicitly credited. Fresh exact finite/arithmetic or spectral classification not mathematically implied by inspected broader statements. Inaccessible plausible primary sources are retained as risks, not falsely described as read.

## value

PASS

A natural minimal-counterexample classification for two connected lazy reversible graph walks with identical stationary measure. Even though each fixed walk is well behaved, switching strictly worsens same-pair hitting, and four vertices are proved minimal with an exact 6.43-percent sharp inflation ratio. The complete finite enumeration and explicit witness are independent useful sharp facts, not an arbitrary slice of an unrelated statistic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
