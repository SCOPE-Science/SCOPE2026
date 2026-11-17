---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Real symmetric Laplacian decomposes into 0 constant vector, radial (m+1)t vector, Fourier rim pairs with eigenvalues t+nu_j, and even Nyquist singleton. Strict monotonicity of nu_j isolates all positive collisions mt=nu_j. PBH restriction to chosen coordinates gives Fourier-pair determinants sin(2*pi*j*d/m), gcd(q,d)=1 and even alternating parity; radial plus resonant double Fourier pair forms a 3-dimensional eigenspace needing 3 controls. Hub+two rim and three rim choices are classified by rank-3 determinant (unit-circle points distinct) and simultaneous Fourier rank-2 gcd constraints. Independent exact SymPy Kalman ranks for m=3,4,6,7 and specified rational weights confirm minimum counts and placement conditions, including m=3 and t=4/m; modular scripts only supply finite corroboration, not proof for irrational weights.

## originality

PASS

Best-of-knowledge original remainder: the complete minimal actuator budget as a function of spoke weight, and ALL size-three configurations at double-mode resonance, including both hub+two-rim and triple-rim modular criteria, are not given by the inspected prior two-rim rank theorem or by cycle/path PBH references. Substantial prior coverage acknowledged: the 2026-11-02 published theorem already gives exact two-rim controllability ranks, every isolated resonance and all size-two placement criteria. These portions are NOT new. The genuinely additional three-input classification and 2-to-3 optimum transition with attainability survive direct implication comparison.

## value

PASS

For a natural symmetric weighted network, exact minimal independent control budget and complete configurations at isolated eigenvalue-resonance thresholds are structurally meaningful, not a restatement of generic PBH. The 3-input geometric-arithmetic criterion determines feasible optimal placements and phase transition omitted by the earlier complete 2-leader rank study; is useful for exact network-actuator design. No claim to nonuniform spokes or shared control.

The dated certificate retains the supplied scientific assessment, sources and limitations.
