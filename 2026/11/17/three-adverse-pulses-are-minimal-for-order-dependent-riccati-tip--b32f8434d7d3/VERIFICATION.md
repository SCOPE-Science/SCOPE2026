---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

With x=z′/z, z″=qz and initial (z′,z)=(1,1), each adverse q=−a² phase has transfer M_a=[[cos(aτ),−a sin(aτ)],[sin(aτ)/a,cos(aτ)]]. For two pulses A,B direct symbolic multiplication gives BA−AB=((a²−b²)/(ab))sin(aτ_a)sin(bτ_b) diag(1,−1), annihilated by (1,1)·diag(1,−1)·(1,1)^T. When both histories remain finite throughout exposure, terminal z>0, so the equal threshold numerators force the same x+1 sign and terminal basin. Appending a third C yields signed difference ((a²−b²)/(ab))sin angles (c+c^{-1})sin(cτ_c), generically nonzero; independently reproduced via symbolic sympy. At a=2,b=1/2,c=1 with each tangent angle 1/2, exact finite histories give terminal −6/7 (recovery to +1) vs −3/2 (post-exposure escape), with all one-pulse outcomes >−1 and no forcing-window poles. Exact post-pulse x′=1−x² basin threshold is x=−1. No claim is made about reorderings with a pole during forcing.

## originality

PASS

Riccati/projective transfer matrices, nonautonomous saddle-node thresholds and tipping contexts are classical. Longo–Núñez–Obaya–Rasmussen and Wieczorek–Xie–Ashwin concern general thresholds/rates and connecting orbits, but available main statements/abstracts do not imply the specifically sharp two-phase commutator cancellation under finite constant adverse forcing plus an exact third-phase outcome reversal. Resultary semantic searches for this phase-order basin question returned no stronger covering claim beyond the current record. Inaccessible or unindexed SL(2) identity literature remains a genuine priority risk.

## value

PASS

The invariant being classified is a dynamical basin decision rather than just the terminal numerical state. The exact universal impossibility for two arbitrary adverse phases, sharp three-pulse construction with individually harmless episodes and strict robustness, resolve a motivated minimal-complexity question about chronology-dependent irreversible tipping. The distinction between state noncommutativity and basin-threshold commutativity is a structural lemma, not an arbitrary example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
