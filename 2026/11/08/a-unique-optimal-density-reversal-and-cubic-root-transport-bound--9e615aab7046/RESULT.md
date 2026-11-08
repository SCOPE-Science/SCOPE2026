# A unique optimal-density reversal and cubic-root transport boundary layer in tandem exclusion

## Finding

Consider the stationary thermodynamic current of the tandem exclusion process (TEP), whose directed allowed updates are \(110\to101\) at rate \(\alpha\) and \(101\to011\) at rate \(\beta=q\alpha\). Define \(\rho_*(q)\) as the density maximizing this current among all \(0<\rho<1\), and let \(J_*(q)\) be the corresponding current. For **every** \(q>0\), the maximizer is unique. Its location has a single reversal:

\[
\rho_*'(q)<0\quad(0<q<q_c),\qquad \rho_*'(q)>0\quad(q>q_c),
\]

where \(q_c\) is the **unique positive root** of

\[
7q^4+12q^3+94q^2+20q-53=0.
\]

Numerically, \(q_c=0.623631289268772\ldots\), and the strict global minimum of the maximizing density is \(\rho_*(q_c)=0.663810878206103\ldots\). The endpoint laws are

\[
\begin{aligned}
\rho_*(q)&=\frac1{\sqrt2}-\frac q4+O(q^2),&
\frac{J_*(q)}\alpha&=3-2\sqrt2+\left(\frac92-3\sqrt2\right)q+O(q^2),&&q\downarrow0,\\
\rho_*(q)&=1-2^{-2/3}q^{-1/3}+O(q^{-2/3}),&
\frac{J_*(q)}\alpha&=1-3\cdot2^{-2/3}q^{-1/3}+O(q^{-2/3}),&&q\to\infty.
\end{aligned}
\]

In the same strong-recovery limit, the equilibrium Gibbs correlation length \(\xi_*(q)=\xi(\rho_*(q),q)\) obeys

\[
\xi_*(q)\sim2^{-1/3}q^{1/3}.
\]

This optimal-density cube-root scaling is different from the previously established square-root scaling at any fixed interior particle density. These results classify **the global optimal-density path**, not only current at fixed density.

## Assumptions and scope

Take \(\alpha>0\), \(\beta>0\), \(q=\beta/\alpha\), and the thermodynamic limit of the translation-invariant Gibbs stationary state on the dynamically active sector of the periodic TEP, followed by an optimization over particle density \(0<\rho<1\). The stationary current and two-point correlation-length formula used as input are established in Ngo Phuoc Nguyen Ngoc, Lam Thi Nhung, and Huynh Anh Thi, *Tandem Exclusion Process*, arXiv:2606.01568v1, equations (10)–(12) and (17)–(18). No finite-ring maximum-current theorem is asserted. In particular, the order of the large-system limit and density optimization is fixed in this statement.

Following the source parameterization, introduce \(s>0\) and

\[
\rho(s,q)=\frac{s(qs+1)}{qs^2+2s+1},\qquad
j(s,q)=\frac{J}{\alpha}=
\frac{q s^2((q+1)s+2)}{(s+1)(qs+1)(qs^2+2s+1)}.
\]

These formulae are equivalent to the source equation \(q(1-\rho)s^2+(1-2\rho)s-\rho=0\) and its stationary current. The \(s\) coordinate maps \((0,\infty)\) bijectively onto \((0,1)\) in density, because

\[
\frac{\partial\rho}{\partial s}=
\frac{qs^2+2qs+1}{(qs^2+2s+1)^2}>0.
\]

## Proof

**1. A single maximum for each rate ratio.** Direct differentiation gives

\[
\frac{\partial j}{\partial s}=
-\frac{qsP(s,q)}{(s+1)^2(qs+1)^2(qs^2+2s+1)^2},
\]

where

\[
\begin{aligned}
P(s,q)={}&q^2(q+1)s^5+4q^2s^4-2(q^2+1)s^3\\
&-(2q^2+8q+6)s^2-(5q+9)s-4.
\end{aligned}
\]

For any \(q>0\), the descending coefficient signs of this polynomial are \(+,+,-,-,-,-\). Descartes' rule therefore bounds the number of positive roots by one, counted with multiplicity. Since \(P(0,q)=-4\) and \(P(s,q)\to+\infty\) as \(s\to\infty\), there is exactly one positive root \(s_*(q)\), which is simple and changes \(P\)'s sign from negative to positive. Because \(j(0+,q)=j(+\infty,q)=0\), this root gives the unique strict global maximum. It depends real-analytically on \(q>0\) by the implicit-function theorem.

**2. Exact elimination for optimal-density stationary points.** Along \(P(s_*(q),q)=0\), implicit differentiation yields

\[
\rho_*'(q)=\frac{\rho_qP_s-\rho_sP_q}{P_s},
\]

all partial derivatives evaluated at \((s_*(q),q)\). Put

\[
H(s,q)=\frac{(qs^2+2s+1)^2}{s}(\rho_qP_s-\rho_sP_q),
\]

which expands to a polynomial. An exact polynomial resultant computation, independently replayable using `verify.py`, gives

\[
\operatorname{Res}_{s}(P,H)=16q^6(q-1)^{12}
(7q^4+12q^3+94q^2+20q-53).
\]

Thus any positive-\(q\) zero of \(\rho_*'(q)\) belongs to \(\{1,q_c\}\), with \(q_c\) as displayed in the finding. The quartic is strictly increasing for \(q>0\), with negative value at zero and positive limit at infinity; hence exactly one positive root exists. At \(q=1\), the polynomial factorizes as

\[
P(s,1)=2(s-2)(s+1)^4,
\]

and direct substitution in the derivative identity gives \(\rho_*'(1)=1/81>0\): the large power of \(q-1\) in the resultant arises from other algebraic branches and does **not** represent an optimal-density stationary point.

**3. Weak-recovery asymptotics and sign.** Let \(t=qs\). Multiplying the critical-point polynomial by \(q^3\) and replacing \(s=t/q\) gives the analytic equation

\[
\begin{aligned}
0={}&t^5-2t^3+q(t^5+4t^4-6t^2)\\
&+q^2(-2t^3-8t^2-9t)+q^3(-2t^2-5t-4).
\end{aligned}
\]

The unique positive root has \(t\to\sqrt2\) as \(q\downarrow0\), because the limiting root is simple and the one-positive-root property excludes other branches. Applying the analytic implicit-function theorem and substituting into \(\rho(s,q)\) and \(j(s,q)\) gives the weak-recovery expansions above, including \(\rho_*'(q)\to-1/4\).

**4. Strong-recovery asymptotics and sign.** Set \(\varepsilon=q^{-1/3}\) and \(s=\varepsilon u\). After multiplication by \(\varepsilon^4\), the critical-point polynomial is analytic in \((\varepsilon,u)\) near \(\varepsilon=0\) and tends to \(u^2(u^3-2)\). Its positive nonzero root \(u_0=2^{1/3}\) is simple; the single-positive-root property fixes \(s_*(q)=2^{1/3}q^{-1/3}+O(q^{-2/3})\). Substitution yields the strong-recovery density and maximal-current expansions. Analyticity in \(\varepsilon\) also yields \(\rho_*'(q)=\frac13 2^{-2/3}q^{-4/3}+O(q^{-5/3})>0\) for large \(q\).

The derivative can vanish only at \(q_c\) or at \(q=1\), which has already been excluded. Since it is negative near zero and positive for large \(q\), continuity forces a sign change at \(q_c\), and no other change is possible. This proves the unique strict global minimum and both monotonicity intervals.

**5. Correlations along the optimal-density path.** From the source transfer matrix, the ratio of the subdominant to dominant eigenvalue simplifies to

\[
R(s,q)=\frac{\lambda_-}{\lambda_+}
=\frac{(q-1)s}{(1+s)(1+qs)}.
\]

For \(q\ne1\), \(\xi(s,q)=-1/\log|R(s,q)|\), and \(\xi=0\) at \(q=1\). Along the optimal path with \(s_*(q)=2^{1/3}q^{-1/3}+O(q^{-2/3})\), the eigenvalue ratio satisfies \(R(s_*(q),q)=1-2^{1/3}q^{-1/3}+O(q^{-2/3})\). Consequently \(\xi_*(q)\sim2^{-1/3}q^{1/3}\), as claimed. This change in exponent is due to letting the optimizing density tend to one together with \(q\), rather than holding density fixed.

## Verification

`verify.py` contains executable, self-contained SymPy identities for the stationary-density parameterization, differentiated current, degree-five critical-point polynomial, exact resultant, exclusion of the spurious \(q=1\) resultant factor, and both limiting algebraic equations. It also tests 15 finite-ring Gibbs global-balance cases by exact rational arithmetic (five ring sizes and three positive recovery ratios), then checks critical-parameter roots and representative finite-parameter values via bisection, along with the cube-root scaling of density, current and correlation length. Run with `python verify.py` in an environment with Python and SymPy. All analytic claims above are proved by sign-counting, resultant exclusion, analytic implicit-function arguments and transfer-matrix identities; numerical spot checks are not substituted for proofs.

For orientation, \(\rho_*(0.5)\approx0.664382053\), \(\rho_*(1)=2/3\), \(\rho_*(2)\approx0.681831996\). At \(q=q_c\) the minimum is approximately \(0.663810878\).

## Relationship to prior work

The source preprint proves the active-sector Gibbs invariant state, derives **the full current formula** and **the full correlation-length formula**, and notes that the maximizing density is greater than one half, close to two thirds in its plots. Its fixed-density strong-recovery current law \(J\to\alpha\rho\) and fixed-density correlation length \(\xi\propto q^{1/2}\) are prior results. This note does not claim those formulas, stationary measures, or current asymmetry as new. The claim here is the unique global optimizing density for every rate ratio, a nonmonotone optimizer path with an exact algebraic crossover, two matched optimal-current boundary expansions, and the **optimized** cube-root correlation length. That optimization is not asserted in the inspected source sections or appendices. Broader cooperative-exclusion literature does study nonmonotone transport in other models, but no located statement gives this precise global optimizer classification for these update rules. Search non-detection is not proof of priority.

## Limitations

The theorem is thermodynamic and stationary; it does not establish finite-size optimality, convergence times, open-boundary phase selection, hydrodynamic stability, or the uniqueness of dynamical attractors outside the specified active-sector Gibbs state. As the density varies in the thermodynamic limit, the active-sector limit is interpreted according to the source stationary-current theorem. The endpoint \(q=0\) and \(q=\infty\) are limiting regimes, not finite-rate transitions. The small-parameter expansions are at fixed positive head-move rate \(\alpha\). Any broader unindexed theorem subsuming this exact one-parameter optimization would affect publication priority, which has not been independently certified.

## References

1. Ngo Phuoc Nguyen Ngoc, Lam Thi Nhung, and Huynh Anh Thi, *Tandem Exclusion Process*, arXiv:2606.01568v1, first submitted 1 June 2026, https://arxiv.org/html/2606.01568v1 . Particularly Theorem 4 and equations (10)–(12), (17)–(19), with transfer-matrix Appendix B.
2. Dong et al., *Entrainment and Unit Velocity: Surprises in an Accelerated Exclusion Process*, Physical Review Letters 109 (2012), 130602, https://arxiv.org/abs/1208.4089 . Different accelerated-exclusion rules; used only as broad related-model context.
