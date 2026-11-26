---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For p^2 dividing N the factor p^(a−1)(p+1) makes psi(N)=0 mod p, contradicting −1 mod p; hence squarefree. If N is even and has any odd prime factor, psi(N) is even while MN−1 is odd; N=2 gives M=2. For odd N, parity and psi(N)>N force odd M≥3. At any fixed support size r, the multiplier expression product(1+1/p)+1/N decreases in each prime, so the first r odd primes maximize it. Independent trial division and exact integer arithmetic confirm nondecreasing maxima through r=15 and 3 minus the terminal maximum equals 14245067754145838/1253429172199617105>0. The contradiction is unrestricted in N and gives no existence claim at larger support. Replay: python3 -B /workspace/branches/frozen_math_replay.py (dedekind section). Frozen verify.py and verify_output.txt were inspected, not executed; the million-integer scan is not part of the proof.

## originality

PASS

Only the stated minus-sign support exclusion through fifteen is credited as a distinct claim, not squarefreeness, parity, or the extremal-product method. The same-function plus-sign theorem uses the same support cutoff but is not a theorem for the requested residue. The exact correction needed for the minus equation is not supplied by its strict product bound alone, and the inspected both-sign results do not provide this classification. This limited originality decision does not credit the routine adaptation as a worthwhile finding.

## value

FAIL

The motivated equation does not by itself make this short adaptation of an established extremal product an independently valuable cutoff. Once the standard parity is used, the only change to the existing fifteen-prime calculation is adding the reciprocal of the same primorial and observing the numerical slack stays positive. No new obstruction on admissible supports, new cutoff mechanism, or reason to need exactly this inherited cutoff is shown. The valid necessary bound is not shown to be tight or to distinguish actual existence near sixteen. Rewording or replay evidence does not repair that issue.

The dated certificate retains the supplied scientific assessment, sources and limitations.
