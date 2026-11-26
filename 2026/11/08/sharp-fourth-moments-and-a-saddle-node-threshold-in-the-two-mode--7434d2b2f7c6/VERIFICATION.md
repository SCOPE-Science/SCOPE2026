---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Using E[(X)_k]=lambda^k and descending exact expansion into the falling-factorial basis through order eight, I recovered N=lambda(1+2lambda t²) and E f⁴=lambda B. Differentiating K gives -8Q/(1+2lambda t²)^3. The sign at t=0 and the nonzero leading quartic term show that neither zero nor infinity is projectively stationary (use s=1/t at infinity); the odd part of B strictly prefers t to -t for positive t, excluding every negative direction from the maximum and every positive one from the minimum. Descartes gives one simple positive root; the negative half-line has at least one real root. The resultant divided by the leading coefficient gives discriminant -256R. Independent Sturm remainders end with a nonzero constant and give variations (3,3,2,2) at (0,1/250,1/200,+infinity), so the change from four simple real roots to two is unique. At small positive lambda the three negative roots deform from -3/2,-1,-1/2; Q(-1)>0 and Q(-1/2)<0 below the transition locate the nearest root in (-1,-1/2), with the other two below -1. The two latter roots cannot cross -1. The simple discriminant zero and fixed nonzero leading coefficient exclude a triple root or simultaneous collisions (the Sylvester matrix would have nullity ≥2). Thus the two left roots merge in a double root, with nonzero quadratic curvature in Q there and a local root splitting controlled by the simple zero of the discriminant. The corresponding K stationary point has nonzero cubic term, so it is an inflection; the derivative signs give the merging negative minimum and adjacent negative maximum. The rightmost negative root stays simple at the transition and, once only two real roots remain, is still in (-1,0) by the signs at those endpoints. The independent anchor comparison with t=-1/2 recovered all five c_i; c0,c1,c3,c4 are positive, and 4c0c4-c2² divided by 32lambda is strictly positive through 1/200 by monotonicity and exact sign there. Hence K(t)>K(-1/2) for all t≤-1 in the transition regime. The rightmost negative minimum is strictly below the anchor by the derivative sign on its right, so uniquely global, and above threshold there is no other candidate. Connectedness on the real projective circle proves the sharp full interval. Replay: python3 -B /workspace/audit_checks/5.py (exact moment/resultant/Sturm/comparison calculations, rational bisection of threshold; root ordering, stationary geometry and global selection are analytical).

## originality

PASS

Pass for the combined all-intensity sharp optimization, exact algebraic threshold for nonglobal stationary directions and exclusion of a competing global minimum. Charlier orthogonality and algebraic moment evaluation are background, not credited as new.

## value

PASS

The two lowest centered polynomial modes are the natural first test of mixing orders in a Poisson norm comparison. Neither extremum is a pure mode. The exact intensity at which a pair of nonglobal stationary directions disappears, with proof that the optimizing branch does not switch, distinguishes the phase portrait from the global norm profile. This is useful exact information for studying mixed-chaos optimizers beyond finite case sampling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
