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

The pair-antisymmetric states have eigenvalue -1, the hub-orthogonal pair-symmetric states have +1, and the remaining two-dimensional matrix is [[0,sqrt(2m)],[sqrt(2m),1]]. Its eigenvalues are (1±s_m)/2 and both have nonzero projection from the pair state. This yields Eq. (1) and, by equality in the unit-modulus phase bound (also for convergent subsequences), three symmetric phases must approach γ and the antisymmetric phase -γ for PGST. The product of the two mixed-sector phases is the +1 eigenphase, which forces γ=1 and contradicts the required relative sign on ±1. In Step 3 the complex equation literally needs the global phase: 2m exp(it/2)a_m=W_m+q_m. All subsequent uses are of the modulus, so Eq. (1) and the proof of the claimed probabilities are unaffected. The value at π/2 is at least (1-1/m)^2, and |W_m|²=(2m-1)²-4m(m-1)cos²t bounds all o(1/m)-optimal sequences within O(m^-1/2) of odd half-periods. Signs of W at shifts by 2π do not change the absolute real projection bound in the irrational case. There, torus density permits the test point (π/2,0), and at a localized time the perturbation contributes at most 1/sqrt(2)+o(1) to |W_m+q_m|. In the integral case the original amplitude is 2π-periodic, and bounded u=s_m(t-t_j) gives the uniform amplitude loss u²/8 plus the two center cosine terms. Modulo 8 and reflection u→-u give the stated two objectives; their negations are uniformly strictly concave, and compactness of localized u justifies optimizing the asymptotic expansion. The equation for u and both decimals were independently recomputed by the contractive fixed-point map. The resonant constants exceed the irrational one (the lower bound could be equal only at u=0 and cos α=1) and differ since the cosine decreases across their separated argument intervals at |u|<=sqrt(2). Inspected check_transport.py and VERIFICATION.md (168 reported finite numerical checks); no uploaded code was executed. The limits are not finite-size identities or approximating-time bounds.

## originality

PASS

Pass for the sharp three-branch asymptotic of best-time partner infidelity. The phase test and invariant-sector methods are standard; the fixed-size no-PGST part is a short application and is not the basis of the originality verdict. The dissertation full text remains an identified priority risk, not a failed scientific check.

## value

PASS

The observation-time supremum is a natural transport figure of merit distinct from average mixing or a yes/no transfer criterion. No finite graph gets arbitrarily close to perfect transfer at fixed m, yet optimal fidelity tends to one with a sharp penalty depending on three arithmetic branches. The resonant splitting is a substantive feature of optimized dynamics and does not follow from merely evaluating at π/2.

The dated certificate retains the supplied scientific assessment, sources and limitations.
