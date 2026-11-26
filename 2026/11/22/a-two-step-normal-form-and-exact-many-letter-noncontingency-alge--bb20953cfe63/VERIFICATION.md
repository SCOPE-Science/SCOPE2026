---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

With q=2^k atomic colors and pointed support data (c,S,T), a depth-one minterm homogeneity test recovers exactly T if |T|>1, and otherwise all such tests are true. In the latter case all opposite-side worlds have the identical successor set and color, so in fact all modal tests are true at every depth. For |T|>1 fix a in T: on the opposite side Δχ_b is a constant h_b, and Δ(χ_a ∧ Δχ_b) at the point holds precisely when h_b is false. These tests recover [S], including the singleton class. When |T|>1 the set of successor depth-two descriptors is then uniquely determined, including when |S|=1, so a formula induction proves stability. For each c there is one monochromatic-opposite descriptor and (2^q−q−1)·2^(q−1) others. Finite Boolean separation gives the powerset algebra at each depth. Varying valuations on K_{q,q} realizes all descriptors by repetition of colors; (c,C,C) forces at least q vertices on each side. Replacing S={c} by S={c,d} with the same non-singleton T proves sharpness. This covers k≥2 and validates the included k=1 example, with no assertion for k=0.

## originality

PASS

Pass is for the many-letter depth-two biclique classification, formulas counts and least universal biclique, not novelty of homogeneity tests, the first-layer count in other frame classes, or the one-letter boundary case. The checked literature and indexed results do not give an equivalent many-letter pointed classification or imply it as stated.

## value

PASS

The classification answers how much of either side is observable with the weaker Δ modality and gives an exact depth cutoff even with arbitrarily many letters. The two masking regimes, the Boolean algebra size and a least common finite testing frame are useful consequences of identifying the exact observable data, not just a census of small examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
