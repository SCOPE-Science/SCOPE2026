# Opposite spectral-order spine transitions and a unique allocation peak on triangular book networks

## Finding

Let \(m\ge2\) and let the triangular book \(B_m=K_2\vee\overline{K_m}\) have two hubs, \(m\) independent page vertices, and the direct hub-to-hub *spine*. Each of the \(2m\) spoke edges has unit price per unit conductance; the spine has price \(c>0\). All \(2m+1\) conductances are independently variable and nonnegative, under a total budget \(B>0\). For a connected weighted Laplacian \(L\) with nonzero eigenvalues \(\lambda_2,\ldots,\lambda_{m+2}\), minimize
\[
\Phi_p(L)=\sum_{j=2}^{m+2}\lambda_j^{-p}\quad(p>0),
\qquad
\Phi_0(L)=-\sum_{j=2}^{m+2}\log\lambda_j.
\]
Disconnected designs have infinite objective. The zero-order objective is negative log pseudodeterminant, not the constant zeroth spectral moment.

**Exact unrestricted optimum.** For every real \(p\ge0\), the globally unique minimizer has one positive spoke conductance \(x\) on every spoke and a common spine conductance \(y\ge0\). Put
\[
 A_{m,p}=(m-1)2^{-p}+(m+2)^{-p},\qquad
 c_{m,p}=\frac{4}{1+(m-1)(m/2)^p+(m/(m+2))^p}.
\]
The spine is present if and only if \(0<c<c_{m,p}\). More precisely, defining \(t=y/x\),
\[
 t=\begin{cases}
 \displaystyle\frac12\left[\left(\frac{m(4-c)}{cA_{m,p}}\right)^{1/(p+1)}-m\right],&0<c<c_{m,p},\\[3mm]
 0,&c\ge c_{m,p},
 \end{cases}
 \qquad
 x=\frac{B}{2m+ct},\quad y=\frac{Bt}{2m+ct}.
\]
Equality at the critical price belongs to spine deletion. Every spoke remains positive.

**Page-number reversal in spectral order.** For two pages,
\[
 c_{2,p}=\frac4{2+2^{-p}}
\]
is strictly increasing from \(4/3\) at \(p=0\) toward \(2\) as \(p\to\infty\). In particular, if \(4/3<c<2\), there is an *activation* order
\[
 p_c=-\log_2(4/c-2)>0,
\]
and the spine is absent for \(0\le p\le p_c\), present for every \(p>p_c\). Conversely, for **every** \(m\ge3\), \(c_{m,p}\) strictly decreases from \(4/(m+1)\) toward zero. For \(0<c<4/(m+1)\), the spine is present for \(0\le p<p_c\) and deleted for \(p\ge p_c\), where \(p_c>0\) is the unique solution \(c=c_{m,p_c}\). At greater prices it is deleted for every order.

**Unique spending peak on the two-page book.** Define
\[
 c_\star=\frac4{1+2^{3/2}}.
\]
For \(0<c\le c_\star\), the optimal spine ratio \(t\) strictly decreases with \(p>0\). For \(c_\star<c<2\), \(t\) has exactly one maximizer \(p_{\mathrm{peak}}>0\) as \(p\) ranges over nonnegative real orders. This is also the unique maximum of the spine's budget share \(cy/B\). It is characterized by
\[
 \frac{(p_{\mathrm{peak}}+1)\log2}{1+2^{p_{\mathrm{peak}}}}
 +\log(1+2^{-p_{\mathrm{peak}}})
 =\log\left(\frac{4-c}{c}\right).
\]
For \(4/3<c<2\), this peak lies strictly after activation: \(p_{\mathrm{peak}}>p_c\). Despite remaining active at every sufficiently large finite order, the spine ratio then decays as
\[
 t\sim\frac{\log((4-c)/c)}{p+1}\quad(p\to\infty),\qquad 0<c<2.
\]
For \(c\ge2\) the optimal spine is absent at every finite order. At fixed \(p\ge0\), the multi-page critical price satisfies
\[
 c_{m,p}\sim\frac{2^{p+2}}{m^{p+1}}\quad(m\to\infty).
\]

For a concrete pair of opposite changes, \(m=2,c=8/5\) is absent through order \(p=1\) and active above it; \(m=3,c=9/10\) is active at determinant order and already absent at first-order coherence. These transitions occur under fully independent, unrestricted edge optimization.

## Assumptions and scope

All graphs are finite, undirected, simple, and connected before conductance allocation. The budget is an equality, \(\sum_{e\ne uv}w_e+c w_{uv}=B\), with strictly positive \(B,c\). All individual weights may vary independently and may be zero. The spectral moment objective uses the combinatorial, not normalized, Laplacian. It is defined only on connected weighted support, extended by \(+\infty\) at disconnection. The exact theorem quantifies every integer \(m\ge2\), every real \(p\ge0\), and all positive \(B,c\). At \(p=0\) the normalized limit of the positive-order objective, after subtracting its constant term and dividing by \(p\), yields the stated log-determinant objective.

## Proof

**1. Existence, strict convexity and symmetry without a symmetry assumption.** Restrict the weighted Laplacian to the fixed \((m+1)\)-dimensional space \(\mathbf1^\perp\), obtaining \(M(w)\succ0\) exactly for connected positive-weight support. On positive definite matrices, \(f_p(s)=s^{-p}\) for \(p>0\) and \(f_0(s)=-\log s\) are strictly convex scalar functions. In an eigenbasis of a positive definite \(M\), the second directional derivative of \(\operatorname{tr} f_p(M+sH)\) at zero is
\[
 \sum_{i,j}\frac{f_p'(\lambda_i)-f_p'(\lambda_j)}{\lambda_i-\lambda_j}|H_{ij}|^2,
\]
with divided differences replaced by \(f_p''(\lambda_i)>0\) at coinciding eigenvalues. Every coefficient is strictly positive because \(f_p'\) is strictly increasing. The linear edge-weight-to-Laplacian map is injective for a simple graph: distinct edge weights appear separately as negative off-diagonal Laplacian entries. Restriction to \(\mathbf1^\perp\) preserves this injectivity, since all Laplacians annihilate \(\mathbf1\). Therefore the spectral objective is strictly convex in all individual conductances on its connected domain.

The budget simplex is compact, contains connected designs, and approaching disconnected designs drives a nonzero eigenvalue to zero, hence the objective to infinity. A unique connected minimizer exists. Hub exchange and arbitrary permutations of pages preserve prices and objective. Uniqueness forces a common \(x>0\) on every spoke and a single \(y\ge0\) on the spine. The positive spoke weight is necessary for connectedness in this symmetric family. No symmetry restriction was placed on the original optimization.

**2. Full nonzero spectrum.** For the symmetry-forced weights, the page-zero-sum subspace gives eigenvalue \(2x\) with multiplicity \(m-1\); the mode with the two hubs equal and all pages equal (orthogonal to constants) gives \((m+2)x\); the hub-antisymmetric mode gives \(mx+2y\). Thus
\[
 \sigma(L)\setminus\{0\}=\{2x\ (m-1\text{ times}),\ (m+2)x,\ mx+2y\}.
\]
The budget is \(2mx+cy=B\). With \(t=y/x\ge0\), one obtains \(x=B/(2m+ct)\) and for \(p>0\)
\[
 \Phi_p(t)=B^{-p}(2m+ct)^p
 \left[A_{m,p}+(m+2t)^{-p}\right].
\]

**3. Sharp global support rule and explicit allocation.** For \(p>0\), the derivative has the sign of
\[
 cA_{m,p}+m(c-4)(m+2t)^{-(p+1)}.
\]
When \(c\ge4\), this is positive. If \(0<c<4\), it is strictly increasing in \(t\), crossing zero at most once; moreover \(\Phi_p(t)\to\infty\) as \(t\to\infty\). Its value at zero is negative exactly when
\[
 c\left[1+m^p A_{m,p}\right]<4,
\]
which is \(c<c_{m,p}\). Solving for the unique positive root yields the displayed \(t\). Otherwise the optimum is \(t=0\), including equality.

For \(p=0\), direct multiplication of the eigenvalues gives
\[
 \Phi_0(t)=(m+1)\log(2m+ct)-\log(m+2t)
 -(m-1)\log2-\log(m+2)-(m+1)\log B.
\]
Its derivative vanishes, when positive, precisely at
\[
 t=\frac{4-c(m+1)}{2c}.
\]
The boundary cutoff is \(c_{m,0}=4/(m+1)\). This agrees exactly with the \(p\downarrow0\) limit of the positive-order formula.

**4. Opposite changes in page count.** For \(m=2\), the denominator in \(c_{m,p}\) equals \(2+2^{-p}\), strictly decreasing in \(p\); hence the price threshold increases and the activation formula follows by solving \(c=c_{2,p}\). For \(m\ge3\), differentiate the denominator \(D_m(p)\). Its derivative is
\[
 (m-1)(m/2)^p\log(m/2)
 +(m/(m+2))^p\log(m/(m+2)).
\]
Since \(m\ge3\) and \(p\ge0\), it is bounded below by
\[
 2\log(3/2)+\log(3/5)=\log(27/20)>0.
\]
The denominator tends to infinity for \(m\ge3\), so its reciprocal falls from \(4/(m+1)\) to zero. The stated active/deleted intervals follow. Dividing the denominator by \(m^{p+1}/2^p\) also proves \(c_{m,p}\sim2^{p+2}m^{-(p+1)}\).

**5. One and only one two-page spending peak.** For \(m=2\) and any active order with \(c<2\), the explicit ratio becomes
\[
 1+t=\exp\left(\frac{g(p)}{p+1}\right),
 \qquad g(p)=\log\frac{4-c}{c}-\log(1+2^{-p}).
\]
The sign of its derivative is the sign of \(N(p)=(p+1)g'(p)-g(p)\). Here
\[
 g'(p)=\frac{\log2}{1+2^p}>0,
 \qquad
 g''(p)=-\frac{(\log2)^2 2^p}{(1+2^p)^2}<0,
 \qquad N'(p)=(p+1)g''(p)<0.
\]
Furthermore \(N(0)=\tfrac32\log2-\log((4-c)/c)\) and \(N(p)\to-\log((4-c)/c)<0\) as \(p\to\infty\) for \(c<2\). Consequently \(N(0)\le0\) exactly when \(c\le c_\star\), yielding monotone decline; otherwise there is exactly one positive zero of \(N\), giving exactly one peak. If the spine begins inactive, then at activation \(g(p_c)=0\) and \(N(p_c)=(p_c+1)g'(p_c)>0\), so the peak necessarily follows activation. The expenditure fraction \(ct/(4+ct)\) increases strictly with \(t\), sharing the same peak. Finally, \(g(p)\to\log((4-c)/c)\) implies the high-order \(1/(p+1)\) asymptotic for \(t\). This concludes all cases.

## Verification

The standalone source `verify_book_moments.py` uses NumPy and SciPy and can be run via `python verify_book_moments.py`. It constructs every Laplacian directly from its individual edges rather than using the reduced spectral formula. On the current packaged source it passed **13,679 independent finite assertions**, including complete eigenvalue cross-checks over multiple page counts, scalar minimization comparisons for real orders and prices, thousands of unrestricted asymmetric feasible competitors, support-threshold comparisons, two-page peak and activation checks, and high-order/large-page asymptotic diagnostics. These computations are finite checks only. The universal claims and uniqueness are established by the analytical proof above.

## Relationship to prior work

Ghosh, Boyd and Saberi (2006/2008) establish convex effective-resistance design and graph symmetry methods; their displayed analytic graph families do not include the present continuous-order book rule. Patterson and Bamieh (arXiv:1310.2592, 2013) establish the first- and second-order noisy-consensus spectral objectives but do not optimize priced book conductances. Two directly relevant previously published book results supply **known endpoint special cases**: *Four exact support regimes for price-constrained D-optimal conductance on book networks* gives \(c_{m,0}=4/(m+1)\) for \(m\ge3\), and *Quadratic page-count threshold for retaining a shortcut in optimal-resistance book networks* gives \(c_{m,1}=8(m+2)/(m^3+m^2+2m+4)\) for \(m\ge2\). Neither endpoint theorem states the opposite dependence on spectral order for two pages versus three or more, the unique two-page interior spending peak, or the continuous all-order allocation formula. The present result claims those continuous-order classifications, **not** the known individual endpoint values or general convexity method.

## Limitations

All spoke edges share one price, the single spine edge has another, and costs are linear. The result does not handle page-specific prices, nonidentical page topology, nonlinear cost, directed or normalized-Laplacian models, nor arbitrary other spectral functionals. At \(p=0\), the objective is negative log pseudodeterminant, specified separately. Published equivalences outside the inspected sources may exist; the novelty comparison is evidence-based and does not certify publication priority. Finite verifier outputs are not proofs for all real parameters, and no external independent mathematical validation is asserted.

## References

1. A. Ghosh, S. Boyd and A. Saberi, *Minimizing Effective Resistance of a Graph*, SIAM Review 50 (2008), 37–66, DOI: 10.1137/050645452. Earlier conference version: MTNS 2006. https://web.stanford.edu/~boyd/papers/pdf/eff_res.pdf
2. S. Patterson and B. Bamieh, *Consensus and Coherence in Fractal Networks*, arXiv:1310.2592, first posted 2013-10-09. https://arxiv.org/pdf/1310.2592
3. *Four exact support regimes for price-constrained D-optimal conductance on book networks*, published research record, 2026-11-02, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-four-exact-support-regimes-for-price-constrained-d-optimal-condu--6bfa0d131382
4. *Quadratic page-count threshold for retaining a shortcut in optimal-resistance book networks*, published research record, 2026-11-02, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-quadratic-page-count-threshold-for-retaining-a-shortcut-in-optim--51c2db896f59
