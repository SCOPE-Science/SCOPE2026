# Exact mean and chi-square fluctuations of Haar central simplex-section vertex counts

## Finding

For an integer \(m\geq 3\), let
\[
\Delta_{m-1}=\operatorname{conv}\{e_1,\ldots,e_m\}
\subset\bigl\{x\in\mathbb R^m:\sum_{i=1}^m x_i=1\bigr\},
\qquad c_m=\frac1m(1,\ldots,1).
\]
Choose an unoriented hyperplane through \(c_m\) with Haar-uniform normal in the \((m-1)\)-dimensional affine span of the simplex, and let \(N_m\) be the number of vertices of its section with \(\Delta_{m-1}\). Then
\[
\boxed{\mathbb E N_m=\binom m2\frac{\arccos(-1/(m-1))}{\pi}
=\frac{m(m-1)}4+\frac{m(m-1)}{2\pi}\arcsin\frac1{m-1}.}
\]
Writing \(\sigma^2=\tfrac14-\tfrac1{2\pi}>0\), the following non-Gaussian distributional limit holds as \(m\to\infty\):
\[
\boxed{\frac{m^2/4-N_m}{m}\ \Longrightarrow\ \sigma^2\chi_1^2,}
\qquad
\boxed{\frac{N_m-\mathbb EN_m}{m}\ \Longrightarrow\ \sigma^2(1-\chi_1^2).}
\]
Here \(\chi_1^2\) denotes the square of a standard Gaussian random variable. In particular,
\[
\mathbb EN_m=\frac{m^2}4-\sigma^2m+O(m^{-1}).
\]
Thus a random central section typically misses the maximal possible section-vertex count by order \(m\), and that order-\(m\) deficit has an explicit one-degree-of-freedom chi-square law rather than a Gaussian law.

## Assumptions and scope

The normal is uniformly distributed on the Euclidean sphere in \(L_m=\{a\in\mathbb R^m:\sum_i a_i=0\}\), with opposite normals identified. This is the rotationally invariant Haar distribution of central sections in the affine hull. The simplex is regular because the coordinate vertices \(e_i\) are equidistant. Nonregular simplices are not covered, and a measure on arbitrary affine (noncentral) hyperplanes is not being used. With probability one no normal coordinate vanishes; all vertex-count statements below refer to such generic sections. The finite-\(m\) expectation is exact for every \(m\ge3\); the chi-square assertions are weak limits as the dimension grows, not finite-\(m\) distribution identities.

## Proof

**1. Section vertices are exactly the crossed simplex edges.** Set \(H_a=\{x:\sum_i x_i=1,\ \langle a,x-c_m\rangle=0\}\) with \(a\in L_m\) and all \(a_i\ne0\). Since \(\langle a,c_m\rangle=0\), the height of vertex \(e_i\) relative to \(H_a\) is \(a_i\). The entries of \(a\) sum to zero, so there are positive and negative heights. Let \(K=\#\{i:a_i>0\}\). The section crosses the relative interior of \([e_i,e_j]\) exactly when \(a_i a_j<0\). Every such crossing is a vertex of the section: its barycentric coordinates have support precisely \(\{i,j\}\), and the \(m-2\) other nonnegativity constraints cut out that point inside the section. Conversely, a section vertex must satisfy at least \(m-2\) independent simplex facet constraints and, since no \(e_i\) is in the section, belongs to the interior of an original edge. Two distinct crossed edges yield distinct points by their different positive barycentric supports. Therefore
\[
N_m=K(m-K)=\frac{m^2}{4}-\left(K-\frac m2\right)^2. \tag{1}
\]
The deterministic possible maximum is \(\lfloor m^2/4\rfloor\), attained by any nonzero zero-sum normal with a nearly balanced sign split.

**2. Haar normals are centered Gaussian observations.** Take independent standard normals \(Z_1,\ldots,Z_m\) and write \(\overline Z=m^{-1}\sum_i Z_i\). Orthogonal projection of the standard Gaussian vector onto \(L_m\) is \((Z_i-\overline Z)_{i=1}^m\). Its direction after normalization is Haar-uniform in \(L_m\), hence
\[
K_m\ \overset{d}=\ \#\{i:Z_i>\overline Z\}. \tag{2}
\]
For \(i\ne j\), the centered Gaussian coordinates \(Y_i=Z_i-\overline Z\) have variance \(1-1/m\), covariance \(-1/m\), and correlation \(\rho=-1/(m-1)\). A two-dimensional centered Gaussian pair with correlation \(\rho\) has opposite signs with probability \(\arccos(\rho)/\pi\). One way to see this is to represent it as \((G_1,\rho G_1+\sqrt{1-\rho^2}G_2)\) for independent standard \(G_1,G_2\). Rotational symmetry then makes the opposite-sign sector have angular proportion \(\arccos(\rho)/\pi\). Since \(N_m\) counts crossed unordered pairs, linearity of expectation yields
\[
\mathbb EN_m=\binom m2\frac{\arccos(-1/(m-1))}{\pi}, \tag{3}
\]
which is the claimed exact formula, equivalently the arcsine expression. Expanding \(\arcsin u=u+O(u^3)\) at \(u=(m-1)^{-1}\) gives the stated mean asymptotic.

**3. The centered sign count has smaller-than-binomial variance.** Let \(F_m\) be the empirical distribution function of the \(Z_i\), \(\Phi\) the standard normal distribution function, and \(\varphi(0)=1/\sqrt{2\pi}\). Equation (2) implies
\[
K_m-m/2=-m\bigl(F_m(\overline Z)-1/2\bigr). \tag{4}
\]
We establish the moving-threshold estimate
\[
\sqrt m\bigl\{[F_m(\overline Z)-F_m(0)]
-[\Phi(\overline Z)-\Phi(0)]\bigr\}=o_{\mathbb P}(1). \tag{5}
\]
Here is an elementary justification, avoiding an unstated process limit. Since \(\sqrt m\,\overline Z\) is exactly standard normal, for any prescribed high probability choose \(C>0\) so that \(|\overline Z|\le C/\sqrt m\). Partition \([-C/\sqrt m,C/\sqrt m]\) by a deterministic grid of mesh at most \(m^{-3/4}\), using \(O_C(m^{1/4})\) points. At each grid point, the variance of the number of observations between that point and zero is at most \(m\,\mathbb P\{|Z_1|\le C/\sqrt m\}=O_C(\sqrt m)\). Chebyshev and a union bound show that the maximum of the centered grid counts is \(o_{\mathbb P}(\sqrt m)\): for any fixed positive error threshold the failure probability is \(O_C(m^{-1/4})\). Between adjacent grid points, monotonicity of empirical counts and of \(\Phi\) bounds the additional deterministic expected increment by \(O(m\cdot m^{-3/4})=O(m^{1/4})=o(\sqrt m)\). This proves (5), first on the high-probability event and then without restriction by letting \(C\) grow.

Taylor expansion at zero and \(\overline Z=O_{\mathbb P}(m^{-1/2})\) yield
\[
\sqrt m\,[\Phi(\overline Z)-1/2]
=\varphi(0)\frac1{\sqrt m}\sum_{i=1}^mZ_i+o_{\mathbb P}(1).
\]
Combining this with (4) and (5),
\[
\frac{K_m-m/2}{\sqrt m}
=\frac1{\sqrt m}\sum_{i=1}^m
\left(\mathbf1_{\{Z_i>0\}}-\frac12-\varphi(0)Z_i\right)
+o_{\mathbb P}(1). \tag{6}
\]
The summands in (6) are independent, identically distributed, mean zero, with
\[
\operatorname{Var}\left(\mathbf1_{\{Z>0\}}-\tfrac12-\varphi(0)Z\right)
=\frac14+\varphi(0)^2-2\varphi(0)\mathbb E[Z\mathbf1_{\{Z>0\}}]
=\frac14-\frac1{2\pi}=\sigma^2,
\]
using \(\mathbb E[Z\mathbf1_{\{Z>0\}}]=\varphi(0)\). The ordinary i.i.d. central limit theorem gives
\[
\frac{K_m-m/2}{\sqrt m}\Longrightarrow\mathcal N(0,\sigma^2). \tag{7}
\]

**4. The quadratic map produces the chi-square limit.** Substitute (7) into the exact identity (1) and apply the continuous mapping theorem to the square:
\[
\frac{m^2/4-N_m}{m}
=\left(\frac{K_m-m/2}{\sqrt m}\right)^2
\Longrightarrow\sigma^2\chi_1^2.
\]
Equation (3) gives \((m^2/4-\mathbb EN_m)/m\to\sigma^2\). Subtract the deterministic mean and use Slutsky's theorem to obtain the centered limit. This completes the proof.

## Verification

The accompanying `verify.py` independently enumerates every nontrivial sign split for \(3\le m\le9\), constructs all crossed-edge points with exact rational barycentric coordinates, checks their distinctness and membership in the section, and tests the count \(K(m-K)\). It checks the exact means for \(m=3,4\), then compares seeded Gaussian-direction simulations at \(m=3,4,5,10,50,250,1000\) against (3) and the asymptotic variance and chi-square cumulative distribution. A successful execution prints `VERIFY_OK`. The tests cover 1,002 finite sign patterns. Such finite checks cannot establish (5) or a weak limit; the analytic argument above supplies the proof for all admissible dimensions.

## Relationship to prior work

Ambrus and Gárgyán (first public version September 11, 2026) study **minimum volume** among central hyperplane sections of the regular simplex. The present statistic instead counts the section's vertices under a Haar-random orientation; neither a minimum-volume characterization nor its local Hessian provides its expectation or probability limit.

De Loera, Lopez-Campos and Torres (2024) investigate the maximum number of vertices of sections of general polytopes and attainable vertex-count gaps. Their maximal bound is consistent with \(\lfloor m^2/4\rfloor\) in the appropriate dimensions but does not determine how a Haar-random section samples those counts. Their examples and tables concentrate on three-dimensional polytopes and hypercubes, not this random regular-simplex law.

Brown, Cohen, Tang and Yam (2021) analyze numbers of observations exceeding the sample mean for **nonnegative, infinite-mean, heavy-tailed** laws with stable index below one, obtaining a different power normalization. Their theorem does not apply to centered, finite-variance Gaussian observations in (2). A published angular-stability result for the minimum simplex-section **volume** likewise does not address combinatorial vertex-count fluctuations. The general Gaussian empirical-process argument is classical; the geometric identification, exact finite-dimensional expectation, and the resulting chi-square section-complexity law are the claims assessed here. An equivalent result in older unindexed geometric-probability or Gaussian-orthant literature remains possible.

## Limitations

Only the regular simplex with centroidal hyperplanes and uniform Euclidean normal directions is covered. The expected count is exact, but no closed finite-\(m\) probability mass function or uniform error bound for the chi-square approximation is claimed. A small-threshold chi-square CDF can exhibit visible finite-dimensional lattice effects. The work does not imply independence of the Gaussian residual signs. The September 2026 motivating manuscript was only accessible in abstract and metadata form; its uninspected full text remains an originality uncertainty. The stated review is not independent certification.

## References

1. G. Ambrus and B. Gárgyán, *Minimal central slices of the regular simplex*, arXiv:2609.12714, first submitted September 11, 2026. https://arxiv.org/abs/2609.12714
2. J. A. De Loera, G. Lopez-Campos and A. J. Torres, *On the Number of Vertices in a Hyperplane Section of a Polytope*, arXiv:2412.12419, first submitted December 17, 2024. https://arxiv.org/abs/2412.12419
3. M. Brown, J. E. Cohen, C.-F. Tang and S. C. P. Yam, *Taylor's law of fluctuation scaling for semivariances and higher moments of heavy-tailed data*, PNAS 118 (2021), e2108031118. https://doi.org/10.1073/pnas.2108031118
4. H. Dirksen, *Sections of the regular simplex — Volume formulas and estimates*, Math. Nachr. 290 (2017), 2567–2584. https://doi.org/10.1002/mana.201600109
5. *Quantitative stability and exact Hessian for minimal central simplex sections*, publicly available research note (2026). https://github.com/published-finding corpus/2026/tree/main/2026/9/19/SCOPE-minimal-simplex-section-angular-stability--47a8f9f119ab
