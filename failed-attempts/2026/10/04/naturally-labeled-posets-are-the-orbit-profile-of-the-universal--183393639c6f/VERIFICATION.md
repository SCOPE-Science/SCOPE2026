---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The formulas are correct. Ultrahomogeneity gives one injective tuple orbit for each labeled finite ordered-poset structure. There are n! choices for the distinguished linear order, and after relabeling increasingly there are exactly s_n naturally labeled partial orders, so a_n=n!s_n. Counting instead by the underlying labeled poset gives the total number of linear extensions. For tuples with repetitions, an equality partition with k blocks together with an injective k-tuple orbit gives the Stirling transform. The Kleitman--Rothschild asymptotic follows because the total linear-extension count lies between the labeled-poset count and n! times that count. Independent small-arity enumeration reproduced A006455 through six points and the first orbit-profile values.

## originality

FAIL

Originality fails because the main profile formula is a routine consequence of the defining Fraisse-homogeneity property and a classical enumeration. For an ultrahomogeneous relational structure, injective tuple orbits are exactly the isomorphism types of the induced labeled finite structures. Here those structures are finite posets together with a distinguished linear extension. Choosing the linear order gives n! choices and the compatible partial order is counted by the classical sequence A006455. The equivalent sum of linear-extension counts is already the standard double-counting interpretation recorded with that sequence. The repeated-coordinate formula is then the ordinary Stirling transform by equality patterns.

## value

FAIL

The identification is tidy, but it is a direct application of the defining orbit-age correspondence for an ultrahomogeneous structure to a classical counting sequence. The repeated-coordinate transform and asymptotic are routine consequences. Under the required value standard this is an elegant reformulation, not a sufficiently distinct mathematical gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
