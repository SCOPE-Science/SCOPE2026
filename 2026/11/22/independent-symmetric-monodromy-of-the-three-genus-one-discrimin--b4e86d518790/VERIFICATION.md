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

The accompanying `CHECK.py` uses exact polynomial arithmetic modulo \(101\), without floating point approximation or third-party dependencies. It reconstructs each \((2,2)\) genus-one fiber discriminant using binary-quartic invariants, verifies a coefficient sample with three squarefree degree-\(24\) discriminants, and verifies a distinct A2 cusp sample whose derivative-GCD degrees are \((1,0,0)\). The first discriminant vanishes to order exactly two at the imposed cusp, while the other two remain squarefree. These certificates establish the existence conditions used in the proof in characteristic zero, because the relevant polynomial leading coefficients and subresultants are nonzero modulo \(101\). Run `python CHECK.py`.

The algebraic conclusions about irreducible critical-point incidence, two-transitivity, local cusp inertia and the product of symmetric groups are argued in `RESULT.md`; they are not inferred merely from modular samples. The theorem is not asserted for special coefficients or positive characteristic. Independent mathematical audit has not been performed.
