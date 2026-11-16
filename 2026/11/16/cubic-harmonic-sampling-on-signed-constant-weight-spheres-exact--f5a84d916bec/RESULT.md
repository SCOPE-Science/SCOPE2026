# Cubic harmonic sampling on signed constant-weight spheres: exact spectra and a five-design blind resonance

## Finding

Let \(d\ge3\) and \(1\le k\le d\) be integers. On the unit sphere \(S^{d-1}\), let
\[
X_{d,k}=\{x\in S^{d-1}:x_j\in\{0,\pm k^{-1/2}\}\text{ for all }j,\ \#\{j:x_j\ne0\}=k\}.
\]
This set of \(2^k\binom dk\) distinct points is the signed-coordinate-permutation orbit of a constant-weight vector. Give \(X_{d,k}\) and \(S^{d-1}\) their respective normalized uniform probability measures. Let \(\mathcal H_3(\mathbb R^d;\mathbb C)\) be the space of complex homogeneous harmonic cubics with spherical inner product. Define its sampling concentration operator \(T_{d,k}\) through
\[
\langle T_{d,k}f,g\rangle_{S^{d-1}}=\frac1{|X_{d,k}|}\sum_{x\in X_{d,k}}f(x)\overline{g(x)}.
\]
Then its **entire spectrum**, including all zeros, is the following three-sector multiset:
\[
\boxed{\begin{array}{c|c|c}
\text{sector}&\text{eigenvalue}&\text{multiplicity}\\ \hline
Z&\dfrac{(d+4)(d+2-3k)^2}{6k^2(d-1)}&d\\[4pt]
T&\dfrac{(k-1)(d-k)(d+2)(d+4)}{2k^2(d-1)(d-2)}&d(d-2)\\[4pt]
S&\dfrac{(k-1)(k-2)(d+2)(d+4)}{k^2(d-1)(d-2)}&\binom d3
\end{array}}
\]
Coincident eigenvalues are combined, and the eigenvectors of the sectors are described in the proof. This yields the sharp lower and upper uniform-sampling frame bounds by taking respectively the minimum and maximum of the three listed values. In particular, for \(3\le k\le d-1\), the sampling map is injective on all pure cubic harmonics **if and only if** \(3k\ne d+2\). At the resonance \(d=3k-2\), its kernel is the entire \(d\)-dimensional zonal sector, even though the equal-weight orbit is a spherical \(5\)-design. The first interior resonance, \((d,k)=(7,3)\), has \(280\) sampling nodes but loses exactly \(7\) of the \(77\) cubic-harmonic dimensions.

The explicit low-weight boundary cases \(k=1,2\) and full-support boundary \(k=d\) are included in the formula for completeness, not claimed to be previously unknown special cases.

## Assumptions and scope

The Euclidean Laplacian is \(\Delta=\sum_{j=1}^{d}\partial_{x_j}^2\). A *pure harmonic cubic* is a homogeneous degree-three polynomial annihilated by \(\Delta\); lower-degree polynomial bands are excluded. All surface and orbit measures are probability-normalized. The stated spectral values are for squared singular values of the restriction map \(f\mapsto(f(x))_{x\in X_{d,k}}\) when samples are scaled by \(1/\sqrt{|X_{d,k}|}\). Equivalently, they are the eigenvalues of \(T_{d,k}\). The formulas hold over both real and complex scalars; the complex case follows by polarization and complexification of the real invariant sectors.

## Proof

**1. Exact moments.** Let \(e=(e_1,\ldots,e_d)\) be a vector of nonnegative integers. Both uniform measures are invariant under changing each coordinate sign independently, so an odd exponent forces the corresponding monomial moment to vanish. For even exponents \(e_j=2a_j\), write \(s=\#\{j:a_j>0\}\), \(A=\sum_j a_j\), and \((u)_{\downarrow s}=u(u-1)\cdots(u-s+1)\). Direct support counting gives
\[
\mathbb E_{X_{d,k}}\prod_jx_j^{2a_j}=\frac{(k)_{\downarrow s}}{(d)_{\downarrow s}\,k^{A}},
\]
with the ratio defined as zero for \(s>k\). Rotational invariance, or the Gaussian polar decomposition, gives the usual sphere formula
\[
\mathbb E_{S^{d-1}}\prod_jx_j^{2a_j}
=\frac{\prod_j(2a_j-1)!!}{d(d+2)\cdots(d+2A-2)},
\]
where \((-1)!!=1\). These two identities are exact for all moments appearing below.

**2. Complete sign-character decomposition.** Every degree-three monomial has a nonempty odd-coordinate support of cardinality one or three. This parity support is preserved by \(\Delta\). The independent coordinate sign symmetries make components with distinct odd supports orthogonal under both inner products. For a triple \(\{i,j,\ell\}\), the corresponding harmonic sector is the single line spanned by \(x_ix_jx_\ell\). There are \(\binom d3\) such mutually orthogonal lines. For odd support \(\{i\}\), every cubic has the form
\[
f=x_i\Big(a x_i^2+\sum_{j\ne i}b_jx_j^2\Big),\qquad \Delta f=2x_i\Big(3a+\sum_{j\ne i}b_j\Big).
\]
Consequently the singleton sector has dimension \(d-1\). It splits into a one-dimensional symmetric line spanned by
\[
p_i=x_i^3-\frac{3}{d+2}x_i r^2,\qquad r^2=\sum_jx_j^2,
\]
and the \((d-2)\)-dimensional coefficient-contrast space
\[
\left\{x_i\sum_{j\ne i}b_jx_j^2:\sum_{j\ne i}b_j=0\right\}.
\]
The latter is spanned by \(x_i(x_j^2-x_\ell^2)\) with mutually distinct indices. The stabilizer of coordinate \(i\) permutes its remaining \(d-1\) coordinates; its trivial line and standard contrast module are inequivalent, and the two invariant inner products act by scalar multiples on each. This is also elementary: any permutation-invariant quadratic form on the contrast hyperplane is a multiple of \(\sum_{j\ne i}|b_j|^2\). Parity supports keep different \(i\) orthogonal. The three exhaustive dimensions sum to
\[
d+d(d-2)+\binom d3=\binom{d+2}{3}-d=\dim\mathcal H_3(\mathbb R^d).
\]

**3. Compute the triple eigenvalue.** For distinct \(i,j,\ell\), the spherical square norm of \(x_ix_jx_\ell\) is \(1/[d(d+2)(d+4)]\). The orbit square mean is \((k-1)(k-2)/[d(d-1)(d-2)k^2]\). Their ratio is exactly the displayed \(\lambda_S\).

**4. Compute the transverse eigenvalue.** For distinct \(i,j,\ell\), take \(f=x_i(x_j^2-x_\ell^2)\). Using the moment identities of step 1, its sphere square norm is \(4/[d(d+2)(d+4)]\), and its orbit square mean is
\[
\frac{2(k-1)(d-k)}{d(d-1)(d-2)k^2}.
\]
Their ratio is \(\lambda_T\). Invariance from step 2 extends this value to every transverse contrast and all \(i\).

**5. Compute the zonal eigenvalue.** On the unit sphere, \(p_i=x_i^3-3x_i/(d+2)\), so the above sphere moments give
\[
\mathbb E_{S^{d-1}}|p_i|^2=\frac{6(d-1)}{d(d+2)^2(d+4)}.
\]
At an orbit node, \(x_i^3=x_i/k\); hence \(p_i=x_i(1/k-3/(d+2))\). Since \(\mathbb E_Xx_i^2=1/d\), its orbit square mean equals
\[
\frac1d\left(\frac1k-\frac3{d+2}\right)^2.
\]
The quotient is \(\lambda_Z\). Steps 2–5 prove all eigenvalues with the asserted multiplicities, including boundary zeros and possible collisions.

**6. Sharp rank and the surprising design resonance.** For \(3\le k\le d-1\), both \(\lambda_T\) and \(\lambda_S\) are strictly positive. The remaining eigenvalue vanishes exactly at \(3k=d+2\), yielding precisely a \(d\)-dimensional kernel. Furthermore, the sign symmetry kills odd moments and permutations normalize degree two. For degree four, a signed-permutation-invariant functional on sphere polynomials is determined by \(\mathbb E x_i^4\) and \(\mathbb E x_i^2x_j^2\); the norm identity forces one from the other. Here
\[
\mathbb E_Xx_i^4=\frac1{dk},\qquad \mathbb E_Sx_i^4=\frac3{d(d+2)}.
\]
Thus the orbit is a spherical \(5\)-design if and only if \(3k=d+2\) (odd degree five vanishes). At precisely this design equation all the zonal cubics vanish nodewise, as seen in step 5. For \((d,k)=(7,3)\), direct substitution gives \(\lambda_Z=0\), \(\lambda_T=22/15\), \(\lambda_S=11/15\), with multiplicities \(7,35,35\). The orbit has \(2^3\binom73=280\) nodes, while the harmonic space has dimension \(77\); its rank is \(70\). This completes the classification. 

## Verification

Run `python3 artifacts/check_cubic.py` after extracting the companion script. It uses exact rational polynomial multiplication, separate orbit and spherical moment functions, and tests every Gram entry (not merely eigenvalues) for all \((d,k)\) with \(3\le d\le8\), \(1\le k\le d\): 33 distinct parameter pairs. It checks the full three-sector identity, dimensions and spectral trace. The separate `python3 artifacts/check_enumeration.py` independently enumerates the signed point orbits for eight selected pairs and checks the predicted sector energies by a direct numerical matrix product; it additionally verifies the full zonal kernel at \((7,3)\). Both scripts were executed successfully on the packaged copies. These finite tests corroborate the proof, but the universal assertion is proved by exact moment identities and the exhaustive invariant decomposition above.

## Relationship to prior work

Xiao and Zhuang [1] motivate stable spherical framelet transforms from spherical designs; their work concerns design construction and multiscale transforms, not the three eigenvalues of a fixed signed-sparse orbit acting on pure cubics. Bajnok [2] establishes the generalized-hyperoctahedron orbits and invariant design conditions; in particular the degree-four moment identity behind the spherical five-design resonance is classical. The new point is its interaction with *every* cubic harmonic and the sharp complete rank/spectral characterization; a design's exactness through degree five does not by itself imply the sixth-degree Gram eigenvalues. Mohammadpour and Waldron [3] give more general group-orbit design methods rather than the present evaluated spectrum. In the published collection [4], the same orbit's **quartic** harmonic sampling nullity has been classified, but its proof and statement address a different exact degree and do not determine the cubic eigenvalues. The separate pure-cubic result on type-\(D_d\) roots [5] covers the boundary \(k=2\), which is not asserted novel here. An earlier all-band Parseval obstruction for orbits with no more than two squared-amplitude levels [6] implies a related *band* impossibility but not these pure-degree three eigenvalues or the design-blind rank resonance. The nonbinary Hamming-shell Fourier-band spectrum [7] applies to a different interaction-degree inner-product space and does not directly supply this Euclidean-harmonic restriction spectrum.

## Limitations

The complete classification treats only homogeneous harmonic degree three, a single equally weighted signed constant-weight orbit, and dimensions \(d\ge3\). It does not establish novelty of the general invariant-moment method, the known orbit five-design equation, or the type-\(D\) special case. It does not determine higher harmonic degrees, arbitrary nonsymmetric node perturbations, or optimal node count among all sampling schemes. A prior equivalent classification may be hidden in representation-theoretic or spherical-cubature literature; available comparisons cannot certify universal historical priority. The theorem and computational reproducibility have not undergone independent mathematical audit.

## References

[1] Y. Xiao and X. Zhuang, *Spherical framelets from spherical designs*, arXiv:2303.05365v1, first posted 2023-03-09. https://arxiv.org/abs/2303.05365.

[2] B. Bajnok, *Orbits of the hyperoctahedral group as Euclidean designs*, J. Algebraic Combinatorics 25 (2007), 375–397, first online 2006-11-14; author's openly available text https://arxiv.org/html/2406.04023v1.

[3] M. Mohammadpour and S. Waldron, *Constructing high order spherical designs as a union of two of lower order*, arXiv:1912.07151v1, first posted 2019-12-16. https://arxiv.org/abs/1912.07151.

[4] *Complete quartic harmonic interpolation defects on signed constant-weight spherical orbits*, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-complete-quartic-harmonic-interpolation-defects-on-signed-consta--ba0967ea448b.

[5] *Complete cubic harmonic sampling spectra on type-D roots*, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-complete-cubic-harmonic-sampling-spectra-on-type-d-n-roots--4fdcf93793d3.

[6] *Three-amplitude signed-permutation Parseval frames for spherical cubics*, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-three-amplitude-signed-permutation-parseval-frames-for-spherical--f7c189c7e816.

[7] *An all-degree spectral law for Fourier sampling on q-ary Hamming spheres*, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-an-all-degree-spectral-law-for-fourier-sampling-on-q-ary-hamming--f3d01cadaa90.
