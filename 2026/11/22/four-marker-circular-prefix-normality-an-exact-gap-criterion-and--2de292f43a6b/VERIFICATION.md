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

A maximizing circular window of positive length can be shifted to its first one without losing any ones. A simultaneous maximizing root is exactly a one-root minimizing each first-attainment length for two, three and four ones. The second and fourth thresholds force the outgoing gap to be a minimum and the incoming gap a maximum. With four gaps those extrema compare the candidate two-gap sum to each of its three rivals, so the third threshold is automatic, including ties. For counting failures, nontrivial stabilizers would give constant or alternating gaps and hence a root. For increasing multiplicity patterns (2,1,1), (1,2,1), (1,1,2), (1,1,1,1), fix the unique appropriate extremum when counting circular arrangements to get 1, 2, 1, 4 forbidden orders. Counting positive successive increments gives the four terms in RESULT.md; their combined numerator over (1-z^4)(1-z^3)(1-z^2)(1-z) is z^3(1+z)^2 before shifting from gap sum to length. The first failure is the gap class of (0,0,2,1), and the leading cubic coefficients are 1/36 for failures and 1/24 for all necklaces. At any weight at least five the stated examples meet the extremum test at only one root, whose length-three prefix 110 loses to 111. At smaller weights 2 and 3 no unaccounted threshold remains. Whole periods add the same number of ones in every window. A fresh direct-window reproduction at /workspace/branches/d53ddb98-0eba-402e-b669-8b5e51e67d51/ordinal1_direct_check.py independently checked the exact sets of roots and counts for all 1,820 tuples of gap sum at most 12, not the universal claim by enumeration. The uploaded checker was inspected, not executed.

## originality

PASS

No inspected distinct record establishes the weight-four circular root criterion, forbidden count, and sharp universal boundary. The strongest same-day comparison is mathematically close: it classifies finite linear cuts for the same necklaces, and its singleton-cut series is exactly z times the circular failure series. Direct comparison of the rank counts explains that shift without equating the underlying properties. This is a best-of-evidence comparison, not a priority certification.

## value

PASS

The extremal adjacency rule turns a simultaneous test against all wrapping factors into a local test even for ties and imprimitive periods. Weight four is the first case where there is an intervening multi-gap obstruction to rule out and the last weight where that simplification works universally. The exact failure census and limiting positive fraction show how often rotation fails even in a sparse, natural family. This identifies a sharp boundary and is stronger than listing initial necklaces or reapplying a generic recognizer.

The dated certificate retains the supplied scientific assessment, sources and limitations.
