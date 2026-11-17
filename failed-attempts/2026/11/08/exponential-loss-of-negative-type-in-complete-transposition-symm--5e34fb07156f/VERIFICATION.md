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

The group-invariant kernel d(g,h)=n−c(g⁻¹h) diagonalizes in nontrivial S_n Specht sectors. The classical Jucys–Murphy content product for shape (n−2,1,1) is H_n(e^{−t})=(1−e^{−t})(1−2e^{−t})∏_{j=1}^{n−3}(1+j e^{−t}); the fractional-power Laplace transform has a sign reversal at log2. Comparing a fixed negative interval [u,v]⊂(0,log2) with the positive tail yields the stated C(u,v)ρ_v^(n−3) upper bound and limsup≤3/4. Exact S3,S4,S5 character tables give the stated critical equations and endpoint ranks 4,14,118; checked the three numerical roots directly. This proves only an *upper* asymptotic rate, not sharpness. Finite row checks do not prove the all-n hook estimate.

## originality

FAIL

FAIL for principal infinite finding: a published **November 2, 2026** source already diagonalizes exactly the SAME complete-transposition Cayley kernel, isolates the SAME hook (n−2,1,1) content polynomial, and proves a far STRONGER β_n<100/(n−3)! for all n≥53, with strict descending obstructions and sharp S6 threshold/nullity. The new 3/4 exponential limsup follows immediately from its factorial bound. Submitted small groups n=3,4,5 fill elementary finite character-table cases obtained by exactly the same classical Jucys formula, not a distinct structural theorem or substantive extension when the difficult all-n part is already dominated. The finite-n roots can be checked but do not rescue the covered core.

## value

FAIL

FAIL as independently valuable final claim: the strongly dominated exponential bound is superseded by the earlier factorial decay, while the initial three low-rank tables and embedding ranks are straightforward character calculations using the prior complete polynomial machinery. No substantively motivated unknown new classification or boundary survives, unlike the prior sharp S6 case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
