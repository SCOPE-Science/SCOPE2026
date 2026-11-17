# Exact duty-cycle and period thresholds for a mirror-switched two-community epidemic

## Finding

Let two contact patterns exchange which community has the higher within-community contact rate, while preserving the cross-community contact rate. In the two-community susceptible--infectious--susceptible (SIS) individual-based approximation, the complete linear invasion exponent is explicit for **every** positive switching period and **every** duty fraction. Its minimum over duty fractions is uniquely attained by an equal-time schedule. More substantially, the formula supplies the **exact full region of schedules that suppress an outbreak even though both static contact patterns individually permit invasion**, including a unique maximal viable switching period and its square-root closing law.

Use the notation below. For all \(T>0\) and \(0\le\theta\le1\), the principal Floquet exponent is
\[
\Lambda(T,\theta)=h+\frac1T\operatorname{arcosh}\!\left[\frac{u^2}{q^2}\cosh(qT)+\frac{v^2}{q^2}\cosh(qT(2\theta-1))\right].
\]
For each fixed \(T\), it has the unique minimizer \(\theta=1/2\), and its maximal value \(h+q\) occurs precisely at the two static endpoints. Its minimum
\[
\Lambda_*(T)=h+\frac2T\operatorname{arsinh}\!\left(\frac uq\sinh\frac{qT}{2}\right)
\]
is strictly increasing in \(T>0\), with endpoint limits \(h+u\) and \(h+q\).

A strict two-static-supercritical/periodic-subcritical paradox exists for some schedule if and only if
\[
h+u<0<h+q.
\]
Under this condition there is a unique \(T_c>0\) satisfying \(\Lambda_*(T_c)=0\). For \(0<T<T_c\), **exactly** the duty fractions
\[
\theta_-(T)<\theta<\theta_+(T),\qquad
\theta_\pm(T)=\frac12\left(1\pm\frac{\operatorname{arcosh}Z(T)}{qT}\right),
\quad
Z(T)=\frac{q^2\cosh(-hT)-u^2\cosh(qT)}{v^2}
\]
yield \(\Lambda(T,\theta)<0\). At \(T=T_c\), only the balanced duty fraction is neutral, and for \(T>T_c\) all schedules have positive invasion exponent. The interval edges obey
\[
\lim_{T\downarrow0}\theta_\pm(T)=\frac12\left(1\pm\frac{\sqrt{h^2-u^2}}v\right),
\]
and, as \(T\uparrow T_c\),
\[
\theta_\pm(T)=\frac12\pm\frac{\sqrt{-2Z'(T_c)}}{2qT_c}\sqrt{T_c-T}+O((T_c-T)^{3/2}),\quad Z'(T_c)<0.
\]
For every subcritical schedule in this region, every nonlinear SIS approximation trajectory starting in \([0,1]^2\) converges exponentially to the disease-free state.

## Assumptions and scope

Choose arbitrary real \(a>c\ge0\), \(b>0\), infection rate \(\beta>0\), and recovery rate \(\mu>0\). The two symmetric nonnegative contact matrices are
\[
A_+=\begin{pmatrix}a&b\\b&c\end{pmatrix},\qquad
A_-=\begin{pmatrix}c&b\\b&a\end{pmatrix}.
\]
They act successively for \(\theta T\) and \((1-\theta)T\) within each period \(T>0\), repeated indefinitely. The nonlinear model on \([0,1]^2\) is
\[
\dot x_i=\beta(1-x_i)\sum_{j=1}^{2}(A_\pm)_{ij}x_j-\mu x_i.
\]
Its disease-free linearizations are \(L_\pm=\beta A_\pm-\mu I\). Set
\[
h=\frac{\beta(a+c)}2-\mu,\quad
u=\beta b>0,\quad v=\frac{\beta(a-c)}2>0,\quad q=\sqrt{u^2+v^2}.
\]
The exponent is \(T^{-1}\log\rho(e^{(1-\theta)TL_-}e^{\theta TL_+})\), where \(\rho\) is the spectral radius. Positive off-diagonal contact ensures irreducibility and an unambiguous positive Perron multiplier. The endpoint values \(\theta=0,1\) are admitted as static schedules, but strict paradoxes require interior fractions. This result concerns the two-dimensional individual-based approximation and its linear threshold, not exact finite-population stochastic extinction times or total infection burden.

## Proof

**Exact monodromy trace.** Let \(X=\begin{pmatrix}0&1\\1&0\end{pmatrix}\), \(Z=\operatorname{diag}(1,-1)\). Then \(L_+=hI+uX+vZ\) and \(L_-=hI+uX-vZ\). The traceless parts \(R_\pm=uX\pm vZ\) satisfy \(R_\pm^2=q^2I\), and
\[
e^{tL_\pm}=e^{ht}\left(\cosh(qt)I+\frac{\sinh(qt)}q R_\pm\right).
\]
The product has determinant \(e^{2hT}\) and normalized half-trace
\[
\Xi=\cosh(q\theta T)\cosh(q(1-\theta)T)
+\frac{u^2-v^2}{q^2}\sinh(q\theta T)\sinh(q(1-\theta)T)
=\frac{u^2}{q^2}\cosh(qT)+\frac{v^2}{q^2}\cosh(qT(2\theta-1)).
\]
Because both exponentials are positive definite and their product has positive real eigenvalues, and because \(\Xi>1\), the Perron multiplier is \(\exp(hT+\operatorname{arcosh}\Xi)\). This proves the first formula with no small-period approximation.

**Duty optimum and period order.** Since \(v>0\), the second term in \(\Xi\) increases strictly with \(|2\theta-1|\); hence the balanced schedule uniquely minimizes the exponent. Its endpoints give \(\Xi=\cosh(qT)\) and \(\Lambda=h+q\). At the balance point use \(\operatorname{arcosh}(1+2z^2)=2\operatorname{arsinh}(z)\) for \(z\ge0\). Put \(k=u/q\in(0,1)\), \(s=qT/2\), and \(g(s)=\operatorname{arsinh}(k\sinh s)\). Direct differentiation yields
\[
g''(s)=\frac{k(1-k^2)\sinh s}{(1+k^2\sinh^2s)^{3/2}}>0\quad(s>0).
\]
Since \(g(0)=0\), strict convexity implies \(g(s)/s\) strictly increases. Its limits are \(k\) at zero and \(1\) at infinity. Substitution proves the claimed strict period order and limits.

**Exact suppression region.** Both static phases have exponent \(h+q\). If \(h+q\le0\), neither is strictly supercritical. If \(h+u\ge0\), then every positive-period balanced exponent is strictly positive, and all other duties are larger. The remaining parameter regime \(h+u<0<h+q\) has precisely one positive zero \(T_c\) of the strictly increasing continuous balanced exponent. For \(0<T<T_c\), \(\Lambda(T,1/2)<0<\Lambda(T,0)=\Lambda(T,1)\); strict order on each half of the duty domain gives exactly two boundary roots. Since \(h<0\), \(\Lambda(T,\theta)<0\) is equivalent to \(\Xi(T,\theta)<\cosh(-hT)\). Solving this inequality for \(|2\theta-1|\) gives the displayed \(Z(T)\) and boundaries, with \(1<Z(T)<\cosh(qT)\). At and beyond \(T_c\), no strict subcritical duty exists. Taylor expansion of \(Z(T)\) at zero proves the short-period edges. At the critical period, writing \(\Xi(T,1/2)=\cosh(T(\Lambda_*(T)-h))\) gives
\[
Z'(T_c)=-\frac{q^2}{v^2}\,T_c\Lambda_*'(T_c)\sinh(-hT_c)<0.
\]
The expansion \(\operatorname{arcosh}(1+z)=\sqrt{2z}+O(z^{3/2})\) gives the square-root narrowing.

**Nonlinear extinction.** The square \([0,1]^2\) is positively invariant: at \(x_i=0\) the component derivative is nonnegative and at \(x_i=1\) it is \(-\mu<0\). On that square, the nonlinear vector field is componentwise bounded above by the positive linear system \(\dot y=L(t)y\). Its matrices are Metzler, so the cooperative comparison principle implies \(0\le x(t)\le y(t)\) for matching nonnegative initial values. If \(\Lambda<0\), the periodic linear fundamental matrix decays exponentially. Therefore the nonlinear infection probabilities decay exponentially as well. No necessity claim about nonlinear global behavior is made at \(\Lambda=0\).

## Verification

The accompanying standalone standard-library program `verify.py` constructs direct Taylor/scaling-and-squaring approximations to both matrix exponentials and checks the resulting Perron exponent against the formula over a multi-parameter grid of periods and duty fractions. It also checks the exact example's root and duty boundaries and the derivative identity numerically. These finite calculations are reproducibility checks, not the proof for continuous parameter domains.

For \(a=2,c=0,b=1/2,\beta=1,\mu=7/4\), one has \(h=-3/4,u=1/2,v=1,q=\sqrt5/2\). Both static phases grow at rate \((2\sqrt5-3)/4>0\), while the infinitely fast balanced average has rate \(-1/4\). The unique switching-period cutoff is
\[
T_c=4.18273078248912424167\ldots .
\]
At \(T=2\), the optimized exponent is \(-0.17187290456102275\ldots\) and the exact suppression interval has endpoints \(0.23970358622398983\ldots\) and \(0.76029641377601017\ldots\).

## Relationship to prior work

Sejunti, Taylor, and Masuda (arXiv:2406.16787, first submitted June 24, 2024) introduced the epidemic Parrondo paradox for periodic switching SIS contact patterns, including a two-community case. Their study gives numerical comparisons at a fixed unequal schedule and a perturbative infection-rate expansion, but not the exact optimal-duty/period suppression region for the mirror-exchanged contact class. The mirror-exchanged class is an intentionally structured, natural two-community subclass; it is not claimed to cover arbitrary pairs of contacts.

Earlier matrix-exponential convexity work (Cohen, Friedland, Kato, and Kelly, 1982; Lieb, 1990) explains general monotonicity/convexity phenomena for some matrix products. In particular, the fact that a balanced or fast schedule can be favorable must **not** be interpreted as a new general matrix inequality. The contribution asserted here is the epidemic-specific **joint exact phase diagram**: complete analytic boundaries for every period and duty, a unique sharp maximum period, and quantitative narrowing of its feasible scheduling interval. The 2004 Floquet switching work of Gökçek discusses fast-switching stabilization more generally but does not, in the material accessible for this comparison, establish the displayed exact two-parameter band.

## Limitations

The contact pair has equal off-diagonal weights and diagonals exchanged exactly; the theorem says nothing about general asymmetric matrices, more communities, or more than two contact phases. Subcritical Floquet growth guarantees extinction in the deterministic SIS approximation, not a sharp extinction-time law for a finite stochastic epidemic. At zero Floquet exponent the rate of nonlinear relaxation is not determined. Earlier general log-convexity may subsume the monotonicity component, and publication-priority uncertainty remains for equivalent unindexed special-case calculations or broader scheduling results.

## References

1. M. I. Sejunti, D. Taylor, N. Masuda, *A Parrondo paradox in susceptible-infectious-susceptible dynamics over periodic temporal networks*, arXiv:2406.16787 (first public version 2024-06-24), https://arxiv.org/abs/2406.16787 ; full HTML of version 3: https://arxiv.org/html/2406.16787v3 .
2. J. E. Cohen, S. Friedland, T. Kato, F. P. Kelly, *Eigenvalue Inequalities for Products of Matrix Exponentials*, Linear Algebra and its Applications **45** (1982), 55–95, https://lab.rockefeller.edu/cohenje/PDFs/099CohenFriedlandKatoKellyLAA1982.pdf .
3. E. H. Lieb, *On the spectral radius of the product of matrix exponentials*, Linear Algebra and its Applications **141** (1990), 271–273, https://doi.org/10.1016/0024-3795(90)90324-6 .
4. C. Gökçek, *Stability analysis of periodically switched linear systems using Floquet theory*, Mathematical Problems in Engineering (2004), https://doi.org/10.1155/S1024123X04401069 .
5. R. Persoons, M. Sensi, B. Prasse, P. Van Mieghem, *Transition from time-variant to static networks: Timescale separation in N-intertwined mean-field approximation of susceptible-infectious-susceptible epidemics*, Physical Review E **109** (2024), 034308, https://doi.org/10.1103/PhysRevE.109.034308 .
