# Independent mathematical audit

## correctness

PASS

Write J=∑(1−U_i), then known-rate Poisson moments are λ/2 and λ/3 (mean and variance), and known-total-count moments are m/2 and m/12. With q=P(Y=0), let D=E[J]−E[J|Y=0]. The two posterior means are E[J]−D and E[J]+Dq/(1−q), so explained variance is D²q/(1−q). Independent future Poisson events give D=λ(t−t²/2) and q=e^(−λt); independent uniforms conditional on all exceeding t give D=mt/2 and q=(1−t)^m. This verifies the exact means, risks and information, including zero information at t=0 and at the fixed-count t=1; the Poisson t=1 remains informative. The Poisson derivative sign is that of 2(1−t)/(1−t/2)−g(λt), with g(x)=x/(1−e^(−x)) strictly increasing. The strictly decreasing difference crosses once, and larger λ moves the root left. Uniformly g(λt)→1 for small λ, giving 2/3, while λt≤c* gives t→0 at high rate and then λt→c*. In the fixed-count case the sign changes once by 2∑(1−t)^k=m; the average of these strictly decreasing terms shrinks as m grows, so the root falls strictly from t₁=1/2. Bracketing at t=x/m uses the limit ∫₀¹e^(−xs)ds and proves mt_m→c*. Substituting in both formulas and using c*²/(e^c*−1)=c*(2−c*) gives the normalized coefficients and the independently checked decimal values. For exact counts, conditional means are affine in N(t) with slopes 1−t/2 and 1/2 respectively, giving the stated explained fractions and optima. The reported 7,219 finite checks agree with the inspected loop counts; the uploaded verifier was not executed. The analytic argument, not the numerical grid and simulations, supplies exact uniqueness and limits.

## originality

PASS

Credit the classical full-count result, the exact Poisson fixed-presence objective covered by the same-day threshold-design record, and the scalar asymptotic optimization shared with first-arrival estimation. The supported distinct claim is the exact finite-density placement laws for the compulsory presence bit, including the known-total-count model and the comparison of their normalized information losses. The compared results do not give the conditioned placement law or the paired design theorem. This is not an originality pass for the standalone Poisson objective, its vanishing captured fraction, or the scalar constant.

## value

PASS

The compelling content is the exact optimized sensing design for two standard count-process laws when only irreversible presence/absence hardware is available, especially the conditioned bridge's entire finite-count placement law and its comparison to the unconditioned process. This shows quantitatively that the best fixed presence sensor must operate on a shrinking first-arrival scale and captures an inverse-density fraction under either law, unlike observing an exact count or a tunable threshold. The value is in the paired statistical design and conditioning comparison, not the scalar root or the known standalone Poisson objective.

The dated certificate retains the supplied scientific assessment, sources and limitations.
