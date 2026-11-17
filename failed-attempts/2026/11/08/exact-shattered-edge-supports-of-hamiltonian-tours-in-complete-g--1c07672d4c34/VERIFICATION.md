---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

PASS: For K_n, an all-positive realizable support lies in a Hamiltonian cycle and is a linear forest unless the support itself is the full cycle. A spanning n−1-edge path fails a trace. Contract forced positive paths into blocks, avoid forbidden path adjacencies; for >=6 blocks Dirac degree bound applies, at 5 explicit complementary tour applies, and at 2,3,4 block cases determine exactly the singleton/long path or two-long-path exceptions. Exponential labeled-forest formula counts smaller supports and the two-path boundary counts the top coefficient, including n=3,4. Fresh direct exhaustive tour enumeration gave counts n=3:1, n=4:1+6z, n=5:1+10z+45z²+60z³, n=6:1+15z+105z²+375z³+360z⁴.

## originality

FAIL

FAIL: An earlier published November 2, 2026 RESULT.md was read in full and establishes exactly the same Hamiltonian-tour shattering iff, maximum two-path exceptions, complete polynomial and VC dimensions. This is covered even though notation and low-level proof arrangements differ.

## value

FAIL

FAIL: The exact complete natural classification and every coefficient are already available in the earlier published full theorem. The claim is mathematically natural and correct, but this submitted artifact adds no independently valuable new invariant/structural deduction beyond the covered published package.

The dated certificate retains the supplied scientific assessment, sources and limitations.
