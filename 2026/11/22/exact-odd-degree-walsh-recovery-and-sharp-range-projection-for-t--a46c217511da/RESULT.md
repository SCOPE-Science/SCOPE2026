# Exact odd-degree Walsh recovery and sharp range projection for the six-rim wheel

## Finding
Let \(W_6\) be the wheel with hub vertex \(0\), rim vertices \(1,\ldots,6\) in cyclic order, six hub spokes and six rim edges. For each of its spanning trees \(T\), let \(d(T)\in\mathbb F_2^7\) be the vertex-degree parity vector, and define the multiplicity kernel \(q(x)=|\{T:d(T)=x\}|\). Convolution by \(q\) on functions on \(\mathbb F_2^7\) has exactly the following unnormalized signed Walsh eigenvalues and multiplicities:

| Eigenvalue | Multiplicity |
|---:|---:|
| \(-52\) | 12 |
| \(-16\) | 12 |
| \(-4\) | 40 |
| \(0\) | 38 |
| \(12\) | 12 |
| \(16\) | 12 |
| \(320\) | 2 |

Therefore its rank is \(90\), its nullity is \(38\), and the sharp least nonzero absolute eigenvalue is \(4\). The canonical projection \(P\) onto the recoverable Fourier space has exact norms
\[
\|P\|_{\ell^1\to\ell^1}=\|P\|_{\ell^\infty\to\ell^\infty}=\frac{105}{32}.
\]
These norms are the smallest possible among **all** (real or complex) linear projections onto that range, whether or not they commute with translations. The visible Hilbert-space condition number for the unnormalized convolution is \(80\), and its Moore--Penrose inverse has \(\ell^2\)-norm \(1/4\).

## Assumptions and scope
The graph is the fixed simple wheel \(W_6\): the rim is a cycle of length six, there is one distinct hub, and all 12 edges are distinct. Spanning trees are unweighted and individually counted; different trees giving the same degree-parity vector contribute separately. Characters are indexed by \(a\in\mathbb F_2^7\), with \(\chi_a(x)=(-1)^{a\cdot x}\), and no Fourier normalization is applied to eigenvalues. The result is a complete *finite* classification of this graph, not an assertion about arbitrary wheel sizes or the full twelve-edge incidence-vector convolution.

## Proof
**1. Weighted matrix-tree formula.** Write \(s_v=(-1)^{a_v}\) and give every edge \(uv\) the signed weight \(w_{uv}=s_us_v\). Since
\[
(-1)^{a\cdot d(T)}=\prod_{uv\in E(T)}s_us_v,
\]
the character multiplier \(\lambda_a=\sum_T\chi_a(d(T))\) is the signed spanning-tree enumerator. By the weighted matrix-tree theorem it is the determinant of the six-by-six reduced Laplacian obtained by deleting hub row and column. Explicitly its entries for rim indices modulo six are
\[
L_{ii}=s_0s_i+s_{i-1}s_i+s_is_{i+1},\qquad
L_{i,i+1}=L_{i+1,i}=-s_is_{i+1},
\]
with the wraparound entry \(L_{1,6}=L_{6,1}=-s_1s_6\); other entries are zero. These are exact integers. Each tree has even total degree sum, so simultaneously negating all seven vertex signs leaves every product unchanged. Consequently \(\lambda_a=\lambda_{a+\boldsymbol1}\). We may fix \(s_0=1\) and enumerate six rim signs.

**2. A complete symmetry-reduced certificate.** Identify the rim-negative set with the integer \(b=\sum_{i=1}^6 a_i2^{i-1}\in\{0,\ldots,63\}\). Dihedral rotation and reflection of the rim preserve the determinant. For each of the following least representative masks, the orbit size and exact signed determinant (from the above six-by-six formula) are as displayed:

| Mask \(b\) | Orbit size | \(\lambda\) |
|---:|---:|---:|
| 0 | 1 | 320 |
| 1 | 6 | -52 |
| 3 | 6 | 16 |
| 5 | 6 | -16 |
| 7 | 6 | 12 |
| 9 | 3 | 0 |
| 11 | 12 | -4 |
| 15 | 6 | 0 |
| 21 | 2 | -4 |
| 23 | 6 | 0 |
| 27 | 3 | 0 |
| 31 | 6 | -4 |
| 63 | 1 | 0 |

The 13 disjoint orbits exhaust all 64 rim sign choices because the displayed sizes add to 64 and their explicitly generated rotation/reflection images are pairwise disjoint. There are \(3+6+6+3+1=19\) zero rim characters; restoring the second hub sign doubles each multiplicity, giving the signed spectrum in the finding. Every eigenvalue is a multiple of four, and \(-4\) occurs, so the sharp surviving gap is four; the largest absolute eigenvalue is \(320\), giving condition number \(320/4=80\).

**3. The Fourier range projection.** Let \(v(a)=\mathbf1_{\{\lambda_a\ne0\}}\). Fourier diagonalization identifies the range with the characters where \(v(a)=1\), and the canonical projection has kernel
\[
p(y)=\frac1{128}\sum_{a\in\mathbb F_2^7}v(a)(-1)^{a\cdot y}.
\]
An exhaustive seven-stage integer Walsh transform of the 128-bit visibility mask yields the following complete numerator distribution:

| Value of \(128p(y)\) | Number of \(y\) |
|---:|---:|
| 0 | 64 |
| 2 | 32 |
| -6 | 18 |
| 10 | 12 |
| 90 | 1 |
| -38 | 1 |

Their multiplicities total 128. The \(\ell^1\)- and \(\ell^\infty\)-norm of convolution by \(p\) is the sum of its absolute kernel entries. Hence both are \((64+108+120+90+38)/128=105/32\).

**4. Unrestricted optimality.** Let \(Q\) be any bounded linear projection onto the same Fourier range \(W\), real or complex. Every translation on \(\mathbb F_2^7\) preserves \(W\) and acts isometrically on \(\ell^1\) and \(\ell^\infty\). Averaging its conjugates \(\tau_y Q\tau_y^{-1}\) over all 128 translations produces a translation-commuting projection onto \(W\) with norm no greater than \(\|Q\|\). Such a projection is unique: a translation-commuting operator is Walsh-diagonal, and its multiplier is forced to be one on \(W\) and zero on the complementary frequency space. The average therefore equals \(P\), proving the claimed minimum.

## Verification
The standalone standard-library-only script `verify_degree_wheel.py` supplies two mathematically independent ways to compute each multiplier. It first enumerates every one of the \(\binom{12}{6}=924\) possible six-edge sets, tests for acyclicity and connectedness, counts all 320 spanning trees by degree-parity mask, and performs a complete integer Walsh transform. Separately, it computes the signed reduced-Laplacian determinant for all 128 characters using the exact six-permutation Leibniz expansion, comparing it with every Walsh value. It generates all 13 dihedral orbits, confirms the complete signed spectrum, transforms the nonzero-frequency indicator, and proves the claimed projection-kernel distribution and norm by exact arithmetic. Run `python verify_degree_wheel.py` with Python 3.8 or later from the extracted file's directory. Exhaustive verification is a rigorous certificate here because the graph and all enumerated sets are finite and fully covered.

## Relationship to prior work
The weighted matrix-tree theorem and unweighted Lucas-sequence wheel-tree counts are classical. Benjamin and Yerger's study establishes the 320 spanning trees (via its general wheel formula), but not the degree-parity convolution spectrum. Existing Fourier results on wheel *edge-incidence* kernels study \(2^{12}\) independently signed edge characters, not the \(2^7\) vertex-degree-parity profile or its sharp endpoint projection. The vertex-character multipliers form a particular structured slice of the edge-character family via \(w_{uv}=s_us_v\), so known all-edge zero-free criteria and nonzero-gap estimates are not claimed as new. The new content is the complete multiplicity-weighted vertex-parity spectrum and exact optimal endpoint projection value.

## Limitations
The classification is specific to the seven-vertex wheel; a general formula for other wheel sizes is not asserted. The proof depends on a fully reproducible finite integer certificate, not an unverified assertion of an infinite pattern. Historical-priority comparison was bounded to the identified classical and related Fourier literature and indexed research records; an unindexed equivalent calculation cannot be ruled out. No independent audit is claimed.

## References
1. A. T. Benjamin and C. R. Yerger, *Combinatorial Interpretations of Spanning Tree Identities*, Bulletin of the Institute of Combinatorics and Its Applications **47** (2006), 37–42. Accessible full-text version: https://www.academia.edu/82497908/Combinatorial_interpretations_of_spanning_tree_identities .
2. G. Aalipour, A. M. Duval, W. Kook, K.-J. Lee, and J. L. Martin, *A weighted cellular matrix-tree theorem, with applications to complete colorful and cubical complexes*, arXiv:1510.00033v1, first public 2015-09-30: https://arxiv.org/abs/1510.00033 .
3. *Period-three Fourier singularity and fourfold divisibility for wheel spanning-tree kernels* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-period-three-fourier-singularity-and-fourfold-divisibility-for-w--8adb2e48710a . The prior theorem concerns independently signed edge-incidence convolutions.
4. *Sharp dyadic Walsh gaps and exact Hilbert deconvolution norms for wheel spanning trees* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-sharp-dyadic-walsh-gaps-and-exact-hilbert-deconvolution-norms-fo--b466fdbcc4e8 .
