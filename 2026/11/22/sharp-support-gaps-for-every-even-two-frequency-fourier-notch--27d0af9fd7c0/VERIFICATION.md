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

Reconstructed the global witness proof in RESULT.md §§1–5. F_k(x)=(-1)^{k/2}T_k(x). On the first negative-cosine lobe, the derivative of −cos(t)/sin(t/k) has the sign of g_k, with g′_k=(1−k^{-2})cos(t)sin(t/k)<0 and opposite signs at π/2 and π. Thus there is exactly one positive maximizing contact there; if k≥6, all later negative lobes have t≥5π/2, and their ratio is strictly smaller than h_k(π) by denominator monotonicity on the allowed range. For k=4 no later negative lobe occurs. Strict decrease of F_k(u)−λ_k u on [0,sin(π/(2k))] gives exactly the left contact. Integration against any positive measure after rotating its complementary support arc forces the contact fibers, excluding any longer gap by the first cosine moment. At the sharp gap the first cosine moment fixes both positive totals, the polynomial witness enforces the kth cosine moment, and the opposite nonzero kth sine signs make the sine matrix nonsingular. Hence the stated four-point measure attains the bound and is rigid. Uniformly on [π/2,π], k g_k(t)=t sin t+cos t+O(k^{-2}); the limiting root is simple. This gives t_k=t_*+O(k^{-2}), λ_k/k=L+O(k^{-2}); the equation for a_k=k arcsin r_k has uniformly O(k^{-2}) error and a simple limiting root, giving the claimed O(k^{-3}) for G_k. Independent 60-digit evaluations agree with the displayed a_*, G₄, G₆ and G₈. The inspected Python checker covers finite meshes and includes k=2 only as a diagnostic; its hardcoded G₄ benchmark differs from the actual 2.569356100631680534… by about 2×10^{-13}, well within its explicit tolerance. No script run or numerical mesh was used as a proof.

## originality

PASS

The supported new scope is the uniform even family beginning at k=6, its rigid optimizers and high-harmonic law. The revealed same-day {1,4} match is exact at k=4 and explicitly credited by the audited record (which names the other result ID in its frozen audit); it is not counted as new. The statement comparisons do not establish an antecedent for the uniform new claim. Older extremal trigonometric papers remain genuine access risks.

## value

PASS

The exact feasible support gap for two prescribed Fourier zeros is a natural sparse quadrature invariant. The uniform first-lobe argument determines it and all extremizers for every even degree, not merely a tabulated low-degree substitution. The limiting approach to a semicircular gap with an exact leading coefficient and the four-node rigidity make the classification useful for comparisons across harmonics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
