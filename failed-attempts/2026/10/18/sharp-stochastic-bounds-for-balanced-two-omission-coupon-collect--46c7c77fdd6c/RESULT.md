# Sharp stochastic bounds for balanced two-omission coupon collection

## Finding
Fix an integer \(n\ge4\). Each independently sampled package contains \(n-2\) distinct coupons selected from the same \(n\)-coupon universe. Write \(p_{ij}\) for the probability that a package omits exactly coupons \(i,j\), for \(1\le i<j\le n\). Assume the **balanced omission condition**
\[
 p_{ij}\ge0,\qquad \sum_{i<j}p_{ij}=1,\qquad
 \sum_{j\ne i}p_{\min(i,j),\max(i,j)}=\frac2n
 \quad(1\le i\le n).
\]
Let \(T_p\) be the number of packages purchased until every coupon has appeared at least once; the package at the stopping time is included. Put \(q=2/n\) and \(M=\binom n2\). Let \(U\) assign equal mass \(1/M\) to all omitted pairs. Define \(L\), unique up to label permutations, as follows:

- For even \(n\), choose a perfect matching on the \(n\) labels and give each of its \(n/2\) edges mass \(q\).
- For odd \(n\), choose a matching on \(n-3\) labels and give each edge mass \(q\); on the remaining three labels choose the three triangle edges with mass \(q/2=1/n\) each.

Then, simultaneously for every balanced law \(p\) and every integer \(k\ge1\),
\[
 \boxed{\Pr(T_L>k)\le\Pr(T_p>k)\le\Pr(T_U>k).}
\]
The two sharp bounds have exact forms
\[
\Pr(T_L>k)=
\begin{cases}
 q^{k-1},& n\text{ even},\\
 q^k\bigl((n+3)/2-3/2^k\bigr),&n\text{ odd},
\end{cases}
\qquad
\Pr(T_U>k)=q^k\left(n-\frac{M}{(n-1)^k}\right).
\]
For every \(k\ge2\), equality on the lower side holds precisely for the described matching (even \(n\)) or matching-plus-triangle (odd \(n\)) constructions, up to a permutation of labels. Equality on the upper side holds precisely for \(p=U\). At \(k=1\), all balanced laws have \(\Pr(T_p>1)=1\).

In particular, the complete stochastic ordering gives the sharp mean bounds
\[
\mathbb E[T_L]\le\mathbb E[T_p]\le\mathbb E[T_U],
\]
where
\[
\mathbb E[T_L]=
\begin{cases}
 1+\dfrac{1}{1-2/n},&n\text{ even},\\
 1+\dfrac{n+3}{n-2}-\dfrac3{n-1},&n\text{ odd},
\end{cases}
\qquad
\mathbb E[T_U]=1+\frac{2n}{n-2}-\frac{M}{M-1}.
\]
The corresponding equality classes for the mean coincide with those for any tail at \(k\ge2\).

## Assumptions and scope
Draws are independent and identically distributed. Within a package all \(n-2\) labels are distinct. The only admissibility restriction on pair probabilities is the exact common one-label omission marginal \(2/n\), with zeros permitted; there is no assumption of exchangeability or equal joint omission probabilities. The theorem covers every integer \(n\ge4\) and all balanced probability vectors, including their boundaries. It is a comparison of full collection-time laws **within** this constrained balanced class. It does not assert the same extrema among arbitrary, unbalanced package laws or for different package sizes.

## Proof
**1. Exact survival identity.** For \(k\ge1\), let \(A_i(k)\) be the event that coupon \(i\) was omitted on all \(k\) draws. Independence and balance give \(\Pr(A_i(k))=q^k\). For \(i\ne j\), the simultaneous event \(A_i(k)\cap A_j(k)\) requires the exact omitted pair \(\{i,j\}\) on every draw, and has probability \(p_{ij}^k\). Three distinct coupons cannot simultaneously be missing after even one draw, so every intersection of at least three events is empty. Inclusion-exclusion therefore gives, with no approximation,
\[
 \boxed{\Pr(T_p>k)=nq^k-\sum_{i<j}p_{ij}^k.}\tag{1}
\]
At \(k=1\), the right-hand side is \(2-1=1\). This also directly shows the collection time is finite almost surely because every individual coupon is seen on each draw with probability \(1-q>0\).

**2. Sharp upper tail.** For each integer \(k\ge2\), strict convexity of \(t\mapsto t^k\), or Jensen's inequality applied to the \(M\) pair masses, gives
\[
 \sum_{i<j}p_{ij}^k\ge M\left(\frac1M\right)^k,
\]
with equality exactly when all pair probabilities are equal. Substitute into (1) and use \(1/M=q/(n-1)\) to obtain the displayed \(U\) tail, with its sharp equality assertion.

**3. Vertices of the balanced polytope.** Write \(w_{ij}=p_{ij}/q\). The balance constraints reduce to
\[
 \mathcal P_n=\left\{w\ge0:\sum_{j\ne i}w_{\min(i,j),\max(i,j)}=1\ \text{for every }i\right\}.
\]
This is a nonempty compact convex polytope. At a vertex, the columns of the **unsigned** vertex-edge incidence matrix corresponding to positive-weight edges must be linearly independent: a dependence vector supported only on strictly positive coordinates would permit distinct feasible perturbations \(w\pm\epsilon h\) for sufficiently small \(\epsilon>0\).

Consider a connected component of the positive-support graph. If it has a vertex of support degree one, the unique incident edge has weight one. The other endpoint then has no other positive edge; thus the component consists of an isolated edge with weight one. Every remaining component has minimum degree at least two. Column independence forces its number of edges to be at most its number of vertices, while the degree sum forces the reverse inequality. Hence each vertex has degree exactly two, so the component is a cycle. An even cycle has a nonzero alternating signed kernel vector for its unsigned incidence columns and is therefore excluded. Every remaining component is an odd cycle; its balance equations force every edge weight to equal one half. Conversely, each disjoint union of weight-one isolated edges and weight-one-half odd cycles has independent positive incidence columns (successively eliminate isolated edges and note that a homogeneous unsigned incidence system on an odd cycle has only the zero solution), so these are exactly the vertices of \(\mathcal P_n\).

**4. Sharp lower tail.** For \(k\ge2\) the function \(F_k(w)=\sum_{i<j}w_{ij}^k\) is strictly convex. A maximizer on a compact polytope must be a vertex: otherwise it would be a nontrivial convex combination of distinct feasible points, for which strict convexity makes its value strictly less than the larger endpoint value. If a vertex has \(r\) total vertices in odd-cycle components, then it has \((n-r)/2\) isolated edges and
\[
 F_k(w)=\frac{n-r}{2}+\frac{r}{2^k}
 =\frac n2-r\left(\frac12-\frac1{2^k}\right).
\]
Since \(k\ge2\), this decreases strictly with \(r\). If \(n\) is even, the smallest possible \(r\) is zero, attained exactly by perfect matchings. If \(n\) is odd, \(r\) must be odd and at least three, attained exactly by a single triangle together with a matching on the other \(n-3\) vertices. Strict convexity excludes all nonvertices from attaining the same maximum. Multiplying by \(q^k\), inserting into (1), and simplifying gives the two stated \(L\) tails and precisely their equality cases. This establishes stochastic ordering at every positive integer time.

**5. Expectations and strictness.** For nonnegative integer-valued \(T_p\), \(\mathbb E T_p=1+\sum_{k\ge1}\Pr(T_p>k)\). All tails decay geometrically by (1), so the series converges. Summing the exact expressions for \(L\) and \(U\) as geometric series gives the displayed means. The strict tail inequalities at \(k=2\) for every nonextremal law show the same extremal equality classes for expectations.

## Verification
The standalone standard-library script `checker.py` uses `fractions.Fraction` and performs 384 exact rational assertions for \(4\le n\le9\). It verifies balance, sharp symbolic-formula evaluations, strict inequalities for interior mixtures, and independently enumerates all omitted-edge sequences of lengths one through three for \(4\le n\le7\), checking the survival identity directly. It also verifies the closed-form means against geometric-series evaluation. Run `python checker.py` in a directory containing this file. These finite calculations are checks of the formulas; the proof above, not finite experimentation, establishes the universal \(n,k,p\) assertion.

## Relationship to prior work
Betken and Thäle's group-drawing coupon collector study, first public as arXiv:2202.07485 on 15 February 2022, studies uniform group sampling and quantitative asymptotic Gaussian and Poisson approximation of missing-coupon counts. The present statement instead fixes fairness marginals, allows arbitrary dependent omitted pairs, and provides a sharp exact finite-sample stochastic sandwich and all optimizers.

Falgas-Ravry, Larsson and Markström (arXiv:1601.04455, 2016) develop general balanced structured coupon-collector coverage and concentration criteria. Their principal estimates are asymptotic and do not give the present finite-sample equality classes or a complete two-sided stochastic-order envelope for packages omitting exactly two labels.

Schilling (2021) studies how uniform package laws affect mean collection time, proving uniform mean optimality for packages of size \(n-1\) and conjecturing nonoptimality for smaller packages. Berend and Sher (arXiv:2509.17201, 2025) subsequently proved that conjecture about **unrestricted expected time**, constructing nonuniform improvements. Neither statement entails a complete two-sided stochastic order **inside the balanced class**; the general class permits uneven one-label marginals. Fang and Chang (2014) prove a stochastic-optimality result for packages of half the coupon universe, which intersects the current \(n-2\) package size only at \(n=4\); that particular boundary case is previously covered, not presented as a separate innovation. The novel content asserted here is the all-\(n\) balanced-law extremal classification, especially the odd matching-plus-triangle structure and the sharp upper/lower ordering for every horizon.

## Limitations
The result makes no general optimality claim among unbalanced laws or for package sizes other than \(n-2\). The 2014 half-package boundary case \(n=4\) is known. Potential coverage by a differently named classical group-drawing or fractional-matching formula remains an originality risk. A relevant 2021 journal article could be assessed from its abstract but its full text was not retrieved, so no claim of whole-document noncoverage is made. No independent audit is asserted.

## References
1. C. Betken and C. Thäle, *Approaching the coupon collector's problem with group drawings via Stein's method*, arXiv:2202.07485 (first posted 15 February 2022); *Journal of Applied Probability* **60** (2023), 1352–1366, DOI: 10.1017/jpr.2023.6. Primary MSC2020: 60C05.
2. J. Schilling, *Results and conjectures on the role of the uniform distribution in the coupon collector's problem with group drawings*, *Information Processing Letters* **169** (2021), 106112, DOI: 10.1016/j.ipl.2021.106112.
3. D. Berend and T. Sher, *On a Conjecture of Schilling Regarding the Coupon Collector's Problem*, arXiv:2509.17201, first posted 21 September 2025. Published as *On a conjecture on uniform group drawings in the coupon collector problem*, *Stochastic Models* (2026), DOI: 10.1080/15326349.2026.2671340.
4. C. Fang and E.-C. Chang, *Optimal strategy of coupon subset collection when each package contains half of the coupons*, *Information Processing Letters* **114** (2014), 703–705, DOI: 10.1016/j.ipl.2014.06.012.
5. V. Falgas-Ravry, J. Larsson and K. Markström, *Speed and concentration of the covering time for structured coupon collectors*, arXiv:1601.04455 (18 January 2016); *Advances in Applied Probability* **52** (2020), 433–462, DOI: 10.1017/apr.2020.5.
