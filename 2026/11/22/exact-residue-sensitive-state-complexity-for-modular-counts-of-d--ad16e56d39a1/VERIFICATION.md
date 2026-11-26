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

With the empty subsequence included, the shifted ending counts start at (1,1), undergo the two determinant-one shears, and output x+y−1. Positive coprime lifts exist for every primitive vector by CRT avoidance of the finitely many prime divisors of the chosen second lift; subtractive Euclid gives all reachable vectors and, with word order reversed, all primitive suffix rows. In a basis beginning with v, rows taking values (1,0) and (1,1) distinguish v from any unequal w for the residue-0 predicate. For the residue-−1 predicate the primitive annihilator (−v₂,v₁) identifies exactly the unit multiples of v; freeness and the prime-power counts give the stated projective count for composite as well as prime m. Pure-letter suffixes of length m−1 recover each coordinate of a Moore state separately. This covers m=2, the empty input, and complete machines. A separate bounded check minimized all three machines for m=2 through 8 and compared prefix outputs against explicit subsequence sets through word length 6; it is corroboration, not the all-m proof.

## originality

PASS

Best of available evidence: credit the known binary-word/coprime-pair correspondence and the related primitive-vector analysis for a constrained language. The supported distinct result is the exact residue-sensitive minimal-recognizer comparison, including the unit-projective collapse and its contrast with the full output machine. No inspected prior statement or implication establishes that comparison.

## value

PASS

Two adjacent predicates for the same natural streaming count require state spaces separated by the unbounded factor φ(m). The exact primitive-versus-projective distinction explains why, supplies optimal complete recognizers at every modulus, and gives the full-output memory requirement. This is not just an effective modular recurrence or a restatement of the cardinality of a projective line.

The dated certificate retains the supplied scientific assessment, sources and limitations.
