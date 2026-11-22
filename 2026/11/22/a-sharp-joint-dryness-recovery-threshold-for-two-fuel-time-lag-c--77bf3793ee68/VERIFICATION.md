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

# Reproduction and boundaries

Run `python3 verify.py` with Python 3 and its standard library. The checker uses direct phase enumeration, scalar root bisection, closed-form derivatives and deterministic grids. A recorded run returned `PASS: 17475 deterministic checks`. The verification script is embedded in the same artifact collection, with no external data or network dependencies. The root-and-maximum formula is derived and proved analytically in `RESULT.md`; a grid approximation of the maximum is diagnostic, not global numerical certification. The explicit \(\rho=2\), \(c=1/50\), \(x=2\) recovery witness has a separate exact inequality in the proof.

The mathematical theorem is restricted to a common sinusoidal equilibrium and two linear relaxation modes. The paper-retrieval limitations documented in `REVIEW.md` affect historical priority, not the algebraic identity. Independent review and empirical validation have not been performed.
