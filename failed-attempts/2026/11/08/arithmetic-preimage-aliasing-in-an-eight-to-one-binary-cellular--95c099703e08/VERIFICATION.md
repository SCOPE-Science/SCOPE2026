---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

Each N-periodic input corresponds bijectively to a closed walk length N on the 16-state order-four de Bruijn graph, including N<5 because closure enforces cyclic neighborhood coincidences. Traces of M0^N, M1^N and (M0M1)^{N/2} count exactly the three target classes. Independently reconstructed exact integer characteristic polynomials as z^8(z-1)^3(z+1)(z²-z+1)(z²+z+1), z^8(z-1)^2(z+1)^2(z²-z+1)(z²+z+1), and z^8(z^8-1). Their root-of-unity spectra give 6|N and 16|N formulas for all ring lengths, not extrapolation. Direct enumeration for N=1..10 matches. The N=16 eight alternating predecessors cannot have period 1,2,4,8 as those lengths have zero such predecessors, thus all are period 16.

## originality

FAIL

FAIL: Another already published November 8 theorem on the *identical* local rule proves an exact stronger finite all-target formula: for every cyclic target y and every N its fiber count equals fixed points of a product of fully specified eight-sheet arrow permutations. In its proof the all-zero letter-loop permutation alpha has one six-cycle and two fixed labels, immediately giving 2 or 8 for constant zero. Applying its provided arrow permutations to all-one and alternating target loops likewise yields the other trace/divisibility outcomes; no new mathematical mechanism is needed. Thus these three target families are special cases of a previously published exact description even though the earlier paper emphasizes asymptotic S8 fiber distribution and does not print the same numbers. The same-date ordering of the two published records is not established; this is coverage, not attribution of earlier authorship.

## value

PASS

The three constant/alternating targets are natural benchmark configurations, and an eight-fold inflation of a period-two output into a primitive period-16 predecessor is a meaningful exact dynamical boundary for nonlinear finite-ring aliases. The arithmetic phase census is intrinsically useful, even though its complete originality is defeated by the more general all-target sheet-permutation description. General preimage graph methodology alone is not treated as making every explicit instance worthless.

The dated certificate retains the supplied scientific assessment, sources and limitations.
