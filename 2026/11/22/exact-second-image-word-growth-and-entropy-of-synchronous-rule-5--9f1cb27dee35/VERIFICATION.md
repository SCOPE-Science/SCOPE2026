---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Compose the radius-one synchronous rule twice. A path through overlapping four-bit contexts supplies precisely an input block of length n+4; every such block extends bilaterally. A label word is accepted precisely when its subset of terminal contexts is nonempty. Deterministic transitions then count each spatial word once, with c_0=1. The independent replay /workspace/replay/rule54.py constructs the local rule and subsets, minimizes by partition refinement rather than using the published table, and obtains 39 reachable subsets and 18 quotient states including the sink. The accepted transfer matrix and its characteristic polynomial determine the entire rational series by Cayley–Hamilton and the initial coefficients; exact reduction gives both frozen polynomials and the stated first 16 terms. Separate two-pass input enumeration agrees for lengths 1–9. The 16 internal states form one strongly connected component with a loop; the initial state enters it, and rejecting edges do not contribute. Its characteristic polynomial is tP(t). Rational Collatz–Wielandt comparisons with K^80 1 give the stated interval; the independent approximation lambda=1.8276841668945112 gives log(lambda)=0.6030496828827792. Perron–Frobenius growth gives the shift entropy via the subshift block-count limit. This is an all-length certificate for two updates only, not a ring, trajectory, or eventual-image calculation.

## originality

PASS

The graph construction and even its use for all elementary rules at the second iterate are antecedent. The distinct result is the complete Rule 54 second-image word-growth series and its exact spatial entropy, established by additional state closure, minimization and exact matrix calculation. Prior short-witness and one-step results do not supply these invariants. Plausible inaccessible process-graph text leaves a concrete priority risk.

## value

PASS

Rule 54's finite-time image filtration has spatial complexity not captured by the first forbidden block or by ring preimage counts. The rational series gives all distinct block counts without re-enumeration and fixes the entropy as an algebraic growth constant for the complete second image. This is a natural invariant of a standard automaton even though its method is classical and later images remain open here.

The dated certificate retains the supplied scientific assessment, sources and limitations.
