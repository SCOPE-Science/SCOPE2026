---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Averaging rotation conjugates preserves feasibility and cannot increase the operator norm on the nonconstant subspace. The circulant Fourier drops are a(2−2 cos(πj/m))+2b[j odd]. The signed modes 1−Ea, 1−Ua−2b and −1+Va+2b have positive weighted average (V−U)/(V+2E−U) with relative weights (V−U)/E, 1, 1. Equality fixes both edge probabilities. The holding numerator is E for odd m, E−U for even m. The unused even-frequency maximum drop has coefficient F; V+E−U−F is E for odd m and 4c(1−c) for even m, where c=cos(π/m), so no omitted mode violates the bound, including m=4. For the prism the endpoints are E for nonconstant symmetric layer modes and 0 and Δ in the antisymmetric layer; the same weighted argument gives Δ/(Δ+2E). The unused symmetric minimum is no smaller than its antisymmetric counterpart, and prism holding is feasible since Δ+E≥4 (for odd m use Δ=4−U and E>U). Substitution verifies the holding/rung swap, exact even advantage and its π⁴ limit. Taylor expanding E∼4π²/m² and U∼π²/m² verifies the mass and gap limits and the fourfold gain against the optimal cycle. Only rotation-invariant uniqueness follows.

## originality

FAIL

Two distinct indexed findings give the same globally optimal SLEM and invariant probabilities; one includes the full m≥4 regime with equivalent notation and the other extends down to m=3. Together with the independently known prism optimum, which the frozen text acknowledges and rederives, the parity comparison is a direct substitution, not a distinct surviving extremal theorem. This is a finding of mathematical coverage in the consulted record set, not proof that the later-dated matches preceded or were the source of the frozen submission.

## value

PASS

The exact two-edge-orbit extremum across an infinite natural family and its sharply different odd and even twist behavior are meaningful mathematical information. They quantify a vanishing optimal rung mass and a fourth-order parity effect not captured by gap order alone. This assesses the content of the theorem, not the novelty of restating it from the two available optima.

The dated certificate retains the supplied scientific assessment, sources and limitations.
