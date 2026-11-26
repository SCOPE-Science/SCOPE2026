# Independent mathematical audit

## correctness

PASS

For the scalar deterministic lemma, if S_n diverges, choose N with w_n≥ηL for n≥N. The step multiplier then is 1−t with 0≤t≤1, and the drop in x² is at least t x²≥ηg²/(Lw). Thus the weighted gradient-energy sum converges. With B_n=Σ_{j=N}^n g_j² and C=ε+sqrt(S_{N−1}+2g_{N−1}²), the difference-square bound gives w_n≤C+2sqrt(B_n). If B diverges then g_n²/(C+2sqrt(B_n))≥[sqrt(B_n)−sqrt(B_{n−1})]/3 once sqrt(B_n)≥C, contradicting weighted summability. B bounded instead forces S bounded, completing the contradiction with no a priori iterate bound. In the Bernoulli case disjoint zero-to-active blocks occur infinitely often almost surely. If w_∞≤ηL/2, every active multiplier has modulus at least one (including equality), and each such block contributes at least L²x_0² to S on a nonzero path, impossible. Above the strict threshold the active multipliers eventually lie in a compact subinterval in modulus below one; the strong law for activations gives exponential decay and squared-gradient summability. For the exact log rate, sum only over active times. If the terminal multiplier is nonzero, its active-step logarithms converge to the stated constant, so Cesàro averaging in the active index and the strong law give the product with p. If it is zero but the path does not hit zero, an arbitrary negative bound eventually holds for all active logarithms and gives rate −∞. This does not assert that such a terminal weight must occur. A coordinate that hits zero has finitely many remaining nonzero gradient differences and stays zero. Each event is coordinatewise; finite intersection requires no within-time independence. Unbiasedness and the variance identity follow by independent current sampling and summing coordinatewise square deviations, without cross terms. Consecutive sampled curvatures are independent, not generally the observed gradients themselves.

## originality

PASS

The same update and deterministic finite variation are prior. The pathwise argument for bounded arbitrary time-varying nonnegative scalar curvature and its stochastic Bernoulli consequences on an unbounded domain are distinct from the strongest compared same-algorithm theorems and the deterministic AdaGrad-Norm threshold analogue.

## value

PASS

The primary paper flags an unconstrained interpolation summability question. This restricted positive answer is mathematically useful because the deterministic lemma gives a mechanism for finite difference memory without bounded-domain assumptions, and the Bernoulli structure gives a precise almost-sure threshold and logarithmic rate for any positive step and denominator floor. It does not purport to solve the generic open problem or to give an expected or uniform rate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
