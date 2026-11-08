# Exact one-vertex stubbornness optimization for network polarization–disagreement

## Finding

In the undirected weighted Friedkin–Johnsen (FJ) opinion-formation model, fixing every resistance except one allows an exact global optimization of the sum of polarization and edge disagreement. The scalar objective, although not necessarily convex in the original resistance parameter, is a strictly convex quadratic in a fractional-linear reparameterization whenever that resistance affects the equilibrium. Consequently, it is either monotone, constant, or has exactly one strict interior minimum. The minimizer requires only two linear solves, a few quadratic forms, and scalar clipping. In particular, a three-vertex path has a strict interior global minimizer at resistance \(t=1/3\), whereas optimization of the sum of expressed opinions has a boundary-optimum principle in an earlier, different objective.

Write \(G=(V,E,w)\), \(|V|=n\ge2\), for a finite connected undirected graph with strictly positive edge weights and combinatorial weighted Laplacian \(L\). Fix a vertex \(\ell\), innate opinions \(s\in[-1,1]^n\), and positive stubbornness coefficients \(\kappa_j>0\) for \(j\ne\ell\). The stubbornness \(\kappa_\ell=t\) varies over \([0,\infty)\). Put

\[
K_0=\operatorname{diag}(\kappa_1,\ldots,0,\ldots,\kappa_n),\quad M=L+K_0,\quad e=e_\ell,
\]
\[
x_0=M^{-1}K_0s,\quad u=M^{-1}e,\quad g=u_\ell,\quad d=s_\ell-(x_0)_\ell,
\]
\[
H=L+I-\frac1n\mathbf1\mathbf1^{\mathsf T},\quad B=u^{\mathsf T}Hx_0,\quad C=u^{\mathsf T}Hu,\quad \eta(t)=\frac{t}{1+gt}.
\]

Then \(g>0\) and \(C>0\), and for every finite \(t\ge0\) the unique FJ equilibrium and its polarization–disagreement satisfy

\[
\boxed{x(t)=x_0+d\eta(t)u,\qquad
\mathcal{PD}(t)=x_0^{\mathsf T}Hx_0+2dB\eta(t)+d^2C\eta(t)^2.}
\]

If \(d=0\), the entire equilibrium and objective are independent of \(t\). If \(d\ne0\), let \(\eta_*= -B/(dC)\). The unconstrained optimum in the compactified coordinate \(0\le\eta\le1/g\) is the projection of \(\eta_*\) onto this interval. A unique finite **strictly interior** optimum occurs exactly when

\[
0<\eta_*<\frac1g,
\]

in which case

\[
\boxed{t_* =\frac{\eta_*}{1-g\eta_*}=-\frac{B}{dC+gB},\qquad
\mathcal{PD}(t_*)=x_0^{\mathsf T}Hx_0-\frac{B^2}{C}.}
\]

Otherwise \(\mathcal{PD}\) is strictly increasing or strictly decreasing for finite \(t\ge0\), with the minimum at \(t=0\) in the former case, or the infimum attained only in the limit \(t\to\infty\) in the latter. The same clipping rule on \(\eta([a,b])\) solves every bounded interval \(0\le a\le b<\infty\).

## Assumptions and scope

The model uses positive symmetric edge weights, a connected graph, and exactly one freely selected coefficient \(t\). All other stubbornness coefficients remain strictly positive; their values and the innate opinions are arbitrary within the stated domain. The FJ update at node \(i\) is the weighted mean of its innate opinion with weight \(\kappa_i\) and its neighbors' current expressed opinions with edge weights \(w_{ij}\). Its equilibrium solves

\[
(L+K(t))x(t)=K(t)s,\qquad K(t)=K_0+t ee^{\mathsf T}.
\]

Polarization is the sum of squared deviations from the expressed-opinion mean (not divided by \(n\)); disagreement is \(\sum_{\{i,j\}\in E}w_{ij}(x_i-x_j)^2\). Their sum is \(\mathcal{PD}(t)=x(t)^{\mathsf T}Hx(t)\). These conventions agree with the cited 2024 study. The case \(t=0\) is interpreted as a fully susceptible selected node. The limit \(t\to\infty\) is a mathematical limiting regime, not a finite feasible coefficient.

## Proof

**Invertibility, convergence and positivity.** For any nonzero real vector \(z\),

\[
z^{\mathsf T}Mz=\sum_{\{i,j\}\in E}w_{ij}(z_i-z_j)^2+
\sum_{j\ne\ell}\kappa_jz_j^2>0.
\]

Indeed, if the first term vanishes, connectedness makes \(z\) constant, and a nonzero constant makes the second term positive. Thus \(M\) is positive definite, as is \(M+t ee^{\mathsf T}\). Even at \(t=0\), the averaging iteration converges to the unique fixed point: its nonnegative update matrix is irreducible and substochastic, with at least one strictly deficient row because an unselected node has positive stubbornness; therefore its spectral radius is less than one. The scalar \(g=e^{\mathsf T}M^{-1}e\) is strictly positive.

**One-coordinate equilibrium identity.** Since \(Mx_0=K_0s\) and \(Mu=e\), look for a solution \(x(t)=x_0+a(t)u\). Substitution into the fixed-point equation gives

\[
a(t)e+t e\bigl((x_0)_\ell+a(t)g\bigr)=t s_\ell e.
\]

Thus \(a(t)(1+tg)=td\), proving \(a(t)=d\eta(t)\) for every \(t\ge0\).

**Strict quadratic curvature.** The matrix \(H\) is positive semidefinite because \(L\) is positive semidefinite and \(I-\mathbf1\mathbf1^{\mathsf T}/n\) is the orthogonal projector onto mean-zero vectors. Its kernel consists exactly of the constant vectors. The vector \(u\) is not constant: if \(u=c\mathbf1\), then \(Mu=cK_0\mathbf1\), whose \(\ell\)-th entry is zero, contradicting \(Mu=e\). Hence \(C=u^{\mathsf T}Hu>0\). Expanding \((x_0+d\eta u)^{\mathsf T}H(x_0+d\eta u)\) establishes the stated quadratic.

**Exact optimizer and boundaries.** We have \(\eta'(t)=1/(1+gt)^2>0\), and \(\eta\) maps \([0,\infty)\) bijectively to \([0,1/g)\). When \(d\ne0\), the quadratic as a function of \(\eta\) has positive curvature \(2d^2C\) and vertex \(\eta_*=-B/(dC)\). Its minimizer on the closure \([0,1/g]\) is the ordinary scalar projection, yielding the claimed finite/interior and limiting cases. The derivative in the original parameter is

\[
\frac{d\mathcal{PD}}{dt}=\frac{2d(B+dC\eta(t))}{(1+gt)^2}.
\]

Its sign changes at most once, and when it does, changes from negative to positive. For finite bounds, project onto \([a/(1+ga),\,b/(1+gb)]\) and invert \(t=\eta/(1-g\eta)\). When \(d=0\), the rank-one coefficient vanishes and the objective is constant.

**An exact interior optimum.** On the unweighted three-vertex path \(0-1-2\), set \(s=(1/2,-1,1/2)^{\mathsf T}\), \(\kappa_1=\kappa_2=1\), and \(\kappa_0=t\). Direct inversion gives

\[
x(t)=\left(\frac{5t-3}{2(5t+3)},\,-\frac{t+3}{2(5t+3)},\,\frac{t}{5t+3}\right)^{\mathsf T},
\]
\[
\mathcal{PD}(t)=\frac{3(21t^2+6t+5)}{4(5t+3)^2},\qquad
\mathcal{PD}'(t)=\frac{24(3t-1)}{(5t+3)^3}.
\]

Thus the unique global minimizer is \(t=1/3\), with \(\mathcal{PD}=9/28\). For comparison, \(\mathcal{PD}(0)=5/12\), \(\mathcal{PD}(1)=3/8\), and \(\lim_{t\to\infty}\mathcal{PD}(t)=63/100\); in particular neither endpoint is optimal. All innate opinions lie in \([-1,1]\), and their mean is zero.

## Verification

Run `python3 verify.py` using Python's standard library. The verifier first solves the original FJ linear system exactly over rational numbers and then independently compares the equilibrium with the rank-one formula and the direct polarization–disagreement objective with the quadratic formula. It also checks the projected minimizer inequalities for sampled finite coefficients, and the path example and its derivative. With its fixed random seed the output is:

```
VERIFY_OK configurations=540 exact_assertions=12831 three_vertex_minimizer=1/3
```

The 540 configurations consist of connected positive-weight graphs of orders two through seven with positive rational fixed stubbornness values and bounded rational innate opinions. These finite checks are not a substitute for the proof above; in particular they do not establish the universal quantifiers or novelty.

## Relationship to prior work

Shirzadi and Zehmakan (2024), especially their Section 4 and Theorem 4.3, study how polarization–disagreement varies under changes in stubbornness and derive a rank-one perturbation expression for a special unit-baseline neutral-node regime. Their three-node example also shows that making a node more stubborn can decrease the objective. The present claim concerns an *arbitrary positive fixed baseline at all other nodes*, exact full-range optimization at the selected node, the scalar phase classification, and a strict **finite interior** optimizer for nonneutral innate opinion; it does not claim the FJ equilibrium formula, polarization definition, or Sherman–Morrison identity as new.

Abebe et al. (2020), Section 5.1, show that the **sum of expressed opinions**, a linear rather than quadratic target, is monotone in a single susceptibility coordinate and hence favors endpoint choices. The path example demonstrates why that endpoint principle cannot be transferred to polarization–disagreement. Hunter and Zaman (2018), Sections 4–5, investigate changing the **placement** of immutable stubborn agents and optimizing total opinion or threshold counts, not the continuous single-coefficient polarization–disagreement objective.

## Limitations

The classification optimizes one coefficient while holding all others fixed; it does not solve joint multi-vertex optimization or optimize network topology. It requires a connected positive-weight undirected graph and positive stubbornness at all unselected vertices. For an unbounded parameter domain, the right-endpoint optimum may be only an infimum as the coefficient tends to infinity. Exact algebra and rational checks do not establish that no equivalent theorem appears in unindexed literature; independent external audit has not been performed.

## References

- Mohammad Shirzadi and Ahad N. Zehmakan, *Do Stubborn Users Always Cause More Polarization and Disagreement? A Mathematical Study*, arXiv:2410.22577v1 (first posted 2024-10-29), https://arxiv.org/abs/2410.22577.
- Rediet Abebe, T.-H. Hubert Chan, Jon Kleinberg, Zhibin Liang, David Parkes, Mauro Sozio, and Charalampos E. Tsourakakis, *Opinion Dynamics with Varying Susceptibility to Persuasion via Non-Convex Local Search*, arXiv:2011.02583v1 (2020), https://arxiv.org/abs/2011.02583.
- D. Scott Hunter and Tauhid Zaman, *Optimizing Opinions with Stubborn Agents*, arXiv:1806.11253 (2018), https://arxiv.org/abs/1806.11253.
