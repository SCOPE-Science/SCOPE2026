---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

PASS: For the nonuniform ternary fixed point of 0→012, 1→02, 2→1, the binary Thue–Morse transition realization yields three groups of 2^j consecutive n-windows. The outer groups have odd one-count, distinct moment M1 mod n; the middle group has N1≡2 mod 4 and M1 separates all but half-turns, distinguished by odd zero count and M0. A 0↔2 interchange and telescoping transition imbalance distinguish the two outer groups. The four statistics N1,M1,N0,M0 are derived from scattered length-≤2 subsequence counts, giving ≥3n binomial classes; published p_x(n)=p_t(n+1)=3n supplies ≤3n. All j≥2; no claim outside dyadic n. Independent direct integer enumeration j=2..8 corroborates but cannot prove infinite scope.

## originality

PASS

PASS best-of-knowledge: The exact all-j ternary squarefree Thue statement concerns scattered 2-binomial signatures. Established Shallit–Shur ordinary factor complexity gives only an upper bound; binary Thue–Morse bounded binomial complexity, Tribonacci full binomial rigidity, uniform generalized Thue–Morse methods and binary Cantor results address different words/substitutions. Compared statement/implication rather than title and found no direct theorem covering the four-statistic separation. Unindexed earlier coverage remains possible.

## value

PASS

PASS: A natural canonical automatic squarefree word has infinitely many lengths at which two-scattered-subsequence data recover every literal factor; the sharp 3n exact law and four explicit fingerprints reveal nontrivial contrast with binary Thue–Morse binomial complexity. Not a single small-n check or routine known-table lookup.

The dated certificate retains the supplied scientific assessment, sources and limitations.
