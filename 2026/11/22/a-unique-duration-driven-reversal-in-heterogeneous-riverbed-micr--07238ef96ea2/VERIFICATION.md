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

Each phase's map on the water fraction is p+s(x-p) with s=exp(-lambda t). Subtraction of the two compositions cancels the common coefficient of x, leaving (p_B-p_A)(1-s_A)(1-s_B) in each class. Thus the total difference has the sign of R(h)-q, where R=F_1/F_2 and F_j is the product of the two positive relaxation deficits. For each phase, a slower deficit divided by a faster one has positive logarithmic derivative: it is f(z_slow)-f(z_fast), where f(z)=z/(exp(zh)-1) is strictly decreasing in z for each h>0. The product is therefore strictly increasing. Its limits are q_0 and 1, neither reached at finite h, so even at q=q_0 or 1 the indicated strict signs follow. The algebra q=(1-w_1)d_2/(w_1 d_1) gives the claimed open weight interval. The product expansion R=q_0[1+((a_2-a_1)+(b_2-b_1))h/2+O(h^2)] gives the linear lower-boundary law; at infinity the slowest numerator relaxation sets 1-R, with multiplicity 2 exactly when a_1=b_1 and no denominator contribution of that order. This yields the logarithmic upper-boundary law with the stated constant. Independent bisection of the explicit difference for a=(1,3), b=(2,5), C=21/50, D=9/50 gives h_*=0.664242444373057 and opposite signs at the printed bracket endpoints. In the supplied rational bracket procedure the remainder of each exponential Taylor series has decreasing alternating terms beyond the cut, and monotone factor products and outward subtraction preserve enclosure. The uploaded script was inspected, not executed; the finite examples are not the proof.

## originality

PASS

Bounded pass for the two-class composition/duration phase diagram, not for the single-class swap identity, exponential-ratio monotonicity, or the observation that two materials may settle differently. The inspected indexed neighbors have timing or order effects, but not this conserved mixture and terminal objective with its exact open weight interval and unique scaled-duration root. Original primary microplastic full text retrieval was limited; that access limit is not negative evidence.

## value

PASS

The exact boundary separates two physically interpretable explanations of a phase-order signal: different initial bed fractions cannot cause the sign under this model, but class composition and a change of common duration can. The sharp weight interval and its independence of the phase-duration ratio let one diagnose whether a reversal is possible without solving for the crossing. The endpoint formulas distinguish rapid emergence at one edge of the window from a log-diverging required duration at the other. This is a complete classification of a simple, motivated batch model, not a claimed field intervention.

The dated certificate retains the supplied scientific assessment, sources and limitations.
