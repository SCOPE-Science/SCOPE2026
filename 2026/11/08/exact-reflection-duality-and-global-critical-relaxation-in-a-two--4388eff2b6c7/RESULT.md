# Exact reflection duality and global critical relaxation in a two-choice threshold map

## Finding

Let \(p>2\), \(0\leq\gamma\leq2\), and define the odd, strictly increasing function
\[
\Phi_p(d)=\left(\frac{1+d}{2}\right)^p-\left(\frac{1-d}{2}\right)^p,\qquad -1\leq d\leq1.
\]
Its inverse maps \([-1,1]\) into \([-1,1]\). Define the interval map \(T_{p,\gamma}(d)=\Phi_p^{-1}((1-\gamma)d)\). This is the fully mobilized invariant subdynamics of the symmetric two-choice threshold model with shape exponent \(\lambda=1/p\), written in the centered share difference \(d=2\rho_A-1\). Put
\[
 c_p=\frac{p}{2^{p-1}},\qquad \gamma_{\mathrm{pf}}=1-c_p,\qquad \gamma_{\mathrm{flip}}=1+c_p.
\]
The following is an exact global classification for every starting point \(d_0\in[-1,1]\):

1. **Parameter reflection:** \(T_{p,2-\gamma}^n(d_0)=(-1)^nT_{p,\gamma}^n(d_0)\) for every integer \(n\geq0\). Thus the trajectories at reflection-paired parameters have *identical absolute deviations at every time*, not merely matching asymptotic exponents.
2. **Two asymmetric fixed points:** If \(0\leq\gamma<\gamma_{\mathrm{pf}}\), there is a unique \(r\in(0,1]\) satisfying \(\Phi_p(r)=(1-\gamma)r\). The only fixed points are \(-r,0,r\); every positive (respectively negative) initial difference converges monotonically to \(r\) (respectively \(-r\)); the origin repels. There are no nontrivial cycles.
3. **Balanced phase:** If \(\gamma_{\mathrm{pf}}\leq\gamma\leq\gamma_{\mathrm{flip}}\), every orbit converges to zero. Except at the two endpoints of this parameter interval, the convergence is locally exponential with modulus \(|1-\gamma|/c_p<1\); at \(\gamma=1\) it takes exactly one update.
4. **Two-cycle phase:** If \(\gamma_{\mathrm{flip}}<\gamma\leq2\), there is a unique \(r\in(0,1]\) satisfying \(\Phi_p(r)=(\gamma-1)r\). Its only nontrivial periodic orbit is \(r\leftrightarrow-r\), and every \(d_0\ne0\) converges to it with alternating sign. The origin is repelling. At \(\gamma=2\), the cycle is the endpoint pair \(\{-1,1\}\).
5. **Exact critical slowing:** At *both* critical parameters \(\gamma=1\pm c_p\), for every \(d_0\ne0\),
\[
 |T_{p,\gamma}^n(d_0)|\sim
 \sqrt{\frac{3}{(p-1)(p-2)}}\,n^{-1/2}\qquad(n\longrightarrow\infty).
\]
The critical constant is identical at the pitchfork and flip thresholds. Neither critical orbit becomes eventually stationary. When the nonzero fixed points or two-cycle exist, the one-step modulus contraction at their limiting amplitude is exactly \(q=|1-\gamma|/\Phi_p'(r)\in(0,1)\).

The amplitude \(r\) is the unique positive root of \(\Phi_p(r)/r=|1-\gamma|\). For integer \(p\geq3\), this is a polynomial in \(r^2\); for example \(p=3\) yields \(r^2=4|1-\gamma|-3\) and \(p=4\) yields \(r^2=2|1-\gamma|-1\). These examples illustrate the general real-exponent theorem, not a restriction to integral \(p\).

## Assumptions and scope

The underlying two-choice map partitions a unit population into two active shares and an abstention share. We examine its **invariant fully mobilized edge** \((\rho_A,\rho_B,\rho_0)=(x,1-x,0)\), with symmetric cross-response parameter \(\gamma\) and symmetric threshold exponent \(\lambda=1/p\). Its cutoff equation is
\[
 u^{p}-(1-u)^p=(1-\gamma)(2x-1),\qquad x^+=u.
\]
For \(0\leq\gamma\leq2\), the right-hand side lies in \([-1,1]\); the unique cutoff \(u\) belongs to \([0,1]\). Since \(p>2\), \(\lambda<1/2\). Starting on the fully mobilized edge, the eligibility intervals cover the population for every parameter in this range: when \(0\leq\gamma\leq1\), the two activation drives lie in \([0,1]\) and \(t^{\lambda}\geq t\); when \(1\leq\gamma\leq2\), both drives are at least one. Therefore the edge is genuinely invariant in the stated model. No claim is made about trajectories started with positive abstention or parameters beyond \(\gamma=2\).

The classification is **pointwise**, includes the endpoints \(d=\pm1\), and distinguishes the fixed orbit \(d=0\) from nonzero orbits. The strict inequalities in the phase cases are essential.

## Proof

**Step 1: Reduction and parameter reflection.** The difference of the cutoff equation's power terms is \(\Phi_p(d^+)\), where \(d^+=2u-1\). On the fully mobilized edge the two activation drives differ by \((1-\gamma)d\). Thus \(d^+=T_{p,\gamma}(d)\). The function \(\Phi_p\) is odd and strictly increasing, so its inverse is odd. Consequently
\[
 T_{p,2-\gamma}(d)=\Phi_p^{-1}(-(1-\gamma)d)=-T_{p,\gamma}(d).
\]
Both maps are odd; induction gives the identity at every time \(n\).

**Step 2: The strictly convex amplitude law.** Write \(s=|1-\gamma|\) and, for \(r\in[0,1]\), set \(A_s(r)=\Phi_p^{-1}(sr)\). This is continuous, increasing, and maps \([0,1]\) to itself. For \(r\in(0,1)\),
\[
 \Phi_p''(r)=\frac{p(p-1)}{2^p}\left((1+r)^{p-2}-(1-r)^{p-2}\right)>0
\]
because \(p>2\). Hence \(r\mapsto\Phi_p(r)/r\) is strictly increasing, with endpoint limits \(c_p=\Phi_p'(0)=p2^{1-p}\) and \(1=\Phi_p(1)\). In particular \(0<c_p<1\).

If \(s<c_p\), then \(\Phi_p(r)>sr\) for every \(r>0\), equivalently \(A_s(r)<r\). Repeated application decreases every positive amplitude to the only fixed amplitude zero. If \(s=c_p\), the same conclusion holds, but its linear multiplier is one. If \(c_p<s\leq1\), strict monotonicity gives exactly one \(r_*\in(0,1]\) with \(\Phi_p(r_*)=sr_*\). Below \(r_*\), \(A_s(r)>r\), and above it \(A_s(r)<r\); as \(A_s\) is increasing, the amplitudes approach \(r_*\) monotonically from either side. Thus *all positive-amplitude orbits converge globally*. There can be no additional periodic amplitudes, since a continuous increasing map of an interval has no nontrivial periodic orbit.

**Step 3: Restore signs and classify periodic points.** If \(0\leq\gamma<1\), \(T_{p,\gamma}\) preserves sign and its nonzero fixed amplitudes give exactly the two fixed points. If \(1<\gamma\leq2\), it reverses sign at each nonzero step, and its nonzero fixed amplitude gives exactly the symmetric two-cycle. For \(\gamma=1\) the first iterate is zero. These observations together with Step 2 give all five parameter cases and exclude every period greater than two. The derivative at a positive limiting amplitude is \(A_s'(r_*)=s/\Phi_p'(r_*)\). Strict convexity implies \(\Phi_p'(r_*)>\Phi_p(r_*)/r_*=s\); hence \(0<A_s'(r_*)<1\) (the endpoint case uses the one-sided derivative). At \(r_*=1\), the factor is \(2/p\).

**Step 4: Critical constant.** Taylor expansion at the origin gives
\[
 \Phi_p(r)=c_p r\left[1+\frac{(p-1)(p-2)}6r^2+O(r^4)\right].
\]
At \(s=c_p\) the inverse amplitude map therefore obeys
\[
 A_{c_p}(r)=r-\beta r^3+O(r^5),\qquad
 \beta=\frac{(p-1)(p-2)}6>0.
\]
Every nonzero critical amplitude converges to zero by Step 2, and remains positive at each finite step. Thus its reciprocal square satisfies
\[
 A_{c_p}(r)^{-2}-r^{-2}=2\beta+O(r^2).
\]
Summing this along the orbit and taking Cesàro means yields \(r_n^{-2}/n\to2\beta\), so \(r_n\sqrt n\to(2\beta)^{-1/2}=\sqrt{3/[(p-1)(p-2)]}\). The sign of \(d_n\) depends on the parity and which critical parameter is chosen, but the amplitude—and therefore the constant—is identical by Step 1. This proves the complete statement.

## Verification

Run `python3 verify.py` with Python 3. The checker independently recomputes exact binomial coefficients and their critical ratio for integer exponents \(3\leq p\leq12\), checks the reflection identity over a grid of real exponents and initial conditions, verifies convergence and the one-step contraction at representative parameter values, and compares finite-time critical scaling against the analytically derived coefficient. On the saved version it printed `VERIFY_OK all_exact_and_numerical_checks_passed`.

The **proof**, not the finite numerical trials, establishes the global theorem for every real \(p>2\). The checker uses floating-point bisection for real-exponent examples; its error tolerances are not proof bounds for every parameter.

## Relationship to prior work

Fontanari, *Negative partisanship drives anti-frontrunner volatility in election dynamics*, first submitted 2026-10-18, arXiv:2610.25210v1, introduces the activation/cutoff model, its symmetric pitchfork and flip thresholds, and qualitative phase portraits. These background threshold locations and the qualitative presence of asymmetric states and a two-cycle are **not** claimed as new. The present claim adds an exact *all-time* parameter-reflection identity, a pointwise global attractor/cycle classification of the entire invariant edge for each real \(p>2\), the unique nonzero amplitude relation, and the exact common critical \(n^{-1/2}\) coefficient. The source's local linearization and qualitative phase diagrams do not state these exact orbitwise and critical-rate conclusions.

Standard facts about monotone interval maps, convexity, and parabolic one-dimensional fixed points are used rather than claimed as inventions. Published-record semantic searches for cutoff maps, period-two bifurcations, mirrored pitchfork/flip dynamics, and critical relaxation returned results for **different** maps, including a positive rational flip map with a distinct time-asymptotic expansion and a two-strategy exponential replicator map. Neither entails the stated exact cutoff-map identity. Historical priority has not been independently established.

## Limitations

The theorem concerns the fully mobilized invariant edge, not the full two-dimensional piecewise map or its basin boundary in the abstention-positive region. The power index must satisfy \(p>2\), and \(0\leq\gamma\leq2\); the implicit cutoff is not guaranteed to lie in \([0,1]\) for arbitrary larger parameters. Convergence at noncritical parameters does not assert a uniform rate over all starting points as parameters approach the thresholds. The source paper's qualitative bifurcation results are acknowledged. The review is same-model only; no independent scientific audit has been performed.

## References

1. José F. Fontanari, *Negative partisanship drives anti-frontrunner volatility in election dynamics*, arXiv:2610.25210v1, submitted 2026-10-18, https://arxiv.org/abs/2610.25210.
2. Steven H. Strogatz, *Nonlinear Dynamics and Chaos*, second edition, CRC Press (2015), general local pitchfork/flip and critical slowing background (not a source of this map's exact theorem).
