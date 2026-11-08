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

# Reproducible mathematical checks

Run `python3 verify.py` in the same directory. Python standard library only. The successful replay reports \(3003\) enumerated six-vertex sets, exactly \(1890\) controllable sets, selected-point counts \((7,84,420,868,420,84,7)\), \(14\) controllable orbits under all \(336\) automorphisms, and agreement of all \(3003\) cases with the independently built full-Laplacian four-Krylov-block test.

The exact lifting of the \(7\times7\) rank test from \(\mathbb F_{101}\) to \(\mathbb Z\) uses the proven uniform Hadamard determinant bound \(27\sqrt7<101\). The full-Laplacian finite-field test is an independent finite consistency check; the all-order statement is proved by projective-plane incidence algebra and PBH, not by running finite cases.

No experimental claim is made about all larger projective planes, optimal energy, noise, finite precision or actuator costs. Independent review has not been performed.
