---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

For four candidates and k=3, each greedy marginal equals a sum of weights 1,1/2,1/3, so integer scaling by 6 permits exact tie tests. Enumerating all multisets of 15 nonempty ballot masks with n=1..7 gives precisely 170543 profiles; removing one occurrence of each present type yields 813960 comparisons. Independent implementation of all winning branches and Kelly min/max checks found anomalies 0,0,0,0,0,0,12; all twelve are one S4 orbit of 2ab+2ac+bd+cd+bcd. Full-profile winners are abc,abd,acd and abstention on ab/ac leads only abc. Thus each has two profitable types occurring twice. This is a logically exhaustive FINITE classification; it makes no claim for other candidate/committee counts or deterministic tie-break rules.

## originality

PASS

A precisely defined seven-voter minimal boundary and complete 12-profile orbit classification go beyond established general seqPAV participation failure, which does not enumerate or bound this finite four-candidate three-seat cell. Searches yielded no competing full exact classification, subject to unindexed-computational-work risk.

## value

PASS

The first nontrivial four-candidate, three-seat cell of a standard committee rule has a meaningful sharp lower bound on electorates and a complete classification of minimal paradox profiles, enabling exact benchmarking of participation and ties. The 12-profile orbit is a natural complete finite invariant not obtained as a textbook deduction from general impossibility.

The dated certificate retains the supplied scientific assessment, sources and limitations.
