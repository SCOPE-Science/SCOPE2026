# An exact all-order moment-finiteness hierarchy in product-kernel coagulation with monomer shattering

## Finding

For every integer \(p\ge3\), the stationary cluster-size moment \(M_p=\sum_{k\ge1}k^p n_k\) is finite exactly when
\[
\lambda>\lambda_p:=\frac{p^2}{p-1}.
\]
At finite orders, these moments are computed recursively by
\[
M_p=\frac{\lambda+\frac12\sum_{j=2}^{p-2}\binom{p}{j}M_{j+1}M_{p-j+1}}{\lambda-p a_\lambda},\qquad
 a_\lambda=\frac{\lambda-\sqrt{\lambda(\lambda-4)}}2.
\]
The first two new boundaries beyond the previously known third-moment threshold are \(\lambda_4=16/3\) and \(\lambda_5=25/4\). At equality, the moment is infinite. This classifies every integer moment order, not merely a fixed collection of low moments.

## Assumptions and scope

We use the infinite mass-conserving monodisperse coagulation–shattering kinetic model at a fixed \(\lambda>4\):
\[
\dot n_1=\lambda-(1+\lambda)n_1,\qquad
\dot n_k=\tfrac12\sum_{i+j=k}ij n_i n_j-(k+\lambda)n_k\quad(k\ge2),
\]
with \(n_k(0)=\mathbf1_{\{k=1\}}\). The non-gelling mass-one solution satisfies \(M_1(t)=1\), the Riccati identity \(\dot M_2=M_2^2-\lambda M_2+\lambda\), and the branch \(M_2(t)\uparrow a_\lambda\), as established for this model in the motivating work. The coefficientwise stationary limit is \(n_1=\lambda/(1+\lambda)\) and
\[
 n_k=\frac{1}{2(k+\lambda)}\sum_{i=1}^{k-1}i(k-i)n_i n_{k-i},\quad k\ge2.
\]
All sums are of nonnegative terms. The present result only concerns this specific mass-one stationary distribution and integer orders \(p\ge3\), at rates strictly above four.

## Proof

**1. Coefficientwise convergence and the second-moment bound.** The monomer equation converges exponentially to its stationary value. Inductively each \(n_k(t)\), for \(k\ge2\), solves a linearly damped equation with a forcing polynomial in the lower-index coordinates; these converge by induction, giving the displayed stationary recurrence. The source's non-gelling second-moment closure gives \(M_2(t)\le a_\lambda\) and \(M_2(t)\to a_\lambda\).

**2. Exact finite-time moment hierarchy.** For each integer \(p\ge3\), summing the coagulation gains minus losses after expanding the binomial identity yields
\[
\dot M_p(t)=(pM_2(t)-\lambda)M_p(t)+\lambda+\frac12\sum_{j=2}^{p-2}\binom pj M_{j+1}(t)M_{p-j+1}(t).
\]
Indeed the two endpoint terms in \(\sum_{j=1}^{p-1}\binom pj M_{j+1}M_{p-j+1}/2\) are exactly \(pM_2M_p\), and every other term uses moment orders strictly below \(p\). The shattering contribution is \(\lambda M_1-\lambda M_p=\lambda-\lambda M_p\). For finite time, the identity can be justified by positive truncation followed by induction and Grönwall bounds: finite initial moments and the bounded second moment control each successive linear moment equation on every compact time interval. In particular, finite experiments or finite truncations are not being equated with an infinite-time conclusion.

**3. Finite side.** Let \(p\ge3\) and suppose \(\lambda>\lambda_p\). The threshold sequence \(p^2/(p-1)=p+1+1/(p-1)\) is strictly increasing for integers \(p\ge2\). Thus, by induction, all moments of order strictly below \(p\) are uniformly bounded in time. The elementary root relation \(a_\lambda^2-\lambda a_\lambda+\lambda=0\) implies
\[
\lambda>\lambda_p\quad\Longleftrightarrow\quad\lambda-p a_\lambda>0\qquad(p\ge3,\lambda>4).
\]
Let \(c=\lambda-pa_\lambda>0\). The differential moment identity then gives \(\dot M_p(t)\le-cM_p(t)+B\) for a finite constant \(B\), hence \(\sup_{t\ge0}M_p(t)<\infty\). Moreover all lower-order moments converge; variation of constants in the scalar moment equation proves that \(M_p(t)\) tends to the exact rational expression stated above. Coefficientwise convergence and Fatou give finiteness of the stationary moment. Since the moment sums are finite, passing the stationary coagulation balance is justified absolutely, so the stationary moment equals the same expression.

**4. Infinite side and sharp equality.** Fix \(p\ge3\) and \(4<\lambda\le\lambda_p\). Suppose that the stationary \(M_p\) were finite. Every lower moment would then also be finite because \(k^j\le k^p\) for \(k\ge1\). The stationary moment balance from Step 2, now justified by nonnegative Tonelli summation and finite moments, would read
\[
(\lambda-pa_\lambda)M_p=\lambda+\frac12\sum_{j=2}^{p-2}\binom pj M_{j+1}M_{p-j+1}>0.
\]
The left-hand side is nonpositive, a contradiction. Equality \(\lambda=\lambda_p\) therefore belongs to the infinite side. This proves both directions for every integer \(p\ge3\).

## Verification

The companion Python checker performs exact rational threshold comparisons for multiple moment orders, independently reconstructs the moment polynomial via the binomial coagulation identity, confirms the first four finite-regime recursive values against stationary recurrence partial sums, and verifies monotonicity of the threshold sequence. Infinite finiteness is established by the proof, not by the finite coefficient checks.

## Relationship to prior work

Matveev's November 6, 2026 preprint gives the stationary recurrence, the non-gelling rate threshold \(\lambda=4\), and its second-moment formula, but does not enumerate the all-integer finiteness boundary sequence. A previously available third-moment result already identifies the single threshold \(9/2\), and a separate critical \(\lambda=4\) result establishes a second-moment logarithmic tail. Those statements are explicitly treated as known special cases and do not classify the fourth and every subsequent integer moment. Fagan–MacKay–Wood study broader stochastic coagulation–fragmentation processes and qualitative steady states; Laurencot–Van Roessel use a different singular fragmentation kernel in a continuous equation. No stronger identical all-integer threshold theorem was identified in the checked comparisons.

## Limitations

This is an all-integer *finiteness* classification, not a sharp tail-equivalent theorem, finite-time moment growth theorem, nor an extension to real moment orders. It uses the source's mass-conserving \(\lambda>4\) solution and second-moment closure; it makes no claims about the gelling regime \(\lambda<4\). Previous work already resolved the special third-moment threshold, and unindexed coagulation literature remains a historical priority risk. Independent mathematical validation has not been performed.

## References

1. S. Matveev, *Suppression of gel formation by spontaneous fragmentation*, arXiv:2611.09537, first submitted 2026-11-06, https://arxiv.org/abs/2611.09537.
2. B. T. Fagan, N. J. MacKay, A. J. Wood, *Robustness of steady state and stochastic cyclicity in generalized coalescence-fragmentation models*, arXiv:2310.04226, 2023, https://arxiv.org/abs/2310.04226.
3. P. Laurençot, H. Van Roessel, *Absence of gelation and self-similar behavior for a coagulation-fragmentation equation*, arXiv:1407.1596, 2014, https://arxiv.org/abs/1407.1596.
