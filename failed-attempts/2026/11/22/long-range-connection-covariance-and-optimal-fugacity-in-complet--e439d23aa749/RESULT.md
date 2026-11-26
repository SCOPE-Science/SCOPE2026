# Long-range connection covariance and optimal fugacity in complete bipartite arboreal gases

## Finding
Let \(G_n=K_{2,n}\) have two distinguished hubs \(u,v\) and leaves \(1,\ldots,n\). For each integer \(n\ge4\), sample an **unrooted spanning forest** \(F\subseteq E(G_n)\) with probability proportional to \(t^{|F|}\), where every edge has the same finite activity \(t>0\). For four distinct leaves, define \(X=\mathbf1\{1\leftrightarrow2\}\) and \(Y=\mathbf1\{3\leftrightarrow4\}\), with connectivity evaluated inside \(F\). Then

\[
\operatorname{Cov}_t(X,Y)=\frac{4t^5\big(2nt^2+nt+4t+4\big)}{(1+2t)^4\big(nt^2+2t+1\big)^2}>0.
\]

For each \(n\ge4\), this covariance has exactly one global maximizer \(t_n\in(1,\infty)\). Writing

\[
F_n(t)=2n^2t^5+n(4-n)t^4-n(n+8)t^3-(15n+16)t^2-(3n+28)t-10,
\]

the optimizer is precisely the unique positive real zero of \(F_n\). Moreover,

\[
t_n=1+\frac{22}{3n}+O(n^{-2}),\qquad
\lim_{n\to\infty}n\operatorname{Cov}_t(X,Y)=\frac{4t^2}{(1+2t)^3},\qquad
\lim_{n\to\infty}n\max_{s>0}\operatorname{Cov}_s(X,Y)=\frac4{27}.
\]

The middle limit holds for every fixed \(t>0\). The maximum in the final limit is over each finite graph's activity, not over the already-taken limit; both give the same asymptotic value.

## Assumptions and scope
The vertex set has \(n+2\) labeled vertices, and every hub is adjacent to every leaf; there are no hub-to-hub or leaf-to-leaf edges. Every acyclic subset of the \(2n\) available edges, including the empty forest and disconnected forests, is allowed with weight \(t^{|F|}\); no component or root weights are inserted. The two connectivity events involve four distinct leaves, so \(n\ge4\). The strict inequality is for finite \(t>0\) only. No claim is made for other host graphs, disjointness patterns, or arbitrary heterogeneous activities.

## Proof
A cycle in \(K_{2,n}\) uses both hub edges at two distinct leaves. Consequently an edge subset is a forest **if and only if** at most one leaf has both of its hub edges present. Put \(d=1+2t\). The three possible states at an unbridged leaf—no edge, its edge to \(u\), and its edge to \(v\)—have respective weights \(1,t,t\). Thus the partition function is exactly

\[
Z_n(t)=d^n+nt^2d^{n-1}=d^{n-1}(d+nt^2).
\]

Let \(B=0\) mean that no leaf has both incident edges, and \(B=i\) mean leaf \(i\) has both. These are mutually exclusive and exhaustive, with

\[
\Pr(B=0)=w_0=\frac{d}{d+nt^2},\qquad
\Pr(B=i)=w_1=\frac{t^2}{d+nt^2}.
\]

Conditional on \(B\), every *other* leaf independently chooses its three unbridged states, with single-hub occupation probability \(p=t/d\) for each specified hub. When \(B=0\), any two leaves are connected exactly when they attach to the same hub, with conditional probability \(2p^2\). When a bridge occurs at a leaf outside an observed pair, the hubs are connected and the observed pair is connected whenever each leaf has at least one edge, with probability \(4p^2\). When the bridge occurs at one of the pair's leaves, the pair connection probability is \(2p\).

For the events \(X,Y\) using disjoint pairs, the above conditional independence yields

\[
\mathbb E[X]=2w_0p^2+4(n-2)w_1p^2+4w_1p
=\frac{2t^2(2nt^2+4t+1)}{d^2(nt^2+d)}
\]

and

\[
\mathbb E[XY]=4w_0p^4+16(n-4)w_1p^4+32w_1p^3
=\frac{4t^4(4nt^2+10t+1)}{d^4(nt^2+d)}.
\]

Subtracting \(\mathbb E[X]^2\) gives the stated covariance. Its numerator and denominator are strictly positive for \(t>0\).

Direct differentiation of the resulting rational expression gives

\[
\frac{d}{dt}\operatorname{Cov}_t(X,Y)=
-\frac{8t^4F_n(t)}{(1+2t)^5(nt^2+2t+1)^3}.
\]

For \(n\ge4\), the coefficients of \(F_n\), in descending powers of \(t\), have exactly one sign change (the leading coefficient is positive, while every nonzero lower coefficient is nonpositive). By Descartes' rule of signs and \(F_n(0)=-10\), \(F_n\) has exactly one positive root. Since covariance vanishes at both \(t\downarrow0\) and \(t\to\infty\), that root is the unique global maximum. Furthermore \(F_n(1)=-2(11n+27)<0\), so \(t_n>1\).

For fixed \(t>0\), division of the exact covariance by leading powers of \(n\) gives

\[
 n\operatorname{Cov}_t(X,Y)\longrightarrow c(t)=\frac{4t^2}{(1+2t)^3}.
\]

The leading \(n^2\) coefficient of \(F_n(t)\) is \(t^3(2t+1)(t-1)\), so the unique positive root converges to \(1\). Inserting \(t=1+a/n+O(n^{-2})\) into \(F_n(t)=0\) yields \(3a-22=0\), hence \(a=22/3\). Finally \(c'(t)\) changes sign exactly once, at \(t=1\), and \(c(1)=4/27\). Continuity of the rational expression with \(t_n\to1\) gives the asserted limiting maximum. This proves every claimed assertion.

## Verification
The accompanying standalone `checker.py` enumerates **all acyclic edge subsets** of \(K_{2,n}\), including disconnected and empty forests, for \(n=4,5,6,7\) at three exact rational activities. It computes both marked connection events from union–find components and compares the resulting exact rational covariance with the formula. Separate exact rational checks verify the one-bridge normalization and moment formulas for six sizes up to \(n=100\). It reports `FOREST_BRIDGE_EXACT_CHECKS_PASSED 48`. The infinite-domain conclusions follow from the proof, not from the finite tests.

## Relationship to prior work
Grimmett and Winkler introduced and investigated uniform spanning forests and edge-negative association. Erickson supplied a sums-of-squares approach to edge-negative dependence for series-parallel forests. Cao and Fu proved negative *edge-occupation* covariance for uniform forests on complete bipartite graphs; that does not determine the dependence of two disjoint **vertex-connectivity** events at general activity. Çiçeksiz and Ravichandran identified positive connectivity-event correlation as a distinct question and established high-fugacity cases, without an all-activity all-size theorem for this observable. Existing all-weight cactus-graph connectivity results do not apply: \(K_{2,n}\) for \(n\ge3\) has overlapping four-cycles. The claim here concerns the explicit nonlocal covariance, its finite-size maximum and its asymptotic optimization, not a general positive-association theorem.

## Limitations
Only homogeneous positive finite activities and four distinct leaves are treated. The correlation is of order \(n^{-1}\) for fixed activity; it therefore vanishes in the infinite-leaf limit even though it is strictly positive at every finite size. The optimum expansion is asymptotic rather than an exact closed form. Independent scientific validation and comprehensive historical-priority verification have not been performed.

## References
- G. R. Grimmett and S. N. Winkler, *Negative association in uniform forests and connected graphs*, arXiv:math/0302185 (first publicly submitted 2003-02-17), https://arxiv.org/abs/math/0302185.
- A. Erickson, *Sums of squares and negative correlation for spanning forests of series parallel graphs*, arXiv:1008.3660 (2010), https://arxiv.org/abs/1008.3660.
- R. A. Çiçeksiz and M. Ravichandran, *Negative Correlation for Forests and the \(q<1\) Random-Cluster Model*, arXiv:2610.00549 (2026), https://arxiv.org/abs/2610.00549.
- Y. Cao and H. Fu, *Negative edge correlation in complete bipartite graphs*, arXiv:2610.36749 (2026), https://arxiv.org/abs/2610.36749.
