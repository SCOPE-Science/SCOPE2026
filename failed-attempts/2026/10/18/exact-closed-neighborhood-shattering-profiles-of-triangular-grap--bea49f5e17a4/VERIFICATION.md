---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

A closed-neighborhood trace on the selected edges is the union of the two endpoint stars of its center. The empty trace needs two unused labels; they also allow padding any trace that uses fewer than two stars. Each singleton trace forces a leaf endpoint, hence all components with edges are stars. The full trace places a limit of two components. Three selected leaves in a larger star need three centers; two selected leaves from a three-edge star together with an edge in a second component do too. These exclusions and the star-center/leaf realizations give precisely the six types and both directions of the classification. The placement factors are 1, 3, 3, 4, 30 and 90, with 90 obtained by choosing an unordered split into two triples and a center on each. The two-extra-label condition gives the stated thresholds; the empty support is shattered for all n>=2 since a center exists. The comparison to the open J(7,2) example is supported by the primary source. An independent direct comparison of all traces on supports of size at most five for 2<=n<=8 checked 155,989 supports, including the jump from zero shattered four-sets at n=7 to 2520 at n=8. The supplied script and verification notes were inspected, not executed. The proof, not the bounded replay, gives the all-n ceiling.

## originality

FAIL

A distinct Resultary entry contains the identical closed-neighborhood support criterion, complete coefficient profile and VC sequence. Distinctness for this whole Finding is therefore not established; its comparison with open neighborhoods is also not a surviving separate claim (the open example is prior work, and the closed threshold is in the match). This is an actual same-regime comparison, not an inference of earlier priority from a catalogue date. The primary literature inspected does not by itself establish prior exact coverage of the closed result.

## value

PASS

The mathematical classification is intrinsically useful: it gives all shattering witnesses and a complete labeled profile for a natural graph family, and it isolates why adding the center changes the exact VC threshold. The failed originality assessment records that these useful facts do not distinguish the submission from the matched catalogue theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
