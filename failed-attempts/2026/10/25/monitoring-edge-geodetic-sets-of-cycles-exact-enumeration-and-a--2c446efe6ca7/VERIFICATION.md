---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

On a cycle a pair monitors precisely the edges of its unique shorter arc (none if antipodal). An arc between probes that crosses an edge of an unprobed gap must traverse the entire gap, so a gap of at least n/2 prevents monitoring. Conversely all shorter gaps are monitored by their own endpoints. The empty set and singletons cannot monitor, and the short-gap bound excludes pairs. Rooting a labeled subset at any of its m probes gives the factor n/m. Deleting a probe merges two adjacent gaps. Summing the lower bounds on those merged lengths gives m(h+1)≤2n, hence only triples for odd n and at most four probes for even n. Equality in the even four-probe case forces alternating gaps and hence the antipodal pairs. For a triple there cannot be two oversized gaps: 2(h+1)≥n and the third gap is positive. This corrects the harmless strict-inequality slip in Lemma 5 for even n. The claimed counts and the cases n=3,4 follow. An independent bounded edge-deletion distance check through n=9 matched both enumerations, but is not the proof.

## originality

FAIL

The earlier unicyclic MEG-polynomial record explicitly contains the bare-cycle gap criterion, the identical labeled all-set polynomial and the same triple counts. The unmatched explicit claim, the inclusion-minimal four-set classification and count, is an immediate consequence of that earlier criterion; neither a new theorem nor a further classification ingredient is needed.

## value

FAIL

The complete labeled census is a natural object, but it was already explicitly obtained. The portion not explicitly stated in the earlier finding reduces to merging two gaps and attaining equality in their cyclic sum. In this submission that deduction does not fill a substantive remaining mathematical gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
