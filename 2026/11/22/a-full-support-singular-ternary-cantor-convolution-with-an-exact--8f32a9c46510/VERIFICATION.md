---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

With an incoming carry of 0 or 1 the next raw sum is 0,1,2,3 or 1,2,3,4 respectively, each equally likely. The three carry updates in RESULT.md follow by reducing modulo 3, and both final carries must be retained for a modular fiber. Both rows admit all output digits. Exactly one input pair out of four yields 2 at either carry, so conditioning on all lower input pairs proves the full independent indicator law, not just its marginals. Its product law gives the exact grouped fiber sum. The digit-frequency event separates the measure from Haar; atomlessness follows by conditioning on Y and using the atomlessness of X. Squaring the three successor row sums gives 6(a+b)^2-2ab, while summing their coordinate products gives (a+b)^2. With the empty row (1,0) this yields the stated collision recurrence and constants. Squared cylinder masses have denominator 16^k, yielding the stated 3-adic correlation dimension. An independent direct enumeration at depths 1 through 8 tested support, energies and every specified pattern of positions with digit 2: these had multiplicities 3^(k-j) and summed to the stated binomial counts. The energies were 6,34,192,1084,6120,34552,195072,1101328. Replay by listing all ternary 0/1 masks, tabulating (x+2y) mod 3^k and grouping those fibers by the digit-2 position mask. The source check.py was inspected, not executed; its reported 9935 counter includes 35 iterations that increment without an exact comparison, so that number is not a count of exact assertions. This does not affect the analytic proof or the independent enumeration.

## originality

PASS

Best-of-knowledge pass for the weighted probability convolution and its specific digit and collision laws, not for the abstract recurrence or general carry-automaton method.

## value

PASS

The weighted sum has complete residues but is not Haar-like: the exactly independent exceptional-digit process supplies a simple singularity witness, while the intrinsic modular collision rate quantifies the concentration. The result gives both a structural and a quantitative invariant for a natural pair of digit measures; its value is not the known recurrence in isolation. It says nothing about Euclidean convolution density or the full dimension spectrum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
