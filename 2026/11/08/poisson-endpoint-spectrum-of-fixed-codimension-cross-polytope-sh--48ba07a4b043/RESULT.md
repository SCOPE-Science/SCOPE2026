# Poisson endpoint spectrum of fixed-codimension cross-polytope shadows

## Finding
Let \(C_n=\operatorname{conv}\{\pm e_i:1\le i\le n\}\subset\mathbb R^n\) be the unit-circumradius regular cross-polytope. Fix an integer \(q\ge1\). Draw \(E_n\in\mathrm{Gr}(n-q,n)\) according to Haar measure and let
\[
r_{n,i}=\|P_{E_n}e_i\|_2,\quad R_{n,q}=\max_{1\le i\le n}r_{n,i},\quad Z_{n,i}=n^{1+2/q}(1-r_{n,i}).
\]
Count each antipodal vertex pair once. For each fixed \(q\), as \(n\to\infty\), the random point measure \(\sum_{i=1}^n\delta_{Z_{n,i}}\) converges in distribution, locally on \([0,\infty)\), to a Poisson point process with intensity
\[
\boxed{\lambda_q(t)\,dt=\frac{t^{q/2-1}}{\Gamma(q/2)}\,dt.}
\]
In particular, setting \(Y_{n,q}=n^{1+2/q}(1-R_{n,q})\) and \(\Lambda_q(t)=t^{q/2}/\Gamma(1+q/2)\),
\[
\boxed{\lim_{n\to\infty}\Pr(Y_{n,q}\le t)=1-e^{-\Lambda_q(t)}\quad(t\ge0),}\qquad
\boxed{\lim_{n\to\infty}\mathbb E[Y_{n,q}^{p}]=\Gamma(1+q/2)^{2p/q}\Gamma(1+2p/q)\quad(p>0).}
\]
The \(k\)-th smallest scaled individual deficit has limiting survival probability \(e^{-\Lambda_q(t)}\sum_{j=0}^{k-1}\Lambda_q(t)^j/j!\). Thus the full near-circumsphere multiplicity spectrum, not merely its outer radius, is asymptotically Poisson. The scale exponent is \(1+2/q\); examples include a square-root Weibull law at codimension one, an exponential law at codimension two, and a quadratic Weibull law at codimension four.

A fully explicit finite-dimensional specialization provides a benchmark. For \(n=3,q=1\), the projected octahedron has circumradius \(R_{3,1}\in[\sqrt{2/3},1]\). For \(\sqrt{2/3}\le r\le1\), put \(s=\sqrt{1-r^2}\). Then
\[
\boxed{\Pr(R_{3,1}\le r)=1-3s+\frac{12}{\pi}\left[s\arcsin\frac{s}{\sqrt{1-s^2}}+\arctan\sqrt{1-2s^2}-\frac{\pi}{4}\right].}
\]
The CDF equals zero below the displayed support and one above it.

## Assumptions and scope
All distances and projections are Euclidean. The random subspace is Haar-distributed and independent for each dimension; the codimension \(q\) is held fixed while the ambient dimension \(n\) tends to infinity. The polytope is the \(\ell_1\)-unit ball, so its original vertices are unit vectors and its circumradius is one. An individual \(r_{n,i}\) is the radius of the projected original antipodal pair and need not be a vertex of the projected polytope; these radii are deliberately counted with their original pair labels. The geometric circumradius \(R_{n,q}\) is nevertheless their maximum. Point-process convergence is vague convergence of locally finite point measures on \([0,\infty)\); no independence of the finite-dimensional projected radii is asserted.

## Proof
**1. Deterministic reduction to leverage scores.** Let \(Q\in\mathbb R^{n\times q}\) have orthonormal columns spanning \(E_n^\perp\). Define \(\ell_i=\|Q^Te_i\|_2^2\). Pythagoras gives \(r_{n,i}=\sqrt{1-\ell_i}\). The projection of \(C_n\) is centrally symmetric, so its minimum enclosing Euclidean ball is centered at zero: if a ball with center \(a\) contains a symmetric set, the antipodal balls with centers \(\pm a\) also contain it, and convexity of the norm shows the ball of the same radius centered at zero contains it. The maximum norm of a convex hull is attained at a generating point. Hence
\[
R_{n,q}=\max_i\sqrt{1-\ell_i}=\sqrt{1-\min_i\ell_i}.
\]

**2. Gaussian representation and precise rare-event scaling.** Let \(G\) be an \(n\times q\) matrix with independent standard normal entries and row vectors \(g_i\). The matrix \(Q=G(G^TG)^{-1/2}\) has the Haar Stiefel distribution, and its leverage scores obey
\[
\ell_i=g_i^T(G^TG)^{-1}g_i=\frac1n g_i^TS_n^{-1}g_i,\qquad S_n=G^TG/n.
\]
For fixed \(q\), the law of large numbers gives \(S_n\to I_q\) in operator norm in probability; for every fixed \(\epsilon>0\), the event \(\|S_n-I_q\|\le\epsilon\) has probability tending to one. On that event, simultaneously for all rows,
\[
\frac{\|g_i\|^2}{n(1+\epsilon)}\le\ell_i\le\frac{\|g_i\|^2}{n(1-\epsilon)}.
\]
Write \(X_i=\|g_i\|_2^2\), independent \(\chi_q^2\) variables. For \(u\downarrow0\), their distribution satisfies the explicit small-ball expansion
\[
\Pr(X_i\le u)=\frac{u^{q/2}}{2^{q/2}\Gamma(1+q/2)}(1+O(u)).
\]
Consequently the independent point process \(\sum_i\delta_{n^{2/q}X_i/2}\) converges to a Poisson point process whose mean measure on \([0,t]\) is \(\Lambda_q(t)=t^{q/2}/\Gamma(1+q/2)\). Indeed on disjoint bounded intervals the cell probabilities are \(O(1/n)\) with \(n\) times each probability converging to the relevant difference of \(\Lambda_q\); the multinomial generating function tends to that of independent Poisson counts. Since \(1-\sqrt{1-z}=z/2+O(z^2)\) uniformly when \(z\) is small, the preceding eigenvalue inequalities sandwich \(Z_{n,i}=n^{1+2/q}(1-\sqrt{1-\ell_i})\) between arbitrarily close positive multiplicative rescalings of \(n^{2/q}X_i/2\), on any fixed bounded window. Letting \(\epsilon\downarrow0\) proves convergence of all finite disjoint-interval counts and their tightness, hence the asserted Poisson point-process convergence.

**3. Radius CDF, order statistics, and moments.** Since \(Y_{n,q}=\min_i Z_{n,i}\), no point in \([0,t]\) has limiting probability \(e^{-\Lambda_q(t)}\). Likewise, the \(k\)-th smallest value exceeds \(t\) exactly when at most \(k-1\) points lie in \([0,t]\), giving the claimed Poisson sum. For moment convergence, on \(\lambda_{\min}(S_n)\ge1/2\), the deterministic bound \(1-\sqrt{1-z}\le z\) gives
\[
0\le Y_{n,q}\le2n^{2/q}\min_i X_i.
\]
Every fixed positive moment of the right side is bounded uniformly in \(n\): the exact tail \(\Pr(\min_iX_i>x)=\Pr(X_1>x)^n\), together with the displayed near-zero small-ball estimate and standard chi-square large-tail estimates, yields uniform tail-integral bounds, including at arbitrarily higher powers. For fixed \(q\), Gaussian Wishart eigenvalue concentration gives \(\Pr(\lambda_{\min}(S_n)<1/2)\le C_qe^{-c_q n}\) for sufficiently large \(n\). On this exceptional event, \(Y_{n,q}\le n^{1+2/q}\) deterministically. Its contribution to every fixed positive moment thus tends to zero. Uniform integrability combined with the Weibull limit gives
\[
\mathbb E[Y_{n,q}^p]\longrightarrow\int_0^\infty p t^{p-1}e^{-\Lambda_q(t)}dt=\Gamma(1+q/2)^{2p/q}\Gamma(1+2p/q).
\]

**4. Exact three-dimensional law.** Let \(u\) be the unit normal to the random plane in \(\mathbb R^3\), and put \(M=\min_i|u_i|\). By the first step, \(R_{3,1}=\sqrt{1-M^2}\), so \(\Pr(R_{3,1}\le r)=\Pr(M\ge s)\) for \(s=\sqrt{1-r^2}\). For \(0\le s\le1/\sqrt3\), the three events \(\{|u_i|<s\}\) have empty triple intersection (except a null boundary). Each single event has probability \(s\), because a coordinate of a uniform point on \(S^2\) is uniform on \([-1,1]\). Conditioning on the first coordinate, a two-coordinate event has probability
\[
I(s)=\frac2\pi\int_0^s\arcsin\frac{s}{\sqrt{1-x^2}}\,dx.
\]
Differentiation under the integral gives \(I'(s)=\frac4\pi\arcsin(s/\sqrt{1-s^2})\) and \(I(0)=0\). Direct differentiation shows
\[
I(s)=\frac4\pi\left[s\arcsin\frac{s}{\sqrt{1-s^2}}+\arctan\sqrt{1-2s^2}-\frac\pi4\right].
\]
Inclusion-exclusion gives \(\Pr(M\ge s)=1-3s+3I(s)\), the stated CDF. At \(s=1/\sqrt3\) it vanishes; at \(s=0\) it equals one. The support is sharp because open neighborhoods of every feasible minimum coordinate have positive spherical measure.

## Verification
Run `python3 verify_projection.py` beside this document with Python, NumPy and SciPy. The program independently integrates the octahedral two-coordinate spherical probability at five thresholds; samples 500000 random octahedron orientations and checks five CDF values; constructs Haar normal frames in four codimensions, explicitly verifies 1920 projected coordinate norms against the leverage-score identity, and compares 4000 Monte Carlo observations per codimension with the corresponding limiting distribution. Its deterministic check and approximate experiments print `CHECKS_PASS` upon success. These checks do not constitute infinite-dimensional Poisson convergence, which follows from Steps 2–3; finite-sample Monte Carlo does not prove the moment assertions.

## Relationship to prior work
Böröczky and Henk (1997 preprint) study expected face numbers of projections of regular polytopes, in a regime with *fixed projected dimension*, rather than Euclidean radii of near-full-dimensional shadows. Donoho and Tanner (arXiv:math/0607364, initially posted 15 July 2006) study surviving projected faces and neighborliness thresholds for high-dimensional simplices and cross-polytopes; their full text treats combinatorial face counts and sparse recovery, not the endpoint radii or Poisson point process here. In a different problem, an October 2026 published result gives an exact diameter law for **central hyperplane sections** of cross-polytopes; sections and projections are not interchangeable, and the normalization there is \(n\sqrt{\log n}\), not the present \(n^3\) when \(q=1\). Another published result gives the **inradius** CDF of Haar-random *planar projections* of the three-dimensional octahedron, not the circumradius CDF. The present statements require the minimum of Gaussian normal-subspace leverage scores rather than the maximum norm of a section or the support-function minimum of a shadow. The reduction to independent small chi-square marks is classical, but the complete codimension-indexed geometric endpoint process, its all-positive-moment law and the exact octahedral shadow-radius benchmark are the asserted contribution. These literature comparisons do not establish exhaustive priority.

## Limitations
The Poisson and moment limits require fixed codimension; neither proportional codimension nor a growing codimension is covered. The point process counts original coordinate-antipodal pairs, not only combinatorially exposed vertices of the projected polytope. The explicit finite-dimensional formula is only for a planar shadow of the three-dimensional regular octahedron. No independent scientific audit has been performed, and stronger unpublished/unevaluated extreme-value results may exist. The 1997 predecessor has a month-only preprint date; a separate fully dated arXiv focal paper supplies the recorded exact first-public date.

## References
1. D. L. Donoho and J. Tanner, *Counting faces of randomly-projected polytopes when the projection radically lowers dimension*, arXiv:math/0607364v1, posted 15 July 2006, https://arxiv.org/abs/math/0607364 ; full accessible text https://arxiv.org/html/math/0607364v2 .
2. K. Böröczky Jr. and M. Henk, *Random Projections of Regular Polytopes*, ZIB Preprint SC 97-21 (May 1997, day unrecorded), https://page.math.tu-berlin.de/~henk/preprints/boeroeczky%20henk%26random%20projections%20of%20regular%20polytopes.pdf .
3. *Exact diameter law and exponential endpoint fluctuations for random cross-polytope hyperplane sections*, publicly indexed October 2026; https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-diameter-law-and-exponential-endpoint-fluctuations-for-ran--72b090c504e9 .
4. *Exact inradius law for random planar projections of the regular octahedron*, publicly indexed October 2026; https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-inradius-law-for-random-planar-projections-of-the-regular--5fbcddcea5e5 .
5. O. Guédon, A. E. Litvak, K. Tatarko, B.-H. Vritsiou, *On random diameters of convex bodies*, arXiv:2609.24131, posted 21 September 2026, https://arxiv.org/abs/2609.24131 .
