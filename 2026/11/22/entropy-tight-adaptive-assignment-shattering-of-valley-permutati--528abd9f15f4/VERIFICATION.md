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

Re-audited corrected RESULT.md and SLOGAN.txt against the frozen assignment-cell definitions. A forbidden triple is exactly one with largest entry in the middle, which gives the decreasing-then-increasing characterization by splitting at the minimum. In the remaining interval after the larger ranks have been removed, the worst rank v is at one endpoint, so the adaptive cell reads the next independent bit (credited background). The matching online upper bound follows from the number of leaves versus hypotheses. For n=2k−1 the odd-value cells above rank 3 can be toggled independently using one left placement per consecutive value pair. The last three values give two independent static answers: b_3 controls the rank-3 cell and b_2 can make b_2+b_3 equal or unequal to 1 to toggle the rank-1 cell. Appending the new maximum preserves those answers at even size; {12,21} handles n=2. A shattered (n−1)-support would give a bijection between hypotheses and traces and hence half marginals for all cells used. The binomial two-atom calculation excludes every v<n at n≥4; the only two half marginals for the maximum are mutually exclusive. For the finite result, an independent exact enumeration filtered all permutations directly, built only supports with an all-positive witness, and counted the distinct Boolean projections onto each such support without splitting trace classes. Every shattered support was included as a candidate. It reproduced every coefficient through n=8, ruled out larger sizes by the first empty layer or the cardinality bound, and confirmed the gaps 0,0,0,1,1,2,2,3. The repair keeps all numerical conclusions, while making the class characterization, singleton example and empty-support trace initialization precise.

## originality

PASS

The original presentation treated the all-order adaptive construction as distinct from the earlier endpoint-deletion comparison tree. That attribution does not survive: the two trees have exactly the same splits on each node's restricted hypotheses. The even-size lower-bound idea also transfers from the earlier nested comparison cubes. The corrected RESULT.md and slogan retain those facts only as credited baseline and place the distinct claim on the static assignment-cell census, the static gap obstruction and odd-order shattering beyond the comparison bound. The inspected prior results do not imply that remaining claim.

## value

PASS

The rank-at-one-position predicate is a natural fixed query on a single-peaked preference ranking. Changing from comparisons to cells preserves the adaptive benchmark but changes the static shattering complex, even changing the first size that realizes a three-unit gap. The odd-size construction and the all-order obstruction give structural evidence beyond the finite experiment, and the coefficientwise census identifies which finite cutoff really occurs rather than testing isolated instances. It is useful as an exact comparison benchmark for any general classification of static shattering, without claiming an exact dimension for larger n.

The dated certificate retains the supplied scientific assessment, sources and limitations.
