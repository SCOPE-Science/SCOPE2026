# Three sharp radial regimes for A-optimal weighted Bergman circle sampling

## Finding
Let \(\alpha>-1\), \(p=\alpha+2>1\), and \(N\ge1\). Among all weighted designs of at most \(N+1\) point evaluations located on one centered circle in the unit disk, where each observation is normalized by the **full** weighted Bergman evaluation-kernel norm and total observation weight is one, there is exactly one design minimizing \(\operatorname{tr}(G^{-1})\): the uniformly weighted regular \((N+1)\)-gon, up to common rotation, at the unique squared radius \(x_N\in(0,1)\) solving
\[
\frac{\sum_{k=0}^N k\,b_k x_N^{-k}}{\sum_{k=0}^N b_k x_N^{-k}}
=\frac{p x_N}{1-x_N},\qquad
b_k=\frac{k!}{(p)_k}.
\]
Writing \(L_N=-N\log x_N\), its sharp three-regime law is
\[
\begin{array}{ll}
-1<\alpha<0:&L_N\longrightarrow c_p,\\
\alpha=0:&L_N=\log\log N+\log2+o(1),\\
\alpha>0:&L_N=\alpha\log N+\log\!\left(\dfrac{(\alpha+2)(\alpha+1)}{\alpha\,\Gamma(\alpha+2)}\right)+o(1).
\end{array}
\]
For \(1<p<2\), \(c_p\) is the unique positive solution of
\[
c_p\frac{\int_0^1u^{2-p}e^{c_pu}\,du}{\int_0^1u^{1-p}e^{c_pu}\,du}=p.
\]
The optimal inverse-Gram trace \(\mathcal A_N\) satisfies
\[
\mathcal A_N\sim
\begin{cases}
\dfrac{\Gamma(p)}{c_p^{p}}\left(\int_0^1u^{1-p}e^{c_pu}\,du\right)N^2,&1<p<2,\\
\dfrac{N^2\log N}{(\log\log N)^2},&p=2,\\
\dfrac{p-1}{(p-2)^{p+1}}\left(\dfrac{N}{\log N}\right)^p,&p>2.
\end{cases}
\]
In particular, the logarithmic and double-logarithmic radius scales are genuine transitions across the unweighted disk exponent \(\alpha=0\).

## Assumptions and scope
The Hilbert space \(A^2_\alpha(\mathbb D)\) uses probability area measure \((\alpha+1)(1-|z|^2)^\alpha dA(z)/\pi\), with monomial orthonormal basis \(e_k(z)=\sqrt{(p)_k/k!}\,z^k\) and full reproducing kernel \(K_p(z,w)=(1-z\overline w)^{-p}\). Restrict to \(\mathcal P_N=\operatorname{span}\{e_0,\ldots,e_N\}\). A design is \(m\le N+1\) sites \(z_j=r\zeta_j\), \(0<r<1\), \(|\zeta_j|=1\), positive masses \(w_j\) summing to one, and measurement matrix
\[
(Af)_j=\sqrt{w_j}\,(1-r^2)^{p/2}f(z_j).
\]
Its information matrix is \(G=A^*A\) on \(\mathcal P_N\); define the A-risk as \(\operatorname{tr}(G^{-1})\) when \(G\) is invertible and \(+\infty\) otherwise. Each measurement has unit full-space kernel norm before multiplication by its design-budget weight. The theorem is about fixed-cardinality, single-radius, positive measurement designs; it does not claim optimality over freely varying radii or alternative normalizations.

## Proof
**1. Exact global angular optimization.** Write \(x=r^2\), \(a_k=(p)_k/k!\), and \(\widehat\mu(h)=\sum_jw_j\zeta_j^h\). In the monomial basis,
\[
G_{k\ell}=(1-x)^p\sqrt{a_ka_\ell}\,x^{(k+\ell)/2}\widehat\mu(k-\ell),\quad0\le k,\ell\le N.
\]
Thus \(G_{kk}=(1-x)^pa_kx^k\), independent of the angular design. For any positive-definite matrix \(G\), the Schur-complement identity gives \((G^{-1})_{kk}\ge G_{kk}^{-1}\), with equality in every coordinate if and only if \(G\) is diagonal. Hence
\[
\operatorname{tr}(G^{-1})\ge F_{N,p}(x):=(1-x)^{-p}\sum_{k=0}^Nb_kx^{-k},\quad b_k=a_k^{-1}.
\]
Equality is equivalent to \(\widehat\mu(h)=0\) for all \(1\le h\le N\). Such a positive probability measure with at most \(N+1\) support points must have exactly \(N+1\), and its \((N+1)\)-by-\((N+1)\) Fourier Vandermonde matrix with rows \(\sqrt{w_j}(1,\zeta_j,\ldots,\zeta_j^N)\) is unitary. Row norms force \(w_j=1/(N+1)\). Orthogonality of distinct rows forces their quotients to be nontrivial \((N+1)\)-st roots of unity. This is exactly a rotated regular polygon, which conversely attains equality.

**2. Unique exact radius.** Set \(t=-\log x>0\), \(S_N(t)=\sum_{k=0}^Nb_ke^{kt}\). Then
\[
\frac{d}{dt}\log F_{N,p}(e^{-t})=\frac{S_N'(t)}{S_N(t)}-\frac p{e^t-1}.
\]
The first summand is the expectation of \(k\) under a strictly positive exponential family and is strictly increasing (derivative is its positive variance); the negative second summand is strictly increasing. The total derivative ranges from \(-\infty\) at \(t\downarrow0\) to \(N>0\) at \(t\to\infty\). Consequently there is precisely one critical point, a strict global minimum. The displayed finite equation follows by substituting \(x=e^{-t}\).

**3. Small weight exponents.** Put \(L=Nt\). For fixed \(1<p<2\), Gamma-ratio asymptotics and integrable Riemann sums give, uniformly for bounded positive \(L\),
\[
S_N(L/N)\sim \Gamma(p)N^{2-p}I_0(L),\qquad
S_N'(L/N)\sim\Gamma(p)N^{3-p}I_1(L),
\]
where \(I_0(L)=\int_0^1u^{1-p}e^{Lu}du\), \(I_1(L)=\int_0^1u^{2-p}e^{Lu}du\). Comparing the exact derivative at two fixed \(L\)-values brackets its unique zero. The limit equation is \(L I_1(L)/I_0(L)=p\). This left side grows strictly from zero to infinity, since \(I_1/I_0>0\) and its derivative is the positive variance of \(u\) under the density proportional to \(u^{1-p}e^{Lu}\). Thus \(L_N\to c_p\). Substituting \(1-e^{-L_N/N}\sim c_p/N\) proves the first sharp risk constant.

**4. Critical unweighted disk.** At \(p=2\) the coefficients are exactly \(b_k=1/(k+1)\). The geometric-series identity \(S_N'(t)=\sum_{k=0}^N e^{kt}-S_N(t)\) turns the exact stationarity condition into
\[
S_N(t)=\frac{e^{(N+1)t}-1}{e^t+1}.
\]
For any fixed real \(c\), evaluate the derivative at \(t=(\log\log N+c)/N\). The elementary bounds
\[
\sum_{k=0}^N\frac1{k+1}=\log N+O(1),\quad
0\le S_N(t)-\sum_{k=0}^N\frac1{k+1}
\le C\!\int_0^1\frac{e^{Lu}-1}{u}\,du+O(e^L L/N)
=O(e^L/L+L)
\]
for \(L=\log\log N+c\) yield \(S_N(t)=\log N(1+o(1))\), while the stationarity right side is \(e^c\log N/2\,(1+o(1))\). Therefore the derivative changes sign across \(c=\log2\), proving \(L_N=\log\log N+\log2+o(1)\). The risk asymptotic follows from \(S_N(t_N)\sim\log N\).

**5. Positive weight exponents.** For \(p>2\), the Beta-integral representation
\[
b_k=(p-1)\int_0^1u^k(1-u)^{p-2}\,du
\]
implies \(\sum_{k\ge0}b_k=B_p=(p-1)/(p-2)\). For every fixed \(c\in\mathbb R\) let \(L=(p-2)\log N+c\) and \(t=L/N\). Splitting the sums at \(k=\varepsilon N\) and \(k=(1-\varepsilon)N\) for fixed small \(\varepsilon>0\), Gamma-ratio comparison on the middle block and the endpoint change \(v=L(1-k/N)\) on the final block give
\[
S_N(L/N)=B_p+o(1),\qquad
S_N'(L/N)=\frac{\Gamma(p)e^cN}{L}(1+o(1)).
\]
The low-block derivative is \(o(N/L)\): by \(b_k\ll(k+1)^{1-p}\) it is \(O(N^{\max(3-p,0)+\varepsilon(p-2)}\log N)\), with a slightly smaller \(\varepsilon\) if \(p\ge3\). The middle block is exponentially smaller than the endpoint contribution in \(L\); the final block gives the displayed coefficient by a one-sided exponential integral. Therefore at the test value \(L=(p-2)\log N+c\) the exact stationary derivative has the sign of \(\Gamma(p)e^c/B_p-p\), up to an error tending to zero after division by \(N/L\). Strict monotonicity brackets the unique root, so
\[
L_N=(p-2)\log N+\log\!\left(\frac{pB_p}{\Gamma(p)}\right)+o(1).
\]
Finally \(S_N(t_N)\to B_p\) and \(1-e^{-t_N}\sim(p-2)\log N/N\), proving the positive-exponent risk constant. This completes all cases.

## Verification
The companion `verify.py` recreates finite Gram matrices, checks the angular trace-inverse inequality and regular-polygon equality, verifies the strictly monotone stationary equation by independent bisection, and compares representative finite optimizers with the asymptotic regimes. These are diagnostic finite computations, not replacements for the analytic all-degree proof. Execute `python3 verify.py` with Python 3 standard library. All constants in the theorem are determined without numerical fitting.

## Relationship to prior work
The normalized Bergman kernels and best-kernel approximation context are explicit in Qu, Qian, Li and Zhu (available online 10 November 2021), but that paper optimizes projections for individually specified functions and proves existence, not a single-circle positive-budget A-optimal inverse-trace criterion. Moeller and Ullrich (2021) study randomized RKHS recovery and worst-case norms, not this deterministic finite-dimensional inverse-Gram risk. The published published-finding corpus record `2026/11/2/SCOPE-universal-single-circle-conditioning-obstruction-for-weighted-be--c051d241328b` gives sharp **spectral condition-number** optimality for one-circle weighted Bergman sampling; the present trace-inverse objective is different, and its weight-dependent logarithm/double-logarithm transition is not implied by that condition-number formula. The regular-polygon Fourier rigidity is a shared ingredient and is not separately asserted to be new.

## Limitations
Historical priority remains provisional. The public published-finding corpus search summary of the nearest condition-number result was accessible, but complete underlying repository contents could not be retrieved; that comparison is based on its stated theorem, not a claimed full-text negative search. The statement assumes the full-space kernel normalization \((1-r^2)^{p/2}\), positive weights with sum one, at most \(N+1\) points, and a common sample radius. Changing the normalization or allowing multiple radii changes the optimal design; no result is claimed in those settings. The unweighted \(\log\log N\) expansion is asymptotic and converges slowly at feasible finite degrees. Independent validation has not been performed.

## References
- W. Qu, T. Qian, H. Li, and K. Zhu, *Best kernel approximation in Bergman spaces*, Applied Mathematics and Computation 416 (2022), 126749; first online 10 November 2021, DOI 10.1016/j.amc.2021.126749; lawful author-hosted full text: https://fie.must.edu.mo/id-14973/file/view/id-11806.pdf?locale=zh_MO
- M. Moeller and T. Ullrich, *\(L_2\)-norm sampling discretization and recovery of functions from RKHS with finite trace*, Sampling Theory, Signal Processing, and Data Analysis 19 (2021), article 13, https://doi.org/10.1007/s43670-021-00013-3.
- Published published-finding corpus record, *Universal single-circle conditioning obstruction for weighted Bergman polynomial sampling*, 2 November 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-universal-single-circle-conditioning-obstruction-for-weighted-be--c051d241328b (summary accessible, underlying repository page not retrieved).
