# Sharp Wiener extension of second-order Hamming data and its arithmetic contact staircase

## Finding
Let \(n\ge 2\) be an integer, let \(G=(\mathbb Z/2\mathbb Z)^n\), and fix \(-1\le t\le1\). Among **all complex-valued functions** \(m:G\to\mathbb C\) satisfying \(m(x)=1\) at Hamming weights zero and one and \(m(x)=t\) at Hamming weight two, consider the Wiener-algebra extension problem
\[
\mathcal E_n(t)=\min_m\sum_{S\subseteq[n]}|\widehat m(S)|,
\qquad \widehat m(S)=2^{-n}\sum_{x\in G}m(x)(-1)^{\sum_{i\in S}x_i}.
\]
Put
\[
d=1-t,\qquad Q=\frac{n(n-1)d}{4},\qquad r=\left\lfloor\frac{(n-1)d}{4}\right\rfloor,\qquad D=(n-r)(n-r-1).
\]
**The sharp extension constant is**
\[
\boxed{\mathcal E_n(t)=1+\frac{2(Q-r(r+1))}{D}.}
\]
It is attained by a real coordinate-permutation-invariant function whose nonzero Fourier coefficients occupy **at most three Hamming layers**: spectral layers \(r\), \(r+1\), and \(n\). If \(b_j\) is the sum of its Fourier coefficients on weight-\(j\) characters, their exact values are
\[
\boxed{b_r=\frac{n(r+1)-Q}{n-r},\qquad
 b_{r+1}=\frac{Q-nr}{n-r-1},\qquad
 b_n=-\frac{r b_r+(r+1)b_{r+1}}n.}
\]
For the constructed optimizer every weight-\(j\) Fourier coefficient is \(b_j/\binom nj\); other coefficients vanish. The coefficients on layers \(r\) and \(r+1\) are nonnegative, and the top-layer coefficient is nonpositive. At coinciding or vanishing layers, contributions are combined; for \(n\ge2\) the three index values are distinct.

The function \(d\mapsto\mathcal E_n(1-d)\), for \(0\le d\le2\), is a continuous, convex, piecewise-affine curve. Its interior slope changes occur precisely at
\[
\boxed{d=\frac{4j}{n-1}\in(0,2),\qquad j=1,2,\ldots,\left\lfloor\frac{n-1}{2}\right\rfloor.}
\]
The slope on the sector with active integer \(r\) is \(n(n-1)/(2(n-r)(n-r-1))\), and successive slopes strictly increase. The formula includes all endpoints, including \(t=1\), where the norm equals one.

## Assumptions and scope
The Fourier characters are \(\chi_S(x)=(-1)^{\sum_{i\in S}x_i}\), with the displayed probability-normalized transform and inversion \(m(x)=\sum_S\widehat m(S)\chi_S(x)\). The target data prescribe **only** the values on the radius-two Hamming ball; there are no constraints whatsoever on values at weight three or above, on pointwise positivity, or on the sign of Fourier coefficients. The norm is the sum of absolute values of all \(2^n\) Fourier coefficients. The scalar \(t\) is real in the stated closed interval; no extrapolation to other targets is claimed. The index \(r\) always lies in \(\{0,\ldots,\lfloor(n-1)/2\rfloor\}\), so \(D>0\).

## Proof
**1. Reduction to a signed Hamming-weight moment problem.** The coordinate-permutation group preserves the interpolation constraints and permutes Walsh coefficients. Averaging any feasible \(m\) over this group preserves the targets and cannot increase its Wiener norm by convexity. Thus it is sufficient to produce a radial solution and a global lower bound. For a radial extension, write
\[
b_j=\sum_{|S|=j}\widehat m(S),\qquad 0\le j\le n.
\]
At weight zero and one, the character averages on a spectral shell of weight \(j\) are \(1\) and \(1-2j/n\). At weight two the average is \(1-4j(n-j)/(n(n-1))\). Consequently the three prescribed values are equivalent to
\[
\sum_{j=0}^n b_j=1,\qquad \sum_{j=0}^n j b_j=0,\qquad
\sum_{j=0}^n j(n-j)b_j=Q.
\tag{1}
\]
Radiality means each Fourier coefficient of weight \(j\) equals \(b_j/\binom nj\), so the Wiener norm is \(\sum_j|b_j|\). Equation (1) is valid for complex coefficients as well. It can alternatively be obtained by evaluating the degree-two binary Krawtchouk character averages explicitly.

**2. Feasible three-layer certificate.** Since \(Q/n=(n-1)d/4\), the chosen floor \(r\) gives \(nr\le Q<n(r+1)\) except possibly at the endpoint, where weak inequalities suffice. Define \(b_r,b_{r+1},b_n\) as in the Finding and set every other aggregate coefficient to zero. The two denominators are positive, while \(b_r,b_{r+1}\ge0\) and \(b_n\le0\). Direct algebra gives
\[
 b_r+b_{r+1}+b_n=1,\qquad
 r b_r+(r+1)b_{r+1}+n b_n=0,
\]
and
\[
r(n-r)b_r+(r+1)(n-r-1)b_{r+1}=Q.
\]
This proves (1) and the interpolation property. Its Wiener norm is \(b_r+b_{r+1}-b_n=1-2b_n\). Substituting the formulas and simplifying yields the claimed value \(1+2(Q-r(r+1))/D\).

**3. A uniform dual polynomial.** Define for every integer \(0\le j\le n\)
\[
 P_r(j)=1-\frac{2(j-r)(j-r-1)}{D}.
\tag{2}
\]
The product of consecutive integer offsets is always nonnegative. It is a convex quadratic in \(j\), whose maximum on \([0,n]\) is attained at an endpoint. Since \(r\le(n-1)/2\),
\[
r(r+1)\le(n-r)(n-r-1)=D.
\]
Hence \(0\le(j-r)(j-r-1)\le D\) at every integer \(j\), and therefore \(|P_r(j)|\le1\). At the three active spectral weights \(r,r+1,n\), the polynomial takes exactly the signs \(+1,+1,-1\). Using
\[
 (j-r)(j-r-1)=(n-2r-1)j-j(n-j)+r(r+1),
\]
any feasible \(b\) obeying (1) satisfies the exact dual identity
\[
\sum_{j=0}^n b_jP_r(j)=1+\frac{2(Q-r(r+1))}{D}.
\tag{3}
\]
The right side is real. The triangle inequality and (2) show
\[
 \sum_{j=0}^n|b_j|\ge\left|\sum_{j=0}^nb_jP_r(j)\right|
 =1+\frac{2(Q-r(r+1))}{D}.
\]
This applies to every radial complex extension; by the symmetrization step, the same bound applies to **all** complex extensions, even without coordinate-permutation invariance. The three-layer constructed extension attains equality in every step, proving sharpness.

**4. Contact staircase.** The floor \(r=\lfloor(n-1)d/4\rfloor\) is constant between consecutive transition values. In such a sector the closed formula is affine in \(d\), with slope \(n(n-1)/(2D)\). When \(r\) increases by one, \(D\) decreases strictly, so the slope increases. Continuity at each boundary follows directly by substituting \(Q=nr\) in the two adjacent formulas, or because the constructed optimizer has one vanishing interior-layer coefficient there. The strict slope changes are precisely those displayed inside \((0,2)\). This completes the theorem.

## Verification
The standalone Python 3 standard-library file `check.py` reconstructs the exact rational primal moments, the dual polynomial bounds, the primal-dual equality and the prescribed values for dimension \(2\le n\le100\) and 41 rational target values, augmented with all transition parameters. It additionally performs an **independent explicit Walsh transform and inverse transform** for every \(2\le n\le7\) at five rational targets. The recorded marker is `HAMMING_WIENER_EXACT_CHECKS_OK 406585`. This is reproducible finite corroboration. The all-dimensional theorem follows from the exact polynomial proof above, not from finite testing.

For example, at \(n=4\), the single interior switch occurs at \(d=4/3\). At \(t=0\) (so \(d=1\)) the optimum is \(\mathcal E_4(0)=3/2\), and the aggregate coefficients are \(b_0=1/4\), \(b_1=1\), \(b_4=-1/4\). This example can be checked directly on the 16-point cube.

## Relationship to prior work
The finite-group Fourier algebra and symmetry reduction are standard; the binary Krawtchouk transform is classical. Feinsilver and Schott (2018) develop the Krawtchouk transform and convolution formalism, but do not solve the minimum-Wiener-norm extension of prescribed zero/one/two Hamming layers. González-Pérez, Parcet, Pérez García and Wang (2026) discuss radial multiplier norms and Fourier–Schur transfer phenomena on trees; their different infinite-tree, \(L_p\)/Schatten setting motivates examination of exact finite radial norms but does not cover this Hamming-cube interpolation claim.

The most closely related published finite-cube result inspected in full, *Sharp positive-definite mass of q-ary Hamming two-balls*, is a **support-constrained positive-definite maximization** problem, with a nonnegative Fourier quadratic. In contrast, the present problem prescribes time-domain local data and permits signed Fourier measures at arbitrary spectral weights. Neither optimization, constraint set, nor the displayed phase diagram is an implication of the other. Likewise, the complete quadratic Walsh concentration spectrum on Hamming balls concerns singular values of a restricted low-frequency basis, and the unweighted two-shell Walsh tight-design theorem concerns Gram isometry, rather than a minimal global Fourier total-variation extension. These comparisons check mathematical coverage, not merely title overlap.

## Limitations
The parameter interval is \(-1\le t\le1\). A real radial optimizer is explicitly constructed, but **not every optimal extension** (including nonradial ones) is classified. No claim is made that this formula yields a new general Fourier algebra factorization theorem, arbitrary alphabet, arbitrary local target profile, or an interpolation constant with a different Fourier normalization. Prior unpublished or unindexed discrete moment interpolation theorems may contain an equivalent formula. The cited 2026 radial tree preprint was accessible in abstract form, not fully inspected, and is not used as a premise of the proof. No independent mathematical validation is represented.

## References
1. A. González-Pérez, J. Parcet, J. Pérez García and S. Wang, *Radial Schur multipliers on trees and the failure of Fourier–Schur transference*, arXiv:2610.15881v1, first public version 2026-10-11, https://arxiv.org/abs/2610.15881.
2. P. Feinsilver and R. Schott, *Krawtchouk transforms and convolutions* (2018), https://link.springer.com/article/10.1007/s13373-018-0132-2.
3. *Sharp positive-definite mass of q-ary Hamming two-balls*, published research note (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-positive-definite-mass-of-q-ary-hamming-two-balls--443142350f41.
4. *Exact quadratic Walsh concentration on Hamming balls and the sharp minimal-sampling instability*, published research note (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-quadratic-walsh-concentration-on-hamming-balls-and-the-sha--52fb6118ea85.
5. *Square-law classification for unweighted two-shell Walsh sampling*, published research note (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-square-law-classification-for-unweighted-two-shell-walsh-samplin--e2a831d987e5.
