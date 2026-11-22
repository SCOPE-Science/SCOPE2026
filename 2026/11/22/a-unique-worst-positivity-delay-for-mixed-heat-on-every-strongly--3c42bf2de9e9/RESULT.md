# A unique worst positivity delay for mixed heat on every strongly regular graph

## Finding

Let \(G\) be a finite, simple, connected, noncomplete strongly regular graph, with \(N\) vertices, degree \(k\), and common-neighbor numbers \(\lambda\) for adjacent vertices and \(\mu\) for nonadjacent vertices. Let \(L=kI-A_G\) be its unweighted combinatorial Laplacian. Its two distinct positive eigenvalues are \(0<a<b\); set \(\Delta=b-a\). For every coupling \(\eta>0\), the mixed heat family

\[
S_\eta(t)=\exp[-t(L+\eta L^2)],\qquad t\geq0,
\]

is entrywise nonnegative **exactly** for

\[
 t\in\{0\}\cup[T_G(\eta),\infty).
\]

Here \(T_G(\eta)>0\) is the **unique positive root** of

\[
 b\exp[-(a+\eta a^2)T]-a\exp[-(b+\eta b^2)T]=b-a.
\tag{1}
\]

Before that root, every nonedge entry is negative; at it, every nonedge entry vanishes; after it, all entries are strictly positive. In particular, the sharp positivity-recovery horizon depends only on the two positive Laplacian eigenvalues, not on any further isomorphism type.

More strongly, \(\eta\mapsto T_G(\eta)\) has **exactly one maximum** on \((0,\infty)\). Define

\[
 U=\log\left(1+\frac ab\right),\qquad
 V=\log\left(1+\frac ba\right).
\]

Then the unique maximizing coupling and the corresponding worst recovery time are

\[
 \boxed{\eta_* =\frac{aV-bU}{b^2U-a^2V}>0,\qquad
 T_G(\eta_*)=\frac{b^2U-a^2V}{ab(b-a)}>0.}
\tag{2}
\]

The recovery horizon tends to zero both as \(\eta\downarrow0\) and as \(\eta\to\infty\), so the delay is genuinely nonmonotone with coupling strength.

## Assumptions and scope

A strongly regular graph here is simple, connected, regular, noncomplete, and has fixed numbers of common neighbors of adjacent and nonadjacent vertex pairs. Both primitive examples (pentagon, Petersen, rook and Paley graphs) and imprimitive examples (connected regular complete multipartite graphs) are included. The result is for the combinatorial graph Laplacian with unit edge conductances and the real symmetric finite-dimensional semigroup above. “Entrywise nonnegative” means every real matrix entry is nonnegative. Strict positivity is asserted only for positive times strictly beyond the recovery horizon. There is no assertion for arbitrary graphs, arbitrary edge weights, or a generator involving higher powers.

The classical strongly regular graph identity is

\[
 A_G^2=(k-\mu)I+(\lambda-\mu)A_G+\mu J.
\]

The two nontrivial adjacency eigenvalues \(r>s\) solve

\[
 z^2-(\lambda-\mu)z-(k-\mu)=0,
\]

and \(a=k-r\), \(b=k-s\). In particular \(\Delta=r-s\). Connectedness gives \(a>0\), and the complement-Laplacian identity gives \(b\le N\).

## Proof

**Spectral projectors and the three entry types.** Write \(A=A_G\), and let \(P_a,P_b\) be the orthogonal projectors onto the \(a\)- and \(b\)-eigenspaces of \(L\). The strongly regular identity and the fact that \(J/N\) projects onto constants give

\[
 P_a=\frac{A-sI-(b/N)J}{\Delta},\qquad
 P_b=\frac{rI-A+(a/N)J}{\Delta}.
\]

These are orthogonal spectral projectors; in particular their diagonal entries are nonnegative. Put \(\alpha=a+\eta a^2\), \(\beta=b+\eta b^2\), so \(0<\alpha<\beta\). Spectral calculus yields

\[
 S_\eta(t)=\frac{J}{N}+e^{-\alpha t}P_a+e^{-\beta t}P_b.
\]

For nonadjacent distinct vertices \(i,j\), \(A_{ij}=0\), so

\[
 S_\eta(t)_{ij}=\frac{1}{N\Delta}
 \bigl[\Delta-be^{-\alpha t}+ae^{-\beta t}\bigr].
\tag{3}
\]

For adjacent distinct vertices, the spectral formula rearranges to

\[
 S_\eta(t)_{ij}=\frac{1-e^{-\beta t}}N
 +\frac{N-b}{N\Delta}\bigl(e^{-\alpha t}-e^{-\beta t}\bigr)>0
 \quad(t>0).
\tag{4}
\]

Both summands in (4) are nonnegative, and the first is positive, since \(b\le N\). Every diagonal entry is positive for all \(t\ge0\), because it equals \(1/N\) plus nonnegative projector-diagonal terms.

**The unique sharp crossing.** Define

\[
 F_\eta(t)=be^{-\alpha t}-ae^{-\beta t}-\Delta.
\]

We have \(F_\eta(0)=0\), \(F_\eta'(0)=ab\eta\Delta>0\), and \(F_\eta(t)\to-\Delta\) as \(t\to\infty\). Its derivative is positive precisely for

\[
 0\le t<\frac{\log[(1+\eta b)/(1+\eta a)]}{\beta-\alpha},
\]

and strictly negative thereafter. Hence \(F_\eta\) has one strict positive maximum and exactly one further zero \(T_G(\eta)>0\). By (3), nonedge entries are strictly negative for \(0<t<T_G(\eta)\), zero at the horizon and strictly positive afterwards. Together with (4) and the diagonal statement, this proves the entire nonnegative-time set and sharpness.

**Existence of an interior maximizing coupling.** The nonzero root is transversal (it lies on the decreasing branch), hence implicit differentiation makes \(T_G\) smooth for \(\eta>0\). Its defining equation implies

\[
 0<T_G(\eta)<\frac{1}{\alpha}\log\left(\frac{b}{b-a}\right),
\]

so \(T_G(\eta)\to0\) when \(\eta\to\infty\). At \(\eta=0\), the corresponding function \(F_0(t)\) is strictly negative for every \(t>0\), since \(F_0'(t)=ab(e^{-bt}-e^{-at})<0\). Uniform convergence on each fixed compact time interval then forces \(T_G(\eta)\to0\) as \(\eta\downarrow0\). Thus the positive continuous horizon attains a global maximum at some finite positive coupling.

**Uniqueness and closed form.** At any stationary coupling of \(T_G\), implicit differentiation of \(F_\eta(T_G(\eta))=0\) gives

\[
 -ba^2e^{-\alpha T}+ab^2e^{-\beta T}=0,
\quad\text{hence}\quad e^{-(\beta-\alpha)T}=a/b.
\]

Combining this with (1) gives

\[
 e^{-\alpha T}=\frac b{a+b},\qquad
 e^{-\beta T}=\frac a{a+b},
\]

or equivalently \(\alpha T=U\) and \(\beta T=V\). Consequently any stationary coupling must obey

\[
 \frac{\beta}{\alpha}=\frac VU.
\]

But \(\beta/\alpha=(b+\eta b^2)/(a+\eta a^2)\) is strictly increasing in \(\eta\), since its derivative is \(ab(b-a)/(a+\eta a^2)^2>0\). Therefore there is **at most one** stationary coupling, while existence was already established. Solving the two linear equations \(T(a+\eta a^2)=U\) and \(T(b+\eta b^2)=V\) yields precisely (2). This stationary point is necessarily the unique global maximum, and existence proves both displayed denominators are positive. \(\square\)

## Verification

The accompanying standalone `check_srg_heat.py` checks the closed-form horizon and maximizer against direct matrix exponentials on seven graph families, including primitive strongly regular graphs. It constructs each adjacency matrix directly, verifies constant degree and uniform common-neighbor counts, independently evaluates \(\exp[-t(L+\eta L^2)]\), checks all three entry types on either side of the calculated horizon, and compares eight couplings per graph. It completed 392 matrix-entry and maximizer consistency cases. These finite floating-point checks are reproducibility aids; the exact all-graph statements are established by the analytic proof, not inferred from the samples.

Run with `python check_srg_heat.py` after installing Python 3, NumPy, SciPy and NetworkX. No downloaded data is required.

## Relationship to prior work

Daners, Glück and Kennedy (arXiv:1511.05294, submitted 2015-11-17) develop general spectral and order-theoretic criteria for eventual positivity, including finite-dimensional matrix semigroups. Those criteria support eventual positivity but do not specify the three strongly regular graph entry types, their unique positive-time zero, or a globally maximizing coefficient of \(L^2\). Lin and Weng (arXiv:1411.6532, submitted 2014-11-24) give the strongly regular Laplacian spectral formula and study extremal eigenvalue bounds, not mixed-heat positivity horizons. Gregorio and Mugnolo (arXiv:1712.07370, submitted 2017-12-20) study pure graph bi-Laplacian semigroups; their Section 2 determines non-positivity of pure bi-Laplacian heat on noncomplete connected graphs but not the mixed all-coupling delay optimization in (2).

Existing results on complete multipartite graphs are contained as a proper subclass of the present strongly regular domain only when the multipartite parts are equal; earlier perturbative results for diameter-two graphs concern the small-coupling limit rather than exact all-coupling optimality. The present theorem also covers primitive strongly regular graphs such as the Petersen and Paley graphs. Nearby results on rational Padé graph updates use a different time-discretized operator, so their positivity thresholds do not imply (1) or (2).

## Limitations

The theorem assumes unweighted, finite, connected, noncomplete strongly regular graphs and positive coupling. The zero-coupling ordinary heat flow is positive at every positive time and is not included in the uniqueness statement. No result for arbitrary weighted graphs or for graphs with more than two distinct positive Laplacian eigenvalues follows merely from this proof. Numerical tests check examples only. Bibliographic searches and the inspected papers do not prove absolute historical priority, and related sources not available in full remain a residual comparison risk. Independent mathematical validation has not been performed.

## References

1. D. Daners, J. Glück and J. B. Kennedy, *Eventually and asymptotically positive semigroups on Banach lattices*, arXiv:1511.05294, initial public submission 2015-11-17. https://arxiv.org/abs/1511.05294 ; full text https://ar5iv.labs.arxiv.org/html/1511.05294 .
2. F.-H. Lin and C.-W. Weng, *Strongly Regular Graphs as Laplacian Extremal Graphs*, arXiv:1411.6532, initial public submission 2014-11-24. https://arxiv.org/abs/1411.6532 .
3. F. Gregorio and D. Mugnolo, *Bi-Laplacians on graphs and networks*, arXiv:1712.07370, initial public submission 2017-12-20; relevant Section 2. https://arxiv.org/html/1712.07370v3 .
