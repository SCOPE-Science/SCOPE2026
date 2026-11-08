# Sharp quartic geometry and Pell-type resonances of complex Grassmannian linear statistics

## Finding

For all integers \(n\ge4\), \(1\le k\le n-1\), take \(P=U\operatorname{diag}(I_k,0)U^*\), where \(U\) is Haar-uniform on \(U(n)\). For each nonzero traceless Hermitian \(n\)-by-\(n\) matrix \(A\), let \(F_A(P)=\operatorname{tr}(AP)\), and put
\[
\rho(A)=\frac{\operatorname{tr}(A^4)}{\operatorname{tr}(A^2)^2},\quad
w=k(n-k),\quad M=n^2+1-5w,\quad
C=\frac{3(n^2-1)}{w(n^2-9)(n^2-4)}.
\]
Then the **exact normalized fourth moment** is
\[
K_{n,k}(A)=\frac{\mathbb E F_A^4}{(\mathbb E F_A^2)^2}
=C\{w(n^2+6)-4n^2+6+2nM\rho(A)\}.
\]
Define
\[
\rho_-=\begin{cases}1/n,&n\text{ even},\\
(n^2+3)/(n(n^2-1)),&n\text{ odd},\end{cases}
\quad
\rho_+=\frac{n^2-3n+3}{n(n-1)}.
\]
For \(M>0\), the sharp interval is \([K_{n,k}(\rho_-),K_{n,k}(\rho_+)]\); for \(M<0\), its endpoints are reversed. Every intermediate value occurs. At \(M=0\), all nonzero \(A\) have the **same** normalized fourth moment
\[
K_{n,k}(A)=\frac{3(n^2-1)}{n^2+1}.
\]

For \(M\ne0\), the \(\rho_-\)-extremizers have exactly two eigenvalues with multiplicities \(\lfloor n/2\rfloor,\lceil n/2\rceil\), with trace zero; the \(\rho_+\)-extremizers have one eigenvalue distinct and the other \(n-1\) equal, again with trace zero. Every unitary conjugate and nonzero real multiple is included. Which geometry minimizes versus maximizes the fourth moment is determined by the sign of \(M\). If \(M=0\), every nonzero traceless Hermitian matrix is simultaneously a minimizer and a maximizer.

The real \((n^2-1)\)-dimensional space \(X_{n,k}=\{F_A:\operatorname{tr}(A)=0,\ A=A^*\}\) has
\[
d_{\mathrm{BM}}(X_{n,k},\ell_2^{n^2-1}(\mathbb R))^4
=K_{n,k,\max}/K_{n,k,\min},
\]
so its \(L^4\) norm is exactly Euclidean precisely when \(5k(n-k)=n^2+1\). Infinitely many such pairs exist, including \((n,k)=(7,2),(18,5),(47,13),(123,34)\). This is an exact *quartic isotropy*, not a claim that the orbit is a spherical 4-design.

## Assumptions and scope

All expectations use normalized Haar measure, \(A\) is real-linear in the space of complex Hermitian traceless matrices, and matrix traces are unnormalized. The projection rank satisfies \(1\le k<n\); the formulas are asserted for \(n\ge4\), avoiding small-dimensional denominators in the Schur expansion. For every such nonzero \(A\), \(\mathbb EF_A=0\) and
\[
\mathbb EF_A^2=\frac{k(n-k)}{n(n^2-1)}\operatorname{tr}(A^2)>0.
\]
Thus every quotient is well defined. The complementary-rank symmetry follows from \(P\mapsto I-P\), as \(\operatorname{tr}(A)=0\).

## Proof

**Exact moments.** Let \(D_k=\operatorname{diag}(I_k,0)\). The Schur--Weyl integration identity, for each positive integer \(r\le n\), is
\[
\mathbb E[\operatorname{tr}(A U D_k U^*)^r]
=\sum_{\lambda\vdash r} f^\lambda
  \frac{s_\lambda(A)s_\lambda(D_k)}{s_\lambda(I_n)}.
\]
Here \(f^\lambda\) is the dimension of the corresponding symmetric-group irreducible and \(s_\lambda\) the Schur polynomial. The hook-content formula gives
\[
\frac{s_\lambda(D_k)}{s_\lambda(I_n)}
=\prod_{(i,j)\in\lambda}\frac{k+j-i}{n+j-i}.
\]
For trace-free \(A\), the Frobenius character formula gives
\[
s_\lambda(A)=\frac{\chi^\lambda(2,2)}8\operatorname{tr}(A^2)^2
+\frac{\chi^\lambda(4)}4\operatorname{tr}(A^4)
\quad (\lambda\vdash4).
\]
For shapes \((4),(3,1),(2,2),(2,1,1),(1,1,1,1)\), the triples \((f^\lambda,\chi^\lambda(2,2),\chi^\lambda(4))\) are respectively \((1,1,1),(3,-1,-1),(2,2,0),(3,-1,1),(1,1,-1)\). Substitution and simplification yield
\[
\mathbb E F_A^4=\alpha_{n,k}\operatorname{tr}(A^2)^2
+\beta_{n,k}\operatorname{tr}(A^4),
\]
where, with \(T=(n^2-9)(n^2-4)(n^2-1)\),
\[
\alpha_{n,k}=\frac{3w\{w(n^2+6)-4n^2+6\}}{n^2T},
\qquad \beta_{n,k}=\frac{6w(n^2+1-5w)}{nT}.
\]
The degree-two character expansion gives \(\mathbb EF_A^2=w\operatorname{tr}(A^2)/(n(n^2-1))\), and division proves the stated formula for \(K_{n,k}\).

**Sharp spectral range.** Normalize eigenvalues \(x_i\in\mathbb R\) of \(A\) by \(\sum_i x_i=0\) and \(\sum_i x_i^2=1\). A constrained extremum of \(\sum_i x_i^4\) is stationary: its distinct eigenvalues are roots of \(4t^3-2\lambda t-\mu=0\), so there are at most three. If three distinct roots \(a,b,c\) occur, their sum is zero. Select one occurrence of each and rotate this triple slightly while keeping its sum and squared length fixed. Because every zero-sum triple obeys \(a^4+b^4+c^4=(a^2+b^2+c^2)^2/2\), the overall fourth-power sum remains unchanged. Since \(n\ge4\), at least one old root still occurs elsewhere. A generic small rotation then produces at least four distinct eigenvalues, contradicting the stationary cubic at the resulting equally extremal point. Therefore every global extremum has exactly two distinct eigenvalues.

If the positive eigenvalue occurs \(m\) times and the negative one \(n-m\) times, the two constraints force
\[
\rho=\frac{n}{m(n-m)}-\frac3n.
\]
This is minimized precisely when \(m\) is as close to \(n/2\) as possible and maximized precisely for \(m\in\{1,n-1\}\), yielding \(\rho_-\) and \(\rho_+\) with the asserted complete equality families. Compactness and connectedness of the zero-sum unit sphere imply every intermediate \(\rho\), and hence every intermediate \(K\), occurs.

**Deficits and phase.** Put \(D=2nC|M|\ge0\). For \(M>0\), the exact endpoint deficits are \(K-K_{\min}=D(\rho-\rho_-)\) and \(K_{\max}-K=D(\rho_+-\rho)\). For \(M<0\), interchange \(\rho_-\) and \(\rho_+\). These are nonnegative and their zero sets give all equality cases. If \(M=0\), direct substitution into the preceding moment formula gives \(K=3(n^2-1)/(n^2+1)\) independently of the spectrum.

**Euclidean distortion.** The \(L^2\) norm is a constant multiple of Hilbert--Schmidt norm and the preceding sharp \(K\) interval gives a Euclidean comparison with distortion \((K_{\max}/K_{\min})^{1/4}\). For any competing Euclidean norm, its squared norm is a positive quadratic form on traceless Hermitian matrices. Average this form over unitary conjugation: by irreducibility of conjugation on that real space, the average is a scalar multiple of Hilbert--Schmidt norm squared. Averaging the upper and lower norm-comparison inequalities preserves their constants, so no competing Euclidean norm improves the distortion. Hence the displayed Banach--Mazur identity is exact.

**Infinitely many resonances.** The condition \(M=0\) is equivalent, for \(t=n-2k\), to \(n^2-5t^2=4\). For each integer \(j\ge2\), the Lucas and Fibonacci numbers \(n=L_{2j}\), \(t=F_{2j}\) satisfy \(L_{2j}^2-5F_{2j}^2=4\), and \(k=(n-t)/2\) is an admissible integer. The first examples listed in the finding follow. At these pairs, the whole function-space \(L^4\) norm is an inner-product norm.

## Verification

Run `python verify_moments.py` with Python 3 and SymPy. It reconstructs all degree-four Schur-character coefficients symbolically, verifies the variance normalization and the independent rank-one Dirichlet specialization, checks the sharp two-level formulas for dimensions through 50, checks the sign boundary for ranks through dimension 60, and verifies multiple resonant Pell examples and the Lucas/Fibonacci recurrence. These exact calculations are corroborative of the universal analytic derivation above. Numerical Haar sampling provided additional finite consistency checks in representative dimensions, but was not used to prove universality.

## Relationship to prior work

Collins' unitary integration formulas (public 2002 preprint) and Zhang's Schur--Weyl account (initial 2014 preprint) give the representation-theoretic tools underlying the moment calculation. The earlier work does not state this sharp two-sided norm classification, its spectral equality cases, the rank-dependent sign reversal, the Pell-type Euclidean resonances, or the exact Euclidean distortion. Ehler--Gräf--Király (2015) study related *real* projector cubatures, with explicit trace moments only through degree three; the present claim concerns complex Haar Grassmannians and degree four. The classical matrix moment formulas are ingredients, not a claim of newly invented integration identities.

## Limitations

The result is restricted to traceless Hermitian coefficients, complex Haar Grassmannians, ambient dimension at least four, and fourth moments. It does not assert analogous behavior for real Grassmannians, arbitrary non-projector spectra, or other exponents. Quartic isotropy at Pell resonances does **not** mean full spherical design strength four: third-order moments generally remain nonzero. No independent external verification of this mathematical result has been performed. Published specialized work not retrieved in the literature search could already contain an equivalent spectral classification.

## References

1. B. Collins, *Moments and Cumulants of Polynomial Random Variables on Unitary Groups, the Itzykson--Zuber Integral and Free Probability*, arXiv:math-ph/0205010 (initial public version 2002-05-07), esp. Theorem 2.1.
2. L. Zhang, *Matrix Integrals over Unitary Groups: An Application of Schur--Weyl Duality*, arXiv:1408.3782 (initial public version 2014-08-17), esp. Section 3.3 and Appendix A.
3. M. Ehler, M. Gräf, F. J. Király, *Phase Retrieval Using Random Cubatures and Fusion Frames of Positive Semidefinite Matrices*, arXiv:1505.05003 (initial public version 2015-05-19), esp. Sections 2 and 7.
