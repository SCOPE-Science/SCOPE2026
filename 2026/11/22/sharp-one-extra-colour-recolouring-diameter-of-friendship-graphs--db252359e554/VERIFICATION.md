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

With three named colours every triangle is frozen and each fixed-hub petal has two states. With four named colours the ordered pairs in a fixed-hub petal form a C6, so the fixed-hub graph is its t-fold Cartesian product. Each of the six unordered hub-colour pairs contributes 2^t edges, and every enabled state has exactly one hub move. This gives 4·6^t states, 4t·6^t+6·2^t edges and 12·2^t hub-enabled states. For two distinct hub colours, the two common ordered pairs are antipodal in each local C6, so the costs via the two gateways add to six, and each petal can independently choose a cost at most three. A path with one hub move then gives 3t+1, while equal hub colours cost at most 3t. Exchanging both endpoint colours in each petal takes at least three moves per petal even if the hub moves, and the witness also has distinct hub colours. This proves the exact diameter, including t=1, without requiring the finite checks. The supplied script was inspected, not executed; its t=1 through 5 output is recorded evidence only.

## originality

PASS

The verified general OAT result covers connectivity, not this sharp distance. No inspected available claim matches or implies the all-t exact diameter on the friendship graph under the same palette and move rule. The size and hub counts are supporting facts, not the basis of the originality decision.

## value

PASS

The family has an unbounded number of interacting petals at the minimum palette permitting moves. The invariant distinguishes frozen three-colour states from a connected four-colour space and quantifies its worst-case distance exactly. Counting hub-change gateways and proving that one hub move suffices for the sharp bound explain why a general connectivity result does not give the answer. This is a useful benchmark for sharp recolouring bounds on clique attachments.

The dated certificate retains the supplied scientific assessment, sources and limitations.
