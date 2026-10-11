---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

Conditional on the Fan--Li torsor presentation quoted by the assigned package, the Chow calculation is correct. A vector bundle and a Zariski-locally-trivial affine-line bundle induce Chow-ring isomorphisms with the base, giving \(\operatorname{CH}^*(W)\cong\mathbb Z[h]/(h^n)\) and the same for \(F\). If \(H_0\) is the zero divisor of the tautological section of \(L=\mathcal O(-1)\), then \(\mathcal O_W(F)=\rho^*L\), so \([F]=-h\) and the normal bundle is the restriction. The stated powers and Picard conclusion follow.

## originality

FAIL

The assigned record itself identifies Fan--Li Proposition 3.6 as giving \(H=\operatorname{Tot}(L\oplus Q)\), a Zariski-locally-trivial affine torsor \(W\to H\), and the scheme-theoretic pullback description of \(F\). Those published structural statements, together with standard Chow homotopy invariance and the zero-divisor line-bundle formula, mechanically imply every novelty-bearing clause. Under implication-based originality, a result need not be printed verbatim to be covered.

## value

FAIL

The computation is useful bookkeeping, but after the published affine-torsor presentation is known it is a direct application of textbook homotopy invariance for Chow groups and the elementary divisor-line-bundle identity for a zero section. Under the common value bar this is a routine formal consequence of the published geometry rather than an independently substantial intersection-theoretic gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
