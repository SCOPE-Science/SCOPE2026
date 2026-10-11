---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

With all chain coefficients zero, source equations (4.24)--(4.25) give \(A+B=0\) and \(Ae^{ik}+Be^{-ik}=0\), hence \(\sin k=0\) for a nonzero loop amplitude. At \(k=n\pi\), equation (4.27) reduces exactly to \(e^{i(\alpha_2-lpha_1)}=(-1)^n\); the \(\delta\) term vanishes because the common vertex value is zero. Conversely \(\sin(n\pi x)\) on a single loop satisfies the boundary system when that phase condition holds. The zero-energy Dirichlet solution is trivial. Translation invariance supplies one mutually orthogonal compactly supported eigenfunction on every loop, giving countably infinite multiplicity. The exact verifier checks both parity roots through \(n=20\).

## originality

FAIL

The primary paper prints the exact four boundary equations used here, including the condition that the relative phase \(\alpha_2^i-\alpha_1^i\) is constant along the graph. Setting all chain amplitudes to zero and imposing support on one loop reduces those equations in a few algebraic steps to Dirichlet loop momenta and the displayed phase parity. Thus the scientifically relevant statement is implication-level covered by the published boundary system even though the paper does not isolate it as a named parity theorem.

## value

PASS

The exact phase selection identifies singular compact localized levels that can be obscured by eliminations dividing by Dirichlet factors, and the resulting infinite multiplicity is spectrally meaningful. The record is rejected for prior implication, not because the localized-state boundary is mathematically unmotivated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
