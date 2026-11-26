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

The matrices are row-stochastic with the asserted initial distribution and sole accepting state. Independently multiplied the full row vectors for all 27 inputs using denominator 6^4=1296. Every entry agrees with the frozen table; abc has numerator 1128, cbc has 1104, and all other words have at most 936. Thus the gap is 24/1296=1/54. A one-state stochastic matrix is [1] for every letter, so no one-state witness can give a positive gap. The result concerns the stated alphabet and the particular witness, not an optimal two-state gap. Independent replay: node /workspace/replays/5.js; the uploaded Python was inspected, not executed.

## originality

FAIL

The substantive finding A_P(abc,{a,b,c})=2, with a rational positive-gap witness, is an immediate case of a distinct indexed theorem for all block-distinct words. The frozen matrices differ and their 1/54 gap is verified, but that exact computation does not distinguish the mathematical classification claim. This establishes coverage, not chronology or authorship priority.

## value

FAIL

The shortest all-distinct ternary case is naturally motivated, but its complexity and existence of a rational positive-gap witness are already covered. The remaining fractions are scores for one chosen parameter set; there is no sharp gap threshold, extremal invariant, or demonstrated need for these precise scores. That numerical remainder does not support a distinct valuable repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
