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

This is ordinary, integral, regular path homology of the chain subcomplex ker(1+tau), for the stated bidirected factors of lengths at least five and r≥2. The signing makes exactly the first factor a connected doubled cycle. In a cycle, a nonalternating path gives a forbidden shortcut in its regular boundary; the position of the only forbidden pair and its unique common neighbor force a unique preimage. Hence only the two alternating paths per edge contribute in degrees ≥2. Explicitly, in degree p≥1 take a_p and k_p, where k_p=a_p+b_p for odd p and a_p−b_p for even p. This basis is unimodular; d k_p=0 and d a_p=±k_(p−1) for p≥2. Pairing these latter basis elements contracts the tail by the same rule on every oriented edge. This leaves the ordinary cellular cycle, equivariantly. Fu–Yau Theorem 2.7 supplies an integral natural chain isomorphism for the marked box product, which here gives precisely the Cartesian graph edges. The deck operation acts only on the first factor, and the other chain modules are free, so the integral anti-invariant subcomplex is the tensor of the first anti-invariant factor with the others. The m1−1 difference columns identify its cellular vertices and its seam column is −2 on the remaining generator. Tensoring this two-term model with the remaining zero-differential rank-one degree 0 and degree 1 generators yields one shifted multiplication-by-two pair per subset of the r−1 untwisted directions, proving the asserted ranks, absence of other homology and real vanishing. In contrast, the deck translation acts trivially on ordinary cover homology via the equivariant cellular model.

## originality

PASS

Credit the exact known degree-zero result and the standard sign-local-system computation on a topological torus. The supported distinct result is the integral path-chain comparison and resulting simultaneous positive-degree calculation for this graph family. Its closest earlier signed integral path theorem has a girth hypothesis for degree one that the toroidal products violate, and the real anti-invariant comparison cannot determine integral torsion. The integral shuffle is a known essential input, not itself new.

## value

PASS

The seam signing on products of long cycles is a natural test of how the signed integral path complex behaves in the presence of coordinate squares, beyond known girth-based low-degree formulas. The complete all-dimensional calculation exhibits a chain-before-homology torsion effect invisible both in real coefficients and in ordinary cover homology. Its useful content is the explicit equivariant integral reduction and exact family computation, not the textbook twisted-circle tensor count in isolation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
