# An eighth-moment sum-of-squares law for the octahedral Fourier aperture

## Finding

Let \(\mathbb T=\{z\in\mathbb C:|z|=1\}\), with normalized Haar probability measure. On the natural three-dimensional octahedral character support \(\Lambda=\{\pm e_1,\pm e_2,\pm e_3\}\), consider every six-coefficient polynomial
\[
P(z_1,z_2,z_3)=\sum_{j=1}^{3}(a_jz_j+b_jz_j^{-1}),\qquad |a_j|=|b_j|=1.
\]
Put \(q_j=a_jb_j\), \(S=q_1+q_2+q_3\), \(T=q_1^2+q_2^2+q_3^2\), and \(Q=q_1q_2+q_1q_3+q_2q_3\). The **exact eighth-moment identity** is
\[
\boxed{\int_{\mathbb T^3}|P|^8\,dm
=6390+3360|S|^2+36|T+4Q|^2.}
\tag{1}
\]
In particular, its exact attainable range is \([6390,44730]\), and its deficit above the sharp minimum satisfies \(\int|P|^8-6390\ge3360|S|^2\). The minimum holds **exactly** when \((q_1,q_2,q_3)\), up to common multiplication by a unit scalar, is a permutation of \((1,\omega,\omega^2)\), with \(\omega=e^{2\pi i/3}\). Modulo multiplication of every coefficient by a common phase and independent coordinate rotations, the minimizers have exactly **two** classes. The maximum holds exactly when \(q_1=q_2=q_3\), giving one maximizing class.

For any integer \(q\ge2\), if each \(a_j,b_j\) is restricted to the \(q\)-th roots of unity, the continuous minimum \(6390\) is attained **if and only if** \(3\mid q\), in which case exactly \(2q^4\) coefficient arrays attain it; the maximum \(44730\) is attained by exactly \(q^4\) arrays for every \(q\). These assertions also hold with the Haar integral replaced by normalized uniform sampling on \(\mu_{N_1}\times\mu_{N_2}\times\mu_{N_3}\) whenever \(N_1,N_2,N_3\ge9\).

## Assumptions and scope

The coefficient magnitudes are all exactly one and the six frequencies are distinct characters in \(\mathbb Z^3\). The measure on \(\mathbb T^3\) is Haar probability measure, giving \(\int|P|^2=6\). Roots of unity used for **coefficient alphabets** need not have the same orders as the independent **sampling grids**. A coefficient-phase orbit identifies two arrays only under transformations \(a_j\mapsto\lambda\alpha_ja_j\), \(b_j\mapsto\lambda\alpha_j^{-1}b_j\) for arbitrary \(\lambda,\alpha_j\in\mathbb T\); permutations of the three coordinate axes are **not** part of this equivalence.

## Proof

**1. Phase reduction.** For each \(j\), choose unit phases \(u_j,\alpha_j\) with \(a_j=u_j\alpha_j\) and \(b_j=u_j\alpha_j^{-1}\). Independent coordinate rotations remove the \(\alpha_j\), so the moment equals that of \(\sum_j u_j(z_j+z_j^{-1})\). Common multiplication by \(\overline{u_1}\) does not change the moment. We may therefore take \((u_1,u_2,u_3)=(1,v,w)\); the normalized products are then \((q_1,q_2,q_3)=(1,v^2,w^2)\). The homogeneous expressions \(|S|^2\) and \(|T+4Q|^2\) are unchanged by an arbitrary common rotation of all products, so it suffices to prove (1) for the normalized phase triple.

**2. Exact coefficient calculation.** For each integer \(m\ge1\), if \(C_m(r)\) denotes the coefficient of \(z_1^{r_1}z_2^{r_2}z_3^{r_3}\) in \(P^m\), character orthogonality gives the exact identity
\[
\int_{\mathbb T^3}|P|^{2m}\,dm=\sum_{r\in\mathbb Z^3}|C_m(r)|^2.
\tag{2}
\]
The coefficient is an explicitly finite multinomial sum:
\[
C_m(r)=\sum_{\substack{k_j,l_j\in\mathbb Z_{\ge0}\\
\sum_j(k_j+l_j)=m\\k_j-l_j=r_j}}
\frac{m!}{\prod_{j=1}^3 k_j!l_j!}\prod_{j=1}^3 a_j^{k_j}b_j^{l_j}.
\tag{3}
\]
At \(m=4\), exactly 85 frequencies occur: one at \(\|r\|_1=0\), eighteen at \(\|r\|_1=2\), and sixty-six at \(\|r\|_1=4\). Substitute \((a_1,b_1,a_2,b_2,a_3,b_3)=(1,1,v,v,w,w)\) into (2)--(3); multiply the finite Laurent polynomials and collect coefficients of \(v^rw^s\). The result is **exactly**
\[
\sum_r|C_4(r)|^2=6390+3360|1+v^2+w^2|^2
+36|1+v^4+w^4+4(v^2+w^2+v^2w^2)|^2.
\tag{4}
\]
This is (1), since \(T=1+v^4+w^4\) and \(Q=v^2+w^2+v^2w^2\). The accompanying dependency-free exact-integer checker independently constructs all 85 coefficients and verifies equality coefficient by coefficient in the two-variable Laurent ring. Thus (4) is a finite symbolic identity, not a numerical fit. For reference, the same calculation gives \(\int|P|^4=54+4|S|^2\) and \(\int|P|^6=564+144|S|^2\); these lower-order formulas are checks rather than additional research claims.

**3. Sharp lower endpoint and rigidity.** Both terms beyond 6390 in (1) are nonnegative. If equality holds, \(S=0\). Three complex unit vectors sum to zero if and only if they are the three vertices of a rotated equilateral triangle. Hence \((q_1,q_2,q_3)=\eta(1,\omega,\omega^2)\) in some order for \(|\eta|=1\). In this case \(T=\eta^2(1+\omega^2+\omega^4)=0\), and \(Q=\eta^2(\omega+1+\omega^2)=0\). Thus every such triple attains 6390, proving necessity and sufficiency. There are six ordered vertex permutations, and common rotation cyclically permutes three of them. The specified four-parameter phase group therefore has exactly two minimizing orbits.

**4. Upper endpoint, range and stability.** Since \(|q_j|=1\), \(|S|\le3\), \(|T|\le3\) and \(|Q|\le3\), so \(|T+4Q|\le15\). Equation (1) yields \(\int|P|^8\le6390+3360\cdot9+36\cdot225=44730\). Equality requires \(|S|=3\), hence precisely \(q_1=q_2=q_3\); such triples also make \(|T+4Q|=15\) and attain the upper bound. The full six-phase coefficient torus is connected; the moment is continuous, so its image is exactly the interval between the attained extrema. Dropping the last square in (1) gives the displayed sharp-exact nonnegative deficit decomposition and its stated lower estimate; no Euclidean-distance stability constant is asserted.

**5. Restricted phase alphabets.** For coefficients in \(\mu_q\), every product \(q_j=a_jb_j\) lies in \(\mu_q\), and every such product has exactly \(q\) ordered factorizations into \((a_j,b_j)\in\mu_q^2\). The three products can be equilateral only when \(\mu_q\) contains primitive cubic roots, namely \(3\mid q\). When this holds, there are exactly \(2q\) ordered product triples: choose a common root \(\eta\in\mu_q\), then choose one of two cyclic orientation classes; the representation has no duplication. Each triple lifts in \(q^3\) coefficient ways, giving \(2q^4\). For the upper bound, there are \(q\) choices of the common product and \(q^3\) factorizations, giving \(q^4\).

**6. Sampling grids.** Every frequency of \(P^4\) lies in \([-4,4]^3\). If each sampling order is at least nine, these frequency vectors remain pairwise distinct modulo the respective orders. Discrete orthogonality gives the identical sum (2), hence all bounds and equality cases carry over unchanged.

## Verification

Run `python3 octahedral_eighth_check.py` with Python 3 and no third-party packages. It constructs the full Laurent coefficient convolution for the fourth, sixth and eighth moments, verifies the exact positive-square formula through integer coefficient equality, checks the all-equal coefficient moments \(90\), \(1860\) and \(44730\), confirms the 85 eighth-moment Fourier frequencies, and checks finite-alphabet equality-count arithmetic for orders three, six and nine. Expected final line: `OCTAHEDRAL_EIGHTH_EXACT_PASS`. These checks verify the finite symbolic identity; the proof of continuous-phase extremizers and all alphabet orders is the mathematical argument above.

## Relationship to prior work

Pai and Chen (2021), arXiv:2102.04043v1, Sections II--III, construct **two-dimensional complementary array sets** and analyze cancellation of the sum of autocorrelations of **multiple** arrays. Du and Jiang (2022), arXiv:2204.09372v1, Sections II, IV--V, build **multidimensional complementary pairs and quads**, using polynomial autocorrelation identities. These papers provide the natural phase-array and autocorrelation motivation but do not derive a sharp eighth-moment identity or classify a **single** complex phase array on the six-vertex three-dimensional octahedron. Sartori and Adhikari (2021), arXiv:2106.03653, Sections III and VI, analyze product processing and statistical Fourier covariances for sparse multidimensional array geometries, not this pointwise eighth-power Haar moment optimization.

Related published calculations on the eight-vertex cubic Fourier aperture and six-point triangular Fourier aperture determine **fourth moments** of different supports; their frequency-pair identities cannot imply the present fourth-convolution (eighth-moment) formula. A finite-group two-axis cross-extension theorem permits arbitrary amplitudes and different support and maximization, not phase-only minimization on the octahedron. Exact support geometry, moment order and statement implication were compared, not just titles. No bibliographic exhaustiveness or independent validation is claimed.

## Limitations

The theorem assumes six nonzero unit-modulus coefficients, exactly three antipodal coordinate pairs, and the eighth moment. It makes no assertion about arbitrary coefficient magnitudes, higher-dimensional crosses, lower-order sampling grids, or optimal restricted-alphabet values when \(3\nmid q\). The phase-orbit classification is only modulo the specified four-torus action; axis permutations would merge its two minimizing orbits. An equivalent specialized earlier polyphase-array calculation cannot be excluded with certainty. Independent mathematical and bibliographic review has not been performed.

## References

1. Cheng-Yu Pai and Chao-Yu Chen, *Two-Dimensional Golay Complementary Array Sets from Generalized Boolean Functions*, first public 8 February 2021, arXiv:2102.04043v1, https://arxiv.org/html/2102.04043v1.
2. Cheng Du and Yi Jiang, *Constructions of Polyphase Golay Complementary Arrays*, first public 20 April 2022, arXiv:2204.09372v1, https://arxiv.org/html/2204.09372v1.
3. Daniel Sartori and Kaushallya Adhikari, *Product Processing for Tapered Sparse Arrays*, first public 7 June 2021, arXiv:2106.03653, https://arxiv.org/abs/2106.03653.
4. *Exact fourth-moment rigidity of the eight-mode cubic Fourier aperture*, research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-fourth-moment-rigidity-of-the-eight-mode-cubic-fourier-ape--486a31ac0a2d.
5. *Sharp fourth-moment phase rigidity for the six-point triangular Fourier aperture*, research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-fourth-moment-phase-rigidity-for-the-six-point-triangular--bea9cf2ed885.
6. *Sharp fourth-moment extension and one-axis rigidity for finite abelian crosses*, research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-fourth-moment-extension-and-one-axis-rigidity-for-finite-a--5b31463115dc.
