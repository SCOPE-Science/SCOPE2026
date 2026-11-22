# Independent mathematical audit

## correctness

PASS

The exact centered quadratic cardinal B-spline moments give quadratic-reproduction iff correction a=1/8. The derivative of a unit input step is a signed three-triangle combination with endpoint heights 0,-a,1+2a,-a,0. Integrating each signed linear segment gives 1+2a+2a^2/(1+3a) for all real a>=0, including 14/11 at a=1/8; the step is a true attaining input. Absolute summability of input jumps and the derivative kernel supplies the global upper bound on the bi-infinite grid. We separately integrated six rational correction strengths, including a=0, 1/8, and 7/3. The finite integral checks corroborate rather than establish the all-input theorem.

## originality

PASS

The exact quadratic-reproducing stencil is classical: Sablonniere (2005) explicitly prints (-f_{j-1}+10f_j-f_{j+1})/8. The novelty that survives is its precise discrete-to-continuous total-variation norm and the full nonnegative-correction tradeoff, not the construction or polynomial reproduction. The primary full text reports a finite-interval infinity norm and approximation rates but no bi-infinite jump-TV operator norm. Nearby cubic interpolatory spline and B-spline projection results use different operators; complete historical priority remains best-of-knowledge only.

## value

PASS

Quantifies a concrete cost of achieving quadratic exactness for a canonical low-cost spline rule: stable positive sampling a=0 becomes intrinsically BV amplifying by exactly 14/11 at the unique quadratic reproducer. Entire natural a>=0 parameter family has an exact attained, monotone stability frontier, with a simple worst-case step witness. This is a motivated precise invariant, not just a code validation or known norm recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
