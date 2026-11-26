---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Nonempty self-inverse partial maps have equal affine domain and image. On each domain the map is I+N with translation b, with N²=0 and Nb=0. The image–kernel flag and induced isomorphism give T(k,r) without multiplicity; solvability of Nx=b gives exactly 2^r admissible translations with fixed points. Including the empty map and taking the rank variable as domain cardinality gives the polynomial. An independent pointwise enumeration through internal dimension 4 matched every stratum; at k=4 the strata by fixed-point count 0, 4, 8, 16 were 645, 840, 210, 1. The normalized affine-involution weights are a_s P_k/P_r at s=k−2r. The Euler product F(u) has F(−1)=0, F(1/2)=F/2 and F(−1/2)=P∞, giving the parity split. Summable domination of a_c P_d/P_{d−c} h_{d−c} gives the codimension law and total constant. Taking even and odd d subsequences separately, the two limits of the fixed-point-free fraction both equal one-half, since the limiting even/odd codimension masses are equal. The independent branch did not execute the frozen verify.py; enumeration is corroboration, not a proof of the limits.

## originality

PASS

The finite joint enumeration is covered as a coefficient extraction from Fripertinger’s broader affine cycle index followed by the standard affine-domain count. Do not claim new priority for those finite numerical data. The supported distinct result is the asymptotic codimension distribution and two-level parity cancellation, including the total constant and global limit. The inspected prior-cycle-index and linear-involution statements do not supply these limits by specialization.

## value

PASS

The new limiting information concerns the natural uniform ensemble of self-inverse partial affine symmetries. It explains why the partial-map sampling law has half density even though the full-domain probabilities have two different limits, and specifies the nondegenerate limiting distribution of the missing dimension. This goes beyond re-extracting finite cycle-index coefficients.

The dated certificate retains the supplied scientific assessment, sources and limitations.
