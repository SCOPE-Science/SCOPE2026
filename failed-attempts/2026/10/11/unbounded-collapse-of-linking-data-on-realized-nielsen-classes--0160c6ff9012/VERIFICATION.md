---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For n≥2 choose c=[x1,x2]∈F_n, and u_j=c^j for 1≤j≤m. Under the cited Makri Proposition 5.1 arbitrary finite Reidemeister coordinate lists are simultaneously realizable for a single homeomorphism with trivial loop braid. Abelianization kills all commutator powers, giving linking vector zero. Theorem 4.6 identifies Nielsen classes at loop braid 1 with ordinary conjugacy. Each c^j is cyclically reduced without cross-copy cancellation and has cyclically reduced length 4j, a conjugacy invariant; hence all constructed fixed points are in distinct Nielsen classes. This is an exact all-finite-m argument conditional on the published proposition as quoted in the frozen package, not extrapolation from m=2.

## originality

FAIL

Makri arXiv:2610.04382v1 already proves a simultaneous realization theorem for arbitrary finite lists of free-group coordinates (Proposition 5.1) and twisted-conjugacy characterization of Nielsen classes (Theorem 4.6), and then illustrates zero-linking noninjectivity in Remark 5.2/Example 5.3. Taking commutator powers c^j and observing their distinct cyclically reduced lengths is a routine free-group specialization, making arbitrary zero-linking fiber size a direct elementary corollary of the source results. The unbounded conclusion need not be stated verbatim to be covered as an immediate implication.

## value

PASS

The distinction between a two-point collision and arbitrarily large finite fibers is mathematically motivated: it quantifies a sharp structural limitation on what linking vectors can recover from realized Nielsen classes while carefully declining claims about essential classes or Nielsen numbers. This remains a meaningful fact, despite being so directly implied by a prior realization theorem that its independent originality fails.

The dated certificate retains the supplied scientific assessment, sources and limitations.
