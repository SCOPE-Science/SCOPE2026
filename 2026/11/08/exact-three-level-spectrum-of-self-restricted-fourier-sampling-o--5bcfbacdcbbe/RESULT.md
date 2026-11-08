# Exact three-level spectrum of self-restricted Fourier sampling on invertible two-by-two matrices

## Finding
For every prime power \(q\ge 2\), let \(F=\mathbb F_q\), let \(G=\operatorname{GL}_2(F)\) and let \(\psi:F\to\mathbb C\) be any nontrivial unitary additive character. Write \(N=(q^2-1)(q^2-q)\). Define the square **additive** Fourier sampling operator
\[
H=\left(\psi\left(\sum_{i,j=1}^2 X_{ij}Y_{ij}\right)\right)_{X,Y\in G}.
\]
Its complete complex singular-value multiset, with equal numerical levels combined, is
\[
\begin{array}{c|c}
\text{singular value}&\text{multiplicity}\\\hline
q&1+q^2\\
q^{3/2}&(q-2)(q+1)^2\\
q^2&N-(1+q^2)-(q-2)(q+1)^2.
\end{array}
\]
The middle level is absent at \(q=2\); every listed level having positive multiplicity is attained, including the maximum. Thus the operator is invertible for all finite fields and has exact singular-value condition number \(\kappa_2(H)=q\). For every \(f\in\mathbb C^G\), the following **sharp** inequalities hold:
\[
q\|f\|_{\ell^2(G)}\le\|Hf\|_{\ell^2(G)}\le q^2\|f\|_{\ell^2(G)}.
\]
The spectral subspaces are described by the irreducible sectors of the permutation representation of \(G\) on \(F^2\setminus\{0\}\), as detailed below. No relation to Fourier analysis on the nonabelian group \(G\) is assumed at the outset: the Fourier kernel is the ambient additive dot product on \(M_2(F)\).

## Assumptions and scope
The dot product is the coordinate pairing \(\langle X,Y\rangle=\sum_{i,j}X_{ij}Y_{ij}\), not the trace pairing \(\operatorname{tr}(XY)\); these are related by transposition, a row permutation preserving singular values. The indexing set on both sides is **all** invertible matrices and is of cardinality \(N\). The norms in the sharp inequalities are ordinary (unnormalized) counting norms. All prime powers, including even characteristic, are included; the complex character is arbitrary but nontrivial. The theorem determines singular magnitudes and their multiplicities, not individual eigenvalue phases of \(H\).

## Proof
**1. Fourier transform of the invertible locus.** Put \(K(A)=\sum_{Y\in G}\psi(\langle A,Y\rangle)\). Left-right changes of variables by invertible matrices preserve rank and the sum, so \(K(A)\) depends only on \(r=\operatorname{rank}(A)\). The exact values are
\[
K_0=N,\qquad K_1=-q(q-1),\qquad K_2=q.
\]
For \(r=1\), take \(A=E_{11}\). Fixing the top-left entry at zero permits \(q(q-1)^2\) invertible completions; fixing it at any given nonzero value permits \(q^2(q-1)\) completions. As \(\sum_{t\ne0}\psi(t)=-1\), their signed sum is \(-q(q-1)\). For \(r=2\), the complete additive character sum over \(M_2(F)\) is zero. The rank-one part is
\[
\sum_{\operatorname{rank}Y=1}\psi(\langle I,Y\rangle)=\frac1{q-1}\sum_{u,v\in F^2\setminus\{0\}}\psi(u\cdot v)=-(q+1),
\]
since for every fixed \(u\ne0\) the inner sum over \(v\ne0\) is \(-1\). Including the zero matrix contributes \(1\), so removing both singular strata leaves \(K_2=q\). In characteristic two the same additive identities hold without modification.

**2. A Gram identity supported by a permutation character.** Direct orthogonality gives
\[
B:=HH^*,\qquad B_{X,X'}=K(X-X').
\]
Write \(A_1(X,X')=\mathbf1_{\{\operatorname{rank}(X-X')=1\}}\), and let \(J\) be the all-ones matrix on \(G\). Since rank is invariant under multiplication by \(X^{-1}\),
\[
B=(N-q)I-q^2A_1+qJ.
\]
Let \(W=\mathbb C[F^2\setminus\{0\}]\) be the permutation representation of \(G\), with character \(\chi_W(g)=|\{v\ne0:gv=v\}|\). Its values are \(q^2-1\) at \(g=1\), \(q-1\) when \(\operatorname{rank}(I-g)=1\), and zero when \(\operatorname{rank}(I-g)=2\). Define the central character-kernel matrix \(C_W(X,X')=\chi_W(X^{-1}X')\). Then \(C_W=(q-1)A_1+(q^2-1)I\), and substitution with \(N=(q^2-1)(q^2-q)\) yields the **exact operator identity**
\[
\boxed{B=q^4I-\frac{q^2}{q-1}C_W+qJ.}
\]
This equality is the structural bridge between ambient additive Fourier sampling and the multiplicative permutation character of \(\operatorname{GL}_2(F)\).

**3. Elementary irreducible decomposition of the nonzero-vector permutation representation.** The scalar center \(F^\times I\) acts freely on \(F^2\setminus\{0\}\), leaving \(q+1\) projective lines. For every multiplicative character \(\eta:F^\times\to\mathbb C^\times\), the \(\eta\)-isotypic scalar subspace \(W_\eta\) has dimension \(q+1\); distinct \(\eta\) have no intertwining operators. At the trivial character, \(W_1\cong\mathbb C[\mathbb P^1(F)]\), and two-transitivity of \(G\) on \(\mathbb P^1(F)\) implies the multiplicity-free split \(W_1=\mathbf1\oplus V\), with \(V\) irreducible of dimension \(q\).

To see that every other \(W_\eta\) is irreducible without importing a classification of irreducible representations, calculate the full commutant dimension of \(W\). The stabilizer in \(G\) of a fixed nonzero vector has \(q-1\) singleton orbits on its nonzero scalar multiples and one further orbit on the vectors off that line. Therefore the number of orbits is \(q\), and \(\dim\operatorname{End}_G(W)=q\). The trivial-center part contributes \(\dim\operatorname{End}_G(W_1)=2\), while the other \(q-2\) scalar-character sectors each contribute at least one. The sum of these lower bounds is exactly \(q\), hence each remaining sector has commutant dimension one and is irreducible. Thus
\[
W\cong\mathbf1\oplus V\oplus\bigoplus_{\eta\ne1}W_\eta,
\qquad\dim V=q,\quad\dim W_\eta=q+1.
\]
Every summand has multiplicity one; this includes \(q=2\), when the last sum is empty.

**4. Fourier diagonalization of the central character kernel.** In the regular representation \(\mathbb C[G]\), an irreducible representation \(U\) of dimension \(d\) appears with multiplicity \(d\). By matrix-coefficient Schur orthogonality, convolution by the character \(\chi_W\) acts by the scalar \(N/d\) on the \(d^2\)-dimensional matrix-coefficient sector when \(U\) occurs once in \(W\); it acts by zero on all other sectors. The matrix \(J\) acts by \(N\) on the trivial sector and by zero on all others. Consequently the Gram eigenvalues from the boxed identity are
\[
\begin{array}{c|c|c}
\text{regular representation sector}&\text{Gram eigenvalue}&\text{dimension}\\\hline
\mathbf1&q^2&1\\
V&q^2&q^2\\
W_\eta\ (\eta\ne1)&q^3&(q-2)(q+1)^2\\
\text{all remaining irreducibles}&q^4&N-(1+q^2)-(q-2)(q+1)^2.
\end{array}
\]
For the trivial sector, the calculation includes the \(qJ\) term: \(q^4-q^2N/(q-1)+qN=q^2\). For the dimension-\(q\) sector it reads \(q^4-qN/(q-1)=q^2\). For a dimension-\(q+1\) sector it reads \(q^4-q^2N/(q^2-1)=q^3\). The remaining sectors have eigenvalue \(q^4\).

All Gram eigenvalues are strictly positive. Their multiplicities add to \(N\), so the table is exhaustive. Taking positive square roots gives the claimed singular spectrum. The residual dimension equals \(q^2(q-2)^2+2q(q-1)(q-2)+1\), which is positive for every \(q\ge2\) (and equals \(1\) at \(q=2\)); both extreme levels therefore occur, giving the exact condition number \(q\) and sharp norm inequalities.

## Verification
The reproducible standalone Python program `check_spectrum.py` independently enumerates every matrix over \(\mathbb F_q\), constructs the complete complex restricted Fourier matrix, checks all three exact rank-dependent Fourier coefficients and the full Gram entries, and compares its numerical singular spectrum to every theoretically predicted level and multiplicity. The finite tests cover \(q=2,3,4,5\), including the nonprime extension field \(\mathbb F_4\). The recorded terminal marker is `GL2_RESTRICTED_FOURIER_SPECTRUM_PASS`. Every finite check passed. The unbounded assertion for all prime powers is proved symbolically above; no finite enumeration is used as a substitute for the general proof. The script requires Python 3 and NumPy.

## Relationship to prior work
Finite-field matrix-rank Fourier coefficients belong to the established theory of bilinear-forms association schemes, notably Delsarte's 1978 work; the rank-dependent Fourier coefficients themselves are not claimed as new. Gnedin and Kerov (first posted 30 June 2004) develop permutation characters associated with finite general linear groups, and Prasad (first posted 25 December 2007) analyzes the principal-series irreducibles that appear in the representation decomposition here. The full article sections were consulted for the representation ingredients. Gurevich and Howe's accessible 2021 paper analyzes additive Fourier transforms of matrix-rank strata; its relevant rank-character formulas are consistent with Step 1.

The result here concerns the **entire square additive Fourier kernel sampled on all of \(\operatorname{GL}_2(F)\) in both row and column variables**. Available published comparisons include the spectral problem for a much narrower first-coordinate Fourier band on rank-one matrices and another narrow first-coordinate band on determinant-one matrices; neither gives the present full \(N\)-by-\(N\) spectrum. Delsarte's general ambient association-scheme framework is relevant and could admit a derivation of this calculation, but a complete historical priority determination is not claimed. The explicit three-level singular spectrum, its multiplicities and exact invertibility/conditioning are the claim assessed here, not the classical constituent character formulas.

## Limitations
The proof determines complex singular magnitudes and subspace multiplicities but not the full eigenphase decomposition of \(H\). It treats dimension exactly \(2\), not every \(\operatorname{GL}_d\) with \(d\ge3\). It uses the standard additive character dot product, not arbitrary nonlinear sampling phases. The residual historical-priority risk is whether an earlier theorem, possibly expressed in rank-metric or association-scheme language, already implies this specific full self-restriction spectrum. The 1978 Delsarte article's complete text was not available for full-text inspection. Self-review is not an independent audit.

## References
1. A. Gnedin and S. Kerov, *Derangement characters of the full general linear group*, arXiv:math/0406614, first submitted 2004-06-30, https://arxiv.org/abs/math/0406614 . Full HTML: https://arxiv.org/html/math/0406614v1 .
2. A. Prasad, *Representations of GL(2,F_q) and SL(2,F_q), and some remarks about GL(n,F_q)*, arXiv:0712.4051, first submitted 2007-12-25, https://arxiv.org/abs/0712.4051 . Full HTML: https://arxiv.org/html/0712.4051v1 .
3. S. Gurevich and R. Howe, *Ranks for Representations of GL(n) Over Finite Fields, their Agreement, and Positivity of Fourier Transform*, arXiv:2107.02240, first submitted 2021-07-05, https://arxiv.org/abs/2107.02240 .
4. P. Delsarte, *Bilinear Forms over a Finite Field, with Applications to Coding Theory*, Journal of Combinatorial Theory A 25 (1978), 226–241, https://doi.org/10.1016/0097-3165(78)90015-8 . Full primary text not consulted.
