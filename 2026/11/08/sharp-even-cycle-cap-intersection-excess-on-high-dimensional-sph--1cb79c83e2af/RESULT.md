# Sharp even-cycle cap-intersection excess on high-dimensional spheres

## Finding
For independent uniform points \(U_1,\ldots,U_{2r}\) on the unit sphere \(S^{d-1}\), with cyclic convention \(U_{2r+1}=U_1\), consider the simultaneous occurrence of the \(2r\) spherical cap-incidence conditions \(\langle U_j,U_{j+1}\rangle\ge c\). Although every proper set of these cyclic incidences is independent, the full set is not.

Let \(p=p_d(c)=\Pr(\langle U_1,U_2\rangle\ge c)\) and define the *even-cycle excess*
\[\Delta_{2r,d}(c)=\Pr\bigl(\bigcap_{j=1}^{2r}\{\langle U_j,U_{j+1}\rangle\ge c\}\bigr)-p^{2r}.\]
For integers \(d\ge3\), \(r\ge2\), and \(-1<c<1\), write
\[L=L_d(c)=\frac{\Gamma(d/2)}{(d-1)\sqrt\pi\Gamma((d-1)/2)}(1-c^2)^{(d-1)/2},\qquad \eta^2=c^2+\frac{1-c^2}{d+1}.\]
Then the exact finite-dimensional **spectral enclosure** is
\[\boxed{0<dL^{2r}\le \Delta_{2r,d}(c)\le dL^{2r}+(L^2\eta^2)^{r-1}\bigl[p(1-p)-dL^2\bigr].}\]
The bracket is nonnegative. The upper bound is computable from the one-edge cap probability, without any multivariate integration.

For \(\phi(z)=(2\pi)^{-1/2}e^{-z^2/2}\) and standard normal distribution function \(\Phi\), for fixed \(r\ge2\) and fixed real \(z\),
\[\boxed{\Delta_{2r,d}(z/\sqrt d)=\phi(z)^{2r}d^{1-r}+O_{r,z}(d^{-r}).}\]
The implied bound is uniform for \(z\) in each fixed compact interval. At fixed edge probability \(p_0\in(0,1)\), choosing the unique cap threshold \(c_{d,p_0}\) yields
\[\boxed{\Delta_{2r,d}(c_{d,p_0})=\phi(\Phi^{-1}(1-p_0))^{2r}d^{1-r}+O_{r,p_0}(d^{-r}).}\]
In particular, for four points and hemisphere incidences,
\[\Delta_{4,d}(0)=\frac{1}{4\pi^2d}+O(d^{-2}).\]
The strict positive sign of even-cycle excess follows already from familiar positive trace identities. The contribution here is the explicit sharp finite-dimensional first-harmonic enclosure, with its all-even-cycle leading constants and bounded-threshold error rates.

## Assumptions and scope
The sphere is the Euclidean unit sphere in \(\mathbb R^d\), equipped with normalized rotation-invariant surface measure \(\sigma_d\); all points are independent. A cap incidence is the event \(\langle u,v\rangle\ge c\) for \(-1<c<1\), equivalent to the shorter great-circle distance being at most \(\arccos c\). The cycle contains \(2r\) distinct vertices; \(r\ge2\) ensures at least four. The dimension \(d\) is an integer at least three. All probability statements concern this precise sampling scheme, not arbitrary random graphs, dependent point processes, or dimensions growing with cycle length. The asymptotic statements keep \(r\) fixed while \(d\to\infty\).

## Proof
**1. Cycle centering and trace.** Let \(K_c(u,v)=\mathbf1_{\{\langle u,v\rangle\ge c\}}-p\). Every proper edge subset of the simple cycle is a forest. Its edge indicators are jointly independent Bernoulli \(p\): successively integrate leaf vertices, and each conditional incident-edge probability equals \(p\) by rotation invariance. Expanding the product of centered indicators therefore gives exactly
\[\Delta_{2r,d}(c)=\mathbb E\prod_{j=1}^{2r}K_c(U_j,U_{j+1}).\]
Let \(T_c\) denote the integral operator with kernel \(K_c\) on \(L^2(S^{d-1},\sigma_d)\). It is self-adjoint and Hilbert–Schmidt, since its bounded kernel is square integrable. For \(r\ge2\), cyclic kernel integration and the trace-class property of \(T_c^{2r}\) imply
\[\Delta_{2r,d}(c)=\operatorname{Tr}(T_c^{2r}).\]

**2. Explicit harmonic eigenvalues.** Put
\[w_d(t)=\frac{\Gamma(d/2)}{\sqrt\pi\Gamma((d-1)/2)}(1-t^2)^{(d-3)/2},\quad -1<t<1.\]
This is the density of the inner product between two independent uniform sphere points. Write \(P_{k,d}\) for the normalized zonal Gegenbauer polynomial of degree \(k\), with \(P_{k,d}(1)=1\); its degree-\(k\) spherical-harmonic multiplicity is \(m_{k,d}\), with \(m_{1,d}=d\). The Funk–Hecke formula gives the eigenvalues \(\lambda_{0}=0\) and
\[\lambda_{k,d}(c)=\int_c^1w_d(t)P_{k,d}(t)\,dt\qquad(k\ge1).\]
The zonal Sturm–Liouville equation
\[\big[(1-t^2)^{(d-1)/2}P'_{k,d}(t)\big]'=-k(k+d-2)(1-t^2)^{(d-3)/2}P_{k,d}(t)\]
and the standard derivative relation
\[P'_{k,d}(t)=\frac{k(k+d-2)}{d-1}P_{k-1,d+2}(t)\]
give, by integration to the endpoint \(1\),
\[\boxed{\lambda_{k,d}(c)=L_d(c)P_{k-1,d+2}(c),\qquad k\ge1.}\]
The first nonconstant eigenvalue is thus \(\lambda_{1,d}(c)=L_d(c)>0\), with multiplicity \(d\).

**3. Uniform suppression of higher harmonics.** For every \(D\ge3\) and integer \(m\ge1\), the normalized zonal polynomial has the complex-moment representation
\[P_{m,D}(c)=\mathbb E\big[(c+i\sqrt{1-c^2}\,V)^m\big],\]
where \(V\) is the first coordinate of a uniformly distributed point on \(S^{D-2}\). In particular, \(\mathbb EV=0\) and \(\mathbb EV^2=1/(D-1)\). Since \(|c+i\sqrt{1-c^2}V|\le1\), Jensen/Cauchy–Schwarz give
\[|P_{m,D}(c)|\le\mathbb E|c+i\sqrt{1-c^2}V|^m\le\sqrt{c^2+\frac{1-c^2}{D-1}}.\]
Taking \(D=d+2\), every \(k\ge2\) satisfies
\[|\lambda_{k,d}(c)|\le L_d(c)\eta_d(c).\]

**4. Sharp first-harmonic enclosure.** Parseval for the Hilbert–Schmidt operator gives
\[\sum_{k\ge1}m_{k,d}\lambda_{k,d}(c)^2=\int\!\int K_c(u,v)^2\,d\sigma_d(u)d\sigma_d(v)=p(1-p).\]
Separating the first harmonic and bounding the others yields
\[\begin{aligned}
\Delta_{2r,d}(c)&=dL^{2r}+\sum_{k\ge2}m_{k,d}\lambda_{k,d}^{2r},\\
0&\le\sum_{k\ge2}m_{k,d}\lambda_{k,d}^{2r}\\
&\le (L^2\eta^2)^{r-1}\sum_{k\ge2}m_{k,d}\lambda_{k,d}^{2}\\
&=(L^2\eta^2)^{r-1}\big[p(1-p)-dL^2\big].
\end{aligned}\]
Every term in the even trace is nonnegative and \(L>0\), proving strict positivity and the enclosure for all stated finite parameters.

**5. Dimension asymptotics and fixed-density quantiles.** Uniformly for bounded \(z\), Stirling's gamma-ratio expansion and \(\log(1-z^2/d)=-z^2/d+O_z(d^{-2})\) imply
\[L_d(z/\sqrt d)=\frac{\phi(z)}{\sqrt d}\big[1+O_z(d^{-1})\big],\qquad \eta_d(z/\sqrt d)^2=O_z(d^{-1}).\]
Since \(0\le p(1-p)-dL^2\le1/4\), the higher-harmonic remainder is \(O_{r,z}(d^{-2r+2})\), bounded by \(O_{r,z}(d^{-r})\) for \(r\ge2\). Meanwhile \(dL^{2r}=\phi(z)^{2r}d^{1-r}+O_{r,z}(d^{-r})\). This proves the first asymptotic, with constants uniform on any bounded \(z\)-interval.

For a fixed \(p_0\in(0,1)\), the density of \(\sqrt d\langle U_1,U_2\rangle\) is \(\phi(z)[1+O_M(d^{-1})]\) on each fixed interval \([-M,M]\). Gaussian convergence and a one-dimensional local inverse-CDF estimate at the positive density \(\phi(z_{p_0})\), where \(z_{p_0}=\Phi^{-1}(1-p_0)\), give
\[\sqrt d\,c_{d,p_0}=z_{p_0}+O_{p_0}(d^{-1}).\]
Substitute this into the uniform bounded-threshold expansion. Setting \(z=0\) and \(r=2\) yields \(\phi(0)^4=1/(4\pi^2)\), as claimed.

## Verification
An executable standalone checker is provided as `check_even_spherical_cycles.py`, using the packages listed in `requirements.txt`. Running it prints `EVEN_SPHERICAL_CYCLE_EXCESS_TESTS_OK`. It independently integrates the Funk–Hecke kernel for 28 combinations of dimension/threshold/harmonic degree, compares those values with the closed eigenvalues, checks truncated spectral traces and dimension-dependent upper bounds, and simulates \(600000\) independent four-point configurations in each of dimensions \(3,6,12\). It also checks the asymptotic \(d\Delta_{4,d}(0)\to1/(4\pi^2)\). Finite numerical calculations do not prove the infinite-dimensional trace bound or the analytic remainder estimate; those follow from the preceding mathematical arguments.

## Relationship to prior work
Bubeck, Ding, Eldan and Rácz (2014, arXiv:1411.5713) study the same spherical threshold sampling model but mainly signed triangles, testing limits and dimension detection. Their results do not state this all-even-cycle sharp coefficient or the explicit finite-dimensional first-harmonic enclosure.

Bangachev and Bresler (2024, arXiv:2402.12589), especially Proposition 1.3, the cycle discussion immediately after it and Appendix A.2, already study signed cycle subgraphs. They prove polylogarithmic-factor upper bounds of the correct dimensional exponent at half density and bound four-cycle contributions. This work **does not claim** the definition of cycle Fourier coefficients, the exponent, or the fact of positivity as new. The claim is the explicit matching coefficient for every even cycle and every fixed edge density, together with the precise finite-dimensional spectral enclosure. The earlier bounds do not give those constants or the stated enclosure.

The classical Funk–Hecke identity, normalized Gegenbauer derivative formulas, even-cycle graphon trace positivity, and Gaussian spherical coordinate limits are inputs rather than novel propositions. Related geometric-graph limit papers by Erba and coauthors (2020, arXiv:2002.12272) and Liu–Rácz (2021, arXiv:2110.15886) study different ensembles or general detection statistics; neither inspected source gives the claimed all-even spherical-cap quantitative formula.

## Limitations
This is a statement for independent, uniformly distributed sphere points and a *fixed* even cycle length. Constants in the asymptotic errors may depend on cycle length and threshold/density; no joint growing-cycle regime or extreme sparse probability regime is established. Strict positivity by itself is pre-existing. No comprehensive historical uniqueness certificate is asserted: any uninspected treatment of spherical cap operator spectra and trace powers could imply comparable formulas. The numerical checker is corroboration, not an independent proof or independent audit.

## References
- S. Bubeck, J. Ding, R. Eldan and M. Z. Rácz, *Testing for high-dimensional geometry in random graphs*, arXiv:1411.5713, first public 2014-11-20. https://arxiv.org/abs/1411.5713
- K. Bangachev and G. Bresler, *On The Fourier Coefficients of High-Dimensional Random Geometric Graphs*, arXiv:2402.12589, first public 2024-02-19. https://arxiv.org/html/2402.12589v1
- V. Erba et al., *Random geometric graphs in high dimension*, arXiv:2002.12272 (2020). https://arxiv.org/abs/2002.12272
- L. Liu and M. Z. Rácz, *A probabilistic view of latent space graphs and phase transitions*, arXiv:2110.15886 (2021). https://arxiv.org/abs/2110.15886
