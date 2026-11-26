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

In the exact coordinates (s,z)=(x+y,y−x), write b=cs^d. Then s'=s+z+3b and z'=b. For V(s)=cs^{d+1}/(d+1), the increment of V(s)−z² is the nonnegative convexity remainder plus z²+bz+2b²=(z+b/2)²+7b²/4. The increment is strict off the fixed origin. A bounded subsequence bounds this increasing quantity above on the entire orbit, so summation forces b and z to zero; otherwise the norm tends to infinity. A nondecreasing step in |s_n| places the orbit in the claimed cone via z_n=cs_{n−1}^d. There must be such a step on every escaping tail, since eventual strict decrease bounds both coordinates; s_n=0 at such a step would also give s_{n−1}=z_n=0 and is impossible on escape. Both cones preserve sign and satisfy r'≥r+2cr^d. Once successive signs agree, r_{n+1}=3cr_n^d(1+e_n) with 0<e_n≤4r_n^{1−d}/(9c), since cr_{n−1}^d≤r_n/3. For W_n=log r_n+log(3c)/(d−1), the recurrence W_{n+1}=dW_n+log(1+e_n) yields a finite positive height (take W_n>0 on a late tail); the geometric tail shows W_n−Hd^n→0, giving the multiplicative constant rather than just a logarithmic scale. Also z_n/s_n→1/3, which gives the signed direction. A sufficiently small neighborhood of a nonzero point has Lyapunov oscillation less than its first-step increment, so no positive iterate returns to it. Its inverse images are disjoint and any invariant probability gives them equal mass; a countable cover then gives zero mass off the origin without integrability assumptions.

## originality

PASS

The stable-basin identification is prior and is not being credited as new. The distinct result is the exhaustive complement dynamics for this odd negative branch, with two signed absorbing channels, quantified escape, and nonwandering/probability rigidity. The closest earlier exact scale is genuinely related but assumes even degree, and the same-map odd-negative published theorem resolves the basin, not the complement.

## value

PASS

The natural unresolved question after identifying the stable basin is the fate of every initial point outside it. Strict global increase and two finite-entry channels settle it in the exact branch and prove recurrence rigidity for all Borel probabilities, not just those of compact support. The exact prefactor and positive height add quantitative information not supplied by the dichotomy alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
