---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

The strictly increasing consecutive-one gaps g_j=(b−1)b^j uniquely identify any occurring two-one core. The one-sided initial pre-gap is l0=1, and later left-zero spans are g_(j−1)−1, giving exact minimal overhangs. Any MAW with >=4 ones would have two occurring maximal factors sharing at least two ones and hence the unique occurrence, contradiction; the three-one case gives only b=2 and b=3 exceptions. Counting pair-gap and boundary families yields the stated exact M_b(N) and N+log_b N+O(1); intersecting with 10*1 proves nonregularity via unbounded geometric gaps. Fifteen independently coded b=2..6 finite-prefix MAW set comparisons through N=20 matched predictions; finite testing is not an infinite proof.

## originality

PASS

Best-of-knowledge PASS for uniform base b>=2 explicit infinite MAW language, exact cumulative count and nonregularity. Entire b=2 statement is already independently published, including identical exceptional boundaries, and must not be presented as novel. No inspected predecessor states the b>=3 classification or the b=3 and b>=4 boundary transition; finite RLE algorithms do not provide the claimed exact infinite specialization without extra mathematics. Search non-detection is not priority proof.

## value

PASS

PASS: minimal forbidden factors describe the exact obstruction language of a naturally defined sparse infinite word; extending dyadic b=2 to every integer b includes genuinely different initial patterns and a simple exact logarithmic correction and nonregularity. These are useful structural and enumeration facts, not a routine reindexing of the dyadic theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
