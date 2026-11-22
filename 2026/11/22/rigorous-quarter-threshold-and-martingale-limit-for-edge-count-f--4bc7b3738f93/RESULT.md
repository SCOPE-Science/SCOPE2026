# Rigorous quarter-threshold and martingale limit for edge-count fluctuations in parent-linked duplication graphs

## Finding

Let \(G_n\) grow from one isolated vertex as follows. At time \(n+1\), select a parent uniformly among the \(n\) old vertices, attach the new vertex to the parent with probability \(r\), and independently copy every edge from the parent to one of its old neighbors with probability \(p\). Fix \(0<p<1\) and \(0<r\leq1\). Write \(E_n=|E(G_n)|\) and \(Q_n=\sum_{v\in V(G_n)}\deg(v)^2\), and put \(a_n=\mathbb EE_n\), \(d_n=\mathbb EQ_n\), and \(v_n=\operatorname{Var}(E_n)\).

**Exact closure.** For every integer \(n\geq1\), starting from \(a_1=d_1=v_1=0\),
\[
\begin{aligned}
a_{n+1}&=(1+2p/n)a_n+r,\\
d_{n+1}&=(1+(2p+p^2)/n)d_n+(4r+4p-2p^2+4pr)a_n/n+2r,\\
v_{n+1}&=(1+4p/n)v_n+b_n,\\
b_n&=r(1-r)+2p(1-p)a_n/n+p^2(d_n/n-4a_n^2/n^2)\geq0.
\end{aligned}
\]

Set \(c=r/(1-2p)\), \(D=[2r+(4r+4p-2p^2+4pr)c]/(1-2p-p^2)\), and
\[
\sigma^2=r(1-r)+2p(1-p)c+p^2(D-4c^2)>0,
\]
where these last three constants are used only when \(0<p\leq1/4\).
Then the edge-count variance has the complete sharp trichotomy
\[
\boxed{\begin{cases}
\displaystyle \lim_{n\to\infty}v_n/n=\sigma^2/(1-4p),&0<p<1/4,\\[2mm]
\displaystyle \lim_{n\to\infty}v_n/(n\log n)=\sigma^2,&p=1/4,\\[2mm]
\displaystyle \lim_{n\to\infty}v_n/n^{4p}=C_{p,r}\in(0,\infty),&1/4<p<1.
\end{cases}}
\]
In the last regime, set \(F_n=\prod_{j=1}^{n-1}(1+4p/j)\). Then the nonzero constant has the convergent exact series
\[
C_{p,r}=\frac{1}{\Gamma(1+4p)}\sum_{k=1}^\infty\frac{b_k}{F_{k+1}}.
\]
Moreover, with \(H_n=\prod_{j=1}^{n-1}(1+2p/j)\),
\[
M_n=\frac{E_n-a_n}{H_n}
\]
is a mean-zero martingale. It converges almost surely and in \(L^2\) to a nondegenerate random variable for every \(p>1/4\), with
\[
\operatorname{Var}(M_\infty)=\Gamma(1+2p)^2 C_{p,r}>0.
\]
For \(p\leq1/4\), this particular normalized martingale is not bounded in \(L^2\). These assertions concern variance and martingale convergence, **not** a central limit theorem or the distribution of \(M_\infty\).

## Assumptions and scope

The graph is simple and undirected; the parent is chosen afresh uniformly at each step. The parent-edge mark and all neighbor-copy marks are conditionally independent; existing edges are never deleted. Both probabilities \(p\) and \(r\) are constant in time and satisfy \(0<p<1\), \(0<r\leq1\). The initial graph is a single isolated vertex. All expectations and variances average over the entire history of the graph. Parameters are fixed before \(n\to\infty\). The theorem is about \(\operatorname{Var}(E_n)\) and the specified martingale; it does not assert joint graph convergence.

## Proof

**1. Conditional drift.** At a step from \(n\) to \(n+1\), condition on the old graph and chosen parent \(u\) with degree \(d_u\). If \(A\sim\operatorname{Bernoulli}(r)\) is the parent-edge mark, and the \(d_u\) neighbor-copy marks are independent \(\operatorname{Bernoulli}(p)\) variables, then \(\Delta E=A+\sum B_w\). Averaging the conditional expectation over uniformly chosen \(u\), using \(\sum_u d_u=2E_n\), yields
\[
\mathbb E[\Delta E\mid G_n]=r+2pE_n/n.
\]
This proves the recurrence for \(a_n\) and that \(M_n\) is a martingale.

**2. Degree-square closure.** Conditional on parent \(u\), each old vertex whose degree increases from \(d\) to \(d+1\) contributes \(2d+1\) to \(Q\). The newborn vertex contributes \((A+\sum B_w)^2\). Hence
\[
\mathbb E[\Delta Q\mid G_n,u]=2r+(2r+2p-p^2+2rp)d_u+2p\sum_{w\sim u}d_w+p^2d_u^2.
\]
The identities \(\sum_u\sum_{w\sim u}d_w=Q_n\) and \(\sum_ud_u^2=Q_n\) give the stated recurrence for \(d_n\). No closure assumption or moment factorization is used.

**3. Variance closure and positivity.** Total variance, first conditioning on the parent and its independent marks, gives
\[
\operatorname{Var}(\Delta E\mid G_n)=r(1-r)+2p(1-p)E_n/n+p^2[Q_n/n-(2E_n/n)^2].
\]
The random conditional mean of \(E_{n+1}\) equals \((1+2p/n)E_n+r\). Applying total variance a second time and canceling the \(4p^2v_n/n^2\) terms yields exactly the recurrence for \(v_n\). Since \(Q_n/n\ge(2E_n/n)^2\) pointwise, Jensen's inequality gives \(d_n/n\ge4a_n^2/n^2\), so \(b_n\ge r(1-r)+2p(1-p)a_n/n\ge0\). For \(r=1\), the initially deterministic parent edge makes \(v_2=0\), but \(v_3=p(1-p)>0\); for \(r<1\), \(v_2=r(1-r)>0\).

**4. Subcritical and critical limits.** If \(p\le1/4\), both linear recurrences in Steps 1–2 have characteristic exponents below one: \(2p<1\) and \(2p+p^2<1\). By direct iteration (or division by \(n\) and the elementary convergence lemma for recurrences \(x_{n+1}=(1+\alpha/n)x_n+f_n\) with \(f_n\to f\), \(\alpha<1\)),
\[
 a_n/n\to c,\quad d_n/n\to D,\quad b_n\to\sigma^2.
\]
The limit is strictly positive, since \(2p(1-p)c>0\) and \(D\ge4c^2\). For \(p<1/4\), applying the same recurrence lemma with exponent \(4p<1\) to \(v_n\) gives \(v_n/n\to\sigma^2/(1-4p)\). For \(p=1/4\), multiplying the variance recurrence by \(1/(n+1)\) gives \(v_{n+1}/(n+1)=v_n/n+b_n/(n+1)\), hence the weighted harmonic sum proves \(v_n/(n\log n)\to\sigma^2\).

**5. Supercritical summability.** For fixed \(0<p<1\), the first recurrence yields \(a_n=O(n^{\max(1,2p)}(1+\log n))\). The second, with exponent \(\lambda=2p+p^2\), yields \(d_n=O(n^{\max(1,\lambda)}(1+\log n)^2)\); this follows by iteration and comparison of harmonic/power sums, because \(\lambda>2p\). Dropping the nonpositive term in \(b_n\) gives the bound
\[
0\le b_n=O\bigl(n^{\max(0,\lambda-1)}(1+\log n)^2\bigr).
\]
For \(p>1/4\), \(\lambda<4p\), so the positive series \(\sum_{k\ge1}b_k/F_{k+1}\) converges. The exact variation-of-constants identity
\[
v_n=F_n\sum_{k=1}^{n-1}b_k/F_{k+1}
\]
and \(F_n\sim n^{4p}/\Gamma(1+4p)\) give the asserted limit. Positivity follows from \(v_2>0\) for \(r<1\), or \(v_3>0\) for \(r=1\).

**6. Martingale transition.** The martingale in Step 1 has \(\mathbb EM_n^2=v_n/H_n^2\), with \(H_n\sim n^{2p}/\Gamma(1+2p)\). In the supercritical regime these second moments converge to the displayed positive constant. The \(L^2\)-martingale convergence theorem gives a nondegenerate almost-sure and \(L^2\) limit. At and below the critical point, the proven variance scales make \(v_n/H_n^2\to\infty\), so this martingale is not \(L^2\)-bounded. This does not exclude other normalizations or modes of convergence.

## Verification

The standalone `checker.py` uses only Python's standard library and exact rational arithmetic. It independently enumerates full one-step graph laws for four rational parameter pairs (including the certain-parent case), compares their exact edge-count mean, squared-degree mean and variance against all three recurrences through five vertices, verifies normalization and nonnegative forcing, and compares the \(r=1\) constant with the published 2016 expression at four rational copying probabilities. Its run completed 2,248 exact assertions. Finite checks are sanity tests, not the proof of the infinite limits. Reproduce with `python checker.py`.

## Relationship to prior work

The **quarter transition itself is not new**: Bhat, Krapivsky, Lambiotte and Redner (2016), Sec. II.B and Eqs. (12)–(17), already derived the exact but unclosed variance recurrence for the **certain-parent-edge case \(r=1\)** and anticipated the \(n\), \(n\log n\) and \(n^{4p}\) variance scales using continuum asymptotics. Their explicit coefficient for \(p\le1/4\) agrees algebraically with the present \(\sigma^2\) when \(r=1\). What is proved here is a finite exact closed three-moment system, rigorous asymptotic constants for all \(0<r\le1\) and all \(0<p<1\), and the nondegenerate \(L^2\) martingale limit above the quarter boundary. No priority is claimed for the conjectured quarter boundary or the older \(r=1\) formal asymptotics.

Dey, Maitra, Manthripragada and Terlov (2026) rigorously study this same parent-linked model's degree distribution, local limits and persistent maximum-degree vertices; their stated results do not imply the global edge variance constant or the centered edge-count martingale theorem. Hermann and Pfaffelhuber (2016) proved \(L^2\) convergence of normalized edge counts for **no parent-link immigration \(r=0\)** starting from an edge-containing seed; that process is different from the \(r>0\) model here (whose singleton seed would otherwise remain empty). Turowski and Szpankowski (2021) studied variance of average degree in a *different* duplication-divergence rule that independently adds extra edges to all non-neighbors at rate \(r/n\), not only a new vertex-to-parent link. These differences matter to the conditional moment recurrences.

## Limitations

The \(p=1/4\) threshold and variance scales were previously predicted in the \(r=1\) physics literature, so only the rigorous closure, general parent-link parameter, constants and martingale statement are assessed as additions. This result does not give a Gaussian limit below the boundary, does not identify the supercritical limit's law or higher moments, and does not handle changing parameters or deletion. Statement-level literature comparisons cannot establish universal historical uniqueness; an unindexed rigorous extension of the earlier physics analysis remains a priority risk. The finite checker cannot replace the proof of the asymptotics.

## References

1. P. S. Dey, N. Maitra, J. M. Manthripragada and G. Terlov, *Uniform duplication-divergence random graphs I: Degrees and Local Limits* (2026), arXiv:2611.00123, first public 2026-10-29, https://arxiv.org/abs/2611.00123.
2. U. Bhat, P. L. Krapivsky, R. Lambiotte and S. Redner, *Densification and structural transitions in networks that grow by node copying* (2016), arXiv:1610.01662, especially Sec. II.B, https://arxiv.org/abs/1610.01662.
3. F. Hermann and P. Pfaffelhuber, *Large-scale behavior of the partial duplication random graph* (2016), arXiv:1408.0904, https://arxiv.org/abs/1408.0904.
4. K. Turowski and W. Szpankowski, *Towards Degree Distribution of a Duplication-Divergence Graph Model*, Electron. J. Combin. 28 (2021), P1.18, https://doi.org/10.37236/9251.
