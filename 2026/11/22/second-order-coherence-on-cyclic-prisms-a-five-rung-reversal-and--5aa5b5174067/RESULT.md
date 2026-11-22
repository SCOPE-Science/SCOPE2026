# Second-order coherence on cyclic prisms: a five-rung reversal and a six-fifths allocation law

## Finding

**Theorem.** For each integer \(m\ge3\), form the cyclic prism \(G_m=C_m\square K_2\). Assign a nonnegative conductance independently to each of its \(3m\) edges, with sum of all conductances equal to one; disconnected networks have infinite objective. For \(p\in\{1,2\}\) minimize the inverse Laplacian spectral moment
\[
F_p(L)=\sum_{j=2}^{2m}\lambda_j(L)^{-p}=\operatorname{tr}((L^+)^p).
\]
Here \(L^+\) is the Moore--Penrose inverse of the connected weighted graph Laplacian. Both problems have **unique global minimizers without any imposed edge-orbit equality**. The minimizer for order \(p\) places common positive conductance \(a_{p,m}\) on every rail edge and common positive conductance \(b_{p,m}\) on every rung. Put \(t_{p,m}=b_{p,m}/a_{p,m}\), \(\mu_k=4\sin^2(\pi k/m)\), and
\[
S_{1,m}=\frac{m^2-1}{12},\qquad S_{2,m}=\frac{m^4+10m^2-11}{720}.
\]
Then \(t_{p,m}\) is the **unique positive solution** of
\[
\boxed{\ \sum_{k=0}^{m-1}\frac{4-\mu_k}{(\mu_k+2t_{p,m})^{p+1}}=S_{p,m}.\ }
\]
The exact conductances and objective values are
\[
a_{p,m}=\frac1{m(2+t_{p,m})},\quad
b_{p,m}=\frac{t_{p,m}}{m(2+t_{p,m})},\quad
F_p^*=m^p(2+t_{p,m})^p\left(S_{p,m}+\sum_{k=0}^{m-1}(\mu_k+2t_{p,m})^{-p}\right).
\]

The objectives' preferred **rung-to-rail ratios reverse at exactly five rungs**:
\[
\boxed{\quad t_{2,3}>t_{1,3},\quad t_{2,4}=t_{1,4}=1,\quad
 t_{2,m}<t_{1,m}\ \text{for every integer }m\ge5.\quad}
\]
There is also a sharp distinction in large-prism scales, where \(c_1=18^{1/3}\) and \(c_2=540^{2/5}/2\):
\[
\boxed{\ t_{1,m}\sim c_1m^{-2/3},\qquad t_{2,m}\sim c_2m^{-6/5}.\ }
\]
The second-order minimum and regret of reusing the first-order design satisfy
\[
\boxed{\ F_2^*=\frac{m^6}{180}+\frac{c_2}{108}m^{24/5}+o(m^{24/5}),\qquad
F_2(L_{1,m}^*)-F_2(L_{2,m}^*)\sim\frac{c_1}{180}m^{16/3}.\ }
\]
The corresponding relative regret tends to zero, with
\[
\frac{F_2(L_{1,m}^*)}{F_2(L_{2,m}^*)}=1+c_1m^{-2/3}+o(m^{-2/3}).
\]

## Assumptions and scope

Vertices are labelled \((j,\ell)\), where \(j\in\mathbb Z/m\mathbb Z\) and \(\ell\in\{0,1\}\). Each rail joins \((j,\ell)\) to \((j+1,\ell)\), and rung \(j\) joins \((j,0)\) to \((j,1)\). All \(2m\) rails and \(m\) rungs have the same unit cost, and the budget is exactly one. Individual edge conductances are initially unrestricted nonnegative real variables; orbit equality is proved, not assumed. The network is undirected, the Laplacian is unnormalized, and the smallest admissible cycle is a triangle. For any positive alternative total budget \(B\), multiply optimal conductances by \(B\) and divide \(F_p^*\) by \(B^p\). The objective for \(p=2\) is proportional to the steady-state disagreement coherence in a standard second-order noisy consensus model at fixed network size and damping coefficient; the displayed raw spectral trace is the precisely optimized invariant.

## Proof

**1. Existence, unrestricted uniqueness, and symmetry.** For any connected feasible conductance vector, restrict its Laplacian to \(\mathbf1^\perp\), obtaining a positive-definite symmetric matrix \(A\). Write \(H\) for a nonzero symmetric Laplacian perturbation restricted to that space. For \(p=1\), the second derivative of \(\operatorname{tr}(A^{-1})\) is \(2\operatorname{tr}(A^{-1}HA^{-1}HA^{-1})>0\). For \(p=2\), the second derivative is
\[
2\sum_{j=1}^{3}\operatorname{tr}(A^{-j}H A^{-(4-j)}H)>0.
\]
Every summand is a squared Frobenius norm of an invertibly conjugated version of \(H\), hence is positive for nonzero \(H\). Distinct edge conductance vectors give distinct full Laplacians, because off-diagonal entries identify the conductance of each simple edge, and the restriction to \(\mathbf1^\perp\) preserves these distinctions. Consequently both spectral-moment objectives are strictly convex over connected feasible edge weights. They tend to infinity as the weighted network approaches disconnection, and attain minima on the compact budget simplex. Homogeneity implies that every optimum uses the full budget. The prism's rotations, reflections, and layer exchange preserve each objective and act transitively on rails and on rungs. Uniqueness forces one common value on each edge orbit. Neither whole orbit can have zero weight, since removing every rail or every rung disconnects the network. Thus all optimal edges are strictly positive.

**2. Spectral reduction and scalar optimality.** Let rail and rung conductances be \(a>0\) and \(b>0\). The unit budget is \(m(2a+b)=1\). Tensor diagonalization by cycle Fourier modes and the two layer parities yields nonzero eigenvalues \(a\mu_k\) for \(1\le k<m\) and \(a\mu_k+2b\) for \(0\le k<m\). The classical exact cycle identities are
\[
\sum_{k=1}^{m-1}\mu_k^{-1}=S_{1,m},\qquad
\sum_{k=1}^{m-1}\mu_k^{-2}=S_{2,m}.
\]
Set \(t=b/a\), \(a=1/[m(2+t)]\). Then
\[
F_p(t)=m^p(2+t)^p\left(S_{p,m}+T_{p,m}(t)\right),\qquad
T_{p,m}(t)=\sum_{k=0}^{m-1}(\mu_k+2t)^{-p}.
\]
Differentiation gives the exact sign identity
\[
\operatorname{sgn} F'_p(t)=\operatorname{sgn}\left(S_{p,m}-R_{p,m}(t)\right),\qquad
R_{p,m}(t)=\sum_{k=0}^{m-1}\frac{4-\mu_k}{(\mu_k+2t)^{p+1}}.
\]
Every numerator is nonnegative and the term at \(k=0\) is strictly positive. Thus \(R_{p,m}\) decreases strictly from infinity to zero as \(t\) increases. It meets positive \(S_{p,m}\) exactly once, proving the root, optimum, and strict positivity in the theorem.

**3. Exact five-rung reversal.** For \(m=3\), at \(t=13/10\) direct rational evaluation gives
\[
R_{1,3}(13/10)-S_{1,3}=-\frac{2221}{198744}<0,\qquad
R_{2,3}(13/10)-S_{2,3}=\frac{3635081}{217028448}>0.
\]
By monotonicity, \(t_{1,3}<13/10<t_{2,3}\). For \(m=4\), \(R_{1,4}(1)=S_{1,4}=5/4\) and \(R_{2,4}(1)=S_{2,4}=9/16\), proving equality. For \(m\ge5\), use the exact ratio
\[
\frac{S_{2,m}}{S_{1,m}}=\frac{m^2+11}{60}.
\]
We claim \(t_{1,m}>30/(m^2+11)\). For \(m=5,6\), substitute the barrier into the first-moment root equation: the respective strictly positive differences \(R_{1,m}(30/(m^2+11))-S_{1,m}\) are
\[
\frac{646}{21025},\qquad \frac{3102126352}{3854592075}.
\]
For \(m\ge7\), the zero Fourier mode gives \(R_{1,m}(t)\ge t^{-2}\), hence \(t_{1,m}\ge\sqrt{12/(m^2-1)}\). The latter is at least \(30/(m^2+11)\) because \((m^2-49)(m^2-4)\ge0\); strictness follows from the strictly positive additional nonzero modes. Finally each spectral summand obeys
\[
\frac{4-\mu_k}{(\mu_k+2t)^{3}}\le
\frac{1}{2t}\frac{4-\mu_k}{(\mu_k+2t)^2},
\]
with strict inequality for some \(k>0\). At \(t=t_{1,m}\), therefore,
\[
R_{2,m}(t_{1,m})<\frac{R_{1,m}(t_{1,m})}{2t_{1,m}}
<\frac{m^2+11}{60}S_{1,m}=S_{2,m}.
\]
As \(R_{2,m}\) decreases, its unique root lies strictly below \(t_{1,m}\). This proves every integer case rather than extrapolating finite computations.

**4. Sharp fractional-power scales.** Define the cycle resolvent
\[
U_m(t)=\sum_{k=0}^{m-1}\frac1{\mu_k+2t}
=\frac{m}{2\sqrt{t(t+2)}}\coth\left(\frac m2\operatorname{arcosh}(1+t)\right).
\]
The identity follows from the Poisson kernel on the cycle, and is exact for every \(m\) and \(t>0\). Differentiation gives \(R_{1,m}=-(2+t)U'_m-U_m\) and \(R_{2,m}=(2+t)U''_m/4+U'_m/2\). For any fixed \(s>0\), at \(t=sm^{-2/3}\), the hyperbolic cotangent tends to one exponentially fast, uniformly for \(s\) in compact positive intervals, and
\[
R_{1,m}(sm^{-2/3})\sim \frac{m}{(2sm^{-2/3})^{3/2}}
=\frac{m^2}{(2s)^{3/2}}.
\]
Since \(S_{1,m}\sim m^2/12\), strict monotonicity and a two-sided \(s\)-bracketing argument force \((2s)^{3/2}=12\), or \(s=c_1=18^{1/3}\). Likewise, at \(t=sm^{-6/5}\),
\[
R_{2,m}(sm^{-6/5})\sim\frac{3m}{4(2sm^{-6/5})^{5/2}}=
\frac{3m^4}{4(2s)^{5/2}}.
\]
Using \(S_{2,m}\sim m^4/720\) forces \((2s)^{5/2}=540\), hence \(s=c_2=540^{2/5}/2\). The same monotone-bracketing method proves the asymptotic of the roots, not merely of trial weights.

**5. Minimum and cross-objective regret.** For \(t=sm^{-6/5}\) on fixed positive \(s\), differentiating the exact resolvent gives uniformly
\[
T_{2,m}(t)\sim\frac{m}{4(2t)^{3/2}}.
\]
Substitution in the exact objective yields
\[
F_2(sm^{-6/5})=\frac{m^6}{180}+m^{24/5}
\left(\frac{s}{180}+\frac1{(2s)^{3/2}}\right)+o(m^{24/5}).
\]
At \(s=c_2\), the coefficient equals \(c_2/108\), proving the optimal expansion. For the first-moment optimizer \(t_{1,m}\sim c_1m^{-2/3}\), the leading correction comes instead from expanding the prefactor \((2+t)^2\), and the transverse resolvent term contributes only \(O(m^4)\); thus
\[
F_2(L_{1,m}^*)=\frac{m^6}{180}+\frac{c_1}{180}m^{16/3}+o(m^{16/3}).
\]
Subtract the smaller second-order optimum correction of order \(m^{24/5}\), yielding the stated absolute and relative regret.

## Verification

Run the accompanying self-contained `verify.py` using Python 3, NumPy, SymPy, and mpmath. At packaging it passed `VERIFY_OK 475`, including exact rational Fourier/matrix identities on small graphs, high-precision cycle reciprocal-moment identities, exact sign certificates for the finite reversal, objective comparisons against all independently weighted Laplacian eigenvalues, bisection roots and ordering across many graph sizes, and large-size asymptotic checks through \(m=30000\). Finite tests supplement the analytic all-size arguments above; they do not by themselves certify an infinite-domain assertion.

## Relationship to prior work

Ghosh, Boyd and Saberi establish a convex first-inverse-spectral-moment conductance-design framework, but their inspected treatment does not optimize the squared-inverse moment on cyclic prisms. Patterson and Bamieh identify the squared-inverse moment as the second-order consensus coherence metric and analyze network dimension/coherence; their inspected paper does not give this edge-budget optimum. Cinkir derives resistances and Kirchhoff indices on fixed unweighted prisms, without optimizing individual conductances.

Two relevant published records, *Mesoscopic rung allocation in resistance-optimal prism networks* and *A two-thirds-power law for resistance-optimal rung investment in prism networks*, were inspected in full. They establish first-moment prism design, including the \(m^{-2/3}\) scaling which is used here for comparison. The new claims concern the **squared-inverse moment**, its \(m^{-6/5}\) optimizer, the exact five-rung reversal, and their quantitative cross-objective regret. Results for log-determinant design, spectral-gap mixing, and fixed unweighted prism spectra have different objectives and do not directly imply these conclusions.

## Limitations

The theorem assumes a cyclic prism of exactly two layers, equal positive edge prices, and Laplacian coherence objectives of order one or two. Different rung/rail prices, growing layer counts, other objectives, and network failures are not classified here. The exact solution requires a monotone scalar root rather than a radical expression for arbitrary \(m\). The infinite-size limits use fixed unit budget. Priority assessment rests on inspected available material; an undiscovered or unindexed equivalent result remains possible. Independent mathematical audit has not been performed.

## References

1. A. Ghosh, S. Boyd, and A. Saberi, *Minimizing Effective Resistance of a Graph*, MTNS 2006 (Kyoto); https://web.stanford.edu/~boyd/papers/pdf/eff_res_mtns06.pdf. The 2008 expanded SIAM Review paper is available at https://web.stanford.edu/~boyd/papers/pdf/eff_res.pdf.
2. S. Patterson and B. Bamieh, *Consensus and Coherence in Fractal Networks*, arXiv:1310.2592v1, first posted October 9, 2013; https://arxiv.org/abs/1310.2592 and full text https://arxiv.org/html/1310.2592v1.
3. Z. Cinkir, *Effective Resistances and Kirchhoff Index of Prism Graphs*, arXiv:1704.03429v1, first posted April 11, 2017; https://arxiv.org/html/1704.03429v1.
4. *Mesoscopic rung allocation in resistance-optimal prism networks*, published record, November 2, 2026; https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-mesoscopic-rung-allocation-in-resistance-optimal-prism-networks--58e191d42f66.
5. *A two-thirds-power law for resistance-optimal rung investment in prism networks*, published record, November 8, 2026; https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-two-thirds-power-law-for-resistance-optimal-rung-investment-in--9aa86612587c.
