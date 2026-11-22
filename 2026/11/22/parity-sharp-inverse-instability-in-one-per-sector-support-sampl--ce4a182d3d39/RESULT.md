# Parity-sharp inverse instability in one-per-sector support sampling of regular-fan polygons

## Finding

Let \(n\ge3\) and \(\theta=2\pi/n\). Reconstruct the support numbers of a planar strictly convex \(n\)-gon with fixed outward facet normals \(v_j=(\cos(j\theta),\sin(j\theta))\), indexed cyclically. Measure its support function once in each consecutive-normal sector, in directions \(u_j=(\cos(j\theta+\alpha_j),\sin(j\theta+\alpha_j))\) with \(0<\alpha_j<\theta\). The resulting linear support-sampling matrix \(A(\alpha)\) has the exact determinant

\[
\det A(\alpha)=\frac{\prod_{j=1}^{n}\sin(\theta-\alpha_j)+(-1)^{n-1}\prod_{j=1}^{n}\sin\alpha_j}{(\sin\theta)^n}.
\]

For odd \(n\), every such sample design is identifiable. For even \(n\), it is nonidentifiable exactly on the smooth hypersurface

\[
\mathcal Z=\Big\{\alpha:\sum_{j=1}^{n}\log\frac{\sin\alpha_j}{\sin(\theta-\alpha_j)}=0\Big\}.
\]

At each point of \(\mathcal Z\), the matrix has rank \(n-1\), and a one-parameter family of distinct, strictly convex, same-normal-fan polygons gives exactly the same noiseless data. The equal-midsector hexagon is a known earlier special case, not a new observation.

Now assume the sector offsets \(\alpha_j\) are independent and identically distributed with a \(C_c^1((0,\theta))\) probability density \(f\) that is positive in a neighborhood of \(\theta/2\). Set \(T=\|A(\alpha)^{-1}\|_2\) on the almost-surely invertible designs. For odd \(n\), \(T\) is deterministically bounded on the support of the design law. For even \(n\),

\[
\Pr(T>t)=\frac{C_{n,f}}{t}+o(t^{-1}),\qquad
C_{n,f}=2\int_{\mathcal Z}\frac{\|\operatorname{adj}A(\alpha)\|_2}{\|\nabla\det A(\alpha)\|_2}\prod_{j=1}^{n}f(\alpha_j)\,d\mathcal H^{n-1}(\alpha)\in(0,\infty).
\]

Consequently, for even \(n\), \(\mathbb E[T^p]\) is finite exactly when \(0<p<1\), whereas for odd \(n\) every positive moment is finite. With independent zero-mean additive support-value noise of covariance \(\sigma^2 I_n\), \(\sigma>0\), the unconstrained linear inverse \(\hat h=A^{-1}y\) has finite unconditional squared-error risk in odd order but **infinite** unconditional squared-error risk in even order, despite almost-sure identifiability in both orders.

A single extra *known-facet-normal* measurement in direction \(v_0\), stacked as the row \(e_0^{\mathsf T}\), eliminates the singularity for every allowable sample design. For offsets in a common compact subinterval of \((0,\theta)\), the augmented least-squares inverse has uniformly bounded operator norm in both parities.

## Assumptions and scope

The unknown \(P(h)=\{x\in\mathbb R^2:\langle v_j,x\rangle\le h_j\ \forall j\}\) is full-dimensional with **exactly** the prescribed regular normal fan, so its support vector \(h\) lies in the interior of the corresponding type cone. The angular sector \((j\theta,(j+1)\theta)\) is an open normal cone of a vertex of \(P(h)\). The normal directions are fixed in advance; no unknown rotation is estimated.

For the probabilistic assertions, \(n\) is fixed, the \(\alpha_j\) are independent with the stated common smooth compactly supported density, and the noise is independent of the angles, mean zero with covariance \(\sigma^2I_n\). The estimator is the *unconstrained parameter inverse*: its noisy output need not be a feasible convex support vector. The assertion of infinite risk is not a claim about a constrained, truncated, Bayesian, or regularized estimator.

## Proof

**1. Sine-coordinate support interpolation.** Any unit direction between consecutive rays has the unique positive decomposition \(u_j=a_jv_j+b_jv_{j+1}\), with

\[
a_j=\frac{\sin(\theta-\alpha_j)}{\sin\theta}>0,\qquad b_j=\frac{\sin\alpha_j}{\sin\theta}>0.
\]

The support function is linear on each vertex normal cone. Hence \(y_j=h_{P(h)}(u_j)=a_jh_j+b_jh_{j+1}\). Thus \(A_{j,j}=a_j\), \(A_{j,j+1}=b_j\), with cyclic indices, and all other entries vanish.

**2. Exact parity, kernel, and actual polygon ambiguity.** Expanding the determinant along admissible cyclic permutations gives precisely two terms: the product of the diagonal entries and the signed product of the wraparound entries. For odd \(n\) both contributions are positive. For even \(n\) they cancel precisely when \(\prod a_j=\prod b_j\), which is the stated logarithmic balance equation. Because the first \(n-1\) rows have an invertible upper-bidiagonal minor, a singular matrix has rank exactly \(n-1\). Solving successive rows gives a nonzero kernel vector satisfying \(z_{j+1}=-a_jz_j/b_j\); every component is nonzero. The regular polygon has the strictly feasible support vector \(h_j=H>0\), so for sufficiently small positive \(\varepsilon\), both \(h+\varepsilon z\) and \(h-\varepsilon z\) stay inside the same open type cone; they produce identical support samples and distinct convex polygons.

**3. The zero determinant is uniformly transverse.** For even \(n\), put \(P_a=\prod a_j\) and \(P_b=\prod b_j\). At any point of \(\mathcal Z\), \(P_a=P_b=P>0\), and direct differentiation gives

\[
\frac{\partial\det A}{\partial\alpha_j}
=-P\left(\cot(\theta-\alpha_j)+\cot\alpha_j\right)
=-P\frac{\sin\theta}{\sin\alpha_j\sin(\theta-\alpha_j)}<0.
\]

Thus \(\nabla\det A\ne0\) everywhere on \(\mathcal Z\), which is a smooth codimension-one submanifold. The rank calculation also implies \(\operatorname{adj}A\ne0\) there.

**4. Sharp inverse tail, including its coefficient.** Let \(K\Subset(0,\theta)^n\) contain the support of the product density. On \(K\), the determinant \(D(\alpha)\) and adjugate \(B(\alpha)\) are smooth. Away from \(D=0\), \(\|A^{-1}\|_2=\|B\|_2/|D|\). Near \(\mathcal Z\cap K\), use \(D\) as a smooth transverse coordinate and apply the coarea formula, with area density \(d\mathcal H^{n-1}/\|\nabla D\|_2\). On each regular level, the inequality \(|D|<\|B\|_2/t\) yields a transverse interval of first-order length \(2\|B\|_2/t\). Uniform continuity and compactness (or a finite submersion-chart cover) give

\[
\lim_{t\to\infty}t\Pr(\|A^{-1}\|_2>t)
=2\int_{\mathcal Z}\frac{\|B\|_2}{\|\nabla D\|_2}\prod_jf(\alpha_j)\,d\mathcal H^{n-1}(\alpha).
\]

The integral is finite by compact support and nonvanishing gradient; it is strictly positive because the midpoint design belongs to \(\mathcal Z\) and the density is positive in its neighborhood. In odd order the determinant is positive throughout the compact design support and thus bounded away from zero. Integrating the tail identity \(\mathbb E[T^p]=p\int_0^\infty t^{p-1}\Pr(T>t)dt\) proves the precise moment threshold.

**5. Noise amplification and a one-row remedy.** Conditionally on the sampled angles, \(\hat h-h=A^{-1}\varepsilon\) and

\[
\mathbb E[\|\hat h-h\|_2^2\mid\alpha]
=\sigma^2\|A^{-1}\|_F^2.
\]

This is at least \(\sigma^2\|A^{-1}\|_2^2\), so its unconditional expectation diverges for even \(n\). In odd order, uniform boundedness of the inverse makes it finite. Finally, append the measurement row \(e_0^{\mathsf T}\). Every singular \(A\) has a one-dimensional kernel whose coordinates are all nonzero, hence that row does not annihilate its kernel. Therefore the augmented \((n+1)\)-by-\(n\) matrix has full column rank for **every** offset configuration. Its smallest singular value has a strictly positive minimum on any compact design domain, proving uniformly bounded least-squares amplification.

## Verification

The included standalone standard-library program `check_polygon_design.py` tests the cyclic determinant identity against independent elimination for 1,120 seeded numerical designs with \(3\le n\le16\); checks the even balanced-kernel and odd midpoint nondegeneracy in all fourteen orders; and confirms the first-order inverse pole along a transverse perturbation in the eight-normal case. Its output is `POLYGON_SUPPORT_DESIGN_PASS`. These tests are illustrative. The all-order determinant, smoothness, coarea coefficient, and moment assertions follow analytically from the preceding proof, not from finite computation.

## Relationship to prior work

Lele, Kulkarni and Willsky (1992), equations (7)–(9), already give sine-weighted interpolation and a sparse support-sampling least-squares matrix for a polygon with fixed reconstruction normals. Prince and Willsky (1990) develop convex support-line consistency and noise-aware reconstruction. Dostert and Jochemko (2022 preprint; 2023 journal), Theorem 3.7, give general generic-rank identifiability conditions, and **their Example 3.4 already exhibits an even hexagonal fan with an alternating one-dimensional reconstruction ambiguity**. None of these facts is claimed as new.

The distinction here is the complete parity classification for all regular-fan one-per-sector designs, the **exact singular hypersurface**, the sharp coarea constant and moment threshold under randomly varied designs, and the consequence for unconditional error of the *unconstrained linear inverse*. The earlier hexagon example does not imply the sharp inverse tail or the all-odd uniform conditioning statement by itself. Comparisons with other regular-polygon and inverse-problem results did not identify a statement covering the combined probabilistic risk law. This comparison is not an exhaustive priority guarantee.

## Limitations

The sampling offsets are independent with a smooth compactly supported law positive near half-sector; the moment claims need not hold under deterministic offsets or other laws. The sharp constant is given by a surface integral, not simplified to elementary functions for all distributions. The result concerns fixed \(n\) and a fixed regular normal fan, not arbitrary polygonal fans, recovering an unknown rotation, or numerical conditioning as \(n\to\infty\). Infinite risk concerns the *unconstrained* linear support-parameter inverse, not a convexity-constrained or regularized estimator. Priority against unpublished and unindexed equivalent analyses remains uncertain.

## References

1. M. Dostert and K. Jochemko, *Learning polytopes with fixed facet directions*, arXiv:2201.03419 (first public version January 10, 2022), especially Sections 3–4, Theorem 3.7 and Example 3.4. https://arxiv.org/abs/2201.03419
2. A. Lele, S. Kulkarni and A. Willsky, *Convex-polygon estimation from support-line measurements and applications to target reconstruction from laser-radar data*, Journal of the Optical Society of America A 9 (1992), 1693–1714, particularly equations (7)–(9). https://www.princeton.edu/~kulkarni/Papers/Journals/j005_1992_lkw_osa.pdf
3. J. Prince and A. Willsky, *Reconstructing convex sets from support line measurements*, IEEE Transactions on Pattern Analysis and Machine Intelligence 12 (1990), 377–389. https://willsky.lids.mit.edu/publ_pdfs/76_pub_IEEE.pdf
