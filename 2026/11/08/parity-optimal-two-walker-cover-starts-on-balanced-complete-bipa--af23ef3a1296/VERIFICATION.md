---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

PASS: Exact destination draws on each side of non-lazy K_(n,n) are iid uniform, so split/same CDFs at even N=2k are F(1,N)^2 and F(2,N)F(0,N); odd CDFs are F(1,N+1)^2 and F(2,N)F(0,N+2). In terms of surjection counts a_(N,j)=j!S(N,j), even difference is [a_(N,n-1)^2-a_(N,n-2)*a_(N,n)]/n^(2N). The sequence is strictly log-concave on positive support by a_(N+1,j)=j(a_(N,j)+a_(N,j-1)), and positivity begins exactly N>=n-1. First-draw identities show the odd difference is positive exactly N>=n-2. Same-vertex start is pathwise dominated by two distinct same-side seeds. Independently recomputed exact coupon recurrences for n=2..10, k=0..12 (234 comparisons) and the n=2 t=1,2 values; finite tests corroborate the self-contained all-n proof.

## originality

PASS

PASS only for the exact finite all-even deadline threshold: The November 2 full primary prior RESULT.md proves IDENTICAL coupon CDF formulas, sharp odd strict threshold, eventual even strict ordering, asymptotic crossing rates and no stochastically best initial placement. Those portions are NOT original. The frozen November 8 claim adds the all-N even log-concavity comparison and exact first feasible strict threshold N=n-1; the earlier complete proof only gave eventual strict even and did not state/derive all finite even strict inequalities. Resultary and primary random-walk comparisons did not produce an earlier exact finite even cutoff. Material risk: because the earlier paper already provides the exact CDF formulas, known log-concavity makes the remaining result an accessible strengthening; broad coverage may be found elsewhere.

## value

PASS

PASS narrowly: The newly sharp finite-time even deadline inequality completes a natural all-horizon initial-placement classification, closing the early-time uncertainty left by an otherwise closely related published theorem. Although mathematical ingredients are elementary, the exact strict cutoff for every n is a motivated, non-arbitrary optimal-start invariant (not merely repeating the already known no-dominance asymptotic). Mathematical value belongs to that finite sharp boundary ONLY.

The dated certificate retains the supplied scientific assessment, sources and limitations.
