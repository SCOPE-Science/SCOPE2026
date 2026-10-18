---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Every proper nontrivial subgroup of H=C_(p^2)xC_p has order p or p^2. The unique E=H[p], p order-p^2 cyclic subgroups with common P, and p other order-p lines yield a K_(p+2) clique plus p pendant vertices at E. A zero-forcing initial blue set must omit at most one leaf and one noncentral clique vertex; this is also sufficient since p>=2 supplies a blue leaf to force the center if needed. White complement generating polynomial (1+pt)(1+(p+1)t)(1+t) reverses to u^(2p-1)(u+p)(u+p+1)(u+1). Independent full subset enumeration for primes 2,3,5,7 verifies classification and coefficients, with arbitrary-prime algebraic proof.

## originality

FAIL

Boyer, Brimkov, English et al, The zero forcing polynomial of a graph (2018 preprint, published 2019), primary FULL text Section 4.2 Theorem 10 classifies zero forcing sets of EVERY threshold graph and Theorem 12 derives every zero forcing polynomial. A (p+2,p) pineapple is the threshold graph of 1^(p+1) 0^p 1. Applying their Theorem 10 forces at most one omitted vertex from each of the three blocks and its second condition is automatic for p>=2, giving exactly the submitted white-set classification and polynomial. This is decisive mathematically stronger prior coverage even without the word pineapple in title or formula.

## value

FAIL

The submitted complete polynomial and forcing set classification are an immediate special case of an established all-threshold-graphs theorem; the subgroup-to-pineapple identification is straightforward from standard p-group subgroup counts. There is no independent unknown invariant or genuinely nonroutine structural gap surviving the general prior theorem. Correctness and independently rerun code do not rescue value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
