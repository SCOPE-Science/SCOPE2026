# Undersampling surjectivity and a two-mode beta law for Gaussian-sketched Ritz values

## Finding
Let \(A\) be a real symmetric positive definite \(n\times n\) matrix and \(S\) an independent real \(k\times n\) matrix with independent standard Gaussian entries. For \(v\in\mathbb R^n\) with \(Sv\ne0\), define the one-vector sketched Ritz value
\[
  r_S(v)=\frac{(Sv)^{\mathsf T}(SAv)}{\|Sv\|_2^2}.
\]
The following all-start alternatives hold (the quantifier over \(v\) is **after** drawing \(S\)).

**(A) Complete undersampling obstruction.** If \(1\le k<n\) and \(A\) is not a scalar matrix, then, with probability one, \(\{r_S(v):Sv\ne0\}=\mathbb R\). Thus even positive-definite \(A\) admits every negative sketched Ritz value when the start is selected after an undersampled sketch is fixed. If \(A=\lambda I\), then \(r_S(v)=\lambda\) for all admissible \(v\).

**(B) Exact injective two-mode reliability.** Suppose \(n=2\), \(k\ge2\), and \(A\) has eigenvalues \(0<m<M\), with \(K=M/m\) and \(z=((K-1)/(K+1))^2\). Then
\[
 \Pr_S\big\{\exists v\ne0:r_S(v)<0\big\}
 =I_z\!\left(\frac{k-1}{2},\frac12\right),
\]
where \(I_z(a,b)=B_z(a,b)/B(a,b)\) is the regularized incomplete beta function. The complement is the probability that every sketched Ritz value is positive. At \(k=2\), the failure probability equals \(\frac2\pi\arcsin((K-1)/(K+1))\). For each fixed \(K>1\), as \(k\to\infty\), the failure probability is asymptotic to
\[
 \sqrt{\frac{2}{\pi(k-1)(1-z)}}\,z^{(k-1)/2}.
\]
For a scalar two-dimensional \(A\), the failure probability is zero for all \(k\); for \(n=2,k=1\), part (A) makes it one for every non-scalar \(A\).

## Assumptions and scope
All matrices, vectors, sketches, and inner products are real. The Gaussian sketch entries are independent \(N(0,1)\) variables; the sketch is drawn once, and the start vector may then depend on it. Calculations are in exact arithmetic and concern the unmodified, one-vector sketched Arnoldi coefficient, not similarity-restoring variants. In (A), \(A\) is fixed, symmetric, positive definite, and non-scalar, \(n\ge2\), and \(1\le k<n\). In (B), the two eigenvalues are strictly distinct and positive, and \(k\ge2\). All statements of almost-sure rank and noninvariance are with respect to the Gaussian sketch. The sample count \(k\), rather than the Krylov iteration index, is varied in the asymptotic law.

## Proof
Write \(P=S^{\mathsf T}S\). The denominator \(v^{\mathsf T}Pv\) is positive exactly on the domain \(Sv\ne0\). The numerator is \(v^{\mathsf T}PAv=v^{\mathsf T}(PA+AP)v/2\), since its skew-symmetric part vanishes in a real quadratic form.

**Proof of (A).** Gaussian \(S\) has row rank \(k\) almost surely. Its kernel \(N\), a Haar-distributed \((n-k)\)-plane, is almost surely not invariant under fixed non-scalar symmetric \(A\): an invariant plane must split along the eigenspace decomposition of \(A\), and the set of such planes is a finite union of products of Grassmannians of strictly smaller dimension than the ambient Grassmannian. Equivalently, invariance is a proper algebraic condition on the random row space. Choose \(w\in N\) with \(PAw\ne0\), and set \(x=PAw\). As \(P\) is strictly positive on its nonzero range, \(e=x^{\mathsf T}Px>0\). Also \(c=x^{\mathsf T}PAw=\|x\|_2^2>0\). Put \(d=x^{\mathsf T}PAx\). Since \(Pw=0\), for every \(t\ne0\) one obtains the **exact** identity
\[
 r_S(w+tx)=\frac{c}{te}+\frac de.
\]
As \(t\) varies over the nonzero reals this covers every real value except \(d/e\), attained by \(r_S(x)=d/e\). Therefore the range is all of \(\mathbb R\). If \(A=\lambda I\), the numerator is identically \(\lambda v^{\mathsf T}Pv\), which proves the exception. No full-row-rank assumption beyond the almost-sure Gaussian rank was used.

**Proof of (B).** Orthogonal invariance permits \(A=\operatorname{diag}(m,M)\) without changing the law of \(S\). Write its independent Gaussian columns as \(g,h\in\mathbb R^k\) and put \(U=\|g\|_2^2\), \(V=\|h\|_2^2\), \(C=g^{\mathsf T}h\). Since \(k\ge2\), \(P\) is positive definite almost surely and the symmetric numerator matrix is
\[
 B=\frac{PA+AP}{2}
 =\begin{pmatrix}mU&(m+M)C/2\\(m+M)C/2&MV\end{pmatrix}.
\]
The diagonal entries are strictly positive. Hence there is a negative value of \(v^{\mathsf T}Bv/(v^{\mathsf T}Pv)\) for some \(v\ne0\) exactly when \(\det B<0\), or
\[
 \frac{C^2}{UV}>\frac{4mM}{(m+M)^2}=1-z.
\]
The squared dot product of two independent uniform directions on the unit sphere in \(\mathbb R^k\) has distribution \(\operatorname{Beta}(1/2,(k-1)/2)\). Therefore the failure probability is its upper tail above \(1-z\), namely \(I_z((k-1)/2,1/2)\). Equality has probability zero. The elementary arcsine CDF gives the \(k=2\) case. Finally, for \(a=(k-1)/2\) and fixed \(0<z<1\), endpoint integration gives
\[
 B_z(a,1/2)\sim \frac{z^a}{a\sqrt{1-z}},\qquad
 B(a,1/2)\sim\sqrt{\frac\pi a},
\]
so their ratio has the stated asymptotic. This completes the proof.

## Verification
Run `python verify_uniform_ritz.py` with NumPy and SciPy installed. The embedded deterministic-seed checker tests the quadratic-form negative-direction criterion against the Gaussian-column correlation condition, the exact \(k=2\) arcsine specialization, the all-real-range identity across many nonscalar dimensions and undersampling sizes, the scalar exception, and finite-sample Monte Carlo consistency with the beta law. It produced `PASS: 11209 numerical/algebraic checks` in the inspected package. Finite numerical checks are not used to infer the almost-sure theorem or the large-sample asymptotic: both follow from the analytic proof above.

## Relationship to prior work
Grigori, Kressner, Shao, and Simunec (2026) formulate the randomized Arnoldi coefficient and document the loss of the usual numerical-range containment, motivating a similarity-restoring correction. Their full preprint develops the correction and algorithmic consequences, not an all-start Gaussian probability formula. Palitta, Schweitzer, and Simoncini (2024) analyze spurious sketched Ritz values and their contribution to matrix-function errors; their theory does not assert this two-mode beta law. Timsit, Grigori, and Balabanov (2023) address randomized orthogonal projections and quasioptimality conditions, not a quantifier-swapped all-start sign certificate.

The elementary beta distribution of an angle between independent Gaussian columns is standard. The content here is its exact equivalence to a global negative-Ritz event for **all starts after the sketch is drawn**, together with the universal complete range obstruction when a non-scalar operator is undersampled. A fixed, sketch-independent starting vector poses a different probability question and cannot be used to replace the existential quantifier in this theorem.

## Limitations
These are worst-case-over-starts guarantees, not failure probabilities for a fixed predetermined right-hand side or for vectors chosen independently of the sketch. The all-real result describes existence of arbitrarily ill-conditioned starts approaching the kernel, not failure of a subspace embedding when restricted to a given fixed, low-dimensional Krylov space. The exact beta law is only for two spatial dimensions and real Gaussian sketches. Similarity-restoring projections, complex sketches, floating-point conditioning and multi-step Arnoldi behavior are not covered. Independent mathematical validation and exhaustive historical-priority verification have not been performed.

## References
1. L. Grigori, D. Kressner, N. Shao, and I. Simunec, *Restoring similarity in randomized Krylov methods with applications to eigenvalue problems and matrix functions*, arXiv:2601.10248v1, first public January 15, 2026. https://arxiv.org/html/2601.10248v1
2. D. Palitta, M. Schweitzer, and V. Simoncini, *Sketched and Truncated Polynomial Krylov Methods: Evaluation of Matrix Functions*, Numerical Linear Algebra with Applications, first online November 11, 2024, doi:10.1002/nla.2596. https://onlinelibrary.wiley.com/doi/10.1002/nla.2596
3. E. Timsit, L. Grigori, and O. Balabanov, *Randomized Orthogonal Projection Methods for Krylov Subspace Solvers*, arXiv:2302.07466v3. https://arxiv.org/html/2302.07466v3
