---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

Execute `python3 verify.py` using only Python 3 standard-library modules. The checker constructs the exact rational Friedkin–Johnsen matrix \(I+L\) on each weighted star and solves every cascade-reachable state by exact rational elimination. For each \(m\in\{1,\ldots,6\}\), \(w\in\{1/3,1,2\}\), and \(p\in\{0,1/4,1/2,3/4,1\}\), it enumerates every possible set of activated leaves and computes the weighted sums for a hub and a leaf seed independently of the closed forms. These values are compared against the formulae, rank sign law, and activation-reach identity: 180 paired exact-rational checks.

The finite checks are not an exhaustive proof over arbitrary population size or real positive edge weights; equations (1)–(4) in `RESULT.md` provide that proof. The reference paper is a model source, not a source of independent validation of the present threshold. An independent audit has not been performed.
