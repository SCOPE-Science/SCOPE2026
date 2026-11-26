# A three-agent threshold for nonmonotone opinion homogenization under heterogeneous platform susceptibility

## Finding

Consider a predictive-loop opinion model with one round of peer interaction between successive perfect platform predictions. Under homogeneous peer susceptibility on an undirected complete graph with three agents, raising a single agent's platform susceptibility can **increase** the equilibrium variance of opinions. This is a sharp and robust boundary of the usual variance-reduction phenomenon for homogeneous platform susceptibility.

More precisely, fix the triangle with peer susceptibility \(\alpha=1/3\), innate opinions \(x^*=(1,0,0)^\top\), and heterogeneous platform susceptibilities \(\beta=(b,z,0)\), where \(0<b<1\) and \(0\le z\le1\). Let \(V_b(z)\) be the population variance (mean squared deviation from the contemporaneous population mean) at the unique stable predictive-loop equilibrium. Then

\[
V_b(z)=\frac{2(1-b)^2(7z^2-18z+12)}{3(12-8b-8z+5bz)^2}.
\]

For **every** \(b\in(0,1)\), this variance has a unique global minimizer on \([0,1]\),

\[
\boxed{z_b=\frac{12(1-b)}{12-11b}\in(0,1)},
\qquad
\boxed{V_b(z_b)=\frac{(1-b)^2}{2(7b^2-18b+12)}}.
\]

It decreases strictly as \(z\) rises from \(0\) to \(z_b\), then increases strictly as \(z\) rises from \(z_b\) to \(1\). In particular,

\[
\boxed{V_b(1)-V_b(z_b)=\frac{b^2(1-b)^2}{6(3b-4)^2(7b^2-18b+12)}>0}.
\]

The phenomenon requires at least three agents: for the corresponding perfect-prediction, one-peer-step model on any connected, undirected **two-agent** graph with a common peer susceptibility \(0<\alpha<1\), increasing either agent's platform susceptibility cannot increase equilibrium opinion variance, for arbitrary innate opinions. With one agent, variance is identically zero. Thus three is the smallest population size supporting this nonmonotonicity in the indicated model class.

## Assumptions and scope

For \(n\) agents with innate opinions \(x^*\in[0,1]^n\), a common peer susceptibility \(\alpha\in(0,1)\), and a simple undirected connected graph whose row-stochastic neighbor matrix is \(W\), one within-period Friedkin–Johnsen step is \(P=(1-\alpha)I+\alpha W\). With perfect predictions equal to the previous expressed opinions, the cross-period expressed opinions follow

\[
y^{(t+1)}=P[(I-B)x^*+B y^{(t)}],\qquad B=\operatorname{diag}(\beta_1,\ldots,\beta_n),\quad 0\le\beta_i\le1.
\]

The equilibrium is a solution of \((I-PB)y=P(I-B)x^*\). When \(\rho(PB)<1\), it is unique and attracts every initial platform-prediction vector. The variance convention is \(V(y)=n^{-1}\sum_i(y_i-\bar y)^2\), with \(\bar y=n^{-1}\sum_i y_i\). No assumption that the equilibrium mean equals the innate mean is made when \(B\) is heterogeneous.

The three-agent claim specializes to \(W=(\mathbf 1\mathbf 1^\top-I)/2\), \(\alpha=1/3\), \(B=\operatorname{diag}(b,z,0)\), and \(x^*=(1,0,0)^\top\). These are bona fide parameters of the model, including the allowed endpoint susceptibility \(z=1\). Because the third agent retains an innate anchor, \(\|PB\|_\infty<1\) on the entire parameter rectangle \(0\le b,z\le1\), so equilibrium existence and convergence do not require extrapolation at the endpoint.

## Proof

**Three agents: exact equilibrium.** For the triangle with \(\alpha=1/3\),

\[
P=\frac16\begin{pmatrix}4&1&1\\1&4&1\\1&1&4\end{pmatrix}.
\]

Write \(D=12-8b-8z+5bz\). Solving the displayed three-by-three equilibrium system yields

\[
\boxed{y(b,z)=\frac{1-b}{D}(8-5z,\,2,\,2-z)^\top}.
\]

The factor \(D\) is strictly positive on \([0,1]^2\): it decreases in either coordinate there, and its minimum is \(D(1,1)=1\). Direct substitution verifies the equilibrium equation, and \(\|PB\|_\infty<1\) establishes uniqueness. The equilibrium components lie in \([0,1]\) because the dynamical map is a convex-combination map on that cube.

**Exact variance and optimization.** Centering the three components around their own mean gives

\[
V_b(z)=\frac{2(1-b)^2(7z^2-18z+12)}{3D^2}.
\]

Its exact derivative is

\[
\frac{dV_b}{dz}=-\frac{4(1-b)^2\big[(11b-12)z+12(1-b)\big]}{3D^3}.
\]

For every \(0<b<1\), the bracket vanishes only at \(z_b=12(1-b)/(12-11b)\), with \(0<z_b<1\). It is strictly positive to the left of \(z_b\), strictly negative to the right. Since \(D>0\), the derivative is negative before and positive after \(z_b\). Hence \(z_b\) is the unique global minimum over the full closed interval. Exact substitution gives the minimum and the strict endpoint gap above; similarly,

\[
V_b(0)-V_b(z_b)=\frac{3(1-b)^4}{2(2b-3)^2(7b^2-18b+12)}>0.
\]

All denominators are positive or nonzero on \(0<b<1\). The formula also shows an open interval of positive \(dV_b/dz\) for each such \(b\), so the variance increase persists under sufficiently small perturbations of the model's numerical data, by continuity and invertibility of \(I-PB\).

**Minimality for one and two agents.** For two agents on the unique connected simple undirected graph, set

\[
P_2=\begin{pmatrix}1-\alpha&\alpha\\\alpha&1-\alpha\end{pmatrix},\qquad B_2=\operatorname{diag}(b,c).
\]

For \(0\le b,c<1\), exact inversion gives the difference of equilibrium expressed opinions:

\[
y_1-y_2=\frac{(1-2\alpha)(1-b)(1-c)}{(1-b)(1-c)+\alpha\big(b(1-c)+c(1-b)\big)}(x_1^*-x_2^*).
\]

After division by \((1-b)(1-c)\), the absolute difference coefficient becomes

\[
\frac{|1-2\alpha|}{1+\alpha\big(b/(1-b)+c/(1-c)\big)}.
\]

It is nonincreasing in each susceptibility. Since the two-agent population variance equals \((y_1-y_2)^2/4\), variance cannot increase. If exactly one of \(b,c\) equals \(1\), the fixed point still exists uniquely and is a consensus by the undivided formula. If both equal \(1\), every equilibrium of the primitive peer matrix is a consensus, so the variance remains zero even though the equilibrium level need not be uniquely anchored. With one agent the variance is always zero. This proves the stated smallest-agent conclusion.

## Verification

The standalone program `verify.py` uses exact SymPy algebra to reproduce the equilibrium system, variance, derivative, optimizer, endpoint differences, and general two-agent difference formula. It also exercises finitely many rational parameter points as regression checks; those finite tests supplement, but do not replace, the preceding symbolic identities and sign proof. Run `python verify.py` after installing the dependencies listed in `requirements.txt`.

For illustration, \(b=3/4\) gives \(z_b=4/5\), and

\[
y(3/4,4/5)=(5/13,5/26,3/26)^\top,\qquad V_{3/4}(4/5)=1/78.
\]

At \(z=1\), the corresponding fixed point is \((3/7,2/7,1/7)^\top\) and variance is \(2/147\), strictly larger by \(1/1274\). Both parameter choices have the same connected regular peer network and peer susceptibility.

## Relationship to prior work

Wu, Abebe, and Mendler-Dünner (2026), *Opinion Dynamics in Learning Systems* (arXiv:2603.12137; HTML manuscript title *Reaching a Consensus in Predictive Loops*), introduces this peer-platform recursion. Its Proposition 3 and Appendix A.5 analyze shrinking variance under **homogeneous** platform susceptibility on regular graphs; its Appendix C treats homogeneous susceptibility for finite numbers of peer steps. The formulas and monotonicity here concern **one varying component** of a heterogeneous platform-susceptibility vector, and the fixed-point mean may vary. The homogeneous monotonicity result therefore does not imply this statement.

Shirzadi and Zehmakan (2024), *Do Stubborn Users Always Cause More Polarization and Disagreement? A Mathematical Study* (arXiv:2410.22577), already studies nonmonotonic effects of heterogeneous stubbornness, especially the combined polarization-plus-disagreement index. Its Section 4 includes a three-agent **path** example and a perturbation theorem for that **combined** objective. That work establishes the relevance of inhomogeneity, but the inspected results do not provide the present complete two-parameter **pure variance** phase diagram on a regular triangle or its two-agent minimality comparison. The predictive-loop equilibrium is algebraically related to a Friedkin–Johnsen equilibrium, so conceptual novelty must not be overstated.

Abebe, Kleinberg, Parkes, and Tsourakakis (2018), *Opinion Dynamics with Varying Susceptibility to Persuasion* (arXiv:1801.07863), studies interventions in susceptibility with a focus on optimizing the **sum** of expressed opinions, a different observable. The 2021 paper *The impact of noise and topology on opinion dynamics in social networks* examines nonmonotone opinion diversity under **noise and uniform susceptibility**, which does not imply the noiseless heterogeneous susceptibility formula above.

## Limitations

The three-agent formula concerns one round of peer updates, perfect lag-one prediction, a regular complete graph, one fixed extreme innate opinion, and a specified two-parameter family of individual susceptibilities. It is not a theorem that increasing an individual susceptibility usually increases polarization. The minimality proof concerns common peer susceptibility on connected undirected graphs and the same one-step perfect-prediction mechanism, not every conceivable social-learning model. No statistical identification from field observations, arbitrary-network classification, or societal causal prediction is asserted. The calculation is an exact specialization of a known linear update rule; independent verification of literature priority remains outstanding.

## References

1. J. Wu, R. Abebe, and C. Mendler-Dünner, *Opinion Dynamics in Learning Systems*, arXiv:2603.12137, publicly posted March 12, 2026. https://arxiv.org/abs/2603.12137
2. M. Shirzadi and A. N. Zehmakan, *Do Stubborn Users Always Cause More Polarization and Disagreement? A Mathematical Study*, arXiv:2410.22577, October 29, 2024. https://arxiv.org/abs/2410.22577
3. R. Abebe, J. Kleinberg, D. C. Parkes, and C. E. Tsourakakis, *Opinion Dynamics with Varying Susceptibility to Persuasion*, arXiv:1801.07863, 2018. https://arxiv.org/abs/1801.07863
4. *The impact of noise and topology on opinion dynamics in social networks*, 2021. https://pmc.ncbi.nlm.nih.gov/articles/PMC8025306/
