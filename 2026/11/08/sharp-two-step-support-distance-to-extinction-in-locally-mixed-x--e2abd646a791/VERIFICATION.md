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

For n≥2 and 0<lambda<1, let b_i=x_(i-1) XOR x_i. Rule60/102 outputs at site i are b_i or b_(i+1), so if equal that output bit is forced, and otherwise both bits can occur with positive probability. Zero is accessible in one step iff no isolated bit in x (no cyclic 010 or 101). Each cyclic b-word admits a smoothing output y preserving all forced positions and with all constant runs at least length two, hence y itself has no isolated bit and can reach zero next; a one-hot x has a forced nonzero update, establishing worst distance exactly 2. Four-overlap-state transition matrix for no-isolated cyclic words has characteristic polynomial (t²-t-1)(t²-t+1), giving exact A_n=phi^n+psi^n+2cos(n pi/3), including n=2; probability of chosen two-step path at least r^(2n), r=min(lambda,1-lambda), implies stated geometric tail and finite expectation. Independent bit-support brute for all 2≤n≤9 and recurrence n≤9 corroborated; finite experiments are not the infinite cyclic run proof.

## originality

PASS

PASS, qualified. Cirillo–Vliem–Schuricht–Spitoni 2026 proves a four-step route to zero for n≥5 at balanced mixing and a one-step cleaning criterion. This does not imply a two-step sharp support diameter or exact census of all initial configurations by minimum distance. Resultary earlier paper computes unconditional one-step absorption probability under fair random x, not worst-case positive-support distance. The new sharp two-step global reachability and exact census survive that prior comparison.

## value

PASS

PASS: Exact positive-support accessibility radius, its distribution of initial-state distances, and explicit finite-volume absorption bound address a natural control/reachability invariant of a probabilistic cellular automaton, sharpening a known four-step result to optimal two and explaining which initial words need two updates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
