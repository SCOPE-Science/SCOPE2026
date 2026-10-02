# Exact complete-Bernstein scale thresholds for the largest Gegenbauer zeros in degrees four and five

## Result

Let \(z_{n,1}(\lambda)\) be the largest positive zero of the Gegenbauer polynomial \(C_n^\lambda\), with the reduced interpretation at \(\lambda=0\), and for \(d\geq 1/2\) define
\[
F_{n,d}(s)=\sqrt{s+d-\tfrac12}\;z_{n,1}(s-\tfrac12),\qquad s>0.
\]
Then the first two previously unresolved largest-zero scale families have exact complete-Bernstein thresholds:
\[
\boxed{F_{4,d}\in\mathcal{CBF}\iff \tfrac12\le d\le3,}
\qquad
\boxed{F_{5,d}\in\mathcal{CBF}\iff \tfrac12\le d\le4.}
\]
Here \(\mathcal{CBF}\) denotes the complete Bernstein functions on \((0,\infty)\).

This improves the sufficient ranges \(d\le \lceil n/2\rceil\) supplied for the largest zero in Proposition A.4 of Castillo, *Complete Bernstein functions and scaled ultraspherical zeros* (arXiv:2609.19186). For \(n=4\) and \(n=5\), those ranges are respectively \(d\le2\) and \(d\le3\), whereas the exact endpoints are \(3\) and \(4\). The same source determines the exact low-degree cases \(n=2,3\), but does not claim optimality of its general largest-zero endpoint for \(n\ge4\).

At the maximal scales the functions have explicit compactly supported complete-Bernstein representing measures:
\[
F_{4,3}(s)=\sqrt{\frac52}+\int_1^{3/2}\frac{s}{s+t}\,\rho_4(t)\,dt,
\]
where
\[
\rho_4(t)=\frac{1}{2\pi t}
\sqrt{
\sqrt{\frac{3(\frac52-t)}{\frac32-t}}-3
},\qquad 1<t<\frac32,
\]
and
\[
F_{5,4}(s)=\sqrt{\frac72}+\int_1^{5/2}\frac{s}{s+t}\,\rho_5(t)\,dt,
\]
where
\[
\rho_5(t)=\frac{1}{2\pi t}
\sqrt{
\sqrt{\frac{15(\frac72-t)}{\frac52-t}}-5
},\qquad 1<t<\frac52.
\]
The densities are zero outside their displayed intervals.

## Algebraic reduction

The degree-four and degree-five Gegenbauer polynomials factor as
\[
C_4^\lambda(x)=\frac{\lambda(\lambda+1)}6
\left[4(\lambda+2)(\lambda+3)x^4-12(\lambda+2)x^2+3\right]
\]
and
\[
C_5^\lambda(x)=\frac{\lambda(\lambda+1)(\lambda+2)}{15}x
\left[4(\lambda+3)(\lambda+4)x^4-20(\lambda+3)x^2+15\right].
\]
Solving the resulting quadratics in \(y=x^2\), the largest positive zeros satisfy
\[
z_{4,1}(\lambda)^2
=
\frac{3+\sqrt{\frac{3(2\lambda+3)}{\lambda+2}}}{2(\lambda+3)},
\]
\[
z_{5,1}(\lambda)^2
=
\frac{5+\sqrt{\frac{5(2\lambda+3)}{\lambda+3}}}{2(\lambda+4)}.
\]
After the translation \(s=\lambda+1/2\), write
\[
F_{4,d}(s)^2=A_4(s)B_{4,d}(s),
\]
with
\[
A_4(s)=\frac{3+\sqrt{6\frac{s+1}{s+3/2}}}{2},
\qquad
B_{4,d}(s)=\frac{s+d-1/2}{s+5/2},
\]
and
\[
F_{5,d}(s)^2=A_5(s)B_{5,d}(s),
\]
with
\[
A_5(s)=\frac{5+\sqrt{10\frac{s+1}{s+5/2}}}{2},
\qquad
B_{5,d}(s)=\frac{s+d-1/2}{s+7/2}.
\]

## Sufficiency

A nonnegative function on \((0,\infty)\) is a complete Bernstein function exactly when its holomorphic continuation to the slit plane is a Pick function. The Möbius map
\[
s\longmapsto\frac{s+a}{s+b},\qquad 0\le a\le b,
\]
is a complete Bernstein function: its imaginary part in the upper half-plane is
\[
\frac{(b-a)\operatorname{Im}s}{|s+b|^2}\ge0.
\]
Complete Bernstein functions are closed under positive affine combinations, powers \(0\le\alpha\le1\), and weighted geometric means whose exponents sum to at most one.

For degree four, \((s+1)/(s+3/2)\) is complete Bernstein, hence so is \(A_4\). If \(1/2\le d\le3\), then
\[
0\le d-\frac12\le\frac52,
\]
so \(B_{4,d}\) is also complete Bernstein. Therefore
\[
F_{4,d}=A_4^{1/2}B_{4,d}^{1/2}\in\mathcal{CBF}.
\]

For degree five, the same argument applies to \((s+1)/(s+5/2)\) and \(A_5\). If \(1/2\le d\le4\), then
\[
0\le d-\frac12\le\frac72,
\]
so \(B_{5,d}\in\mathcal{CBF}\), and hence \(F_{5,d}\in\mathcal{CBF}\).

## Sharpness of the upper endpoints

Write \(c=d-1/2\). For degree four, if \(d>3\), then \(c>5/2\). Choose a real point
\[
x\in(-c,-5/2).
\]
Along the upper boundary, \(A_4(x+i0)\) is positive real because both \(x+1\) and \(x+3/2\) are negative. In contrast,
\[
B_{4,d}(x)<0,
\qquad
\operatorname{Im}B_{4,d}(x+iy)
=
\frac{(5/2-c)y}{|x+5/2+iy|^2}<0
\]
for \(y>0\). Moreover \(A_4\) approaches its positive boundary value from the upper half-plane. Hence, for all sufficiently small \(y>0\),
\[
A_4(x+iy)B_{4,d}(x+iy)
\]
lies below the negative real axis. The holomorphic square-root branch that is positive on \((0,\infty)\) therefore has negative imaginary part there. Thus \(F_{4,d}\) does not preserve the upper half-plane and cannot be complete Bernstein.

For degree five, if \(d>4\), then \(c>7/2\). Taking
\[
x\in(-c,-7/2)
\]
gives the identical obstruction: \(A_5(x+i0)>0\), while
\[
\operatorname{Im}B_{5,d}(x+iy)
=
\frac{(7/2-c)y}{|x+7/2+iy|^2}<0.
\]
Consequently \(F_{5,d}\) fails the Pick property. Finally, \(d<1/2\) cannot occur because the prefactor \(s+d-1/2\) is negative for sufficiently small positive \(s\), so the scale does not define a nonnegative real function throughout \((0,\infty)\).

This proves both exact equivalences.

## Endpoint representing measures

At the sharp upper endpoints the rational factors cancel:
\[
F_{4,3}(s)=
\left(\frac{3+\sqrt{6\frac{s+1}{s+3/2}}}{2}\right)^{1/2},
\]
\[
F_{5,4}(s)=
\left(\frac{5+\sqrt{10\frac{s+1}{s+5/2}}}{2}\right)^{1/2}.
\]
For a complete Bernstein representation
\[
f(s)=a+\int_0^\infty\frac{s}{s+t}\rho(t)\,dt,
\]
the Stieltjes inversion formula gives
\[
\rho(t)=\frac{\operatorname{Im}f(-t+i0)}{\pi t}.
\]

For \(F_{4,3}\), the only nonzero boundary imaginary part occurs for \(1<t<3/2\). There
\[
\sqrt{6\frac{-t+1+i0}{-t+3/2+i0}}
=i\sqrt{\frac{6(t-1)}{3/2-t}},
\]
so the elementary formula for the imaginary part of a square root gives precisely \(\rho_4\) above. Likewise, for \(F_{5,4}\) the cut is \(1<t<5/2\), yielding \(\rho_5\). The densities are positive, vanish at the left endpoint, and have only an integrable fourth-root singularity at the right endpoint.

Thus the exact maximal scale has a compact representing measure, while crossing that scale reverses the Pick orientation of the remaining Möbius factor on an open real interval.

## Verification

The accompanying script `artifacts/verify_low_degree_formulas.py` independently checks the factorizations and largest-root formulas symbolically and numerically checks the two endpoint integral representations at \(s=0.1,1,10\) to high precision.

## Relation to prior literature and originality

Castillo (arXiv:2609.19186) establishes broad complete-Bernstein results for scaled ultraspherical zeros. Its Appendix A proves an exact threshold \(d\le k-1/2\) for nonlargest zeros, but for the largest zero gives the sufficient range
\[
\frac12\le d\le\left\lceil\frac n2\right\rceil
\]
without claiming optimality of that upper endpoint; the appendix separately identifies the exact cases \(n=2\) and \(n=3\). The theorem above resolves the next two degrees and shows that the general sufficient endpoint is not sharp already at \(n=4,5\).

Targeted searches by the source identifier, by the explicit degree-four and degree-five Gegenbauer zero formulas, and by combinations of “largest ultraspherical/Gegenbauer zero”, “complete Bernstein”, “Pick”, “operator monotone”, and the candidate endpoint scales did not locate an equivalent theorem or correction. To the best of our knowledge, the exact thresholds above and the compact endpoint representing measures are new. Residual originality risk remains because the source preprint is recent and the low-degree algebra is elementary enough that equivalent observations could occur under different terminology.

## Limitations

The result determines only the largest-zero thresholds in degrees four and five. It does not prove a general formula for the optimal largest-zero threshold for \(n\ge6\). The sequence of exact endpoints in degrees \(2,3,4,5\) is consistent with \(d_{\max}=n-1\), but no such general statement is claimed here. No optimal statement for other rescalings or for non-Gegenbauer orthogonal polynomial families is asserted.

## References

1. K. Castillo, *Complete Bernstein functions and scaled ultraspherical zeros*, arXiv:2609.19186 (2026), https://arxiv.org/abs/2609.19186.
2. R. L. Schilling, R. Song, and Z. Vondraček, *Bernstein Functions: Theory and Applications*, 2nd ed., De Gruyter (2012), https://doi.org/10.1515/9783110269338.
3. W. Gautschi, *On the Ismail–Letessier–Askey monotonicity conjecture for zeros of ultraspherical polynomials* (2018), as cited and discussed in arXiv:2609.19186.
