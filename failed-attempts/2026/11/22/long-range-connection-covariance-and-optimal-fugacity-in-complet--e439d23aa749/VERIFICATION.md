---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

A forest has at most one doubly attached leaf. Let d=1+2t, M=d+nt^2 and p=t/d. The probabilities of no bridge and a bridge in a specified pair are w=d/M and b=2t^2/M. Conditional on the bridge identity the two events are independent; the pair mean is 4p^2-Delta times the no-bridge indicator added to the base 4p^2 in the sense that it equals 4p^2-Delta*1_{no bridge}+h*1_{bridge in pair}, with Delta=2p^2 and h=2p-4p^2. The covariance of the two conditional means is Delta^2 w(1-w)+2 Delta h w b-h^2 b^2, giving the displayed rational formula. Independent exact enumeration of K_{2,4} at t=1/3 gave covariance 816/225625, consistent with the formula. Rational differentiation gives the stated negative multiple of F_n. There is just one sign change for n>=4, F_n(0)<0 and F_n(1)=-22n-54<0; the unique positive zero is the maximum, beyond 1. With epsilon=1/n the normalized polynomial at epsilon=0 is t^3(2t+1)(t-1), with derivative 3 at t=1, and its first epsilon coefficient there is -22. The implicit root expansion therefore gives 22/(3n), with O(n^-2) remainder. The rational formula for n times the covariance extends continuously to epsilon=0 near t=1, giving 4/27 at the convergent optimizers. The supplied checker was not run; the finite reproduction does not establish the optimizer or the asymptotics.

## originality

FAIL

The exact covariance and its positivity coincide with the acyclic limit of a distinct indexed exact random-cluster covariance for the same graph and leaf pairs. Both records carry the same date, so this establishes mathematical coverage, not chronological priority. The stated extension to n=4,5 requires no change to the other proof's sector identities, and the optimization is a routine differentiation, sign count and simple-root expansion of the identical rational function, not an independent substantive claim.

## value

FAIL

The exact sign and magnitude of global connectivity covariance are scientifically motivated, but the matching broader exact law already resolves them. The remaining two finite sizes need no new argument, and the optimizer and finite-size shift follow by routine calculus from the same rational function. No independently useful new mechanism, boundary phenomenon or optimization problem beyond this mechanical analysis was established as a surviving claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
