# Reentrant clique grounding and a three-quarter-power imbalance law on complete split networks

## Finding
Let \(p,q\ge2\) be integers, and let \(G_{p,q}=K_p\vee\overline{K_q}\) have unit-conductance edges. For any \(B>0\), minimize
\[
J(g)=\operatorname{tr}\!\left[(L(G_{p,q})+\operatorname{diag}(g))^{-1}\right],
\qquad g_i\ge0,\quad \sum_i g_i=B.
\]
There is exactly one minimizer. All \(p\) clique vertices get the same gain \(a_*\ge0\), all \(q\) independent-set vertices get the same gain \(b_*>0\), and \(pa_*+qb_*=B\).

Define the dimensionless budget \(t=B/(pq)\) and
\[
\alpha=\frac{q(q-1)}p,\qquad
\beta=1+\frac{q^2(p-1)}{(p+q)^2},\qquad
F_{p,q}(t)=\frac{\alpha}{(1+t)^2}-\beta-\frac2t.
\]
Then the *exact complete support criterion* is
\[
\boxed{a_*=0\quad\Longleftrightarrow\quad F_{p,q}(t)\ge0.}
\]
Put
\[
t_0=\frac{2}{1+\sqrt{1+4\beta}},\qquad
\Gamma(\beta)=\frac{(1+t_0)^3}{t_0^2}.
\]
If \(\alpha<\Gamma(\beta)\), every budget has \(a_*>0\). At equality the clique gains vanish only at \(B=pqt_0\). If \(\alpha>\Gamma(\beta)\), there are exactly two positive roots \(t_-<t_+\) of \(F_{p,q}(t)=0\): the clique gains are zero exactly for \(pq t_-\le B\le pq t_+\), and positive below and above this interval. Thus the clique can be optimally grounded, abandoned, and grounded again as the budget grows.

The smallest independent-class size at which this occurs for \(p=2\) is \(q=6\). There the two thresholds are \(B_\pm=12t_\pm\), where the positive roots \(t_\pm\) of
\[
25t^3+82t^2-151t+32=0
\]
are approximately \(0.2477791964\) and \(1.1131220841\).

There is a sharp *network-size* crossover. If \(p\to\infty\) and \(q/p^{3/4}\to c\in(0,\infty)\) with \(c\ne\sqrt2\), then sufficiently large networks exhibit a nonempty clique-abandonment budget interval if and only if \(c>\sqrt2\). With fixed \(p\) and \(q\to\infty\), the two transition budgets satisfy
\[
\boxed{B_-\sim\frac{2p^2}{q},\qquad B_+\sim q^2.}
\]

## Assumptions and scope
The graph is simple and connected; every existing edge has conductance one. All vertex gains are independent nonnegative decision variables, with one fixed **total sum**, not one fixed number of leaders. The inverse-trace objective is twice the total stationary variance for unit-intensity independent white-noise-driven first-order grounded consensus. The exact support criterion holds for every real \(B>0\) and every integer \(p,q\ge2\). The size crossover assumes a joint limit with \(q/p^{3/4}\to c\) and excludes the unresolved boundary layer \(c=\sqrt2\). The fixed-\(p\) budget asymptotics are a separate limit.

## Proof
**1. Strict convexity and symmetry.** For any feasible \(g\), connectedness and \(B>0\) imply \(A=L+\operatorname{diag}(g)\succ0\). Along any nonzero diagonal perturbation \(D\),
\[
\frac{d^2}{ds^2}\operatorname{tr}(A+sD)^{-1}\bigg|_{s=0}
=2\operatorname{tr}(A^{-1}DA^{-1}DA^{-1})
=2\|A^{-1/2}DA^{-1}\|_F^2>0.
\]
The feasible simplex is compact and the objective continuous, so the minimizer exists and is unique. Every permutation of the clique vertices and every independent permutation of peripheral vertices is a graph automorphism. Uniqueness forces constant gains \(a\) and \(b\) on those two vertex orbits.

**2. Exact objective.** On the clique contrast subspace the grounded Laplacian has eigenvalue \(p+q+a\) with multiplicity \(p-1\); on the independent-class contrast subspace it has eigenvalue \(p+b\) with multiplicity \(q-1\). On normalized partwise constants the matrix is
\[
M=\begin{pmatrix}q+a&-\sqrt{pq}\\-\sqrt{pq}&p+b\end{pmatrix},
\quad\det M=pa+qb+ab,
\quad\operatorname{tr}M=p+q+a+b.
\]
Consequently the exact scalar objective is
\[
\Phi(a,b)=\frac{p-1}{p+q+a}+\frac{q-1}{p+b}
+\frac{p+q+a+b}{pa+qb+ab}.
\]
With \(b=(B-pa)/q\), minimize the strictly convex function \(f_B(a)=\Phi(a,(B-pa)/q)\) on \(0\le a\le B/p\).

**3. Exclusion of ungrounded periphery.** Direct differentiation at the right endpoint gives
\[
f_B'(B/p)=\frac{N}{Bp(B+p(p+q))^2},
\]
where
\[
N=B^3+2p(p+q+1)B^2+p^2\bigl(q^2+2pq+4q+5p\bigr)B+2p^3(p+q)^2>0.
\]
Therefore the right endpoint cannot minimize; \(b_*>0\) for every admissible parameter choice.

**4. Exact clique-abandonment criterion.** At the left endpoint, using \(t=B/(pq)\), differentiation and simplification give
\[
q^2 f_B'(0)=\frac{q(q-1)}{p(1+t)^2}
-\left(1+\frac{q^2(p-1)}{(p+q)^2}\right)-\frac2t=F_{p,q}(t).
\]
A differentiable strictly convex function on a compact interval minimizes at its left endpoint exactly when its right derivative there is nonnegative. This proves the biconditional, including equality.

**5. Number of support transitions.** Since \(t>0\), \(F_{p,q}(t)\ge0\) is equivalent to
\[
\alpha\ge h_\beta(t),\qquad h_\beta(t)=(\beta+2/t)(1+t)^2.
\]
The derivative is \(h_\beta'(t)=2(1+t)(\beta t^2+t-1)/t^2\). Thus \(h_\beta\) decreases strictly up to the unique positive zero \(t_0=2/(1+\sqrt{1+4\beta})\), and then increases strictly; it diverges at both endpoints \(0\) and infinity. Using \(\beta t_0^2+t_0=1\), its minimum is \(h_\beta(t_0)=(1+t_0)^3/t_0^2=\Gamma(\beta)\). The three claimed regimes and uniqueness of both transition roots follow without numerical assumptions. For \(p=2\) and \(q\le5\), we have \(\alpha\le10\), while \(\beta\ge1\) implies \(\Gamma(\beta)\ge\Gamma(1)=(11+5\sqrt5)/2>10\), so reentrance is impossible. For \((p,q)=(2,6)\), \(F_{2,6}(1/2)=53/48>0\); the support inequality reduces exactly to \(25t^3+82t^2-151t+32\le0\), proving the minimal-size witness.

**6. Sharp size crossover.** Take \(q/p^{3/4}\to c\in(0,\infty)\). Algebra gives
\[
\alpha\sim\beta\sim c^2p^{1/2},\qquad
\alpha-\beta=2c^3p^{1/4}+o(p^{1/4}).
\]
The exact defining identity \(\beta t_0^2+t_0=1\) implies \(t_0=\beta^{-1/2}+O(\beta^{-1})\) and
\[
\Gamma(\beta)-\beta=\frac4{t_0}+3+t_0
=4\sqrt\beta+O(1)=4cp^{1/4}+o(p^{1/4}).
\]
Therefore
\[
\alpha-\Gamma(\beta)
=2c(c^2-2)p^{1/4}+o(p^{1/4}).
\]
Its eventual sign proves the threshold \(c=\sqrt2\). No assertion is made at that limiting boundary.

**7. Fixed-clique budget scales.** For fixed \(p\) and \(q\to\infty\), \(\alpha\sim q^2/p\) and \(\beta\to p\), so \(\alpha>\Gamma(\beta)\) for large \(q\). The two roots obey \(t_-\to0\), \(t_+\to\infty\). At the small root, \(\alpha/(1+t_-)^2=\beta+2/t_-\) gives \(t_-\sim2/\alpha\sim2p/q^2\). At the large root, the same equality gives \(t_+\sim\sqrt{\alpha/\beta}\sim q/p\). Multiplication by \(pq\) yields the two budget asymptotics. 

## Verification
Run `python3 verify.py` in the directory containing this file. It uses the Python standard library and independently inverts exact rational grounded Laplacians (not the two-class eigenvalue formula), differentiates using the exact inverse-square diagonal, compares the derived formula and all endpoint signs, checks the concrete cubic and selected phase regimes, and tests the asymptotic size crossover away from its critical layer. The run reported 712 passed assertions. Finite tests do not prove the all-size statements; steps 1–7 are the analytic proof.

## Relationship to prior work
Lin, Fardad and Jovanović [1] formulate and convexly relax noisy-leader selection using inverse-grounded-Laplacian trace, but optimize Boolean leader choices and do not provide this all-budget split-network allocation or the three-quarter-power threshold. Fitch and Leonard [2] analyze centrality and placement of finitely many equal-gain/noise-free leaders, rather than independently adjustable continuous gains. A published exact result on balanced split graphs [3] determines the numbers of *noise-free* leaders in two parts as a function of an integer leader budget; its square-root leader-count migration does not imply the present finite-gain, positive-real-budget reentrance or the different network-size threshold. Standard convexity and spectral reductions are existing tools; the asserted contribution is the explicit two-parameter support criterion, its phase classification, and its sharp size crossover.

## Limitations
This result assumes homogeneous unit graph-edge conductances, a linear sum of nonnegative gains, and isotropic noise. It does not establish an optimal allocation under actuator-price heterogeneity or limited leader cardinality. The asymptotic sign result excludes the critical scaling constant itself; it does not claim the exact first integer \(q\) at which reentrance occurs for arbitrary \(p\). A literature and database comparison can miss an equivalent differently phrased result; this work has not received independent validation.

## References
1. F. Lin, M. Fardad and M. R. Jovanović, *Algorithms for Leader Selection in Stochastically Forced Consensus Networks*, arXiv:1302.0450, first publicly posted 2013-02-03. https://arxiv.org/abs/1302.0450
2. K. Fitch and N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569, first publicly posted 2014-07-07. https://arxiv.org/abs/1407.1569
3. *A square-root migration law for optimal noise-free leaders on balanced split networks*, published research record, 2026-11-08. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-square-root-migration-law-for-optimal-noise-free-leaders-on-ba--fe1c9ab36e72
