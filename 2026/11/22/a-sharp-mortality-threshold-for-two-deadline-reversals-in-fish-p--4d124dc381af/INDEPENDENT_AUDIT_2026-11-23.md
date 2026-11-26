# Independent mathematical audit

## correctness

PASS

Independence from the common mortality model gives P(T)=∫₀ᵀe^(−μs)f(s)ds for each design separately; it does not require any coupling of the two counterfactual passage times. Scaling by τ gives P_E=(1−e^(−(1+a)x))/(1+a) and P_R=4[1−(1+(2+a)x)e^(−(2+a)x)]/(2+a)². The derivative of the difference is e^(−(2+a)x)(4x−e^x). The concavity and peak of log(4x)−x give exactly two derivative zeros x_-<1<x_+, with signs −,+,−. At infinity the difference is −a²/[(1+a)(2+a)²], strictly negative when a>0. When a=0 the strictly decreasing right branch tends to zero from above, leaving exactly one finite crossing. For the critical height write e^(a x_-)Δ_a(x_+)=∫₀^{x_+}e^(a(x_-−s))(4s e^(−2s)−e^(−s))ds. In its derivative the sign of x_-−s is opposite to the sign of the density difference throughout, so the derivative is strictly negative. The height is positive at zero; direct evaluation at a=1 gives −1/18+(3x_+/2−1)/(144x_+³)<0 since x_+>2. This yields uniqueness of a_c in (0,1), and the branch signs give exactly the stated two-crossing, tangency, and no-crossing alternatives. Δ'' at x_+ is e^(−(2+a)x_+)(4−4x_+)<0, so the critical equality is a true tangency, not a crossing. As a→0⁺, any fixed M>x_+ has positive Δ_a(M) eventually, forcing the right root beyond M. As a→a_c from below, Δ_a(M)<0 eventually for each fixed M>x_+, trapping that root arbitrarily close to x_+; the compact left branch and the unique positive zero at a_c give the same limit for the left root. Independent bisection of 4x−exp(x) on (0,1), (1,3) and then of the height on (0,1) gave x_-=0.3574029561813888, x_+=2.153292364110349 and a_c≈0.316461352642133, consistent with the illustrative values.

## originality

PASS

The nearest inspected formulations clarify a genuine comparison: neither a competence interval with no mortality, a different pair of lifetime distributions, nor the finite-horizon Laplace identity fixes the sign of this local maximum as the mortality parameter varies. The exact catalogue match is the assigned record. No inspected distinct source contains an equivalent classification or a result making the mortality switch a parameter substitution; this does not establish priority.

## value

PASS

The point is not evaluating a standard Erlang CDF. With equal mean and the same independent mortality, the more concentrated design is worse at short deadlines and also worse at eventual completion with any positive mortality, yet can be strictly better at intermediate deadlines. Locating exactly when that interior advantage exists and disappears is a useful benchmark for the interplay between variability and competing mortality. The two boundaries and the isolated tangency give a complete decision diagram for this natural minimal model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
