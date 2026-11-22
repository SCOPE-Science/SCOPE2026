# Sharp finite-time six-cycle transition in the no-chartist three-zone market map

## Finding

On the no-chartist, unit fundamental-response boundary of the three-zone market model, a strict threshold between extinction and persistent boom–bust dynamics occurs at \(d=h\). For every initial condition in the full real plane, if \(0<d\le h\), the orbit reaches the origin by iteration five. If \(d>h\), every orbit reaches by iteration three either the origin or the unique primitive six-cycle, with first-coordinate word
\[
(-d,0,d,d,0,-d).
\]
Its six points are \((x_i,x_{i-1})\), and the word is interpreted cyclically. The complete invariant-probability simplex is therefore a point when \(d\le h\), and the line segment between the atomic fixed-point measure and the uniform six-cycle measure when \(d>h\). Both periodic components attract their finite-time basins, but no claim is made that either basin is the whole plane.

## Assumptions and scope

Let \(d,h>0\), with switching convention
\[
\sigma_h(u)=\begin{cases}
+1,&u>h,\\
0,&-h\le u\le h,\\
-1,&u<-h.
\end{cases}
\]
Consider the complete real-plane map
\[
F_{d,h}(x,y)=\bigl(d\sigma_h(x-y),\ x\bigr).
\]
It is the \(b=0,c=1\) specialization of the three-partition stock-market recurrence of Gardini et al.: no trend-following orders and exact one-step fundamental-price correction. The previously studied model includes strictly positive chartist coefficient; this theorem concerns only this natural boundary case. Orbits are forward-defined at thresholds because the neutral branch is closed. An invariant probability means an \(F\)-invariant countably additive Borel probability on \(\mathbb R^2\).

## Proof

Write \(x_n\) for the first coordinate after \(n\) iterations and set \(x_{-1}=y_0\). Then
\[
x_{n+1}=d\sigma_h(x_n-x_{n-1}).
\]
For every initial \((x_0,x_{-1})\), both \(x_1\) and \(x_2\) belong to \(S=\{-d,0,d\}\). Thus by the second iterate, the full planar state belongs to the nine-point grid \(S^2\), without any assumptions on the starting amplitude. Scale this grid by \(d\), write its state as \((p,q)=(x_{n-1}/d,x_n/d)\), and put \(r=h/d>0\). The exact grid transition is
\[
\Phi_r(p,q)=\bigl(q,\operatorname{sgn}(q-p)\mathbf1_{\{|q-p|>r\}}\bigr),\qquad p,q\in\{-1,0,1\}.
\]
This nine-point formula is a complete global reduction rather than an approximation.

For \(r\ge1\), differences of magnitude one are neutral. If \(r\ge2\), every successor's newly generated coordinate is zero, so every grid state reaches \((0,0)\) in at most two further steps. If \(1\le r<2\), only the two pairs \((-1,1)\) and \((1,-1)\) can yield a nonzero successor. Their images are, respectively, \((1,1)\) and \((-1,-1)\); both then pass to \((\pm1,0)\) and finally \((0,0)\). Every other grid state reaches zero in at most two steps. Hence all grid states reach the origin after at most three transitions, proving the global five-iterate bound for \(d\le h\), including the equality \(d=h\).

For \(0<r<1\), every nonzero difference of two symbols produces its sign. Directly applying \(\Phi_r\) gives the six-state directed cycle
\[
(-1,-1)\mapsto(-1,0)\mapsto(0,1)\mapsto(1,1)\mapsto(1,0)\mapsto(0,-1)\mapsto(-1,-1).
\]
The only remaining grid states are \((0,0)\), \((-1,1)\), and \((1,-1)\). The first is fixed; the second enters \((1,1)\) in one transition; the third enters \((-1,-1)\) in one transition. Thus every planar state reaches a periodic component after at most three iterations. The displayed six states are all distinct, so the orbit has least period six. This also proves there are no other periodic points and no other recurrent orbits in the plane.

To classify invariant Borel probabilities, observe that every orbit reaches the finite invariant set \(K\) by iteration five (or three in the second regime), so \(F^5(\mathbb R^2)\subseteq K\) and every invariant probability \(\mu\) satisfies \(\mu(K)=\mu(F^{-5}(K))=1\). On a finite disjoint union of cycles, invariance forces uniform weights on each cycle. This proves the stated measure simplex and excludes nonperiodic invariant probabilities. The threshold is sharp because the six-cycle persists for every \(d>h\), while at \(d=h\) its unit-sized jumps become neutral.

## Verification

Execute `python3 check_six_cycle.py` (Python standard library only). It exhaustively checks all nine grid states in each threshold regime, confirms the exact absorbing-time bounds, checks the six-cycle's distinctness and closure, and tests off-grid initial states and both equality conventions. The infinite-state assertion is proved analytically by the two-step collapse onto \(S^2\); finite computations are used solely to verify the nine-state transition table, not to extrapolate from a finite sample of real initial conditions.

## Relationship to prior work

Gardini, Radi, Schmitt, Sushko and Westerhoff introduced the three-zone piecewise-affine stock-market map in 2023. Their main analysis assumes \(d>h>0\) and positive chartist feedback and develops period-adding families, while explicitly highlighting \(0<d<h\) for further study. The present classification treats the distinct, economically interpretable boundary \(b=0,c=1\), where the linear memory collapses in two steps and supports a globally exact periodicity and invariant-measure classification. It is not a restatement of the paper's local cycle bifurcations.

The closest accessible subsequent result, *A sharp weak-sentiment five-cycle threshold in a three-zone market map*, studies \(b=1/4,c=5/4\) and certain \(b>0\) five-cycle bands, with a different primitive period and nonzero memory; its conclusions do not imply the no-chartist global six-cycle-versus-extinction dichotomy. Earlier two-zone market maps lack the same closed neutral band. General finite-state automaton theory supplies the reduction method, but not this threshold for the model's precise switching rule.

## Limitations

This is an exact theorem for the no-chartist unit-response boundary only. It neither rules out longer cycles when \(b>0\) nor proves that the real economy realizes these idealized discrete adjustments. Basin volumes and perturbation robustness near the discontinuity are not classified. The conclusion is independent of any numerical time horizon. Priority against literature not available through the inspected primary and indexed results remains subject to further external checking; no independent mathematical audit is claimed.

## References

1. L. Gardini, D. Radi, N. Schmitt, I. Sushko and F. Westerhoff, “A 2D piecewise-linear discontinuous map arising in stock market modeling: Two overlapping period-adding bifurcation structures,” *Chaos, Solitons & Fractals* 176 (2023), 114143, DOI `10.1016/j.chaos.2023.114143`. Public online date 2023-10-12. Sections 2–4 and conclusion. Open-access copy: https://publicatt.unicatt.it/retrieve/1397dc5d-93b5-40e9-8081-4aab287cfcd1/1-s2.0-S0960077923010445-main.pdf
2. “A sharp weak-sentiment five-cycle threshold in a three-zone market map,” publicly indexed result, https://github.com/published-finding corpus/2026/blob/main/2026/11/1/SCOPE-a-sharp-weak-sentiment-five-cycle-threshold-in-a-three-zone-mark--2c50dbdce3ba/RESULT.md. Its \(b>0\) five-period claim is distinct from the no-chartist global theorem.
