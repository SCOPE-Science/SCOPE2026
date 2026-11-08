# Odd-coefficient phase rigidity at the first clipped-triangle boundary

## Finding
For each integer \(N\ge3\), define the clipped triangular aperture
\[
T_N=\bigl\{(i,j)\in\mathbb Z_{\ge0}^2:i+j\le N-1\bigr\}\setminus\bigl\{(N-1,0)\bigr\}.
\]
Let \(f:T_N\to2\mathbb Z+1\) have an odd integer coefficient at **every** aperture site. Write its two-variable Fourier polynomial as
\[
P(z,w)=\sum_{(i,j)\in T_N}f(i,j)z^i w^j,\qquad |z|=|w|=1.
\]
If any complex array \(h\) supported **inside** \(T_N\), possibly vanishing at sites, satisfies \(|\widehat h|=|\widehat f|\) at every torus point, then \(h=e^{i\alpha}f\) for a real constant \(\alpha\). This determination is up to a **global** phase only; no translations or reflections need to be identified.

The coefficient hypothesis matters. Put
\[
A_N(z,w)=\sum_{i,j\ge0,\ i+j\le N-2}z^i w^j,
\quad P_+(z,w)=A_N(z,w)(1+2w),\quad
P_-(z,w)=A_N(z,w)(2+w).
\]
Both arrays have strictly positive integer coefficients at every point of \(T_N\), and no coefficients elsewhere, but \(|P_+|=|P_-|\) on the complete torus although they are not proportional. Thus removing the odd-integer condition makes the assertion false on the identical support.

## Assumptions and scope
The complete Fourier intensity means the **aperiodic** (not cyclic-aliased) Fourier intensity on all real angles \((\theta,\phi)\) via \(z=e^{i\theta}\), \(w=e^{i\phi}\). All coefficients of \(f\) are nonzero odd integers, with no bound on magnitude or sign. The competitor may have arbitrary complex coefficients and zero entries but must be supported within the same known aperture. The result is uniform in \(N\ge3\).

## Proof
**1. The four corners are forced in any competitor.** The convex hull of \(T_N\) is the quadrilateral
\[
D_N=\operatorname{conv}\bigl\{(0,0),(N-2,0),(N-2,1),(0,N-1)\bigr\}.
\]
The aperiodic autocorrelation coefficient at displacement \((N-2,-N+1)\) is solely the nonzero product of the coefficients at \((N-2,0)\) and \((0,N-1)\). Likewise displacement \((N-2,1)\) uses only \((N-2,1)\) and \((0,0)\). Equality of Fourier intensities implies equality of all aperiodic autocorrelation coefficients, hence all four vertex coefficients of the competitor are nonzero. Its Newton polygon therefore equals \(D_N\).

**2. Factor-reversal geometry.** In the Laurent polynomial unique-factorization ring \(\mathbb C[z^{\pm1},w^{\pm1}]\), the identity \(P P^*=Q Q^*\) holds, where \(Q\) is the competitor polynomial and \(P^*(z,w)=\overline{P(z^{-1},w^{-1})}\). By unique factorization, \(Q\) is obtained from irreducible factors of \(P\) by replacing any collection of them by their reciprocal-conjugates, times a Laurent monomial and a constant of modulus one (factors common to reciprocal pairs cause no exception). The Newton polytope of a product is the Minkowski sum of the Newton polytopes of its factors.

The quadrilateral \(D_N\) has three unoriented edge directions: horizontal, vertical and diagonal. Of these, **only vertical** occurs as a pair of oppositely directed boundary edges. A nonpoint Minkowski summand of \(D_N\) with nonzero horizontal width necessarily has a horizontal or diagonal exposed edge; its negative has the *opposite* exposed direction, absent from \(D_N\). In a Minkowski sum, an exposed edge direction cannot cancel. Consequently, any factor reversed in a factorization having unchanged Newton polygon \(D_N\) must have zero horizontal width: it is a vertical line-segment factor (up to a Laurent monomial), therefore a nonconstant polynomial in \(w\) alone. Every such nonconstant factor over \(\mathbb C\) has a linear divisor \(w-\rho\).

**3. Odd parity forbids a vertical divisor.** If \(w-\rho\) divided \(P\), it would divide every coefficient polynomial of \(P\) in the variable \(z\). The coefficient of \(z^{N-2}\) is \(a+bw\) with two **odd** nonzero integers \(a,b\), so \(\rho=-a/b\). The coefficient of \(z^{N-3}\) is \(c+dw+ew^2\) with three **odd** integers \(c,d,e\). Evaluating at the same root and clearing denominators would require
\[
c b^2-dab+e a^2=0.
\]
The left side is odd modulo \(2\), a contradiction. Hence \(P\) has no nonconstant vertical factor. By step 2 no nontrivial factor reversal can preserve \(D_N\). Thus \(Q\) differs from \(P\) only by a Laurent monomial and constant phase. Equal Newton polygons force the monomial exponent to be zero, and equality of intensities forces the scalar modulus to be one.

**4. The boundary counterexample.** On the unit circle, \(|1+2w|=|2+w|\). Multiplication by \(A_N\) gives equal intensity. The two polynomials are not proportional: their \(z^{N-2}\) coefficients are \(1+2w\) and \(2+w\) respectively. Their common support is exactly \(T_N\), since every coefficient in the product is strictly positive. Both are integer-valued, showing that the oddness condition provides genuine arithmetic rigidity beyond the geometric support constraint.

## Verification
`CHECK.py` exactly enumerates all normalized binary arrays on \(T_N\) for \(3\le N\le5\), independently computes their complete aperiodic autocorrelation signatures, checks no distinct signatures coincide, and confirms the positive-coefficient counterexample for \(3\le N\le6\) using integer polynomial arithmetic. The general statement is proved in the four steps above, not inferred from finite enumeration. The published script has no external data dependencies.

## Relationship to prior work
Novikov and Xu (2026) construct many multidimensional Fourier phase ambiguities through finite-difference operators; they do not assert the odd-integer clipped-triangle rigidity. Crimmins (1987) and Brames (1986) give convex-support uniqueness criteria requiring no parallel sides. Here the known aperture has an opposite vertical pair of sides, so those criteria do not imply the claim. Their geometrical results are credited, not reasserted. The standard factor-reversal mechanism is also acknowledged; the new point is how a local mod-two obstruction eliminates its only admissible factor on the first clipped-simplex polygon. A one-dimensional signed-binary recovery theorem cannot cover the stated two-dimensional support geometry.

## Limitations
No claim is made for general integer or complex coefficients, unknown supports, sampled or aliased Fourier intensities, or noisy measurements. The constructive nonunique pair proves that extension to arbitrary positive integer coefficients is impossible as stated. No quantitative stability or efficient inverse algorithm is proved. The historical literature has several support-specific uniqueness criteria, and an exact earlier odd-coefficient clipped-triangle formulation cannot be categorically excluded; independent priority review remains necessary.

## References
- R. G. Novikov and T. Xu, *On Phase Retrieval for Continuous and Discrete Fourier Transforms*, arXiv:2604.25662, first posted April 28, 2026, in particular Theorems 1 and 2.
- T. R. Crimmins, *Phase retrieval for discrete functions with support constraints*, Journal of the Optical Society of America A **4** (1987), 124–134, DOI: 10.1364/JOSAA.4.000124.
- B. J. Brames, *Unique phase retrieval with explicit support information*, Optics Letters **11** (1986), 61–63, DOI: 10.1364/OL.11.000061.
- R. Beinert and G. Plonka, *Enforcing uniqueness in one-dimensional phase retrieval by additional signal information in time domain*, Applied and Computational Harmonic Analysis **45** (2018), 505–525, DOI: 10.1016/j.acha.2016.12.002.
