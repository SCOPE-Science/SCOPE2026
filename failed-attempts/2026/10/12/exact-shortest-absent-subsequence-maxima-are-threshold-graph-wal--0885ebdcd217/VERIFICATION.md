---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

The assigned maximum is correct as a direct consequence of known extremal A_k and its exact weak-zigzag SAS characterization: a length k+1 word is absent from k alternating permutation arches exactly if each transition forces the next block, i.e. x0>=x1<=x2>=..., including ties. Reflecting odd positions y_i=sigma−1−x_i converts each inequality to y_i+y_{i+1}>=sigma−1. Appending the universal threshold vertex sigma−1 gives a length k+1 graph walk, so its count is OEIS A050447 row sigma−1,column k+1. Kosche et al. Proposition 3.14 independently proves A_k maximizes SAS over words at fixed universality index. Independent exhaustive direct subsequence checks for sigma=2..5, k=1..4 matched the weak-zigzag/graph recurrence and tabulated values. Bounded scans are not proof of global extremality; that assertion is already established in the cited 2021 primary theorem.

## originality

FAIL

FAIL: The central two mathematical facts that determine the alleged new exact maximum were already proved by Kosche–Koß–Manea–Siemer: Proposition 3.14 gives the global maximum at A_k, and the opening of their Proposition 3.10 proof explicitly CHARACTERIZES every SAS(A_k) as the identical alternating weak inequalities. They further provide endpoint prefix-sum recurrences in the proof of Proposition 3.14. Separately OEIS A050447 (pre-October 2026, updated March 15 2026) already explicitly describes the same reversed-prefix-sum operator and threshold-graph walk matrix. The asserted all-(sigma,k) values therefore follow by a direct combinatorial reindexing of a known full characterization and an existing table. Absence of a verbatim SAS label in OEIS does not make this mathematical count independent prior work; claim-vs-prior implication is decisive.

## value

FAIL

FAIL: On the strict shared value bar, merely identifying the already-determined alternating weak-zigzag enumeration with the already-tabulated threshold-graph walk matrix is a low-cost parity reflection/renaming of an existing exact recurrence. Although explicit look-up of maximum SAS numbers is convenient, the submitted package establishes no motivated unknown invariant beyond the already characterized class and existing table, no new extremal witnesses/classification, and no substantive mathematical obstacle beyond the textbook bijection. Correctness, reproducibility and the missing phrase on an OEIS page do not independently prove value. The earlier extremality and full object characterization make the claimed exact count mechanically implied.

The dated certificate retains the supplied scientific assessment, sources and limitations.
