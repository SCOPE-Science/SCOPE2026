---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The endpoint indicators and overlapping adjacent indicator products count exactly the legal swaps; different swap positions produce different words. With the initial two distinct colors fixed, a distance-two inequality bit allows q−2 extensions and an equality bit allows one. This gives independent Bernoulli indicators under the uniform word measure, and the two-state weighted transfer with endpoint factors yields the stated rational series (including the separate n=2 term). Zero degree forces zero endpoints and an independent set of interior ones, giving the recurrence; full degree forces every indicator to be one. The two endpoints collapse to the same bit at n=3, as reflected in the variance. At n≥4 the only nonzero cross terms are neighboring products and the two endpoint/product covariances. The interior sum is bounded and 1-dependent; the stated separated blocks have total variance asymptotic to n times the positive variance density, negligible omitted centered variance, and third-moment bound O(n^(7/5)), sufficient for the CLT. An independent direct-swap script matched all histogram coefficients and exact rational moments for 18 strata (2≤q≤4, 2≤n≤7); the proof, not the script, covers all parameters. Replay: python3 /workspace/audit_replay/path_degree.py.

## originality

FAIL

A distinct indexed result directly states the substantive degree-spectrum theorem, frozen and full-degree counts, and finite moments on the common nondegenerate range. Both entries are dated the same day; the evidence establishes equivalent coverage, not publication order. The extra q=2 and n=2 cases are immediate degeneracies. The Gaussian limit is not directly stated in that entry, but follows using the standard bounded 1-dependent CLT on its expressly identified independent bits and the same adjacent-product formula. The frozen combined finding does not establish a distinct substantive theorem apart from that coverage.

## value

FAIL

An unknown exact degree spectrum for this move graph would be useful for local branching and frozen-state counts, but the precise spectrum and those consequences are already supplied for the substantive range. The distinct additions in the frozen finding are two trivial regimes and a standard 1-dependent normal approximation from the existing exact representation. No separate meaningful invariant or new asymptotic regime beyond that routine implication is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
