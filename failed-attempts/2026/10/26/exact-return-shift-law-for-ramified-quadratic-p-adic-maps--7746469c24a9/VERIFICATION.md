---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

With x=1/2+pt and a=−(1−4c)/(4p), the induced map is g(t)=t+a+pt²; a is a unit. This proves invariance, and f_c(x)−x=p(a+pt²) rules out fixed points. Modulo p the first p iterates visit all residues, so telescoping g^p(t)−t gives pa modulo p² because the sum of all squares vanishes for p≥5. For G=g^{p^n}, the reduction of G as a polynomial is a translation, so its Taylor coefficients of degree ≥2 are divisible by p and G'≡1 mod p. For n≥1 and increments in p^n Z_p, the nonlinear remainder lies in p^{2n+1} Z_p⊆p^{n+2} Z_p. The p return iterates therefore accumulate the normalized shift multiplied by 1+G'+⋯+(G')^{p−1}≡p mod p². This proves the induction on n (with n=0 from g mod p); restoring x gives the stated modulus and coefficient. Since each shift has valuation n+1 in x, every cycle attains all p lifts at the next level, giving the adding machine by inverse limit. Independent finite replay: for p∈{5,7,11}, n∈{0,1,2}, a∈{1,2,p−1,p+1}, reduce c=1/4+pa modulo p^{n+2}, iterate x↦x²+c exactly p^n times for every x≡1/2 mod p in that quotient, and compare with x+p^{n+1}a. All 8068 comparisons matched; the frozen p=5,c=−1 example also gives 28 modulo 125. At p=3,c=1,x=2, the third iterate is 2 modulo 27 instead of the proposed 11, confirming that the excluded case cannot just be included. The finite replay does not prove the unrestricted n claim.

## originality

FAIL

The exact family-specific formula was not located verbatim. It is nonetheless mechanically implied by the signed displacement computations in DesJardins–Zieve, not merely by a general theorem on transitivity. Work in the original x coordinate: the level-one residue 1/2 is a fixed residue, its return multiplier is f_c'(x)≡1 mod p, and its translated lift coefficient b_1(x)=(f_c(x)−x)/p≡−(1−4c)/(4p) mod p for every x in the ball. Appendix B's first-lift congruence and §4's later-lift congruence preserve this very coefficient mod p, pointwise. This yields the entire displayed return-shift law directly. Fan–Liao and Jeong also cover the structural consequences. No claim is made that DesJardins–Zieve explicitly name this parameter family.

## value

FAIL

An exact leading return digit on a natural ramified family is potentially more useful than merely knowing its cycles grow. Here that digit is already carried unchanged by prior cycle-lifting equations, and its initial value is read from one expansion of the quadratic. Minimality and conjugacy bring no separate uncovered result. No higher-order digit, new parameter case, or distinct use of the coefficient is established in the submitted claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
