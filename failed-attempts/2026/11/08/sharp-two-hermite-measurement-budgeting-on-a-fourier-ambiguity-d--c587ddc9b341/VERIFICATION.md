---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
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

The assigned Gaussian and h1 short-time Fourier ambiguity integrals indeed give e^{-s/2} and (1-s)e^{-s/2}; pointwise two-channel singular value squared F_w(s)=e^{-s}(1+w(s²-2s)). Its derivative has no interior minimum for w<=1/2, and for w>1/2 it has one interior local minimum s_-=2-sqrt(2-1/w), competing monotonically with outer radius T. At T=2, exact optimizers w∈[0,1/2]; T>2 a unique crossing gives given implicit equation and asymptotics. Independently algebraically checked the precise correspondence with the earlier October 25 theorem under u=2-a; validity of these calculations does not imply originality.

## originality

FAIL

FAIL: The complete submitted objective, optimization over all T>0 and w∈[0,1], equality set, unique optimal interior weight, balance equation and large-radius asymptotics were already proved in the published October 25 Resultary theorem. Its input disk R and lower bound μ_R(w) are exactly this Gamma(T) with R=T, and its u_R=2-a_T. A second November 8 full result independently reproduces the same classification. The identical same-claim archive cannot be counted as novelty.

## value

FAIL

FAIL: Although sharp allocation for two Hermite windows is naturally motivated and would be valuable if new, this submission only reproduces the complete earlier exact threshold/weight/equioscillation theorem under a renamed stationary parameter. It adds no independently useful structural lemma, stronger hypothesis range or substantive exact fact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
