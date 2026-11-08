# Global logarithmic prey escape and the critical predator-extinction clock

## Finding
For the discrete Holling-II predator–prey map
\[
\begin{aligned}
x_{n+1}&=x_n+r x_n e^{1-x_n}-\frac{\alpha x_ny_n}{1+x_n},\\
y_{n+1}&=y_n\left(1-\gamma+\frac{\alpha x_n}{1+x_n}\right),
\end{aligned}
\]
fix \(r>0\), \(0<\alpha\le\gamma\le1\), \(x_0>0\) and \(0<y_0<1/\alpha\). Every iterate is strictly positive; the predators decrease to zero, while the prey diverge. The sharp asymptotic laws are
\[
x_n=\log n+\log\log n+\log(re)+o(1),
\]
and, in the strictly subcritical regime \(\alpha<\gamma\),
\[
\lim_{n\to\infty}\frac1n\log\frac{y_n}{y_0}=\log(1-\gamma+\alpha)<0.
\]
At the critical boundary \(\alpha=\gamma\), the extinction is instead subexponential, with
\[
\boxed{\lim_{n\to\infty}\frac{\log n}{n}\log\frac{y_n}{y_0}=-\gamma.}
\]
In particular, the change of decay clock is sharp at the exact parameter boundary separating existence and nonexistence of a positive coexistence fixed point.

## Assumptions and scope
The map is evaluated at all nonnegative integer times, with its parameters held fixed. The strict bound \(\alpha y_0<1\) is part of the theorem: unlike some commonly studied population maps, this recurrence does not preserve the full positive quadrant for arbitrarily large predator initial data. The positive invariant region selected here is \(x>0\), \(0<y<1/\alpha\), when \(0<\alpha\le\gamma\le1\). The statement is for every positive initial state in this region, without restrictions on \(r\). All logarithms are natural.

## Proof
Write \(f(x)=r e\,x e^{-x}\), \(p_n=\alpha x_n y_n/(1+x_n)\), and \(q=1-\gamma+\alpha\). Since \(0<\alpha\le\gamma\le1\), the predator multiplier
\[
m_n=1-\gamma+\frac{\alpha x_n}{1+x_n}=q-\frac\alpha{1+x_n}
\]
is strictly between zero and one whenever \(x_n>0\). Thus \(0<y_{n+1}<y_n<1/\alpha\). The prey multiplier satisfies
\[
1+r e^{1-x_n}-\frac{\alpha y_n}{1+x_n}>1-\alpha y_0>0,
\]
proving strict positivity inductively. Also \(f(x)\le r\) for \(x>0\), because \(x e^{1-x}\le1\). Hence \(x_n\le x_0+rn\).

If \(\alpha<\gamma\), then \(y_{n+1}\le q y_n\) with \(0<q<1\), so \(y_n\to0\). If \(\alpha=\gamma\), then
\[
\frac{y_{n+1}}{y_n}=1-\frac\gamma{1+x_n}
\]
and \(\log y_n\le\log y_0-\gamma\sum_{j<n}(1+x_0+rj)^{-1}\to-\infty\). Thus \(y_n\to0\) in both cases.

Next prove \(x_n\to\infty\). Choose a sufficiently late index \(N\) so that \(\alpha y_n<\min\{1/2,r/2\}\) for \(n\ge N\). When \(x_n\le1\), the prey multiplier is at least \(1+r/2\); when \(x_n>1\), the next prey value is above \(1/2\). Therefore a constant \(a>0\) satisfies \(x_n\ge a\) for every \(n\ge N\). Fix \(B>1\). At sufficiently late times, if \(x_n\in[a,B+1]\), then
\[
x_{n+1}-x_n\ge a\left(r e^{-B}-\alpha y_n\right)>c_B>0.
\]
If \(x_n\ge B+1\), then \(x_{n+1}\ge x_n-\alpha y_n>B\). Once the orbit crosses \(B\) sufficiently late, it therefore never falls below \(B\). It must cross: otherwise positive increments of at least \(c_B\) would keep increasing a bounded sequence. As \(B\) is arbitrary, \(x_n\to\infty\).

For a quantitative upper bound, let \(F(x)=x+f(x)\). For sufficiently large \(K\), \(F'(x)>0\) for every \(x\ge K\). Start an auxiliary prey-only orbit \(v_N=x_N\) at a time when \(x_n\ge K\), and set \(v_{n+1}=F(v_n)\). Monotonicity of \(F\) and \(p_n\ge0\) give \(x_n\le v_n\) for \(n\ge N\). Define
\[
G(x)=\int_K^x\frac{dt}{f(t)}=\frac1{re}\int_K^x\frac{e^t}{t}\,dt.
\]
Since \(v_n\to\infty\), the mean-value theorem and \(f(v_n)\to0\) imply
\(G(v_{n+1})-G(v_n)=1+o(1)\). Hence \(G(v_n)\sim n\). Integration by parts gives \(G(x)\sim e^x/(re\,x)\), so \(v_n=\log n+\log\log n+\log(re)+o(1)\). In particular, \(x_n=O(\log n)\).

This upper bound strengthens the predator estimate. If \(\alpha=\gamma\), then \(y_{n+1}\le y_n\exp[-\gamma/(1+C\log(n+2))]\) for some fixed \(C>0\) and all large \(n\); hence \(y_n\le C_1\exp[-c n/\log(n+2)]\). If \(\alpha<\gamma\), the stronger geometric estimate already holds. In either case, since \(x_n\to\infty\) and \(x_n=O(\log n)\),
\[
\frac{p_n}{f(x_n)}=\frac{\alpha y_n e^{x_n}}{re(1+x_n)}\longrightarrow0.
\]
Thus \(x_{n+1}-x_n=f(x_n)(1+o(1))\) and these increments tend to zero. Reapplying the mean-value theorem to \(G\) yields \(G(x_{n+1})-G(x_n)=1+o(1)\); summation gives \(G(x_n)\sim n\). Therefore
\[
\frac{e^{x_n}}{re\,x_n n}\to1,
\]
which is equivalent to the asserted full three-term prey asymptotic.

Finally, if \(\alpha<\gamma\), then \(m_n\to q\in(0,1)\), and Cesàro averaging of \(\log(y_n/y_0)=\sum_{j<n}\log m_j\) proves the exponential logarithmic rate. If \(\alpha=\gamma\), then \(x_j\sim\log j\), and
\[
\log\frac{y_n}{y_0}=\sum_{j<n}\log\left(1-\frac\gamma{1+x_j}\right)
=-\gamma\sum_{j<n}\frac1{1+x_j}+O\left(\sum_{j<n}\frac1{(1+x_j)^2}\right).
\]
Here \(\sum_{j<n}(1+x_j)^{-1}\sim n/\log n\), while the squared-denominator sum is \(O(n/(\log n)^2)\) up to finitely many initial terms. This gives the critical limit.

## Verification
`CHECK.py` performs finite forward iterations for subcritical and critical parameter sets, checks positivity and monotone predator decrease, and displays the asymptotic residual and normalized predator clocks at increasing horizons. The statements for every initial state and all sufficiently large times are established by the proof above, not by the simulations.

## Relationship to prior work
Emam, El-Metwally and Hamada (2026) introduce and investigate this exact recurrence, identifying the positive equilibrium when \(\alpha>\gamma\) and analyzing local bifurcations and numerical trajectories. The present result addresses the complementary noncoexistence domain \(\alpha\le\gamma\) with global positive-orbit selection and quantitative asymptotic clocks. General results on scalar recurrences of the form \(x_{n+1}=x_n+f(x_n)\) motivate the time-change argument but do not by themselves cover the predator coupling or its critical extinction clock. No exclusive historical priority is asserted.

## Limitations
The initial-state restriction \(\alpha y_0<1\) is essential to the invariant positivity region used here; no assertion is made for arbitrary positive predator initial density. The theorem is not a bounded-prey persistence result: prey diverges, a feature of this exact additive recruitment formula. The result does not analyze positive coexistence dynamics for \(\alpha>\gamma\), perturbations, or stochastic effects. The originality comparison is limited to the material inspected and indexed searches; independent validation has not been performed.

## References
1. H. H. Emam, H. El-Metwally, M. Y. Hamada, “Dynamics of a discrete-time predator-prey model with exponential prey growth and saturated response,” *Scientific Reports* **16** (2026), 9662, doi:10.1038/s41598-026-41693-y, published 2026-03-21. Full text: https://www.nature.com/articles/s41598-026-41693-y .
2. MSC2020, classification 37N25, “Dynamical systems in biology,” https://mathscinet.ams.org/mathscinet/msc/msc2020.html .
