# Sharp defect-norm thresholds for band projections on \(L_p\)

## Finding
Let \(1\le p<\infty\), let \((\Omega,\Sigma,\mu)\) be any measure space, and let \(E\in\Sigma\) be such that both \(L_p(E)\) and \(L_p(\Omega\setminus E)\) contain a nonzero vector. Write \(P_Ef=\mathbf 1_Ef\). For \(0\le t<1\) define the Pythagorean defect of the strict contraction \(T=tP_E\) by
\[
A_{p,t}(f)=\left(\|f\|_p^2-t^2\|P_E f\|_p^2\right)^{1/2}.
\]
Then \(A_{p,t}\) is a norm on real or complex \(L_p(\mu)\) exactly when
\[
\boxed{\quad p=2\quad\text{or}\quad
(1<p<2\ \text{and}\ t^2\le \frac{p-1}{p}2^{2/p})
\quad\text{or}\quad t=0.\quad}
\]
For \(1<p<2\), the sharp admissible interval is \(0\le t\le\sqrt{(p-1)2^{2/p}/p}<1\). For \(p=1\) and every \(2<p<\infty\), no positive scaling \(t\) works. This is a complete, dimension-independent two-band phase diagram, including its borderline equality.

## Assumptions and scope
The measure space is arbitrary; no nonatomicity, countability or finiteness is assumed. The condition on the two bands means that there are norm-one vectors \(u,v\in L_p(\mu)\) supported respectively on \(E\) and its complement. The scalar field is \(\mathbb R\) or \(\mathbb C\). The endpoint \(t=1\) is excluded because \(A_{p,1}\) then vanishes on every vector supported on \(E\). The exponent \(p=\infty\) is not treated. The primary invariant is normability of the displayed defect, not normability of arbitrary nonlinear differences of norms.

## Proof
Set \(c=t^2\in[0,1)\). The disjoint support identity gives
\[
\|f\|_p^p=\|P_E f\|_p^p+\|(I-P_E)f\|_p^p.
\]
Consequently, defining on \([0,\infty)^2\)
\[
F_{p,c}(a,b)=\Big((a^p+b^p)^{2/p}-ca^2\Big)^{1/2},
\]
we have \(A_{p,t}(f)=F_{p,c}(\|P_E f\|_p,\|(I-P_E)f\|_p)\). The expression is positive away from the origin since \((a^p+b^p)^{2/p}\ge a^2\) and \(c<1\); it is positively homogeneous.

For \(1<p<\infty\), restrict to the line \(b=1\), and put
\[
G(r)=(1+r^p)^{2/p}-cr^2,\qquad g(r)=G(r)^{1/2}\quad(r>0).
\]
Direct differentiation, with all factors shown, yields
\[
4G(r)^{3/2}g''(r)
=2G(r)G''(r)-(G'(r))^2
=4(1+r^p)^{2/p-2}\big(1+(p-1)r^p\big)\big(H_p(r^p)-c\big),
\]
where
\[
H_p(z)=\frac{(p-1)z^{(p-2)/p}(1+z)^{2/p}}{1+(p-1)z},\qquad z>0.
\]
In particular \(g''(r)\ge0\) everywhere if and only if \(c\le\inf_{z>0}H_p(z)\). Moreover,
\[
\frac{d}{dz}\log H_p(z)
=-\frac{(p-2)(z-1)}{p z(1+z)(1+(p-1)z)}.
\]
When \(1<p<2\), this derivative changes from negative to positive at \(z=1\); hence the global minimum is
\[
\inf_{z>0}H_p(z)=H_p(1)=\frac{p-1}{p}2^{2/p}.
\]
When \(p=2\), \(H_p\equiv1\), and when \(p>2\), \(H_p(z)\to0\) as \(z\downarrow0\).

For sufficiency with \(1<p<2\) and \(c\le(p-1)2^{2/p}/p\), the preceding curvature calculation makes \(g\) convex. The perspective identity \(F_{p,c}(a,b)=b\,g(a/b)\) for \(b>0\) implies joint convexity of \(F_{p,c}\) on the positive quadrant: apply the scalar Jensen inequality to the weights proportional to the two interpolated second coordinates. Continuity extends this convexity to the boundary. Also \(F_{p,c}\) is nondecreasing separately in both arguments. Indeed for \(a,b>0\), differentiating its square in \(a\) gives
\[
\frac{\partial}{\partial a}F_{p,c}(a,b)
=\frac{a}{F_{p,c}(a,b)}
\left[\left(1+(b/a)^p\right)^{(2-p)/p}-c\right]>0,
\]
because \(p<2\) and \(c<1\); the partial derivative in \(b\) is positive as well, and the boundary follows by continuity. Since \(F_{p,c}\) is positively homogeneous, convexity implies subadditivity on the positive quadrant. Thus for all \(f,h\), coordinatewise Minkowski and monotonicity yield
\[
\begin{aligned}
A_{p,t}(f+h)&\le F_{p,c}\big(\|P_E f\|_p+\|P_E h\|_p,\|(I-P_E)f\|_p+\|(I-P_E)h\|_p\big)\\
&\le A_{p,t}(f)+A_{p,t}(h).
\end{aligned}
\]
Positive definiteness and absolute homogeneity were already established. For \(p=2\), \(F_{2,c}(a,b)=\sqrt{(1-c)a^2+b^2}\) is a weighted Euclidean norm for every \(0\le c<1\); for any \(p\), \(c=0\) recovers the original \(L_p\) norm.

For necessity, if the displayed \(H_p\) test fails at some \(r>0\), then \(g''(r)<0\) and therefore, for sufficiently small \(\varepsilon>0\),
\[
2g(r)>g(r-\varepsilon)+g(r+\varepsilon).
\]
Choose unit vectors \(u\) and \(v\) on the respective disjoint bands, and set \(f_\pm=(r\pm\varepsilon)u+v\). The strict inequality says
\[
A_{p,t}\big((f_++f_-)/2\big)>
\big(A_{p,t}(f_+)+A_{p,t}(f_-)\big)/2,
\]
which contradicts convexity (hence the triangle inequality) of any norm. For \(1<p<2\), failure occurs when \(c>H_p(1)\). For \(p>2\), every \(c>0\) fails for sufficiently small \(r\) because \(\inf H_p=0\). Finally, for \(p=1\) direct differentiation of \(g(r)=\sqrt{(1+r)^2-cr^2}\) gives
\[
g''(r)=-\frac{c}{\big((1+r)^2-cr^2\big)^{3/2}}<0
\quad(c>0,r>0),
\]
so the same midpoint obstruction applies. These cases exhaust the parameter ranges.

## Verification
The curvature factorization was independently recomputed by symbolic differentiation, and the logarithmic derivative was simplified and checked exactly. Numerical evaluations of \(H_p\) across both sides of \(z=1\) for \(p=5/4,3/2,7/4\) agreed with the analytic minimum; checks at \(p=2,5/2,3,10\) agreed with the degeneracy on the super-Hilbert side. These finite evaluations are consistency checks only; the global argument is the derivative-sign proof above. Necessity constructs an explicit family of two-band midpoint violations whenever the parameter lies outside the admissible range.

## Relationship to prior work
Jana, Pal and Roy (arXiv:2407.15112, initially public 21 July 2024) introduce this defect for general Banach-space strict contractions. Their Theorem 7.13 identifies defect normability with their orthogonally decomposed isometric-dilation notion; Example 7.18 gives a positive example on an \(\ell_2\)-sum, while Example 7.20 constructs different operators failing defect normability on non-Hilbert \(L_p\). Those statements do not compute the exact threshold for scaled band projections. Fackler and Glück (arXiv:1709.08547, Theorem 7.1) obtain dilations for all positive \(L_p\)-contractions under a distinct dilation definition using contractive embedding and compression; that does not imply normability of the Pythagorean defect. The present phase diagram quantifies the boundary specifically for these natural projections.

## Limitations
The formula concerns only scalar multiples of nontrivial band projections, not arbitrary contractions, general conditional expectations, or non-idempotent multipliers. The corresponding result for \(p=\infty\) is not claimed. Prior-art searches cannot exclude every unindexed equivalent formulation, and there is no claim of independent audit or external certification.

## References
1. S. Jana, S. Pal and S. Roy, *A dilation theoretic approach to Banach spaces*, arXiv:2407.15112 (first submission 21 July 2024), especially Section 7, Proposition 7.6, Theorem 7.13, Examples 7.18 and 7.20. https://arxiv.org/abs/2407.15112
2. S. Fackler and J. Glück, *A toolkit for constructing dilations on Banach spaces*, arXiv:1709.08547 (2017/2018), Definition 2.7 and Theorem 7.1. https://arxiv.org/abs/1709.08547
