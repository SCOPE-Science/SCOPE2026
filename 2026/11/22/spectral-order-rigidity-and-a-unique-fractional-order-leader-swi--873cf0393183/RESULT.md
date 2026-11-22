# Spectral-order rigidity and a unique fractional-order leader switch on complete split networks

## Finding
Let \(p,q\ge2\) be integers and let \(G_{p,q}=K_p\vee\overline{K_q}\) be the unweighted complete split graph, with a clique \(C\) of size \(p\) and an independent set \(I\) of size \(q\). For every real \(r\ge1\), select exactly two distinct perfectly grounded leaders \(S\) to minimize
\[
\Phi_r(S)=\operatorname{tr}\bigl(L_{FF}(S)^{-r}\bigr)
=\sum_{j=1}^{p+q-2}\lambda_j(L_{FF}(S))^{-r},\qquad F=V(G_{p,q})\setminus S.
\]
Here \(L\) is the *combinatorial* Laplacian with unit edge conductances and \(L_{FF}\) is the principal follower submatrix. All possible optimal leader sets are as follows.

1. If \(q=2\), the **only** minimizer is \(S=I\), for every \(r\ge1\).
2. If \((p,q)=(2,3)\), there is a unique \(\rho\in(1,2)\) solving
\[
2^\rho+2^{-\rho}+(2/5)^\rho=3,
\qquad \rho=1.1293316509672375\ldots.
\]
For \(1\le r<\rho\), the minimizers are exactly the \(\binom32=3\) pairs lying in \(I\); at \(r=\rho\), those three pairs and the unique pair \(C\) all minimize; for \(r>\rho\), only the clique pair minimizes.
3. If \(p=2\), \(q\ge4\), and \(r=1\), every clique pair and every mixed clique–independent pair minimizes, and no independent–independent pair does. There are \(1+2q\) minimizers. For \(r>1\), only the clique pair minimizes.
4. If \((p,q)=(3,3)\) and \(r=1\), precisely the three clique pairs and three independent pairs minimize. For \(r>1\), precisely the three clique pairs minimize.
5. In every remaining case with \(q\ge3\), **exactly** the \(\binom p2\) clique pairs minimize for all \(r\ge1\).

Thus the preference for clique leaders is stable through *all* integer and noninteger spectral orders \(r\ge1\), except for one minimal split graph, \(G_{2,3}\), where a genuine fractional-order switch occurs. This result also identifies all boundary ties, including first-order ties that disappear immediately for \(r>1\).

## Assumptions and scope
All graph edges have fixed weight one; both vertex classes contain at least two vertices. Leader nodes are perfectly pinned; noise is applied only to followers. The trace power is defined by functional calculus for the positive definite grounded Laplacian. The mathematical conclusion concerns the explicitly specified spectral objective for every real \(r\ge1\); for \(r=1\) it is proportional to stationary first-order leader–follower consensus variance under isotropic disturbance, and for \(r=2\) it is the inverse-square spectral proxy used in second-order noisy-coherence design. No claim is made that arbitrary fractional \(r\) represents a particular physical dynamics, or that conclusions extend to finite feedback gains or nonunit weights.

## Proof
**1. Exact spectra of the three leader orbits.** Put \(N=p+q\), and let \(a=|S\cap C|\in\{0,1,2\}\). The remaining numbers are \(u=p-a\) clique vertices and \(v=q-2+a\) independent vertices. Graph automorphisms permute vertices freely inside each class, so every leader pair belongs to exactly one of these three orbit types. In the ordering by vertex class,
\[
L_{FF}(a)=\begin{pmatrix}NI_u-J_u&-J_{u,v}\\-J_{v,u}&pI_v\end{pmatrix}.
\]
For \(u,v>0\), the within-class contrast modes have eigenvalues \(N\) with multiplicity \(u-1\) and \(p\) with multiplicity \(v-1\). The remaining two eigenvalues \(\lambda_-^{(a)}<\lambda_+^{(a)}\) belong to
\[
B_a=\begin{pmatrix}q+a&-\sqrt{uv}\\-\sqrt{uv}&p\end{pmatrix},\quad
\lambda_-^{(a)}+\lambda_+^{(a)}=N+a,\quad
\lambda_-^{(a)}\lambda_+^{(a)}=D_a=2p+a(q-2+a).
\]
If \(u=0\) or \(v=0\), the corresponding empty block is omitted; the formulas below incorporate those cases directly. Each grounded matrix is positive definite, since every nonempty follower component touches a leader in a connected graph.

Write \(X_a\) for the decreasing list of reciprocal eigenvalues of \(L_{FF}(a)\). The *clique–clique* orbit \(a=2\) has the particularly simple spectrum
\[
X_2=\left(\frac12,\underbrace{\frac1p,\ldots,\frac1p}_{q-1},\underbrace{\frac1N,\ldots,\frac1N}_{p-2}\right),
\]
because \(\lambda_-^{(2)}=2\) and \(\lambda_+^{(2)}=N\). For \(q\ge3\), the other two decreasing lists are
\[
\begin{aligned}
X_1&=\left(\frac1{\lambda_-^{(1)}},\underbrace{\frac1p,\ldots,\frac1p}_{q-2},\frac1{\lambda_+^{(1)}},\underbrace{\frac1N,\ldots,\frac1N}_{p-2}\right),\\
X_0&=\left(\frac1{\lambda_-^{(0)}},\underbrace{\frac1p,\ldots,\frac1p}_{q-3},\frac1{\lambda_+^{(0)}},\underbrace{\frac1N,\ldots,\frac1N}_{p-1}\right).
\end{aligned}
\]
Indeed, both quotient matrices have positive off-diagonal coupling, hence \(\lambda_-^{(a)}<p<\lambda_+^{(a)}\). Evaluating their characteristic polynomials at \(2\) gives \(1-q<0\) for \(a=1\), and \(4-2q<0\) for \(a=0\); thus the small eigenvalue lies below \(2\). In addition, \(\lambda_-^{(1)}>1\): its polynomial at \(1\) equals \(p-1>0\), while its large root exceeds \(p\ge2\). Consequently \(\lambda_+^{(1)}=N+1-\lambda_-^{(1)}<N\). For \(a=0\), \(\lambda_+^{(0)}=N-\lambda_-^{(0)}<N\). These facts justify the displayed ordering, even in the cases \(p=2\) where some entries tie.

**2. Weak reciprocal-spectrum majorization.** For decreasing vectors \(x,y\) of equal length, write \(x\preceq_w y\) when every leading partial sum of \(x\) is no larger than the corresponding partial sum of \(y\). The Hardy–Littlewood–Pólya weak-majorization principle says that for every continuous increasing convex \(h\),
\[
x\preceq_w y\ \Longrightarrow\ \sum_j h(x_j)\le\sum_j h(y_j).
\]
For \(h(t)=t^r\), \(r>1\), the inequality is strict whenever the sorted vectors differ. This strictness follows, for example, from the integral representation of convex functions by positive weighted upper-tail functions and the strict convexity of \(t^r\). For \(r=1\), it becomes an ordinary comparison of full sums.

For \(q\ge3\), subtract the prefix sums of \(X_2\) from those of \(X_1\). For prefix lengths \(1\le k\le q-1\) the difference equals \(1/\lambda_-^{(1)}-1/2>0\); for \(q\le k\le N-2\) it equals
\[
\frac{N+1}{2p+q-1}-\frac12-\frac1p
=\frac{(p-2)(q-1)}{2p(2p+q-1)}\ge0.
\]
Thus \(X_2\preceq_w X_1\). For \(r=1\), equality occurs exactly at \(p=2\); for every \(r>1\) the inequality in spectral objectives is strict.

Similarly, subtracting the prefixes of \(X_2\) from \(X_0\), the differences are respectively
\[
\begin{cases}
1/\lambda_-^{(0)}-1/2>0,&1\le k\le q-2,\\
(q-2)/(2p)>0,&k=q-1,\\
(q-4)/(2p)+1/N,&q\le k\le N-2.
\end{cases}
\]
The last expression is nonnegative for every \(q\ge4,p\ge2\) and for \(q=3,p\ge3\), since at \(q=3\) it reduces to \((p-3)/(2p(p+3))\). In all those cases \(X_2\preceq_w X_0\); equality of the full sums at \(r=1\) occurs only at \(p=q=3\), and strict inequality holds for all \(r>1\). This proves every claimed \(q\ge3\) case except \((p,q)=(2,3)\).

**3. The two-independent-vertex exception.** If \(q=2\), grounding both independent vertices leaves a clique grounded matrix with eigenvalue \(2\) once and \(N\) repeated \(p-1\) times, so
\[
X_0=\left(\frac12,\underbrace{\frac1N,\ldots,\frac1N}_{p-1}\right).
\]
For clique–clique leaders, \(X_2\) is as above with exactly one \(1/p\) entry, hence \(X_0\preceq_w X_2\) with a strict full-sum inequality. For mixed leaders, the two quotient roots satisfy \(1<\lambda_-^{(1)}<2\) and \(p<\lambda_+^{(1)}<N\), while the remaining \(p-2\) eigenvalues equal \(N\). Thus at prefix length one, \(X_1-X_0\) has strictly positive sum difference. At every longer prefix, the difference is the constant
\[
\frac{p+3}{2p+1}-\frac12-\frac1{p+2}
=\frac{p+8}{2(p+2)(2p+1)}>0.
\]
Therefore \(X_0\preceq_w X_1\), strictly for every power \(r\ge1\). This proves that the unique pair \(I\) is optimal for \(q=2\).

**4. The unique fractional transition.** For \((p,q)=(2,3)\), the three reciprocal spectra are
\[
X_0=(1,1/4,1/5),\qquad X_2=(1/2,1/2,1/2),\qquad
X_1=\left(\frac1{3-\sqrt3},\frac12,\frac1{3+\sqrt3}\right).
\]
The already-proved relation \(X_2\preceq_w X_1\) eliminates the mixed orbit for all \(r>1\), and at \(r=1\) the mixed orbit ties \(X_2\) but loses strictly to \(X_0\). For the other two orbits,
\[
\Phi_r(0)-\Phi_r(2)
=1+4^{-r}+5^{-r}-3\cdot2^{-r};
\]
multiplication by \(2^r>0\) reduces its sign to that of \(f(r)=2^r+2^{-r}+(2/5)^r-3\). The function \(f\) is strictly convex on \([0,\infty)\), has \(f(0)=0\), \(f(1)=-1/10<0\), and \(f(2)=141/100>0\). Since its derivative increases strictly, it has exactly one root in \((1,2)\). The sign changes from negative to positive there. The complete classification, including all ties and counts, follows.

## Verification
The standalone script `verify.py` uses exact rational Gauss–Jordan matrix inversion to compare the inverse-power traces from actual grounded matrices against the spectral formulas for all \(2\le p\le7\), \(2\le q\le8\), and integer orders \(r\in\{1,2,3\}\). It checks the complete minimizing orbit sets, plus 50,454 floating-point leading-partial-sum inequalities on a larger parameter grid and a numerical bracket of the exceptional root. The verified invocation is `python3 verify.py`, using only the standard Python library. These tests provide finite corroboration; the universal result for arbitrary graph sizes and all real \(r\ge1\) follows from the exact spectral and majorization proof above.

## Relationship to prior work
Fitch and Leonard [1] derive the established joint-centrality formulation for minimizing the inverse trace of grounded Laplacians in noise-free leader selection, with explicit cycle/path cases; their full arXiv manuscript does not provide the complete-split all-power phase diagram. Patterson and Bamieh [2] establish inverse-squared Laplacian spectral coherence for second-order dynamics, but study ungrounded self-similar network families rather than exact leader sets on split graphs. The previously published study [3] derives a first-order inverse-trace leader-budget migration on **balanced** complete split graphs; its formula applies to \(r=1\) and cannot by itself imply optimality under nonlinear powers \(r>1\), the weak majorization domination, or the unique fractional-order exception on an unequal split graph. The present theorem strengthens the objective comparison to every convex increasing function of the reciprocal grounded eigenvalues in the indicated weak-majorization regimes. Related bipartite and multipartite leader-placement notes concern distinct topologies and mainly the first inverse power. This is a comparison of mathematical claims, not a proof of publication priority.

## Limitations
The result requires exactly two perfectly pinned leaders, unit conductances, \(p,q\ge2\), and real spectral order \(r\ge1\). It does not classify \(0<r<1\), weighted split graphs, arbitrary gain or noise models, or budgets other than two. The location and uniqueness of the exceptional root have an exact analytic proof; its displayed decimal is only a numerical approximation. The finite verifier is not a substitute for the all-size proof. Unindexed or inaccessible mathematical sources may contain equivalent statements; no external audit or independent validation has been undertaken.

## References
1. K. E. Fitch and N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569, first posted 2014-07-07. https://arxiv.org/abs/1407.1569.
2. S. Patterson and B. Bamieh, *Consensus and Coherence in Fractal Networks*, arXiv:1310.2592, first posted 2013-10-09. https://arxiv.org/abs/1310.2592.
3. *A square-root migration law for optimal noise-free leaders on balanced split networks*, publicly available mathematical note, 2026-11-08. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-square-root-migration-law-for-optimal-noise-free-leaders-on-ba--fe1c9ab36e72.
4. A. W. Marshall, I. Olkin and B. C. Arnold, *Inequalities: Theory of Majorization and Its Applications*, 2nd ed., Springer, 2011, weak-submajorization and increasing convex functions, Chapter 3.
