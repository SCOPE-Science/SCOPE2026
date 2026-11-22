---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

The paper specifies a fixed labelled left-to-right in-place complement-of-majority Rule 23 scan on n>=3, not synchronous ECA. If an update output equals its current right input c, the two other inputs must equal 1-c, enabling backward propagation from boundary equal outputs; this shows every image point is either boundary-antialigned or, for odd n, alternating. Direct forward scan gives on S_n the bijective signed shift (1-x_1,...,1-x_(n-1),x_1), with odd-n alternating exceptions forming a 2-cycle. The internal coordinate shift of L=n-1 bits has g=gcd(L,t) cycles; traversing each contributes complement parity (L-1)t/g, yielding N_n(t)=2^g when allowed plus 2 odd-n exceptional points for even t. Explicit all-zero orbit achieves max period L or 2L. Independently enumerated all 2^n states, exact image and temporal fixed counts for n=3..11 and all 1<=t<=2n. The universal statement follows from backward identity and signed-shift algebra, not finite tests.

## originality

PASS

Full primary Rule 23 paper Donoso-Leiva et al Theorem 12 concerns an E-covering COLLECTION of state-dependent sequential update modes on even rings, which can lead an initial state to a fixed point. It does not assert what the ONE fixed natural left-to-right order does, nor derive its 2^(n-1) signed-shift recurrent core or gcd fixed-period spectrum. Earlier ECA Rule 3, Rule 150 and synchronous Rule232 published results have different local maps or update conventions. No stronger result implying the exact fixed-scan conjugacy found after aliases and primary reading; historical priority qualification remains.

## value

PASS

Nonlinear elementary automata rarely admit a complete explicit description of the entire post-sweep recurrent image. The exact one-sweep phase collapse, signed-shift conjugacy and all-time gcd/parity temporal spectrum for all ring sizes resolve a motivated dynamical classification problem, not a trivial boundary/type check. The proven fixed-order result contrasts with state-dependent order convergence work.

The dated certificate retains the supplied scientific assessment, sources and limitations.
