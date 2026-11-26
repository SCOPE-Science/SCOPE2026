---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Translation by L=lcm(1,...,n) preserves all eligible offsets. At m=(n-1)^2 and H=2n-3 the sole multiple of each of n-1 and n is at offset n-1, proving the uniform lower bound by monotonicity in H. I wrote and ran an independent exact search /workspace/branches/audit_interval.py (arguments 2 through 17); the executed n=17 scan was split into million-residue chunks, with logs in /workspace/branches/interval_runs. The search uses no augmenting paths: it eliminates a modulus of degree at least the remaining number of moduli (assign it last), eliminates a modulus with a private offset (assign it there), enforces forced singleton assignments, and otherwise branches over every candidate offset of a minimum-degree modulus. Modulus 1 can be assigned last because H>=n. Reflection of actual interval values maps m to -m-H-1 modulo L and preserves matching, so one representative per reflection pair is exhaustive. For 2<=n<=16 the scan found no failures at 2n-2. At n=17,H=32 it checked all 6,126,120 reflection classes, recovered 32 full-period failures, minimum 485749, and checksum 11468177711038706587. None of the checked failures is consecutive modulo the full period; hence every length-33 interval contains a successful length-32 subinterval starting at m or m+1. This independently proves the upper bound without testing all length-33 intervals separately. At 485749 the six stated moduli have union {9,11,22,23,26}, validating the explicit Hall obstruction. Nothing beyond n=17 is certified.

## originality

PASS

Credit the all-start problem, its period reduction, and prior bounds to the existing work. The supported distinct contribution is the first finite deviation from 2n-2, together with the exact obstruction census at that index. The exact matching Resultary item is the assignment itself. The closest primary material inspected establishes the same uniform function and asymptotic bounds, not a finite result implying this census. Unavailable portions and the unresolved database lead leave a historical-priority risk; neither is used as negative evidence.

## value

PASS

This is a natural, historically posed uniform matching problem. Locating the first failure of the simple two-modulus lower bound identifies where that obstruction ceases to explain the exact extremum; the explicit six-to-five Hall obstruction explains the change. The full residue census also shows that the obstruction is rare and never occurs at consecutive starts, precisely the structural fact needed for an independent length-33 proof. The cutoff was motivated by the first deviation, not an arbitrary finite endpoint.

The dated certificate retains the supplied scientific assessment, sources and limitations.
