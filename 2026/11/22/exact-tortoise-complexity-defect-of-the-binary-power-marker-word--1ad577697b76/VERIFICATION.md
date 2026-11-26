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

There is one zero word and every offset of an isolated one occurs; all n weight-one words have the same image. For a factor with at least two ones, the second one is at offset r+2^j where j is the first marker index and r is the first-one offset. Excluding the preceding marker gives 0≤r<2^(j−1) when j≥1, while j=0 forces r=0 by the one-sided boundary. The word is fixed by (j,r). The image's first one is at offset r+2^j−1 by the one-step stack rule: the leading zeros and the first internal zero block are emitted before the first one is popped. Its allowable offset intervals [2^j−1, 3·2^(j−1)−2] for j≥1 and {0} for j=0 are disjoint. Thus the image recovers (j,r), and weight preservation separates all three classes. For n≥2 and k=floor(log₂n), j<k contributes 2^(k−1) factors including j=0; j=k contributes min(2^(k−1),n−2^k); larger j contribute none. This gives M(n), including dyadic endpoints, hence the stated counts and difference. For n=1 both letters are fixed. A separate literal-stack simulation on complete finite window sets corroborated every length 1 through 256 (`cd /workspace && python3 power_marker_reproduction.py`); the interval argument, not that simulation, establishes the all-length claim.

## originality

PASS

The distinct claim is the exact tortoise-image complexity, its size-n fiber and its linearly unbounded defect as a boundary example. The ordinary factor-complexity formula is a baseline already covered by growing-gap theory and does not receive independent novelty credit.

## value

PASS

The source is an explicit linear-complexity witness that bounded one-gaps cannot simply be deleted from the uniform-defect theorem. Quantifying the full loss and its sole collision fiber at every length explains the failure rather than merely exhibiting sporadic large deficits. The result is specific to one step and one source, not a general converse.

The dated certificate retains the supplied scientific assessment, sources and limitations.
