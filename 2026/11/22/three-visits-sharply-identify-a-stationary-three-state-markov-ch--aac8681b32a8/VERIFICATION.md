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

For the full labelled length-three count law, E(C_i)/3 identifies the positive stationary mass; the all-i event identifies the nonnegative loop q_i by its square. Flow conservation makes the three symmetric edge-flow sums the unique solution of the three incident-sum equations. The (2i,1j) event has probability q_i S_ij + pi_i P_ij P_ji by enumerating its three paths. The product of the two flows and their sum determine their absolute difference; zero divergence identifies the oriented differences on 12,23,31 as one common signed current. No step divides by a possibly zero transition: only pi_i is a required nonzero denominator. Both signs are realized by the given chain and its stationary reverse, which have identical counts by path reversal (one matrix if the current is zero). Diagonal similarity of the transpose preserves every indexed principal minor of P and I-P. The strictly positive circulant example has six equiprobable two-visit counts at both delta values and minors 3/16 and 13/64. For two states, same-state two-visit counts recover the loops and hence the rows; at one visit the symmetric two-state family with variable positive switching rate has constant stationary law. This is identification from a population law, not estimation from one path. Independent rational count recursion replay: python3 /workspace/branches/independent_checks.py 3; checks the collision, minor values, reversal, and the directed-cycle boundary, not the universal proof. The frozen checker was inspected, not executed.

## originality

PASS

The exact discrete three-visit inversion and positive two-visit obstruction are distinct on the inspected evidence. The closest motivating full-text passage explicitly asks the finite-visit discrete question. The exact Resultary hit is the matching mirror of the assigned finding, not a distinct earlier theorem.

## value

PASS

The first state-space size with irreversible stationary circulation gives a natural sharp finite cutoff for an explicitly posed occupation-law inverse problem. The inversion recovers the entire chain modulo its unavoidable reversal, while the positive two-visit collision separates recovery of stationary/symmetric flows from even the weaker goal of recovering principal minors. The result does not claim a higher-dimensional threshold or robustness near the boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
