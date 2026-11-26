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

Reconstructed RESULT.md lines 34–63 for a type-one seed and column-parent means. With f=R_u/R_0, det(aI−M)=−uD and the smaller eigenvalue is below a; the larger is Perron, including u=1 by nonnegative irreducibility (the proof's wording 'positive matrix' is imprecise at u=1). The positive Perron amplitude gives the advertised tail sign when D≠0. The derivative of f has at most one zero since it is a sum of two distinct real exponentials. In the B=0 case Cayley–Hamilton gives f''(0)=uD; for D=0 the trajectory is constant or a constant plus one decaying exponential. These facts cover all strict, zero, and competing signs and give the unique crossing when claimed. Inverting I−M under D<0 gives the excess sign b(1−a+c)−a(1−d); crossing the positive endpoints of the interval for b gives c<a−d exactly. The integrated difference rises and then falls strictly to that resolvent excess, including strict finite-time positivity in the zero-limit case. Lifetime integration equals expected progeny by Tonelli and the mean-one lifetime of each newborn. Replayed the printed rational witness by direct determinant/resolvent algebra and independently bisected f−1 on [1,15], obtaining 6.658067198520774. Inspected checker.py and VERIFICATION.md without executing them; finite tests are illustrative, not the classification proof.

## originality

PASS

On the evidence inspected, the supported addition is the full parameter classification of crossing and cumulative ordering for this seeded displacement family, with the sharp wedge for opposite spectral and total-progeny rankings. The practical qualitative displacement effect, Perron/resolvent methods, and two-exponential representations are not themselves original.

## value

PASS

Separates three naturally competing quantities—initial activity, asymptotic reproduction, and cumulative volume—in a motivated two-channel model. The sharp intensity-independent wedge and finite-horizon sign law, including a nonzero transient excess at equality of total means, are more informative than a single engineered example. Value is mathematical and does not establish effects of a real platform policy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
