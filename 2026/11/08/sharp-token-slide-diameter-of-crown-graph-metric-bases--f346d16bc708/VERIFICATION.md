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

For the connected crown H_n n>=3, ordinary graph distances distinguish same-index endpoint by 3, same-side distinct indices by 2, and opposite-side unmatched by 1. Every resolving set meets at least n-1 pairs; exactly one-hole transversals of n-1 matched pairs form all metric bases. Legal slides swap the hole with an occupied index and flip the selected side at the old hole. Thus there are n·2^(n-1) states, degree n-1. An induction freezing a shared token, plus explicit n+3-step same-hole complement route and n+2-step no-common unequal-hole route, prove all-pairs upper bound n+3; to reverse all n-1 signs and restore the same hole requires at least two reverse-color slides, giving matching lower bound. Independently constructed the entire vacancy-side graph and performed BFS from every state for n=3..7, giving diameters 6,7,8,9,10, including the C12 base case. The source artifacts/verify_state.py paths were inspected; finite BFS corroborates, not proves, all n.

## originality

PASS

The full vertex-metric basis set and n·2^(n-1) count were established earlier and are not claimed as novel. The specific legal-slide graph and exact unbounded diameter n+3 are not consequences of that state count or the different minimum closed-neighborhood identifying-code slide graph. An inaccessible 2026 metric-basis reconfiguration thesis presents a real residual risk but no inspected theorem contradicts priority; best-of-knowledge PASS limited to diameter/routes.

## value

PASS

The diameter of the natural reconfiguration graph of all optimal resolving landmark placements is a structural invariant useful for routing optimal configurations, and n+3 is a nontrivial sharp overhead beyond Hamming/one-token exchange counts. The all-parameter classification and explicit shortest worst-case obstruction constitute a motivated exact result, not a mere basis-count recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
