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

From exchangeability without replacement E R=k(n-k)/(n-1); marking a 0,1^ell,0 pattern yields ES_ell=n(k)_ell(n-k)_2/(n)_(ell+2), and conditional R mean 1+(k-ell)(n-k-1)/(n-ell-2) for n>=ell+3. Cov=ES_ell(E[R|mark]-ER) factors into stated exact affine numerator B=(ell+1)k-(ell-1)n-2, strictly decreasing with ell. Exceptional n=ell+2,k=ell computed separately, k=n-1 or ell>k yield zero. Independent exhaustive rational enumeration of labeled fixed-weight words n=3..11 verifies the formula and degenerate boundaries; the proof establishes all integer sizes.

## originality

PASS

Qualified best-knowledge PASS for the **sign theorem**, not invention of circular-run mixed moments. Inoue–Aki 2005 provides general circular joint generating functions; coefficient extraction may supply the covariance, but the global fixed-composition sign classification, unique zero criterion and all-boundary factored form require a new nontrivial evaluation not present in inspected theorem statements. 2010 same-parameter paper inaccessible; its coverage remains material priority risk.

## value

PASS

PASS: The conditional fixed-content runs null is a natural benchmark for runs tests; one-switch sign boundary and density phase line describe when total segmentation becomes positively vs negatively associated with counts of long exact runs. This is a meaningful dependence classification beyond unevaluated joint-PGF generality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
