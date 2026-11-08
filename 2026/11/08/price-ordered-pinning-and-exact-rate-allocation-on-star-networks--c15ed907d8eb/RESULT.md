# Price-ordered pinning and exact rate allocation on star networks

## Finding

Let \(m\ge 2\) be an integer. On the unit-conductance star \(K_{1,m}\), label the hub \(0\), the leaves \(1,\dots,m\), and let \(L\) be its ordinary combinatorial Laplacian. Fix strictly positive actuator prices \(p_0,p_1,\dots,p_m\) and budget \(B>0\). All individual nonnegative gains \(u_i\) are adjustable, with total price \(\sum_{i=0}^m p_i u_i\le B\). Define the optimal decay rate

\[
 r(B)=\max_{u_i\ge0,\;\sum_{i=0}^m p_i u_i\le B}
 \lambda_{\min}\!\left(L+\operatorname{diag}(u_0,\dots,u_m)\right).
\]

The maximizer exists, is **unique**, and spends the entire budget. It can be calculated using only two scalar monotone root solves, with no matrix optimization. For any proposed rate \(\lambda>0\), set

\[
 t_i(\lambda,\alpha)=\max\left\{1-\lambda,\sqrt{\alpha/p_i}\right\},\qquad
 g_\lambda(\alpha)=\lambda-m+\sum_{i=1}^m t_i(\lambda,\alpha)^{-1}
 \quad(0<\alpha\le p_0).
\]

Define \(\alpha_\lambda=p_0\) when \(g_\lambda(p_0)\ge0\); otherwise \(\alpha_\lambda\) is the unique root of \(g_\lambda(\alpha)=0\) in \((0,p_0)\). Write \(t_i=t_i(\lambda,\alpha_\lambda)\). The **unique minimum-cost gains attaining rate at least \(\lambda\)** are

\[
 u_i(\lambda)=t_i+\lambda-1\quad(1\le i\le m),\qquad
 u_0(\lambda)=\max\left\{0,\lambda-m+\sum_{i=1}^m t_i^{-1}\right\}.
\]

Let \(F(\lambda)=p_0u_0(\lambda)+\sum_{i=1}^m p_i u_i(\lambda)\). Then \(F\) is continuous, strictly increasing from \(F(0)=0\) to infinity, and

\[
 \boxed{r(B)\text{ is the unique positive root of } F(\lambda)=B.}
\]

As the budget grows, leaf actuators enter **in increasing price order**, with ties entering simultaneously; no active leaf subsequently switches off. The hub also activates at most once and never switches off. For all

\[
 \lambda\ge\Lambda_0:=\max\left\{1,\;m-\sum_{i=1}^m\sqrt{p_i/p_0}\right\},
\]

all leaves are active and the hub is nonnegative, and the exact high-rate cost law becomes affine:

\[
 \boxed{F(\lambda)=\left(p_0+\sum_{i=1}^m p_i\right)\lambda
 -mp_0-\sum_{i=1}^m p_i+2\sqrt{p_0}\sum_{i=1}^m\sqrt{p_i}.}
\]

The inverse rate curve \(r(B)\) is increasing and concave, becoming exactly affine beyond \(F(\Lambda_0)\).

In the important two-price case \(p_0=P\), \(p_1=\dots=p_m=Q\), define \(R=\sqrt{P/Q}\). If \(P<Q\), initially only the hub is controlled, up to rate \(1-R\); if \(P>Q\), initially only the leaves are controlled, up to rate \(m(1-R^{-1})\). Above that point both classes are controlled. In the final phase the gains are exactly

\[
 u_0=\lambda-m+m/R,\qquad u_1=\cdots=u_m=\lambda-1+R.
\]

For \(P=Q\), all \(m+1\) gains equal \(B/[P(m+1)]\) at every positive budget.

## Assumptions and scope

All vertices have unit masses and the \(m\) undirected star edges have fixed conductance one. The performance index is the smallest eigenvalue of the **diagonally pinned Laplacian** and hence the asymptotic exponential rate of \(\dot z=-(L+\operatorname{diag}u)z\). All gains can be zero, although a positive-budget optimum is not identically zero. Prices are linear, strictly positive, and arbitrary across leaves. Nothing here optimizes the largest-to-smallest eigenvalue ratio, uses hard-grounded nodes, changes edge conductances, or applies to a general graph without its star structure. The spectral-rate result for scalar linear pinned consensus does not by itself establish a global nonlinear synchronization guarantee.

## Proof

**1. Exact spectral constraint.** In hub-first order, the matrix \(L+\operatorname{diag}(u)-\lambda I\) has diagonal hub entry \(m+u_0-\lambda\), leaf diagonal entries \(t_i=1+u_i-\lambda\), and hub–leaf entries \(-1\). Positive semidefiniteness forces every \(t_i>0\): if a leaf diagonal were zero, the nonzero hub–leaf entry would contradict positive semidefiniteness of its principal two-by-two block. The Schur complement therefore gives the exact equivalence

\[
 \lambda_{\min}(L+\operatorname{diag}u)\ge\lambda
 \iff t_i>0,\quad t_i\ge1-\lambda,\quad u_0\ge0,
 \quad u_0\ge\lambda-m+\sum_{i=1}^m t_i^{-1}.
\]

The inequality \(u_i\ge0\) is exactly \(t_i\ge1-\lambda\).

**2. Cost duality with no gap.** For fixed \(\lambda>0\), minimize \(p_0u_0+\sum_i p_i(t_i+\lambda-1)\) under the preceding constraints. This is a convex problem: \(t\mapsto t^{-1}\) is strictly convex on positive reals. Strict feasibility is obtained with sufficiently large leaf and hub gains, so Lagrange duality has no gap. Assign multiplier \(\alpha\ge0\) to the hub Schur inequality. Minimizing over \(u_0\ge0\) forces \(0\le\alpha\le p_0\); minimizing the remaining separable terms \(p_i t_i+\alpha/t_i\) over \(t_i\ge1-\lambda\) gives precisely

\[
 t_i(\lambda,\alpha)=\max\{1-\lambda,\sqrt{\alpha/p_i}\}.
\]

For \(\alpha>0\), the derivative of the dual objective in \(\alpha\) equals \(g_\lambda(\alpha)\). This derivative is nonincreasing and becomes strictly decreasing as soon as at least one leaf is interior. Its limit at zero is positive for every \(\lambda>0\): for \(\lambda<1\) it is \(\lambda(m+1-\lambda)/(1-\lambda)\), while for \(\lambda\ge1\) it is infinite. Thus the unique dual maximizer is \(p_0\) if \(g_\lambda(p_0)\ge0\), and otherwise the unique interior root \(g_\lambda=0\). Complementary slackness yields the stated \(u_0,u_i\) and exactly the minimum cost \(F(\lambda)\).

**3. Uniqueness of the allocation.** For each diagonal gain vector, \(L+\operatorname{diag}u\) is a symmetric irreducible \(Z\)-matrix; its smallest eigenvalue is simple with a strictly positive eigenvector. Its derivative in each \(u_i\) is the strictly positive square of the corresponding normalized eigenvector coordinate. Thus a maximizing allocation spends the budget. Suppose two different budget-feasible vectors have the same maximal smallest eigenvalue \(\lambda\). Their midpoint is feasible, and concavity of the smallest eigenvalue gives value at least \(\lambda\). Equality would force its positive lowest eigenvector to be a lowest eigenvector of both endpoint matrices (the two endpoint Rayleigh quotients, each at least \(\lambda\), average to \(\lambda\)); subtracting the eigen-equations then gives \((u_i-v_i)w_i=0\) for every \(i\), hence equality of gains. Strict inequality at the midpoint would contradict maximality. The maximizer and, equivalently, the minimum-cost prescribed-rate allocation are therefore unique.

**4. Inverting the cost.** For \(\lambda>0\), any optimal prescribed-rate gains attain smallest eigenvalue exactly \(\lambda\); otherwise a small reduction of one positive gain lowers cost while retaining rate at least \(\lambda\). Increasing the desired rate strictly increases the minimum cost by the same argument, and parameterized convex optimization supplies continuity. At zero the unique zero-cost allocation has rate zero. As \(\lambda\to\infty\), the leaf diagonal condition implies \(u_i\ge\lambda-1\) and thus \(F(\lambda)\to\infty\). Hence \(F(\lambda)=B\) has exactly one positive solution, and its gains uniquely optimize the budgeted problem. Convexity of \(F\) follows because the set of \((\lambda,c)\) admitting a positive-semidefinite constraint \(L+\operatorname{diag}(u)-\lambda I\succeq0\) and cost at most \(c\) is a convex projection. Its increasing inverse \(r\) is concave.

**5. Activation and terminal affine law.** For fixed \(\alpha>0\), \(g_\lambda(\alpha)\) strictly increases with \(\lambda\), as the term \(\lambda\) increases and all \(t_i\) are nonincreasing until their interior values are reached. Consequently \(\alpha_\lambda\) is nondecreasing with \(\lambda\). At \(\lambda<1\), a leaf is active precisely when \(p_i<\alpha_\lambda/(1-\lambda)^2\); for \(\lambda\ge1\), every leaf is active. This proves the price-ordered irreversible activation. The hub is active precisely when \(g_\lambda(p_0)>0\), another increasing condition. When \(\lambda\ge\Lambda_0\), \(\alpha_\lambda=p_0\), all \(t_i=\sqrt{p_0/p_i}\), and substitution proves the affine identity.

**6. Explicit two-price transition.** With \(R=\sqrt{P/Q}\), the scalar optimum has \(t_i=R\) after all controls become positive. If \(R<1\), its early constraint is \(u_i=0\), whence

\[
 F(\lambda)=P\,\frac{\lambda(m+1-\lambda)}{1-\lambda},
 \quad 0<\lambda\le1-R,
\]

and the switch budget is \(P(1-R)(m+R)/R\). If \(R>1\), its early constraint is \(u_0=0\), whence

\[
 F(\lambda)=mQ\,\frac{\lambda(m+1-\lambda)}{m-\lambda},
 \quad 0<\lambda\le m(1-R^{-1}),
\]

and the switch budget is \(mQ(R-1)(R+m)/R\). Above either boundary, \(F(\lambda)=(P+mQ)\lambda-mP-mQ+2m\sqrt{PQ}\). At \(R=1\), the uniform-gain solution follows directly from the same formula.

## Verification

The complete standard-library script `verify_star.py` separately evaluates the claimed scalar root construction and a separate secular root for the smallest eigenvalue of an arbitrary pinned star. It includes exact rational identities for the two-price branch formula and randomized heterogeneous-price, fixed-budget feasible-comparison and activation tests. On the packaged script, it reports 549 exact rational cases, 400 heterogeneous-price rate/secular checks, 6,000 feasible-competitor comparisons and 7,600 activation comparisons: **14,549 supplemental checks passed**. Exact rational tests cover only selected finite cases; numerical optimization/comparisons are not used to infer the universal theorem. All-parameter validity follows from the Schur, duality and Perron arguments above.

## Relationship to prior work

Li, Duan and Chen introduced cost-based pinning of star networks and proved sufficient spectral conditions for either a common gain at all leaves or one pinned hub; their 2007 manuscript's Section 3, Theorem 1 and Remarks 4–5 do not optimize simultaneously variable hub and independent leaf gains under arbitrary positive prices. Zhou and coauthors formulated a general gain-selection LMI in 2015, with an analytic uniform-weight case and numerical nonuniform allocations; the present scalar formula is an explicit star-only solution, **not** a claim that the general semidefinite formulation is new. Shafi, Arcak and El Ghaoui (2012) optimize node masses and edge weights for Laplacian spectral constraints, a different set of decision variables. Orouskhani, Jalili and Yu (2016) optimize an augmented-Laplacian eigenratio and network structure, not the smallest-eigenvalue objective at fixed positive individual actuator prices. Boyd's 2006 exposition of convex graph-Laplacian eigenvalue design is acknowledged as general background.

## Limitations

The theorem is for a single hub with fixed unit spokes, independent diagonal gains, positive linear prices and a smallest-eigenvalue performance index. It does not handle actuator upper caps, nonlinear costs, spectral-ratio optimization, uncertain topology, nonlinear synchronization dynamics or networks beyond stars. General semidefinite methods predate this result, and a specialist unpublished or inaccessible analytic star allocation theorem could affect publication priority. The verification script gives finite evidence but is not an independent audit or an infinite proof.

## References

- R. Li, Z. Duan and G. Chen, *Cost and Effects of Pinning Control for Network Synchronization*, arXiv:0710.2716, first publicly submitted 2007-10-15; later *Chinese Physics B* 18 (2009), 106–118. https://arxiv.org/abs/0710.2716
- F. Sorrentino, M. di Bernardo, F. Garofalo and G. Chen, *Controllability of complex networks via pinning*, *Physical Review E* 75 (2007), 046103. https://arxiv.org/abs/cond-mat/0701073
- S. Y. Shafi, M. Arcak and L. El Ghaoui, *Graph Weight Allocation to Meet Laplacian Spectral Constraints*, *IEEE Transactions on Automatic Control* 57 (2012), 1872–1877. https://people.eecs.berkeley.edu/~elghaoui/Pubs/Laplace_tac2012.pdf
- M.-Y. Zhou et al., *Enhancing speed of pinning synchronizability: low-degree nodes with high feedback gains*, *Scientific Reports* 5 (2015), 17459. https://pmc.ncbi.nlm.nih.gov/articles/PMC4667188/
- Y. Orouskhani, M. Jalili and X. Yu, *Optimizing Dynamical Network Structure for Pinning Control*, *Scientific Reports* 6 (2016), 24252. https://www.nature.com/articles/srep24252
- S. Boyd, *Convex Optimization of Graph Laplacian Eigenvalues*, ICM 2006, vol. 3, pp. 1311–1319. https://stanford.edu/~boyd/papers/cvx_opt_graph_lapl_eigs.html
