# A sharp one-ninth refractory threshold for topological acceleration by resetting

## Finding

For a Brownian particle on a ring, resetting along the shortest arc can complete a winding, but a safe-zone reset instead renews the experiment. If safe-zone resets are followed by an independent refractory wait of finite mean \(\delta\), **some positive reset rate is faster than no resetting precisely when the mean wait is smaller than one ninth of the unreset mean winding time**:

\[
\boxed{\delta<\frac{L^2}{18D}=\frac{\mathbb E T_0}{9}}.
\]

The boundary is strict: at equality and beyond, every nonzero reset rate is slower. This criterion is the same for all nonnegative refractory-time distributions with the given finite mean. Below the boundary, a global mean-minimizing positive reset rate exists; uniqueness is not asserted.

## Assumptions and scope

Fix \(L>0\), \(D>0\), and \(r\ge0\). The particle begins at lifted arclength \(0\), diffuses with generator \(D\partial_{xx}\), and completes a clockwise or counterclockwise turn when its lift first reaches \(L\) or \(-L\). Reset attempts arrive according to an independent Poisson process of rate \(r\) while the particle is actively diffusing. At a reset:

- If the pre-reset lift satisfies \(|X|<L/2\), the particle travels instantaneously back to \(0\) along the shortest arc without completing a winding, incurs a nonnegative refractory duration \(W\), and then starts a statistically fresh attempt.
- If the pre-reset lift satisfies \(|X|>L/2\), return along the shortest arc completes a winding immediately, and the process ends with no refractory wait.

The midpoint convention at \(|X|=L/2\) does not affect the law because a reset samples an absolutely continuous position. The waits are independent and identically distributed, independent of the active Brownian motion and Poisson clocks, and satisfy \(\mathbb EW=\delta<\infty\). No reset attempts occur during a refractory wait. Physical completion time includes all refractory waits, but a return jump itself takes zero time. There is no energetic cost term.

Put
\[
z=\frac L2\sqrt{\frac rD},\qquad d=\frac{\delta D}{L^2}.
\]

For \(r>0\), the exact physical mean is
\[
\boxed{\mathbb E T_r=\frac{\cosh(2z)-1}{r\cosh z}
+\delta\left(\frac{\cosh(2z)}{\cosh z}-1\right).}
\]
At \(r=0\), direct absorbing-Brownian first passage gives \(\mathbb E T_0=L^2/(2D)\).

## Proof

**1. Single active attempt and its safe-reset probability.** Let \(\tau\) be the ordinary first exit of the diffusion from \((-L,L)\), and let \(E_r\) be an independent exponential time of rate \(r>0\). Each active attempt lasts \(A=\min(\tau,E_r)\). The killed-Brownian resolvent at initial point \(0\), with \(k=\sqrt{r/D}\), has density
\[
G_r(y)=\frac{\sinh(k(L-|y|))}{2Dk\cosh(kL)},\quad |y|<L.
\]
This solves \((r-D\partial_{yy})G_r=\delta_0\) with zero boundary values, by continuity and the derivative jump at \(0\). Hence the probability that an active attempt ends in a safe-zone reset, rather than completing the winding, is
\[
p_s=r\int_{-L/2}^{L/2}G_r(y)\,dy
=1-\frac{\cosh(kL/2)}{\cosh(kL)}
=1-\frac{\cosh z}{\cosh(2z)}.
\]
In particular \(0<p_s<1\). The expectation of active duration is
\[
\mathbb E A=\int_0^\infty e^{-rt}\mathbb P(\tau>t)\,dt
=\frac{1-\mathbb E[e^{-r\tau}]}r
=\frac{1-\operatorname{sech}(kL)}r,
\]
where \(\mathbb E[e^{-r\tau}]=\operatorname{sech}(kL)\) follows from the Dirichlet problem \(Du''=ru\), \(u(\pm L)=1\), evaluated at the origin.

**2. Physical-time renewal.** A failed active attempt contributes its active duration and then a wait of independent mean \(\delta\), followed by a fresh completion time. Thus
\[
m_r=\mathbb E A+p_s(\delta+m_r).
\]
Since \(p_s<1\), the expected number of attempts is finite, and solving gives the exact formula in the statement. Only \(\mathbb EW\) enters. For \(r=0\), the solution to \(Du''=-1\), \(u(\pm L)=0\), gives the baseline.

**3. Sharp threshold, including equality.** Write \(F_d(z)=Dm_r/L^2\) with \(r=4Dz^2/L^2\). Then
\[
F_d(z)=\frac{\cosh(2z)-1}{4z^2\cosh z}
+d\left(\frac{\cosh(2z)}{\cosh z}-1\right),
\]
and its expansion as \(z\downarrow0\) is
\[
F_d(z)=\frac12+\left(\frac{3d}{2}-\frac1{12}\right)z^2+O(z^4).
\]
If \(d<1/18\), every sufficiently small \(z>0\) improves on the baseline \(1/2\).

For the converse it is enough to prove strict inferiority at the critical \(d_0=1/18\), because \(F_d(z)\) increases strictly with \(d\) for each \(z>0\). Define the positive-factor-cleared difference
\[
G(z)=4z^2\cosh z\,[F_{1/18}(z)-1/2]
=\left(1+\frac{2z^2}{9}\right)\cosh(2z)
-\frac{20z^2}{9}\cosh z-1.
\]
Its Taylor series is
\[
G(z)=\sum_{n=1}^\infty\frac{c_n z^{2n}}{(2n)!},\qquad
c_n=4^n+\frac{(2n)(2n-1)}9(2\cdot4^{n-1}-20).
\]
Direct substitution gives \(c_1=c_2=0\). For every integer \(n\ge3\), \(2\cdot4^{n-1}-20>0\), so \(c_n>0\). Consequently \(G(z)>0\) for every \(z>0\), proving that at \(d_0\) every \(r>0\) is strictly slower. For \(d>d_0\), the additional difference \((d-d_0)(\cosh 2z/\cosh z-1)\) is positive, yielding the same strict conclusion. The threshold is therefore both necessary and sufficient.

**4. Existence, without an unsupported uniqueness claim.** For \(d<1/18\), the small-rate improvement is strict. As \(z\to\infty\), the first term of \(F_d(z)\) grows asymptotically as \(e^z/(4z^2)\); all other contributions are nonnegative. Continuity and coercivity then imply that some \(0<r_*<\infty\) globally minimizes the mean, with \(m_{r_*}<m_0\). The proof does not classify the number of stationary points or establish uniqueness of this optimal rate.

## Verification

The included `verify.py` independently discretizes the backward equation for expected completion time on \((-L,L)\), with diffusion and reset terms on the interior, zero Dirichlet endpoint values, and the safe-zone renewal term \(r[m(0)+\delta]\). Its midpoint convention uses a symmetric half-weight grid cell. For \(L=D=1\), 40 rate/delay pairs agree with the analytic formula to absolute error below \(10^{-4}\) on the specified grid. The code also checks the Taylor coefficients through the 79th nontrivial index and the critical inequalities. Run `python verify.py` with dependencies in `requirements.txt`.

The proof of all-rates positivity is the analytic coefficient argument above, **not** the finite-difference experiment or a finite check of coefficients.

## Relationship to prior work

Grange [1] studies first winding completion on a Brownian ring with shortest-arc reset, including instantaneous completion from the dangerous zone, **without any refractory phase**. Evans and Majumdar [2] develop a general refractory-resetting renewal framework; its absorbing-target model does not analyze shortest-arc winding where a reset may itself be the terminal event. Pal and Prasad [3] analyze interval absorption with resetting to the initial position, where no reset is terminal. Sunil and coauthors [4] study additive costs of resets with a target on the line; their general cost formalism is relevant to restart penalties but does not state the global threshold for this ring mechanism.

The claim here is the exact **all-positive-rate** criterion for whether *any* reset can beat the no-reset winding mean, together with the strict boundary \(\mathbb E T_0/9\) and distributional invariance under arbitrary independent finite-mean waits. These results use known renewal machinery but require a sharp positive-series comparison in the ring-specific model. This does not establish priority over all literature, and derivability from combining prior general renewal formulas is an explicit residual risk.

## Limitations

The safe-zone return itself is instantaneous. A nonzero travel time, correlated refractory wait, reset attempts during the wait, non-Poisson reset timing, biased diffusion or other winding-completion conventions need new analysis. The result concerns mean physical completion time, not variance, distributional convergence, energetic efficiency, or uniqueness of a positive optimal rate. No independent scientific validation is asserted.

## References

[1] P. Grange, *Winding number of a Brownian particle on a ring under stochastic resetting*, arXiv:2111.15241 (first posted 2021-11-30), https://arxiv.org/abs/2111.15241.

[2] M. R. Evans and S. N. Majumdar, *Effects of refractory period on stochastic resetting*, arXiv:1809.01551 (first posted 2018-09-05), https://arxiv.org/abs/1809.01551.

[3] A. Pal and V. V. Prasad, *First passage under stochastic resetting in an interval*, arXiv:1812.03009 (2018), https://arxiv.org/abs/1812.03009.

[4] J. C. Sunil, R. A. Blythe, M. R. Evans and S. N. Majumdar, *The cost of stochastic resetting*, arXiv:2304.09348 (first posted 2023-04-19), https://arxiv.org/abs/2304.09348.
