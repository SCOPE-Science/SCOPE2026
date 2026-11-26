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

For a minimizing deletion the complement is nonempty (deleting all but one vertex would suffice). Its edge count gives 2k−n=c+e(S), hence k≥floor(n/2)+1. Adjacent empty columns are forbidden by a square. For the candidate minima, intact rungs are isolated. Between them there can be only one connecting path, provided the surviving rail stays constant across the intervening singleton run; other surviving path segments are acyclic and attach to at most one intact rung. Contract intact rungs and suppress connecting paths, retaining possible loops and parallel edges: the surviving cyclic chain has a cycle exactly when no link is cut, including one or two intact rungs. A double deletion cuts the chain. The empty-column bound leaves just the stated odd pattern or the three even patterns; the odd pair must select opposite rails, and at least one of the two adjacent pairs in an even single-only state must do so. Both parities therefore attain the bound. For the two length-two runs, anchor one of the m−1 empty columns and choose two of its m−1 ordered cyclic gaps; dividing by m−1 gives n(m−2)/2 placements of labelled column sets. The four rail-assignment counts give the two census formulas. In odd lengths the isolated singleton flips are always legal; a horizontal slide that preserves the independent empty-column set must move from the unique paired run, and its destination pair must be oppositely selected. The two tests involve distinct unconstrained singleton rails for n≥7, the same singleton with opposite requirements for n=5, and both moves are legal for n=3. The special degrees and all-size polynomial follow.

## originality

PASS

The minimum size is prior; the full labelled optimum census and odd adjacent-slide degrees are not established by the identified prior results. This is a bounded best-evidence assessment.

## value

PASS

These are exact natural statistics of a cubic family with known minimum deletion number. Classification distinguishes the extra even-parity patterns, and the complete degree enumerator gives quantitative information about permissible repairs that ordinary exchange connectivity misses; these are useful exact benchmarks and not a claim about global slide distances.

The dated certificate retains the supplied scientific assessment, sources and limitations.
