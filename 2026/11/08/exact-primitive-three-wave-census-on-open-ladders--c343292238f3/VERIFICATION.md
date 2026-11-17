---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

In a connected graph, every nonfixed 3-periodic GHM state must cycle all vertices through 0,1,2; any permanently zero vertex adjacent to a cycling vertex would be excited, a contradiction. This is equivalent to each initial vertex seeing a successor-color neighbor. The 27 normalized ordered-rung states, open-boundary vectors and transition M count each coloring with global color shift factor three. Independently reconstructed all 27 entries and verified the componentwise exact identity M^3 b=4M²b-Mb-2b, plus 3a[b,Mb,M²b,M³b]=[0,6,24,90]. Independently applied three literal GH updates to all ternary configurations on open ladders n=2..6; counts 0,6,24,90,324. Thus the unbounded recurrence follows from a complete finite matrix identity, not sample extrapolation.

## originality

PASS

Best-of-knowledge: searched published general GHM papers and nearby ladder-specific results. An existing November 8 open-ladder theorem counts all initial configurations by eventual excitation rate (0,3/4,1), NOT those immediately on primitive period-three cycles; its rate-one class includes transients and is numerically far larger. Another November 8 theorem treats circular/Möbius ladders and explicitly identifies the open-ladder recurrence as a different boundary problem. Neither yields this exact open-boundary N_n recurrence by direct specialization.

## value

PASS

An exact population law for immediate Greenberg–Hastings oscillations on the natural finite-width open ladder is an independently useful structural census. The unexpected cubic recurrence and small 27-state certificate give all sizes and a sharp entropy exponent, distinguishing immediate waves from long-term activity classes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
