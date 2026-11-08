# An exact Specht resonance in binary Fourier sampling on permutation matrices

## Finding
For every integer \(n\ge7\), write \(P_\sigma\) for the \(n\times n\) permutation matrix over \(\mathbb F_2\) corresponding to \(\sigma\in S_n\). The self-restricted (unnormalized) Walsh/Fourier matrix is
\[
H_n(\sigma,\tau)=(-1)^{\sum_{i,j}(P_\sigma)_{ij}(P_\tau)_{ij}}
=(-1)^{\#\operatorname{Fix}(\sigma^{-1}\tau)}.
\]
It is singular in **every** dimension \(n\ge7\), with a concrete irreducible symmetry sector in its kernel.

For \(z\in\mathbb C\), form the central convolution pencil \(K_n(z)=(z^{\#\operatorname{Fix}(\sigma^{-1}\tau)})_{\sigma,\tau\in S_n}\). For the partition \(\lambda_n=(3,2,2,1^{n-7})\), the scalar on its full isotypic component of the regular \(S_n\)-representation is exactly
\[
\boxed{\Theta_{\lambda_n}(z)=(z-1)^{n-3}(z+1)\bigl(z^2+(n-4)z+n-1\bigr).}
\]
The irreducible dimension is \(d_n=n(n-1)(n-3)(n-6)/8\), so
\[
\boxed{\dim\ker H_n\ge d_n^2.}
\]
The scalar \(\Theta_{\lambda_n}(z)\) vanishes on the complex unit circle exactly at \(z=1,-1\), not at any other root of unity. This **does not** establish invertibility of the entire pencil for other values of \(z\). For \(n=7\), the bound is exact: \(\dim\ker H_7=441\) and \(\operatorname{rank}H_7=4599\).

## Assumptions and scope
All matrix entries in the binary self-restriction use the standard additive bicharacter \(\psi(x)=(-1)^x\) on \(\mathbb F_2\). The matrix has \(n!\) rows and columns, indexed by distinct permutation matrices in \(M_n(\mathbb F_2)\); the dot product is the entrywise coordinate pairing, not matrix multiplication or determinant. Characteristic two enters only upon specializing \(z=-1\) in the auxiliary complex pencil. The partition \(\lambda_n=(3,2,2,1^{n-7})\) is well-defined for \(n\ge7\), and its conjugate is \(\lambda_n'=(n-4,3,1)\).

## Proof
**1. Central Fourier reduction.** For permutations \(\sigma,\tau\), the overlap of ones in \(P_\sigma,P_\tau\) is the number of fixed points of \(\sigma^{-1}\tau\). Thus \(K_n(z)\) is convolution by the central function \(g\mapsto z^{\#\operatorname{Fix}(g)}\) on \(S_n\). Over \(\mathbb C\), its eigenvalue in irreducible sector \(\lambda\vdash n\) is
\[
\Theta_\lambda(z)=\frac1{d_\lambda}\sum_{g\in S_n}z^{\#\operatorname{Fix}(g)}\chi_\lambda(g),
\quad d_\lambda=\chi_\lambda(1),
\]
with multiplicity \(d_\lambda^2\) in the regular representation. The irreducible characters of \(S_n\) are real-valued, so no conjugation convention changes the result.

**2. Exact Schur specialization.** Under the Frobenius character map, the normalized character-weighted sum is
\[
\frac1{n!}\sum_{g\in S_n}z^{\#\operatorname{Fix}(g)}\chi_\lambda(g)
=s_\lambda\bigl[p_1=z,\ p_j=1\ (j\ge2)\bigr].
\]
Write \(a=z-1\). The elementary-symmetric generating function under this specialization is
\[
\sum_{k\ge0} e_k u^k
=\exp\!\left(\sum_{j\ge1}\frac{(-1)^{j-1}p_j u^j}{j}\right)
=(1+u)e^{au}.
\]
Consequently \(e_0=1\), \(e_k=a^{k-1}(a+k)/k!\) for \(k\ge1\), and \(e_k=0\) for negative indices.

**3. Three-column determinant.** Since \(\lambda_n'=(n-4,3,1)\), dual Jacobi--Trudi yields
\[
 s_{\lambda_n}=\det\begin{pmatrix}
 e_{n-4}&e_{n-3}&e_{n-2}\\
 e_2&e_3&e_4\\
 0&1&e_1
 \end{pmatrix}
=e_{n-4}(e_3e_1-e_4)-e_{n-3}e_2e_1+e_{n-2}e_2.
\]
Here \(e_2=a(a+2)/2\) and \(e_3e_1-e_4=a^2(a+2)^2/8\). Direct substitution and collection of powers gives the **rational polynomial identity**
\[
 s_{\lambda_n}\bigl[p_1=z,p_j=1\bigr]
=\frac{(n-6)(n-3)}{8(n-2)!}
 (z-1)^{n-3}(z+1)\bigl(z^2+(n-4)z+n-1\bigr).
\]
The hook-length formula for \(\lambda_n\) gives \(d_n=n(n-1)(n-3)(n-6)/8\). Multiplication by \(n!/d_n\) proves the asserted exact multiplier. This calculation works symbolically for every integer \(n\ge7\), not by extrapolation from small dimensions.

**4. The binary nullspace and the unit circle.** Setting \(z=-1\) annihilates the entire \(\lambda_n\)-isotypic component, of dimension \(d_n^2\). For \(|z|=1\),
\[
 |z^2+(n-4)z|\le1+(n-4)=n-3<n-1,
\]
so the quadratic factor cannot vanish. The remaining factors have unit-circle roots only at \(z=1\) and \(z=-1\). The root \(z=1\) corresponds to the all-ones matrix, whereas \(z=-1\) gives binary self-Fourier sampling.

**5. Exact boundary at seven letters.** For \(n=7\), all fifteen irreducible sectors can be checked without numerical approximation. Expand \(z^{\#\operatorname{Fix}(g)}=\sum_{k=0}^7\binom{\#\operatorname{Fix}(g)}k(z-1)^k\), and apply the branching rule: the multiplicity of \(S^\lambda\) in the permutation representation on ordered \(k\)-tuples is the number of standard branching paths from \(\lambda\) down to the one-row partition \((7-k)\). This produces the following **exhaustive** partition/eigenvalue table at \(z=-1\):

| Partition | Irreducible dimension | Eigenvalue |
|---|---:|---:|
| \((7)\) | 1 | 656 |
| \((6,1)\) | 6 | -240 |
| \((5,2)\) | 14 | 80 |
| \((5,1,1)\) | 15 | 96 |
| \((4,3)\) | 14 | -64 |
| \((4,2,1)\) | 35 | -64 |
| \((4,1,1,1)\) | 20 | -16 |
| \((3,3,1)\) | 21 | 96 |
| \((3,2,2)\) | 21 | 0 |
| \((3,2,1,1)\) | 35 | 32 |
| \((3,1,1,1,1)\) | 15 | 96 |
| \((2,2,2,1)\) | 14 | -160 |
| \((2,2,1,1,1)\) | 14 | -64 |
| \((2,1,1,1,1,1)\) | 6 | 96 |
| \((1,1,1,1,1,1,1)\) | 1 | 320 |

These dimensions obey \(\sum_{\lambda\vdash7}d_\lambda^2=5040\). The only zero eigenvalue belongs to \((3,2,2)\), of irreducible dimension \(21\). Consequently \(\dim\ker H_7=21^2=441\) and \(\operatorname{rank}H_7=5040-441=4599\).

## Verification
Run `python3 verify_permutation_fourier.py` with Python 3 and no external packages. It derives the central polynomial eigenvalues using an independent Young-branching recursion and checks **every coefficient** against the closed product formula for \(7\le n\le20\). It independently verifies the hook-length dimensions, exhaustively enumerates all irreducible sectors at \(n=4,5,7\), and constructs the actual binary permutation-matrix Fourier operators for \(n=2,3,4,5\), comparing exact finite-field Gaussian-elimination ranks to the sector counts. Successful output includes `PERMUTATION_BINARY_FOURIER_RESONANCE_PASS`. These checks corroborate but do not establish the all-\(n\) theorem; the three-column determinant and Schur character identity supply its infinite proof.

## Relationship to prior work
The Frobenius character formula, Schur symmetric functions, Jacobi--Trudi, and Young branching are classical. Diaconis--Fulman--Guralnick study distributions of permutation fixed points; Ku--Wales study the derangement graph, whose central kernel is \(\mathbf1_{\{\#\operatorname{Fix}=0\}}\), rather than the binary parity kernel. Harden--Penman's fixed-point polynomial is the **trivial-character sector** of this pencil, not its nontrivial Specht blocks. Orellana--Zabrocki study broad symmetric-function methods for symmetric-group characters. The present calculation identifies a specific infinite sequence of nontrivial irreducible spectral factors, its characteristic-two vanishing, and its quantified Fourier-reconstruction obstruction. General character theory makes the quantity computable but does not itself state the exact factor or the cancellation. Bounded literature comparison does not establish absolute historical priority.

## Limitations
No formula for the **entire** spectrum or exact nullity in all \(n\ge8\) is claimed. The lower bound can be strict. The value of the chosen multiplier at an odd-order root of unity is nonzero, but this does **not** imply that the full Fourier restriction is invertible in odd characteristic. The exact rank at \(n=7\) rests on a finite exhaustive character census, fully specified above and reproducible by the checker. No independent mathematical audit or historical-priority certification has been performed.

## References
1. P. Diaconis, J. Fulman, R. Guralnick, *On Fixed Points of Permutations*, arXiv:0708.2643v1 (first posted 2007-08-20), https://arxiv.org/abs/0708.2643.
2. C. Y. Ku, D. B. Wales, *Eigenvalues of the Derangement Graph*, arXiv:0803.2901v1 (first posted 2008-03-19), https://arxiv.org/abs/0803.2901.
3. C. M. Harden, D. B. Penman, *Fixed Point Polynomials of Permutation Groups*, Electron. J. Combin. 20(2), P26 (2013), https://doi.org/10.37236/2955.
4. R. Orellana, M. Zabrocki, *Symmetric Group Characters as Symmetric Functions*, arXiv:1510.00438v1 (first posted 2015-10-01), https://arxiv.org/abs/1510.00438; expanded arXiv:1605.06672.
