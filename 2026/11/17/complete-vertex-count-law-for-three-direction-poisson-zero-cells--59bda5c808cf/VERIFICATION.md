---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

PASS. Independent offset Poisson processes give six independent Exp(lambda_i) nearest signed gaps. Since n1+n2+n3=0, each upper facet disappears precisely on E_i={A_i>B_j+B_k}, and each lower disappears on F_i={B_i>A_j+A_k}, equality events having probability zero. For each nonempty I, conditional Laplace integration over the B_j gives b_I; E_i with F_j for i≠j are mutually exclusive, whereas E_i and F_i use disjoint variables and contribute b_i² as the only mixed two-facet removal. Inclusion-exclusion yields the four displayed probabilities, N∈{3,4,5,6}, and E[N]=6-2u1. Independently recomputed exact equal-rate b_single=1/4, b_double=1/12, b_triple=1/27, s=3/16, resulting in (2/27,67/144,25/72,49/432) and mean 9/2. The geometric reason is exact; finite Monte Carlo in the inspected checks/verify.py is corroboration only.

## originality

PASS

Best-of-knowledge PASS for the complete zero-cell four-type law for arbitrary three positive rates. The highly relevant Heerten–Hübner–Thäle theorem is for the typical cell; its probability weights cannot simply be reused for the area-weighted origin cell. The published isotropic Crofton zero-cell study is a different direction distribution.

## value

PASS

PASS. A complete arbitrarily anisotropic four-point discrete distribution of a natural planar Poisson zero cell provides a substantive stochastic-geometry invariant. It distinguishes the area-biased zero-cell law from the independently well-studied typical-cell distribution, and the exact mixed facet-redundancy term is nontrivial. This is not simply a known-cell table recomputation or a tiny numerical gain.

The dated certificate retains the supplied scientific assessment, sources and limitations.
