# Universal real-range obstruction for undersampled Gaussian Ritz quotients

## Theorem
Let \(A\in\mathbb R^{n\times n}\) be a fixed real symmetric matrix, \(n\ge2\), and let \(S\in\mathbb R^{k\times n}\) have independent standard real Gaussian entries, where \(1\le k<n\). For \(v\) with \(Sv\ne0\), define the one-vector, unmodified sketched Ritz quotient
\[
 r_S(v)=\frac{(Sv)^{\mathsf T}SAv}{\|Sv\|_2^2}.
\]
If \(A\) is not a scalar multiple of the identity, then, almost surely in \(S\),
\[
 \{r_S(v):v\in\mathbb R^n,\ Sv\ne0\}=\mathbb R.
\]
If \(A=\lambda I\), this range equals the singleton \(\{\lambda\}\) whenever \(S\ne0\). In particular, for every fixed nonscalar symmetric positive-definite \(A\), *every real value, including arbitrarily negative ones*, is an attainable sketched Ritz quotient after an undersampled Gaussian sketch has been drawn.

The existential choice of \(v\) takes place **after** the random sketch is observed. The result is not a fixed-start distribution or a statement about stable numerical evaluation near a sketch nullspace.

## Proof
Set \(P=S^{\mathsf T}S\). A real Gaussian \(k\times n\) matrix has full row rank \(k\) almost surely, so its nullspace \(N=\ker S=\ker P\) has dimension \(n-k\), while \(P\) is positive definite on its nonzero range.

If \(A\) is nonscalar and symmetric, a Haar-distributed \((n-k)\)-dimensional subspace is almost surely not \(A\)-invariant. Indeed, decompose \(\mathbb R^n\) into the mutually orthogonal eigenspaces of \(A\), of at least two distinct eigenvalues. An invariant subspace of the prescribed dimension decomposes into subspaces of these eigenspaces. For each of the finitely many possible eigenspace-intersection dimensions, the corresponding product of Grassmannians has strictly smaller dimension than the full Grassmannian of \((n-k)\)-planes; their finite union therefore has Haar measure zero. Since the nullspace of a standard Gaussian sketch is Haar-distributed, \(AN\not\subseteq N\) almost surely.

Fix such a sketch. Choose \(w\in N\) with \(Aw\notin N\), and put \(x=PAw\ne0\). Then \(x\) belongs to the range of \(P\), and hence
\[
 e=x^{\mathsf T}Px>0,\qquad c=x^{\mathsf T}PAw=(PAw)^{\mathsf T}(PAw)=\|x\|_2^2>0,
 \qquad d=x^{\mathsf T}PAx\in\mathbb R.
\]
For every real \(t\ne0\), define \(v_t=w+tx\). Since \(Pw=0\), its denominator is \(v_t^{\mathsf T}Pv_t=t^2e>0\), whereas its numerator is \(v_t^{\mathsf T}PAv_t=tc+t^2d\). Thus the exact identity
\[
 r_S(v_t)=\frac{c}{te}+\frac de
\]
holds for all \(t\ne0\). The map \(t\mapsto c/(te)+d/e\) covers \(\mathbb R\setminus\{d/e\}\). The missing value is attained by the admissible vector \(v=x\), for which \(r_S(x)=d/e\). This proves full real surjectivity without numerical approximation. If \(A=\lambda I\), the numerator is identically \(\lambda\) times the denominator, proving the scalar exception.

## Scope, verification and limitations
The proof applies to every fixed nonscalar real symmetric matrix, and in particular to symmetric positive-definite matrices. It uses only a rank-deficient Gaussian observation operator and the post-sketch choice of start. It does **not** establish a probability for a fixed start, any favorable lower bound for a prescribed Krylov subspace, or an actual floating-point instability at a numerically well-conditioned start. Arbitrarily negative values may require starts approaching \(\ker S\), and the two endpoints \(k=0\) and \(k\ge n\) are excluded.

The source package's `verify_uniform_ritz.py` includes finite numerical checks of the explicit nullspace identity for several dimensions and sketch sizes. Those experiments corroborate but do not prove the almost-sure assertion; the Grassmannian argument and exact pencil identity above prove it. The verifier also contains separate tests of a previously known two-dimensional beta-angle probability law; that prior law is **not** part of this theorem and is **not claimed as a discovery** here.

## Mathematical significance and prior coverage
An undersampled sketch may be a useful embedding of an individually chosen Krylov subspace, yet it cannot certify positivity or numerical-range containment **uniformly over every starting vector selected after the sketch** for any nonscalar symmetric operator. The theorem gives the sharp rank obstruction and a constructive mechanism: a noninvariant nullspace causes a rational affine pencil of Ritz values to sweep the whole real line. The scalar exception shows exactly when this obstruction disappears in the undersampled symmetric class.

Grigori, Kressner, Shao and Simunec (2026) analyze unmodified randomized Arnoldi, the possible loss of numerical-range containment and a similarity-restoring correction; they do not provide this full-real-range quantifier-swapped theorem. Earlier work on sketched Krylov methods gives fixed-subspace or fixed-start guarantees, which do not imply the claim about every post-sketch start. Separately, the earlier *Exact adaptive negative-Ritz probability and sharp embedding-safety radius for Gaussian harmonic sketching* theorem determines the same two-dimensional beta-tail negative-direction event that was stated in the unrepaired version of this record: although its quotient is harmonic rather than ordinary, its **sign** is controlled by the identical symmetric quadratic form \((PA+AP)/2\). That probability law is therefore covered and has been removed from the present final finding.

Historical-priority qualification: an earlier equivalent linear-algebraic statement about rank-deficient symmetrized matrix pencils might exist under another name. The constructive proof here does not rely on that possibility being absent.

## References
- L. Grigori, D. Kressner, N. Shao, and I. Simunec, *Restoring similarity in randomized Krylov methods with applications to eigenvalue problems and matrix functions*, arXiv:2601.10248v1 (2026), https://arxiv.org/html/2601.10248v1.
- D. Palitta, M. Schweitzer, and V. Simoncini, *Sketched and Truncated Polynomial Krylov Methods: Evaluation of Matrix Functions*, Numerical Linear Algebra with Applications (2024), https://doi.org/10.1002/nla.2596.
- *Exact adaptive negative-Ritz probability and sharp embedding-safety radius for Gaussian harmonic sketching* (2026-11-02), https://github.com/Resultary/2026/blob/main/2026/11/2/SCOPE-exact-adaptive-negative-ritz-probability-and-sharp-embedding-saf--e211315c6a25/RESULT.md.
