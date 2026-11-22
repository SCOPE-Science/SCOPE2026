# Sharp positivity recovery for fractional heat on all connected strongly regular graphs

## Finding
Let \(G\) be a finite connected, noncomplete, simple strongly regular graph with parameters \((v,k,\lambda,\mu)\). Write \(A_G\) for its adjacency matrix, \(L=kI-A_G\), and let \(k>r>s\) be its three adjacency eigenvalues. Set
\[
a=k-r,\quad b=k-s,\quad C=\frac{k-s}{r-s}>1,\quad h=v-k-1>0.
\]
For every real \(\alpha>0\) define \(K_\alpha(t)=\exp(-tL^\alpha)\) for \(t\ge0\), using nonnegative spectral functional calculus and \(0^\alpha=0\). Then all entries of \(K_\alpha(t)\) are strictly positive at all positive times **if and only if** \(0<\alpha\le1\). When \(\alpha>1\), all diagonal and adjacent-vertex entries remain strictly positive. All nonadjacent distinct-vertex entries agree and are negative exactly for \(0<t<T_\alpha\), vanish at the single positive time \(T_\alpha\), and are positive for \(t>T_\alpha\). That sharp recovery time is the unique positive root of
\[
1-Ce^{-a^\alpha t}+(C-1)e^{-b^\alpha t}=0.
\]
In particular, the matrix is entrywise nonnegative exactly at \(t=0\) or \(t\ge T_\alpha\) when \(\alpha>1\). With \([u]_+=\max\{u,0\}\), the exact operator norm on both counting \(\ell^1\) and \(\ell^\infty\) is
\[
\boxed{\|K_\alpha(t)\|_{\infty\to\infty}=\|K_\alpha(t)\|_{1\to1}=1+\frac{2h}{v}[Ce^{-a^\alpha t}-(C-1)e^{-b^\alpha t}-1]_+.}
\]
For \(\alpha>1\), its unique peak occurs at
\[
t_{\rm pk}=\frac{(\alpha-1)\log(b/a)}{b^\alpha-a^\alpha}.
\]
For this fixed graph and \(\varepsilon=\alpha-1\downarrow0\),
\[
\boxed{T_{1+\varepsilon}=\frac{2\log(b/a)}{b-a}\varepsilon+O_G(\varepsilon^2),\qquad
\sup_{t\ge0}\|K_{1+\varepsilon}(t)\|_{\infty\to\infty}=1+\frac{hCa\log^2(b/a)}{v(b-a)}\varepsilon^2+O_G(\varepsilon^3).}
\]
Furthermore, as \(\alpha\to\infty\),
\[
\boxed{a^\alpha T_\alpha\longrightarrow\log C,\qquad
\sup_{t\ge0}\|K_\alpha(t)\|_{\infty\to\infty}\longrightarrow1+\frac{2h(C-1)}{v}.}
\]
These assertions include primitive strongly regular graphs such as the five-cycle, Petersen, rook and triangular graphs; they are not limited to complete multipartite graphs.

## Assumptions and scope
A strongly regular graph has \(v\) vertices, degree \(k\), precisely \(\lambda\) common neighbors for adjacent vertices, and precisely \(\mu\) for nonadjacent distinct vertices. We require \(0<k<v-1\) and connectivity, so \(\mu>0\) and the graph has diameter two. The adjacency eigenvalues \(r>s\) other than \(k\) are the two roots of
\[
x^2-(\lambda-\mu)x-(k-\mu)=0.
\]
The positive Laplacian eigenvalues satisfy \(0<a<b\). The scalar exponent \(\alpha\) ranges over all positive real numbers, not just the fractional-diffusion interval. All statements use the unweighted combinatorial Laplacian, real counting-space entries and the standard row/column sum operator norms. The graph is held fixed for both asymptotic expansions. The case \(t=0\) is the identity matrix, not strictly positive.

## Proof
Let \(E_0=J/v\), \(E_a\), and \(E_b\) be the orthogonal spectral projectors of \(L\), where \(J\) is the all-ones matrix. Since
\[
E_a=\frac{A_G-sI-(k-s)J/v}{r-s},\qquad E_b=I-E_0-E_a,
\]
for nonadjacent distinct vertices \(i,j\),
\[
(E_a)_{ij}=-\frac{C}{v},\qquad (E_b)_{ij}=\frac{C-1}{v},
\]
and hence
\[
(K_\alpha(t))_{ij}=\frac1v\bigl[1-Ce^{-a^\alpha t}+(C-1)e^{-b^\alpha t}\bigr].\tag{1}
\]
For adjacent vertices, set \(U=(v-k+s)/(r-s)\), giving
\[
(K_\alpha(t))_{ij}=\frac1v\bigl[1+Ue^{-a^\alpha t}-(1+U)e^{-b^\alpha t}\bigr].\tag{2}
\]
Here \(U\ge0\): the complement graph has degree \(v-k-1\) and adjacency eigenvalue \(-1-s\), so its spectral radius bound gives \(-1-s\le v-k-1\). Thus the numerator in (2) equals \((1-e^{-b^\alpha t})+U(e^{-a^\alpha t}-e^{-b^\alpha t})>0\) whenever \(t>0\). Every diagonal is positive because the constant-mode projector contributes \(1/v\), and the other projector diagonals are nonnegative.

The strict inequality \(C>1\) follows from \(C-1=(k-r)/(r-s)=a/(b-a)>0\). Therefore \(C/(C-1)=b/a\). Put \(A=a^\alpha\), \(B=b^\alpha\) and \(q(t)=1-Ce^{-At}+(C-1)e^{-Bt}\). Then
\[
q(0)=0,\quad q'(t)=CAe^{-At}-(C-1)Be^{-Bt},\quad
q'(0)=CA\bigl[1-(b/a)^{\alpha-1}\bigr].\tag{3}
\]
The ratio between the positive and negative derivative terms is \([CA/((C-1)B)]e^{(B-A)t}\), strictly increasing. For \(0<\alpha\le1\) it is at least one at \(t=0\), hence \(q'(t)>0\) for all \(t>0\). For \(\alpha>1\), it starts below one, crosses one precisely once at \(t_{\rm pk}=(\alpha-1)\log(b/a)/(B-A)\), and then exceeds one; consequently \(q\) decreases from zero to a strictly negative minimum, then increases strictly to one. It has exactly one positive root \(T_\alpha>t_{\rm pk}\), with the asserted strict signs. This proves the full entrywise classification.

The heat matrix is symmetric and every row and column sums to one because \(L^\alpha\mathbf1=0\). Each row has \(h=v-k-1\) nonadjacent entries, all equal to \(q(t)/v\); the other entries are strictly positive for positive time. Thus the absolute row sum is exactly \(1+2h[-q(t)]_+/v\), yielding the stated sharp norm and its peak. Symmetry gives the \(\ell^1\) result.

Write \(\varepsilon=\alpha-1\). Taylor expansion at \((\varepsilon,t)=(0,0)\) gives
\[
q'(0)=-Ca\log(b/a)\,\varepsilon+O_G(\varepsilon^2),\qquad
q''(0)=Ca(b-a)+O_G(\varepsilon).
\]
As the positive root tends to zero, divide the Taylor identity \(q(T_\alpha)=0\) by \(T_\alpha\); the implicit-function theorem applies to \(q(t)/t\) analytically extended at zero, with nonzero \(t\)-derivative \(Ca(b-a)/2\). Hence
\[
T_{1+\varepsilon}=\frac{2\log(b/a)}{b-a}\varepsilon+O_G(\varepsilon^2).
\]
The peak is at half this time to leading order, and the quadratic minimum is
\[
q(t_{\rm pk})=-\frac{Ca\log^2(b/a)}{2(b-a)}\varepsilon^2+O_G(\varepsilon^3).
\]
Substitution in the norm formula gives its claimed critical expansion. Finally put \(u=a^\alpha t\) and \(R=(b/a)^\alpha\). The positive root solves \(1-Ce^{-u}+(C-1)e^{-Ru}=0\). As \(R\to\infty\), the root tends to \(\log C\): the function converges uniformly to \(1-Ce^{-u}\) on compact positive intervals, and its unique positive root is trapped between any two positive numbers straddling \(\log C\). At the peak, \(a^\alpha t_{\rm pk}=(\alpha-1)\log(b/a)/(R-1)\to0\), while \(b^\alpha t_{\rm pk}=R(\alpha-1)\log(b/a)/(R-1)\to\infty\). Therefore \(q(t_{\rm pk})\to1-C\), proving the large-order norm limit.

## Verification
The accompanying `checker.py` builds five independent strongly regular graph adjacency matrices from combinatorial definitions: the five-cycle, Petersen graph, four-by-four rook graph, triangular graph on five points, and complete bipartite graph with two parts of three vertices. It constructs \(L\) directly, diagonalizes it numerically, and compares its spectral heat kernel against the two explicit off-diagonal formulas for eight positive orders and five positive times each. It also independently compares the exact maximum row-sum norm, checks graph parameters and the near-critical root coefficient. Run `OPENBLAS_NUM_THREADS=1 python checker.py` with NumPy available. All 200 heat-kernel and norm comparison cases passed. These finite computations are corroboration only; the proof above covers all admissible graphs, orders and times.

## Relationship to prior work
Benzi, Bertaccini, Durastante and Simunec (first public preprint 16 December 2019) develop spectral fractional graph dynamics and positivity for \(0<\alpha\le1\); they do not classify the \(\alpha>1\) negative-entry recovery for all connected strongly regular graphs. The established projectors and three-eigenvalue relations underlie the proof; no new spectral classification of strongly regular graphs is claimed. Published exact positivity laws for fractional heat on complete multipartite graphs already cover that subfamily, including balanced multipartite graphs that are strongly regular; those special cases are credited, not counted as new. Other published strongly regular diffusion results concern Gauss–Legendre or Runge–Kutta rational/polynomial update operators rather than this exact fractional heat semigroup. The contribution is the full strongly regular graph family, including primitive examples, with sharp \(\ell^1/\ell^\infty\) norms and two critical asymptotic regimes.

## Limitations
The conclusion does not apply without the strongly regular three-eigenspace structure, nor to arbitrary weighted or directed graphs, normalized Laplacians, other matrix norms, or operator families approximating rather than equaling \(e^{-tL^\alpha}\). The expansions are not uniform in varying graph parameters. Symbolic reasoning establishes the general theorem; finite numerical checks do not certify all cases. A residual risk of unindexed equivalent spectral-graph results remains. No independent validation is asserted.

## References
1. M. Benzi, D. Bertaccini, F. Durastante and I. Simunec, *Nonlocal network dynamics via fractional graph Laplacians*, arXiv:1912.07288v1 (16 December 2019), https://arxiv.org/abs/1912.07288; later *Journal of Complex Networks* 8 (2020), cnaa017.
2. F.-H. Lin and C.-W. Weng, *Strongly Regular Graphs as Laplacian Extremal Graphs*, arXiv:1411.6532 (24 November 2014), https://arxiv.org/abs/1411.6532 (established spectral background).
3. *A sharp positivity transition for fractional graph heat on complete multipartite networks* (published mathematical result; restricted graph family), https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-a-sharp-positivity-transition-for-fractional-graph-heat-on-compl--8af258cef8b1.
4. *A sharp Padé positivity horizon for strongly regular graph diffusion* (published result; a different rational heat-update operator), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-sharp-pad-positivity-horizon-for-strongly-regular-graph-diffus--894835468c5c.
