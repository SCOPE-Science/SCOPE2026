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

# Verification and scope

The included `CHECK.py` uses only the Python standard library. Invoking `python3 CHECK.py` enumerates every independent subset of Lucas index positions for each cutoff \(m\) from 3 through 24, groups exact integer sums, verifies that no value has more than two representations and that each collision has a unique representation containing positions \(0,2\), and independently compares the complete excess-summand count to \(F_{m-2j-2}\). It also tests the parity-specific total for every cutoff. At \(m=24\) the counts are 28,656 double-represented integers and 167,762 represented integers.

The proof for unrestricted \(m\) is mathematical, using canonical interval uniqueness, maximal-tail dominance, the exact even-prefix Lucas identity and a path-independent-set count. Finite tests do not prove infinite cases. Closest literature covers the underlying unweighted two-representation phenomenon, and publication priority remains a bibliographic risk. No independent mathematical audit has been conducted.
