# Majorization and dimension laws for Crank–Nicolson positivity on weighted Boolean cubes

## Finding
Let \(d\ge 2\) and let \(w_1,\ldots,w_d\ge0\) have fixed sum \(W>0\). On the Boolean cube \(\{0,1\}^d\), give every edge flipping coordinate \(i\) conductance \(w_i\). Denote the weighted graph Laplacian by \(L_w\), and set
\[
T_w(h)=\left(I+\frac h2L_w\right)^{-1}\left(I-\frac h2L_w\right),\qquad h\ge0.
\]
Write \(r=\#\{i:w_i>0\}\) and \(w(S)=\sum_{i\in S}w_i\). Define the normalized resolvent-return function
\[
F_w(h)=2^{-d}\sum_{S\subseteq\{1,\ldots,d\}}\frac1{1+h\,w(S)}.
\]
If \(r\ge2\), there is a unique finite positive \(H(w)\) satisfying \(F_w(H(w))=1/2\), and
\[
T_w(h)\text{ is entrywise nonnegative}\quad\Longleftrightarrow\quad 0\le h\le H(w).
\]
If \(r=1\), the update is entrywise nonnegative for every finite \(h\ge0\), so put \(H(w)=\infty\).

The step frontier obeys a strict **majorization law**. If \(w\) majorizes \(v\) (both are nonnegative vectors of length \(d\) with total \(W\)), then
\[
H(w)\ge H(v),
\]
with strict inequality unless the vectors differ by a permutation. In particular, the unique minimizing rate allocation up to permutation is the isotropic choice \(w_i=W/d\), and the largest allowable step over all nonnegative allocations is unbounded, attained when all conductance is assigned to one coordinate.

For the isotropic allocation write \(t_d=W H(W/d,\ldots,W/d)\). It is the unique positive root of the \(d+1\)-term equation
\[
2^{-d}\sum_{j=0}^d\binom dj\frac1{1+t_d j/d}=\frac12.
\]
The normalized sharp thresholds obey
\[
1+\sqrt5=t_2>t_3>t_4>\cdots>2,
\]
and have the two-correction asymptotic law
\[
\boxed{\displaystyle t_d=2+\frac1d+\frac5{4d^2}+O(d^{-3})}\qquad(d\to\infty).
\]
Thus the exact least positivity timestep for a fixed total rate \(W\) approaches \(2/W\), from above, with explicit finite-dimensional corrections. For dimension two, \(w=(a,b)\) with \(a,b>0\), the critical step is also the unique positive root of
\[
ab(a+b)H^3-2(a+b)H-2=0.
\]
As \(a\downarrow0\) with \(b=W-a\), the threshold diverges according to
\[
H(a,W-a)=\sqrt{\frac{2}{a(W-a)}}+\frac1{2W}+O_W(\sqrt a).
\]

## Assumptions and scope
Coordinate conductance \(w_i\) is the rate on **each** edge flipping coordinate \(i\), so \(W\) fixes the global conductance budget up to the common factor \(2^{d-1}\). Zero weights are allowed, and the corresponding graph may be disconnected. The update is the exact completed Crank–Nicolson (implicit trapezoidal) matrix for the autonomous graph diffusion equation \(\dot u=-L_wu\), with the standard step normalization displayed above. All comparisons use identical dimension and total rate, except for the explicitly normalized dimension sequence.

Majorization means that, after sorting both weight vectors in nonincreasing order, every initial partial sum of \(w\) is at least the corresponding initial partial sum of \(v\), with equal total sum. Strictness is understood up to coordinate permutation. The conclusion concerns entrywise positivity of the **completed step**, not positivity at internal numerical stages or unconditional stability/error estimates.

## Proof
**(1) Positivity reduces to one scalar return.** Put \(R_w(h)=(I+hL_w/2)^{-1}\). The rational identity
\[
T_w(h)=2R_w(h)-I
\]
is exact. The Laplacian generates a stochastic positive semigroup, and
\[
R_w(h)=\int_0^\infty e^{-s}e^{-shL_w/2}\,ds
\]
is entrywise nonnegative and row-stochastic. Therefore all off-diagonal entries of \(T_w(h)\) are nonnegative. The weighted cube is translation-invariant, so all diagonal entries of \(R_w(h)\) coincide.

For each subset \(S\subseteq\{1,\ldots,d\}\), the Walsh character \(\chi_S(x)=(-1)^{\sum_{i\in S}x_i}\) is an eigenvector of \(L_w\) with eigenvalue \(2w(S)\). Fourier inversion therefore gives precisely \(F_w(h)\) for the common diagonal of \(R_w(h)\). Hence \(T_w(h)\ge0\) entrywise if and only if \(F_w(h)\ge1/2\). For \(W>0\), \(F_w\) is strictly decreasing on \([0,\infty)\), with \(F_w(0)=1\) and \(\lim_{h\to\infty}F_w(h)=2^{-r}\). This proves the finite unique cutoff for \(r\ge2\). For \(r=1\), the single active rate gives \(F_w(h)=\bigl(1+(1+hW)^{-1}\bigr)/2>1/2\) for finite \(h\), proving unconditional positivity.

**(2) Majorization with strictness.** Let \(f_h(z)=(1+hz)^{-1}\), strictly convex for \(h>0\). Consider two coordinate weights \(x,y\ge0\) with fixed sum \(s=x+y\). Conditional on the remaining coordinate subset having total weight \(b\), averaging over inclusion or exclusion of these two coordinates contributes
\[
\frac14\bigl[f_h(b)+f_h(b+s)+f_h(b+x)+f_h(b+y)\bigr].
\]
The last two terms are strictly minimized by \(x=y=s/2\); more generally their sum strictly increases when \(|x-y|\) increases. Repeated pairwise Robin-Hood averaging (the finite characterization of majorization) therefore shows \(F_w(h)\ge F_v(h)\) when \(w\) majorizes \(v\), with strict inequality for \(h>0\) unless the vectors are permutations. At the crossing \(H(v)\), a strictly larger return at the same step moves the decreasing crossing strictly rightward. This proves the threshold order, including the \(\infty\) boundary case. Every vector majorizes the equal vector, with equality only for that vector, proving the unique isotropic minimum.

**(3) Dimension monotonicity and exact two-dimensional endpoint.** For isotropic weights let \(J_d\sim\operatorname{Bin}(d,1/2)\). The cutoff equation is \(\mathbb E f_t(J_d/d)=1/2\), where \(f_t(z)=(1+tz)^{-1}\). Strict Jensen convexity gives \(\mathbb E f_2(J_d/d)>f_2(1/2)=1/2\); hence \(t_d>2\). Take \(d+1\) independent fair Bernoulli variables and form the mean after deleting a uniformly random one. Its conditional expectation given the whole sample is the full-sample mean. Strict Jensen therefore gives
\[
\mathbb E f_t(J_{d+1}/(d+1))<\mathbb E f_t(J_d/d),\qquad t>0.
\]
As each return decreases strictly in \(t\), it follows that \(t_{d+1}<t_d\). For \(d=2\), clearing the strictly positive denominators in the cutoff equation produces \(t^3-8t-8=0\), whose positive root is \(1+\sqrt5\). By the law of large numbers, \(J_d/d\to1/2\) in probability. Bounded convergence together with the monotone bounded root sequence yields \(t_d\to2\).

**(4) Sharp finite-size correction.** Set \(Y_d=J_d/d-1/2\). Symmetry and binomial moments give
\[
\mathbb EY_d^2=\frac1{4d},\qquad
\mathbb EY_d^4=\frac3{16d^2}-\frac1{8d^3},\qquad
\mathbb EY_d^6=O(d^{-3}).
\]
Uniformly for \(t\) in a fixed neighborhood of \(2\), expand \((1+t(1/2+Y_d))^{-1}\) about \(Y_d=0\). The geometric series is absolutely and uniformly convergent for \(|Y_d|\le1/2\); odd expectations vanish and its order-six remainder has expectation \(O(d^{-3})\). Substituting \(t=2+a/d+b/d^2\) yields
\[
\mathbb E\frac1{1+tJ_d/d}-\frac12
=\frac{1-a}{8d}+\frac{a^2+a+3-4b}{32d^2}+O(d^{-3}).
\]
Choosing \(a=1\) and \(b=5/4\) cancels the first two orders. The derivative with respect to \(t\) tends uniformly to \(-1/8\) near \(2\), so the true root differs from this approximation by \(O(d^{-3})\).

**(5) Two-coordinate exact threshold and singular limit.** With \(d=2\) and weights \(a,b>0\), the cutoff equation becomes
\[
\frac1{1+ah}+\frac1{1+bh}+\frac1{1+(a+b)h}=1.
\]
Multiplying by its positive denominator simplifies it to \(ab(a+b)h^3-2(a+b)h-2=0\). Uniqueness of the positive root follows from the already-proved monotonic return, not an unproved cubic-root count. If \(p=ab\) and \(W=a+b\), the cubic is \(ph^3-2h-2/W=0\). At \(h_0=\sqrt{2/p}\), the left side equals \(-2/W\) and its derivative is \(4\). A Taylor expansion about \(h_0\), with the second derivative of order \(\sqrt p\) there, gives \(h=h_0+1/(2W)+O_W(\sqrt p)\), proving the stated \(a\downarrow0\) law.

## Verification
The accompanying pure-standard-library program `verify.py` checks exact rational Walsh resolvent kernels against directly inverted matrices for two through four coordinates, verifies strict rational pair-balancing comparisons, checks the scalar positivity criterion and mass conservation, and recomputes two binomial moment identities exactly. It also locates critical steps numerically for isotropic dimensions up to four hundred, tests strict dimension ordering in a finite range, checks the two-rate cubic sign identity, and tests the singular asymptotic regime. These calculations are finite consistency checks, **not** proofs of the statements for arbitrary dimension or real weights.

To run from the package directory: `python verify.py`. No third-party dependencies or external files are required.

## Relationship to prior work
General Runge–Kutta positivity-radius results of Horváth and the analysis of Crank–Nicolson diffusion by Reisinger–Whitley provide the numerical-method context. Higueras–Roldán explicitly classify positivity thresholds for one-dimensional Dirichlet heat discretizations, not Boolean products. A published *resolvent-return law for Crank–Nicolson positivity on reversible Markov chains* already proves the general identity \(T=2R-I\), the return-diagonal criterion, and existence of finite fixed-chain thresholds; these statements are acknowledged as prior tools, not new claims.

The contribution here is the **rate-majorization extremal theorem on weighted Cartesian binary products**, including strict optimizer classification, a sharp decreasing normalized dimension sequence, its two correction terms, and the exact singular two-rate boundary law. The cited general results do not provide these weight-allocation and binomial dimension comparisons. The closest accessible historical claim about an unweighted two-dimensional cycle torus compares *period lengths* for that different graph family rather than *coordinate-rate allocations* on Boolean cubes.

## Limitations
The theorem assumes coordinate-homogeneous nonnegative rates. It does not optimize over completely independent weights on every cube edge; symmetrizing arbitrary rates is **not** claimed to preserve or optimize this positivity threshold. A positivity threshold is not a timestep needed for accuracy, nor is a longer positivity interval necessarily a better integrator for stiff decay. The asymptotic statement keeps total directional conductance \(W\) fixed as dimension grows. No characterization is claimed for nonlinear or time-varying diffusion. The strict comparison invokes the standard finite majorization theorem, whose elementary pair-averaging step is proved explicitly here. An equivalent specialized weighted-cube statement in unindexed matrix-function literature cannot be ruled out by finite searches.

## References
1. C. Reisinger and A. Whitley, *The impact of a natural time change on the convergence of the Crank–Nicolson scheme*, arXiv:1210.5487, initially public 19 October 2012. https://arxiv.org/abs/1210.5487
2. I. Higueras and T. Roldán, *A new insight on positivity and contractivity of the Crank–Nicolson scheme for the heat equation*, arXiv:2301.01066, initially public 3 January 2023. https://arxiv.org/abs/2301.01066
3. Z. Horváth, *Positivity of Runge–Kutta and diagonally split Runge–Kutta methods*, Applied Numerical Mathematics 28 (1998), 309–326. DOI: 10.1016/S0168-9274(98)00050-6.
4. *A resolvent-return law for Crank–Nicolson positivity on reversible Markov chains*, publicly available research record, identifier d475df91cd2a (2026).
