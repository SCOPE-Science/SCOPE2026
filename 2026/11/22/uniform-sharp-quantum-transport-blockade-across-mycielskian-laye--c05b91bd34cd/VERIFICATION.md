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

Regularity gives invariance of the normalized original and shadow layer sums with the hub; no transitivity or connectedness of the base is needed. In the order original–shadow–hub the symmetric tridiagonal compression has diagonal (r,0,0) and off-diagonal (r,√n). Its characteristic polynomial is (z−r)(z²−n)−r²z; its corner resolvent cofactor is r√n, so the residues give the actual full-layer amplitude. The two outer residues are positive and the middle is negative; their sum is zero since the off-diagonal resolvent is O(z⁻³). The triangle bound 4c₀² therefore holds at every time, with no phase-alignment assumption. Weyl bounds first locate the middle root in O_r(1), and the characteristic equation then gives λ₀=r+O_r(n⁻¹). For the outer roots the scaled polynomial at ε=n⁻¹ᐟ² has simple roots ±1 at ε=0 and zero first derivative there; this yields λ±=±√n+O_r(n⁻¹ᐟ²). The residues then give the upper constant 4r²; at π/√n the outer phases approach −1 and the center approaches +1, attaining that same constant asymptotically. The lumped classical equations give h(t)≤e^(−nt)+1/n and the stated integral formula and O(r(1+t)/n) fixed-time error. This is a statement about occupation in two different processes, not repeated measurements or first-passage probabilities.

## originality

PASS

Best-of-knowledge pass for the sharp, uniform-time law on the full regular-base Mycielskian family with its specified classical contrast. The strongest prior overlap is exact, not just phenomenological: the depth-two spider has a related three-state reduction, and reciprocity turns its published formula into an outer-layer law with the same scale and an adjustable matching coefficient. Its reduced Hamiltonian has no endpoint diagonal, unlike the Mycielskian quotient. No novelty is credited to a zero-diagonal trimer blockade, the equitable reduction method or the generic strong-root suppression mechanism.

## value

PASS

The Mycielski graph operation produces an exact, graph-geometry-independent obstruction for coherent layer occupation despite a positive classical probability on that same layer at every fixed positive time. The number 4r² is certified over all times and is reached at an explicit shrinking timescale; neither statement would follow from a simulation at selected times, and both are relevant to comparison across graph families. The zero-diagonal spider antecedent limits the scope of significance but does not give this precise combined law on the regular-base family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
