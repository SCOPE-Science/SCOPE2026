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

Write b=bρ, s=b/ρ and use y=r/b. The energy integral has prefactor √(ρ/g). On 0<y≤1, the scaled center arclength Q is comparable to y^(1/a), Q'/Q=O(1/y), and the relative difference of the scaled height factor from Q² is O(y^((a−1)/a)+s²y^(2/a)). Subtracting the reference integrand Q'/√(η²+Q²) therefore costs O(1) uniformly even as η tends to zero; the reference integral is arsinh(Q(1)/η)=log(1/η)+O(1). Outside b the relative perturbations are O(ρ r^(-(a−1)/a)), giving integrated error O(ρ b^(-(a−1)/(2a)))=O(√(ρ/g)); the omitted point-particle integral up to b is of this same order. Applying these bounds at each positive level and inverting the increasing hitting times gives compact-time uniform convergence of the clipped paths, including T=0 and T=∞. Contact holds locally since the offset curvature is at most both κ_a and 1/ρ; these bounds give Hρ κ_q=O(r^(2/a)) and v²κ_q≤g(b/ρ)². N in the proof is the magnitude of the outward support force, despite the wording ‘inward normal reaction’.

## originality

PASS

The specific addition supported by the checked sources is the uniform two-scale first-passage estimate for positive apex speeds, and the ensuing deterministic selection of every delay by a vanishing launch. Neither offset geometry, exact-rest uniqueness at fixed radius, nor the delayed point-particle paths themselves are new here.

## value

PASS

The result reconciles fixed-radius uniqueness with point-particle nonuniqueness using an explicit physical perturbation. It distinguishes vanishing launches selecting immediate departure, arbitrary finite delays, and remaining at rest in the limit, with an error uniform over the relevant launch speeds. Exact-rest divergence alone cannot make that distinction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
