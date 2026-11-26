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

The final theorem is unchanged. On a periodic orbit, excitation events have disjoint predecessor and successor neighbor sets, since a vertex cannot re-excite within two updates. The total required predecessor contacts are at least the sum of the thresholds, and the sum of predecessor plus successor contacts is at most the sum of the degrees. At the rounded half-degree threshold equality holds event by event: all neighbors occur in one of these sets and exactly half in each. Connectedness propagates activity to every vertex and forces every degree even. On a triangle with excitations a(t), b(t−1), c(t+1), independence and the no-repeat rule force c(t−2) and b(t+2), then a(t+3); repeating on the periodic time axis gives exactly the three-step clock. The frozen Step 4 reversed the predecessor and successor phase labels (for an excited vertex of color 1 they are 2 and 0, not 0 and 2). The replacement derives the phase counts at excitation and then shifts the time slice; the symmetric balance condition and its converse are unchanged. A fixed (k−1)-set yields a clique of size n−k+1, at least four except J(4,2). That graph is K_{2,2,2}, with exactly six proper balanced colorings partitioned into two orbits. Finiteness and the unique all-rest fixed point give the extinction equivalence.

## originality

PASS

Pass for the complete recurrence classification at a vertex-dependent rounded half-degree threshold on connected vertex-triangle-covered graphs. The J(n,2) slice is already covered in a distinct same-date record and is not credited; the full Johnson range is an application, not the essential contribution. The repair corrects phase bookkeeping and acknowledges the exact overlap without claiming priority within a date.

## value

PASS

The final claim provides an extinction criterion at the critical contact ratio, where strict inequalities give no answer. The structural timing lemma converts arbitrary recurrence to local balance constraints, handles heterogeneous degrees, and gives a natural infinite family application. The boundary is genuine: the triangle-free K_{2,2} at local threshold one permits a rotating four-cycle. The value is the reusable recurrence theorem, not a duplicate count for J(4,2).

The dated certificate retains the supplied scientific assessment, sources and limitations.
