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

For the specified uniform start and sticky boundaries, the exact input moments agree with Jeon–Go–Kim, Eqs. (28), (113), and with an independent backward-equation derivation. For first passage on [0,1], let D_k=M_k^+−M_k^- and t=1/v: D_k′=−kt(M_{k−1}^++M_{k−1}^-), D_k(1)=kM_{k−1}^+(1) by the exponential sticky hold, and (M_k^-)′=t(D_k+kM_{k−1}^-) with M_k^-(0)=0 for k>0. Averaging the first-hit moments and using the outgoing-origin return moments, a geometric number of failed crossings adds q times the return mean and q times its variance plus Q times its squared mean. This gives the supplied expressions. At fixed a both objectives diverge at the speed endpoints. In inverse speed the mean curvature exceeds 4/3 because z coth(z/2)>2, hence there is a unique global mean optimum. For weak capture, q≥1/z−1/2 and Q≥1/z²−1/12 follow from the displayed hyperbolic inequalities: the latter reduces by differentiation to sinh³x>x³cosh x, using y(2+cosh y)−3sinh y strictly increasing for y>0. The resulting global lower bounds and the trial at v=c a^(1/3) trap all optima in a common compact interval for s=v/a^(1/3). There the stated C² expansions have leading f and 4f with positive curvature; inserting c³=4/3 into the first corrections gives c²/8 and c²/5, so the gap is 3c² a^(2/3)/40+O(a). For strong capture the trial z=log a and the lower bounds force log a−O(log log a)≤z≤O(log a) at every minimum. The leading derivative balances in z give a exp(−z)→3/2 for mean and →1 for variance. On [log a−1,log a+1] the variance curvature is 2 exp(−z)(1+o(1))+O(a⁻²)>0, giving uniqueness there and hence globally for large a; subtraction gives the asserted log(3/2) coefficient. From /workspace, python3 reproductions/run_tumble.py reproduced the exact rational first-hit and return polynomial coefficients and checked stationary speeds at a=10⁻⁹,10⁻⁶,10,10⁹. At a=10⁻⁶ they are 0.01102156774 and 0.01103064384, and at a=10 they are 4.56964452 and 4.24722284 (mean then variance). The frozen script was inspected, not executed. Numeric roots do not prove global uniqueness or intermediate-reactivity behavior. The theorem compares absolute variance, not CV, and gives neither all-a variance uniqueness nor a single-crossover theorem.

## originality

PASS

Pass the two-objective optimizer reversal with explicit asymptotic gap coefficients and variance-optimum uniqueness in both limiting regimes. The stochastic model, exact moments, weak leading mean scale and strong mean logarithmic denominator are prior work, not separate novel contributions. The bounded comparisons establish substantive distinction from nearby first-passage optimization results without guaranteeing priority.

## value

PASS

Mean absorption time and its absolute variance are distinct, naturally motivated objectives for selecting propulsion in a confined search. The theorem shows that the preference between their optimal speeds reverses as capture reactivity changes, gives the separation on two different scales, and establishes actual unique global variance optima in both regimes. That explains when mean-optimal tuning does or does not also improve repeatability; the result is more than another evaluation of known moments or an intermediate-parameter plot.

The dated certificate retains the supplied scientific assessment, sources and limitations.
