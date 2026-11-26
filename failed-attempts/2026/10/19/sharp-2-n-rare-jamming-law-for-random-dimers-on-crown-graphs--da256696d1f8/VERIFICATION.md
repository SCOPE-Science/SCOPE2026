---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

FAIL

RESULT.md lines 4, 19, and 22 assume merely independent continuous priorities but use uniform order. On the n=3 crown graph give a1b2 and a2b1 independent Uniform(0,1) priorities and the other four independent Uniform(2,3) priorities. Both early edges are necessarily accepted, and a3,b3 are left unmatched, so P3=1>1/2. The vacancy dichotomy is valid regardless of order. Under a uniform order (e.g. i.i.d. continuous priorities), the eligible relative order remains uniform conditional on the accepted history: reveal its first edge, then restrict the uniform remaining order to the surviving subset. The overlap transition, first-moment drift and second factorial-moment bound then prove the stated inequality. A specified derangement on n−1 labels gives positive failure probability for n≥3, while both crown edges are forced for n=2. Independent finite checks give 240 failures among 720 orders for n=3 and P4=4/21 by exact vertex-subset recursion. Read the supplied checker and verification notes without executing source code. Narrowing the law would fix correctness but would not leave an original valuable result.

## originality

FAIL

The substantive uniform-order law and exact recurrence are covered in distinct catalogue records; even the specific harmonic lower bound is a direct bound on their identical exact stage drift/survival formulas. The literal nonexchangeable scope is false and contributes no extension. Coverage is not a finding of historical priority or of shared provenance.

## value

FAIL

The factor-two rare-failure rate on the dense crown is a meaningful question. However, narrowing the invalid priority scope leaves a covered law. Replacing the survival estimate by its immediate tighter value at t=2 does not establish a new phenomenon, sharper asymptotic order, or new quantitative threshold with independent scientific use.

The dated certificate retains the supplied scientific assessment, sources and limitations.
