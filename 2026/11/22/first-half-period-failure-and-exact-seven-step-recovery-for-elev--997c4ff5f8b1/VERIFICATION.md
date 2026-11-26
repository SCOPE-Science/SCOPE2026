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

Independently enumerated precisely the (p-1)! cycles by anchoring their cyclic words at rank zero. For 0<t<p the two extreme rank comparisons are constant; each other comparison was assigned a separate bit, and all relevant prefixes were compared as exact unsigned integers. At p=5,7,11 respectively the h-1 prefix has 4,128,82080 colliding unordered pairs and h has none; at p=3 the first row separates the two cycles (the empty row cannot). Refinement gives the minimal horizons 1,3,4,7. At p=11 the six-step fibers of sizes 1,2,4 number 3470400,77760,720 and no other sizes occur; the seven-step partition has 3628800 singleton fibers. Also independently checked both displayed witness rows at the first divergence. The prime 11 threshold uses the four consecutive odd primes, not an inference about later primes. Replay: python3 /workspace/review-evidence/ordinal.py and the same command with large, using NumPy integer arrays; ordinal-small.log and ordinal-large.log record the output.

## originality

PASS

The truncated fixed-rank horizon and ambiguity census are distinct from the strongest inspected complete-signature reconstruction results. No distinct record inspected establishes or implies those truncated claims. This is a bounded comparison, not a priority assertion.

## value

PASS

This locates a genuine failure of recovery with a half-period budget even when all spatial ranks are observed, and quantifies exactly how badly that budget fails at its first odd-prime obstruction. The jump to guaranteed recovery at seven and the multiplicities separating typical from ambiguous observations are meaningful benchmarks for shorter ordinal inversion. This is not a claim of an asymptotic law or an efficient inverse for arbitrary prime lengths.

The dated certificate retains the supplied scientific assessment, sources and limitations.
