# Exact nine-state computation and logarithmic path-variation instability of finite Haar soft thresholding

## Finding
Let \(d\ge1\), \(N=2^d\), and let \(H_N\) be the real orthogonal discrete Haar transform, including the normalized constant vector. Fix \(\lambda>0\). Define \(T_{d,\lambda}\) by leaving the constant Haar coefficient unchanged, applying scalar soft thresholding \(\eta_\lambda(z)=\operatorname{sgn}(z)(|z|-\lambda)_+\) to every other Haar coefficient, and inverting the transform. On real length-\(N\) vectors put
\[
 V_N(x)=\sum_{i=0}^{N-2}|x_{i+1}-x_i|.
\]
Then the **sharp global two-input path-variation coefficient**
\[
 C_d=\sup_{V_N(x-y)>0}\frac{V_N(T_{d,\lambda}x-T_{d,\lambda}y)}{V_N(x-y)}
\]
is independent of the positive threshold \(\lambda\), and is given exactly at every depth by the nine-state integer recurrence below. It requires \(O(N)\) integer operations, without enumeration of Haar active sets.

For every dyadic size \(n=2^r\), each interior cut \(1\le k<n\), and \(p,q\in\{-1,0,1\}\), define integers \(R_n^{p,q}(k)\). For \(n=2\), use the center formula. For \(n=2s\), set
\[
 R_n^{p,q}(k)=\begin{cases}
 \max\{2R_s^{p,1}(k),\ 2R_s^{p,-1}(k)+k(2-p+q)\},&k<s,\\
 \max\{0,\ n+s(q-p)\},&k=s,\\
 \max\{2R_s^{-1,q}(k-s),\ 2R_s^{1,q}(k-s)+(n-k)(2-p+q)\},&k>s.
 \end{cases}
\]
The theorem is
\[
 \boxed{\displaystyle C_d=\frac1{2^d}\max_{1\le k<2^d}R_{2^d}^{0,0}(k).}
\]
In particular the first eight exact coefficients are
\[
 1,\quad\frac32,\quad2,\quad\frac{21}{8},\quad3,\quad
 \frac{117}{32},\quad4,\quad\frac{597}{128}.
\]
Moreover, for \(d\ge3\),
\[
 \boxed{\displaystyle \frac43\left\lfloor\frac d3\right\rfloor+\frac47\le C_d\le2d.}
\]
Thus \(C_d=\Theta(d)=\Theta(\log N)\); there is no dimension-independent path-variation Lipschitz bound for this otherwise Euclidean-nonexpansive nonlinear shrinker. Every finite-depth coefficient in the recurrence is sharp (attainable as a two-input quotient by distinct real vectors).

## Assumptions and scope
Coordinates are ordered \(0,\ldots,N-1\), with *nonperiodic* adjacent variation and no boundary edge. The discrete Haar basis contains one wavelet for every aligned dyadic interval \(I=[a,a+n)\) of length \(n\ge2\): it takes \(+1/\sqrt n\) on the first half, \(-1/\sqrt n\) on the second half, and zero elsewhere. The coefficient of the constant vector is not thresholded. The threshold \(\lambda\) is a fixed positive real number, identical for all nonconstant coefficients. All vectors and coefficients are real. A depth \(d\) involves \(N=2^d\) signal entries, not \(d\) entries.

## Proof
**1. Reduction to arbitrary Haar subprojections.** The soft-threshold map is continuous and affine on each region where every detail coefficient lies strictly inside or outside \([-\lambda,\lambda]\). Its derivative there is the orthogonal Haar coordinate projector \(P_S\) onto the constant and an arbitrary selected subset \(S\) of detail wavelets. Every such subset occurs on a nonempty open region: choose each selected coefficient \(2\lambda\) and each unselected coefficient zero. The line-segment formula for a continuous piecewise-affine map shows that its global Lipschitz coefficient in \(V_N\) is \(\max_S\|P_S\|_{V_N\to V_N}\). Conversely, at any point strictly within the chosen region, a sufficiently small perturbation realizes the corresponding projector and norm quotient, proving attainment of the finite-depth coefficient.

Every linear \(P_S\) sends constants to constants. Let \(h_k\) have \(k\) leading zero entries and \(N-k\) trailing ones; then \(V_N(h_k)=1\). Every input vector is a constant plus its first differences multiplied by these step vectors, so the triangle inequality proves
\[
 \|P_S\|_{V_N\to V_N}=\max_{1\le k<N}V_N(P_Sh_k).
\]
The constant Haar component does not affect variation. For fixed \(k\), only the wavelets on the unique chain of dyadic intervals whose interiors contain the cut can have nonzero coefficient. Hence the full \(2^{N-1}\)-mask problem reduces to at most \(d\) binary choices per cut.

**2. Endpoint bounds and the nine-state recurrence.** For a dyadic block of length \(n\) and an interior cut \(k\), let \(g\) range over all projections of \(h_k\) onto subsets of the *nonconstant* Haar wavelets supported in that block. Every contributing wavelet has a nonpositive coefficient and, at the rightmost coordinate, a nonnegative reconstructed value; at the leftmost coordinate the reconstructed value is nonpositive. The sum of all such endpoint contributions is exactly the endpoint value of \(h_k\) minus its block mean. Therefore
\[
 -\frac{n-k}{n}\le g_0\le0,\qquad0\le g_{n-1}\le\frac{k}{n}.
\]
Define
\[
 Q_n^{p,q}(k)=\max_g\{V_n(g)+p g_0+q g_{n-1}\},
 \qquad R_n^{p,q}(k)=nQ_n^{p,q}(k).
\]
For \(n=2s\) and \(k<s\), the cut is in the left child. Let \(u\) be the projection using the lower Haar wavelets in that child and set \(a=k/n\). If the root wavelet is inactive, the total variation is \(V_s(u)+u_{s-1}\), the first endpoint is \(u_0\), and the last is zero. If the root wavelet is active, the root contribution is \(-a\) on the left and \(+a\) on the right; the total variation is \(V_s(u)+2a-u_{s-1}\), and the endpoints are \(u_0-a\) and \(a\). The absolute value at the boundary disappears because \(0\le u_{s-1}\le2a\). Maximizing these two options gives
\[
 Q_n^{p,q}(k)=\max\{Q_s^{p,1}(k),\ Q_s^{p,-1}(k)+a(2-p+q)\}.
\]
For \(k>s\), perform the corresponding computation in the right child, now with \(a=(n-k)/n\) and \(-2a\le u_0\le0\), to get
\[
 Q_n^{p,q}(k)=\max\{Q_s^{-1,q}(k-s),\ Q_s^{1,q}(k-s)+a(2-p+q)\}.
\]
When \(k=s\), only the root coefficient can be nonzero, giving \(Q_n^{p,q}(s)=\max\{0,1+(q-p)/2\}\). Multiplying by \(n\) yields exactly the displayed integer recurrence. Finally, \(Q_N^{0,0}\) is the largest output variation among all active sets for the given cut, proving the exact formula. The number of stored states per cut is nine, and summing all dyadic lengths through \(N\) gives \(O(N)\) integer operations.

**3. Quantitative unboundedness.** For \(d\ge3\), put \(m=\lfloor d/3\rfloor\) and choose the cut
\[
 k=\begin{cases}(2^d-1)/3,&d\text{ even},\\(2^d+1)/3,&d\text{ odd}.\end{cases}
\]
Select just the Haar wavelets on the cut chain at levels \(j=0,3,6,\ldots,3(m-1)\), with support length \(s_j=2^{j+1}\). All their intervals are strictly inside the full path (as \(s_j\le N/4\)). The gradient of each selected projected wavelet is supported at its left endpoint, midpoint, and right endpoint. These three-edge support sets are disjoint between selected levels: consecutive support lengths differ by a factor eight, while the cut lies at distance strictly greater than \(s_j/8\) from the midpoint and at least \(s_j/4\) from either endpoint of the larger interval. These inequalities follow directly from \(k\bmod s_j\in\{(s_j\pm1)/3,(2s_j\pm1)/3\}\), with the signs chosen so the expressions are integral, for \(s_j\ge16\); the smallest scale has \(s_0=2\).

The contribution of each selected wavelet to path variation is \(4u_j\), where \(u_j=\min(k\bmod s_j,s_j-(k\bmod s_j))/s_j\). At level zero, \(u_0=1/2\); at all other selected levels, \(u_j\ge(s_j-1)/(3s_j)\). Since the gradient supports are disjoint,
\[
 C_d\ge2+\sum_{h=1}^{m-1}\left(\frac43-\frac{4}{3\cdot2^{3h+1}}\right)
 \ge\frac{4m}{3}+\frac47.
\]
For the upper bound, each step has at most one nonzero detail coefficient per level, and one selected detail contributes variation no more than \(4(1/2)=2\). There are only \(d\) levels; hence \(C_d\le2d\). This proves the asserted logarithmic order of growth.

## Verification
The included `verify_haar_bv.py` uses only exact integer and rational arithmetic. It separately computes the nine-state recurrence through depth fourteen, checks the first exact values stated above, and reconstructs every pertinent Haar mask directly for every cut through depth seven. It also checks the explicit disjoint-scale witnesses and their analytical lower bound through depth fourteen. The checker is a finite corroboration, not a substitute for the all-depth argument in the proof. Run `python verify_haar_bv.py`.

## Relationship to prior work
Donoho and Johnstone's 1994 wavelet-shrinkage work and Donoho's 1995 soft-thresholding paper give foundational nonlinear wavelet denoising, primarily with statistical loss and smoothness guarantees. Cohen–Dahmen–Daubechies–DeVore (2003) explain why BV does not admit an unconditional basis and establish weak coefficient-space estimates, but do not state the present finite, two-input path-variation coefficient or its integer computation. Steidl–Weickert–Brox–Mrázek–Welk (2004) identify equivalences between soft Haar shrinkage and TV diffusion/regularization on two-pixel and multiscale pyramid components; those equivalences concern filtering representations and not the sharp two-input path-variation norm of the whole multiscale filter. Osękowski (2013) studies restricted weak-type estimates for Haar coordinate projections in \(L^p\)-type norms, not path variation. Durand–Froment (2003) give a TV-minimization method for reconstructing wavelet coefficients, rather than the stability modulus of ordinary soft thresholding. The exact dyadic signed \(L^\infty\) endpoint results reported in related work concern another norm and different multipliers, and do not by themselves yield these coefficients. The novelty assessment is based on accessible primary material and searches; historical priority is not independently certified.

## Limitations
The exact recurrence is a computational closed determination, **not** a claimed elementary closed form for every depth. The constants displayed for the first eight depths and the observed pattern at larger tested depths do not establish an unproved all-depth closed-form sequence. The all-depth growth bounds are valid but do not identify the limiting ratio \(C_d/d\). Only standard equal-length dyadic Haar blocks, real signals, a common positive threshold, the unthresholded constant coefficient, and nonperiodic path variation are covered. Statistical expected risk, continuous BV stability under other wavelet families, and multidimensional image variation are not classified. Independent mathematical review has not been performed.

## References
1. D. L. Donoho and I. M. Johnstone, *Ideal spatial adaptation by wavelet shrinkage*, Biometrika 81 (1994), 425–455. https://doi.org/10.1093/biomet/81.3.425 .
2. D. L. Donoho, *De-noising by soft-thresholding*, IEEE Trans. Inf. Theory 41 (1995), 613–627. https://doi.org/10.1109/18.382009 .
3. A. Cohen, W. Dahmen, I. Daubechies, R. A. DeVore, *Harmonic analysis of the space BV*, Rev. Mat. Iberoam. 19 (2003), 235–263. https://doi.org/10.4171/RMI/345 .
4. A. Osękowski, *Sharp inequalities for the Haar system and Fourier multipliers*, Journal of Function Spaces and Applications (2013), article 646012. https://doi.org/10.1155/2013/646012 .
5. G. Steidl, J. Weickert, T. Brox, P. Mrázek and M. Welk, *On the equivalence of soft wavelet shrinkage, total variation diffusion, total variation regularization, and SIDEs*, SIAM J. Numer. Anal. 42 (2004), 686–713. https://doi.org/10.1137/S0036142903422429 .
6. S. Durand and J. Froment, *Reconstruction of wavelet coefficients using total variation minimization*, SIAM J. Sci. Comput. 24 (2003), 1754–1767. https://doi.org/10.1137/S1064827501397792 .
