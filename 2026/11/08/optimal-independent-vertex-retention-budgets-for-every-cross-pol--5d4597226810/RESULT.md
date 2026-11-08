# Optimal independent vertex-retention budgets for every cross-polytope

## Finding

Let \(n\ge 2\) and let \(v_1,\ldots,v_n\in\mathbb R^n\) be linearly independent. Retain the vertices \(v_i\) and \(-v_i\) of their cross-polytope independently, with probabilities \(p_i^+\) and \(p_i^-\) in \([0,1]\). Write \(Q\) for their random convex hull, assigning zero \(n\)-dimensional volume to the empty hull or a lower-dimensional hull. Then the exact expectation is

\[
\mathbb E\operatorname{Vol}_n(Q)=\frac{|\det(v_1,\ldots,v_n)|}{n!}\left[\prod_{i=1}^n(p_i^++p_i^-)-\prod_{i=1}^n(p_i^++p_i^--2p_i^+p_i^-)\right].
\]

For every fixed expected number \(M=\sum_{i=1}^n(p_i^++p_i^-)\) of retained vertices with \(0<M<2n\), this expectation is **uniquely maximized** over all \(2n\) independent retention probabilities by the uniform design

\[
p_i^+=p_i^-=p=\frac{M}{2n}\qquad(1\le i\le n).
\]

Equivalently, with \(P=\operatorname{conv}\{\pm v_1,\ldots,\pm v_n\}\), the sharp inequality and its exact equality case are

\[
\frac{\mathbb E\operatorname{Vol}_n(Q)}{\operatorname{Vol}_n(P)}\le p^n[1-(1-p)^n],
\]

with equality precisely when all \(2n\) retention probabilities equal \(p\). The optimizer is independent of the cross-polytope's aspect ratios and linear embedding.

## Assumptions and scope

The columns \(v_i\) form an invertible real matrix, \(n\ge2\), and all \(2n\) Bernoulli decisions are mutually independent. The sampling budget is an expectation, not a fixed realized sample size. The condition \(0<M<2n\) excludes forced empty or complete retention. There is no uniformity assumption in the first formula.

## Proof

**Exact expectation.** In standard coordinates, classify each opposite vertex pair into absent, singleton, or complete. If an axis is absent, the hull is lower-dimensional. If every axis is represented but no pair is complete, the hull is an \((n-1)\)-simplex and has zero \(n\)-volume. Otherwise, with \(k\ge1\) complete pairs and all remaining axes singleton, the hull is the union (up to common boundaries) of exactly \(2^k\) coordinate-sign simplices, each of volume \(1/n!\). Hence its volume is \(2^k/n!\). An invertible linear map with columns \(v_i\) multiplies all these volumes by \(|\det(v_1,\ldots,v_n)|\).

Let \(N_i\in\{0,1,2\}\) count retained vertices in pair \(i\). The volume divided by \(|\det(v_1,\ldots,v_n)|/n!\) is exactly \(\prod_iN_i-\mathbf1_{\{N_1=\cdots=N_n=1\}}\): when all axes are nonempty and a pair is complete, the product is \(2^k\); when all are singleton the subtraction removes the spurious unit; otherwise both terms vanish. Independence and \(\mathbb E N_i=p_i^++p_i^-\), \(\mathbb P(N_i=1)=p_i^++p_i^--2p_i^+p_i^-\) yield the claimed formula.

**Optimal balance within each opposite pair.** Set \(s_i=p_i^++p_i^-\in[0,2]\). The singleton probability satisfies

\[
p_i^++p_i^--2p_i^+p_i^-\ge s_i-\frac{s_i^2}{2}
\]

by \(p_i^+p_i^-\le s_i^2/4\). Consequently the expectation is at most \(|\det(v_1,\ldots,v_n)|\Phi(s_1,\ldots,s_n)/n!\), where

\[
\Phi(s_1,\ldots,s_n)=\left(\prod_i s_i\right)\left[1-\prod_i\left(1-\frac{s_i}{2}\right)\right].
\]

**Strict balance across opposite pairs.** Hold every coordinate sum except \(a=s_i\) and \(b=s_j\) fixed, and hold \(a+b=u\) fixed. Put \(B=\prod_{\ell\ne i,j}s_\ell\), \(C=\prod_{\ell\ne i,j}(1-s_\ell/2)\in[0,1]\), and \(t=ab\). Then

\[
\Phi=B\,g(t),\quad g(t)=t\left(1-C+\frac{Cu}{2}-\frac{Ct}{4}\right),\qquad
g'(t)
=1-C+\frac C2(u-t).
\]

For \(0\le a,b\le2\), \(u-t=a+b-ab=1-(a-1)(b-1)\ge0\); the derivative is strictly positive whenever \(a\ne b\). Since replacing \((a,b)\) by \((u/2,u/2)\) increases \(t\) by \((a-b)^2/4\), it strictly increases \(\Phi\) if \(B>0\) and \(a\ne b\). An optimizer cannot have any \(s_i=0\), because that makes \(\Phi=0\), whereas the uniform design has positive expected volume. Thus pairwise balancing proves that the unique maximizing sum vector is \(s_i=M/n\) for every \(i\).

At this vector, \(0<s_i<2\); all other singleton factors are strictly positive. The first balancing inequality is then strict unless every pair is internally balanced. Hence \(p_i^+=p_i^-=M/(2n)\) is the unique optimum. Substituting this vector yields the stated sharp bound. Finally \(\operatorname{Vol}_n(P)=2^n|\det(v_1,\ldots,v_n)|/n!\), giving the normalized form.

## Verification

Execute `python VERIFY.py` with NumPy and SciPy available. The script independently enumerates all \(2^{2n}\) retention masks in dimensions \(n=2,3,4\), determines their convex-hull volumes using the independent Qhull implementation, and averages with nonidentical Bernoulli weights. It compares these with the exact formula for randomly chosen invertible column matrices and probability vectors. It also samples feasible nonuniform allocations for fixed expected budgets in dimensions \(2\le n\le12\) and checks the sharp inequality. The recorded run ended with `CROSSPOLY_HETEROGENEOUS_VOLUME_OPTIMIZATION_CHECKS_PASSED`.

The finite tests are corroborative only. The proof's sign-simplex decomposition and pairwise-balancing derivative establish the all-dimensional statements without numerical reliance.

## Relationship to prior work

Random independent retention of vertices is a standard geometric-probability model. Newman's *Doubly random polytopes* (arXiv:2006.07000, first posted 12 June 2020) explicitly defines the common-probability Bernoulli vertex-subselection model, and studies its facet complexity after a random first polytope. Earlier equal-probability calculations for regular cross-polytopes already give the value attained at uniform retention; that equal-probability case is not claimed here as new. The present theorem instead establishes an exact expectation for **all distinct vertex probabilities** and a strict global optimum under **one fixed total expected sampling budget**, valid for every linearly transformed cross-polytope.

Kabluchko's 2020 analysis of Poisson zero polytopes and spherical random hulls gives different geometric-probability models and does not yield this design inequality. The required comparison is an implication comparison: formulas restricted to the diagonal probability vector do not establish a global inequality over the entire probability cube, much less uniqueness of its maximizer.

## Limitations

The theorem requires independence of the retention indicators. It does not assert optimality for correlated sampling, fixed-size sampling, other polytopes, other intrinsic volumes, or probability-of-success objectives. An equivalent optimization could exist in earlier literature under probability-design or multilinear-extension terminology; historical priority needs independent examination. Independent mathematical audit has not been performed.

## References

1. A. Newman, *Doubly random polytopes*, arXiv:2006.07000, first submitted 12 June 2020, Sections 1–3, https://arxiv.org/abs/2006.07000.
2. Z. Kabluchko, *Expected f-vector of the Poisson zero polytope and random convex hulls in the half-sphere*, Mathematika 66 (2020), 1028–1053, https://doi.org/10.1112/mtk.12056.
3. Standard facts about cross-polytopes, simplices, and volume scaling under invertible linear maps; all required special instances are proved directly above.
