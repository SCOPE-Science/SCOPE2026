# Parity-forced omission and a complete optimizer face for Kaczmarz sampling on endpoint-anchored paths

## Finding

**Theorem.** Let \(n\ge2\) be an integer. In \(\mathbb R^n\), consider the \(n+1\) unit-norm measurement rows
\[
 a_{\mathrm L}=e_1,\qquad a_{\mathrm R}=e_n,\qquad
 a_j=\frac{e_j-e_{j+1}}{\sqrt2}\quad(1\le j<n).
\]
The two endpoint rows calibrate absolute values, while the remaining rows measure neighboring differences. Choose a row independently at each Kaczmarz step with nonnegative probabilities \(p_{\mathrm L},p_{\mathrm R},p_1,\ldots,p_{n-1}\) totaling one. Set
\[
 M(p)=p_{\mathrm L}a_{\mathrm L}a_{\mathrm L}^{\mathsf T}
 +p_{\mathrm R}a_{\mathrm R}a_{\mathrm R}^{\mathsf T}
 +\sum_{j=1}^{n-1}p_j a_ja_j^{\mathsf T}.
\]
Define the tent profile and its squared norm by
\[
 v_i=1+\sqrt2\min\{i-1,n-i\},\qquad
 S_n=\sum_{i=1}^n v_i^2.
\]
Then the sharp worst-direction *one-step expected squared-error decrease* is
\[
 \boxed{\max_{p}\lambda_{\min}(M(p))=\frac1{S_n}.}
\]
The following formulas describe **every** maximizing probability vector.

If \(n=2m\), the maximizer is unique. The central comparison row is never sampled:
\[
 \boxed{p_m=0,\quad p_{\mathrm L}=p_{\mathrm R}=
 \frac{\sum_{i=1}^m v_i}{S_n},\quad
 p_j=p_{n-j}=\frac{\sqrt2\sum_{i=j+1}^{m}v_i}{S_n}
 \ (1\le j<m).}
\]
All the other \(n\) rows have strictly positive probability.

If \(n=2m+1\), the entire optimizer set is the one-dimensional closed segment indexed by \(0\le\theta\le1\):
\[
 \begin{aligned}
 p_{\mathrm L}&=\frac{\sum_{i=1}^m v_i+\theta v_{m+1}}{S_n},&
 p_{\mathrm R}&=\frac{\sum_{i=1}^m v_i+(1-\theta)v_{m+1}}{S_n},\\
 p_j&=\frac{\sqrt2(\sum_{i=j+1}^{m}v_i+\theta v_{m+1})}{S_n},&
 p_{n-j}&=\frac{\sqrt2(\sum_{i=j+1}^{m}v_i+(1-\theta)v_{m+1})}{S_n}
 \quad (1\le j\le m).
 \end{aligned}
\]
In the two endpoint designs \(\theta=0,1\), precisely one of the two comparisons adjacent to the central vertex is omitted; interior designs \(0<\theta<1\) sample all \(n+1\) rows positively. In either parity,
\[
 \boxed{\lim_{n\to\infty}n^3\max_p\lambda_{\min}(M(p))=6.}
\]

## Assumptions and scope

The linear system \(Ax=b\) is consistent, with the rows above. Every selected row triggers its exact orthogonal Kaczmarz projection, with independent identically distributed fixed sampling. All rows have Euclidean norm one; no additional cost weighting is imposed. The exact sharp one-step conditional mean-squared reduction is the minimum eigenvalue of \(M(p)\), because for the current error \(z\),
\[
 \mathbb E(\|z^+\|_2^2\mid z)=\|z\|_2^2-z^{\mathsf T}M(p)z.
\]
This gives a recursively valid uniform convergence bound, not an assertion that the bound is an exact multi-step error exponent. Even zero-probability rows may remain in the supplied consistent system.

## Proof

**Upper certificate.** The vector \(v\) is strictly positive, with \(v_1=v_n=1\). Every edge difference has absolute magnitude \(\sqrt2\), except the central edge of an even-order path, for which the difference vanishes. Consequently
\[
 \frac{v^{\mathsf T}M(p)v}{v^{\mathsf T}v}
 =\begin{cases}
 1/S_n,&n\text{ odd},\\
 (1-p_m)/S_n,&n=2m.
 \end{cases}
\]
The Rayleigh principle yields the asserted universal upper bound and forces \(p_m=0\) at any even-order optimum.

**Achievability and normalization.** Substituting either displayed probability formula into the node equations gives \(M(p)v=v/S_n\). At a left interior vertex on the increasing half, the edge contributions equal \((p_{i-1}-p_i)/\sqrt2=v_i/S_n\), since adjacent edge-probability numerators differ by \(\sqrt2 v_i\). The analogous identities hold by reflection on the right. The endpoint equations hold because \(p_{\mathrm L}-p_1/\sqrt2=v_1/S_n\) and \(p_{\mathrm R}-p_{n-1}/\sqrt2=v_n/S_n\). At an even center the middle probability vanishes and the adjacent edge contributes exactly \(v_m/S_n\) to each central vertex. At an odd center, \(p_m+p_{m+1}=\sqrt2 v_{m+1}/S_n\). All probabilities are nonnegative, with strictly positive anchor probabilities. The identity \(v^{\mathsf T}M(p)v=1\) and the fact that every positively sampled row has \((a_j^{\mathsf T}v)^2=1\) prove that the probabilities total one.

**Smallest eigenvalue.** Whenever a symmetric matrix \(M\) has off-diagonal entries \(-p_j/2\) along path edges and satisfies \(Mv=\mu v\) with \(v_i>0\), direct expansion gives for any \(z\in\mathbb R^n\)
\[
 z^{\mathsf T}(M-\mu I)z
 =\frac12\sum_{j=1}^{n-1}p_jv_jv_{j+1}
 \left(\frac{z_j}{v_j}-\frac{z_{j+1}}{v_{j+1}}\right)^2\ge0.
\]
This remains true for zero middle-row probabilities. Therefore \(\lambda_{\min}(M)=\mu=1/S_n\), proving attainment.

**Exhaustiveness.** Every optimum must satisfy \(Mv=v/S_n\), since the Rayleigh quotient at \(v\) equals the optimal minimum eigenvalue. In even order, \(p_m=0\); solving the two endpoint equations and successive interior difference equations inward, with the two center equations, determines uniquely the displayed weights. In odd order, the central equation is \(p_m+p_{m+1}=\sqrt2 v_{m+1}/S_n\). Set \(\theta=p_m S_n/(\sqrt2v_{m+1})\). Nonnegativity is exactly \(0\le\theta\le1\), and solving inward-to-outward forces the complete displayed segment. There are no other optimizers.

**Limit.** In both parities, the tent profile has two linear arms of height asymptotic to \(n/\sqrt2\), and direct summation of squares gives \(S_n=n^3/6+O(n^2)\). Hence \(n^3/S_n\to6\).

## Verification

The companion `verify.py` uses exact arithmetic in \(\mathbb Q(\sqrt2)\) for \(2\le n\le100\) and five parameter choices per order, checking probability normalization, nonnegativity, the complete eigenvector equation and the saturated Rayleigh rows. It reports `VERIFY_OK 495`. Independent floating-point symmetric-eigensolver calculations for small orders and admissible parameters agreed with the formula. These finite checks support, but do not replace, the preceding all-order argument.

## Relationship to prior work

Strohmer and Vershynin's randomized Kaczmarz framework gives convergence bounds for row-norm sampling. Gower and Richtárik formulate optimization of the sharp one-step spectral contraction as a semidefinite program for general randomized iterative methods. These statements cover the *optimization framework*, not the explicit parity-dependent optimizer face of this overdetermined two-endpoint path design. Agaskar, Wang and Lu additionally optimize the *different* exact annealed mean-squared error exponent via a Kronecker-projection semidefinite program, without the present path classification. The earlier inverse-positive SPD coordinate-sampling theorem supplies exact results for a different, square inverse-positive class; taking a square subdesign does not establish optimality over the extra central comparison row or classify all global optimizers. The present proof supplies the required dual Rayleigh witness and equality characterization explicitly.

## Limitations

This theorem concerns a consistent system, Euclidean orthogonal projections, and iid fixed row probabilities. It does not optimize adaptive row choices, unequal sampling costs, noisy measurements, block projections, or the exact multi-step annealed exponent. The uniqueness statement is parity-specific, and the row probabilities are allowed to be zero. The claim has not undergone independent mathematical validation; any unindexed equivalent endpoint-anchored design theorem could affect publication priority.

## References

1. T. Strohmer and R. Vershynin, *A Randomized Kaczmarz Algorithm with Exponential Convergence*, public preprint 2007-02-08, https://arxiv.org/abs/math/0702226.
2. R. M. Gower and P. Richtárik, *Randomized Iterative Methods for Linear Systems*, public preprint 2015-06-10, https://arxiv.org/abs/1506.03296; in particular Section 5.1.
3. P. Richtárik and M. Takáč, *On Optimal Probabilities in Stochastic Coordinate Descent Methods*, first preprint 2013-10-13, https://arxiv.org/abs/1310.3438.
4. B. Osting, C. Brune and S. J. Osher, *Optimal Data Collection For Informative Rankings Expose Well-Connected Graphs*, JMLR 15 (2014), 2981–3012, https://www.jmlr.org/papers/volume15/osting14a/osting14a.pdf.
5. A. Agaskar, C. Wang and Y. M. Lu, *Randomized Kaczmarz Algorithms: Exact MSE Analysis and Optimal Sampling Probabilities*, GlobalSIP 2014, pp. 389–393, https://scholar.harvard.edu/files/yuelu/files/randkac_globalsip14.pdf.
6. *Closed-form optimal coordinate sampling for inverse-positive SPD quadratics*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-inverse-positive-optimal-coordinate-sampling--82c9d23eb995.
