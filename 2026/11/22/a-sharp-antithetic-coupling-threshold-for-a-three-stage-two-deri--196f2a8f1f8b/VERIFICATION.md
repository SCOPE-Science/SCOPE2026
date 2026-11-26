---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The tableau gives the real multiplier aI+bJ with a=1−x/2+q1 x²/24 and b=√x[1−(q0+q1)x/12+q0 q1 x²/96]. Put w=s(2p−1); the required moments are E(q0 q1)=1+w, E(qi²)=1+s, E(qi² qj)=1+s+2w for i≠j, and E(q0² q1²)=(1+s)²+4w. In E(a²+b²) the x and x² terms cancel; the x³, x⁴ and x⁵ coefficients are respectively (1+2s+5w)/144, (−1−s−4w)/576 and [(1+s)²+4w]/9216. These give the exact stability polynomial and rational example. Conditional expectation over independent steps gives the full energy law. The strict positive p-slope for x,s>0 proves unique antithetic optimality. At p=0 and 0<s<1/3 the quadratic discriminant is 256s(s+1)(3s−1)<0; at s=1/3 the polynomial is 4x²/9. Above s=1/3, at p=pc the constant term vanishes and the linear and quadratic coefficients are positive; increasing p can only increase the polynomial. Below pc its constant term is negative, linear coefficient positive and leading coefficient nonnegative, proving the unique threshold and the rationalized formula, including the linear case (s,p)=(1,0), x*=4. The s=0 polynomial gives the isolated neutral x=8 separately. The read-only inspection of the packaged rational checker and output supports the arithmetic but is not needed for the general result.

## originality

PASS

The inspected work supplies the deterministic tableau, a general iid mean-square criterion and related stochastic examples, but does not cover the complete dependence on the within-step binary coupling for this tableau, including the uniquely optimal antithetic law and the stable small-step interval.

## value

PASS

A fixed published integrator on the canonical energy-preserving test problem has opposite qualitative behavior depending only on the within-step error coupling, with an exact classification of all couplings and steps in the stated family. Neither independent nor shared errors can produce the contraction. This is a meaningful benchmark for how coupling affects stability; it is not evidence for physical fidelity, ordinary roundoff, or nonlinear problems.

The dated certificate retains the supplied scientific assessment, sources and limitations.
