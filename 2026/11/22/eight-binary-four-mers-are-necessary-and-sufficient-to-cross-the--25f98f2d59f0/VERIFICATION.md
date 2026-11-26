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

The frozen endpoint argument incorrectly asserts that any overlap of length at least four identifies the terminal and initial four-mers; it does so at length four, not at greater lengths. The replacement first proves noncontainment is preserved: a third string contained across the two merged copies would start before the second copy and end after the first, giving an overlap strictly longer than the chosen global maximum. With noncontainment, any new overlap with the merged string must be shorter than the relevant full prefix or suffix copy, so was already available before the merge. The maximum never increases from its initial bound three, and endpoint reduction follows. The worst-Greedy recurrence enumerates all maximizing ordered choices and minimizes earned overlap. The corrected optimum argument uses successive start gaps in any superstring for one inequality and explicit assembly in a permutation for the reverse. Independently, a literal-state search and a scan of all 1,048,560 binary words of lengths 4–19 with a superset-min transform confirm the two quantities for all 39,202 input sets; length 19 suffices by an exhibited linearized de Bruijn word. All eight rows and counts agree. The only strict exceeders are masks 1343, 5431, 60584, 64672 with (G,L)=(17,11), and they are exactly one complement/reversal orbit. The explicit Greedy witness was checked at each step; the shortest witness meets the four-mer factor-count lower bound. The corrected RESULT.md was reread and requires no changes to either checker or log.

## originality

PASS

The repaired result credits the prior endpoint lemma and expressly distinguishes the companion global maximum and identical four equality cases from the surviving distinct contribution: the first 3/2 crossing, the exhaustive list of strict exceeders through size eight, and the per-size maximum/count table. The global result and its published log report only the global optima; the global bound and equality classification do not imply the lower 3/2 exclusion, since ratios strictly between 3/2 and 17/11 remain possible under those statements. The companion itself describes a preceding limited-cardinality result matching this threshold, not an independent derivation of the per-size table; no exact publication order is inferred from the dates.

## value

PASS

Fixing width four and the binary alphabet isolates the smallest obstruction to a meaningful 3/2 bound for maximum-overlap Greedy. The sharp jump from equality at size seven to a strict violation at size eight, with just one orbit and a short checkable witness, identifies a useful exact boundary not given by the global maximum alone. The row counts describe the complete bounded extremal regime, rather than a lone example or a recomputation of the companion global ratio.

The dated certificate retains the supplied scientific assessment, sources and limitations.
