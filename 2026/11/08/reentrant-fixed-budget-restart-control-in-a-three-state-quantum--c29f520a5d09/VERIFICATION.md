---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

Reconstructed the precise stationary-renewal-phase objective, not synchronized-time convergence or first detection. Direct four-step Grover coin-amplitude recurrence gives p_0..p_3 exactly as in RESULT.md. Under E T=3 and support {1,2,3,4}, the feasible law polytope is exactly conv{D=3, B=(1,4) weights (1/3,2/3), C=(2,4) weights (1/2,1/2)} and R=E F_T/3. Independent SymPy factorization confirmed differences R_B-R_D=-8P/(9(ell+2)^5), R_B-R_C=-4Q/(9(ell+2)^5), R_C-R_D=-4(ell²-7ell+2)(ell²+ell+2)/(3(ell+2)^5). Descartes and sign brackets ensure all positive roots; nonwinning second P root does not cause phase transition. Regimes are D,B,C,D at alpha≈0.1400136787, beta≈1.60855434465, gamma≈6.70156212; ties exactly adjacent edges. Independent rational p_cl for lazy walk yields strict D optimum. At ell=1, B=1471/2187 and D=5/9. Finite code calculations corroborate, but infinite conclusion is algebra/LP/root signs.

## originality

PASS

Best-of-knowledge independent source and logical implication comparison supports an exact new statement after explicit credit for known techniques and partial cases. Historical priority is not certified and residual access risks are retained.

## value

PASS

Under natural fixed mean-three resource budget and four-step maximum latency, full phase diagram of optimal reset clocks is a sharp, nontrivial control classification: coherent walker switches between deterministic and two randomized distributions then back, while matched classical increments never randomize. Dependence on the invariant-phase observation and the two different quantum/classical models is explicitly delimited; significance does not rely on unsupported unrestricted optimality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
