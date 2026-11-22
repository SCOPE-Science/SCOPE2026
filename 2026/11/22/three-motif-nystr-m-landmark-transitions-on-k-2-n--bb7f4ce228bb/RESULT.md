# Three-motif Nyström landmark transitions on \(K_{2,n}\)

## Finding
For every integer \(n\ge3\), every real screening parameter \(\mu>0\), and the unweighted complete bipartite graph \(K_{2,n}\), exactly two columns of the shifted-Laplacian inverse \(G_\mu=(\mu I+L)^{-1}\) are selected to minimize the standard unrescaled Nyström residual trace. There are exactly three pair orbits: \(A\), the two vertices of the size-two shore; \(B\), two vertices of the size-\(n\) shore; and \(C\), one vertex on each shore.

Define
\[
\alpha_n=\frac{2}{n-2},\qquad
\beta_n=\frac{\sqrt{n^2+4n-8}-n}{2},
\]
\[
P_n(t)=(n-2)t^4+2(n^2-n-1)t^3+n(n^2+2)t^2+8(2n-1)t-2(n^3-3n^2-4n+4).
\]
For \(n\ge4\), \(P_n\) has a unique positive zero \(\gamma_n\).

For \(3\le n\le5\), the maximizing orbit is \(A\) for \(0<\mu<\beta_n\), both \(A\) and \(B\) at \(\mu=\beta_n\), and \(B\) for \(\mu>\beta_n\). Orbit \(C\) never minimizes the trace residual in these sizes.

For every \(n\ge6\), the maximizing orbit is \(A\) for \(0<\mu<\alpha_n\), both \(A\) and \(C\) at \(\alpha_n\), \(C\) for \(\alpha_n<\mu<\gamma_n\), both \(C\) and \(B\) at \(\gamma_n\), and \(B\) for \(\mu>\gamma_n\). No other ties occur. The respective orbit sizes are \(1\), \(\binom n2\), and \(2n\), so the statement also counts every optimal unordered column pair. Moreover \(\gamma_n\to\sqrt2\) and \(\alpha_n\sim 2/n\) as \(n\to\infty\).

## Assumptions and scope
The graph is connected, simple and unweighted, with the combinatorial Laplacian \(L=D-A\); the shift is strictly positive; columns are two distinct coordinate columns; and the Nyström approximation is \(N_S=G_{\mu,:,S}(G_{\mu,S,S})^{-1}G_{\mu,S,:}\). Since \(G_\mu\) is strictly positive definite, every selected two-by-two principal submatrix is invertible. The residual \(G_\mu-N_S\) is positive semidefinite, so its trace is its nuclear norm. The theorem optimizes over *all* \(\binom{n+2}{2}\) pairs, not only over a prescribed shore or across-shore pairs.

## Proof
Write \(t=\mu\), \(N=n+2\). The graph Laplacian has orthogonal spectral projectors for constants (eigenvalue zero), the shore-contrast mode (eigenvalue \(N\)), size-two shore contrasts (eigenvalue \(n\)), and size-\(n\) shore contrasts (eigenvalue \(2\)). Therefore the Green matrix is a sum of four corresponding scalar inverses. For each pair orbit, the determinant of its Green principal block simplifies to
\[
D_A(t)=\frac{t+2}{t(t+n)(t+n+2)},\quad
D_B(t)=\frac{t^2+(n+2)t+4}{t(t+2)^2(t+n+2)},
\]
\[
D_C(t)=\frac{(t+1)(t+n+1)}{t(t+2)(t+n)(t+n+2)}.
\]
Differentiate \(G_t=(tI+L)^{-1}\) to obtain \(G'_t=-G_t^2\). Jacobi's determinant identity gives the captured trace
\[
T_J(t)=\operatorname{tr}\bigl((G_t)_{S,S}^{-1}(G_t^2)_{S,S}\bigr)=-\frac{d}{dt}\log D_J(t),
\]
for \(J\in\{A,B,C\}\). The Nyström error is \(\operatorname{tr}G_t-T_J(t)\); thus maximizing \(T_J\) minimizes the residual. Direct differentiation and cancellation give, with strictly positive denominators,
\[
T_A-T_C=\frac{2-(n-2)t}{(t+1)(t+2)(t+n+1)},
\]
\[
T_A-T_B=\frac{-2(n-2)(t^2+nt-n+2)}{(t+n)(t+2)[t^2+(n+2)t+4]},
\]
\[
T_B-T_C=\frac{P_n(t)}{(t+n)(t+1)(t+2)(t+n+1)[t^2+(n+2)t+4]}.
\]
The first difference changes sign exactly at \(\alpha_n\). The second changes from positive to negative at \(\beta_n\). For \(n=3\), all coefficients of \(P_n\) are positive, so \(T_B>T_C\) for all \(t>0\). For every integer \(n\ge4\), the coefficients of \(P_n\), ordered from degree four to degree zero, have positive first four entries and a negative constant term. The derivative is strictly positive for \(t>0\), while \(P_n(0)<0\) and \(P_n(t)\to\infty\); hence there is exactly one positive root \(\gamma_n\), with \(T_B<T_C\) below and \(T_B>T_C\) above.

Comparison of the first two crossings gives
\[
\left.\left(t^2+nt-n+2\right)\right|_{t=\alpha_n}
=-\frac{n^3-8n^2+16n-12}{(n-2)^2}.
\]
The cubic in the numerator is negative at \(n=3,4,5\), positive at \(n=6\), and strictly increasing for real \(n\ge4\) (derivative \(3n^2-16n+16\ge0\) for \(n\ge4\)). Thus \(\beta_n<\alpha_n\) for \(n=3,4,5\) and \(\alpha_n<\beta_n\) for all \(n\ge6\). If \(\beta_n<\alpha_n\), then \(A\) dominates until \(\beta_n\), and \(B\) dominates thereafter: for \(n\ge4\), \(\gamma_n<\beta_n\) because at \(\beta_n\) we have \(T_B=T_A>T_C\); for \(n=3\), \(T_B>T_C\) everywhere. If \(\alpha_n<\beta_n\), then at \(\beta_n\), \(T_C>T_A=T_B\), so \(\gamma_n>\beta_n\). The \(A\)-to-\(C\)-to-\(B\) ordering follows by comparing signs on the resulting intervals. Since \(P_n(t)/n^3\to t^2-2\) uniformly on compact \(t\)-intervals and each polynomial has one positive root, \(\gamma_n\to\sqrt2\). The formula for \(\alpha_n\) gives its asymptotic directly.

## Verification
The accompanying `check_biclique.py` independently recomputes all three determinant formulas and captured traces from exact rational inverses of \(\mu I+L(K_{2,n})\), checks the three symbolic pairwise differences, performs exhaustive pair-orbit checks for sample graph sizes, and checks all relevant polynomial coefficient signs. Run `python check_biclique.py` with Python 3 and SymPy. The script has no network or private data dependencies and prints the exact assertion count. The infinite-family result rests on the symbolic formulas and analytic sign arguments above; the finite checks are corroboration only.

## Relationship to prior work
Gittens and Mahoney (2013, arXiv:1303.1849) formulate Nyström SPSD sketches and prove broad trace-norm approximation bounds, but their inspected 2013 conference article does not derive this exact two-column graph-family optimizer phase diagram. Fornace and Lindsey (2024, arXiv:2407.01698) develop nuclear-score algorithms and theory for column selection and graph Laplacian reduction; the accessible abstract does not supply this specific three-orbit classification. Published results on perfect/noise-free leader selection in bipartite networks optimize a different grounded-Laplacian inverse-trace functional, not the positive-screening Nyström residual; they do not directly imply the two threshold laws stated here. The explicit positive-screening comparison, tie multiplicities, and the \(n=6\) structural frontier are therefore the separate contribution claimed here, subject to the residual publication-priority uncertainty below.

## Limitations
No assertion is made for general \(K_{m,n}\) with \(m>2\), unequal edge weights, noisy landmarks, more than two columns, or other low-rank objectives. The full texts of every potentially relevant publication could not be exhaustively searched, so unindexed equivalent prior work remains possible. The result has received mathematical self-review only, not independent review or publication certification.

## References
1. A. Gittens and M. W. Mahoney, “Revisiting the Nyström method for improved large-scale machine learning,” ICML/PMLR 28, 2013; original preprint arXiv:1303.1849, first posted 2013-03-07. https://arxiv.org/abs/1303.1849 and https://proceedings.mlr.press/v28/gittens13.html
2. M. Fornace and M. Lindsey, “Column and row subset selection using nuclear scores: algorithms and theory for Nyström approximation, CUR decomposition, and graph Laplacian reduction,” arXiv:2407.01698 (2024). https://arxiv.org/abs/2407.01698
3. “Exact leader allocation and a square-root law on complete bipartite networks,” public indexed mathematical result, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-leader-allocation-and-a-square-root-law-on-complete-bipart--3151e2186be2
