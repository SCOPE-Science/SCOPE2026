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

Reconstructed the labelled overlap graph. An m=n-1 word with two changes has forced predecessor and successor, and forward shifts along its forced extensions eventually remove its first run. Thus there are no all-degree-one components. Contracting these paths gives a directed cycle through A_0,...,A_m,B_1,...,B_(m-1), two constant-word loops, and reciprocal links A_j to B_(m-j). In a tree to A_0 the loop at A_m cannot be chosen; if B_j is the first B-vertex to choose its cross-link, the set A_(m-j),...,A_m,B_1,...,B_j is closed away from the root. All B choices are therefore forced. Each internal A choice then reaches the forced B chain independently, giving 2^(m-1) trees (one when m=1). This construction also makes the graph Eulerian. The fixed-first-edge BEST multiplier is one since all outdegrees are 1 or 2. The unique occurrence of 0^n gives exactly one rotation of each admissible host; no reversal or colour quotient enters. Counting change locations gives n^2-n+2 windows. The uploaded checker was inspected as evidence; it checks reduced transitions, exact cofactors at 2<=n<=10, and exhaustive fixed-first-edge tours at 2<=n<=7. The all-n argument here does not depend on those recorded runs.

## originality

PASS

No inspected primary source or distinct catalogued record states or directly entails the switch-restricted count and its freely binary last-exit choices. Restricted-cycle existence and the use of overlap digraphs and BEST are established methods; neither is credited as new here.

## value

PASS

A change cap tests universal cycling on the first family admitting a return to a previous letter within a window while allowing arbitrary run lengths. The exact host multiplicity and binary parameters say considerably more than Eulerian existence, giving a construction and an exact all-length test case for restricted universal-cycle enumeration. A routine uncomputed tree determinant would not supply that classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
