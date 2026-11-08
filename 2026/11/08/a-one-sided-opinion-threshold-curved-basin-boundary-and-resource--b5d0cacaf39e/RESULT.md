# A one-sided opinion threshold, curved basin boundary, and resource memory in a Hawk–Dove feedback game

## Finding

For the Table 1 Hawk–Dove instance of Lorits and Gubar's environment–opinion evolutionary game [1], the behavioral–opinion dynamics have two attracting endpoint regimes and exactly one interior saddle. Every interior solution tends to one of these three regimes; there are no nonstationary recurrent limit sets. Opinion share \(y\leq 1/2\) is a **one-sided threshold**: except at the exact saddle, an initially half-or-lower opinion share necessarily tends to zero, but starting just above half need not lead to the high-opinion regime.

The basin boundary is the stable manifold of \((x,y)=(1/2,1/2)\). Its exact local graph is
\[
y=\frac12+\frac{44}{103}\left(x-\frac12\right)^2+O\!\left(\left|x-\frac12\right|^3\right).
\]
Thus a nonzero behavioral imbalance raises the opinion share required for high-opinion convergence to second order. In the low-opinion basin, the environmental state retains a continuum of initial-condition-dependent limits strictly between zero and one; in the other two regimes it tends to one.

## Assumptions and scope

Use the deterministic, continuous-time model [1, equations (7)–(10) and Table 1], with hawk fraction \(x\in(0,1)\), opinion-1 fraction \(y\in(0,1)\), and environmental resource \(n\in(0,1)\). The base matrices have resource values \(v_0=4\), \(v_1=7\), encounter costs \(c_0=12\), \(c_1=10\), and diagonal confidence matrix \(B=\operatorname{diag}(1/2,1/2)\). The environmental rates are \(\theta=2\), \(\psi=-1\). These are the source's exact Table 1 parameters, not free fitted coefficients.

Write \(v(y)=4+3y\), \(c(y)=12-2y\) and the expected payoffs
\[
u_H(x,y)=v(y)-\frac{v(y)+c(y)}2x,\qquad
u_D(x,y)=\frac{v(y)}2(1-x).
\]
Set
\[
f(x,y)=\frac12x(1-x)[v(y)-c(y)x],\qquad
h(x,y)=\frac12\{yx u_H(x,y)-(1-y)(1-x)u_D(x,y)\}.
\]
With \([a]_+=\max\{a,0\}\), the precise dynamics are
\[
\dot x=f(x,y),\qquad
\dot y=(1-y)[h(x,y)]_+-y[-h(x,y)]_+,\qquad
\dot n=n(1-n)(3x-1).
\]
The source's imitation protocol saturates the payoff difference to the interval \( [0,1]\). In this concrete instance no upper saturation activates: \( -1\le h(x,y)\le 49/68<1\) for \(0\le x,y\le1\). Indeed \(h(x,\cdot)\) is convex and so its upper bound is the larger of \(h(x,0)=-(1-x)^2\) and \(h(x,1)=x(14-17x)/4\le49/68\). For the lower bound, the degree-\((2,2)\) tensor-product Bernstein coefficients of \(1+h\), with rows indexed by the degree in \(x\), are
\[
\begin{pmatrix}0&1/8&1\\ 1&3/2&11/4\\ 1&0&1/4\end{pmatrix}.
\]
They are all nonnegative, so \(1+h\ge0\) on the unit square. Consequently the specified saturated protocol is exactly the displayed positive-part equation. The payoff matrix in \(\dot x\) depends on the *opinion* share \(y\), not on the resource \(n\); this triangular feature is part of the printed model [1]. No stochastic finite-population, alternative update, or generalized-parameter result is claimed.

## Proof

**Step 1 (forward domain and trapping).** The open unit square for \((x,y)\) and the open resource interval for \(n\) are forward invariant for positive finite time. The clipped field is locally Lipschitz. Since \(v(y)-c(y)x\) increases strictly with \(y\), scalar comparison with the two endpoint replicator equations gives
\[
\liminf_{t\to\infty}x(t)\geq\frac13,\qquad
\limsup_{t\to\infty}x(t)\leq\frac7{10}.
\]
The closed strip \(1/3\leq x\leq7/10\) is forward invariant and contains every positive \((x,y)\) omega-limit set.

**Step 2 (complete equilibrium census).** Interior equilibria of \(\dot x=0\) lie on \(x=\phi(y)=v(y)/c(y)\). At this nullcline, the two pure-strategy payoffs coincide at \(v(y)[1-\phi(y)]/2>0\), hence
\[
h(\phi(y),y)=\frac{v(y)[1-\phi(y)]}{4}[y+\phi(y)-1],\qquad
y+\phi(y)-1=\frac{(2y-1)(8-y)}{12-2y}.
\]
The sole interior equilibrium is \(Q=(1/2,1/2)\). The only equilibria on the boundary of the trapping strip are \(P_0=(1/3,0)\) and \(P_1=(7/10,1)\). Their two inward linear eigenvalues are respectively \((-4/3,-4/9)\) and \((-21/20,-147/400)\), so both are attracting. The linearization at \(Q\), where the two clipped branches share the same derivative, is
\[
J_Q=\begin{pmatrix}-11/8&1/2\\0&15/32\end{pmatrix}.
\]
Consequently \(Q\) is a hyperbolic saddle and has topological index \(-1\).

**Step 3 (global convergence).** In the open square the opinion component equals \(m(x,y)h(x,y)\), with \(m=y>0\) when \(h<0\), and \(m=1-y>0\) when \(h>0\). Replacing \(m\) continuously by one changes no zeros, so all equilibrium indices equal those of the smooth field \((f,h)\). A periodic orbit wholly in the open square has planar index \(+1\), but its interior contains either no equilibrium (index zero) or just \(Q\) (index \(-1\)). Thus periodic orbits are impossible. A homoclinic saddle loop would likewise require an additional interior equilibrium of positive index; none exists. Within the trapping strip the only boundary equilibria are the two sinks, which cannot belong to a recurrent saddle-connection cycle. The planar limit-set theorem now implies every interior solution tends to \(P_0\), \(P_1\), or \(Q\). Precisely those initial states on the one-dimensional stable set of \(Q\) converge to it; the complementary basins of the two sinks are open, and this stable set is their boundary.

**Step 4 (one-sided opinion barrier).** Direct polynomial identities give
\[
h(x,0)=-(1-x)^2,\qquad
h\left(x,\frac12\right)=-\frac{11}{16}(2x-1)^2,\qquad
\frac{\partial^2h}{\partial y^2}=\frac{2x^2+3}{2}>0.
\]
Convexity in \(y\) makes \(h(x,y)<0\) throughout \(0<x<1,\ 0<y<1/2\). On the half-opinion line, it is negative unless \(x=1/2\). Accordingly \(y\) strictly decreases for an initial \(y<1/2\), and immediately decreases when \(y=1/2\), \(x\ne1/2\). By Step 3 such an orbit cannot converge to either \(Q\) or \(P_1\), and therefore tends to \(P_0\). The stable manifold of \(Q\) lies strictly above the half-opinion line away from \(Q\).

**Step 5 (exact basin curvature).** Put \(u=x-1/2\), \(w=y-1/2\). The stable tangent at \(Q\) is horizontal. On an analytic continuation of the \(h<0\) branch, \(\dot y=yh\), write its stable graph \(w=a u^2+O(u^3)\). The expansions are
\[
\dot u=-\frac{11}{8}u+O(u^2),\qquad
\dot w=\frac{15}{32}w-\frac{11}{8}u^2+O(u^3)
\]
along that graph. Invariance gives \(-11a/4=15a/32-11/8\), or \(a=44/103\). Substitution into \(h\) gives \(h=-242u^2/103+O(u^3)<0\) for small nonzero \(u\), so the analytic branch's stable graph really is the stable graph of the original clipped field. This also establishes the stated cubic-order remainder.

**Step 6 (environmental memory).** For every interior resource state,
\[
\log\frac{n(t)}{1-n(t)}=\log\frac{n(0)}{1-n(0)}+\int_0^t[3x(s)-1]\,ds.
\]
When \((x,y)\to P_0\), exponential local attraction makes the integral converge absolutely, and
\[
\boxed{\quad n_\infty=\left[1+\frac{1-n(0)}{n(0)}\exp\!\left(-\int_0^\infty[3x(s)-1]ds\right)\right]^{-1}\in(0,1).\quad}
\]
For any fixed \((x(0),y(0))\) in this basin, varying \(n(0)\in(0,1)\) realizes every possible limiting resource state in \((0,1)\). In the other regimes \(x\to1/2\) or \(7/10\), so the log-odds diverge positively and \(n(t)\to1\).

## Verification

The accompanying `verify.py` checks the polynomial reductions, equilibria, one-sided identities, Jacobian entries, exact stable-manifold coefficient, and boundary eigenvalues using symbolic rational arithmetic. It also integrates representative low- and high-opinion trajectories; those finite computations illustrate but do not prove the infinite-time classification. Reproduce with `python verify.py` after installing `sympy` and `scipy`. Its successful output ends with `VERIFY_OK`.

## Relationship to prior work

Lorits and Gubar [1], Section 3 and Figure 1, introduce this exact payoff and confidence specification and numerically demonstrate distinct outcomes for opinion initials \(0.45\) and \(0.7\) with initial hawk fraction \(0.5\). This result does **not** claim those observed outcomes or the basic existence of bistability as new. It proves a complete all-initial-state classification for the source's concrete clipped imitation system, a sharp one-sided opinion barrier, a locally exact curved separator, and the entire limiting-resource memory family.

Paarporn et al. [2] use a linear opinion-tracking equation \(\dot o=-\gamma(o-n)\) coupled to population and resource feedback, rather than the clipped payoff-weighted opinion imitation of [1]; their optimal-control and oscillation conclusions do not imply this basin classification. Ito and Yamamichi [3] classify game–environment feedback where payoffs respond directly to the environmental state; the distinct triangular opinion-dependent dynamics and its resource-memory effect are not obtained from that classification. The general existence of a stable manifold and the planar index theorem are classical methods; the exact model-specific barrier and curvature are the contribution.

## Limitations

The classification concerns only the source's specified Hawk–Dove parameters and its deterministic, non-smooth opinion rule. The separating curve is described globally as a stable manifold and locally by an exact expansion, not by a global closed-form equation. The environmental limiting value in the low-opinion basin has an exact trajectory-integral representation, not a formula in elementary functions of every initial state. No finite-population stochastic theorem, parameter robustness theorem, independent external validation, or assertion of publication priority beyond the inspected literature is made.

## References

[1] E. M. Lorits and E. A. Gubar, *An evolutionary game with environmental feedback and players' opinions*, arXiv:2307.04902v1, first posted 2023-07-10, equations (7)–(10), Table 1, Figure 1. https://arxiv.org/abs/2307.04902

[2] K. Paarporn, C. Eksin, J. S. Weitz, and Y. Wardi, *Optimal control policies for evolutionary dynamics with environmental feedback*, arXiv:1803.06737v1 (2018), Section IV. https://arxiv.org/abs/1803.06737

[3] H. Ito and M. Yamamichi, *A complete classification of evolutionary games with environmental feedback*, PNAS Nexus 3 (2024), pgae455, doi:10.1093/pnasnexus/pgae455. https://pmc.ncbi.nlm.nih.gov/articles/PMC11639210/
