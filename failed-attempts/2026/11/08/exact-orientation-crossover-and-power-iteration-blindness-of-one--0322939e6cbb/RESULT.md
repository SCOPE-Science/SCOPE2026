# Exact orientation crossover and power-iteration blindness of one-column sign sketches

## Finding

For a real, rank-two matrix with exactly two columns, standard one-vector randomized range finding exhibits a sharp, orientation-dependent reversal between independent Rademacher and Gaussian input sketches. The reversal persists for every nonnegative integer number of power iterations. In particular, sign sketches can have smaller expected squared Frobenius error than Gaussian sketches when right singular directions are nearly coordinate-aligned, but larger error near a diagonal orientation. At precisely diagonal orientation, power iteration cannot remove the sign method's positive mean error excess.

Here is the exact statement. Define the singular-value ratio \(\kappa=\sigma_1/\sigma_2>1\), let \(q\in\mathbb Z_{\ge0}\), put \(p=\kappa^{2q+1}>1\), and define the alignment statistic \(t=|\sin(2\theta)|\in[0,1]\), where \(\theta\) is the angle of a leading right singular vector with the first coordinate axis. If \(G_q\) and \(S_q\) are the expected squared residuals under standard Gaussian and independent fair-sign sketches, respectively, then

\[
\frac{G_q}{\sigma_2^2}=1+\frac{\kappa^2-1}{p+1},\qquad
\frac{S_q}{\sigma_2^2}=1+(\kappa^2-1)\frac{p^2+1+(p^2-1)t^2}{(p^2+1)^2-(p^2-1)^2t^2}.
\]

The denominator is strictly positive. The sign error increases strictly with \(t\) on \([0,1]\), and the unique comparison threshold is

\[
t_c^2=\frac{p^2+1}{(p+1)^2}.
\]

The inequalities are \(S_q<G_q\) for \(0\le t<t_c\), equality at \(t=t_c\), and \(S_q>G_q\) for \(t_c<t\le1\). The global sign-sketch endpoints at fixed singular values and power count are

\[
S_q(0)=\sigma_2^2\left(1+\frac{\kappa^2-1}{p^2+1}\right),\qquad
S_q(1)=\frac{\sigma_1^2+\sigma_2^2}{2}.
\]

For each fixed \(\kappa>1\) and \(t<1\), \(S_q\to\sigma_2^2\) as \(q\to\infty\), yet \(S_q(1)\) is unchanged for all \(q\). This failure of uniform convergence is intrinsic to exactly orthogonal sign draws. At \(q=0\) the three values \(S_0(0),G_0,S_0(1)\) are, respectively, the harmonic, geometric, and arithmetic means of \(\sigma_1^2\) and \(\sigma_2^2\).

## Assumptions and scope

Fix an integer \(m\ge2\), a rank-two real matrix \(A\in\mathbb R^{m\times2}\), an orthonormal left singular pair \(u_1,u_2\), and ordered singular values \(\sigma_1>\sigma_2>0\). Choose a right singular pair \(v_1,v_2\) with \(v_1=(\cos\theta,\sin\theta)^\mathsf T\); changing signs or orientation conventions does not affect \(t\). For each integer \(q\ge0\), draw one real random vector \(\omega\in\mathbb R^2\), form

\[
y_q=(AA^\mathsf T)^qA\omega,\quad P_q=\frac{y_qy_q^\mathsf T}{y_q^\mathsf Ty_q},\quad E_q(\omega)=\lVert A-P_qA\rVert_F^2.
\]

The two laws compared are (i) two independent standard real Gaussian coordinates and (ii) two independent symmetric signs, each \(\pm1\) with probability \(1/2\). For either law, \(y_q\ne0\) almost surely; both projections are therefore well-defined. This is the untruncated rank-one range projection with a **single sketch vector**, no oversampling, no rounding errors, and a fixed matrix. The word "power" refers to the integer \(q\), not a stochastic iteration count; each sketch uses the same initial \(\omega\) through its power applications.

## Proof

Write the thin SVD as \(A=U\operatorname{diag}(\sigma_1,\sigma_2)V^\mathsf T\) and write \(V^\mathsf T\omega=r(\cos\psi,\sin\psi)^\mathsf T\), with \(r>0\). As \(\sigma_2>0\), the projected vector is proportional to \(p\cos\psi\,u_1+\sin\psi\,u_2\). Expanding \(\operatorname{tr}(A^\mathsf TA)-\operatorname{tr}(A^\mathsf TP_qA)\) gives the exact deterministic identity

\[
\frac{E_q(\omega)}{\sigma_2^2}=1+(\kappa^2-1)\frac{\sin^2\psi}{p^2\cos^2\psi+\sin^2\psi}.\tag{1}
\]

For the Gaussian sketch, rotational invariance makes \(\psi\) uniform modulo \(2\pi\). Its angular integral is

\[
\frac1{2\pi}\int_0^{2\pi}\frac{\sin^2\psi}{p^2\cos^2\psi+\sin^2\psi}\,d\psi=\frac1{p+1}.\tag{2}
\]

One direct derivation uses the positive-quadrant substitution \(z=\tan\psi\), which changes the integrand to \(z^2/((p^2+z^2)(1+z^2))\) integrated with factor \(2/\pi\) over \([0,\infty)\); partial fractions or continuity at \(p=1\) yields (2). Substitution in (1) proves the Gaussian formula.

For two fair signs, \(\omega/\lVert\omega\rVert\) occupies the four diagonals of the coordinate square. Opposite signs give identical residuals. Up to swapping the two outcomes, their squared directional coordinates in the right singular basis are

\[
(\cos^2\psi,\sin^2\psi)=\left(\frac{1+t}{2},\frac{1-t}{2}\right)
\quad\text{or}\quad
\left(\frac{1-t}{2},\frac{1+t}{2}\right),
\]

with probability \(1/2\) each. Averaging (1) gives

\[
\frac{S_q}{\sigma_2^2}=1+\frac{\kappa^2-1}{2}\left[
\frac{1-t}{p^2(1+t)+1-t}+\frac{1+t}{p^2(1-t)+1+t}\right].\tag{3}
\]

Common-denominator simplification of (3) proves the stated rational expression. Define \(u=t^2\), \(D=p^2+1\), and \(H=p^2-1\). Then the additive factor divided by \(\kappa^2-1\) is \((D+Hu)/(D^2-H^2u)\); its derivative is

\[
\frac{H D(D+H)}{(D^2-H^2u)^2}>0
\]

for \(p>1\) and \(0\le u\le1\). The endpoint denominators obey \(D^2-H^2u\ge D^2-H^2=4p^2>0\). Subtracting (2) from (3) and factoring yields

\[
\frac{S_q-G_q}{\sigma_2^2}=
\frac{(\kappa^2-1)p(p-1)[(p+1)^2t^2-(p^2+1)]}{(p+1)[(p^2+1)^2-(p^2-1)^2t^2]}.\tag{4}
\]

Every factor outside the square bracket is strictly positive; (4) proves the exact threshold and strict comparison. The threshold lies strictly between \(1/2\) and \(1\) after squaring, and its dependence on \(p\) is monotone increasing for \(p>1\) because \(d[(p^2+1)/(p+1)^2]/dp=2(p-1)/(p+1)^3>0\).

Putting \(t=0\) and \(t=1\) in (3) proves the sharp endpoint formulas. Since \(p=\kappa^{2q+1}\to\infty\), the aligned and every fixed non-diagonal case \(t<1\) converge to the optimal rank-one residual \(\sigma_2^2\). More precisely, for \(0\le t<1\),

\[
\lim_{q\to\infty}p^2\left(\frac{S_q}{\sigma_2^2}-1\right)
=(\kappa^2-1)\frac{1+t^2}{1-t^2}.
\]

At \(t=1\), one of the sign directions has \(\cos\psi=0\) and is exactly orthogonal to the leading right singular vector. The powered sketch from that draw remains in the lower singular direction for every finite \(q\), while the other draw remains in the leading direction; each has probability \(1/2\), giving \(S_q(1)=(\sigma_1^2+\sigma_2^2)/2\). Finally, setting \(p=\kappa\) at \(q=0\) produces the harmonic/geometric/arithmetic means stated above. This completes the proof for all stated dimensions, angles, gaps, and integer power counts.

## Verification

The accompanying standalone `verify.py` uses SymPy exact identities and exact rational parameters, plus SciPy independent angular integration and NumPy direct projected-matrix tests. Run `python verify.py` with Python 3, SymPy, SciPy and NumPy installed. Its output is provided in `verify_output.txt`. The tests cover the comparison factorization, monotonicity, endpoint values, threshold, power limits, rational sign enumeration, Gaussian quadrature, and direct tall-matrix projection for selected parameters. These finite tests do **not** replace the proof in the preceding section or certify floating-point behavior at arbitrarily ill-conditioned parameters.

For example, when \(\kappa=3\), \(\sigma_2=1\), and \(q=0\), the sign-sketch extremal mean errors are \(9/5\) and \(5\), bracketing the Gaussian mean error \(3\). At \(q=1\), the aligned sign error is \(1+8/730\), the Gaussian error is \(1+8/28\), and the diagonal sign error remains \(5\).

## Relationship to prior work

Halko, Martinsson and Tropp established the standard randomized range-finder and power-subspace-iteration framework. Saibaba and Międlar [1] study randomized low-rank approximation beyond Gaussian matrices, including Rademacher sketches; their main results are general distributional high-probability bounds with sample-size conditions and experiments, not the exact, one-vector, right-singular-orientation comparison (3)–(4). Epperly and Webber [2] prove minimax sharpness for rotation-invariant randomized-SVD embeddings and explicitly report increased errors of small sign embeddings on coherent test matrices; this **already establishes a qualitative orientation/discreteness vulnerability**. Their statements do not supply the parameter-exact two-column Gaussian/sign crossover for arbitrary power count, or the precise nonuniform limit in this theorem. Thus the method, qualitative concern, and general comparison idea are established; the claim here is specifically the closed-form phase boundary and power-dependent risk profile.

The arithmetic/geometric/harmonic mean identity at zero power is algebraically elementary once (1)–(3) have been derived. It is used as a boundary check, not presented as an independently novel inequality. Specialist equivalent formulas in earlier randomized numerical-linear-algebra literature remain a possible precedence risk.

## Limitations

This theorem concerns a matrix with exactly two columns, one sketch vector, two distinct positive singular values, an untruncated orthogonal range projection, and expected **squared Frobenius** residual. It does not prove universal Gaussian superiority or infer the behavior of oversampled sketches, structured randomized Hadamard transforms, noisy computations, other norms, more than two columns, or modern robust large-scale randomized-SVD pipelines. The diagonal obstruction is a positive-probability exact annihilation for a discrete sketch, not a lower bound for every sign-based algorithm. Independent external validation and comprehensive historical precedence verification have not been performed.

## References

[1] A. K. Saibaba and A. Międlar, *Randomized low-rank approximations beyond Gaussian random matrices*, arXiv:2308.05814, originally public 2023-08-10, https://arxiv.org/abs/2308.05814.

[2] E. N. Epperly and R. J. Webber, *Sharp analysis of sketched least squares and randomized low-rank approximation*, arXiv:2605.19096, originally public 2026-05-18, https://arxiv.org/abs/2605.19096.

[3] N. Halko, P.-G. Martinsson and J. A. Tropp, *Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions*, SIAM Review 53 (2011), 217–288, https://doi.org/10.1137/090771806.
