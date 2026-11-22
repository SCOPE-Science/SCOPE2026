# Hub rigidity for sharp short-time variation error of Kirchhoff heat on metric stars

## Finding

Let \(S_m\) be the compact metric star with \(m\ge3\) unit-length arms, each parametrized by \(x\in(0,1)\) outward from its common hub. Let \(H_t=e^{t\Delta_K}\) be the heat semigroup with Kirchhoff matching at the hub and Neumann conditions at the outer leaves. For real \(f=(f_1,\ldots,f_m)\) with \(f_j\in BV(0,1)\), put
\[
V_\star(f)=\sum_{j=1}^m |Df_j|((0,1))+
\min_{c\in\mathbb R}\sum_{j=1}^m|f_j(0+)-c|.
\]
Define \(C_m(t)^2=\sup_{V_\star(f)>0}\|(I-H_t)f\|_{L^2(S_m)}^2/V_\star(f)^2\). **For every integer \(m\ge3\), there exists \(t_m>0\) such that for every \(0<t<t_m\)**,
\[
\boxed{C_m(t)^2=\left(1-\frac1m\right)\frac2{\pi^2}
\sum_{n=0}^\infty\frac{\left(1-e^{-\pi^2(n+1/2)^2t}\right)^2}{(n+1/2)^2}.}
\]
Every nonconstant extremizer is exactly \(f=c+a\,\mathbf1_{\text{one entire arm}}\), almost everywhere, with \(c\in\mathbb R\) and \(a\ne0\). In particular,
\[
\boxed{\lim_{t\downarrow0}C_m(t)^2/\sqrt t=
2\left(1-\frac1m\right)\frac{2-\sqrt2}{\sqrt\pi}.}
\]
For three arms the coefficient is \(0.4406594750568629\ldots\); it increases strictly with the degree. This is **eventual short-time rigidity**, not an assertion of an explicit threshold or of the same optimizer at arbitrary time.

## Assumptions and scope

All edge measures are ordinary arclength and the norm squared is the sum of the \(m\) arm \(L^2(0,1)\) norms. At the hub the Kirchhoff Laplacian has a common continuous trace and sum of outward derivatives zero; at the leaves the derivatives vanish. The variation \(V_\star\) is the edgewise distributional variation plus the \(\ell^1\)-median mismatch of hub traces. It vanishes precisely on global constants. For stars it agrees with the metric-graph variation defined via bounded Kirchhoff test fields: integration by parts and the dual identity
\[\sup_{\substack{|z_j|\le1\\\sum_jz_j=0}}\sum_ja_jz_j
=\inf_{c\in\mathbb R}\sum_j|a_j-c|\]
show this, since the interior derivatives and hub traces of the test fields can be approximated independently away from vanishing boundary layers. No assumption of continuity of the input at the hub is imposed.

## Proof

**1. Sharp single-cut reduction.** Set \(h_{j,s}=\mathbf1_{\{\text{arm }j,\,x>s\}}\) for \(0\le s<1\). Choose a minimizing median \(c\) of the hub values. On each arm the signed measure \(\mu_j=(f_j(0+)-c)\delta_0+Df_j\) on \([0,1)\) gives the exact almost-everywhere representation
\[f-c=\sum_j\int_{[0,1)}h_{j,s}\,d\mu_j(s),\qquad \sum_j\|\mu_j\|_{TV}=V_\star(f).\]
Linearity, Minkowski's integral inequality, and \((I-H_t)\mathbf1=0\) therefore imply
\[C_m(t)^2=\max_{0\le s\le1}F_m(s,t),\quad F_m(s,t)=\|(I-H_t)h_{1,s}\|_2^2,\]
where \(h_{1,1}=0\) is included for compactness. Each step has \(V_\star(h_{1,s})=1\) for \(s<1\) when \(m\ge3\). This gives equality, not merely an upper bound.

**2. Exact scalar split.** Decompose \(\mathbb R^m\) into its common-arm line and its orthogonal zero-sum subspace. On the former the scalar operator has Neumann conditions at both ends (\(NN\)); on the latter it has Dirichlet condition at the hub and Neumann at the leaf (\(DN\)). If \(g_s=\mathbf1_{(s,1)}\), set \(N_t(s)=\|(I-P_t^{NN})g_s\|_{L^2(0,1)}^2\) and \(D_t(s)=\|(I-P_t^{DN})g_s\|_2^2\). Orthogonality gives the exact formula
\[F_m(s,t)=\frac1mN_t(s)+\left(1-\frac1m\right)D_t(s).\]
The scalar eigenbases give, for all \(t>0\) and \(s\in[0,1]\),
\[
N_t(s)=\frac2{\pi^2}\sum_{n=1}^\infty\frac{\sin^2(n\pi s)}{n^2}(1-e^{-\pi^2n^2t})^2,
\quad D_t(s)=\frac2{\pi^2}\sum_{n=0}^\infty\frac{\cos^2((n+1/2)\pi s)}{(n+1/2)^2}(1-e^{-\pi^2(n+1/2)^2t})^2.
\]
Thus \(N_t(0)=0\), and \(F_m(0,t)=(1-1/m)D_t(0)\), the claimed exact series provided the hub is uniquely maximizing for sufficiently small \(t\).

**3. Half-line boundary profiles and the strict branch gap.** Put \(L_\infty=(2-\sqrt2)/\sqrt\pi\). On the reflecting half-line, the squared heat residual of a step at distance \(s=z\sqrt t\) from the boundary is \(\sqrt t\,L(z)\), where
\[
L(0)=0,\qquad L'(z)=1-2\operatorname{erf}(z)+\operatorname{erf}(z/\sqrt2),\qquad
L(\infty)=L_\infty.
\]
The explicit antiderivative is
\[
L(z)=zL'(z)+\frac2{\sqrt\pi}(1-e^{-z^2})-\sqrt{\frac2\pi}(1-e^{-z^2/2}).
\]
The reflection kernels on the half-line are \(g_t(x-y)\pm g_t(x+y)\), with \(g_t(u)=e^{-u^2/(4t)}/\sqrt{4\pi t}\). For one step, the \(NN\) and \(DN\) squared residuals sum to \(2L_\infty\sqrt t\): write the free-line error as \(A(x)=\mathbf1_{x>s}-\Phi((x-s)/\sqrt{2t})\) and the reflected tail as \(B(x)=\Phi(-(x+s)/\sqrt{2t})\). The residuals are \(A-B\) and \(A+B\), while the truncated free-line integral of \(A^2\) differs from its whole-line integral by exactly \(\int_0^\infty B^2\). Consequently the **hub profile** for the star is
\[
J_m(z)=2\left(1-\frac1m\right)L_\infty-\left(1-\frac2m\right)L(z).
\]
For \(m\ge3\), \(L(z)>0\) whenever \(z>0\), so \(J_m\) has its unique global maximum at \(z=0\), of height \(H_m=2(1-1/m)L_\infty\).

At the outer Neumann leaf the local boundary profile is instead \(L(z)\), and in the bulk it is \(L_\infty\). To prove a quantitative strict separation, note that \(L'(z)=2\operatorname{erfc}(z)-\operatorname{erfc}(z/\sqrt2)\) has one positive zero: the Gaussian tail hazard rate is strictly increasing, hence \(\operatorname{erfc}(z/\sqrt2)/\operatorname{erfc}(z)\) increases strictly from \(1\) to infinity. Rational alternating-series bounds for \(\operatorname{erf}\), \(e^{-z}\), and Machin's series for \(\pi\) certify \(L'(.99)>0\), \(L'(1)<0\), \(L(1)<.4\), and \(L_\infty>.33\); see `checker.py` for exact-fraction interval inequalities. Since \(|L'|\le2\), the unique maximum of \(L\) is below \(.4+2(.01)=.42\). For every \(m\ge3\), \(H_m\ge\frac43L_\infty>.44>.42>\sup_zL(z)\), and also \(H_m>L_\infty\). These margins are strict and uniform in the degree.

**4. Transfer to the compact graph and exact localization.** The exact image kernels are
\[
K_t^{NN}(x,y)=\sum_{k\in\mathbb Z}\bigl(g_t(x-y+2k)+g_t(x+y+2k)\bigr),\quad
K_t^{DN}(x,y)=\sum_{k\in\mathbb Z}(-1)^k\bigl(g_t(x-y+2k)-g_t(x+y+2k)\bigr).
\]
For any fixed positive distance \(d\), \(\int_d^\infty g_t(v)\,dv\le C e^{-d^2/(8t)}\) for small \(t\); the corresponding Gaussian image series are dominated by a geometric sequence of such tails. Fix \(\delta=1/4\). When \(s\le\delta\), compare the finite-interval residual on \(x\le1/2\) with the half-line residual, retaining only the \(k=0\) direct and hub-reflected images; all other paths and missing source tails beyond \(y=1\) travel at least a fixed distance. On \(x>1/2\), both residuals are themselves exponentially small because the initial step is constant near the outer Neumann leaf. Thus the \(L^2\) norm and its square differ from the half-line value by \(O(e^{-c/t})\). At the observation point \(x=s\le1/4\), the same omitted-image bound holds for the heat integrals at times \(t\) and \(2t\). Gaussian tail integration yields, uniformly for \(0\le s\le\delta\), the following normalized profile and its derivative (the constants are absolute for each fixed \(m\)):
\[
F_m(s,t)=\sqrt t\,J_m(s/\sqrt t)+O(e^{-c/t}),\quad
\partial_sF_m(s,t)=J'_m(s/\sqrt t)+O(e^{-c/t})
\]
for some \(c>0\); the squared-residual derivative follows directly from
\[\partial_s E_t(s)=-1+4(P_tg_s)(s)-2(P_{2t}g_s)(s),\quad E_t(s)=\|(I-P_t)g_s\|_2^2.\]
The image terms omitted on the hub side travel at least a fixed positive distance to and from the opposite leaf, so Gaussian tails bound both displayed errors; any polynomial factor in \(t^{-1}\) is absorbed by the exponential. For \(\delta\le s\le1-\delta\), the same kernels give \(F_m(s,t)=L_\infty\sqrt t+O(e^{-c/t})\) uniformly. For \(1-\delta\le s\le1\), reflecting the coordinate about the Neumann leaf gives \(F_m(s,t)=\sqrt t\,L((1-s)/\sqrt t)+O(e^{-c/t})\), uniformly. These claims follow termwise from the image series, whose nonlocal image separations are bounded below by a positive constant in each stated zone.

Choose \(\varepsilon>0\) small enough that \(L'(z)>1/2\) on \([0,\varepsilon]\). On \(0\le s\le\varepsilon\sqrt t\), the derivative formula gives \(\partial_s F_m<0\) when \(t\) is sufficiently small. On \(\varepsilon\sqrt t\le s\le\delta\), \(\inf_{z\ge\varepsilon}L(z)>0\) and hence \(J_m(z)\le H_m-(1-2/m)\inf_{z\ge\varepsilon}L(z)<H_m\). The exponentially small errors do not close this gap. The middle and outer-leaf zones are separated from \(H_m\) by the strict bounds above. Since \(F_m(0,t)=H_m\sqrt t+O(e^{-c/t})\), the unique global maximizing location is \(s=0\) for all sufficiently small \(t\), giving the exact spectral series.

**5. Equality rigidity and leading coefficient.** Because \(H_t\) is self-adjoint and its only stationary functions are constants, \(I-H_t\) is injective modulo global constants. Distinct single cuts \(h_{j,s}\) are not scalar multiples modulo constants when \(m\ge3\). Equality in the Hilbert-space integral triangle inequality therefore forces the signed-variation measure to be concentrated at one maximizing cut, yielding exactly a scalar multiple of one whole-arm indicator plus a global constant. Finally, the half-line Dirichlet profile at \(s=0\), or the same Gaussian image estimate, gives \(D_t(0)/\sqrt t\to2L_\infty\); this proves the displayed degree-dependent limit.

## Verification

`checker.py` uses only the Python standard library. It executes exact rational interval checks of the analytic leaf-versus-hub gap, confirms the half-line derivative signs and normalizations, and cross-checks the two scalar spectral components and their weighted star decomposition numerically. A finite check is not a proof of the infinite-dimensional supremum; the proof is the measure reduction and Gaussian-profile comparison above. Run with `python checker.py`.

## Relationship to prior work

Kostrykin, Potthoff, and Schrader (arXiv:math-ph/0701009, first posted January 4, 2007) provide general metric-graph heat kernels and the Kirchhoff scattering rule \(2/m-\delta_{ij}\). Their kernel and trace formulas do not state the variation-to-\(L^2\) residual norm, its whole-arm extremizers, or the exact degree-dependent sharp coefficient. Frank and Kovařík (arXiv:1108.6145, first posted August 31, 2011) establish graph/tree heat-kernel bounds and Schrödinger spectral consequences, not exact bounded-variation residual norms. Marola, Miranda Jr., and Shanmugalingam (arXiv:1405.0186, first posted May 1, 2014) study heat-characterizations of perimeter and variation in metric spaces, not this operator's sharp error norm. Mazón (arXiv:2112.13035, first posted December 24, 2021) develops a metric-graph variation including vertex jumps and nonlinear total-variation flow; it is supporting later context, not the archival primary source or an equivalent sharp theorem. Related periodic-circle and reflecting-interval heat estimates involve degree-two rather than branching Kirchhoff geometry, so their inequalities do not imply the strict degree-three hub-versus-leaf comparison under the star variation defined here.

## Limitations

The theorem asserts existence, not an explicit or optimal numerical value, of the time threshold \(t_m\). It treats equal unit arms and Kirchhoff heat with outer Neumann conditions; arbitrary edge lengths, vertex masses, different diffusion coefficients, other error norms, and longer times are not classified. Unindexed historical equivalents or broader results not encountered in the source comparison remain a priority risk. Numerical evaluations and rational interval calculations complement, but do not replace, the analytic argument.

## References

1. V. Kostrykin, J. Potthoff, R. Schrader, *Heat kernels on metric graphs and a trace formula*, arXiv:math-ph/0701009 (initial public posting 2007-01-04), https://arxiv.org/abs/math-ph/0701009.
2. N. Marola, M. Miranda Jr., N. Shanmugalingam, *Characterizations of sets of finite perimeter using heat kernels in metric spaces*, arXiv:1405.0186 (initial public posting 2014-05-01), https://arxiv.org/abs/1405.0186.
3. R. L. Frank, H. Kovařík, *Heat kernels of metric trees and applications*, arXiv:1108.6145 (initial public posting 2011-08-31), https://arxiv.org/abs/1108.6145.
4. J. M. Mazón, *The Total Variation Flow in Metric Graphs*, arXiv:2112.13035 (initial public posting 2021-12-24), https://arxiv.org/abs/2112.13035.
