# Exact Euclidean decoding geometry of first-order Reed–Muller codeword polytopes

## Finding

Let \(m\ge 2\), \(n=2^m\), and let \(P_m\subset[0,1]^n\) be the convex hull of the truth tables of all \(2^{m+1}\) affine Boolean functions on \(\mathbb F_2^m\). For every real vector \(y\in\mathbb R^n\), its **unique nearest point in \(P_m\)** has a closed Walsh soft-threshold formula, and the formula identifies its minimal containing face. For binary \(y\), this gives a complete Euclidean convex-decoding rule, rather than nearest-codeword Hamming decoding.

For every even \(m\ge2\), the intrinsic ambient Euclidean Hausdorff distance from the full unit cube to this codeword polytope is
\[
\boxed{d_H^{(2)}([0,1]^n,P_m)=\frac{\sqrt n-1}{2}.}
\]
**Every maximizer is a binary cube vertex representing a bent Boolean function, and every such vertex is a maximizer. There are no nonvertex maximizers.** Its unique nearest point lies in the relative interior of an \((n-1)\)-dimensional simplex facet of \(P_m\). For odd \(m\), the same full projection formula applies, but the displayed Hausdorff equality is **not** asserted; the corresponding bound is strict.

## Assumptions and scope

Index coordinates of \(\mathbb R^n\) by \(x\in\mathbb F_2^m\). For \(a\in\mathbb F_2^m\) put \(\chi_a(x)=(-1)^{a\cdot x}\), and let \(H\) be the \(n\times n\) real Walsh matrix with entries \(H_{x,a}=\chi_a(x)\). Then \(H^{\mathsf T}H=nI\). For \(y\in\mathbb R^n\) define its sign-scale vector \(s_x=1-2y_x\) and normalized Walsh coefficients
\[
 w_a=\frac1n\sum_x s_x\chi_a(x).
\]
Let \(B_1^n=\{z\in\mathbb R^n:\sum_a|z_a|\le1\}\). If \(\sum_a|w_a|\le1\), set \(\tau=0\). Otherwise let \(\tau>0\) be the **unique** number with
\[
\sum_a\max\{|w_a|-\tau,0\}=1.
\]
Set \(z_a=\operatorname{sgn}(w_a)\max\{|w_a|-\tau,0\}\), with \(\operatorname{sgn}(0)=0\).

The projection and squared distance are exactly
\[
\boxed{\bigl(\Pi_{P_m}(y)\bigr)_x=\frac12\left(1-\sum_a z_a\chi_a(x)\right),\qquad
\operatorname{dist}_2(y,P_m)^2=\frac n4\sum_a\min\{|w_a|,\tau\}^2.}
\]
When \(\|w\|_1>1\), the unique nearest point is in the relative interior of a face with dimension \(\#\{a:|w_a|>\tau\}-1\). When \(\|w\|_1<1\), it is in the interior of \(P_m\). At equality \(\|w\|_1=1\), it is already in \(P_m\), with boundary status depending on the zero coefficients.

A binary vertex \(y=(f(x))_x\) is called bent when all unnormalized Walsh sums \(\sum_x(-1)^{f(x)}\chi_a(x)\) have magnitude \(\sqrt n\). Such functions exist for even \(m\) and not for odd \(m\).

## Proof

**1. Cross-polytope isometry.** For affine \(f(x)=a\cdot x+b\) over \(\mathbb F_2\), its binary codeword satisfies \(1-2f(x)=(-1)^b\chi_a(x)\). Therefore
\[
P_m=\left\{\frac12\mathbf1-\frac12Hz:z\in B_1^n\right\}.
\]
The columns of \(H\) are orthogonal and have squared norm \(n\), so this map is an invertible affine similarity of a regular cross-polytope. For any \(y\), the identity \(s=Hw\) gives
\[
\left\|y-\left(\frac12\mathbf1-\frac12Hz\right)\right\|_2^2
=\frac n4\|w-z\|_2^2.
\]

**2. Exact projection and face.** Euclidean projection of \(w\) onto \(B_1^n\) has the thresholded coordinates \(z_a\) stated above: if the point is outside the ball, use the Lagrange multiplier \(\tau>0\) for \(\sum|z_a|\le1\). Each active coordinate satisfies \(w_a-z_a=\tau\operatorname{sgn}(z_a)\); each inactive coordinate has \(|w_a|\le\tau\), and complementary slackness holds. Strict convexity of the quadratic objective gives uniqueness. The distance formula follows because each residual has magnitude \(\min\{|w_a|,\tau\}\). A boundary point with nonzero coefficients precisely in an index set \(J\) is in the relative interior of the simplex face \(\operatorname{conv}\{\operatorname{sgn}(z_a)e_a:a\in J\}\) of the cross-polytope; its dimension is \(|J|-1\). Affine similarity transfers this face description to \(P_m\).

**3. Universal cubical bound.** If \(y\in\{0,1\}^n\), then \(s\in\{-1,1\}^n\), so Walsh Parseval gives \(\|w\|_2=1\). Put \(L=\|w\|_1\), so \(1\le L\le\sqrt n\). The radial point \(w/L\) belongs to \(B_1^n\), giving
\[
\operatorname{dist}_2(y,P_m)
\le \frac{\sqrt n}{2}\left(1-\frac1L\right)
\le\frac{\sqrt n-1}{2}.
\]
Distance to a convex set is convex; hence this upper bound on cube vertices extends to the entire cube, and \(P_m\subseteq[0,1]^n\) makes the one-sided supremum equal the Hausdorff distance.

**4. Sharpness and iff for even dimension.** If \(m=2r\), the quadratic Boolean function \(f(x)=\sum_{j=1}^{r}x_{2j-1}x_{2j}\pmod2\) is bent: its Walsh transform factors into \(r\) two-variable sums, each of magnitude two. For any bent \(f\), all \(|w_a|=1/\sqrt n\), so the soft threshold is \(\tau=1/\sqrt n-1/n\), every \(|z_a|=1/n\), and
\[
\operatorname{dist}_2(y,P_m)=\frac{\sqrt n-1}{2}.
\]
Conversely, equality in the universal bound forces \(L=\sqrt n\), and equality in Cauchy–Schwarz with \(\|w\|_2=1\) forces every \(|w_a|=1/\sqrt n\). This is exactly bentness. All \(n\) coordinates of the nearest cross-polytope point are nonzero, so it is in the relative interior of a facet. In original cube coordinates, the nearest point to bent \(y\) is
\[
\boxed{\Pi_{P_m}(y)=\frac12\mathbf1+\frac1{\sqrt n}\left(y-\frac12\mathbf1\right).}
\]
For odd \(m\), bentness is impossible because integer Walsh sums cannot have common absolute value \(2^{m/2}\), which is irrational. The finite set of cube vertices consequently attains a strictly smaller maximum.

**5. No nonvertex cube maximizers.** Write any nonvertex \(y\in[0,1]^n\) as a nontrivial convex combination of distinct cube vertices \(v_i\) with positive weights. Let \(p_i\) be their nearest points in \(P_m\). Convexity gives \(p=\sum_i\alpha_i p_i\in P_m\) and
\[
\operatorname{dist}(y,P_m)^2\le\left\|\sum_i\alpha_i(v_i-p_i)\right\|^2
\le\sum_i\alpha_i\|v_i-p_i\|^2.
\]
For equality at the universal maximum, every selected \(v_i\) must be bent. The formula in step 4 shows \(v_i-p_i=(1-1/\sqrt n)(v_i-\mathbf1/2)\), which is different for distinct bent vertices. Thus the last quadratic Jensen inequality is strict. Only bent cube vertices can maximize.

## Verification

The accompanying standalone Python checker uses exact integer Walsh transforms and exact rational threshold and KKT certificates. It enumerates every Boolean truth table for \(m=2,3,4\), namely 16, 256, and 65,536 inputs, respectively. For even \(m=2,4\), the farthest-square-distance multiplicities are 8 and 896, consistent with known bent-function counts. The checker also builds and verifies bent witnesses for \(m=2,4,6,8\) with exact squared distances \(1/4,9/4,49/4,225/4\), and checks their full facet supports. An independent numerical simplex-constrained quadratic optimization corroborated 21 small examples. Run `python verify.py` with Python 3; no third-party packages are required for the distributed exact checker. The proof above, not any finite enumeration, establishes the infinite even-\(m\) assertion.

## Relationship to prior work

The regular-cross-polytope realization of Hadamard codewords is already explicit in G. M. Ziegler's 2001 discussion of the 0/1-Borsuk problem, and is used here as a known ingredient. Oblaukhov (arXiv:1912.10811, first publicly submitted December 23, 2019) discusses the *discrete Hamming* metric complements and the known bent deep holes of first-order Reed–Muller codes. Potapov (arXiv:2303.16547, first submitted March 29, 2023) uses the known Walsh-flatness characterization of bent functions, which is not claimed as new here. A prior published affine-codebook random-access result determines a different minimax coordinate-success objective and its unique optimal uniform encoder at bent inputs; that uniform mixture coincides with the present bent-point Euclidean projection, but its coordinatewise objective does not establish the **general** Euclidean nearest-point map, exact residual metric for arbitrary real inputs, or the cubical Hausdorff statement without an additional norm argument.

The claimed contribution is the exact Euclidean projection/distance and minimal-face formula for the complete unpunctured codeword polytope, together with its sharp even-dimensional cubical farthest-point geometry. Neither a new construction of bent functions nor an improved Hamming covering radius is claimed. The logical ingredients are classical, and independent priority verification remains warranted.

## Limitations

For odd \(m\), the exact Hausdorff maximum is not determined here; only the all-input projection formula and a strict comparison with the even-dimensional upper-bound expression apply. This theorem is about real Euclidean projection onto the **convex hull** of binary affine codewords, not Hamming nearest-codeword decoding or unrestricted randomized-decoder optimality. An equivalent convex-geometric statement could exist under Hadamard, spectral norm, or probability-mixture terminology. Independent mathematical audit has not been performed.

## References

- A. Oblaukhov, *On metric regularity of Reed–Muller codes*, arXiv:1912.10811 (first public December 23, 2019), especially Introduction and metric-complement discussion. https://arxiv.org/abs/1912.10811
- V. N. Potapov, *Upper bounds on the numbers of binary plateaued and bent functions*, arXiv:2303.16547 (first public March 29, 2023), Section 2 on Walsh transforms. https://arxiv.org/abs/2303.16547
- G. M. Ziegler, *The 0/1-Borsuk Problem*, in *Computational Discrete Mathematics*, Lecture Notes in Computer Science 2122 (2001), pp. 164–171, especially p. 170 on Hadamard cross-polytopes.
- *Sharp affine-codebook random access and rigidity of bent worst-case inputs* (2026), published published-finding corpus record 7628acdda7d2, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-sharp-affine-codebook-random-access-and-rigidity-of-bent-worst-c--7628acdda7d2 .
