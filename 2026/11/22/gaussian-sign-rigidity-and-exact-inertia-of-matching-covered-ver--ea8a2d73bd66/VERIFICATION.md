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

Walsh diagonalizes the unnormalized real symmetric convolution. A covered mask of size 2r has (2r-1)!! preimages, giving the Gaussian multiplier E[(1-Z²)^q(1+Z)^(n-2q)] after a possible reversal of all signs. Independently, the centered moments a_j=E[(Z²-1)^j] satisfy a_0=1, a_1=0 and a_(j+1)=2j(a_j+a_(j-1)) for j≥1 by Gaussian integration by parts. In the expansion of (-1)^q times the multiplier, all terms are nonnegative: Z^(2r)=(1+(Z²-1))^r. The constant term proves strict positivity for q=0 or q≥2; for q=1 the Z² term suffices exactly when n-2q≥2. Thus n=2,3 have only the stated zeros, n=0,1 are identities, and the exceptional ranks are both two. For n≥4, reflection and the alternating partial-binomial sum give positive-minus-negative count zero at n=2m and 2(-1)^m binom(2m,m) at n=2m+1. An independent exact evaluation by weight classes through n=50 summed (-1)^a binom(k,a) binom(n-k,b)(a+b-1)!! over a+b even (1,326 values); it agreed on signs, zeros and inertia. The frozen verify.py was inspected, not executed; its recorded 11,014 assertions are finite corroboration, not the all-order proof.

## originality

PASS

The mixed-sign evaluation is of a classical polynomial, and a prior edge-spectrum identity gives the same signed evaluations as a restricted transform, plus partial nonvanishing. Neither establishes the full real sign rule, exceptional zero list and inertia. The distinct specialization passes on the examined evidence, not as an exhaustive priority claim.

## value

PASS

The kernel is the natural pushforward that retains which vertices a matching covers and forgets how they were paired. The theorem isolates all failures of convolution inversion and gives a balanced or centrally biased inertia according to the parity of the host size. These invariants of the full counting operator are not recoverable from total matching counts or the prior dyadic gaps alone. It does not assert sharp conditioning or a classification for other hosts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
