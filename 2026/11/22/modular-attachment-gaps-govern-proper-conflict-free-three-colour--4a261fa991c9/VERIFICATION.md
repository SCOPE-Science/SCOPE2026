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

With a vertex and parent fixed in three named colours, the permitted assignments to children are either all in the third colour or exactly one in that colour; merge these when there is one child, and handle no children separately. This gives b(d). With the cycle fixed, equal cycle-neighbour colours require exactly one child in the third colour (t_i choices), and distinct colours require monochromatic attachments (two choices if nonempty, one if empty). The tree recursion is a bijection and the sign sum counts exactly the proper cycle assignments with these weights. Unattached vertices force the edge increment to remain constant. Each nonzero gap contributes freely +1 or −1 modulo three and these can sum to zero via opposite pairs or an equal triple unless there is exactly one. Two colours cannot provide a witness at a cycle vertex. The length-3 and length-4 core blocks have distinct consecutive triples even across joins; on a decorated C5 rotate (1,2,3,4,2) so its only equal-neighbour vertex has a child available as a witness. Outward extension with children different from the vertex and parent preserves a singleton parent colour. Independent direct checks matched N₃=6 and 0 for adjacent and distance-two C5 leaves, and 12 and 36 for two C6 examples including a branched tree; the obstructed C5 example had 288 valid four-colour assignments.

## originality

PASS

The verified overlap is the old tree/bare-cycle and corona chromatic information, and the exact census on uniformly hairy cycles. The part supporting the pass is the exact modular obstruction for arbitrary nonuniform attachment positions together with the three-colour census for arbitrary attached rooted trees. The strong-odd citation in RESULT.md should not be described as a stronger condition implying PCF: it permits odd multiplicities greater than one. This attribution issue does not affect the explicit four-colour PCF construction or the distinctive three-colour results.

## value

PASS

The attachment-position obstruction is a natural exact colouring invariant and distinguishes equal-size and equal-degree-multiset examples. It applies across arbitrary rooted trees, and the local factorization gives exact polynomial-time three-palette counting rather than only an existence bound. Neither the four-colour construction alone nor the uniform leaf subfamily is the value claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
