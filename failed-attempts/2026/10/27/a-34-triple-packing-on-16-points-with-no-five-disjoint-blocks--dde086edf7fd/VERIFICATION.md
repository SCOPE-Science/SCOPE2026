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

The numerical claim, separated from its assertion of priority, is correct. Parsing the triples from RESULT.md gives 34 distinct triples on the displayed point set, using 102 distinct unordered pairs. An exhaustive maximum-clique search in the disjointness graph has optimum four. The displayed four blocks are one optimal clique. Each vertex of any 16-point system belongs to at most seven triples because their other-point pairs must be disjoint. Thus 3B <= 112, so B <= 37. The resulting interval is true but weaker than what already follows from Stinson.

## originality

FAIL

Stinson explicitly states that there is an STS(15) with largest partial parallel class of size four, hence beta(4,15)=35. Adjoin an unused point to obtain a 16-point packing with exactly the same maximum partial parallel class and 35 triples. Unused points are allowed by the frozen definition. This already gives beta(4,16)>=35. Deleting a block outside a fixed four-block matching then gives the unrestricted 34-block existence claim as well. The presentation as a one-block improvement on the prior mathematical lower bound does not survive.

## value

FAIL

The purported advance for beta(4,16) decreases, rather than increases, an available lower bound of 35. The standalone full-support 34-block witness neither resolves the gap 35–37 nor settles any motivated extremal statistic or classification beyond the previously known unrestricted existence. Substituting 35 would only restate the prior implication.

The dated certificate retains the supplied scientific assessment, sources and limitations.
