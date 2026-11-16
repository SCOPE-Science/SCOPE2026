# Exact erasure spectra of quadratic harmonic sampling on the icosahedron

## Finding
Let \(X\) be the twelve vertices of a regular icosahedron on \(S^2\), and let \(\mathcal P_2=\mathcal H_0\oplus\mathcal H_1\oplus\mathcal H_2\) be the nine-dimensional space of spherical polynomials of degree at most two. Using the normalized uniform sphere measure, choose any orthonormal basis \(\{Y_j\}_{j=1}^9\), and define \(U_{xj}=Y_j(x)/\sqrt{12}\). For an erased vertex set \(E\subseteq X\), let \(U_{X\setminus E}\) be the matrix of retained observations.

**Complete recovery classification.** The retained samples determine every element of \(\mathcal P_2\) if and only if
\[
|E|\leq3\quad\text{and}\quad E\text{ contains no pair }\{u,-u\}.
\]
Exactly \(233\) of the \(2^{12}=4096\) erasure sets satisfy this condition: \(1,12,60,160\) respectively have \(0,1,2,3\) erased points. Among the \(220\) triples, exactly \(60\) contain an antipodal pair and are singular. The remaining \(160\) divide into \(80\) with positive and \(80\) with negative product \((u\cdot v)(v\cdot w)(w\cdot u)\).

**Complete squared-singular-value spectra.** Set \(a=1/(4\sqrt5)\). The following are the eigenvalues of \(U_{X\setminus E}^{*}U_{X\setminus E}\), with multiplicities indicated by exponents. In the triple cases without antipodal pairs, define \(\eta=\operatorname{sgn}((u\cdot v)(v\cdot w)(w\cdot u))\).

| Erasure type | Squared singular values |
|---|---|
| \(|E|=0\) | \(1\) (ninefold) |
| \(|E|=1\) | \(1\) (eightfold), \(1/4\) |
| \(|E|=2\), nonantipodal | \(1\) (sevenfold), \(1/4-a,1/4+a\) |
| \(|E|=2\), antipodal | \(1\) (sevenfold), \(0,1/2\) |
| \(|E|=3\), nonantipodal, \(\eta=+1\) | \(1\) (sixfold), \(1/4-2a\), \(1/4+a\) (twofold) |
| \(|E|=3\), nonantipodal, \(\eta=-1\) | \(1\) (sixfold), \(1/4-a\) (twofold), \(1/4+2a\) |
| \(|E|=3\), antipodal | \(1\) (sixfold), \(0,3/8-\sqrt{65}/40,3/8+\sqrt{65}/40\) |

For \(|E|\geq4\), fewer than nine observations remain, so the sampling map cannot be injective. The sharp smallest squared singular value over **every recoverable erasure mask** is
\[
\lambda_{\mathrm{min,robust}}=\frac14-\frac1{2\sqrt5}=\frac{\sqrt5-2}{4\sqrt5},
\]
attained exactly at the \(80\) positive-product nonantipodal triples. The largest squared singular value of every retained Gram matrix with at most three erasures is one, so the sharp worst recoverable condition number is
\[
\kappa_{\mathrm{worst}}=\left(\frac14-\frac1{2\sqrt5}\right)^{-1/2}\approx6.15536707435.
\]

## Assumptions and scope
The vertices are the unit-normalized twelve points of the form \((0,\pm1,\pm\varphi)\), \((\pm1,\pm\varphi,0)\), and \((\pm\varphi,0,\pm1)\), where \(\varphi=(1+\sqrt5)/2\). Signs vary independently within each displayed pair. The common normalization factor is \(\sqrt{1+\varphi^2}\). The spaces and all operator norms use the normalized probability surface measure on \(S^2\); the discrete measurement vector is normalized by \(1/\sqrt{12}\), *not* by the number of retained samples. The classification concerns arbitrary complex coefficients in \(\mathcal P_2\) and exact, noiseless uniqueness; the spectrum provides the corresponding Euclidean noise stability.

## Proof
**1. Tight full sampling.** The vertex set is antipodal. Direct coordinate sums give \(\frac1{12}\sum_x x_i^2=1/3\), \(\frac1{12}\sum_x x_i^4=1/5\), and \(\frac1{12}\sum_x x_i^2x_j^2=1/15\) for \(i\neq j\); all monomials of degree at most four with an odd power in some coordinate average to zero. These agree with the corresponding spherical moments. Thus quadrature is exact on products of elements of \(\mathcal P_2\), yielding \(U^*U=I_9\) (equivalently, this icosahedron is a spherical five-design).

**2. Three-point reduction and exact kernel.** By the addition formula for spherical harmonics, the row Gram kernel is
\[
K(u,v)=(UU^*)_{uv}=\frac{1+3(u\cdot v)+5P_2(u\cdot v)}{12},\qquad P_2(t)=\frac{3t^2-1}{2}.
\]
For an erased set \(E\), \(U_{X\setminus E}^*U_{X\setminus E}=I_9-U_E^*U_E\). The only eigenvalues different from one therefore equal \(1-\lambda\), where \(\lambda\) runs over the eigenvalues of the \(|E|\)-by-\(|E|\) matrix \(K_E=U_EU_E^*\). Here \(K(u,u)=3/4\); for distinct vertices \(K(u,-u)=1/4\), and \(K(u,v)=\pm a\) if \(v\neq\pm u\), because \(u\cdot v=\pm1/\sqrt5\).

**3. The exact blocks.** For two vertices the \(2\)-by-\(2\) kernel has eigenvalues \(3/4\pm1/4\) if antipodal, and \(3/4\pm a\) otherwise. For three pairwise nonantipodal vertices, the signed off-diagonal triangle can be switched by diagonal sign conjugation to a matrix with all off-diagonal entries \(a\) when \(\eta=+1\), giving kernel eigenvalues \(3/4+2a,3/4-a,3/4-a\). When \(\eta=-1\), the kernel eigenvalues are \(3/4-2a,3/4+a,3/4+a\). If the triple contains \(u,-u,w\), the sum of the first two standard basis vectors is a kernel eigenvector of eigenvalue one, while the orthogonal \(2\)-by-\(2\) block has diagonal \(1/2,3/4\) and off-diagonal of magnitude \(\sqrt2a\); its eigenvalues are \(5/8\pm\sqrt{65}/40\). Subtraction from one establishes every spectral entry above. In particular, since \(2a<1/4\), a triple without an antipodal pair has full column rank, whereas an antipodal pair forces exactly one-dimensional loss.

**4. Counting all patterns without enumeration assumptions.** There are six antipodal pairs. Thus precisely six of the \(\binom{12}{2}=66\) two-point erasures are singular, and precisely \(6\cdot10=60\) of the \(\binom{12}{3}=220\) three-point erasures contain an antipodal pair. Choose one representative from each pair to form a \(3\)-by-\(6\) vertex matrix \(V\). Spherical second moments give \(VV^T=2I_3\). Since its Gram matrix \(G=V^TV=I_6+S/\sqrt5\) has eigenvalues two (threefold) and zero (threefold), the symmetric Seidel matrix \(S\), with zero diagonal and \(\pm1\) off-diagonal entries, has eigenvalues \(\sqrt5\) and \(-\sqrt5\), each threefold. Hence \(\operatorname{tr}(S^3)=0\). But \(\operatorname{tr}(S^3)=6\sum_{i<j<k}S_{ij}S_{jk}S_{ki}\). Therefore exactly ten of the twenty axis triples have positive signed product and ten negative. Each axis triple has eight possible choices of vertex signs, leaving its triple product unchanged, and the resulting \(160\) three-vertex erasures divide into \(80+80\). Combining the information-theoretic limit \(|E|\leq3\) with the three-point spectra yields all \(233\) successful patterns and proves the sharp condition number.

## Verification
The standalone script `verify_icosa_erasure.py` constructs the twelve normalized vertices and a fully specified orthonormal nine-function polynomial basis, independently evaluates the \(12\)-by-\(9\) sampling matrix, tests \(U^*U=I\), checks its row kernel, and checks the exact candidate characteristic polynomials for every erasure set of size at most three. It verifies the rank classification and the \(80+80+60\) triple partition; the reported run passed \(1,317\) scalar checks. It requires only the Python standard library. These finite computations corroborate, but do not substitute for, the exact proof above.

## Relationship to prior work
Spherical-design quadrature and tight spherical framelets are established methods, as in Xiao and Zhuang (2023). Zandieh, Han, and Avron (2022) establish sample-complexity results for spherical-harmonic reconstruction using randomized nodes; those bounds do not fix the icosahedral design or classify every deletion mask. An, Chen, Sloan, and Womersley (2010) study conditioning and interpolation via spherical designs, without an equivalent complete icosahedral three-erasure spectral result identified in the inspected material. Related published finite-configuration harmonic-sampling analyses address other vertex sets (including a cuboctahedral quadratic erasure census) and do not imply the numerical spectra of the icosahedral frame. The present statement is the configuration-specific classification, not a claim to have discovered general frame-complement identities or spherical designs.

## Limitations
The result is for the regular icosahedron, bandlimit two, equal original-sample weights, and arbitrary deterministic erasures; it is not an optimality theorem over all twelve-site designs and does not cover higher harmonic degrees, perturbations of sites, or arbitrary reweighting. The complete historical-priority status is not independently established; specialized frame-erasure literature may contain equivalent formulations. The proof and code are self-contained but have not been independently audited.

## References
- Y. Xiao and X. Zhuang, *Spherical framelets from spherical designs*, first public arXiv version March 9, 2023, https://arxiv.org/abs/2303.05365 (MSC2020 42C15).
- A. Zandieh, I. Han, and H. Avron, *Near Optimal Reconstruction of Spherical Harmonic Expansions*, first public arXiv version February 25, 2022, https://arxiv.org/abs/2202.12995.
- C. An, X. Chen, I. H. Sloan, and R. S. Womersley, *Well Conditioned Spherical Designs for Integration and Interpolation on the Two-Sphere*, SIAM J. Numer. Anal. 48 (2010), 2135–2157, https://doi.org/10.1137/100795140.
- Delsarte, Goethals and Seidel, *Spherical Codes and Designs*, Geom. Dedicata 6 (1977), 363–388, classical background on spherical designs.
