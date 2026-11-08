# A sharp fourth-moment law and six-phase rigidity for the twelve-root \(A_3\) Fourier aperture

## Finding
For four unit-circle variables \(z_0,z_1,z_2,z_3\), with their common rotation immaterial, let
\[
P_a(z)=\sum_{\substack{0\le i,j\le3\\i\ne j}}a_{ij}\frac{z_i}{z_j},\qquad |a_{ij}|=1.
\]
The twelve frequencies \(e_i-e_j\) are the vertices of the three-dimensional cuboctahedron, the root system of type \(A_3\). With normalized Haar probability measure on the three-dimensional quotient torus, set \(M(a)=\int |P_a|^4\,dm\). Then
\[
\boxed{M(a)\ge180.}
\]
There are precisely **two** attaining coefficient families modulo transformations \(a_{ij}\mapsto\lambda\,u_i\overline{u_j}a_{ij}\), where \(\lambda,u_i\in\mathbb T\). More explicitly, set \(\zeta=e^{\pi i/3}\), fix the four coefficients \(a_{01}=a_{02}=a_{03}=a_{12}=1\), and list the remaining coefficients in lexicographic order. The only attaining exponent strings, taken modulo six, are
\[
\boxed{000101354523\quad\text{and}\quad000505312143,}
\]
where the full twelve-character string is ordered by directed edges \((01,02,03,10,12,13,20,21,23,30,31,32)\). Every general extremizer is obtained from one of these two coefficient matrices by the stated phase transformations.

For the restricted alphabet \(a_{ij}\in\mu_q\), the set of \(q\)-th roots of unity, **the universal minimum \(180\) is attained if and only if \(6\mid q\)**. When attainable, there are exactly \(2q^4\) distinct minimizing ordered coefficient arrays. For the five smallest nontrivial alphabets, the exact minima and all equality counts are:

| \(q\) | Minimum \(M\) | Normalized minimizers | All minimizers |
| ---: | ---: | ---: | ---: |
| 2 | 188 | 3 | 48 |
| 3 | 216 | 16 | 1296 |
| 4 | 188 | 9 | 2304 |
| 5 | \(240-20\sqrt5\) | 24 | 15000 |
| 6 | 180 | 2 | 2592 |

Thus the optimum is nonmonotone across small phase alphabets: ternary phases are worse than binary, and five phases are worse than four. On every product Fourier grid with all three cyclic coordinate orders at least five, the same results hold with Haar integration replaced by the normalized full grid average.

## Assumptions and scope
The indices are \(\{0,1,2,3\}\); the polynomial uses **all twelve** oriented pairs, with all coefficients having modulus exactly one. For convenience set \(z_0=1\), retaining independent \(z_1,z_2,z_3\in\mathbb T\). No power of a variable in the frequency set exceeds one in absolute value. The transformations in the finding use arbitrary common phase \(\lambda\) and vertex phases \(u_i\); multiplication of all \(u_i\) by the same constant acts trivially. For \(q\)-th-root arrays all these phases must belong to \(\mu_q\) when counting discrete orbits. Coordinate permutations and complex conjugation are **not** quotiented out. No assertion of unrestricted optimality over coefficients with varying magnitudes is made.

## Proof
**1. Correlation multiplicities and the exact sum of squares.** Write \(\alpha_{ij}=e_i-e_j\), with \(e_0=0\) and \(e_1,e_2,e_3\) the standard basis in \(\mathbb Z^3\). For every difference \(d\) of two roots define
\[
C_d=\sum_{\alpha_{ij}-\alpha_{kl}=d}a_{ij}\overline{a_{kl}}.
\]
Orthogonality gives \(M(a)=\sum_d|C_d|^2\), independently of whether one uses the difference expansion of \(|P_a|^2\) or the sum expansion of \(P_a^2\). There is one zero displacement with twelve pairs, twelve nonzero displacements with one pair, twenty-four with two pairs, and eighteen with four pairs. The first two classes contribute exactly \(144+12=156\).

Set \(q_{ij}=a_{ij}a_{ji}\) on the six unoriented edges. For each three-element subset \(T=\{i,j,k\}\), the three two-pair displacements \(2e_i-e_j-e_k\), \(2e_j-e_i-e_k\), and \(2e_k-e_i-e_j\) have squared correlation moduli \(|q_{ij}+q_{ik}|^2\), \(|q_{ij}+q_{jk}|^2\), and \(|q_{ik}+q_{jk}|^2\). Their opposite displacements contribute the same values. The elementary identity
\[
|x+y|^2+|x+z|^2+|y+z|^2=3+|x+y+z|^2\quad(|x|=|y|=|z|=1)
\]
therefore yields the exact **nonnegative deficit formula**
\[
\boxed{M(a)-180=2\sum_{|T|=3}\left|\sum_{\{i,j\}\subset T}q_{ij}\right|^2+\sum_{\substack{d:\ \#\{(\alpha,\beta):\alpha-\beta=d\}=4}}|C_d|^2.}\tag{1}
\]
The sum on the right of the second term runs over all eighteen four-pair displacements, not only one representative of each opposite pair. This proves the universal inequality without finite enumeration.

**2. Consequences of equality.** The four triangle sums must vanish. Writing \(A=q_{01},\ C=q_{02},\ F=q_{03}\), those four equations imply
\[
q_{23}=A,\qquad q_{13}=C,\qquad q_{12}=F,\qquad A+C+F=0.
\tag{2}
\]
Because these quantities lie on the unit circle, they form a rotated equilateral triple.

The phase action has exactly one representative satisfying \(a_{01}=a_{02}=a_{03}=a_{12}=1\). In this gauge, let \(B=a_{13}\) and \(T=a_{23}\). Equation (2) determines all twelve entries:
\[
(a_{01},a_{02},a_{03},a_{10},a_{12},a_{13},a_{20},a_{21},a_{23},a_{30},a_{31},a_{32})
=(1,1,1,A,1,B,C,F,T,F,C/B,A/T).
\tag{3}
\]
Directly collecting the four-pair correlations gives, for nine representatives \(d\) of the eighteen opposite displacements, the following exact expressions:

| \(d\) | \(C_d\) |
| --- | --- |
| \((1,-1,0)\) | \((A+C)(B+T)/(CT)\) |
| \((1,-1,-1)\) | \(2(BF+C)/(CF)\) |
| \((1,0,-1)\) | \((A+F)(A+T)/(AF)\) |
| \((0,1,-1)\) | \((C+F)(BF+C)/(CF)\) |
| \((0,1,0)\) | \((A+F)(A+T)/A\) |
| \((0,0,1)\) | \((A+C)(B+T)/(BT)\) |
| \((1,-1,1)\) | \(2(A+T)/T\) |
| \((1,1,-1)\) | \(2(B+T)\) |
| \((1,0,0)\) | \((C+F)(BF+C)/(CF)\) |

Vanishing of the entries for \(d=(1,-1,1)\) and \(d=(1,1,-1)\) forces \(T=-A\) and \(B=A\). Since \(C+F=-A\ne0\), the entry for \(d=(0,1,-1)\) then forces \(BF+C=0\), i.e. \(C=-AF\). Together with \(A+C+F=0\), this becomes \(A+F=AF\), or \(\overline A+\overline F=1\). Two unit vectors sum to one precisely when they are \(e^{\pm\pi i/3}\). Thus
\[
(A,C,F,B,T)=(\zeta,-1,\overline\zeta,\zeta,-\zeta)
\quad\text{or}\quad
(\overline\zeta,-1,\zeta,\overline\zeta,-\overline\zeta).
\]
Conversely these choices make **every** entry in the displayed table vanish, and all triangle sums vanish. They therefore attain \(180\) by (1). The corresponding twelve entries are the two exponent strings in the finding; the phase-gauge uniqueness proves there are no others.

**3. Phase-alphabet threshold and exact low-alphabet census.** The four-anchor gauge can be carried out uniquely using phases from \(\mu_q\) whenever the input array lies in \(\mu_q\). The normalized unrestricted minimizers contain primitive sixth roots, so the minimum is attainable in \(\mu_q\) exactly when \(6\mid q\). The finite gauge group has \(q^4\) elements and acts freely on arrays, proving the count \(2q^4\) for every multiple of six.

For the restricted minima with \(q=2,3,4,5\), a separate **exhaustive exact calculation** is needed. Once the four anchors are fixed, exactly eight phase exponents remain free, so the search space has precisely \(q^8\) elements. The standalone `checker.cpp` enumerates every one, computes all support-difference autocorrelations exactly, and accumulates squared norms in \(\mathbb Z\), \(\mathbb Z[i]\), or \(\mathbb Z[\zeta]\). For \(q=5\), squared norms belong to the real quadratic field \(\mathbb Q(\sqrt5)\), and all comparisons of values \((u+v\sqrt5)/2\) are performed by exact integer sign tests, never by floating-point ordering. Every normalized minimizer is counted, and each lifts to exactly \(q^4\) distinct arrays. This proves every value and count in the table. The checker verifies the normalization multiplicity profile and independently recomputes the moments of the minimizing representatives using the coefficient convolution of \(P_a^2\).

**4. Nonaliasing discrete Fourier grids.** Every difference of two roots has each coordinate between \(-2\) and \(2\). If each cyclic coordinate order is at least five, reduction of these differences to the finite group is injective. Finite character orthogonality therefore gives exactly the same formula (1), bounds, and equality conditions.

## Verification
Compile and execute `checker.cpp` using a C++17 compiler:

```sh
g++ -O3 -std=c++17 checker.cpp -o checker && ./checker
```

The program must end with `A3_FOURTH_MOMENT_EXACT_PASS normalized_cases=2142594`. The output reports all five exact minima, normalized and total optimizer counts, the two normalized hexaphase minimizers, and independent coefficient-convolution checks. The universal inequality and the full continuous-phase classification are proved analytically above; enumeration is used only for the additional finite-alphabet refinements. The exact result in the fifth-root case is \(240-20\sqrt5\), not a floating-point approximation.

## Relationship to prior work
The use of squared aperiodic autocorrelations as a Fourier moment is standard. Pai–Chen (arXiv:2102.04043v1, publicly posted 8 February 2021), Zhang–Fan–Mesnager (arXiv:2107.11599v1), and Du–Jiang (arXiv:2204.09372v1) treat complementary **pairs or sets** of arrays. Their cancellation results do not determine the sharp squared-autocorrelation energy of this *single twelve-root* trigonometric polynomial.

Published sharp fourth-moment classifications for the six-frequency triangular simplex, eight-frequency cubic aperture, nine-frequency planar square, and sixteen-frequency binary four-cube use distinct support geometries and hypotheses. In particular, the binary four-cube result restricts phases to signs, and the triangular-simplex phase-rigidity result has six planar frequencies; neither gives the lower bound or the two continuous-phase equality classes for the nonplanar twelve-frequency \(A_3\) root set. The present proof uses a four-triangle sum-of-squares identity specific to that root geometry, rather than transferring one of those finite tables.

## Limitations
The unrestricted assertion holds only for equal-magnitude coefficients on the type-\(A_3\) twelve-root support. For nonmultiples of six greater than five, the exact finite-alphabet minimum is not determined, although strict inequality above \(180\) is proved. There is no assertion concerning higher-rank root systems or Fourier sampling grids with aliasing. Previously undiscovered specialist classifications of cuboctahedral polyphase arrays cannot be ruled out by a bounded literature search.

## References
1. C.-Y. Pai and C.-Y. Chen, *Two-Dimensional Golay Complementary Array Sets from Generalized Boolean Functions*, arXiv:2102.04043v1, first publicly posted 2021-02-08, https://arxiv.org/abs/2102.04043.
2. H. Zhang, C. Fan, and S. Mesnager, *New constructions of q-Ary 2-D Z-Complementary Array Pairs*, arXiv:2107.11599v1, first publicly posted 2021-07-24, https://arxiv.org/abs/2107.11599.
3. C. Du and Y. Jiang, *Constructions of Polyphase Golay Complementary Arrays*, arXiv:2204.09372v1, first publicly posted 2022-04-20, https://arxiv.org/abs/2204.09372.
4. *Sharp fourth-moment phase rigidity for the six-point triangular Fourier aperture*, public mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-fourth-moment-phase-rigidity-for-the-six-point-triangular--bea9cf2ed885.
5. *Sharp phase-alphabet fourth moments for the nine-mode square Fourier aperture*, public mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-phase-alphabet-fourth-moments-for-the-nine-mode-square-fou--f31c28437f0d.
6. *Sharp binary fourth moments on the four-cube and quadratic path rigidity through seven variables*, public mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-binary-fourth-moments-on-the-four-cube-and-quadratic-path--280918c7a8c9.
