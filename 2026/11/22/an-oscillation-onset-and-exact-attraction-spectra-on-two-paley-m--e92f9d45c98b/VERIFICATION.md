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

Independently enumerated all 8,192 and 131,072 labelled configurations using cyclic rotations and bit-plane binary addition to construct the successor, then forward iteration to the first y with F(F(y))=y. The residues were verified directly from squares. For replay, rotate the p-bit state right by each residue, add the resulting bits lane-wise, and set each output bit by comparing its lane sum to 3 or 4 respectively, retaining the input bit at equality. For each input iterate while F(F(y))≠y and increment the basin keyed by min(y,F(y)); this labels one orbit rather than counting each of its states. Every input reached the test within six updates; because the test is equivalent to period dividing two, this also excludes all longer periods without assuming the general period theorem. At p=13 the depth vector is [106,1664,3640,2314,78,234,156] and basin triples are (1,1,26),(1,5,78),(1,3888,2). At p=17 the vector is [3164,17782,69054,29376,9112,2040,544] and triples are (1,1,34),(1,29,68),(1,62323,2),(2,2,1122),(2,4,272),(2,8,136). Both unanimous masks were checked directly for their basin totals. Witness paths through time 6 are 375→574→119→62→54→34→0 and 4971→67506→1003→66482→937→640→0, with F(0)=0. This establishes the sharp F^8=F^6, F^7≠F^5 and verifies all published populations and probabilities. Inspected the frozen enumeration methods and their reference outputs; no submitted script was executed. The result is finite and asserts neither a general cutoff nor a monotone onset over primes.

## originality

PASS

The supported distinct claim is the exact labelled two-graph classification, not eventual period at most two or the known self-vote equivalence. The strongest inspected general results do not give the exact cutoff, presence/absence of temporal two-cycles, or basin spectra. The closest catalogue statements use different directed graphs and do not imply these counts. This finding is best of current knowledge, not a priority certificate.

## value

PASS

Paley-17 is the canonical maximal (4,4)-Ramsey example, and 13 is the preceding prime order in the undirected prime Paley family; comparison uses canonical objects rather than arbitrarily selected graphs. The exact spectra answer a meaningful finite dynamical question that a period bound does not answer: oscillations appear in one graph but not the other, yet the two have the same sharp transient length. The basin multiplicities distinguish the occurrence of oscillations from their exact reach under uniform initial data. These are usable finite invariants for comparing bounded-time and long-time behavior without claiming a family-wide phase transition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
