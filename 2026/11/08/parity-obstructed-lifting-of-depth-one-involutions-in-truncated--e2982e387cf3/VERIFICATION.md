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

PASS: Read actual frozen RESULT.md (Git blob 5895d4d358c345f351588747026513d5743276fb) and characteristic-two truncated composition checker. For f=t+a2*t^2+... with a2 nonzero, the first nontrivial term of f^2 is necessarily even: commutation of f with f^2 gives the leading obstruction r*a2*b in degree r+1, impossible if r odd. The even coefficient E_(2j) is triangular with invertible coefficient a2 on a_(2j-1), and independent of later coefficients. Thus odd-indexed coefficients are uniquely determined for full lifts, even-indexed coefficients free; N=2m jets all lift, N=2m+1 jets have exactly one codimension-one next-coefficient condition. This yields the reduced G_m x A^floor((N-1)/2) geometry and both finite-field counts for every field of characteristic two. Independently recomputed F2 truncated composition at N=2..9 (depth-one/lift counts 1/1, 2/1, 2/2, 4/2, 4/4, 8/4, 8/8, 16/8). Finite examples corroborate but do not prove infinite-field result; nilpotent or nonreduced equation schemes explicitly excluded.

## originality

PASS

PASS, best-of-knowledge: distinguishing nonliftable finite order-two jets from formal genuine involutions is a distinct question from classical torsion conjugacy. Relevant primary Lubin article sections were read; Szechtman truncation-paper title and abstract examined, full text inaccessible; Resultary semantic search finds related finite Nottingham conjugacy and other torsion, not the present all-level affine stratum/liftability ratio. No stronger implication located, but inaccessible full Szechtman text and unindexed torsion-lifting results remain genuine risks.

## value

PASS

PASS: Natural depth-one ramification stratum of finite substitution-group quotients; exact dimension, scheme reduction, and arithmetic proportion of liftable involutions answer a structured and reusable torsion-lifting obstruction question at every cutoff, not merely restating a conjugacy theorem or tiny example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
