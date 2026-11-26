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

Apply scalarization by norm-one functionals and the maximum-modulus principle in each variable to put both suprema on the distinguished torus; with zeta=z/w, these are the circle suprema of P and its two-term section. Writing xi=exp(i pi/3), the relation xi^2=xi-1 gives the moments (1,1,0) for the weight (2-xi)/3 at xi and its conjugate weight at conjugate(xi). Each weight has squared modulus 1/3. Rotating both nodes and applying the triangle inequality proves the Banach-valued bound. For (a,b,c)=(1/2,1,-1/4) the circle squared profile as a function of s=cos(t) is 25/16+s/2-s^2/2, peaking at 27/16, versus a truncated supremum of 3/2. A unit vector in any nonzero target transfers that ratio. In the scalar equality problem, a zero retained coefficient gives ratio at most one by the Fourier coefficient bound. Normalize both retained coefficients to be positive by a common phase and input rotation. At zeta=1 both weighted node values must then be positive real and saturate the norm; adding and subtracting the resulting node equations forces real c=(a-b)/2. Stationarity at s=1/2 gives b(a+c)+2ac=(a+b)(2a-b)/2=0, hence b=2a and c=-a/2. This gives the claimed orbit, and the explicit peak proves the converse. Independently replayed the exact moments, weight size and boundary peak in rational arithmetic; numerical trials are not needed for universality. Replay: python3 /workspace/independent_replays.py 2.

## originality

PASS

The exact three-monomial supremum projection norm and scalar equality orbit were not found in the compared statements. Grando covers the same ordered scalar section with a nonsharp bound of 3; Geddes–Mason works with the full disk algebra, which has a larger input class; the closest Resultary exact quadratic extremum has a different source norm and objective. Priority is qualified by the limits of the 1975 full-text access and older finite-degree projection literature.

## value

PASS

The cutoff is the first homogeneous bidisk block and first retained segment where the universal monomial-section bound can be noncontractive: an initial single monomial is bounded by its Fourier coefficient estimate, and the only other sections in degree zero or one are identities or single monomials. The exact sharp loss, uniformly for complex Banach coefficients, and the scalar equality orbit are meaningful for sharp finite-block section estimates. The norming representation explains why the same loss remains sharp in every target rather than merely giving a numerical scalar improvement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
