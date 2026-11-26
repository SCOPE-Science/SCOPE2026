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

Robustness makes the reduced outsider map exact for every admissible initial state. Nondecreasing quantizers and nonnegative weights make it isotone on the invariant cube. Iterating from its bottom and top gives nested bounds; both extreme initializations are themselves admissible. Once both extreme actions equal a, their opposite monotonicities and their ordering keep both there. Conversely, if every admissible initialization adopts permanently, the two extreme ones do so; the later of their times is the sharp uniform time. During a constant action stage the geometric update holds through the first change, including all simultaneous changes. For an upward crossing the limit must be strictly above an unreached cut, with equality at a finite iterate allowed; for a downward crossing both the limit and the crossing iterate must be strictly below the cut. These rules and the monotone sum of level distances prove termination within the claimed number of changes. Independent exact substitution yields T_3=4 and T_4=3 in the example: the upper private state at time 3 is (67/200,121/200), with actions (9/10,0), and at time 4 is (67/400,229/400), with actions (0,0). The lower actions are (0,0) from time 3. Both scalar admission thresholds are max(1/5,7/10)=7/10, above the actual seed weight 2/5. At time 1 the exact ties at -4/5 and 4/5 take the higher action as stipulated.

## originality

PASS

The inspected prior results supply monotonicity, robust-cluster tests, and significant overlap in exact two-sided adopter sets and scalar-rule counterexamples. The supported distinction is the joint least-uniform clocks and finite event-skipping bound for general finite ordered alphabets in the stated regime, not the idea of two-sided comparison or the existence of a scalar-rule counterexample by itself.

## value

PASS

The exact clock is a stronger and practically different invariant than a sufficient cascade or an eventual consensus claim. Fast-forwarding through constant action stages addresses arbitrarily long silent waits while detecting truly nonadopting outsiders; the exact tie-sensitive example shows why a sufficient scalar rule cannot stand in for this procedure. The bound is on scientifically relevant action events, not computational running time.

The dated certificate retains the supplied scientific assessment, sources and limitations.
