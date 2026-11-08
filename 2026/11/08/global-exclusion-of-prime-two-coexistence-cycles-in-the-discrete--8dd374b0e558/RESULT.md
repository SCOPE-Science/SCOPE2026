# Global exclusion of prime-two coexistence cycles in the discrete linear-response plankton model

## Finding

For every \(r>0\) and \(\gamma>0\), let
\[
F(x,y)=\bigl(x(2-x-y),\;y(1-r+\gamma x)\bigr).
\]
**Theorem.** If \(z\) and \(F(z)\) both belong to the nonnegative quadrant and \(F^2(z)=z\), then \(F(z)=z\). Thus the model possesses no nonconstant two-cycle which remains biologically nonnegative. In fact its complete nonnegative periodic-point census at periods dividing two consists of \((0,0)\), \((1,0)\), and, when \(\gamma>r\), \((r/\gamma,1-r/\gamma)\).

The result holds across the whole positive \((r,\gamma)\) parameter quadrant, including regimes beyond the invariant trapping triangle and beyond the coexistence equilibrium's Neimark–Sacker instability boundary.

## Assumptions and scope

The state is \((x,y)\in[0,\infty)^2\), representing nonnegative phytoplankton and zooplankton populations. The parameters satisfy \(r>0\), \(\gamma>0\), with **no** upper bound on either parameter. The map need not preserve the entire quadrant. A nonnegative period-two orbit means two states \(z,F(z)\in[0,\infty)^2\) with \(F^2(z)=z\) and \(F(z)\ne z\). The theorem does not assert that all algebraic roots of \(F^2(z)=z\) with \(z\ge0\) have nonnegative intermediate iterates when the parameters permit negative population updates.

## Proof

Write the two states as \((x_0,y_0)\) and \((x_1,y_1)\), and suppose first that all four coordinates are strictly positive.

If \(x_0=x_1\), then the positive first-coordinate multiplier gives \(2-x_0-y_0=2-x_1-y_1=1\), so \(y_0=y_1\): the orbit is fixed. For a hypothetical nonfixed two-cycle, swap the states if necessary so that \(0<x_0<x_1\), and put \(s=x_1/x_0>1\). The two prey updates give the exact identities
\[
x_0+y_0=2-s,\qquad
x_1+y_1=2-s^{-1},\qquad x_1=sx_0.
\]
The strict positivity of \(x_0,y_0\) forces \(x_0<2-s<1\). Subtracting the two sum identities then yields
\[
y_1-y_0=(s-1)(1+s^{-1}-x_0)>0. \tag{1}
\]
But the two predator updates give
\[
t_0=\frac{y_1}{y_0}=1-r+\gamma x_0,\qquad
t_1=\frac{y_0}{y_1}=1-r+\gamma x_1.
\]
Both multipliers are positive, their product is one, and \(t_1>t_0\) because \(\gamma>0\) and \(x_1>x_0\). Hence \(t_0<1<t_1\), which implies \(y_1<y_0\), contradicting (1). Thus no strictly positive nonfixed two-cycle exists.

It remains to treat boundary states. The factors in each update make both coordinate axes forward invariant as sets, subject to the stated orbit remaining nonnegative.

On \(x=0\), the dynamics is \(y\mapsto(1-r)y\). A nonzero nonnegative two-cycle would require \((1-r)^2=1\) and \(1-r\ge0\), which for \(r>0\) is impossible. Thus the origin is the only admissible two-step fixed point on this axis.

On \(y=0\), the dynamics is \(x\mapsto f(x)=x(2-x)\). For a strictly positive nonnegative two-cycle, \(0<x_0<2\) and \(0<x_1=f(x_0)\le1\). If \(x_0>1\), the next iterate \(x_2=f(x_1)\le1<x_0\), impossible. If \(0<x_0\le1\), the map \(f\) is increasing on \([0,1]\), and an increasing interval map has no nonfixed two-cycle; equivalently \(f(x)>x\) for \(0<x<1\) and \(f(1)=1\). This leaves only \(x=1\) and \(x=0\).

Finally, the fixed-point equations are \(x(1-x-y)=0\) and \(y(\gamma x-r)=0\). They give precisely the three stated possibilities, with the positive one present only for \(\gamma>r\). This concludes the proof.

## Verification

The analytic contradiction proves the theorem for every real \(r>0,\gamma>0\); finite checks are supplementary. Run `python verify_period_two.py` (requires Python 3 and SymPy). The program checks the exact symbolic identity used in (1) and tests \(7{,}225\) rational state/parameter combinations, explicitly requiring the intermediate iterate to be nonnegative before checking \(F^2(z)=z\).

## Relationship to prior work

Shoyimardonov's paper *Stability and Bifurcation Analysis of a Phytoplankton-Zooplankton Model with Linear Functional Responses*, arXiv:2505.09968v1, first publicly available 15 May 2025, defines precisely this two-species map in equation (1.4). Section 3.0.1 proves the absence of nonfixed two-cycles **on the predator-free axis**; its Theorem 3 proves convergence to an equilibrium on a restricted invariant triangle for specified parameter regions. Section 4 studies a Neimark–Sacker bifurcation at \(\gamma=1+r\) for \(0<r\le1\). None of these results implies a global exclusion of *interior* prime-two cycles for all \(r,\gamma>0\).

Liu and Xiao, *Bifurcations in a discrete time Lotka-Volterra predator-prey system* (2006), study another discretization and report a flip bifurcation. Its abstract alone does not settle the present map; the full article was not available for material comparison. The claim here is restricted to the exact polynomial map above, not to arbitrary Euler predator–prey schemes.

## Limitations

No existence or nonexistence theorem is claimed for periodic orbits of least period at least three, invariant circles, quasiperiodic dynamics, or chaos. No uniform forward-invariance claim is made for the entire nonnegative quadrant at arbitrary parameter values. Priority beyond the inspected accessible sources is provisional. The mathematical proof is independent of the supplementary finite tests.

## References

1. S. K. Shoyimardonov, *Stability and Bifurcation Analysis of a Phytoplankton-Zooplankton Model with Linear Functional Responses*, arXiv:2505.09968v1 (15 May 2025). https://arxiv.org/html/2505.09968v1
2. X. Liu and D. Xiao, *Bifurcations in a discrete time Lotka-Volterra predator-prey system*, Discrete and Continuous Dynamical Systems B **6** (2006), 559–572, doi:10.3934/dcdsb.2006.6.559.
