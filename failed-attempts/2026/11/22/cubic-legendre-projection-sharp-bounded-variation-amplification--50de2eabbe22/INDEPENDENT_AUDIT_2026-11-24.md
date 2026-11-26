# Independent mathematical audit

## correctness

PASS

For μ=Df, Fubini applied to the step representation gives the sharp column L¹ norm of the derivative kernel. Differentiating the three Legendre coefficients gives q(t,x) as stated, and its two central roots give the exact radical. On t²≤1/100 the quadratic is negative at both endpoints and positive at zero; the integral between roots gives R−D, and the stated logarithmic derivative has negative numerator and positive denominator while D increases. I independently reconstructed and bounded all 225 Bernstein coefficient integrals by polarization and rational midpoint sums with explicit derivative errors, with maximum upper bound less than 1.779874. A separate rational t-grid and x-midpoint estimate with explicit two-variable derivative errors bounded the whole region |t|≥1/10 by less than 1.794188, below 9/5. Replay: python3 /workspace/branches/record4_midpoint_check.py. This verifies the continuum, not just sampled values. For equality, integrating a strictly positive gap against |Df| forces support at zero. The frozen script was read, not run.

## originality

FAIL

Direct prior coverage of the exact same norm and central jump in Resultary 9f934dc097f6. Its strict inequalities at every other jump, together with its step-measure representation, also imply the full equality class. Changing the rational certificate is not a surviving new scientific claim here.

## value

FAIL

The sharp seminorm is a motivated stability invariant, but as a new finding this repeats the known cubic benchmark, including the extremizer class already forced by the earlier proof. The alternate finite certificate does not by itself give a distinct mathematical outcome, range of applicability, or new extremizer. No genuine surviving repair was identified.

The dated certificate retains the supplied scientific assessment, sources and limitations.
