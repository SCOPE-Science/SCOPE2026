# Reentrant finite-horizon investment in premium clique edges of complete split networks

## Finding

Fix integers \(p,q\ge2\). Let \(G=K_p\vee\overline{K_q}\) have all \(pq\) clique-to-independent-set edges priced at one per unit conductance and all \(p(p-1)/2\) clique-internal edges priced at \(r>1\). For every budget \(B>0\) and observation time \(t>0\), uniquely minimize

\[
H_t(w)=\operatorname{tr}\bigl(e^{-tL(w)}\bigr)
\]

subject to independent conductances \(w_e\ge0\) and \(\sum_{e\in E_{\rm cross}}w_e+r\sum_{e\in E_{\rm clique}}w_e=B\). The unique optimizer assigns a common cross-edge conductance \(a_t>0\) and a common clique-edge conductance \(b_t\ge0\). Put

\[
a_0=\frac{B}{pq},\qquad
R_{p,q}(t)=\frac{2pq}{p(q-1)e^{(q-p)a_0t}+(p+q)e^{-pa_0t}+q(p-1)}.
\]

**Exact support criterion:** every clique edge is funded (\(b_t>0\)) if and only if \(r<R_{p,q}(t)\). At equality all clique edges have zero conductance. If funded, \(b_t\) is the unique root, in \(\bigl(0,2B/[rp(p-1)]\bigr)\), of the explicit derivative equation in the proof, and \(a_t=(B-rp(p-1)b_t/2)/(pq)\).

The following gives the complete time-support phase diagram for **premium** clique edges (\(r>1\)):

* If \(q<p\), the function \(R_{p,q}\) increases strictly from one to \(2p/(p-1)\). Clique edges activate exactly once at a finite time if \(1<r<2p/(p-1)\); for \(r\ge2p/(p-1)\) they remain absent.
* If \(q=p\), the same statement holds with limiting threshold \(p/(p-1)\).
* If \(q\ge p+2\), then \(R_{p,q}(t)<1\) for all \(t>0\), so premium clique edges are never funded.
* If \(q=p+1\), there is a **reentrant investment window**. Define

\[
\tau_p=\frac pB\log\left(2+\frac1p\right),\quad
u_p=\left(2+\frac1p\right)^{1/(p+1)},\quad
r_p^*=\frac{2p(p+1)}{p(p+1)\nu_p+p^2-1}.
\]

Then \(r_p^*>1\), and for every \(1<r<r_p^*\) there are exactly two times \(0<T_-(r)<\tau_p<T_+(r)<\infty\) determined by \(R_{p,p+1}(T_\pm)=r\). All clique edges are uniquely optimal **only for the intermediate interval** \(T_-(r)<t<T_+(r)\); they are optimally deleted at both smaller and larger times, including the two transition times. For \(r\ge r_p^*\) they are deleted for all finite times. The strict price window persists for each \(p\ge2\), with the sharp size law

\[
\lim_{p\to\infty}p(r_p^*-1)=\frac{1-\log2}{2}>0.
\]

For the smallest example \(p=2,q=3,B=1,r=26/25\), the two transition times are approximately \(0.5622300103\) and \(3.1987079650\). These decimal values illustrate the exact implicit characterization; they are not defining data or an exhaustive certificate.

## Assumptions and scope

The graph is simple and undirected. The weighted combinatorial Laplacian is \(L(w)=\sum_{\{i,j\}\in E}w_{ij}(e_i-e_j)(e_i-e_j)^\top\), without vertex masses or self-loops. Conductances are symmetric but otherwise free nonnegative variables, not constrained a priori to be equal within price classes; disconnected feasible designs are allowed. The objective is a finite-time *heat trace*, not the limiting spectral gap, normalized Markov-chain SLEM, or a heat-kernel entry. The theorem classifies support for \(r>1\); no claim about the full support diagram for cheaper clique edges \(0<r<1\) is made.

## Proof

**Strict convexity and global symmetry.** For every fixed \(t>0\), \(F(L)=\operatorname{tr}(e^{-tL})\) is strictly convex in real symmetric \(L\). More precisely, in any nonzero symmetric direction \(X\), its second derivative is

\[
\frac{d^2}{ds^2}F(L+sX)\bigg|_{s=0}
=t^2\int_0^1\operatorname{tr}\left(e^{-(1-u)tL}Xe^{-utL}X\right)\,du>0.
\]

The integrand is a strictly positive squared Frobenius norm after inserting matrix square roots. The map from edge conductances to \(L\) is injective because every off-diagonal edge entry is minus that edge's conductance. Consequently the heat trace is strictly convex in all edge conductances, including on the closed nonnegative simplex. Existence follows from compactness. Full budget use follows from strict decrease of the trace under positive uniform scaling of any nonzero Laplacian. The unique minimizer must be fixed by every permutation of the clique vertices and every permutation of the independent vertices, which preserve both budget and objective. Hence it has common rates \(a,b\) on the two classes.

**Exact spectral reduction.** The class-symmetric Laplacian has eigenvalues, including multiplicities,

\[
0\ (1),\qquad pa\ (q-1),\qquad (p+q)a\ (1),\qquad qa+pb\ (p-1).
\]

These arise respectively from the constant vector, independent-set sum-zero vectors, the two-block quotient, and clique sum-zero vectors. Writing \(m=p(p-1)/2\), budget equality gives \(a=(B-rmb)/(pq)\) with \(0\le b\le B/(rm)\), and thus

\[
h(b)=1+(q-1)e^{-pat}+e^{-(p+q)at}+(p-1)e^{-(qa+pb)t}.
\]

Put \(c=r(p-1)/(2q)>0\). Since \(da/db=-c\), direct differentiation yields

\[
\frac{h'(b)}t=
cp(q-1)e^{-pat}+c(p+q)e^{-(p+q)at}
+(p-1)(qc-p)e^{-(qa+pb)t}.
\]

Furthermore \(h''(b)>0\) throughout its interval, because the two terms proportional to \(c^2p^2(q-1)\) and \(c^2(p+q)^2\) already give strictly positive contributions. At the upper endpoint \(a=0\),

\[
\frac{h'(B/(rm))}{t(p-1)}
=\frac{r(p+1)}2-\left(p-\frac{r(p-1)}2\right)
 e^{-pBt/(rm)}>0
\]

for every \(r>1\): if the parenthesized quantity is nonnegative, replace its exponential by one to obtain the lower bound \(p(r-1)>0\); otherwise both displayed terms are positive. Thus all crossing edges are positive at the unique optimum. Substituting \(b=0,a=a_0\) gives

\[
\frac{h'(0)}{t(p-1)}=
\frac{r}{2q}\bigl[p(q-1)e^{-pa_0t}+(p+q)e^{-(p+q)a_0t}+q(p-1)e^{-qa_0t}\bigr]
-p e^{-qa_0t}.
\]

This is nonnegative exactly when \(r\ge R_{p,q}(t)\). Strict convexity and positivity of the upper-endpoint derivative now prove the exact support criterion, including equality and uniqueness.

**All time regimes.** Let \(g(t)=2pq/R_{p,q}(t)\). Differentiating twice shows

\[
\frac{g'(t)}{a_0}
=p(q-1)(q-p)e^{(q-p)a_0t}-p(p+q)e^{-pa_0t},
\]

\[
\frac{g''(t)}{a_0^2}
=p(q-1)(q-p)^2e^{(q-p)a_0t}+p^2(p+q)e^{-pa_0t}>0.
\]

At time zero, \(g(0)=2pq\) and \(g'(0)=a_0pq(q-p-2)\). When \(q\le p\), \(g'\) is everywhere negative, so \(R\) increases strictly from one. Its limiting denominator is \(q(p-1)\) for \(q<p\), and \(2p(p-1)\) for \(q=p\), yielding the stated ceiling prices. When \(q\ge p+2\), strict convexity of \(g\) and \(g'(0)\ge0\) give \(g(t)>g(0)\), hence \(R(t)<1\).

For \(q=p+1\), \(g'(0)<0\), \(g''>0\), and \(g'(t)\to\infty\). Therefore \(g\) has a unique positive minimum (equivalently \(R\) a unique maximum). Solving \(g'(t)=0\) gives \(\tau_p=pB^{-1}\log((2p+1)/p)\). Writing \(\nu_p=e^{a_0\tau_p}\), the derivative relation reduces the two exponential terms of \(g(\tau_p)\) to \(p(p+1)\nu_p\). Hence its maximum is exactly \(r_p^*\) as stated. Since \(g'(0)<0\), \(r_p^*>1\); since \(g(t)\to\infty\), the level equation \(R(t)=r\) has exactly two positive roots precisely for \(1<r<r_p^*\). The support criterion supplies the full three-stage conclusion. Finally,

\[
\nu_p=1+\frac{\log2}{p}+O(p^{-2}),\qquad
r_p^*=1+\frac{1-\log2}{2p}+O(p^{-2}),
\]

which proves the window-width limit.

## Verification

Run `python3 verify.py` from the same directory. It uses only the Python 3 standard library. The checker constructs exact rational Laplacians and verifies their action on a complete eigenbasis for multiple sizes and conductances, compares the exact reduced heat trace and derivatives with independent finite evaluations, verifies the two-transition phase numerically for fifty graph sizes, checks strict sample optimality against class-symmetric allocations, and reproduces the stated five-vertex transition times. It reports 10,812 finite checks. The proof above, not sampling, establishes unrestricted global optimality and every infinite-family quantifier.

## Relationship to prior work

Sun, Boyd, Xiao and Diaconis (2006) develop linear-budget optimization of the continuous-time Laplacian **spectral gap**, not the finite-time exponential trace. Boyd (2006) presents the broader convex spectral optimization perspective. A separately published exact spectral-gap result on the same complete split graph determines the optimal asymptotic rate for every \(p,q\); in particular, when \(q\ge p\), a design without clique edges always attains maximum algebraic connectivity. That result does **not** imply the present claim: when \(q=p+1\), the heat-trace optimizer funds premium clique edges at an intermediate time, despite the existence of a zero-clique spectral-gap optimizer. The result here does not reassert spectral-gap formulas as new; it supplies an independently derived full-spectrum, finite-time support theorem and identifies its exceptional reentrant regime.

## Limitations

The theorem is for uniform prices on each of two edge orbits; arbitrary heterogeneous edge prices, different vertex masses, signed conductances, infinite graphs and time-integrated objectives are excluded. The classification assumes \(r>1\) and does not cover all cheaper-price cases. Individual switching times outside the five-vertex illustration are given by unique roots rather than elementary closed forms. Numerical checks corroborate but cannot certify the all-size proof. Novelty is qualified by possible unindexed equivalent work, and independent mathematical audit has not been performed.

## References

1. J. Sun, S. Boyd, L. Xiao and P. Diaconis, “The Fastest Mixing Markov Process on a Graph and a Connection to a Maximum Variance Unfolding Problem,” *SIAM Review* 48(4), 681–699 (2006), https://doi.org/10.1137/S0036144504443821; full text https://web.stanford.edu/~boyd/papers/pdf/fmmp.pdf; first online 2006-11-02.
2. S. Boyd, “Convex Optimization of Graph Laplacian Eigenvalues,” *Proceedings of the International Congress of Mathematicians*, vol. 3, 1311–1319 (2006), https://www-leland.stanford.edu/~boyd/papers/pdf/cvx_opt_graph_lapl_eigs.pdf.
3. “A sharp price transition for continuous-time fastest mixing on complete split graphs,” openly available mathematical result, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-a-sharp-price-transition-for-continuous-time-fastest-mixing-on-c--7cfd411fbd51/RESULT.md (accessed 2026-11-18).
