# Independent mathematical audit

## correctness

PASS

The one-vector orthogonal projection has squared residual ab(X+Y)/(aX+bY), with a=σ1²>b=σ2²>0 and X,Y the positive squared coordinates. Put U=X/(X+Y); exchangeability gives E U=1/2. The strictly convex function ab/(b+(a-b)u) gives the lower bound 2ab/(a+b), with equality only if U=1/2 almost surely. Independent, identically distributed X and Y equal almost surely must be constant (every measurable threshold event has probability equal to its square); unit variance and centering then force iid fair signs. Gaussian polar coordinates make the angle uniform; quadrant substitution t=tan θ gives expected residual (2ab/π) times the integral from 0 to infinity of 1/(a+bt²), hence √(ab). Division yields (κ+κ⁻¹)/2, and κ→infinity proves noncomparability in the stated mean-squared sense. If a=b there is no strict optimizer, as the source notes. The singular-basis alignment, no oversampling, and squared norm are essential to the stated comparison. The supplied spot-check script and its reported 5316 cases were inspected as evidence, not executed; the audit uses exact derivations.

## originality

FAIL

The central extremality and equality claim is a direct dimension-two, identity-filter specialization of the earlier Resultary exchangeability theorem. The exact two means also occur in a distinct indexed comparison on the same UTC date; the quotient and its unboundedness are immediate. The evidence establishes prior or equivalent coverage, not falsity or priority between same-date records.

## value

FAIL

The aligned two-mode example is a useful illustration of why sketch laws need not be interchangeable. As a standalone scientific contribution, however, the optimizer and equality case are directly obtained from the existing exchangeability theorem and the penalty is a one-line consequence of the available exact means. There is no further quantitative or structural claim left after subtracting this coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
