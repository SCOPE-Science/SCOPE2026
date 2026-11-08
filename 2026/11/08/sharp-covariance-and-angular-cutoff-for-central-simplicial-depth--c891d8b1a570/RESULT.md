# Sharp covariance and angular cutoff for central simplicial depth and circular geometric-graph edges

## Finding
Let \(n\ge3\) independent points be uniform on the unit circle, let \(T_n\) count triples whose convex hull contains the center, and let \(E_{n,\alpha}\) count pairs with *shorter* angular distance at most \(\alpha\), where \(0<\alpha<\pi\) and \(q=\alpha/\pi\). Then
\[
\operatorname{Cov}(T_n,E_{n,\alpha})=-\frac{n-2}{4}\binom n2 q(1-q),\qquad
\operatorname{Corr}(T_n,E_{n,\alpha})=-\sqrt{\frac{3(n-2)}n q(1-q)}.
\]
In particular their covariance and correlation are strictly negative. Their correlation is most negative for the **unique** cutoff \(\alpha=\pi/2\), corresponding to Euclidean chord threshold \(\sqrt2\). The optimal correlation is \(-\sqrt{3(n-2)/(4n)}\) and tends to \(-\sqrt3/2\) as \(n\to\infty\).

## Assumptions and scope
Points are independent with uniform arclength distribution on \(\mathbb S^1\). The origin is strictly within the convex hull of three sampled points except on a zero-probability boundary. The number \(T_n\) is the unnormalized central simplicial depth count, using unordered distinct triples. The number \(E_{n,\alpha}\) is the *unnormalized* edge count of the circular threshold graph, using unordered distinct pairs. Shorter angular separation lies in \([0,\pi]\), and its distribution is uniform. Cutoffs \(0\) and \(\pi\) give deterministic edge counts and zero variance, hence no defined Pearson correlation at those endpoints. No assertion concerns points sampled uniformly inside a disk or spheres of dimension above one.

## Proof
Write \(H_{ijk}\) for the indicator that the origin lies in the triangle formed by three fixed sampled points, and \(J_{ab}\) for the indicator that the shorter angular separation of a fixed pair is at most \(\alpha\).

**One and two point conditionings.** Rotation invariance and the elementary hemisphere criterion give \(\mathbb EH_{ijk}=1/4\). Conditional on any one of its points, the triangle indicator also has conditional mean \(1/4\). Fix two points separated by the shorter angle \(\delta\in[0,\pi]\). The third point forms a triangle containing the origin precisely on the antipodal arc subtending angle \(\delta\), hence
\[
\mathbb E(H_{ijk}\mid U_i,U_j)=\frac{\delta}{2\pi}.
\]
As \(\delta\) is uniform on \([0,\pi]\), \(\mathbb EJ_{ij}=q\), and
\[
\mathbb E(H_{ijk}J_{ij})=\frac1\pi\int_0^\alpha\frac{\delta}{2\pi}\,d\delta=\frac{q^2}{4};\qquad
\operatorname{Cov}(H_{ijk},J_{ij})=-\frac{q(1-q)}4.
\]

**The covariance sum.** If a triangle and a pair share no point, independence makes their covariance vanish. If they share exactly one point, conditioning on that point and using rotational invariance of the conditional expectations again makes the covariance vanish. A pair contained in a triple gives the preceding \(-q(1-q)/4\). There are exactly \(3\binom n3=(n-2)\binom n2\) such incidences, proving the covariance formula.

**Individual variances.** Two distinct edge indicators are independent when disjoint; if they share one endpoint, conditional on that point they are independent with the same constant mean \(q\). Thus
\[\operatorname{Var}(E_{n,\alpha})=\binom n2 q(1-q).\]
Each triangle indicator has variance \(3/16\). Distinct triangles sharing at most one point are uncorrelated. For distinct triangles sharing two points, condition on their common two points: the remaining two point draws are independent with conditional success probability \(\delta/(2\pi)\), so
\[
\operatorname{Cov}(H_{ijk},H_{ij\ell})
=\operatorname{Var}\bigl(\delta/(2\pi)\bigr)=\frac1{48}.
\]
There are \(\binom n2(n-2)(n-3)\) **ordered** pairs of distinct triples meeting in two points. Consequently
\[
\operatorname{Var}(T_n)=\frac3{16}\binom n3+\frac1{48}\binom n2(n-2)(n-3)=\frac{n^2(n-1)(n-2)}{96}.
\]
Dividing the covariance by the square root of these variances yields the stated correlation. Since \(q(1-q)\le1/4\) with equality only at \(q=1/2\), the sharp cutoff and limiting constant follow.

## Verification
The included `verify.py` checks the finite-parameter formulas by exact rational symbolic identities for a range of sample sizes and cutoffs, and tests independent geometric realizations as a diagnostic. The proof above, not a simulation, establishes the results for every integer \(n\ge3\) and every real \(\alpha\in(0,\pi)\). Run `python verify.py` with Python, SymPy and NumPy installed.

## Relationship to prior work
Wendel's hemisphere probability and planar simplicial depth give the single-triangle probability. Liu and subsequent work study the marginal depth statistic; the exact null distribution for the marginal depth is known. Circular uniformity tests and the geometric-graph edge-count literature establish pairwise distance statistics. The contribution here is **the exact joint covariance and correlation of these distinct statistics for every sample size and radius**, including the uniquely most strongly anticorrelated radius. Neither marginal distribution alone determines the joint covariance. General covariance identities for \(U\)-statistics provide a method, but do not themselves supply the evaluated circular-overlap integrals or sharp geometric scale.

## Limitations
The result assumes complete rotational uniformity and independence. It does not characterize their full joint distribution, nonuniform circular distributions, other spatial dimensions, or the efficiency of any test built from the two statistics. General theory of mixed \(U\)-statistics could imply the finite-sample formula after specialization; independent priority examination remains appropriate. The presented computational checks are finite and cannot certify an infinite theorem.

## References
1. Wendel, *A Problem in Geometric Probability*, Math. Scand. 11 (1962), https://journals.msp.org/mscand/article/view/2688.
2. Liu, *On a Notion of Data Depth Based on Random Simplices* (1988), https://pmc.ncbi.nlm.nih.gov/articles/PMC279852/.
3. García-Portugués and Verdebout, *An Overview of Uniformity Tests on the Hypersphere*, arXiv:1804.00286, https://arxiv.org/abs/1804.00286.
4. Ebner, Nestmann and Schulte, *Testing multivariate uniformity based on random geometric graphs*, arXiv:1812.08638, https://arxiv.org/abs/1812.08638.
5. Killeen and Hettmansperger, work on null distributions of planar simplicial depth, https://doi.org/10.1080/03610926.2019.1710205.
