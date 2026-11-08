# Exact second-cumulant matrix for the shortest cycles of a two-parent recursive DAG

## Finding

Write \(C_2(n)\) for the number of pairs of parallel edges and \(C_3(n)\) for the number of edge-labeled three-cycles in the two-parent uniform-attachment recursive multigraph on vertices \(1,\ldots,n\). Set \(H_m^{(r)}=\sum_{j=1}^m j^{-r}\), \(H_m=H_m^{(1)}\), and \(S_m=\sum_{t=2}^m H_{t-1}/t^2\), interpreting empty sums as zero. For every integer \(n\ge2\), the means and complete covariance matrix are exactly

\[
\begin{aligned}
\mathbb E C_2(n)&=H_{n-1},\\
\operatorname{Var}C_2(n)&=H_{n-1}-H_{n-1}^{(2)},\\
\mathbb E C_3(n)&=4\bigl(H_{n-1}-H_{n-1}^{(2)}\bigr),\\
\operatorname{Var}C_3(n)&=\mathbb E C_3(n)+4S_{n-1}
 -16\bigl(H_{n-1}^{(2)}-2H_{n-1}^{(3)}+H_{n-1}^{(4)}\bigr),\\
\operatorname{Cov}(C_2(n),C_3(n))&=-4\bigl(H_{n-1}^{(2)}-H_{n-1}^{(3)}\bigr).
\end{aligned}
\]

The second factorial-cumulant corrections have nonzero finite limits:

\[
\begin{aligned}
\operatorname{Var}C_2(n)-\mathbb EC_2(n)&\longrightarrow-\zeta(2),\\
\operatorname{Var}C_3(n)-\mathbb EC_3(n)&\longrightarrow
 36\zeta(3)-16\zeta(2)-16\zeta(4)\approx-0.3620682952,\\
\operatorname{Cov}(C_2(n),C_3(n))&\longrightarrow
 -4\bigl(\zeta(2)-\zeta(3)\bigr)\approx-1.7715087.
\end{aligned}
\]

In particular, \(\operatorname{Var}C_3(n)<\mathbb EC_3(n)\) for every \(n\ge4\), while \(\operatorname{Cov}(C_2(n),C_3(n))<0\) for every \(n\ge3\). Thus the asymptotically independent Poisson approximation for these short-cycle counts conceals a persistent order-one negative covariance and a strictly negative variance correction.

## Assumptions and scope

Begin with a single vertex \(1\). Independently for each birth \(j\ge2\), choose two **labeled**, independently uniform parent targets \(U_j,V_j\in\{1,\ldots,j-1\}\) with replacement, inserting the directed edges \(j\to U_j\) and \(j\to V_j\). Parallel edges are retained, loops never arise. A two-cycle is exactly a pair of parallel edges, and a three-cycle consists of three distinct vertices joined by three distinct labeled edges, ignoring their common decreasing-label orientation. Counts include multiplicities of edge choices. The theorem is specifically for two outgoing edges per new vertex; it makes no claim for more general attachment kernels or simple-graph triangle conventions.

## Proof

Let \(\mathcal F_t\) be the history through vertex \(t\). For the birth of vertex \(t+1\), let \(X_{t+1}\) count newly created three-cycles. For distinct older vertices \(u,v\), write \(M_t(u,v)\in\{0,1,2\}\) for their pre-existing edge multiplicity. Because a new three-cycle must contain the latest vertex,

\[
X_{t+1}=\mathbf1_{\{U_{t+1}\ne V_{t+1}\}}M_t(U_{t+1},V_{t+1}).
\]

There are deterministically \(2(t-1)\) edges among the \(t\) older vertices. Writing \(D_t=C_2(t)\) for the number of double-edge pairs, we have

\[
\sum_{u<v}M_t(u,v)=2(t-1),\qquad
\sum_{u<v}M_t(u,v)^2=2(t-1)+2D_t.
\]

Uniform independent parent sampling therefore gives the exact conditional moments

\[
\mathbb E[X_{t+1}\mid\mathcal F_t]=\frac{4(t-1)}{t^2}=:\mu_t,
\qquad
\mathbb E[X_{t+1}^2\mid\mathcal F_t]=\mu_t+\frac{4D_t}{t^2}.
\]

The first conditional moment is deterministic. Hence the centered increments \(X_{t+1}-\mu_t\) are martingale differences, pairwise orthogonal in \(L^2\). Since \(C_3(n)=\sum_{t=1}^{n-1}X_{t+1}\), with \(X_2=0\), we obtain

\[
\mathbb EC_3(n)=\sum_{t=2}^{n-1}\mu_t
=4\bigl(H_{n-1}-H_{n-1}^{(2)}\bigr)
\]

and, using \(\mathbb E D_t=H_{t-1}\),

\[
\operatorname{Var}C_3(n)=\sum_{t=2}^{n-1}
\left(\mu_t+\frac{4H_{t-1}}{t^2}-\mu_t^2\right).
\]

Expanding \(\mu_t^2=16(t-1)^2/t^4\) proves the stated exact variance formula. Independently across birth times, \(I_j=\mathbf1_{\{U_j=V_j\}}\) is Bernoulli with success probability \(1/(j-1)\), and \(C_2(n)=\sum_{j=2}^n I_j\). This proves the two-cycle mean and variance.

For \(i\ne j\), \(\operatorname{Cov}(X_i,I_j)=0\): if \(i>j\), condition on \(\mathcal F_{i-1}\) using the deterministic conditional mean of \(X_i\); if \(i<j\), use the deterministic conditional mean of \(I_j\). At the same birth time, \(X_j I_j=0\), and therefore

\[
\operatorname{Cov}(X_j,I_j)=-\mathbb EX_j\,\mathbb E I_j
=-\frac{4(j-2)}{(j-1)^3}.
\]

Summing over births establishes the exact cross-covariance.

Euler's identity \(\sum_{t=2}^{\infty}H_{t-1}/t^2=\zeta(3)\) follows, for example, from \(\tfrac12\int_0^1\log^2(1-x)/x\,dx=\zeta(3)\). Taking the limit in the finite formulas proves the zeta-valued matrix corrections.

For strict three-cycle underdispersion, let

\[
\delta_t=\frac4{t^2}\left(H_{t-1}-4\left(1-\frac1t\right)^2\right),
\qquad
\operatorname{Var}C_3(n)-\mathbb EC_3(n)=\sum_{t=2}^{n-1}\delta_t.
\]

Direct exact rational comparison gives \(\delta_2=0\), \(\delta_t<0\) for \(3\le t\le21\), and \(\delta_t>0\) for \(22\le t\le31\). For \(t\ge32\), the inequality \(H_{t-1}\ge H_{31}>4>4(1-1/t)^2\) proves positivity. Thus the partial sums first decrease and then increase. Their limit is strictly negative: with \(R=100\), the rational bounds \(\zeta(3)\le H_R^{(3)}+1/(2R^2)\), \(\zeta(2)\ge H_R^{(2)}\), and \(\zeta(4)\ge H_R^{(4)}\) give

\[
36\zeta(3)-16\zeta(2)-16\zeta(4)
\le 36\left(H_R^{(3)}+\frac1{2R^2}\right)
-16H_R^{(2)}-16H_R^{(4)}<0.
\]

It follows that all partial sums starting at \(n=4\) are strictly negative. Finally \(H_{n-1}^{(2)}>H_{n-1}^{(3)}\) for \(n\ge3\) gives strict negative cross-covariance.

## Verification

A standalone rational-arithmetic checker, `checker.py`, enumerates every ordered-parent history through \(n=6\), up to \(14{,}400\) histories, computes the complete five-component mean/variance/covariance tuple independently from the graph definitions, and compares it with the formulas above. It additionally verifies the finite sign threshold and the rational zeta-bound certificate. The checker reports 153 passed finite assertions. These finite checks corroborate the algebra and signs; the infinite limits follow from the analytic proof and classical Euler identity, not from enumeration.

## Relationship to prior work

Björklund, Holmgren, Janson, and Lo gave Poisson approximations for uniform-attachment multigraph cycle counts and the exact mean of three-cycles for arbitrary fixed outdegree; their Section 3 and Equation (3.10) contain the mean credited above. Their Section 7 provides total-variation estimates but not the exact finite second-cumulant matrix derived here; total-variation convergence with diverging Poisson means alone does not imply convergence of unbounded second moments. Burghart's recent work uses the same uniform-parent recursive DAG but studies ancestry and descendant sets, not joint cycle-count second moments. The current result identifies the finite cumulant residue left invisible by first-order Poisson approximations. No claim is made to the general Poisson approximation theorem or to Euler's identity.

## Limitations

The exact joint second-moment identities are restricted to two labeled out-edges chosen independently with replacement. They do not describe all higher cumulants, a full mod-Poisson correction, or growing outdegree. A complete historical priority check beyond the sources listed is still warranted; these calculations have not been independently audited.

## References

1. J. Björklund, C. Holmgren, S. Janson, and T. Y. Y. Lo, *Approximation of Subgraph Counts in the Uniform Attachment Model*, arXiv:2311.04184 (first posted 2023-11-07), especially Definition in Section 2, Example 3.4 and Equation (3.10), and Section 7. https://arxiv.org/abs/2311.04184 ; https://doi.org/10.1017/S0963548324000294.
2. F. Burghart, *Ancestries in Random \(d\)-DAGs*, arXiv:2606.30475 (first posted 2026-06-29); proceedings version *Ancestries and Descendants in a Random DAG*, LIPIcs AofA 2026, Article 7. https://arxiv.org/abs/2606.30475 ; https://doi.org/10.4230/LIPIcs.AofA.2026.7.
