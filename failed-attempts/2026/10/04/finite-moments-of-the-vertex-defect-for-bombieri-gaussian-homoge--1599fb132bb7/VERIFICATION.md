---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

Given the quantitative ingredients cited from Pinasco-Zalduendo, the upgrade is correct. On the event \(M(Q_n)\ge a_m n^{(m+1)/2}\), the deterministic defect bound reduces \(Z_n^q\) to \(M(R_n)^q n^{-q(m+1)/2}\). The cited Gaussian union-bound tails for each r-variable block integrate to fixed-q norms \(O(n^{(r+1)/2})\); finitely many blocks give \(\|M(R_n)\|_q=O(n^{m/2})\). The bad denominator event is exponentially small and \(0\le Z_n\le1\). Thus the q-th moment is \(O(n^{-q/2})\).

## originality

PASS

Best-of-knowledge originality is retained because the accessible primary abstract states only an \(O_{\mathbb P}(n^{-1/2})\) defect theorem, not finite-moment or expectation bounds, and Resultary's only exact hit is this submitted record. Full-text inaccessibility prevents a whole-document noncoverage claim; it is explicitly retained as residual risk.

## value

FAIL

The finite-moment statement is useful, but the mathematical increment is routine once the cited source tails are available: integrate a standard sub-Gaussian finite-maximum bound, apply Minkowski across finitely many blocks, and split on the source's exponentially likely denominator event. Under the common value bar this is a standard probabilistic cleanup of existing quantitative estimates rather than a new structural lemma, boundary, classification, or independently motivated invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
