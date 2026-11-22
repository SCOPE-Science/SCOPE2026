# Sharp likelihood-ratio-order transition after wrapping the XLindley law

## Finding

The fixed-origin wrapped XLindley family undergoes an exact parameter threshold in likelihood-ratio ordering. Put \(L=2\pi\), and let \(g_\lambda\) be the density of the wrapped XLindley distribution on \([0,L)\), as defined below. There exists a unique \(\lambda_*\in(0.18008,0.18009)\), characterized by
\[
\left(e^{L\lambda_*}-1\right)\left((\lambda_*+2)^2+1\right)
   +L(2\lambda_*+4-L)=0,
\]
such that **every** pair \(\lambda_*\leq\lambda_1<\lambda_2\) has a strictly decreasing density ratio \(g_{\lambda_2}(t)/g_{\lambda_1}(t)\) on \(0<t<L\). This range is sharp: for every \(0<\lambda_1<\lambda_*\), some \(\lambda_2>\lambda_1\), arbitrarily close to it, has a ratio that first strictly increases and then strictly decreases, attaining a unique interior maximum.

In fact, there is a complete two-parameter classification. For arbitrary \(0<\lambda_1<\lambda_2\), set
\[
b_\lambda=\lambda+2+\frac{L}{e^{L\lambda}-1},\qquad
D(\lambda_1,\lambda_2)=\frac1{b_{\lambda_2}}-\frac1{b_{\lambda_1}}-(\lambda_2-\lambda_1).
\]
If \(D\leq0\), the density ratio is strictly decreasing on \((0,L)\). If \(D>0\), the ratio has exactly one interior maximum and is increasing before that point and decreasing afterward. For example, \(\lambda_1=0.10\) and \(\lambda_2=0.11\) give \(D=0.00109038233155\ldots>0\), with the unique maximum near angle \(0.46901\) radians.

## Assumptions and scope

For every \(\lambda>0\), begin with the one-parameter XLindley density on nonnegative reals,
\[
f_\lambda(x)=\frac{\lambda^2}{(\lambda+1)^2}(x+\lambda+2)e^{-\lambda x},\qquad x\geq0.
\]
The wrapped variable is \(\Theta_\lambda=X_\lambda\bmod L\), represented in the fixed branch \([0,L)\) with \(L=2\pi\). Its strictly positive density is
\[
g_\lambda(t)=\sum_{k=0}^\infty f_\lambda(t+kL)
 =\frac{\lambda^2e^{-\lambda t}}{(\lambda+1)^2(1-e^{-L\lambda})}
  (t+b_\lambda),\qquad 0\leq t<L.
\]
All ratios are densities with respect to Lebesgue measure on this **fixed** angular branch. The statistician's choice of zero direction matters; this theorem does not assert a rotation-invariant order on an uncut circle. The density can have a jump at the seam as a function of a periodically extended argument.

## Proof

**1. A one-dimensional criterion.** The positive normalizing factor in \(g_\lambda\) is independent of \(t\). Therefore
\[
\frac{\partial}{\partial t}\log g_\lambda(t)
    =-\lambda+\frac1{t+b_\lambda},
\qquad
J(\lambda,t):=\frac{\partial^2}{\partial\lambda\,\partial t}\log g_\lambda(t)
    =-1-\frac{b_\lambda'}{(t+b_\lambda)^2}.
\]
Write \(E=e^{L\lambda}\), so
\[
b_\lambda'=1-\frac{L^2E}{(E-1)^2}.
\]
Because \(t+b_\lambda>0\), the sign of \(J(\lambda,0)\) is the negative of that of \(H(\lambda)=b_\lambda^2+b_\lambda'\). Direct cancellation yields
\[
H(\lambda)=\frac{K(\lambda)}{E-1},\quad
K(\lambda)=(E-1)\big((\lambda+2)^2+1\big)+L(2\lambda+4-L).
\]
\(K(0)=L(4-L)<0\), while \(K(\lambda)\to+\infty\). Moreover
\[
K'(\lambda)=LE\big((\lambda+2)^2+1\big)
   +2(E-1)(\lambda+2)+2L>0
\]
for every \(\lambda>0\). Thus \(K\) has one and only one positive root \(\lambda_*\). It follows that \(J(\lambda,0)>0\) below the root, vanishes at the root, and is negative above it.

**2. The terminal mixed derivative is always negative.** Since \(b_\lambda+L=\lambda+2+LE/(E-1)\), direct expansion gives
\[
(b_\lambda+L)^2+b_\lambda'
   =(\lambda+2)^2+1
    +\frac{LE}{E-1}\big(2(\lambda+2)+L\big)>0.
\]
Hence \(J(\lambda,L)<0\) for every positive \(\lambda\). If \(J(\lambda,0)\geq0\), then \(b_\lambda'<0\), and \(J(\lambda,t)\) is strictly decreasing in \(t\); it has exactly one zero in \((0,L)\) when \(\lambda<\lambda_*\), located at
\[
t_c(\lambda)=\sqrt{-b_\lambda'}-b_\lambda.
\]
At the boundary \(\lambda=\lambda_*\), the mixed derivative is strictly negative for \(0<t<L\). For larger \(\lambda\), it is negative everywhere in \((0,L)\), whether \(b_\lambda'\) is negative or positive.

**3. The sharp family cutoff.** For \(\lambda_1<\lambda_2\),
\[
\frac d{dt}\log\frac{g_{\lambda_2}(t)}{g_{\lambda_1}(t)}
    =\int_{\lambda_1}^{\lambda_2}J(\lambda,t)\,d\lambda.
\]
If \(\lambda_1\geq\lambda_*\), this integral is strictly negative for every \(0<t<L\). Conversely, if \(\lambda_1<\lambda_*\), continuity gives a sufficiently close larger \(\lambda_2\) for which the integral is positive at \(t=0\), while step 2 makes it negative at \(t=L\). This proves both the cutoff and its sharpness.

**4. Every pair's exact shape.** The derivative has the explicit form
\[
Q(t):=\frac d{dt}\log\frac{g_{\lambda_2}(t)}{g_{\lambda_1}(t)}
   =-(\lambda_2-\lambda_1)
     +\frac{b_{\lambda_1}-b_{\lambda_2}}
           {(t+b_{\lambda_1})(t+b_{\lambda_2})}.
\]
Step 2 proves \(Q(L)<0\). When \(b_{\lambda_1}\leq b_{\lambda_2}\), \(Q(t)<0\) everywhere. Otherwise \(Q\) is strictly decreasing in \(t\). Since \(Q(0)=D(\lambda_1,\lambda_2)\), the two cases in the finding follow immediately, including uniqueness of any interior maximum. No other turning-point pattern is possible.

**5. Consequence for one-observation testing.** Under the simple hypotheses \(H_0:\lambda=\lambda_1\) versus \(H_1:\lambda=\lambda_2>\lambda_1\), the Neyman--Pearson likelihood-ratio rejection region for \(\lambda_1\geq\lambda_*\) is a lower angular interval on the fixed branch (up to randomization or an endpoint). When \(D>0\), choosing a threshold strictly between the larger of the two endpoint density-ratio limits and the unique interior maximum instead gives an interior angular interval as the most powerful rejection region. In particular, the wrapping operation destroys the global likelihood-ratio ordering established for the unwrapped XLindley family, even though it restores that ordering above a sharp parameter boundary.

## Verification

The standard-library-only script `checker.py` checks the exact algebraic expression for \(K\), uses rational alternating-series bounds for \(\pi\) and rational exponential Taylor bounds to prove
\[
0.18008<\lambda_*<0.18009,
\]
and rigorously verifies the positive initial density-ratio derivative for \((\lambda_1,\lambda_2)=(0.10,0.11)\). It also runs seeded diagnostic derivative comparisons and endpoint sign checks; these diagnostics are not substitutes for the global proof above. Run `python3 checker.py` from the extracted package directory. The recorded run passed 506 assertions, with all reported sign brackets proved by exact rational arithmetic.

## Relationship to prior work

Zinhom, Nassar, Radwan and Elmasry (2023) define the wrapped XLindley law, compute its density, trigonometric moments and estimators, and discuss angular-origin invariance. This finding takes precisely their fixed-origin density as its starting point and derives a new **sharp likelihood-ratio ordering classification** rather than another density or moment formula. Chouia and Zeghdoudi (2021, Section 5, Theorem 1) show likelihood-ratio ordering for the **unwrapped** XLindley family. The wrapped model does not inherit that theorem at small parameters, while the root above identifies its precise range of recovery. Bell and Nadarajah (2024, Section 2.45) survey the same wrapped density and moments without supplying the likelihood-ratio order cutoff.

## Limitations

This is a theorem about one published one-parameter fixed-origin model and the fixed angular ordering \([0,2\pi)\); it does not transfer unchanged to a freely rotated, reflected, or location-unknown family. The likelihood-ratio argument yields a single-observation Neyman--Pearson consequence, but does not prove a scalar-threshold uniformly most powerful test for arbitrary sample size. It does not establish a more general stochastic-order classification or inferential efficiency of estimators. The priority comparison is based on inspected open-access papers, a mathematical-record search and available claims; absence of a search hit is not a proof of global priority. Independent mathematical review has not been performed.

## References

1. E. Zinhom, M. M. Nassar, S. S. Radwan and A. Elmasry, *The wrapped XLindley distribution*, Environmental and Ecological Statistics **30** (2023), 669–686. Published online 2023-10-31. DOI: https://doi.org/10.1007/s10651-023-00579-2.
2. S. Chouia and H. Zeghdoudi, *The XLindley Distribution: Properties and Application*, Journal of Statistical Theory and Applications **20** (2021), 318–327, Section 5. DOI: https://doi.org/10.2991/jsta.d.210607.001.
3. W. Bell and S. Nadarajah, *A Review of Wrapped Distributions for Circular Data*, Mathematics **12** (2024), 2440, Section 2.45. DOI: https://doi.org/10.3390/math12162440.
