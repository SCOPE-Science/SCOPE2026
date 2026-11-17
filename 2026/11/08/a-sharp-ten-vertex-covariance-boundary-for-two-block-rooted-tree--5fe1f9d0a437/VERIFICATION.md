---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Directly derived D=d(P)+1 and L=2ell-1_{P leaf}, hence Cov=(ell U-iQ)/t^2. The internal vertices are ancestor-closed, so U<=i(i-1)/2, equality only on an internal path. Each of the i-1 internal edges has a descendant leaf, hence Q>=ell+i-1; simultaneous equality forces one terminal leaf and all remaining leaves at root (including star i=1). The polynomial identity (t-i)(i-3)-2(i-1)=(t-9)(i-3)-(i-5)^2 gives sign cutoff and unique n=9,10 maximizers. Uniform cubic limit yields 2/27 at i/t=2/3. Inspected all proof and checker.py at pinned Git tree; an independently written rational rooted-tree enumeration reproduced sharp values through n=11 (n=9 0; n=10 numerator 6; n=11 numerator 15). Finite tests corroborate but are not needed for the all-order proof.

## originality

PASS

No identified prior implies the combined two-copy, uniform-parent covariance maximum, sharp nine/ten-vertex sign cutoff and equality shapes; original block work provides model and marginal updates but not this joint sharp result.

## value

PASS

A natural stochastic mixed observable of block-tree growth admits a genuinely sharp sign transition, exact shape classification, and asymptotic envelope. The joint covariance is not a mere recitation of leaf/depth marginals, and the t=9 and t=10 boundaries answer an interpretable structural extremal question.

The dated certificate retains the supplied scientific assessment, sources and limitations.
