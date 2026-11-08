# Cyclic-interval formula and order-sensitive Minkowski asymmetry of chainlink polytopes

## Finding

For the chainlink polytopes introduced by Kantarcı Oğuz, Özel and Ravichandran, the Minkowski measure of asymmetry has an exact finite barrier formula indexed by proper cyclic intervals and one complete ring. In the notation below,
\[
\mu(K)=\max\left\{\frac{A}{A-s\ell},\max_{1\le i\le s,\,1\le m<s}\frac{A_{i,m}}{A_{i,m}-m\ell}\right\}.
\]
All optimal centers form the explicit feasible polytope in (3) below; in particular they need not be unique. At fixed composition multiset, changing the cyclic order can change the asymmetry: \((4,4,20,20)\) has \(\mu=4/3\), whereas \((4,20,4,20)\) has \(\mu=6/5\), both with \(\ell=2\).

## Assumptions and scope

Let \(s\ge3\), and let \(a_1,\dots,a_s\) and \(\ell\) be positive integers with \(2\ell\le\min_i a_i\). Indices are cyclic modulo \(s\), and
\[
K=\operatorname{CL}(\mathbf a,\ell)=\{x\in\mathbb R^s:0\le x_i\le a_i,\ x_i-x_{i+1}\le a_i-\ell\}.
\]
This polytope is full-dimensional because a constant vector with all entries strictly between zero and the smallest \(a_i\) satisfies each strict difference inequality. Write \(A=\sum_{i=1}^s a_i\) and \(A_{i,m}=a_i+\cdots+a_{i+m}\) (cyclic indices, \(1\le m<s\)). Define
\[
\mu(K)=\inf_{c\in\mathbb R^s}\inf\{\lambda\ge1:-(K-c)\subseteq\lambda(K-c)\}.
\]
Its optimal-center set consists exactly of the \(c\) satisfying
\[
0\le u_i\le(\lambda-1)a_i,\qquad u_i-u_{i+1}\le(\lambda-1)a_i-\lambda\ell,
\quad u_i=(\lambda+1)c_i-a_i,\quad\lambda=\mu(K).\tag{3}
\]

## Proof

**Support extrema.** All coordinate functionals have minimum \(0\) and maximum \(a_i\). For a cyclic difference functional, \(x_i-x_{i+1}\), the maximum is \(a_i-\ell\) by definition and is realized by \(x_i=a_i\), all other coordinates \(\ell\). Its minimum is \(-a_{i+1}\), attained by \(x_{i+1}=a_{i+1}\), \(x_i=0\), and all other coordinates \(\ell\). Every displayed witness is feasible because \(2\ell\le\min a_i\); the construction also applies for \(s=3\). Thus these are actual support extrema, not merely formal right-hand sides.

**Containment into a dilate.** For \(\lambda\ge1\) put \(y=(\lambda+1)c\). The containment \(-(K-c)\subseteq\lambda(K-c)\) is equivalent to \(y-K\subseteq\lambda K\). Applying each of the defining halfspaces, and substituting the exact support extrema, yields
\[
a_i\le y_i\le\lambda a_i,\qquad y_i-y_{i+1}\le\lambda(a_i-\ell)-a_{i+1}.
\]
Writing \(u_i=y_i-a_i\) gives precisely (3). The inequalities are both necessary and sufficient because they test every halfspace in a complete description of \(\lambda K\).

**Cyclic feasibility.** Put \(M_i=(\lambda-1)a_i\) and \(v_i=(\lambda-1)a_i-\lambda\ell\). We seek \(0\le u_i\le M_i\) and \(u_i-u_{i+1}\le v_i\). These are standard difference constraints on vertices \(0,1,\ldots,s\): arcs from \(i+1\) to \(i\) have weight \(v_i\); arcs from \(0\) to \(i\) have weight \(M_i\); arcs from \(i\) to \(0\) have weight zero. The directed graph's simple cycles are exactly: two-arc cycles through \(0\), cycles through \(0\) following a *proper* contiguous run of \(m\) ring arcs, \(1\le m<s\), and the full directed ring (parallel two-arc cases are harmless). The standard shortest-path potential criterion says the constraints have a solution iff every directed cycle has nonnegative total weight. The proper-run cycles yield
\[
M_{i+m}+\sum_{j=0}^{m-1}v_{i+j}=(\lambda-1)A_{i,m}-m\lambda\ell\ge0,
\]
while the whole ring yields \((\lambda-1)A-s\lambda\ell\ge0\). The two-arc cycles require only \(M_i\ge0\), already true. Since \(a_i\ge2\ell\), each denominator \(A_{i,m}-m\ell\) and \(A-s\ell\) is positive. Solving these inequalities for \(\lambda\) yields exactly the claimed maximum. Shortest-path potentials then provide a feasible center for that value, so the lower bound is attained, and (3) lists **every** minimizing center.

**Uniform case.** If all \(a_i=a\), the ring ratio is \(a/(a-\ell)\); every proper interval ratio is smaller because \(m/(m+1)<1\). At this \(\lambda\), each \(v_i=0\), so the ring inequalities force all \(u_i\) equal. The remaining bounds give \(0\le u\le(\lambda-1)a\), exactly the claimed segment of scalar centers. It is nondegenerate when \(\ell>0\).

**Order dependence.** With \(\ell=2\), for \((4,4,20,20)\) the two-small-block interval gives \(8/(8-2)=4/3\), larger than the full-ring \(48/(48-8)=6/5\); direct inspection of the finitely many other interval ratios shows none exceed \(4/3\). For \((4,20,4,20)\) no proper interval has ratio exceeding the ring value \(6/5\). This proves the asserted discrepancy for the same unordered coordinate lengths.

## Verification

Run `python verify_chainlink.py` with NumPy and SciPy installed. The checker enumerates finitely many short compositions, evaluates every exact fraction in the interval formula, independently computes true support minima and maxima by linear programming against the original halfspace system, and solves the enlarged center/dilation linear program. It also verifies explicit contrasting examples. The finite checker is corroboration; the infinite-dimensional parameter statement follows from the exact difference-constraint proof above.

## Relationship to prior work

Kantarcı Oğuz, Özel and Ravichandran introduced \(\operatorname{CL}(\mathbf a,\ell)\) and the condition \(2\ell\le\min a_i\) in their 2022 preprint [1]. They proved lattice-point and complementary-section symmetry statements, not the Minkowski-asymmetry formula here. Cyclic difference-constraint and negative-cycle feasibility are classical methods [2], used explicitly rather than claimed as new. Related investigations determine a Euclidean *inradius* by cyclic-interval barriers, a different invariant: metric Chebyshev centers do not imply affine Minkowski asymmetry. The contribution is the exact Minkowski formula, all minimizing centers, and the cyclic-order contrast.

## Limitations

The theorem assumes a positive link number satisfying \(2\ell\le\min a_i\), and at least three coordinates. It does not assert a formula outside that range or for fixed-coordinate-sum sections. The full center-polytope inequalities are explicit, but no closed combinatorial face count is claimed. Bibliographic searches cannot exclude an unindexed earlier equivalent potential formulation. Independent mathematical validation has not been carried out.

## References

[1] E. Kantarcı Oğuz, C. Y. Özel, M. Ravichandran, *Chainlink Polytopes and Ehrhart-Equivalence*, arXiv:2211.08382v1, first posted 2022-11-15; published in *Annals of Combinatorics* 28 (2024), 1141–1166.

[2] Standard shortest-path feasibility characterization of finite systems of difference constraints (negative directed cycles).