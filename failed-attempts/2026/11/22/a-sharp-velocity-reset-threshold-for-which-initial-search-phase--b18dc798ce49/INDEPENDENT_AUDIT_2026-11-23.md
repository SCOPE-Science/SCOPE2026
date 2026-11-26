# Independent mathematical audit

## correctness

PASS

With all rates and D,v positive and equal initialization directions, the Fourier-resolvent elimination of the ballistic states yields G_D and G_B in RESULT.md; the free first-detection decomposition divides both spatial Green functions by the diffusive-start value at the target. This uses the strong Markov property at detection, which occurs only in the diffusive state. The characteristic quadratic is positive at zero and negative at lambda^2/v^2, so the two decay roots strictly straddle that positive argument and have the claimed signs. Partial fractions give the stated transforms. Subtraction leaves the two coefficients (mu_-^2-R)/mu_- and (R-mu_+^2)/mu_+; the second is strictly negative. At zero their sum is (mu_- - mu_+)(1+R/(mu_- mu_+))<0. Since R is below the larger root, evaluation P(R)=r lambda beta(1-D lambda/v^2) determines the sign of the first coefficient, including zero at equality. Factoring out the slower exponential gives either a strict negative sign at every finite distance, or an affine function of exp(-(mu_+-mu_-)x) that strictly increases with distance and has the stated single zero. The renewal mean is strictly decreasing in the discounted detection probability, and at x=0 a diffusive start detects immediately whereas a ballistic start does not. Independently evaluated the displayed normalized quadratic and logarithm at D=alpha=beta=r=1, v^2=5, yielding x_*=2.500456035756232. CHECK.py and its finite diagnostic scope were inspected, not executed.

## originality

FAIL

The exact all-distance statement is not spelled out in the inspected passages, but is a direct corollary of the previously published exact two-mode comparison data, not just of a generic model or renewal law. Flaquer-Galmés, Campos and Méndez supply both explicit transform and mean curves as combinations of the same two positive decay rates, and explicitly compare the near- and far-distance means. Their formulas already reduce the full mean ordering to the sign of one affine function on (0,1], with far-end sign read by evaluating their characteristic polynomial at R. Credit this as a useful extraction from exact prior formulas, not as a separately established original classification. The distinct same-day Resultary stationary-density result is not the reason for this failure.

## value

FAIL

The initialization choice is a natural question and the result is a convenient interpretation of the published curves. However, its claimed new content is exhausted by the sign and single root of a common-factor affine comparison of two already explicit means, whose limiting ratio the prior paper already computes. The sharp boundary and logarithmic distance are direct algebraic readings of those data, not a substantively new classification under the mechanically-implied-result criterion. Adding diagnostics or changing presentation would not produce a surviving distinct claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
