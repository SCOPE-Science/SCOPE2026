# Exact Ville-bound equality angles for two-row randomized Kaczmarz

## Finding

A two-equation, full-rank randomized Kaczmarz system has an exact binomial squared-error law. More importantly, there is a *complete classification* of the row angles and confidence thresholds at which its data-adapted time-uniform martingale inequality holds with equality.

For every real \(0<q<1\), let
\[
a_1=(1,0),\qquad a_2=(\sqrt q,\sqrt{1-q}),\qquad A=\begin{pmatrix}a_1\\a_2\end{pmatrix},\qquad b=0,
\]
and solve \(Ax=b\) by independently selecting either normalized row with probability \(1/2\) at every iteration. Take \(x_0=e_2\), and let \(x_n\) be the error after \(n\) projections. Put \(r=(1+q)/2\) and \(Z_n=\|x_n\|_2^2/r^n\). Then, for every integer \(n\ge0\),
\[
\|x_n\|_2^2\ \stackrel{\mathrm d}=\ q^{B_n},\qquad B_n\sim\operatorname{Binomial}(n,1/2),
\qquad \mathbb E\|x_n\|_2^2=r^n.
\]
The stronger pathwise fact is that the counts can be realized jointly using independent fair Bernoulli increments, and \((Z_n)_{n\ge0}\) is a nonnegative martingale converging to zero almost surely. Thus \(\Pr(\sup_{n\ge0}Z_n\ge\lambda)\le1/\lambda\) for every \(\lambda>1\).

**Sharp classification.** Equality holds for some \(\lambda>1\) if and only if there exists an integer \(d\ge3\) with \(q=r^d\). For each integer \(d\ge3\), this equation has exactly one solution \(q_d\in(0,1)\), equivalently \(q_d=r_d^d\), where \(r_d\in(0,1)\) is the unique nonunit root of
\[
r_d^d-2r_d+1=0.
\]
At the angle \(q=q_d\), the *complete* all-time tail is
\[
\boxed{\Pr\!\left(\sup_{n\ge0}Z_n\ge\lambda\right)=r_d^{\left\lceil\log(\lambda)/\log(1/r_d)\right\rceil}\quad(\lambda>1).}
\]
Consequently, the Ville inequality is attained **exactly** for \(\lambda=r_d^{-m}\), with integers \(m\ge1\), where its probability equals \(r_d^m=1/\lambda\). For every other pair \((q,\lambda)\) with \(0<q<1\) and \(\lambda>1\), the inequality is strict.

For the first member, \(d=3\),
\[
r_3=(\sqrt5-1)/2,\quad q_3=\sqrt5-2,\quad
\Pr\bigl(\sup_n Z_n\ge r_3^{-m}\bigr)=r_3^m.
\]

## Assumptions and scope

All vectors and matrices are real, and all projections are exact orthogonal projections. Both rows of \(A\) have unit Euclidean norm, are linearly independent, and are sampled independently and uniformly with replacement. The initial error \(x_0=e_2\) lies in the nullspace of the first row; the exact solution is zero. The ambient space is \(\mathbb R^2\). The time horizon is infinite, while \(m,d,n\) above are nonnegative or positive integers only in the ranges explicitly given. The rate \(r=(1+q)/2\) is *instance- and initialization-specific*, and is not the general operator-norm rate \(\rho=(1+\sqrt q)/2\).

## Proof

**1. Independent switch indicators.** Define \(I_0=1\) and let \(I_j\in\{1,2\}\) be the chosen row at iteration \(j\ge1\). The projection \(P_i=I-a_i^{\mathsf T}a_i\) has one-dimensional image orthogonal to \(a_i\). Starting from \(x_0=e_2\in\operatorname{im}P_1\), applying the same row as last time leaves the vector unchanged. Switching between the two rows multiplies its Euclidean norm by \(|a_1\cdot a_2|=\sqrt q\) (the same cosine is the overlap of their one-dimensional nullspaces). Thus, with \(D_j=\mathbf1\{I_j\ne I_{j-1}\}\),
\[
\|x_n\|_2^2=q^{\sum_{j=1}^nD_j}.
\]
For each \(n\), the map from \((I_1,\ldots,I_n)\) to \((D_1,\ldots,D_n)\) is a bijection on \(\{1,2\}^n\) and preserves the uniform probability \(2^{-n}\). The \(D_j\) are therefore independent \(\operatorname{Bernoulli}(1/2)\) random variables, simultaneously for all \(j\). The distribution and mean in the Finding follow. Additionally, \(\mathbb E\|x_n\|_2^4=((1+q^2)/2)^n\), so the squared-error variance equals \(((1+q^2)/2)^n-r^{2n}\).

**2. Martingale and its limit.** From the independent increments, conditionally on the past, \(\|x_{n+1}\|_2^2/\|x_n\|_2^2\) equals \(1\) or \(q\), each with probability \(1/2\). Since \(r=(1+q)/2\), \(Z_n\) is a mean-one nonnegative martingale. The strong law gives \(n^{-1}\log Z_n\to\frac12\log q-\log r<0\) almost surely, because \(r>\sqrt q\) for \(0<q<1\). Therefore \(Z_n\to0\) almost surely.

**3. Crossing probabilities and overshoots.** Let \(\lambda>1\), and set \(\tau=\inf\{n\ge0:Z_n\ge\lambda\}\). The only upward multiplier of \(Z_n\) is \(1/r\), while the other multiplier \(q/r<1\). Hence \(0\le Z_{\tau\wedge N}\le\lambda/r\) for all \(N\). Optional stopping at the bounded time \(\tau\wedge N\), followed by bounded convergence as \(N\to\infty\), gives the **exact identity**
\[
1=\mathbb E\bigl[Z_\tau\,\mathbf1\{\tau<\infty\}\bigr].
\]
Thus \(\Pr(\tau<\infty)\le1/\lambda\), with equality precisely when every crossing lands at \(Z_\tau=\lambda\) almost surely on \(\{\tau<\infty\}\) (no strict overshoot).

Write \(a=\log(1/r)>0\) and \(b=\log(r/q)>0\). The logarithmic process has independent increments \(+a\) and \(-b\), equally likely. If equality holds at \(\lambda=e^h\), the positive-probability path consisting exclusively of \(+a\) steps must hit without overshoot. Therefore \(h=ma\) for an integer \(m\ge1\). Next, the positive-probability path with one \(-b\) step followed by sufficiently many \(+a\) steps must also hit without overshoot. Since its first hit is at \(-b+\lceil m+b/a\rceil a\), this forces \(b/a\) to be an integer. Conversely, if \(b/a=d-1\) is an integer and \(h=ma\), the entire log process lies on the lattice \(a\mathbb Z\) and can cross an upper lattice boundary only by its \(+a\) step; hence every crossing is exact. Now
\[
\frac ba=\frac{\log q}{\log r}-1>1,
\]
where the last inequality follows from \(r>\sqrt q\). Therefore \(b/a=d-1\) is integral precisely when \(d\ge3\) and \(q=r^d\), proving the necessary-and-sufficient assertion.

**4. Exactly one nontrivial angle at each integral slope.** Set \(r=q^{1/d}\). The equation \(q=r^d\) and the definition \(r=(1+q)/2\) give \(f_d(r)=r^d-2r+1=0\). On \([0,1]\), \(f_d(0)=1\), \(f_d(1)=0\), \(f_d'(1)=d-2>0\), and \(f_d''(r)>0\) in \((0,1)\). Strict convexity and the negative values immediately to the left of \(1\) give one and only one other root \(r_d\in(0,1)\). For this root, the upper log increments are exactly \(+a\), so for any \(\lambda>1\), the crossing event is identical to crossing the lattice level \(r_d^{-m}\) with \(m=\lceil\log(\lambda)/a\rceil\). The exact crossing probability from step 3 is \(r_d^m\), completing the full tail formula and classification.

## Verification

Run `python3 verify_exact.py` using Python 3 standard-library modules. The script checks exact \(\mathbb Q(\sqrt5)\) algebra for \(d=3\), exhaustively tests all \(2^n\) row sequences for \(0\le n\le10\) at three nondegenerate angles, verifies all associated binomial histograms, and computes exact dyadic finite-horizon crossing probabilities for \(d=3,4,5\) and several levels. It also numerically isolates the unique interior algebraic root for \(3\le d\le7\). These finite checks supplement but do not replace the infinite-time optional-stopping and no-overshoot proof above.

## Relationship to prior work

Anderson, Collins, Haddock, Lok and Rebrova [1, Sections 2.2–2.3] prove general error-concentration and time-uniform high-probability bounds for randomized iterative methods, including Kaczmarz, by a supermartingale argument. They give a generic lower bound from repeated row choices; they do not present the two-row binomial law or the exact characterization of equality cases developed here. Their general \(\rho\) for this two-row matrix is \((1+\sqrt q)/2\), strictly larger than the instance-specific \(r\) used here; **this result does not claim that their bound at rate \(\rho\) is attained**.

Classical Ville/Doob inequalities and the overshoot criterion are not new. Howard, Ramdas, McAuliffe and Sekhon [2, Section 5.1, Proposition 3] study the sharpness of time-uniform martingale boundaries and identify zero overshoot as the equality mechanism. The new part here is the exact realization by a normalized full-rank Kaczmarz instance and the complete discrete classification of all row angles and confidence levels with equality. The general overshoot result does not specify these matrix geometries or compute the joint error law.

## Limitations

This is a family of two-equation, exact-arithmetic examples with one specified initialization. It neither improves general high-dimensional Kaczmarz concentration bounds nor proves that the operator-norm-rate bound in [1] is sharp. Generic choices of \(q\) have strictly smaller crossing probabilities than the simple \(1/\lambda\) bound at every threshold. The strictness classification concerns the precise *mean-normalized process* defined here. No optimal sampling policy, noisy system, stopping algorithm, or implementation-level convergence claim is established. General sharp martingale theory supplies the mechanism; historical priority for the specific Kaczmarz specialization remains subject to broader literature review.

## References

1. T. Anderson, M. Collins, J. Haddock, J. Lok and E. Rebrova, *Beyond Expectation: Concentration Inequalities for Randomized Iterative Methods*, arXiv:2511.20877v1, first publicly submitted 2025-11-25, https://arxiv.org/html/2511.20877.
2. S. R. Howard, A. Ramdas, J. McAuliffe and J. Sekhon, *Time-uniform Chernoff bounds via nonnegative supermartingales*, Probability Surveys 17 (2020), 257–317, arXiv:1808.03204, https://arxiv.org/html/1808.03204v8, especially Section 5.1.
3. W. M. Koolen-Wijkstra, M. F. Pérez-Ortiz and T. Lardy, *A generalisation of Ville's inequality to monotonic lower bounds and thresholds*, Statistics & Probability Letters 229 (2026), 110577, https://doi.org/10.1016/j.spl.2025.110577. This is general background on sharpness, not a claimed source of this example.
