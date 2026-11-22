# Exact positive count–power-length covariance for circular reciprocal nearest neighbors

## Finding
Let \(n\ge5\) independent uniform points lie on a circle of circumference one, with intrinsic geodesic distance. Let \(R_n\) count unordered mutual nearest-neighbor pairs, once each, and let \(W_{n,\alpha}\) be the sum of the \(\alpha\)-th powers of their geodesic lengths, also once each. For **every real \(\alpha>0\)**,
\[
\mathbb E R_n=\frac n3,\qquad
\mathbb E W_{n,\alpha}=\frac{n\Gamma(n)\Gamma(\alpha+1)}{3^{\alpha+1}\Gamma(n+\alpha)},
\]
\[
\boxed{\operatorname{Cov}(R_n,W_{n,\alpha})
=\frac{n\Gamma(n)\Gamma(\alpha+1)}{3\Gamma(n+\alpha)}
\left(3^{-(\alpha+1)}-5^{-(\alpha+1)}\right)>0.}
\]
In particular, the ordinary-length covariance is **independent of sample size**:
\[
\mathbb E W_{n,1}=\frac19,\qquad
\operatorname{Cov}(R_n,W_{n,1})=\frac{16}{675}\quad(n\ge5).
\]
For each fixed \(\alpha>0\), the covariance is asymptotic to
\[
\frac{\Gamma(\alpha+1)}3\left(3^{-(\alpha+1)}-5^{-(\alpha+1)}\right)n^{1-\alpha}.
\]
Thus \(\alpha=1\) is the unique power with an order-one nonzero limiting covariance; the covariance grows for \(0<\alpha<1\) and decays for \(\alpha>1\). This all-power positive law is different from the **negative** covariance \(-1/36\) with the *total directed nearest-neighbor length* (a different edge-length statistic) previously obtained on the same circular model [3].

## Assumptions and scope
The circle has circumference one and contains exactly \(n\) iid uniform points. Distances are intrinsic shorter-arc distances, not planar chord lengths. Ties and coincident points have probability zero. A pair is counted only if each point selects the other as its unique nearest neighbor; its length is counted once. Indices below are modulo \(n\), and the claimed identities hold for every integer \(n\ge5\) and every real \(\alpha>0\), with no large-sample restriction. The continuous extension at \(\alpha=0\) gives the known \(\operatorname{Var}(R_n)=2n/45\).

Let \(G_i\) be the cyclic gaps in their order around the circle, and set \(I_i=\mathbf1\{G_i<G_{i-1},\ G_i<G_{i+1}\}\). Since a nearest point is a cyclic neighbor and a gap longer than half the circumference cannot be a local minimum, reciprocal edges are exactly these local-minimum gaps. Hence \(R_n=\sum_i I_i\) and \(W_{n,\alpha}=\sum_iG_i^\alpha I_i\).

## Proof
**1. Dirichlet/exponential reduction.** Let \(X_1,\ldots,X_n\) be independent \(\operatorname{Exp}(1)\) variables and \(S=\sum_iX_i\). The circular spacings have the law \((X_1/S,\ldots,X_n/S)\). The normalized gap vector is independent of \(S\sim\operatorname{Gamma}(n,1)\). Put
\[
U_\alpha=\sum_i X_i^\alpha I_i,\qquad
m_\alpha=\mathbb E[X_i^\alpha I_i]=\int_0^\infty x^\alpha e^{-3x}\,dx
=\frac{\Gamma(\alpha+1)}{3^{\alpha+1}}.
\]
The minimum of three iid continuous variables is equally likely at any position, so \(\mathbb EI_i=1/3\). Because \(U_\alpha=S^\alpha W_{n,\alpha}\), while \(S\) is independent of \((R_n,W_{n,\alpha})\), the gamma moment \(\mathbb ES^\alpha=\Gamma(n+\alpha)/\Gamma(n)\) gives the exact identities
\[
\mathbb EW_{n,\alpha}=\frac{nm_\alpha\Gamma(n)}{\Gamma(n+\alpha)},\qquad
\operatorname{Cov}(R_n,W_{n,\alpha})=
\frac{\Gamma(n)}{\Gamma(n+\alpha)}\operatorname{Cov}(R_n,U_\alpha).
\]
These identities use *gamma normalization*, not the invalid replacement of \(\mathbb E(1/S)\) by \(1/\mathbb ES\).

**2. Local mixed moments.** Events involving \(I_i\) and \(X_j^\alpha I_j\) are independent if their cyclic index distance exceeds two. For the diagonal term,
\[
\operatorname{Cov}(I_i,X_i^\alpha I_i)=\frac23m_\alpha.
\]
For either adjacent position, the two indicators are mutually exclusive, so
\[
\operatorname{Cov}(I_i,X_{i\pm1}^\alpha I_{i\pm1})=-\frac13m_\alpha.
\]
At cyclic distance two, write \(x=X_i\) and \(y=X_{i+2}\). The constraints for both local minima require three other exponentials to exceed \(x\), \(\max(x,y)\), and \(y\), respectively. Integrating them out gives
\[
\begin{aligned}
\mathbb E[I_iX_{i+2}^\alpha I_{i+2}]
&=\int_0^\infty\!\int_0^\infty
 y^\alpha e^{-2x-2y-\max(x,y)}\,dx\,dy\\
&=\frac{\Gamma(\alpha+1)}2\left(3^{-(\alpha+1)}-5^{-(\alpha+1)}\right)
+\frac{\Gamma(\alpha+1)}{3\,5^{\alpha+1}}\\
&=\Gamma(\alpha+1)\left(\frac{1}{2\,3^{\alpha+1}}-\frac{1}{6\,5^{\alpha+1}}\right).
\end{aligned}
\]
The second line follows by splitting the domain at \(x=y\) and applying \(\int_0^\infty y^\alpha e^{-cy}\,dy=\Gamma(\alpha+1)c^{-(\alpha+1)}\). Subtracting \(\mathbb EI_i\cdot m_\alpha\) gives
\[
\operatorname{Cov}(I_i,X_{i+2}^\alpha I_{i+2})
=\frac{\Gamma(\alpha+1)}6\left(3^{-(\alpha+1)}-5^{-(\alpha+1)}\right).
\]
The same expression holds for the offset \(-2\).

**3. Cyclic summation and sign.** For \(n\ge5\), the five relevant offsets \(0,\pm1,\pm2\) are distinct. Summing the covariances in Step 2 over \(j\) for each \(i\), the diagonal \(2m_\alpha/3\) cancels the two adjacent contributions \(-m_\alpha/3\). Exactly two distance-two contributions remain. Thus
\[
\operatorname{Cov}(R_n,U_\alpha)
=\frac{n\Gamma(\alpha+1)}3\left(3^{-(\alpha+1)}-5^{-(\alpha+1)}\right).
\]
Applying Step 1 yields the theorem. All factors are positive when \(\alpha>0\). Setting \(\alpha=1\) gives \(16/675\) exactly; the gamma-ratio asymptotic \(\Gamma(n)/\Gamma(n+\alpha)\sim n^{-\alpha}\) proves the stated scale trichotomy.

## Verification
The standalone `verify.py` uses only Python's standard library and exact rational arithmetic. It independently enumerates all permutations of circular exponential-gap ranks for \(n=5,6,7,8\), calculates the exact conditional moments of exponential order statistics from their independent increment law, and checks \(\mathbb ER_n\), \(\mathbb EW_{n,\alpha}\), and \(\operatorname{Cov}(R_n,W_{n,\alpha})\) for each integer \(\alpha=0,1,2,3\). It also checks the distance-two split-integral identity at five integer powers and specialized rational formulas. Execute `python verify.py`; it reports 69 exact checks. These finite tests do **not** establish the real-power or all-\(n\) claim; Steps 1–3 do.

## Relationship to prior work
Penrose and Wade [1] treat arbitrary power-weighted lengths of the **whole directed nearest-neighbor graph** on an interval, not the reciprocal-edge subgraph or the joint count–length moment. Bahadır and Ceyhan [2] give the unweighted reflexive-pair count law on an interval. The 2026 circular result [3] gives a negative count covariance for the **sum over all outgoing arcs** at power one; it does not imply the positive reciprocal-only all-power covariance. The 2026 interval result [4] computes the power-one reciprocal count–length covariance and its joint normal limit. In fact, its interior-spacing calculation supplies some of the same local integrals used above, and its limiting power-one constant agrees with the circular exact constant. This agreement is acknowledged rather than claimed as a separate discovery. None of these inspected claims states the circular covariance as an exact closed-form function for **every** real positive power, with a uniform sign and the critical power-one scaling.

## Limitations
The exact formulas concern a fixed-size uniform sample on a circle with intrinsic distance, not arbitrary densities, planar chord distance, higher dimensions, or sample sizes three and four. They do not provide a joint distribution or a multivariate central limit theorem for different powers. The derivation uses standard exponential spacing identities and local integration; a still-earlier or more general weighted-nearest-neighbor theorem could subsume the result, and historical priority remains qualified. Scientific review of the proof and comparisons is not independent validation.

## References
1. M. D. Penrose and A. R. Wade, *Limit theory for the random on-line nearest-neighbour graph*, arXiv:math/0603561v1, first publicly submitted 2006-03-23. https://arxiv.org/abs/math/0603561
2. S. Bahadır and E. Ceyhan, *On the Number of Reflexive and Shared Nearest Neighbor Pairs in One-Dimensional Uniform Data*, arXiv:1605.01940v1, first publicly submitted 2016-05-06. https://arxiv.org/html/1605.01940v1
3. *Exact negative motif–length covariance in the circular nearest-neighbor graph*, published technical result, 2026-10-27. https://github.com/published-finding corpus/2026/tree/main/2026/10/27/SCOPE-exact-negative-motif-length-covariance-in-the-circular-nearest-n--d272683b84c8
4. *Exact count–length coupling of mutual nearest-neighbor pairs on an interval*, published technical result, 2026-11-08. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-count-length-coupling-of-mutual-nearest-neighbor-pairs-on--58929be679e6
