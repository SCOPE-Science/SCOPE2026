# Independent mathematical audit

## correctness

PASS

The torus sum/difference map has determinant of absolute value 2 and is onto, so the two output angles are jointly Haar. The squared sine of either half-angle is arcsine; the original length is 2SR with independent S^2 and (R^2-b^2)/(a^2-b^2) both arcsine. Writing q=R^2 and x=ell/2 gives density pi^(-2) times the integral of [(q-b^2)(a^2-q)(q-x^2)]^(-1/2) from max(b^2,x^2) to a^2. Substitution q=a^2-[a^2-max(b^2,x^2)]sin^2(theta) gives both branches with the stated modulus and normalizes by conditioning. On either side of the caustic the complementary modulus squared is asymptotic to b|ell-2b|/(a^2-b^2), and deviations in the prefactor times the logarithm are o(1), giving precisely the factor 16 in the logarithm. K(0) and the continuous lower endpoint give the outer limits, with no atoms; the circle has constant R and the stated arcsine transform. Independence and the first two arcsine moments 1/2 and 3/8 yield m2 and m4 as stated, and 4m4/3-2m2^2=(a^2-b^2)^2. To see that no continuous scalar can recover both axes locally, restrict it to a small circle in any proposed injectivity neighborhood: its values coincide at some pair of antipodes by continuity. The supplied standard-library code and notes were inspected, not executed; finite quadrature and simulation are not used to justify the all-ellipse result.

## originality

PASS

The inspected comparisons cover the circle law and related elliptic-integral forms or inverse-moment constructions for different measures. They do not give both branches and the minor-diameter constant for the independent eccentric-anomaly law, or its exact inversion formulas. The mathematical comparisons hinge on the measure and on which random variable the density describes, not just an ellipse and a K function appearing in both statements.

## value

PASS

The affine-uniform model is a natural image of circular line picking and should not be confused with arclength or invariant-line models. It yields a calibrated interior singularity while both outer endpoint limits stay finite, tracing a concrete change from the circle. Exact two-moment recovery offers a separate inverse use of the law, including scale. The value is the complete noncircular law and its distinctive transition and inversion, not a new evaluation of the classical circle law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
