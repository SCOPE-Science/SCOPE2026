---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-19.md",
      "INDEPENDENT_AUDIT_2026-11-19.json"
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

For each peripheral edge the update f_h sends (h,h) to (1-h,1-h) and fixes the other three ordered states, hence f_h is idempotent. Fixed states forbid exactly the (h,h) edge and the hub sees at least m opposite neighbors, yielding F_m=2*3^m. For a primitive period-two state, a constant hub would force idempotent edges and a globally fixed state. Thus the hub alternates; composing f_1 f_0 shows that, for phase h=0, only (0,0),(0,1),(1,0) return, and at least one (0,0) is necessary and sufficient for strict hub switching on both phases. Hence precisely 3^m-2^m possible phase-zero edge assignments, 2(3^m-2^m) initial primitive states, and 3^m-2^m temporal 2-orbits. All m>=1 and all labelled edge orientations are covered; at m=1 the graph K_3 gives (F,P)=(6,2). A separately implemented graph-neighbor update exhaustively checked all 2^(2m+1) states for m=1..7.

## originality

PASS

Best-of-knowledge PASS for the combined family-specific exact classification, particularly P_m=2(3^m-2^m) and hub-flipping necessary/sufficient conditions. Credited prior same-graph asynchronous minority 2*3^m count: a coincident fixed-state cardinality is partially covered and not treated as priority for that number alone. The full examined relevant theoretical and recorded graph results do not logically imply the synchronous primitive two-orbit census. Historical risk is explicit.

## value

PASS

The friendship graph is a standard natural nonbipartite graph family and its initial recurrent states are natural invariants of antiferromagnetic best-response dynamics. The formula classifies every fixed state and every immediate period-two orbit for all m and explains the nontrivial hub-coupled oscillation mechanism: exactly one or more hub-matching monochromatic peripheral edges, with all other edges mixed. The 3^m-2^m full orbit count is not supplied by earlier general period-two theory or the separate asynchronous minimum-energy class, and can serve as an exact benchmark for more general stabilization and basin analyses. No broader family theorem or downstream application is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
