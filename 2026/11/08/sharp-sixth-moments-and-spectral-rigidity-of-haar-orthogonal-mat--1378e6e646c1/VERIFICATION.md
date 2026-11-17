---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

PASS: For full Haar O(n), n>=3, 1<=k<=n and all nonzero real n-by-k coefficients, the 15-pairing sixth-order Weingarten inverse was reconstructed exactly using the three cycle-component types (3,2,1). Contracting gives E F^6 =15[(n^2+3n-2)S^3-6(n+2)ST+16U]/[n(n-2)(n-1)(n+2)(n+4)] with S=tr G,T=tr G^2,U=tr G^3 and E F^2=S/n. On normalized squared singular values x_i, the submitted two exact pairwise nonnegative deficit sums show rank-one minimum and k-equal positive singular-value maximum, with strict equality geometry. Averaging an arbitrary Euclidean comparison quadratic over O(n) times O(k) proves the Frobenius ellipsoid optimal and the Banach–Mazur formula, including k=1 and k=n boundary cases. Independently inverted the symbolic 15x15 pairing Gram matrix in exact arithmetic; finite integrations are corroboration rather than proof of all n.

## originality

PASS

PASS best-of-knowledge: Gorin and Collins–Śniady provide the underlying orthogonal Weingarten calculus and even a specific entry of its sixth-order inverse, but the full coefficient-space sharp two-sided sixth norm geometry, spectral equalities, two deficits and optimal Euclidean distortion were not supplied in their inspected full texts. The matching Resultary item is the same source blob and not independent prior art; unitary/Sp analogues integrate different Haar spaces.

## value

PASS

PASS: The rectangular real Stiefel manifold and first-order linear statistics are canonical in random matrix theory. A sharp rank-dependent all-coefficient norm range plus exact equality classes and Banach–Mazur invariant are useful independently of merely computing a Weingarten coefficient; both rank-one and equal-spectrum endpoints are structurally characterized for every n,k.

The dated certificate retains the supplied scientific assessment, sources and limitations.
