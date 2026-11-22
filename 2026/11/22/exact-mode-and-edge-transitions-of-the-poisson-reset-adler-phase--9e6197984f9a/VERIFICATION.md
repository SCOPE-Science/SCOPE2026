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
# Verification of the stationary reset-Adler density

The claim applies to \(K,\Delta,r>0\), with simultaneous full resetting of both oscillator phases to zero. Its exact invariant law is the pushforward of an exponential reset age. On the running circle every interior angle has ages \(A(\phi)+nT\); for locked trajectories each interior angle has exactly one preimage. This gives the two densities and their normalization without numerical approximation. Exact logarithmic differentiation reduces the full mode classification to the sign of \(K\cos\phi-r\). The locked simple-root expansion and the critical double-root exact antiderivative give the boundary exponents and constants. There is no stationary atom at a stable equilibrium because the stationary elapsed reset age is finite almost surely.

`verify.py` was run with Python and SciPy and printed `Passed 97 deterministic numerical checks`. The checks cover rotating, locked and critical regimes; normalization including explicitly accounted small omitted edge tails; direct density derivative comparison; algebraic edge slopes; critical essential asymptotics; and the exact revolving period integral. Finite numerical checks are diagnostics only; the proof in RESULT.md establishes the full infinite-parameter statements.

No independent scientific audit or external mathematical certification has been performed. The comparison with all unindexed literature is unresolved.
