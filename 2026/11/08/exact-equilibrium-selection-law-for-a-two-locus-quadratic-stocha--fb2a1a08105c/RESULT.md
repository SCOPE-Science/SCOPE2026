# Exact equilibrium-selection law for a two-locus quadratic stochastic map

## Finding

For the two-locus quadratic stochastic operator of Diyorov and Rozikov, sampling the initial four gamete frequencies uniformly on their three-dimensional probability simplex produces an explicit non-Beta family of limiting allele-fraction distributions. For parameters \(0<a,b\leq 1\), put
\[
\kappa=\frac{(a-b)^2}{ab},\qquad s(z)=z(1-z).
\]
If \(Z\) is the second coordinate of the limiting product-state parameters, then its probability density on \(0<z<1\) is exactly
\[
\boxed{f_\kappa(z)=\frac{s(z)\bigl[\kappa(\kappa+2)s(z)+2(\kappa+3)\bigr]}{[1+\kappa s(z)]^2}.}
\]
In particular \(f_0(z)=6z(1-z)\), whereas the family tends to the uniform density for increasingly unequal positive parameters. For every fixed \(\kappa\), the rare-selection probability near either endpoint is
\[
\Pr(Z\leq\varepsilon)=(\kappa+3)\varepsilon^2+O_\kappa(\varepsilon^3)\quad(\varepsilon\downarrow0).
\]
The approach to uniformity has a singular boundary layer: for each \(w\geq0\),
\[
\lim_{\kappa\to\infty} f_\kappa(w/\kappa)=1-\frac{1}{(1+w)^2},\qquad
\lim_{\kappa\to\infty}\kappa\Pr(Z\leq w/\kappa)=\frac{w^2}{1+w}.
\]
The density convergence is pointwise for interior \(z\) and convergence in distribution; neither endpoint formula is uniform across all parameter and endpoint scales.

## Assumptions and scope

Let \(\mathcal S=\{(x,y,u,v):x,y,u,v\geq0,\ x+y+u+v=1\}\). The discrete-time map \(W_{a,b}:\mathcal S\to\mathcal S\) is
\[
\begin{aligned}
 x'&=x+a(yu-xv), &y'&=y-a(yu-xv),\\
 u'&=u-b(yu-xv), &v'&=v+b(yu-xv).
\end{aligned}
\]
We assume \(0<a,b\leq1\), and the starting state \((X,Y,U,V)\) is uniform with respect to the induced three-dimensional Euclidean volume on \(\mathcal S\), equivalently \(\operatorname{Dirichlet}(1,1,1,1)\). In this theorem \(C=X+Y\), and \(Z\) parametrizes the almost-sure limit
\[
(CZ,C(1-Z),(1-C)Z,(1-C)(1-Z)).
\]
The parameter \(\kappa\) is dimensionless and nonnegative. A limit \(\kappa\to\infty\) is taken through positive \(a,b\) in the given domain; it does not assert any theorem at a zero coefficient.

## Proof

**1. Selection of the limiting fixed point.** The first and second coordinate pairs sum to fixed values \(c=x+y\) and \(1-c=u+v\). Also \(bx+au\) is invariant under \(W_{a,b}\). Using \(y=c-x\), \(v=1-c-u\), write \(d(c)=a(1-c)+bc\). The restricted \((x,u)\)-map is linear with eigenvalues \(1\) and \(1-d(c)\). Since \(0<d(c)\leq1\) for \(c\in(0,1)\), the second eigenvalue has modulus less than one. Its fixed eigenvector is \((c,1-c)\), and invariance of \(bx+au\) identifies the limit as
\[
(x_\infty,u_\infty)=(cZ,(1-c)Z),\qquad
Z=\frac{bX+aU}{bC+a(1-C)}.
\]
The remaining coordinates follow from the conserved pair sums. The boundary cases \(C\in\{0,1\}\) have zero probability under the specified sampling law.

**2. Uniform-simplex disintegration.** The standard aggregation property of a uniform Dirichlet vector gives
\[
C\sim\operatorname{Beta}(2,2),\qquad f_C(c)=6c(1-c),
\]
while, conditional on \(C=c\), the variables \(R=X/c\) and \(S=U/(1-c)\) are independent uniform variables on \((0,1)\), and their joint distribution does not depend on \(c\). Accordingly,
\[
Z=q(c)R+[1-q(c)]S,\qquad
q(c)=\frac{bc}{a(1-c)+bc}.
\]
For \(0<q<1\), convolution of two uniforms gives for \(0<z<1\)
\[
h(z\mid q)=\frac{z-(z-q)_+-(z-1+q)_+}{q(1-q)},
\qquad t_+=\max(t,0).
\]
This is a normalized conditional density.

**3. Exact pushforward integration.** Because \(q(c)[1-q(c)]=ab\,c(1-c)/d(c)^2\),
\[
f(z)=\frac6{ab}\int_0^1d(c)^2
\left[z-(z-q(c))_+-(z-1+q(c))_+\right]dc.
\]
The two positive-part terms occur on \(c\in[0,c_q]\) and \(c\in[c_r,1]\), respectively, where
\[
c_q=\frac{az}{b(1-z)+az},\qquad
c_r=\frac{a(1-z)}{a(1-z)+bz}.
\]
Hence, with \(d(c)=a+(b-a)c\),
\[
\begin{aligned}
f(z)=\frac6{ab}\bigg[&z\int_0^1d(c)^2dc
-\int_0^{c_q}\bigl(zd(c)^2-bc\,d(c)\bigr)dc\\
&-\int_{c_r}^1\bigl(zd(c)^2-a(1-c)d(c)\bigr)dc\bigg].
\end{aligned}
\]
Every integrand here is a polynomial in \(c\); evaluating at the stated rational endpoints, cancelling factors and putting \(\kappa=(a-b)^2/(ab)\) yields the boxed expression. The accompanying exact-arithmetic checker independently re-evaluates these antiderivatives and verifies their equality to the compact formula. Since the conditional density \(h\) integrates to one, Fubini's theorem proves normalization without numerical integration.

**4. Parameter and endpoint limits.** The closed form is invariant under \(z\mapsto1-z\). For \(\kappa=0\), it becomes \(6z(1-z)\); for fixed \(0<z<1\), its leading numerator and denominator as \(\kappa\to\infty\) are both \(\kappa^2s(z)^2\), so \(f_\kappa(z)\to1\). The density is a mixture of the conditional laws above, hence integrates to one for each \(\kappa\); pointwise density convergence to a normalized density gives convergence in total variation by Scheffé's lemma.

For \(\kappa>0\), this law is not a Beta distribution: its symmetry and linear vanishing at both endpoints would force any Beta representation to be \(\operatorname{Beta}(2,2)\), but the central density is \(f_\kappa(1/2)=(\kappa+6)/(\kappa+4)<3/2\), unlike that Beta law. For fixed \(\kappa\), expansion at \(z=0\) gives \(f_\kappa(z)=2(\kappa+3)z+O_\kappa(z^2)\), proving the stated endpoint cumulative law. Finally, insert \(z=w/\kappa\) into the rational density and use \(\kappa s(w/\kappa)\to w\). This gives the first boundary-layer limit. The convergence is uniform for \(w\) in a fixed bounded interval by the explicit rational expression, and therefore integration after \(z=w/\kappa\) gives
\[
\lim_{\kappa\to\infty}\kappa\Pr(Z\leq w/\kappa)
=\int_0^w\left(1-\frac1{(1+r)^2}\right)dr
=\frac{w^2}{1+w}.
\]
This completes all asserted cases.

## Verification

The companion program `verify_two_locus.py` uses symbolic algebra to reconstruct the invariant \(bx+au\), the reduced dynamics, the full positive-part integral, the exact rational density, symmetry, endpoint coefficient, central density and boundary scaling. It also checks density normalization and conditional convolution numerically at four rational parameter pairs, with a documented tolerance for piecewise quadrature. The executed program printed `TWO_LOCUS_EXACT_DENSITY_AND_CRITICAL_SCALING_OK`. The proof, not a finite quadrature or symbolic log, establishes the claims for all allowed parameters.

## Relationship to prior work

Diyorov and Rozikov, *Evolutionary behavior in a two-locus system* (arXiv:2210.00247, first public 2022-10-01), establish the two-locus map, invariant fiber structure, and deterministic convergence formula; the present calculation **does not claim those facts as new**. Omirov and Rozikov, *A many-loci system with evolution characterized by uncountable linear operators* (arXiv:2409.19687), extend the invariant-fiber viewpoint, again without the stated uniform-simplex pushforward. Roozegar, *Certain Family of Some Beta Distributions Arising from Distribution of Randomly Weighted Average* (arXiv:1508.01731), develops Dirichlet-weighted averaging laws and beta closure; it covers related principles but not the parameter-dependent non-Dirichlet weight \(q(C)\) above. The previously known symmetric beta case is presented as a benchmark, not as a new special case. The claimed contribution is the concrete asymmetric selection density and its noncommuting edge/asymmetry limits.

## Limitations

The initial law is the uniform three-simplex distribution, not a demographic inference or a universal law for natural populations. No result is asserted for zero \(a\) or \(b\), or for arbitrary initial priors. The uniform high-asymmetry limit is a distributional limit; its endpoint behavior requires the separate boundary-layer scaling. Equivalent calculations may exist in unindexed or specialized probabilistic literature, and an independent mathematical audit has not been performed.

## References

1. A. M. Diyorov and U. A. Rozikov, *Evolutionary behavior in a two-locus system*, arXiv:2210.00247 (2022), https://arxiv.org/abs/2210.00247.
2. B. A. Omirov and U. A. Rozikov, *A many-loci system with evolution characterized by uncountable linear operators*, arXiv:2409.19687 (2024), https://arxiv.org/abs/2409.19687.
3. R. Roozegar, *Certain Family of Some Beta Distributions Arising from Distribution of Randomly Weighted Average*, arXiv:1508.01731 (2015), https://arxiv.org/abs/1508.01731.
4. H. Homei, *Randomly weighted averages with beta random proportions*, Statistics & Probability Letters (2012), DOI:10.1016/j.spl.2012.04.017. Full text not inspected.
