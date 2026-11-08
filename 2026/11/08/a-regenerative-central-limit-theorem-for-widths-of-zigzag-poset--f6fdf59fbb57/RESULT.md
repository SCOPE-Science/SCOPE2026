# A regenerative central limit theorem for widths of zigzag-poset polytopes

## Finding

For each integer \(n\ge 2\), let \(Z_n\) be the zigzag poset on \([n]\) with alternating covers \(1<2>3<4>\cdots\), and let \(K_n\subset\mathbb R^n\) be either its standard order polytope or its standard chain polytope, endowed with the ambient Euclidean metric. Let \(U_n\) be uniform on \(S^{n-1}\), and set
\[
W_n=h_{K_n}(U_n)+h_{K_n}(-U_n).
\]
Both choices of \(K_n\) have the same entire width law, because the two polytopes are related by an explicit coordinate-complementing Euclidean isometry.

Let \(G_i\), \(i\in\mathbb Z\), be independent standard Gaussian variables. There exist unique stationary nonnegative processes
\[
D_i^+=(G_i-D_{i-1}^+)_+,\qquad D_i^-=(-G_i-D_{i-1}^-)_+,
\]
where \(x_+=\max\{x,0\}\). Define \(X_i=D_i^++D_i^-\) and \(c=\mathbb E D_0^+\). In particular \(0<c<1/\sqrt{2\pi}\). The law \(F\) of \(D_0^+\) is the unique probability law on \([0,\infty)\) satisfying, for all \(t\ge0\),
\[
F(t)=\int_{[0,\infty)}\Phi(t+y)\,dF(y),\qquad
c=\int_0^\infty(1-F(t))\,dt.
\]
Here \(\Phi\) is the standard-normal cumulative distribution function. Put \(a_n=\sqrt2\,\Gamma((n+1)/2)/\Gamma(n/2)\). For every \(n\ge2\) there is the explicit finite-size estimate
\[
\left|a_n\,\mathbb EW_n-2cn\right|\le\frac4{\sqrt{2\pi}}.
\]
In particular \(\mathbb EW_n=2c\sqrt n+O(n^{-1/2})\).

Let \(T_j\) enumerate the consecutive occurrences of the sign pattern \(G_{T_j-1}<0<G_{T_j}\) in the two-sided Gaussian sequence. Under the law conditioned on an occurrence at \(T_0=0\), let \(L=T_1-T_0\); then \(\mathbb EL=4\). Define the exact positive constant
\[
\sigma^2=\frac14\,\mathbb E\left[\left(\sum_{i=T_0}^{T_1-1}\bigl(X_i-2c-c(G_i^2-1)\bigr)\right)^2\right].
\]
The expectation is under that regeneration-start law. Then \(0<\sigma^2<\infty\), and
\[
\boxed{W_n-2c\sqrt n\ \xrightarrow{d}\ N(0,\sigma^2),\qquad
\lim_{n\to\infty}\operatorname{Var}(W_n)=\sigma^2.}
\]
Equivalently, if
\[
\tau^2=\operatorname{Var}(X_0)+2\sum_{k=1}^{\infty}\operatorname{Cov}(X_0,X_k),
\]
then the covariance series converges absolutely and \(\sigma^2=\tau^2-2c^2\). The subtraction is the exact correction due to normalizing a Gaussian direction to unit length. Numerical quadrature and simulation (not a numerical certification) give \(c\approx0.307510818\) and \(\sigma^2\approx0.0627\).

## Assumptions and scope

All coordinates use the ordinary Euclidean inner product; no normalization of the polytope is made. The poset has \(n\) elements and \(n-1\) alternating cover relations, so its comparability graph is the path on \(n\) vertices. For the chain polytope,
\[
K_n=\left\{x\in\mathbb R_{\ge0}^n:x_i+x_{i+1}\le1\text{ for }1\le i<n\right\}.
\]
For the order polytope, \(0\le x_i\le1\) and \(x_i\le x_{i+1}\) for odd \(i\), \(x_i\ge x_{i+1}\) for even \(i\). The stationary-process and renewal constants use standard-normal weights. The Gaussian limit is for the **random length of a one-dimensional orthogonal projection**, not for the polytope's random-vertex distribution. The limiting variance is not asserted to have an elementary closed form.

## Proof

**1. Isometry and Gaussian support recursion.** For the order polytope replace the even coordinates \(x_{2j}\) by \(1-x_{2j}\), keeping odd coordinates unchanged. This is an affine Euclidean isometry mapping each order inequality into \(y_i+y_{i+1}\le1\), hence onto the chain polytope. Since the comparability graph is a path, the chain polytope is the integral stable-set polytope of that bipartite graph. Its vertices are the indicator vectors of independent sets. For any deterministic \(g=(g_1,\ldots,g_n)\), write \(M_i\) for the maximum weight of a stable set on the first \(i\) path vertices and \(M_0=0\). The standard last-vertex dichotomy gives
\[
M_i=\max\{M_{i-1},M_{i-2}+g_i\},\quad
M_1=(g_1)_+.
\]
Thus with \(M_{-1}=0\), the increments \(D_i=M_i-M_{i-1}\) satisfy \(D_0=0\), \(D_i=(g_i-D_{i-1})_+\), and \(h_{K_n}(g)=\sum_{i=1}^nD_i\). Applying the same recursion to \(-g\), the Gaussian width numerator is
\[
H_n:=h_{K_n}(G)+h_{K_n}(-G)=\sum_{i=1}^n(D_{i,n}^++D_{i,n}^-),
\]
with both finite recursions initialized at zero. Since \(G=R U_n\), where \(R=\|G\|_2\) and \(U_n\) are independent, \(H_n=RW_n\), \(\mathbb ER=a_n\), and \(\mathbb EH_n=a_n\mathbb EW_n\).

**2. Stationarity and an explicit finite error.** Whenever \(G_j\le0\), the positive recursion sets \(D_j^+=0\) regardless of its prehistory; whenever \(G_j\ge0\), the negative recursion sets \(D_j^-=0\). With probability one, both kinds of reset occur arbitrarily far back. Iterating forward after the most recent respective reset defines the stationary processes uniquely as measurable functions of past Gaussian variables. Also \(0\le D_i^+\le(G_i)_+\) and \(0\le D_i^-\le(-G_i)_+\). Two copies of the positive recursion disagree at time \(i\) only if all of the intervening Gaussian weights are positive; hence their coupling-disagreement probability is bounded by \(2^{-r}\) after \(r\) steps, and similarly for the negative recursion. This proves uniqueness of the one-dimensional fixed-point law and the stated integral equation. The equality \(c=\int_0^\infty(1-F(t))dt\) is the layer-cake identity.

Couple finite and stationary recursions using the same \(G_1,G_2,\ldots\). For each \(i\ge1\), they can differ in the positive coordinate only when \(G_1,\ldots,G_i>0\); their absolute difference is at most \((G_i)_+\). Therefore
\[
\mathbb E|D_{i,n}^+-D_i^+|\le\frac{2^{-(i-1)}}{\sqrt{2\pi}},
\qquad
\mathbb E|D_{i,n}^--D_i^-|\le\frac{2^{-(i-1)}}{\sqrt{2\pi}}.
\]
Summing the geometric series yields \(|\mathbb EH_n-2cn|\le4/\sqrt{2\pi}\). Since \(a_n=\sqrt n(1-1/(4n)+O(n^{-2}))\), the claimed sharp-order mean estimate follows. Strictly positive \(c\) follows from \(\Pr(G_i>1,D_{i-1}^+<1/2)>0\); strict upper bound follows because \(\Pr(D_{i-1}^+>0,G_i>D_{i-1}^+)>0\).

**3. Regeneration and the Gaussian central limit theorem.** Set \(X_i=D_i^++D_i^-\). Each \(X_i\) depends only on finitely many preceding Gaussian variables almost surely: a negative weight resets the positive recursion, and a positive weight resets the negative recursion. In particular \(0\le X_i\le|G_i|\), and the probability that more than \(r\) predecessors are needed is at most \(2^{1-r}\). This yields exponentially decreasing dependence and absolutely summable covariances. More explicitly, at each occurrence \(G_{t-1}<0<G_t\), the two-component state is exactly \((D_t^+,D_t^-)=(G_t,0)\), independent of earlier states. The successive blocks beginning at these occurrences are independent and identically distributed under their regeneration-start law; lengths have exponential tails and mean four, while their Gaussian-weighted rewards have finite moments of every fixed order. The ordinary regenerative renewal-reward central limit theorem therefore applies jointly to \(\sum_{i=1}^nX_i\) and \(\sum_{i=1}^n(G_i^2-1)\). Coupling from step 2 changes the former by a random finite amount with integrable square: the squared discrepancy in either sign at index \(i\) is at most \(G_i^2\) on the event of \(i\) consecutive same-sign weights, whose expectation is \(2^{-i}\); Minkowski's inequality then bounds the \(L^2\) norm of the summed discrepancy by a convergent geometric series. Hence finite initialization does not change its central limit theorem or variance asymptotics.

Set \(Q_n=\sum_{i=1}^nG_i^2\). Since \(H_n\) is a nonnegative, degree-one homogeneous, Lipschitz, piecewise-linear function of \(G\), Euler's identity and Gaussian integration by parts give the **exact finite-dimensional identity**
\[
\operatorname{Cov}(H_n,Q_n)
=\sum_{j=1}^n\mathbb E[G_j\partial_jH_n]
=\mathbb EH_n.
\]
The first equality uses \(\mathbb E[(G_j^2-1)H_n]=\mathbb E[G_j\partial_jH_n]\), valid by smoothing or almost-everywhere Lipschitz differentiation. The second uses \(\sum_jG_j\partial_jH_n=H_n\). Regeneration gives \(\operatorname{Var}(H_n)/n\to\tau^2\); the preceding identity gives \(\operatorname{Cov}(H_n,Q_n)/n\to2c\), while \(\operatorname{Var}(Q_n)/n=2\).

The delta method applied to \(W_n=H_n/\sqrt{Q_n}\), \(H_n/n\to2c\), and \(Q_n/n\to1\) gives
\[
W_n-2c\sqrt n
=\frac{H_n-2cn}{\sqrt n}-c\frac{Q_n-n}{\sqrt n}+o_{\Pr}(1).
\]
Its limiting variance is therefore \(\tau^2+c^2(2)-2c(2c)=\tau^2-2c^2\), equal to the stated cycle-reward expression. The exact radial factorization also gives
\[
\operatorname{Var}(H_n)=n\operatorname{Var}(W_n)+(n-a_n^2)(\mathbb EW_n)^2.
\]
Because \(n-a_n^2\to1/2\), \(\operatorname{Var}(H_n)/n\to\tau^2\), and \((\mathbb EW_n)^2/n\to4c^2\), this identity proves \(\operatorname{Var}(W_n)\to\tau^2-2c^2\), without any unproved moment-interchange assumption.

**4. Strict positivity.** For a regeneration cycle of length two, the Gaussian signs are \((+,-)\) on the cycle and the next Gaussian sign is positive. Writing the two absolute Gaussian magnitudes as \(a,b>0\), its two increments satisfy \(X_t=a\), \(X_{t+1}=b\), and the centered cycle reward is
\[
a+b-4c-c(a^2+b^2-2)=a+b-c(a^2+b^2)-2c.
\]
This is not constant on the positive quadrant, which has a strictly positive continuous conditional density. The mean-zero renewal-reward variance is thus strictly positive. Finiteness follows from exponential cycle-length tails and the Gaussian moment bounds. This completes the claim.

## Verification

Execute `python check.py` with Python 3, NumPy, and SciPy. The checker independently enumerates stable-set vertices for small \(n\), verifies their maximum weight equals the recursive support function, tests the coordinate-complementing isometry, iterates the stationary fixed-point equation by quadrature, and compares a seeded finite-dimensional width sample to the predicted leading mean and exact Gaussian integration-by-parts identity. Its successful marker is `ZIGZAG_WIDTH_CHECKS_PASSED`. A separate long Gaussian trace gave an exploratory renewal-variance estimate near \(0.0627\); this numerical estimate is not needed in the proof. Finite enumeration and quadrature are checks, not infinite-dimensional certifications.

## Relationship to prior work

Coons and Sullivant (first arXiv posting January 22, 2019) studied the zigzag order polytope through canonical triangulations, shellings, and Ehrhart \(h^*\)-polynomials. Petersen and Zhuang (2024) developed zigzag Eulerian and order-polynomial recurrences. Hibi and Li established a general criterion for unimodular equivalence of order and chain polytopes; the explicit coordinate isometry here is an elementary specialization and is not presented as new.

The established random-weight independent-set literature, including Gamarnik, Nowicki, and Świrszcz, has tree fixed-point recurrences and expected-optimum limits; it can explain the leading stationary mean constant after discarding negative weights. The novelty claim is **not** that max-weight independent-set dynamic programming, the Gaussian support identity, or a fixed-point mean exists. The additional conclusion is the spherical directional-width central limit theorem, its **strictly positive** exact renewal variance and radial correction, and a finite-dimension mean-width error bound for this particular geometric family. Kabluchko, Litvak, and Zaporozhets proved Gaussian-width and projection-length limits for regular cubes, simplices, and crosspolytopes, not this family. Foss, Konstantopoulos, Logachov, and Mogulski prove renewal-based Gaussian and local limit results for maximal paths with *independent edge weights* on a complete ordered graph. Their model is not a Gaussian vertex-weighted independent-set problem on a fixed path, and their statement does not address the normalization by the Euclidean norm of the common Gaussian direction. The regenerative technique itself is not claimed as new.

## Limitations

The theorem is for alternating fence posets whose comparability graph is a path, standard ambient Euclidean coordinates, and one-dimensional Haar-uniform orthogonal projections. The two-dimensional or higher-dimensional projection laws, non-Gaussian directional measures, other fence compositions, and a closed elementary expression for the variance constant are not treated. The fixed-point and renewal formulas are exact characterizations, not claims of elementary evaluation. Numerical constants quoted above are approximations and are not rigorous certified intervals. Historical priority remains provisional, especially for equivalent versions in stochastic dynamic-programming/renewal theory.

## References

1. J. I. Coons and S. Sullivant, *The h-star polynomial of the order polytope of the zig-zag poset*, arXiv:1901.07443 (first public version January 22, 2019), Electron. J. Combin. 30 (2023), P2.44. https://arxiv.org/abs/1901.07443
2. T. K. Petersen and Y. Zhuang, *Zig-zag Eulerian polynomials*, arXiv:2403.07181 (first public version March 11, 2024). https://arxiv.org/abs/2403.07181
3. D. Gamarnik, T. Nowicki, and G. Świrszcz, *Maximum Weight Independent Sets and Matchings in Sparse Random Graphs: Exact Results Using the Local Weak Convergence Method*, arXiv:math/0309441 (2003). https://arxiv.org/abs/math/0309441
4. Z. Kabluchko, A. E. Litvak, and D. Zaporozhets, *Mean width of regular polytopes and expected maxima of correlated Gaussian variables*, arXiv:1511.08479 (2015). https://arxiv.org/abs/1511.08479
5. T. Hibi and N. Li, *Unimodular Equivalence of Order and Chain Polytopes*, Mathematica Scandinavica 118 (2016), 5–12, DOI:10.7146/math.scand.a-23291.
6. S. Foss, T. Konstantopoulos, A. Logachov, and A. Mogulski, *Limit theorems for the maximal path weight in a directed graph on the line with random weights of edges*, arXiv:2011.09981 (first version November 19, 2020). https://arxiv.org/abs/2011.09981
7. J. Lee, *A refinement of the edge theorem for order and chain polytopes*, arXiv:2610.07413 (2026; related later literature, not a source for the 2019 public-date anchor). https://arxiv.org/abs/2610.07413
