---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification record

The supplied `RESULT.md` proves the unconditional perimeter sampling law by three disjoint, exhaustive endpoint-side assignments. It derives exact conditional moment integrals and explicitly inverts the three raw moments to recover area, the elementary symmetric functions of normalized side lengths, and finally the scale using Heron's identity. An exact two-moment counterexample and the boundary-attainment arguments complete the scope. This proof—not computational testing—supports the all-triangle assertion.

## Actual reproducibility checks

Execute `python3 check_area_moment.py` with standard Python 3; no third-party dependencies are needed. The checker evaluates the universal all-distinct-side moments by exact rational polynomial integration through orders one to six, checks the two-on-one-side moment formula, verifies normalized triangle-ratio and exact inverse-minimality calculations, and independently simulates 400,000 triplets on each of four actual Euclidean triangular perimeters. On the reviewed copy the checker returned `VERIFY_OK exact_moment_orders=1..6 configurations=4 simulation_trials=1600000`; the exact conditional moments were \(1/4\), \(1/12\), and \(5/144\). The witness first moments both equaled \(4/25\), second moments both equaled \(4/75\), and third moments differed by \(1/50625\). Monte Carlo comparisons use finite sampling and a predefined tolerance; they are diagnostic rather than infinite proofs.

## Limits and provenance of components

The different-edge conditional area distribution is known from Maesumi, arxiv:1804.11007, and is credited. The claim adds the same-side and two-on-one-side patterns to establish the complete perimeter law and moment-based inverse reconstruction. The result requires nondegenerate Euclidean triangles and exact population moments. No uncertainty/stability estimates or higher-polygon identification are proved. Independent mathematical audit has not been performed; historical priority remains provisional.
