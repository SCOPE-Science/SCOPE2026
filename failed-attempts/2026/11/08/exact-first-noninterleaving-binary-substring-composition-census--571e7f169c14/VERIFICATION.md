---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

The two supplied independent C++ enumerators were inspected: each loops over all 2^23=8,388,608 linear binary words; equal exact substring-composition profiles necessarily hash together, and any nontrivial hash buckets are checked with complete exact profile vectors. Singleton and reverse-pair shortcuts are justified by reversal invariance. Direct independent exhaustive C++ counting from scratch reproduced 4096 singleton, 4191936 pair and 160 four-word fibers, total 4196192 observations, and zero hash collisions. The 24=(|s|+1)(|t|+1) factor-length argument and full four-class witness listing distinguish 152 interleaving classes and eight indecomposable ones. Finite exhaustive enumeration is a proof of THIS finite universe, not an infinite conclusion.

## originality

FAIL

Decisively already published: the 2026-10-25 full Resultary RESULT.md proves the exact same length-23 fiber histogram, optimum codebook size, 152 interleaving versus eight noninterleaving classes, and enumerates all 160 quadruples. The 2026-11-02 all-length-1-to-23 census independently contains the identical length-23 table. The later submitted package has no independent scientific claim surviving these predecessors.

## value

FAIL

Length 23 is a natural first exception and the exhaustive data are mathematically interesting, but an exact census already completely published twice, including every 4-word class and exceptional orbit. This later duplicate supplies no new needed invariant or boundary; independent reproducibility alone does not establish new contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
