# One-sided finite-level first-passage convergence for a noisy monitored oscillator

## Finding

For the vacuum-initialized, infinitely frequently energy-monitored noisy harmonic oscillator, let \(T_B\) be its first passage to number level \(B\ge 1\), with heating rate \(\kappa>0\), and put \(Y_B=\kappa T_B/B\). Define \(\Phi_B(s)=\mathbb E[e^{-sY_B}]\) for \(s\ge0\). Let \(I_0\) and \(I_2\) denote modified Bessel functions of the first kind. The following *one-sided finite-level crossover theorem* holds.

For every integer \(B\ge1\),
\[
\Phi_B(s)=\frac{1}{L_B(-s/B)},\qquad
L_B(z)=\sum_{k=0}^{B}{B\choose k}\frac{(-z)^k}{k!}.
\]
For every fixed \(s>0\), the full strict order, including the limiting classical law, is
\[
\Phi_1(s)>\Phi_2(s)>\cdots>\Phi_B(s)>\Phi_{B+1}(s)>\cdots>
\Phi_\infty(s):=\frac{1}{I_0(2\sqrt{s})}.
\]
In addition, a bound valid simultaneously for every \(B\ge1\) and every \(s>0\) is
\[
0<\Phi_B(s)-\Phi_\infty(s)
\le\frac{s I_2(2\sqrt{s})}{2B(1+s)I_0(2\sqrt{s})}.
\]
For each finite \(S>0\), uniformly in \(0\le s\le S\), the *sharp* first-order correction is
\[
\boxed{\quad
\Phi_B(s)=\frac{1}{I_0(2\sqrt{s})}
+\frac{sI_2(2\sqrt{s})}{2B I_0(2\sqrt{s})^2}
+O_S(B^{-2}).\quad}
\]
Its \(B^{-1}\) coefficient is strictly positive for every \(s>0\). Consequently \(Y_B\) converges in law to the first time that the diffusion with generator \(x\partial_x^2+\partial_x\), started at zero, reaches one. In the same normalization, \(\mathbb E[Y_B]=1\) and
\[
\operatorname{Var}(Y_B)=\frac{B+1}{2B}>\frac12
=\operatorname{Var}(Y_\infty).
\]
Thus mean-matched passage fluctuations approach their classical limit from one side, with a nonzero explicitly calibrated first-order correction for every positive Laplace argument.

## Assumptions and scope

The positive integer \(B\) is an absorbing *number-state* threshold: surviving Fock levels are \(\{0,1,\dots,B-1\}\), with a reflecting bottom at level zero. The physical noise yields the infinite-temperature master equation, restricted to diagonal populations and taken in the limit of vanishing stroboscopic measurement interval. The resulting birth-death process jumps from level \(n\) to \(n+1\) at rate \(\kappa(n+1)\) and from \(n\) to \(n-1\) at rate \(\kappa n\). We start from \(n=0\). These dynamics and their finite-level Laguerre first-passage transform are in Ryan et al. (2026), equations (10), (27)--(29); they are *inputs*, not claimed as new results.

The time \(Y_B\) is normalized by the *integer threshold* \(B\), not by the oscillator energy \(B+1/2\) in zero-point-shifted units. The limiting diffusion is at a fixed *rescaled threshold one*. All stated order inequalities concern Laplace transforms at the same \(s\), not cumulative distribution functions or a pathwise coupling. No result here treats finite, nonzero measurement intervals or nonvacuum initial states.

## Proof

**1. Exact transform and series.** Rescale physical time by \(\kappa\). If \(u_n(q)=\mathbb E_n[e^{-q\kappa T_B}]\), the stopped backward equation and boundary condition are
\[
(2n+1+q)u_n=(n+1)u_{n+1}+nu_{n-1}\quad(0\le n<B),
\qquad u_B=1,
\]
with the term involving \(u_{-1}\) omitted at \(n=0\). Standard Laguerre polynomials obey \((2n+1+q)L_n(-q)=(n+1)L_{n+1}(-q)+nL_{n-1}(-q)\), with \(L_0(-q)=1\); hence uniqueness of the finite Dirichlet problem gives \(u_n(q)=L_n(-q)/L_B(-q)\). In particular, at \(q=s/B\), \(\Phi_B(s)=1/L_B(-s/B)\). The numerator identity and the finite boundary problem also confirm a.s. absorption and normalization at \(s=0\).

Put \(A_B(s)=L_B(-s/B)\) and, for integers \(k\ge0\),
\[
p_{B,k}=\begin{cases}\displaystyle\prod_{j=0}^{k-1}(1-j/B),&0\le k\le B,\\0,&k>B.\end{cases}
\]
Then exactly
\[
A_B(s)=\sum_{k=0}^{\infty}\frac{s^k}{(k!)^2}p_{B,k},
\qquad
I_0(2\sqrt s)=\sum_{k=0}^{\infty}\frac{s^k}{(k!)^2}.
\]
Each \(p_{B,k}\) is nondecreasing in \(B\), and \(p_{B,2}\) strictly increases for \(B\ge1\). For fixed \(k\), \(p_{B,k}\uparrow1\). Therefore for \(s>0\), \(1+s\le A_B(s)<A_{B+1}(s)<I_0(2\sqrt s)\), the last limit following from dominated convergence. Taking reciprocals proves the strict order.

**2. A global quantitative bound.** For \(k\le B\), the elementary product/union bound gives
\[
0\le 1-p_{B,k}\le\sum_{j=0}^{k-1}\frac jB=\frac{k(k-1)}{2B}.
\]
For \(k>B\), the same inequality holds because \(k(k-1)/(2B)\ge1\) whenever \(k\ge B+1\) and \(B\ge1\). Consequently
\[
0<I_0(2\sqrt s)-A_B(s)
\le\frac1{2B}\sum_{k=0}^{\infty}\frac{k(k-1)s^k}{(k!)^2}
=\frac{sI_2(2\sqrt s)}{2B}.
\]
Since \(A_B(s)\ge1+s\), dividing by \(A_B(s)I_0(2\sqrt s)\) proves the claimed nonasymptotic Laplace error bound.

**3. Uniform asymptotic expansion.** Write \(h=k(k-1)/(2B)\). The elementary second-order Bonferroni bound for a finite product yields, for \(k\le B\),
\[
0\le p_{B,k}-(1-h)\le h^2/2.
\]
When \(k>B\), \(p_{B,k}=0\) and \(\lvert p_{B,k}-(1-h)\rvert=\lvert h-1\rvert\le k^4/B^2\). Combining the two regimes (with a universal constant) gives
\[
\left|p_{B,k}-1+\frac{k(k-1)}{2B}\right|\le\frac{k^4}{B^2},\qquad B\ge1,\quad k\ge0.
\]
For any fixed \(S>0\), the series \(\sum_{k\ge0}k^4 S^k/(k!)^2\) converges. Hence the expansion
\[
A_B(s)=I_0(2\sqrt s)-\frac{sI_2(2\sqrt s)}{2B}
+O_S(B^{-2})
\]
holds *uniformly* for \(s\in[0,S]\). Using \(A_B(s)\ge1\) and \(I_0(2\sqrt s)\ge1\), a reciprocal expansion gives the displayed uniform expansion for \(\Phi_B\). Positivity of \(I_2(z)\) for \(z>0\), immediate from its series with positive terms, makes its rate coefficient sharp and nonzero.

**4. Identification of the limiting law and finite variance.** A continuous nonnegative diffusion started at zero with generator \(\mathcal Af(x)=xf''(x)+f'(x)\) has the regular bounded backward solution of \(\mathcal Au=su\), \(u(1)=1\), given by
\[
u_s(x)=\frac{I_0(2\sqrt{sx})}{I_0(2\sqrt{s})}.
\]
Its hitting time of one has Laplace transform \(u_s(0)=1/I_0(2\sqrt{s})\); the unique bounded solution at the entrance/instantaneously reflecting zero boundary excludes the logarithmically singular second Bessel solution. Standard Laplace-transform continuity yields \(Y_B\Rightarrow Y_\infty\). Finally
\[
A_B(s)=1+s+\frac{B-1}{4B}s^2+O(s^3),
\]
so Taylor expansion of \(A_B^{-1}\) at zero gives \(\mathbb E[Y_B]=1\) and \(\mathbb E[Y_B^2]=(3B+1)/(2B)\). Their difference gives \(\operatorname{Var}(Y_B)=(B+1)/(2B)\). The limiting series yields \(\operatorname{Var}(Y_\infty)=1/2\). All derivatives are legitimate since the finite killed chain has an exponential tail, while the limiting diffusion has an exponential hitting-time tail (or by the finite-radius analytic transform).

## Verification

Run `python check.py` using Python 3.9 or later, without external packages. The checker independently solves the finite backward equations with exact rational Gaussian elimination for thresholds through twelve and four rational Laplace arguments, checks the transformed Laguerre formula, tests the strict transform order at sixteen thresholds and six positive arguments, checks the sign and first-order coefficient against separately summed Bessel series, and verifies the exact finite variance for 499 thresholds. The completed checker reports 1,232 successful assertions. These are diagnostics; the proof above, not extrapolation from numerical tests, establishes every universal quantifier.

For example, at \(s=1\), \(\Phi_1=1/2\), \(\Phi_2=8/17\), and \(\Phi_\infty\approx0.438676279837\). The sharp coefficient of \(B^{-1}\) at \(s=1\) is approximately \(0.0662895443584\).

## Relationship to prior work

Ryan, Gorbaty, Teitsworth and Noel (2026) derive the exact finite-threshold transform for *arbitrary* initial number states in their Appendix A, equation (29), and describe the leading classical crossover using the Mehler--Heine formula in Appendix B. Their figure 4 examines the divergence of quantum and classical first-passage densities at particular thresholds. Those identities and the leading limit are prior results. The present theorem instead establishes a comparison *among all rescaled thresholds*, proves strict global one-sided Laplace convergence, supplies a nonasymptotic bound uniform in every threshold, and extracts an explicit positive first correction to the entire transform uniformly on compact Laplace intervals. The exact classical hitting transform follows as a direct consequence of the known diffusion model.

The NIST Digital Library of Mathematical Functions §18.11.6 records the classical leading Mehler--Heine limit for Laguerre polynomials. Deaño, Huertas and Marcellán (2013) develop higher-order Laguerre asymptotics and thus represent a potential general source of the algebraic expansion technique. Neither source, in the inspected relevant material, states the strict finite-threshold first-passage ordering or the combined physical Laplace error law. The first correction alone is elementary once the published exact Laguerre representation is given; originality is attached to the comparison-plus-uniform-quantification theorem, not to discovery of a new special-function identity.

## Limitations

The claims are for the infinite-frequency monitoring limit and a ground-state start. They do not imply stochastic dominance of passage times or pointwise ordering of their distribution functions; Laplace-transform order is weaker. The uniform asymptotic expansion is on each bounded \(s\)-interval, not on the full positive half-line with a constant independent of \(s\). The diffusion benchmark uses the threshold rescaling \(B\), whereas the full oscillator energy threshold contains a zero-point \(1/2\) shift. General higher-order Laguerre expansions could yield the algebraic \(B^{-1}\) term under specialization; the global finite-threshold monotonicity and joint rate certificate are the proposed distinct structural conclusion. Independent mathematical novelty review has not been conducted.

## References

1. Joseph M. Ryan, Simon Gorbaty, Stephen W. Teitsworth and Crystal Noel, *Quantum-classical crossover in noisy monitored oscillators*, arXiv:2608.08267v1 (first public 2026-08-08), https://arxiv.org/abs/2608.08267 . Read sections III.1 and Appendices A--B for finite transform, normalization, and classical limit.
2. NIST Digital Library of Mathematical Functions, §18.11.6, *Mehler--Heine type formulas: Laguerre*, https://dlmf.nist.gov/18.11.E6 .
3. Alfredo Deaño, Edmundo J. Huertas and Francisco Marcellán, *Strong and ratio asymptotics for Laguerre polynomials revisited*, arXiv:1301.4266 (first public 2013-01-17), https://arxiv.org/abs/1301.4266 . Read Introduction and sections 2--3 for higher-order special-function asymptotics.
4. Edgar Martin, Ulrich Behn and Guido Germano, *First-passage and first-exit times of a Bessel-like stochastic process*, Physical Review E **83**, 051115 (2011), https://doi.org/10.1103/PhysRevE.83.051115 . Related classical first-passage background; only abstract available for comparison.
