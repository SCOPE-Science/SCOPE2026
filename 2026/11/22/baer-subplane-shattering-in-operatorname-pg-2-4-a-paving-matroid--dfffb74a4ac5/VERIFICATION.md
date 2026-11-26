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

A projective frame generates one Fano subplane; counting the 2520 unordered frames and seven frames per Fano subplane gives 360. Double counting with collineation transitivity gives extension counts 120 for a point, 36 for a pair, 12 for a collinear triple, 9 for a noncollinear triple, and 1 or 3 for a frame or collinear-triple-plus-point. Four collinear points cannot all be positive. For either other four-point type, the point/pair/triple extension counts dominate the union bounds for excluded positions, and inclusion–exclusion gives respectively 61 and 60 empty traces. Every <=3 support extends to a valid four-set. A five-set in one Fano plane contains the four-point complement of the Fano line through the two omitted points. That frame fixes the subplane, preventing the trace positive on its frame but negative on the fifth point. The stated basis exchange holds, and a collinear triple closes to its projective line while a noncollinear triple is itself closed, proving the rank-three hyperplane description and paving property. Matroid shellability and reduced Euler characteristic −4740 give the wedge count. Independent replay: a fresh GL(3,4)-orbit enumeration checked all trace supports through size five, the 32-leaf supplied depth-five tree as data, and the recurrence; see /workspace/branches/768b49c7-f259-4f00-bccf-ebef2e5e0463/independent_check.py. A second bounded construction tested all 116280 seven-sets and retained 360 whose intersections with every ambient line had size 1 or 3; their induced triples form the Fano plane and all 32 certificate leaves were nonempty (minimum multiplicity 1). There is also a direct upper proof: the first four queries on the all-positive branch of any full tree must be distinct (a repeated query cannot split). Their common positive family has size at most 3, but a depth-six tree would still need four realizable leaves below that prefix. Thus depth six is impossible independently of the supplied search. Neither frozen program was executed; no generalization to larger planes is inferred.

## originality

PASS

The 360 subplanes and their classical incidence parameters are not new. The quartic classification actually parametrizes the same family after passing to distinct F4-rational point sets, contrary to a literal reading of the frozen prior-work sentence about different classes; it does not characterize shattering or adaptive depth. The identical indexed frozen result is not separate evidence. The distinct same-day PG(2,3) line-symmetric-difference theorem gives the same two dimensions and an analogous support criterion, but not for these objects. The supported claim is the exact point-membership trace criterion and adaptive gap for the Baer/Fano subplane family, with the matroid/topology interpretation as a consequence.

## value

PASS

These are canonical embedded Fano subplanes in the smallest nontrivial Baer-subplane setting, and fixed supports versus adaptive point queries test genuinely distinct information. The exact classification proves a sharp gap for this natural family, not just a count of configurations; the independence complex has a concrete rank-four paving description. Both the witness and analytic upper bound identify the precise five-round cutoff, with potential use as a finite-geometric benchmark without an all-orders claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
