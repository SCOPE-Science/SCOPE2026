# Endpoint Gamma scaling for extremal marks in Poisson–Laguerre tessellations

## Result

Consider the bounded-mark Poisson–Laguerre model of Schulte and Švarc Petráková (2026). Let the dimension satisfy \(d\ge 3\), let the stationary marked Poisson process have spatial intensity \(\gamma>0\), and let its mark law \(\mathbb Q\) be supported on \([0,A]\) with \(A>0\) as its right endpoint. Let \(M\sim\mathbb Q\), and suppose that for some \(C>0\) and \(\kappa>0\),
\[
\mathbb P(A-M\le y)\sim C y^\kappa,\qquad y\downarrow0.
\]
Write \(v_d\) for the volume of the Euclidean unit ball, \(c_d=2^dv_d\), and
\[
L_\rho=\log \rho^d,
\qquad
 a_{d,\rho}=d(v_d\gamma)^{2/d}L_\rho^{1-2/d}.
\]
Let \(s_{d,\rho}\) be any correct shift in the sense of Theorem 1.1 of Schulte–Švarc Petráková, and let \(r((x,m),\eta)\) denote the Laguerre inradius attached to the marked nucleus \((x,m)\). Then the refined point process
\[
\Xi_\rho^*=
\sum_{(x,m)\in\eta\cap(W_\rho\times[0,A])}
\delta_{\left(x/\rho,\,a_{d,\rho}(A-m),\,c_d\gamma r((x,m),\eta)^d-s_{d,\rho}\right)}
\]
converges in distribution, in the vague topology on
\(W\times[0,\infty)\times\mathbb R\), to a Poisson point process with intensity
\[
\lambda_d|_W\otimes \Gamma_{\kappa,2A}\otimes\mathbb K,
\]
where \(\Gamma_{\kappa,2A}\) is the Gamma probability law with shape \(\kappa\) and rate \(2A\), and
\[
\mathbb K([u,v])=e^{-u}-e^{-v},\qquad u\le v.
\]
Equivalently, the source paper's first-order degeneration of extremal marks to \(A\) has the sharp second-order scale
\[
A-M_{\mathrm{extreme}}\asymp
\big(\log \rho^d\big)^{-(1-2/d)}.
\]
At that scale the limiting deficit is Gamma rather than degenerate.

For the cell of maximal inradius, if \((X_{\max,\rho},M_{\max,\rho})\) denotes its nucleus and mark and \(R_{\max,\rho}\) its inradius, then
\[
\left(
\frac{X_{\max,\rho}}{\rho},
 a_{d,\rho}(A-M_{\max,\rho}),
 c_d\gamma R_{\max,\rho}^d-s_{d,\rho}
\right)
\xrightarrow{d}
(X,Y,G),
\]
where the three components are independent,
\[
X\sim\operatorname{Unif}(W),\qquad
Y\sim\Gamma(\kappa,\text{rate }2A),\qquad
G\sim\text{standard Gumbel}.
\]
Thus the endpoint exponent \(\kappa\) of the original mark law survives in the extremal geometry even though the unscaled limiting mark in dimensions \(d\ge3\) is always the point mass at \(A\).

## Why the scale is universal

The intensity calculation in the source paper expands the large-inradius exponent in powers of the mark. Its first mark-sensitive coefficient can be written
\[
\alpha_{1,d}
=
\frac{v_d\gamma\,c_{1,d}}
{(c_d\gamma)^{(d-2)/d}},
\]
where the Taylor coefficient of
\((1+\sqrt{1+z})^d\) is
\[
c_{1,d}=d2^{d-2}.
\]
Since \(c_d=2^dv_d\), this simplifies exactly to
\[
\alpha_{1,d}=d(v_d\gamma)^{2/d}.
\]
A correct shift satisfies \(s_{d,\rho}=L_\rho+o(L_\rho)\), so the leading mark-selection factor is asymptotically
\[
\exp\{-a_{d,\rho}(\mathbb EM^2-m^2)\}.
\]
Relative to the endpoint \(A\), a mark
\[
m=A-\frac{y}{a_{d,\rho}}
\]
therefore receives the limiting relative weight
\[
\exp\{-a_{d,\rho}(A^2-m^2)\}\longrightarrow e^{-2Ay}.
\]
All higher mark-sensitive terms are negligible on this scale. Indeed, the \(i\)-th term has size \(L_\rho^{1-2i/d}\), while changing \(m\) by \(O(a_{d,\rho}^{-1})\) changes its coefficient by \(O(a_{d,\rho}^{-1})\). Relative to the first term this is
\[
O\big(L_\rho^{-2(i-1)/d}\big)=o(1),\qquad i\ge2.
\]
Marks separated from \(A\) by a fixed positive amount are exponentially suppressed by the first term.

Now put \(Y=A-M\). The endpoint assumption is
\[
\mathbb P(Y\le y)\sim Cy^\kappa.
\]
Karamata's Laplace–Stieltjes asymptotics give
\[
\mathbb E e^{-qY}\sim C\Gamma(\kappa+1)q^{-\kappa},
\qquad q\to\infty.
\]
Since
\[
a_{d,\rho}(M^2-A^2)
=-2Aa_{d,\rho}Y+a_{d,\rho}Y^2,
\]
the quadratic remainder is negligible under the endpoint tilt. Consequently, under the extremal weighting,
\[
a_{d,\rho}(A-M)\Longrightarrow \Gamma(\kappa,\text{rate }2A).
\]
More explicitly, its limiting Laplace transform is
\[
\left(\frac{2A}{2A+t}\right)^\kappa.
\]

For any bounded inradius-height strip, the source paper's Poisson approximation applies after the deterministic output relabeling
\(m\mapsto a_{d,\rho}(A-m)\): the exceedance event and the dependency neighborhoods are unchanged. Combining that approximation with the preceding intensity limit gives the product Poisson intensity on every compact mark-height rectangle. Vague point-process convergence follows by exhaustion. The maximum-cell statement follows from the unique top point of the limiting Poisson process and the same truncation/argmax argument used for the first-order maximum in the source paper.

## Explicit three-dimensional centering

For \(d=3\), the source paper gives the exact correct shift
\[
s_{3,\rho}
=L_\rho-a_\rho\mathbb EM^2+
\log\mathbb E e^{a_\rho M^2}+\log\gamma,
\]
with
\[
a_\rho=3(v_3\gamma)^{2/3}L_\rho^{1/3}.
\]
The endpoint assumption implies
\[
\mathbb E e^{aM^2}
\sim
e^{aA^2}\frac{C\Gamma(\kappa+1)}{(2A)^\kappa a^\kappa}.
\]
Hence an explicit asymptotically correct centering is
\[
\boxed{
\begin{aligned}
s_{3,\rho}
={}&L_\rho+a_\rho(A^2-\mathbb EM^2)-\kappa\log a_\rho\\
&+\log\!\left(\frac{\gamma C\Gamma(\kappa+1)}{(2A)^\kappa}\right)+o(1).
\end{aligned}}
\]
In particular, every polynomial endpoint with exponent \(\kappa\) contributes the universal lower-order term
\[
-\frac{\kappa}{3}\log\log\rho^3.
\]

For the source paper's continuous example
\[
\mathbb Q(ds)=\frac{2s}{A^2}\,ds,\qquad 0\le s\le A,
\]
one has \(\kappa=1\) and \(C=2/A\). The formula above becomes
\[
\boxed{
\begin{aligned}
s_{3,\rho}
={}&L_\rho+a_\rho(A^2-\mathbb EM^2)
-\frac13\log L_\rho\\
&-\log\!\big(3(v_3\gamma)^{2/3}A^2\big)+\log\gamma+o(1).
\end{aligned}}
\]
Direct comparison with equation (1.7) shows that the formula printed as equation (3.24) in arXiv:2609.20750v1 appears to omit the final \(+\log\gamma\). The same issue occurs in the discrete-top-atom example (3.23): if the largest mark \(A_K\) has mass \(p_K\), equation (1.7) gives
\[
s_{3,\rho}
=L_\rho+a_\rho(A_K^2-\mathbb EM^2)+\log p_K+\log\gamma+o(1),
\]
whereas the displayed example omits \(+\log\gamma\). This is also forced by the constant-mark specialization \(p_K=1\), for which the source paper itself states the Poisson–Voronoi centering \(\log(\gamma\rho^3)\).

## Verification

The accompanying script checks three independent pieces of the calculation:

1. the exact leading coefficient \(c_{1,d}=d2^{d-2}\) for dimensions \(3\) through \(8\);
2. Karamata/Gamma scaling for the explicit endpoint law \(\mathbb P(A-M\le y)=(y/A)^\kappa\), including convergence of the tilted scaled-gap Laplace transform to \((2A/(2A+t))^\kappa\);
3. the three-dimensional continuous-example centering. For \(\gamma=2.3\), the corrected expansion agrees with the exact equation (1.7) up to the exponentially small remainder, while the version without \(+\log\gamma\) retains the constant discrepancy \(-\log\gamma=-0.832909122935104\ldots\).

The verification was executed with Python 3.13.5 and mpmath 1.3.0. It is numerical support for the asymptotic algebra; the theorem itself is proved by the intensity expansion and Poisson-approximation argument above.

## Originality boundary and limitations

Schulte and Švarc Petráková prove the first-order point-process limit for large Poisson–Laguerre inradii and show that, for bounded marks in dimensions \(d\ge3\), the unscaled extremal mark converges to the endpoint \(A\). That theorem, their Poisson approximation, and the exact \(d=3\) shift are prior work and are used here.

The Laplace–Stieltjes regular-variation step is a classical consequence of Karamata's theorem and is not claimed as new. Earlier work on random Laguerre tessellations develops the model and typical-cell characteristics, while Poisson–Voronoi extreme-radius theory covers the constant-mark specialization. Searches located no prior statement resolving the degenerate bounded-mark limit at the scale \((\log\rho^d)^{-(1-2/d)}\), no Gamma endpoint law for the extremal mark, and no all-\(d\) product point-process refinement of this form. The originality claim is therefore restricted to those refinements, the resulting general \(d=3\) endpoint-tail centering, and the identified constant correction in the two v1 examples, all to the best of our knowledge.

The main limitations are:

- the mark law is bounded with a regularly varying right endpoint \(Cy^\kappa\); atoms at \(A\) and non-regular endpoint laws require different scalings or mixtures;
- only \(d\ge3\) is covered by the Gamma endpoint refinement stated here; the planar bounded-mark limit is genuinely different in the source paper;
- the result inherits the Poisson–Laguerre model, inradius definition, and geometric approximation hypotheses of arXiv:2609.20750v1;
- no quantitative convergence rate for the refined Gamma-mark point process is claimed;
- the full text of Lautensack–Zuyev (2008) was not inspected here, only its accessible abstract and the source paper's description; this is a residual originality risk for older Laguerre-tessellation formulas, although that work is described as concerning typical characteristics rather than large-inradius extremes;
- the earlier Poisson–Voronoi extreme-radius literature concerns the constant-mark case and therefore cannot itself contain the non-degenerate endpoint-mark law, but it supplies relevant extreme-value machinery.

## References

1. M. Schulte and M. Švarc Petráková, *Point process convergence of large inradii of Poisson-Laguerre tessellations*, arXiv:2609.20750v1 (2026), https://arxiv.org/abs/2609.20750v1.
2. C. Lautensack and S. Zuyev, *Random Laguerre tessellations*, Advances in Applied Probability 40 (2008), 630–650, https://doi.org/10.1239/aap/1222868179.
3. P. Calka and N. Chenavier, *Extreme values for characteristic radii of a Poisson-Voronoi tessellation*, Extremes 17 (2014), 359–385, https://doi.org/10.1007/s10687-014-0184-y.
4. N. Chenavier, M. Otto, and C. Thäle, *Poisson approximation with applications to stochastic geometry*, https://doi.org/10.1214/20-AAP1605.
5. N. H. Bingham, C. M. Goldie and J. L. Teugels, *Regular Variation*, Cambridge University Press, 1987.
