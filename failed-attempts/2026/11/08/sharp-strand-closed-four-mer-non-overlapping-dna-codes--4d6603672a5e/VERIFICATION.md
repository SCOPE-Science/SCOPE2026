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

As abstract finite-word combinatorics, the endpoint restriction is exhaustive: the final-letter set is the involutive image of the first-letter set and must be disjoint from it. A singleton first-letter set allows at most nine words by the two-letter overlap test. For a two-letter first set the internally valid reversal-involution orbits are indivisible candidates, and pair conflicts encode both directions including all proper overlap lengths; the weight is the number of words. The frozen isolated-orbit and clique certificate gives 8+2+2+2+2+1=17. An independently written exhaustive subset enumeration, independent_enumeration.py, produced 6 usable orbits, optimum 7 and 2 maximizers for the singleton case; and 20 usable orbits, optimum 17 and 8 maximizers for the two-letter case. It checked the supplied witness and computed the group action on the transported codes: 32 labeled optima, four size-eight classes. Reversal acts on closed codes exactly as the letter involution. The frozen replay sources are verify.py with certificate.json and the standalone crosscheck.cpp, inspected but not executed. Nothing here verifies physical performance or other word lengths.

## originality

FAIL

A distinct, published Resultary record gives the same constrained extremum, labeled census and orbit classification under the matching definitions. The frozen result provides no supported distinct finding. This is demonstrable equivalent coverage; no claim about authorship or priority follows from the indexed dates alone.

## value

FAIL

A sharp closure penalty and complete equality classification are natural finite invariants relative to the ordinary 27-word optimum. The frozen finding, however, recomputes the exact existing census and symmetry classes without a separate theorem or distinct useful invariant; reproducibility alone does not create an additional scientific contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
