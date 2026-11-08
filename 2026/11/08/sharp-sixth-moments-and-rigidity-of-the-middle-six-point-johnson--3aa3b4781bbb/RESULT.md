# Sharp sixth moments and rigidity of the middle six-point Johnson slice

## Finding
Let \(\Omega\) be the twenty three-element subsets of \(\{1,2,3,4,5,6\}\), with uniform probability measure. For a real nonzero vector \(a=(a_1,\ldots,a_6)\) satisfying \(\sum_i a_i=0\), put
\[
F_a(T)=\sum_{i\in T}a_i,\qquad K(a)=\frac{\mathbb E_{T\in\Omega}F_a(T)^6}{(\mathbb E_{T\in\Omega}F_a(T)^2)^3}.
\]
Then the full sharp and attained norm interval is
\[
\boxed{1\ \leq\ K(a)\ \leq\ \frac{1025}{81}}.
\]
Lower equality holds exactly for nonzero scalar multiples and coordinate permutations of \((5,-1,-1,-1,-1,-1)\). Upper equality holds exactly for nonzero scalar multiples and coordinate permutations of \((1,1,1,-1,-1,-1)\). Every intermediate ratio occurs.

More strongly, with \(p_j=\sum_{i=1}^{6}a_i^j\), every nonzero centered \(a\) satisfies the quantitative sharp-endpoint stability bound
\[
\boxed{\frac{1025}{81}-K(a)\ \geq\ \frac{50}{27}\left(\frac{p_4}{p_2^2}-\frac16\right)}.
\]
The right side vanishes only when all six coefficient magnitudes are equal, which under the zero-sum condition means the upper equality orbit.

Let \(X\) denote the real five-dimensional space of these functions with its induced \(L^6(\Omega)\) norm. Then the exact Euclidean Banach--Mazur distance is
\[
\boxed{d_{\mathrm{BM}}(X,\ell_2^5(\mathbb R))=\left(\frac{1025}{81}\right)^{1/6}}.
\]

## Assumptions and scope
The coefficients are real; the measure is uniform counting measure on *all twenty* three-element subsets; \(\Omega\) is the middle slice of the six-dimensional Boolean cube. One imposes \(\sum_i a_i=0\) to remove the constant direction, which is not identifiable on a fixed-cardinality slice. The map from this five-dimensional coefficient hyperplane to functions on the slice is injective. All norms in the finding are norms on that probability space.

## Proof
**Exact moment identity.** Since \(\sum_i a_i=0\), direct enumeration of the twenty subsets (or expansion by elementary symmetric polynomials) gives
\[
20\,\mathbb E F_a^6=15p_2^3-60p_2p_4-20p_3^2+66p_6,
\qquad \mathbb E F_a^2=\frac3{10}p_2.
\]
Consequently,
\[
K(a)=\frac{50}{27}\left(15-60\frac{p_4}{p_2^2}-20\frac{p_3^2}{p_2^3}+66\frac{p_6}{p_2^3}\right).
\]

**The upper bound and its stability.** Define two homogeneous sextics on centered six-vectors:
\[
G=60p_2p_4+20p_3^2-66p_6-\frac{49}{6}p_2^3,
\qquad A=p_2p_4-\frac16p_2^3.
\]
We prove \(G\ge A\ge0\). The second inequality is Cauchy--Schwarz applied to the six squared coordinates. For the first, let \(H=G-A=59p_2p_4+20p_3^2-66p_6-8p_2^3\). If \(x\in\mathbb R^6\), let \(b_i=x_i-\frac16\sum_jx_j\), and let \(\widetilde H(x)=H(b)\). This is a symmetric homogeneous real polynomial of degree six. The half-degree principle (Riener, Theorem 1.3, following Timofte) states that nonnegativity of such a sextic on all of \(\mathbb R^6\) is equivalent to nonnegativity on vectors having at most three distinct components. Subtracting the mean preserves the multiplicity pattern, so it suffices to test all partitions of six into at most three positive multiplicities.

For a three-level vector with multiplicities \((m,n,k)\), write its values as \(u,v,w\), where \(w=-(mu+nv)/k\). Up to permuting the multiplicities, the possibilities are \((1,1,4)\), \((1,2,3)\), and \((2,2,2)\). For \((1,1,4)\) put \(s=u+v\), \(d=u-v\); exact substitution gives
\[
H=\frac58d^6+\frac{111}{32}d^4s^2+\frac{675}{128}d^2s^4+\frac{729}{512}s^6\ge0.
\]
For \((2,2,2)\) with the same variables,
\[
H=\frac{21}{8}d^6+\frac{351}{8}d^4s^2+\frac{243}{8}d^2s^4+\frac{729}{8}s^6\ge0.
\]
For \((1,2,3)\), substitution gives
\[
H=\frac8{27}(u-v)^2\left(41u^4+153u^3v+411u^2v^2+499uv^3+300v^4\right).
\]
The quartic in parentheses is positive definite: setting \(z=u+v\) makes it
\[
\frac{71}{2}z^4+\frac{357}{2}z^2v^2+86v^4+\frac{11}{2}z^2(z-v)^2+14v^2(z-v)^2.
\]
For two-level vectors with multiplicities \((1,5)\), \((2,4)\), and \((3,3)\), taking the first level to be \(u\) and the other to be \(-mu/(6-m)\), the respective values of \(H\) are \(31104u^6/3125\), \(729u^6/8\), and \(0\). Single-level centered vectors are zero. Thus the half-degree principle proves \(H\ge0\) globally, and hence \(G\ge A\ge0\).

The difference of the proposed upper constant and the moment ratio is \(\frac{50}{27}G/p_2^3\), giving the quantitative inequality. Its equality forces \(A=0\), so equality in Cauchy--Schwarz makes all six \(|a_i|\) equal. The zero-sum condition then requires exactly three signs of each kind. Conversely these vectors attain \(1025/81\): the twenty subset sums consist of \(+3c\) once, \(-3c\) once, and \(\pm c\) nine times each.

**The lower bound and all its equality cases.** Jensen's inequality applied to \(F_a^2\) gives \(\mathbb E F_a^6\ge(\mathbb E F_a^2)^3\). Equality requires all twenty absolute subset sums to agree. Choose indices \(i,j\) with \(a_i\ne a_j\). Comparing the squared sums of \(\{i,r,s\}\) and \(\{j,r,s\}\) for any distinct \(r,s\) outside \(\{i,j\}\) yields
\[
(a_i-a_j)(a_i+a_j+2a_r+2a_s)=0.
\]
All pair sums among the other four coordinates must therefore be identical, forcing those four coordinates to equal a common \(c\). Hence the coefficient vector is a permutation of \((u,v,c,c,c,c)\), where \(u+v=-4c\). The subset sum \(3c\) and the sums \(u+2c\), \(v+2c\) must have equal absolute values. If \(c=0\), they force the zero vector. Otherwise \(|u+2c|=3|c|\) and \(v+2c=-(u+2c)\) force \(\{u,v\}=\{c,-5c\}\). The stated one-outlier orbit is necessary and sufficient. Continuity on the connected coefficient unit sphere gives every intermediate moment ratio.

**Optimal Euclidean distortion.** Let \(N(a)=\|F_a\|_6\) on the centered coefficient hyperplane. Its symmetry group contains the entire permutation group \(S_6\), acting irreducibly on this real five-dimensional hyperplane. Suppose an ellipsoid, represented by a positive quadratic form \(Q\), provides \(r\sqrt{Q(a)}\le N(a)\le R\sqrt{Q(a)}\). Squaring both inequalities and averaging the quadratic form over all coordinate permutations yields the same bounds and constants with the invariant form \(\bar Q\), which must be a positive multiple of \(p_2\). Thus the Hilbert--Schmidt norm is an optimal Euclidean comparator. Since \(\mathbb E F_a^2=3p_2/10\), the sixth power of the optimal distortion is exactly the ratio of the sharp normalized sixth moments, \((1025/81)/1\).

## Verification
The companion `check_six_slice.py` is a standalone exact-arithmetic SymPy verifier. It establishes the second- and sixth-moment polynomial identities in five independent variables (after the zero-sum substitution), all five two-/three-level substitution formulas, the positive quartic square decomposition, and both extremizing witness values. Execution returned `ALL_SIX_SLICE_EXACT_CHECKS_PASSED`. This checker verifies the algebraic identities; global nonnegativity additionally uses the explicitly cited and stated half-degree theorem. Numeric experiments are neither used nor needed for the universal conclusion.

## Relationship to prior work
The Boolean-slice harmonic framework and asymptotic comparisons in Filmus--Mossel, *Harmonicity and invariance on slices of the Boolean cube* (2015), concern general harmonic functions and limit regimes, not an exact finite \(L^6/L^2\) constant or its equality set at the six-point middle slice. Riener's 2010 proof of Timofte's half-degree principle is an essential established positivity tool rather than an earlier evaluation of this norm. A known exact fourth-moment theorem on the same first-harmonic Johnson space covers all slice dimensions at exponent four, but it cannot determine the independent degree-six symmetric-polynomial terms or the resulting sixth-moment equality orbits. A public result on the **second** Johnson spherical projector gives endpoint \(\ell^1/\ell^\infty\) operator norms, not this first-harmonic \(L^6/L^2\) comparison. A public sixth-moment result on finite subgroup-complement Fourier spectra concerns a different coefficient space and measure; its extremal one-outlier coset vector does not imply the balanced Johnson-slice upper extremizer. Relevant equivalence and broader-coverage searches found no claim covering the theorem; this does not exclude unindexed formulations.

## Limitations
The theorem is specific to the real five-dimensional degree-one harmonic space on the uniform \(J(6,3)\) slice, and to sixth moments. It makes no claim for arbitrary Johnson dimensions, other slice sizes, higher-degree slice harmonics, complex coefficients, or general exponents. The stability estimate is explicit and positive but is not claimed to have an optimal prefactor. Independent mathematical validation has not been carried out.

## References
1. Y. Filmus and E. Mossel, *Harmonicity and invariance on slices of the Boolean cube*, arXiv:1507.02713v1, first public 2015-07-09, https://arxiv.org/abs/1507.02713.
2. C. Riener, *On the degree and half degree principle for symmetric polynomials*, arXiv:1001.4464v1, first public 2010-01-25, https://arxiv.org/abs/1001.4464, Theorem 1.3.
3. V. Timofte, *On the positivity of symmetric polynomial functions. I: General results*, J. Math. Anal. Appl. 284 (2003), 174--190; DOI 10.1016/S0022-247X(03)00301-9.
4. *Exact endpoint norm of the second Johnson spherical projector*, publicly available at https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-endpoint-norm-of-the-second-johnson-spherical-projector--f9735429621e.
5. *Sharp sixth-moment constant for finite subgroup-hole spectra*, publicly available at https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-sixth-moment-constant-for-finite-subgroup-hole-spectra--1b6345819859.
