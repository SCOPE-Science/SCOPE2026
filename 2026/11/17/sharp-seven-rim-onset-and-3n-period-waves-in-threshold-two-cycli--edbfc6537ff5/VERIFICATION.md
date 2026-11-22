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

For fixed hub colour zero, at most one rim successor colour one is allowed, and a 2-to-0 rim adjacency is forbidden, yielding exactly n+2 fixed rim words, hence 3(n+2). The explicitly displayed three-step update of (hub 1, rim 0^(n-4)1122) advances the hub three times and rotates its rim by one for n>=7, hence least temporal period 3n since the rim word has no shorter rotational symmetry and hub phase requires a multiple of three. The full labelled functional graph of 3^(n+1) states was independently recomputed for each n=3..7 (not sampled): n<=6 only fixed recurrent states; n=7 has 27 fixed points, exactly two primitive period-21 cycles, and period-21 basin size 168. The finite census covers only those five sizes; no general spectrum theorem is claimed for n>7.

## originality

PASS

Threshold-one cyclic automata on wheel graphs previously have only fixed and primitive three-cycles and rapid stabilization, but a threshold-two cyclic rule (advance only with two successor-coloured neighbors) has a different transition graph. Threshold-two Greenberg-Hastings refractory wheel model has uniform extinction, but automatic refractory steps are fundamentally different from current CCA. Neither implies the exact n=7 onset, 21-cycle census or all-size 3n waves. Classical 2D-lattice CCA work motivates dynamics without a wheel enumeration.

## value

PASS

A sharp minimum graph circumference where a natural deterministic contact rule becomes capable of nontrivial cycling, combined with an explicit infinite family of growing primitive temporal periods and an exact 6561-state first-bifurcation basin, is a motivated finite-graph dynamical classification. Finite n=7 census is complete, and the all-n wave is analytically constructed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
