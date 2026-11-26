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

The residue classes modulo g are the directed d-cycles. The rotation permutes them and b maps within them, so none can become empty. Under the word-action convention the macro E_j fixes every point except j, which it sends to j+d. A target meeting every cycle leaves missing vertices in disjoint paths, and deleting each path in source-to-successor order decreases rank at every step and gives exactly the desired target. Conversely a strict decrease is possible only when source and successor are both present, so these and only these precedence constraints apply; ell_i must denote the number of vertices in each path. The empty sequence works for the full target. Each b drops at most one rank and the rotations drop none, proving the optimal b-count. Independent nonempty subset choices give the stated polynomial and all ranks from g to n, with the coefficient formula by inclusion–exclusion. Independent /workspace/branches/audit_automaton.py found exact image sets and rank counts for 14 noncoprime pairs n<=10 and replayed actual forward contractions for 665 smaller targets and the 70-order example. Frozen verify.py lines 41–57 instead counts reverse schedules (a missing successor must already have been removed by its recursion); reversal is a bijection and preserves the count, but it does not independently simulate forward legal contractions as its comment suggests. The theorem is established by the proof and forward replay, not by interpreting that recursion as forward validation.

## originality

FAIL

A distinct indexed result states the same reachable subsets, optimal number of defect letters and factorial schedule count for the identical automaton over a broader parameter range. Its schedules are exactly the frozen macros' strict orders. The explicit rank polynomial is the direct binomial product for that already characterized family, not a separate unsupported-priority issue. This is a finding of scientific coverage, not an inference of authorship or priority from catalogue dates.

## value

FAIL

The partial image family and optimal strict-collapse counts are natural invariants, but their exact determination is already supplied by the broader indexed result. The only incremental expressions here are the immediate independent-residue-class product, its specialization, and its expansion. They make a convenient restatement but do not form a distinct, independently useful scientific result under this standard. No valuable uncovered remainder in the frozen finding warrants a repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
