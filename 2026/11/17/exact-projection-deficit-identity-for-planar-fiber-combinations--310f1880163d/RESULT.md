# Exact projection-deficit identity for planar fiber combinations

## Finding

Let \(K_1,K_2\subset\mathbb R^2\) be full-dimensional convex bodies, with fiber direction \(L=\mathbb R e_2\) and base \(M=\mathbb R e_1\). Write \(P_i=\operatorname{proj}_M K_i\), and let \(\ell_i(x)=\mathcal H^1(K_i\cap(\{x\}\times\mathbb R))\) for \(x\in P_i\), extended by zero outside \(P_i\). For \(0<\theta<1\), let
\[
F_\theta=\theta\circ_{L|M}K_1\;?_{L|M}\;(1-\theta)\circ_{L|M}K_2
\]
be the classical fiber combination. Then
\[
\operatorname{area}(F_\theta)
=\theta\int_{P_1\cap P_2}\ell_1(x)\,dx
 +(1-\theta)\int_{P_1\cap P_2}\ell_2(x)\,dx,
\]
and therefore
\[
\begin{aligned}
&\theta\operatorname{area}(K_1)+(1-\theta)\operatorname{area}(K_2)
-\operatorname{area}(F_\theta)\\
&\qquad=\theta\int_{P_1\setminus P_2}\ell_1(x)\,dx
 +(1-\theta)\int_{P_2\setminus P_1}\ell_2(x)\,dx.
\end{aligned}
\]
The right side is nonnegative and vanishes exactly when \(P_1=P_2\). Consequently, the unrestricted lower bound printed in Theorem 2.4 of arXiv:2503.05392v3 (and in the corresponding published statement) fails when the projections differ.

A concrete counterexample is
\[
K_1=[-1,1]\times[-1,1],\qquad
K_2=[-2,2]\times[-1,1],\qquad \theta=\tfrac12.
\]
The fiber combination is \([-1,1]\times[-1,1]\), of area \(4\), whereas the claimed lower bound is \(\tfrac12(4)+\tfrac12(8)=6\).

## Assumptions and scope

Both bodies are full-dimensional and convex. The fiber direction is vertical, the base is horizontal, the fiber dimension is one, and the combination parameter is \(p=1\). The formula concerns the classical fiber sum whose base is \(P_1\cap P_2\). It does not assert anything about higher-dimensional fibers, \(p>1\), or a version of the inequality that explicitly assumes equal projections. It identifies a missing necessary condition in the unrestricted statement as printed; it does not infer the authors' intended formulation.

## Proof

For \(x\in P_1\cap P_2\), each fiber \(I_i(x)=K_i\cap(\{x\}\times\mathbb R)\) is a compact interval of length \(\ell_i(x)\). The fiber of \(F_\theta\) over \(x\) is the interval
\[
\theta I_1(x)+(1-\theta)I_2(x),
\]
whose length is \(\theta\ell_1(x)+(1-\theta)\ell_2(x)\). Outside \(P_1\cap P_2\), the fiber sum has no fiber. Fubini's theorem therefore gives the displayed area formula.

For each \(i\), Cavalieri's principle gives
\[
\operatorname{area}(K_i)=\int_{P_i}\ell_i(x)\,dx.
\]
Subtracting the area formula for \(F_\theta\) from the weighted sum of these two identities yields the exact deficit formula.

Since \(K_i\) is full-dimensional, \(\ell_i(x)>0\) for every \(x\) in the interior of the interval \(P_i\). If \(P_1\ne P_2\), at least one of \(P_1\setminus P_2\) and \(P_2\setminus P_1\) contains an interval of positive length, so the corresponding integral is strictly positive. If \(P_1=P_2\), both integrals vanish. This proves the equality characterization.

For the stated rectangles, the common base of the fiber sum is \([-1,1]\). Each scaled vertical fiber has half-length \(1/2\), so their sum has half-length \(1\) and area \(2\cdot2=4\). The weighted input area is \(6\), contradicting the printed lower bound.

## Verification

The analytic argument proves the identity for all full-dimensional planar convex bodies under the stated assumptions. The accompanying exact-arithmetic checker verifies the rectangular counterexample and its deficit. That finite check is supplementary; it is not used as proof of the universal identity.

## Relationship to prior work

Hoehner's paper introduces fiber, chord, and graph combinations and states McMullen's fiber Brunn–Minkowski inequality in its introduction. The arXiv v3 wording of Theorem 2.4 is unrestricted over \(K_1,K_2\in\mathcal K_n^o\), while the definition of the fiber sum and Proposition 2.2(i) make its base projection \(P_1\cap P_2\). The publisher's full-text page displays the corresponding inequality as Theorem 2.8. The exact deficit identity above addresses the planar case \(p=1\), \(\dim L=1\): it shows that the printed lower bound is incompatible with unequal projections and gives the exact equality condition for the weighted-area identity. It does not claim that McMullen's original theorem is false under its original hypotheses; the original paper was not independently inspected here.

## Limitations

The result is specific to one-dimensional fibers in the plane and \(p=1\). The proof does not extend directly to \(p>1\), where fiber lengths do not combine linearly, or to higher-dimensional fibers, where fiber volumes are not additive. An author-intended common-projection hypothesis or an unindexed correction may exist; neither is assumed away. Independent audit has not been performed.

## References

1. S. Hoehner, “New fiber and graph combinations of convex bodies,” arXiv:2503.05392v1 (first public version, 7 March 2025), arXiv:2503.05392v3.
2. S. Hoehner, “New fiber and graph combinations of convex bodies,” *Mathematika*, DOI: 10.1112/mtk.70043.
