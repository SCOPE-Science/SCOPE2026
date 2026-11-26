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

For t>=1 the refractory set at t equals the excited set at t-1, so the two Boolean layers and the initial resting test encode the stated synchronous rule with distinct neighbors exactly. Independent ordered ternary diagrams, with skipped variables weighted by their numbers of three-way completions, reproduce the latest excitation times for n=1..13: 1,1,2,2,3,3,4,4,4,4,5,5,5. All time-six roots vanish. Restricting to the original columns within horizontal distance six of a site preserves its time-six state: the update cannot use a site outside this window before time six. Such a restriction is an open strip of at most 13 columns, including all boundary cases. If a last excitation occurs at t, it leaves refractory sites at t+1 and the strip is first all-rest at t+2. If there is no excitation at any time, tau is 0 or 1, so this case does not affect a maximum. On width 11 the only possible time-five excitations are at the top and bottom of column 6 (one-based); the exact event sizes are 632,772 each and disjoint. In particular, their union size is 1,265,544; a time-five center-column excitation has the same dependency window after any extension of the block. Direct witness counts at times 0..6 are 11,12,7,4,2,1,0, and disjoint eleven-column blocks have independent trigger events of probability 1736/3^27. These facts give the asserted maximal times and probability lower bound for every n.

## originality

PASS

Best-of-knowledge pass for the sharp length-dependent extinction clock and exact minimal-width trigger count. The strongest inspected comparisons either change the contact threshold, change the graph, or address a large-range probabilistic planar limit, rather than the all-initial-states open width-three rule.

## value

PASS

An exact all-input collapse clock on a natural infinite family of strips is useful as a boundary-sensitive test of finite-width excitability. The five sharp length regimes, the finite radius needed to prove the exclusion, and the exact count of the first local trigger jointly resolve more than existence of extinction. The count provides a quantitative explanation of why maximum delay becomes typical without sustained activity; it is not claimed to be a large probability on modest lengths or to generalize to other widths.

The dated certificate retains the supplied scientific assessment, sources and limitations.
