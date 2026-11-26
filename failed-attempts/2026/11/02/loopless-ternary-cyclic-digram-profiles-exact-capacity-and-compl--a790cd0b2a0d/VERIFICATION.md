---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Balance enforces a common signed circulation and gives a unique decomposition into reciprocal pairs and one oriented triangle type. The non-isolated support is connected for any nonzero parameters on three vertices, so Euler realization is exact. For two positive reciprocal pairs at zero circulation the hub excursions reduce to binary necklaces; singletons occur exactly when one multiplicity is one. With one reciprocal pair and positive circulation the detour allocations are cyclic weak compositions, unique exactly when t=1 or the reciprocal count is one. For the remaining supports, the two explicit base words in each case have matched digrams and unequal cyclic 012 counts, and replacing an edge by its alternating three-edge walk inserts two alternating triples and preserves the old triple counts. This proves all excluded cases. Summing gives both generating functions; their primitive cube-root and minus-one poles do not cancel (the numerator of C has only a simple zero at −1). The fourth-order pole at 1 has coefficient 1/12, giving n³/72, and the singleton formula gives the stated small cases and eventual period. Code size is the number of realizable profiles by taking one representative per deterministic observation. Inspected but did not execute verify.py; the recorded enumeration through length 16 and parameter checks through 100 are supporting finite checks, not the proof.

## originality

FAIL

The mathematical results are correct, but the entire substantive claim is covered by explicit zero-loop specialization of published archive results. The Oct. 26 support-refined flow enumeration gives the all-profile slice, and two distinct indexed same-day records classify singleton profiles with loops allowed; setting the three loop counts to zero reproduces exactly the frozen singleton classification. This is actual implication, not reliance on titles, on mere same-alphabet usage, or on inferred priority among same-day entries. The generating functions, exact eventual periods and code size then follow by elementary summation and coefficient analysis.

## value

FAIL

The loopless model is natural and the explicit word pairs give a transparent proof, but the submitted contribution is a mechanically extracted slice of the broader exact structural and counting results. Neither the derived residue list nor the capacity reformulation adds an independent mathematical conclusion. The constructive proof has not been turned into a distinct claim with independently demonstrated value, so no surviving repair is delivered.

The dated certificate retains the supplied scientific assessment, sources and limitations.
