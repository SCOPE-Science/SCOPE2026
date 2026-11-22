# Unique worst positivity delay for mixed heat on complete multipartite graphs

## Finding
Let \(G=K_{s_1,\ldots,s_r}\), \(r\ge2\), be any **unweighted** complete multipartite graph with integer part sizes \(s_i\ge1\), total order \(N=\sum_i s_i\), and combinatorial Laplacian \(L\). For each mixing strength \(\eta>0\), consider the real symmetric, constant-preserving semigroup
\[
S_\eta(t)=\exp[-t(L+\eta L^2)],\qquad t\ge0.
\]
If every part is a singleton, \(S_\eta(t)\) is entrywise nonnegative at every \(t\ge0\). Otherwise let \(m=\max_i s_i\ge2\), \(p=m/N\in(0,1)\), and \(q=1-p\). Introduce, for \(x>0\),
\[
F_p(x)=\frac1x\int_0^x\frac{e^u-1}{1+p(e^u-1)}\,du,
\qquad \kappa=\frac{N\eta}{1+N\eta}\in(0,1).
\]
There is a unique \(x_p(\kappa)>0\) such that \(F_p(x_p(\kappa))=\kappa\). The **complete positivity-time set** is
\[
\boxed{\{t\ge0:S_\eta(t)\text{ is entrywise nonnegative}\}
=\{0\}\cup[T_G(\eta),\infty),\qquad
T_G(\eta)=\frac{1-\kappa}{N}x_p(\kappa).}
\]
For \(0<t<T_G(\eta)\), every off-diagonal entry joining distinct vertices within a largest part is negative. At the recovery time such entries are zero, and all other existing entries are nonnegative; every entry is strictly positive after recovery.

The map \(\eta\mapsto T_G(\eta)\) has **exactly one global maximizer** on \((0,\infty)\). With
\[
x_*=\log\frac{2-p}{1-p},\qquad
\kappa_*=F_p(x_*),\qquad
\eta_* =\frac{\kappa_*}{N(1-\kappa_*)},
\]
one has
\[
\boxed{T_G(\eta_*)=\frac1N\left[
\frac{2-p}{1-p}\log(2-p)
+\frac{1-p}{p}\log(1-p)\right].}
\]
The last expression is strictly increasing in \(m\) for fixed \(N\). Indeed, for **each** fixed \(\eta>0\) the entire recovery time depends only on \(N\) and the largest part size \(m\), and increases strictly with \(m\). Consequently, for fixed \(N\ge4\), among all connected noncomplete unweighted complete multipartite graphs, a clique with one deleted edge (parts \(2,1,\ldots,1\)) has the smallest recovery time at each \(\eta\) and the smallest maximal delay, whereas the star (parts \(N-1,1\)) has the largest. For \(N=3\), both extreme descriptions represent the same graph.

For each fixed noncomplete graph,
\[
T_G(\eta)\sim 2\eta\quad(\eta\downarrow0),\qquad
T_G(\eta)\sim\frac{x_p(1)}{N^2\eta}\quad(\eta\to\infty).
\]
After optimizing over \(\eta\), the large-order graph-shape contrast is finite:
\[
\lim_{N\to\infty}N\max_{\eta>0}T_{K_{2,1,\ldots,1}}(\eta)=2\log2-1,
\qquad
\lim_{N\to\infty}N\max_{\eta>0}T_{K_{N-1,1}}(\eta)=1.
\]
The ratio of the largest to the smallest optimized delay therefore tends to \(1/(2\log2-1)\), rather than diverging with graph size.

## Assumptions and scope
The vertex measure is counting measure, edges between different parts have conductance one, and there are no edges within a part. The Laplacian is \(L=D-A\), not its normalized counterpart. The positivity order is the standard coordinatewise order on real vertex signals; hence a matrix is positive precisely when all its entries are nonnegative. Only the mixed generator \(-L-\eta L^2\), with \(\eta>0\), is included. At \(t=0\), the matrix is the identity (nonnegative but not strictly positive). All graph-shape comparisons hold at fixed total order \(N\). No graph-uniform statement over arbitrary weighted or nonmultipartite graphs is claimed.

## Proof
**1. Spectral projectors and transition entries.** Let \(J\) denote the all-ones \(N\)-by-\(N\) matrix, \(J_i\) the all-ones block supported on part \(i\), and \(I_i\) the identity block there. The orthogonal projectors onto constants, partwise constants of zero global sum, and within-part mean-zero subspaces are
\[
P_0=J/N,\quad P_N=\sum_i J_i/s_i-J/N,\quad P_i=I_i-J_i/s_i.
\]
The corresponding Laplacian eigenvalues are respectively \(0\), \(N\), and \(N-s_i\), so, with \(a=N(1+N\eta)\) and \(b_s=(N-s)(1+(N-s)\eta)\),
\[
S_\eta(t)=P_0+e^{-at}P_N+\sum_i e^{-b_{s_i}t}P_i.
\]
For two distinct vertices in different parts the entry is \((1-e^{-at})/N>0\) for \(t>0\). For two distinct vertices in the same part of size \(s\), it equals
\[
w_s(t)=\frac1s\left[\frac{s}{N}+\frac{N-s}{N}e^{-at}-e^{-b_st}\right].
\]
A diagonal entry in such a part is
\[
d_s(t)=\frac1N+\frac{N-s}{sN}e^{-at}
+\left(1-\frac1s\right)e^{-b_st}>0.
\]
For singleton parts, there are no distinct within-part pairs. These formulas account for every matrix entry, without any qualitative semigroup approximation.

**2. Reduction to a strictly monotone scalar average.** Put \(p=s/N\), \(q=1-p\), \(\beta=N\eta\), \(\kappa=\beta/(1+\beta)\), and \(x=at\). Then \(b_s/a=q(1-\kappa p)\) and
\[
sw_s(t)=p+q e^{-x}-e^{-q(1-\kappa p)x}.
\]
For \(x>0\), taking logarithms shows that \(w_s(t)\) has the sign of \(F_p(x)-\kappa\), where
\[
\begin{aligned}
F_p(x)&=\frac1p\left[1+
\frac{\log(p+q e^{-x})}{qx}\right]\\
&=\frac1x\int_0^x g_p(u)\,du,\qquad
 g_p(u)=\frac{e^u-1}{1+p(e^u-1)}.
\end{aligned}
\]
(The sign identity follows by comparing the logarithms of the two positive terms, remembering that \(\log\) is increasing.) For fixed \(p\in(0,1)\), \(g_p\) is strictly increasing from \(0\) to \(1/p>1\). Consequently \(F_p\) is continuous and strictly increasing from \(0\) to \(1/p\); since \(0<\kappa<1\), the equation \(F_p(x)=\kappa\) has exactly one positive solution. Each nonsingleton part thus starts with negative off-diagonal entries, crosses zero once, and thereafter has positive off-diagonal entries. Together with step 1, this proves its full positivity-time classification.

**3. Largest-part dominance and graph-shape comparison.** For every \(u>0\), \(g_p(u)\) decreases strictly as \(p\) increases. Hence \(F_p(x)\) decreases strictly in \(p\) for each fixed \(x>0\). Its inverse level \(x_p(\kappa)\) therefore increases strictly in \(p\). At fixed \(N\) and \(\eta\), the largest part has the last nonedge sign recovery, proving the exact formula and graph ordering. The smallest possible largest-part size for a noncomplete graph is two, achieved by parts \((2,1,\ldots,1)\); the largest is \(N-1\), achieved by a star. This proves both fixed-parameter extremal graph statements and the corresponding extremal ordering after taking the supremum over \(\eta\).

**4. A unique optimizer with an explicit closed value.** Since \(\kappa=F_p(x)\) increases strictly from zero to one as \(x\) increases from zero to \(x_p(1)\), maximizing \(T_G(\eta)\) over \(\eta>0\) is equivalent to maximizing
\[
N T=x(1-F_p(x))=x-\int_0^x g_p(u)\,du,
\qquad 0<x<x_p(1).
\]
The derivative is \(1-g_p(x)\). Because \(g_p\) is strictly increasing, it equals one at exactly
\[
x_*=\log\bigl(1+1/(1-p)\bigr).
\]
At this point \(F_p(x_*)<g_p(x_*)=1\), so the critical point lies in the permitted interval. The derivative is positive before and negative after this point, establishing a strict unique *global* maximum. At \(x_*\), the identity \(p+(1-p)e^{-x_*}=1/(2-p)\) and the integral representation yield
\[
x_* -\int_0^{x_*}g_p(u)\,du
=\frac{2-p}{1-p}\log(2-p)+\frac{1-p}{p}\log(1-p).
\]
This is the claimed exact maximum, while \(\kappa_*=F_p(x_*)\) and \(\eta_*=\kappa_*/[N(1-\kappa_*)]\) specify the unique coupling strength.

**5. Limiting couplings and graph sizes.** As \(x\downarrow0\), \(g_p(x)=x+O_p(x^2)\), hence \(F_p(x)=x/2+O_p(x^2)\). Since \(\kappa=N\eta+O_N(\eta^2)\), it follows that \(T_G(\eta)\sim 2\eta\). As \(\eta\to\infty\), \(\kappa\to1\) and \(x_p(\kappa)\to x_p(1)\), giving \(\eta T_G(\eta)\to x_p(1)/N^2\). Finally let \(p\to0\) or \(p\to1\) in the exact maximized-delay expression. For \(p\to0\), \((1-p)\log(1-p)/p\to-1\), while the first summand tends to \(2\log2\). For \(p\to1\), the first summand tends to one and the second to zero. Taking \(p=2/N\) and \(p=(N-1)/N\), respectively, proves the two graph-family limits and their finite ratio.

## Verification
The standalone `artifacts/verify_mixed_multipartite.py` independently constructs complete multipartite adjacency and combinatorial Laplacian matrices, computes \(L^2\) through multiplication, and exponentiates \(-t(L+\eta L^2)\) by scaled Taylor series and matrix squaring, without relying on the spectral projector formula. It checks all transition entries against that formula, row sums, signs before/after the analytically defined recovery threshold, the closed optimized-delay identity, strict discrete graph-shape ordering, and both coupling limits. The executed program returned `VERIFY_OK matrix-entry-comparisons=19560 parameter-checks=1152 limit-tests=16`. These finite numerical checks test implementation and arithmetic; the universal quantifiers, unique roots, and strict optimization are proved in steps 1–5 above.

## Relationship to prior work
Daners, Glück and Kennedy's 2015 preprints [1,2] establish structural spectral criteria for eventual positivity of operator semigroups, including finite-dimensional cases, but not this graph-family positivity-time classification or coupling optimizer. Gregorio and Mugnolo [3] prove qualitative eventual positivity for discrete bi-Laplacians on connected finite graphs, and treat the pure \(-L^2\) generator rather than optimizing the mixed \(-L-\eta L^2\) generator. The published complete-multipartite squared-Laplacian cutoff [4] is recovered here only in the singular large-\(\eta\) limit; its largest-part ordering does not by itself imply the all-coupling ordering or finite unique optimizing \(\eta\). A published universal scalar-filter criterion [5] provides the underlying multipartite spectral entry formula, but does not establish the present mixed-exponential sign geometry, the scalar-integral monotonicity, the unique coupling optimum, or the shape-ratio limit. An earlier exact mixed-heat star calculation gives the largest-part extreme only; no new priority is claimed for the star specialization. Likewise, an existing small-\(\eta\) diameter-two graph expansion covers a perturbative portion of the present family, not its global all-coupling optimization.

## Limitations
This is not a theorem for arbitrary nonmultipartite graphs, directed edges, conductance-weighted multipartite graphs, normalized graph Laplacians, or arbitrary spectral mixtures. It does not assert a universal coupling maximizer across different graph orders. The singular \(\eta\to\infty\) root generally has no elementary closed form. An older unindexed exact matrix-exponential calculation or a stronger spectral-filter theorem could predate the presently identified comparisons; historical priority is not independently certified. No numerical experiment replaces any infinite proof.

## References
[1] D. Daners, J. Glück and J. B. Kennedy, *Eventually and asymptotically positive semigroups on Banach lattices*, arXiv:1511.05294, first submitted 2015-11-17, https://arxiv.org/abs/1511.05294 .

[2] D. Daners, J. Glück and J. B. Kennedy, *Eventually Positive Semigroups of Linear Operators*, arXiv:1511.09020, first submitted 2015-11-29, https://arxiv.org/abs/1511.09020 .

[3] F. Gregorio and D. Mugnolo, *Bi-Laplacians on graphs and networks*, arXiv:1712.07370, first submitted 2017-12-20, https://arxiv.org/abs/1712.07370 .

[4] *Sharp positivity cutoff for squared-Laplacian heat on every complete multipartite graph*, public mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-sharp-positivity-cutoff-for-squared-laplacian-heat-on-every-comp--e4f9c89a420f .

[5] *An exact positivity criterion on complete multipartite diffusion graphs*, public mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-an-exact-positivity-criterion-on-complete-multipartite-diffusion--690509e7de2b .

