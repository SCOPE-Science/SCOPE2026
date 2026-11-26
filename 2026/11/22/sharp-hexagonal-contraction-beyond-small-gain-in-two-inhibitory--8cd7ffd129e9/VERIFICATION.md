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

Both sequential argument evaluations are in I and the update preserves the state rectangle. Same-forcing secants give the matrix with rows (-A,-A) and (AB,-B(1-A)), where 0<=A<=a and 0<=B<=b. On representatives (1,0),(1,-1),(0,1) of the opposite pairs of hexagonal unit vertices, its output norms are A,B,A+B-AB; by convexity the last is exactly its norm. The componentwise-increasing maximum is q. With the state held fixed, the two forcing columns are (-A,AB) and (0,-B), of norms A and B. The mixed comparison therefore gives the stated geometric-series bound. Pullback trajectories at each k are Cauchy by comparing over the common suffix on the bounded rectangle; continuity gives the recurrence, and the same estimate gives bilateral uniqueness. Only forcing indices strictly below k enter; uniqueness gives shift equivariance and constancy at zero forcing. The unforced period follows from strict increase and endpoint signs of T-f(T)-g(T). The admissible tanh example attains the matrix bound to first order, including a zero gain by taking the corresponding map constant. The affine endpoint gives p_k=2-p_{k-1}, n_k=1 and hence a continuum of distinct two-cycles (take 0<s<=1/5). The proof is for the invariant one-lag event model; no asymptotic spectral-radius or physical realization claim follows. VERIFICATION.md and verify.py were inspected, not executed; the universal checks replay by the unit-vertex and pullback arguments above, not by the finite script.

## originality

PASS

Best-of-knowledge pass for the sharp norm contraction and individual-gain threshold, with the resulting forced response, in the nonincreasing one-lag class. The event recurrence and unforced period equation already occur in the cited work. Neither its theorem under the strict sum bound nor the inspected embedding result covers the claim at gains (4/5,4/5), and neither supplies the sharp hex-norm factor.

## value

PASS

The signed sequential update permits a stability region not certified by the usual sum of gains, together with a usable disturbance estimate. The exact worst-case norm factor and explicit failure at a unit endpoint show what the monotonicity/one-lag restriction buys and where a universal guarantee stops. The value is the sharp event-domain bound, not the standard fixed-point or period-balance deductions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
