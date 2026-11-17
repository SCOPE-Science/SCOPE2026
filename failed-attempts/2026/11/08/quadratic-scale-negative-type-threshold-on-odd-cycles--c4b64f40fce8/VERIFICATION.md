---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For every odd n>=5 the powered cycle distance matrix is circulant, with nontrivial Fourier multipliers Lambda_j(p)=2*sum_{r=1}^{(n-1)/2} r^p*cos(2*pi*j*r/n). The exact p=1 formula is negative on every frequency, with even j approaching -1/4 and odd j diverging negative. Linearization for p=1+t/n^2, a uniform Fourier-tail bound, and fixed-frequency integration show that j=2 first obstructs at K=2*pi^2/integral_0^{2*pi}(1-cos u)/u du = 8.0976273568..., while all modes stay negative below this scale. This proves n^2(wp_n-1)->K and the Hilbert snowflake/positive-kernel equivalents. The separate comparison to ordinary four-point roundness correctly concerns a different invariant. Independent numerical Fourier checks verified exact p=1 multipliers and a second-mode obstruction for n=11,41,101; they are not the all-mode proof.

## originality

FAIL

The complete principal theorem is already established by the dated November 1, 2026 published result Sharp asymptotic negative-type exponent of odd cycle metrics. It uses the same shortest-path odd-cycle metric, identical supremal negative-type definition, exact n^-2 law with the same cosine-integral coefficient, and proves both the second-mode obstruction and all-other-mode nonpositivity. A still-earlier October 26 publication established the single-frequency part. Renaming wp_n, including Schoenberg equivalents, or comparing with known ordinary-roundness asymptotics does not create an independently original finding.

## value

FAIL

The exact sharp exponent would be mathematically valuable as a first determination, but here it has already been established in the same natural objects and parameter range. The remaining four-point-roundness comparison is routine division of published asymptotics and is not a separate motivated unknown invariant or meaningful classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
