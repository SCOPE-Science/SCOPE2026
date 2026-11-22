# Four positive coexistence equilibria are sharp for the predator-dependent two-prey replicator

## Finding

In the positive-payoff predator-dependent replicator model with two prey types and one predator, every **nondegenerate** parameter choice has at most four strictly positive coexistence equilibria. Here nondegenerate means that the explicit polynomial \(Q\), defined below, is not identically zero. This bound is sharp: the strictly positive rational payoff matrices
\[
M_R=\begin{pmatrix}183/50&49/100\\329/100&191/100\end{pmatrix},\qquad
M_P=\begin{pmatrix}57/100&9/50\\1/4&111/50\end{pmatrix},\qquad K=687/1000
\]
admit **exactly four** distinct strictly positive coexistence equilibria, for every predator conversion parameter \(\beta>0\). All four are isolated, and the coexistence count persists for an open neighborhood of the displayed parameters.

The exact equilibrium equation has degree at most four, because an apparent fifth-degree term cancels as a consequence of the population-average structure. The result is a sharp equilibrium-count theorem; it does not assert stability of any of the four states.

## Assumptions and scope

Let \(M_R=\begin{pmatrix}a&b\\c&d\end{pmatrix}\) and \(M_P=\begin{pmatrix}a'&b'\\c'&d'\end{pmatrix}\), with every entry strictly positive, and take \(K,\beta>0\). If \(A,B,Y\) denote densities of two prey types and their shared predator, put \(P=A+B\) and \(x=A/P\). The dynamics in the strictly positive region are
\[
\begin{aligned}
\dot x&=x(1-x)[g(x)-h(x)Y],\\
\dot P&=P[r(x)-P/K-\delta(x)Y],\\
\dot Y&=\beta Y[-1+\delta(x)P].
\end{aligned}
\]
Define the affine type-specific rates and their differences by
\[
\begin{aligned}
u_A(x)&=ax+b(1-x),&u_B(x)&=cx+d(1-x),&g(x)&=u_A(x)-u_B(x),\\
v_A(x)&=a'x+b'(1-x),&v_B(x)&=c'x+d'(1-x),&h(x)&=v_A(x)-v_B(x),
\end{aligned}
\]
and let \(r(x)=xu_A(x)+(1-x)u_B(x)\), \(\delta(x)=xv_A(x)+(1-x)v_B(x)\). These latter rates are quadratic and \(\delta(x)>0\) throughout \([0,1]\). A *positive coexistence equilibrium* means \(0<x<1\), \(P>0\), and \(Y>0\), equivalently \(A,B,Y>0\).

Define
\[
Q(x)=K\delta(x)\big(r(x)h(x)-\delta(x)g(x)\big)-h(x).
\]
The upper bound applies whenever \(Q\) is not the zero polynomial; no finite bound is asserted here for degenerate families in which \(Q\equiv0\). All example payoffs are strictly positive, and no stability assumption is imposed.

## Proof

**1. Exact quartic reduction.** At a strictly positive equilibrium, \(\dot Y=0\) forces \(P=1/\delta(x)\), while \(\dot x=0\) gives \(g(x)=h(x)Y\). The prey-abundance equation then gives \(r(x)-1/(K\delta(x))-\delta(x)Y=0\). Multiplying this equation by \(K\delta(x)h(x)\), and substituting \(hY=g\), produces the necessary equation \(Q(x)=0\). This derivation does *not* divide by \(h\) and is therefore also valid when \(h=0\).

By construction,
\[
r=u_B+xg,\qquad \delta=v_B+xh.
\]
Consequently the highest-degree terms cancel **identically**:
\[
\boxed{rh-\delta g=u_Bh-v_Bg.}
\]
The right side is of degree at most two, because all four constituent type-specific rates or differences are affine. Since \(\delta\) is quadratic and \(h\) affine, \(Q\) has degree at most four. For a fixed root \(x\), \(P=1/\delta(x)\) is uniquely determined and so is \(Y\) from \(r-1/(K\delta)-\delta Y=0\), including when \(h(x)=0\). Therefore every distinct positive equilibrium gives a distinct root of \(Q\). A nonzero quartic has at most four real roots, which proves the universal upper bound in the stated nondegenerate class.

**2. Exact sharp witness.** For the matrices in the finding, direct rational arithmetic yields
\[
\begin{aligned}
g(x)&=\frac{179x-142}{100},& h(x)&=\frac{236x-204}{100},\\
r(x)&=\frac{191}{100}-\frac{x}{25}+\frac{179x^2}{100},&
\delta(x)&=\frac{111}{50}-\frac{401x}{100}+\frac{59x^2}{25}.
\end{aligned}
\]
The degree-four eliminant is exactly
\[
\boxed{10^9 Q(x)=905295840-8056257752x+23130348810x^2-26920918713x^3+10997575692x^4.}
\]
Its signs at the following rational endpoints are certified by exact fraction computation:

| Interval for \(x\) | Sign at left endpoint | Sign at right endpoint |
|---|---|---|
| \((1/5,1/4)\) | \(+\) | \(-\) |
| \((1/2,3/5)\) | \(-\) | \(+\) |
| \((7/10,3/4)\) | \(+\) | \(-\) |
| \((9/10,1)\) | \(-\) | \(+\) |

The zero of \(g\) is \(142/179\), and the zero of \(h\) is \(51/59\), with
\[
\frac34<\frac{142}{179}<\frac{51}{59}<\frac9{10}.
\]
Hence \(g\) and \(h\) are both negative throughout the first three intervals and both positive throughout the last. Any root in the listed intervals therefore has \(Y=g/h>0\), and \(P=1/\delta>0\). By the defining equilibrium equation, \(Q=0\) implies the remaining \(\dot P=0\). Thus the intermediate value theorem gives four distinct positive coexistence equilibria. The nonzero quartic bounds their number by four; in particular all four roots are simple. Strict endpoint signs and strict positivity inequalities persist under sufficiently small perturbations of the payoff entries and \(K\), proving robustness. Neither the existence nor location of equilibria depends on \(\beta>0\).

## Verification

Run `python3 verify_equilibria.py` using the Python standard library. The program reconstructs the payoff averages, independently checks both sides of the degree-reducing identity, confirms all five coefficients of \(Q\) exactly, evaluates the eight endpoint signs using rational arithmetic, checks sign alignment of \(g,h\) on the four intervals and verifies the relative positions of the two affine zeros. The full output ends with `PASS: quartic cancellation, exact polynomial, four positive equilibria, sharp bound.`. The continuous root-existence, nondegenerate upper-bound and robustness arguments follow analytically from the inequalities; the script is an exact finite certificate for the supplied rational witness, not a substitute for the polynomial-degree proof.

## Relationship to prior work

Braga and Wardil introduced the predator-dependent replicator and supplied coexistence and persistence criteria. Cruz and Neves derive the same three-dimensional representation, the positive-equilibrium equations and the admissibility intervals for \(g/h\); Section 4 describes solving a fifth-degree polynomial and gives examples with up to three simultaneous positive coexistence equilibria. The present degree cancellation sharpens that general equation to a quartic and supplies a four-equilibrium positive rational construction. Its contribution is the sharp nondegenerate global equilibrium *count*, not the original model, the general positive-equilibrium formula or local bifurcation theory.

Separate related analyses study local stability exchange, Hopf bifurcations and exactly solvable balanced-payoff subclasses of this model. None of those statements determines the maximum number of positive equilibria over arbitrary strictly positive payoff matrices. This comparison is based on accessible source texts and does not establish universal historical priority.

## Limitations

The upper bound excludes the algebraic degeneracy \(Q\equiv0\); that case may admit a continuum of equilibria and requires separate classification. The four-state example proves existence and robustness only: it does not classify equilibria as attracting, repelling or saddle-type, does not identify basins or limit cycles, and does not address stochastic finite-population models. A search of accessible literature cannot rule out an unindexed earlier equivalent theorem. No independent mathematical audit has been performed.

## References

1. H. M. Cruz and A. G. M. Neves, *Predator-dependent replicator dynamics or a predator-prey model with two prey types and frequency dependence*, arXiv:2607.13281 (first public version 2026-07-14), https://arxiv.org/abs/2607.13281.
2. I. Braga and L. Wardil, *The predator-dependent replicator dynamics*, Journal of Physics A: Mathematical and Theoretical **55** (2022), 025601, https://doi.org/10.1088/1751-8121/ac40e4.
