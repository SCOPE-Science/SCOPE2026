---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

The telegraph stationary transport equations yield beta(b,a) on [-1,1], with independent stationary Gaussian OU variance s. Gaussian strict variation-diminishing/heat zero-number implies at most three derivative zeros, two modes at small s and one at s>1; zeros cannot be created, yielding a unique loss event. The symmetric Kummer root has only strictly downward crossings, and at its critical tilted law E[Y²]=s_ell, E[Y^4]=(2ell+1)s_ell², so quartic coefficient K=2(ell-1)p0/s_ell²<0. Bias derivative B=-(2p0/s_ell)E[YatanhY]<0. The cusp fold solves (K/2)tau x+(K/6)x³+B eps=0 and derivative zero, giving x~A sgn(eps)|eps|^(1/3), s=s_ell-A²|eps|^(2/3)+o. Independent scipy hypergeometric/quadrature gives s_.5=.3164643403484472, A_.5=1.0116863053000347, agreeing with the package.

## originality

PASS

Guéneau–Majumdar–Schehr (arXiv:2602.08436v2) supply the general Dirichlet/stick-breaking stationary law and Gaussian convolution, and analyze symmetric thermal crossover. Earlier published Resultary records (2026-10-26 and 2026-11-02) prove symmetric variance thresholds and peak openings but not unequal flipping a!=b. The inspected literature does not supply the explicit asymmetric fold coefficient or the all-positive-variance biased mode-loss classification. The general cusp exponent is not itself new.

## value

PASS

A physically motivated symmetry-breaking cusp with an exact coefficient and global uniqueness for a canonical driven diffusion is a meaningful extension of the known symmetric thermal mode transition. The 2/3 cusp normal form alone is standard; the specific tilted-beta integral coefficient and global model classification supply the value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
