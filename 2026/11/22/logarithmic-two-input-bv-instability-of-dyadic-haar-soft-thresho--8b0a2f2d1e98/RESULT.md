# Logarithmic two-input BV instability of dyadic Haar soft thresholding

## Finding
Fix an integer \(d\geq1\), let \(n=2^d\), and fix a threshold \(\lambda>0\). On real vectors \(x\in\mathbb R^n\), let \(S_{\lambda,d}\) preserve the constant Haar coefficient and independently soft-threshold every other coefficient of the orthonormal dyadic Haar basis at level \(\lambda\). Set
\[
V(x)=\sum_{i=1}^{n-1}|x_{i+1}-x_i|,
\qquad K_d=\sup_{V(x-y)>0}\frac{V(S_{\lambda,d}x-S_{\lambda,d}y)}{V(x-y)}.
\]
The constant \(K_d\) is independent of the positive threshold, is attained by pairs with arbitrarily small nonzero differences, and has the **exact finite, all-depth formula**
\[
K_d=\max_{1\le j<n}\max_{\varepsilon\in\{0,1\}^d}
\sum_{i=1}^{n-1}\left|\sum_{k=1}^d\varepsilon_k\bigl(q_{j,k}(i+1)-q_{j,k}(i)\bigr)\right|.
\]
Here, for \(s=2^k\), \(L=s\lfloor j/s\rfloor\), \(R=L+s\), and \(m=\min(j-L,R-j)\), the explicitly specified vector \(q_{j,k}\) has value \(-m/s\) on positions \(L+1,\ldots,L+s/2\), value \(m/s\) on positions \(L+s/2+1,\ldots,R\), and zero elsewhere (when \(m=0\), it is identically zero). All positions are numbered from one. Thus the formula involves only cuts and at most \(d\) relevant wavelets per cut, not all Haar subsets.

Exact values, certified by exhaustive integer arithmetic, are
\[
\begin{array}{c|rrrrrrrr}d&1&2&3&4&5&6&7&8\\\hline
K_d&1&3/2&2&21/8&3&117/32&4&597/128\end{array}.
\]
Moreover, for **every** integer \(d\geq1\),
\[
\boxed{\ \lfloor d/4\rfloor\le K_d\le2d\ }.
\]
Consequently \(K_d=\Theta(d)=\Theta(\log n)\): orthogonal Haar soft thresholding is nonexpansive in Euclidean norm, but its two-input first-variation Lipschitz modulus diverges with resolution. The finite formula is an exact algorithm, **not** a claim of a closed-form expression for arbitrary \(d\).

## Assumptions and scope
The vector length is exactly \(n=2^d\). Use the real, standard \(\ell^2\)-orthonormal Haar basis: on each aligned dyadic block \([L+1,L+s]\) with even length \(s\), the associated detail vector equals \(s^{-1/2}\) on its first half, \(-s^{-1/2}\) on its second half and zero elsewhere. The constant vector has entries \(n^{-1/2}\). Scalar soft thresholding is \(\eta_\lambda(t)=\operatorname{sgn}(t)(|t|-\lambda)_+\), with \(\eta_\lambda(0)=0\). The seminorm \(V\) is the unweighted, open-path first-difference variation, without a wraparound edge. No stochastic assumptions on the input are made. Constant vectors are annihilated by \(V\), and \(S_{\lambda,d}\) commutes with addition of constants. In particular the quotient seminorm and the displayed two-input ratio are well-defined.

## Proof
**1. Chamber Jacobians and attainment.** The map is continuous and piecewise affine in the orthonormal Haar coefficient coordinates. At every point strictly away from the finitely many threshold hyperplanes, its derivative is an orthogonal projector \(P_A\) onto the constant vector plus an arbitrary chosen subset \(A\) of detail vectors: active details have scalar derivative one and inactive details have derivative zero. Every such pattern is realized in an open chamber by assigning coefficient magnitudes \(2\lambda\) to active details and zero to inactive details. Any segment between two input vectors decomposes at finitely many hyperplane crossings into affine pieces. Applying the variation triangle inequality on those pieces gives the upper bound by the largest \(V\)-operator norm of a chamber projector. Conversely, a point in a strict chamber permits a sufficiently small perturbation in any chosen direction, so each projector norm is achieved as a finite difference. This proves
\[K_d=\max_A\sup_{V(z)>0}\frac{V(P_Az)}{V(z)}\]
and shows independence of \(\lambda>0\).

**2. All input directions reduce to one jump.** Write \(e^{(j)}=(0,\ldots,0,1,\ldots,1)\) with the transition between positions \(j\) and \(j+1\). Every real vector has the exact decomposition \(z=z_1\mathbf1+\sum_{j=1}^{n-1}(z_{j+1}-z_j)e^{(j)}\), and \(V(z)=\sum_j|z_{j+1}-z_j|\). Each \(P_A\) preserves constants, and variation ignores constants. Hence the sharp \(V\)-norm of \(P_A\) is \(\max_jV(P_Ae^{(j)})\), with equality for an elementary step. Maximizing over \(A\) yields a maximum over cuts \(j\) and active Haar subsets.

**3. Exactly one Haar detail per scale survives each cut.** For an aligned dyadic block not straddling the cut, the step \(e^{(j)}\) is constant on the entire block; therefore its inner product with the zero-mean detail vanishes. At each block length \(s=2^k\) there is at most one straddling block, namely \([L+1,L+s]\). Directly taking the inner product of its Haar detail with the step gives \(-m/\sqrt{s}\), where \(m=\min(j-L,L+s-j)\), and multiplication by the detail yields exactly the vector \(q_{j,k}\) above. Its sign is negative on the block's first half and positive on its second half; this identity also holds when the cut coincides with a block boundary, because then \(m=0\). All irrelevant details vanish. The constant projection has zero variation. Thus only one independent binary selector per scale remains and the displayed exact finite formula follows. At each scale the derivative of \(q_{j,k}\) has at most three nonzero entries, located at the two block ends and its midpoint when those positions are interior to the path; this supports an elementary polynomial-time exact evaluation with a Gray-code update rather than enumerating every Haar mask of size \(2^d-1\).

**4. Upper bound.** The total variation of the length-\(s\) detail response satisfies \(V(q_{j,k})\le4m/s\le2\), with possibly fewer boundary terms on the outermost blocks. The triangle inequality across the at most \(d\) active scales proves \(K_d\le2d\).

**5. Divergent logarithmic lower bound.** First take even \(d\ge4\), and set \(j=(2^d-1)/3\), an integer. Select just the scales \(k=2,6,10,\ldots\) with \(k\le d-2\). For each such even \(k\), modular arithmetic gives \(j\bmod 2^k=(2^k-1)/3\), hence \(m=(2^k-1)/3\). The relevant block has both endpoints strictly within \(1,\ldots,n\), so its variation equals
\[
V(q_{j,k})=\frac43(1-2^{-k})\ge1.
\]
For two successively selected scales, the finer block occupies dyadic child number five (counting from zero) among the sixteen children of its scale-sixteen ancestor. Its left edge, midpoint edge, and right edge therefore cannot coincide with any of the three derivative edges of the larger selected block. The derivative supports for all the selected scales are pairwise disjoint, so no absolute-value cancellation occurs. Consequently this chosen mask has
\[
V\!\left(\sum_{r=0}^{\lfloor d/4\rfloor-1}q_{j,4r+2}\right)
=\sum_{r=0}^{\lfloor d/4\rfloor-1}\frac43\bigl(1-2^{-(4r+2)}\bigr)
\ge\lfloor d/4\rfloor.
\]
For odd \(d\), duplicate each coordinate of a depth-\(d-1\) data vector into two adjacent coordinates and retain the corresponding coarser Haar details. The projector outputs are duplicated similarly and open-path variation is unchanged, so \(K_d\ge K_{d-1}\). Since \(\lfloor d/4\rfloor=\lfloor(d-1)/4\rfloor\) for odd \(d\), the lower bound follows at every depth (trivially for depths below four). The bound, together with Step 4, proves logarithmic divergence.

## Verification
The companion standard-library `verify.py` implements the step-response formula using integers after multiplying by \(n\). It enumerates **every** cut and **every relevant active mask** for depths \(1\le d\le8\), yielding the eight displayed exact rational values; verifies the disjoint-support construction for depths \(4,8,12,16\); and separately runs 600 seeded real-data, two-input soft-threshold comparisons for depths up to five. The rational enumeration is exhaustive for the specified finite dimensions only. The general all-depth claims follow from Steps 1–5, not from finite experiments.

## Relationship to prior work
Donoho–Johnstone (1994) introduced the canonical soft wavelet shrinkage estimator. Steidl–Weickert–Brox–Mrázek–Welk (2004) studied relationships between soft wavelet shrinkage, total-variation diffusion and total-variation regularization. Mrázek–Weickert–Steidl (2005) established variation-diminishing properties of specific shift-invariant, single-scale Haar procedures. These results do not provide the **two-input open-path variation Lipschitz modulus** of unshifted, independently thresholded *all-scale* Haar coefficients. Classical finite Haar martingale-transform endpoint constants in \(L^\infty\) concern a different domain norm and signed coefficient multipliers; the bound here concerns the first-difference seminorm and all \(0/1\) chamber Jacobians. A related fixed-mask criterion establishes exactly when an individual Haar coefficient-suppression projector contracts variation, but does not determine the maximizing modulus across all masks nor its logarithmic scale growth. The algebraic reduction to individual masks is shared; its sharp global consequences are distinct.

## Limitations
This result is about real dyadic vectors, all detail coefficients with a common positive scalar threshold, an unweighted **open-path** variation seminorm and orthonormal, aligned Haar details. It does not determine a closed-form formula for \(K_d\) for every depth; the exact all-depth expression is a finite maximization. No claim is made for circular variation, nonuniform grids, other wavelet families, shift-invariant shrinkage, or threshold-dependent statistical risk. Historical priority beyond the inspected literature cannot be excluded. A historically relevant 2003 BV-Haar approximation article and the original 1994 shrinkage article were only partially accessible, so neither is claimed exhaustively absent of related statements.

## References
- D. L. Donoho and I. M. Johnstone, *Ideal spatial adaptation by wavelet shrinkage*, Biometrika **81** (1994), 425–455, DOI: https://doi.org/10.1093/biomet/81.3.425, first publicly dated September 1, 1994.
- G. Steidl, J. Weickert, T. Brox, P. Mrázek, and M. Welk, *On the Equivalence of Soft Wavelet Shrinkage, Total Variation Diffusion, Total Variation Regularization, and SIDEs*, SIAM Journal on Numerical Analysis **42** (2004), 686–713, https://lmbweb.informatik.uni-freiburg.de/Publications/2004/Bro04/steidl_siam04.pdf.
- P. Mrázek, J. Weickert, and G. Steidl, *Diffusion-Inspired Shrinkage Functions and Stability Results for Wavelet Denoising*, International Journal of Computer Vision **64** (2005), 171–186, https://www.mia.uni-saarland.de/Publications/mrazek-ijcv05.pdf.
- P. Wojtaszczyk, *Projections and Non-Linear Approximation in the Space BV(\(\mathbb R^d\))*, Proceedings of the London Mathematical Society **87** (2003), 471–497, DOI: https://doi.org/10.1112/S0024611503014084 (abstract inspected; full text not available).
