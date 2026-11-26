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

Reproduced the census independently on the 20 subset vertices and 30 containment edges, without executing the uploaded programs. The scan covered all 184756 side-labelled ten-vertex sets. The cut formula c=30-2e(S) follows from cubicity, so there are no odd widths. Exactly ten labelled sets attain width 6; the five coordinate families and their complements are all balanced and attain it. Dividing the labelled histogram by two gives exactly the stated 12 nonzero unordered coefficients, summing to 92378. Enumerating all 100 exchange candidates from each legal state and traversing components gives 10 singletons at b=6; ten components of 31 and 60 singletons at b=8; and a 5650-state component and 12 singletons at b=10. Every 31-state component has one optimum, and the giant component has all ten, so every pair of distinct optima requires width at least 10 and can attain it. At b=8 the ten nontrivial components pair under complementation since each has just one optimum; at b=10 the unique giant is invariant and halves in the quotient. The isolated states pair in both cases. Within the structural argument the maximum for a fixed two-set family is the sum of the largest compatible triple degrees; the full census independently certifies the reported optimizers. The two graph presentations can also be checked directly: modulo five, use outer vertices {i,i+1}, {i,i+1,i+2} in alternating order, and respective spoke partners {i,i+1,i+3}, {i,i+2}. Containment makes the outer step one and the inner step three in the alternating indices. Frozen replay paths: verify_middle_levels.py and verify_gp.cpp, with verification_middle_levels.txt and verification_gp.txt. No larger-family claim is established.

## originality

PASS

The supported distinct result is the exact balanced-cut and balanced-swap landscape of Desargues GP(10,3), especially the four-edge barrier between optimal cuts. The closest exact indexed excursion theorem concerns dodecahedral GP(10,2) and has different minimizers and budget-eight connectivity. The inspected same-family middle-level and bipartite Kneser results establish Hamiltonicity rather than a cut distribution or a width-constrained swap census. No equivalent coverage was found in the checked statements; some graph-bisection literature remains inaccessible.

## value

PASS

The problem asks whether optimal balanced cuts can be interchanged while remaining near optimal, a natural reconfiguration question on a canonical cubic middle-levels graph. A one-step budget increase produces sizable but mutually disjoint optimum neighborhoods; the next admissible increase joins all optima. The exact four-edge barrier and the counted low-width state spaces give a meaningful benchmark distinct from static width or a generic graph statistic. The polynomial supplies useful exact context, but the justified value is not predicated on a claim for larger graphs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
