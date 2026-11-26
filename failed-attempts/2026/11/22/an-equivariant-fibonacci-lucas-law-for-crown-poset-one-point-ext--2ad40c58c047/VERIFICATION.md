---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

An induced pointed extension is specified by its ideal of predecessors and filter of successors with all cross-comparisons strict; homogeneity identifies the comparison pattern with the complete nonalgebraic type over the named base. Passing from an ideal to its maximal antichain gives an equivariant bijection with independent sets of the 2n-cycle. A rotation by k reduces this cycle to length 2 gcd(n,k) (a single adjacency in the 2-vertex case); a rank-preserving reflection folds it along opposite fixed old vertices to a loopless path on n+1 vertices. The cycle and path recurrences give L_{2 gcd(n,k)} and F_{n+3}. Complementation pairs the two one-sided sectors; the empty pair is counted once. Mixed types are indexed by incidence edges, minima, and maxima, respectively: identity fixes all 4n, nonidentity rotations none, and a reflection fixes no incidence edge and exactly two old vertices. This gives the character, including both even-n reflection classes. Burnside gives the quotient formula; the proper-divisor bound d <= n/2 and a union bound give both asymptotics. At n=5 the fixed counts 265, four times 5 and five times 43 give 50 orbits. The supplied verify.py and verification_output.txt describe finite enumeration for n=5..9 and arithmetic checks through 50; inspected, not executed and not relied on for all n.

## originality

FAIL

A distinct indexed record supplies the identical quotient and asymptotics for n>=3, and supplies the same equivariant decomposition and fixed-ideal character from which the exact type character follows mechanically. This is demonstrated overlapping coverage, not a determination of same-day publication order or historical priority.

## value

FAIL

A fixed-point character is a natural invariant, but the quotient, its asymptotics and the equivariant decomposition are already in the matching record. The only difference in presentation is evaluating fixed points in the three explicitly indexed mixed orbits and adding them to the stated fixed-ideal counts. The resulting packaged character and transfer-matrix presentation do not supply a distinct, nonmechanical finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
