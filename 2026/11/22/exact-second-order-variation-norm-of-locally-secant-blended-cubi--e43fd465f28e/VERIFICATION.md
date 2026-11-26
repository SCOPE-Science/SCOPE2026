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

The displayed norm theorem holds, but the frozen Finding incorrectly calls the first distributional derivative of the nodal linear interpolant atomic. For example, the nodal data y_i=x_i give L(x)=x, so DL=dx, whereas every a_j=0. The complete repaired RESULT.md keeps the theorem and identifies the atomic measure as D²L=sum_j a_j Dirac(x_j), proved by cellwise integration by parts and cancellation of traces. It also fixes the one-jump support description at theta_j=0 or 1 and scopes the finite checks to the actual rational inputs. For the repaired claim, independent differentiation from the four endpoint equations (/workspace/replay/local_formulas.py) gives normalized H''=(4-6t)(1-theta_i)a_i+(6t-2)theta_{i+1}a_{i+1}; each absolute kernel integral is 5/3. The physical cell factor cancels. C¹ matching eliminates point masses in D²H, and summing the cellwise triangle inequality proves the upper bound, including convergence for bounded weights. Any coordinate vector of the secant jumps is realized by taking one slope jump and integrating on this bilateral grid. Its two cell interiors are disjoint, and their total mass is exactly the corresponding column weight, giving the supremum, with no need to attain it; for unbounded weights these single-jump norms are arbitrarily large. The identity |1-theta|+|theta|=1+2dist(theta,[0,1]) gives exactly the minimizing blends. No finite test supplies the bilateral or real-parameter quantifiers.

## originality

PASS

The revised derivative interpretation is standard and not itself novel. The distinct claim is the exact second-variation gain for the fixed local blend operator on arbitrary bilateral grids, including spatially varying and extrapolating weights. The closest local-blend result treats first variation, and the accessible primary minimization and approximation results do not establish this norm. Assessment is bounded by the material inspected.

## value

PASS

Integrated absolute second derivative is a natural quantitative measure of spline roughness. The exact sharp worst-case factor is independent of arbitrary mesh contrasts, classifies all minimizing real local slope blends, and gives the precise penalty and loss of boundedness for extrapolating weights. These are usable bounds for prescribed interpolation rules, not statements about geometric curvature or optimality among all interpolants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
