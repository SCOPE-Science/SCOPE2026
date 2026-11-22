# Integral Smith form of quadratic-root convolution at prime-square modulus

## Finding
For every odd prime \(p\), let \(q=p^2\) and define the integer \(q\)-by-\(q\) matrix
\[
K_q(a,b)=\#\{x\in\mathbb Z/q\mathbb Z:x^2\equiv b-a\pmod q\},\qquad a,b\in\mathbb Z/q\mathbb Z.
\]
Its determinant is nonzero and its entire integral cokernel is
\[
\boxed{\operatorname{coker}K_{p^2}\cong
(\mathbb Z/p\mathbb Z)^{p(p-2)}\oplus
(\mathbb Z/p^2\mathbb Z)^{(p+1)/2}\oplus
(\mathbb Z/p^3\mathbb Z)^{(p-3)/2}\oplus
\mathbb Z/p^4\mathbb Z.}
\]
There are exactly \(p\) unit invariant factors. In particular,
\[
|\det K_{p^2}|=p^{p^2+(p+1)/2},\qquad
\operatorname{rank}_{\mathbb F_p}(K_{p^2})=p,
\]
and the exponent of the cokernel is exactly \(p^4\), for every odd prime \(p\).

## Assumptions and scope
All roots are counted as residue classes, including nonunits. Smith factors are over \(\mathbb Z\), not over a field or the ring of integers of a cyclotomic field. In formulas involving \(K_p\), the same root-count definition is used with modulus \(p\). For \(a,b\in\mathbb F_p\), let \(H_p(a,b)=1\) if \(b-a\) is a nonzero square in \(\mathbb F_p\), and let it be zero otherwise. No result for higher prime-power depths or for \(p=2\) is asserted.

## Proof
**1. Prime-level integral invariants.** The number of roots of a square modulo \(p\) is one at zero and two at a nonzero quadratic residue, so
\[
K_p=I_p+2H_p=J_p+Q_p,
\]
where \(J_p\) is the all-ones matrix and \(Q_p(a,b)=\chi_p(b-a)\) for the Legendre character extended by zero. The standard elementary quadratic-character correlation identity yields
\[
Q_pJ_p=J_pQ_p=0,\quad Q_pQ_p^{\mathsf T}=pI_p-J_p,
\quad Q_p^{\mathsf T}=\chi_p(-1)Q_p.
\]
For completeness, the off-diagonal correlation is \(-1\) because, after translating and scaling two distinct arguments, \(\sum_z\chi_p(z(z-1))=-1\); this last identity follows by counting the \(p-1\) solutions of \((2z-1)^2-w^2=1\). The diagonal correlation is \(p-1\). The constant vector is an eigenvector of \(K_p\) with eigenvalue \(p\); on the rational sum-zero subspace \(K_p=Q_p\) and \(Q_p^2=\chi_p(-1)pI\). Therefore
\[
|\det K_p|=p^{(p+1)/2}.
\]

To calculate its reduction modulo \(p\), identify the additive group algebra with \(\mathbb F_p[X]/(X^p-1)=\mathbb F_p[t]/(t^p)\), where \(X=1+t\). The operator \(K_p\) is multiplication by
\[
S(t)=\sum_{x\in\mathbb F_p}(1+t)^{x^2}.
\]
For \(0\le j<(p-1)/2\), the coefficient \(\sum_x\binom{x^2}{j}\) vanishes modulo \(p\), because it is a polynomial sum of degree at most \(2j<p-1\), including \(j=0\). For \(r=(p-1)/2\), its coefficient is \(-1/r!\ne0\), since the leading term is \(x^{p-1}/r!\). Thus \(S(t)\) has exact \(t\)-adic order \(r\) and multiplication by it has rank \(p-r=(p+1)/2\). Since \(\det K_p\) is a pure power of \(p\), precisely \(r\) Smith factors are divisible by \(p\), and their total exponent is \(r+1\). Consequently
\[
\operatorname{SNF}(K_p)=\operatorname{diag}
\bigl(1^{\times(p+1)/2},p^{\times(p-3)/2},p^2\bigr).
\]
In the same group algebra, \(H_p=(K_p-I_p)/2\) is represented modulo \(p\) by \((S(t)-1)/2\), with nonzero constant term \(-1/2\). This is a unit of \(\mathbb F_p[t]/(t^p)\), proving \(p\nmid\det H_p\).

**2. Exact prime-square lifting.** For \(a,b\in\mathbb Z/p^2\mathbb Z\), if \(b-a\) is a unit, Hensel's simple-root lifting gives exactly two roots when its reduction modulo \(p\) is a nonzero square, and none otherwise. If \(b-a\) is a nonzero multiple of \(p\), it has no square root; if it is zero, its roots are the \(p\) multiples of \(p\). Hence the entrywise identity
\[
K_{p^2}(a,b)=p\mathbf1_{a=b}+2H_p(a\bmod p,b\bmod p).
\]
Let \(b_a=e_{a}\) be the standard basis vector indexed by the chosen lift \(a\in\{0,\ldots,p-1\}\), and let \(d_{a,u}=e_{a+pu}-e_a\), for \(1\le u<p\). Together the \(b_a,d_{a,u}\) form a unimodular integral basis. If \(U_a=\sum_{u=0}^{p-1}e_{a+pu}\), then \(U_a=pb_a+\sum_{u=1}^{p-1}d_{a,u}\). The entrywise identity shows that \(K_{p^2}\) maps each \(d_{a,u}\) to \(p d_{a,u}\), and maps each \(b_a\) to \(p b_a+2\sum_b H_p(b,a)U_b\). The choice of orientation gives \(H_p\) or its transpose, both with identical Smith form and prime-local invertibility. Choosing the corresponding orientation, the matrix in this basis has block form
\[
\begin{pmatrix}
 pK_p&0&0&\cdots&0\\
 2H_p&pI_p&0&\cdots&0\\
 2H_p&0&pI_p&\cdots&0\\
 \vdots&\vdots&\vdots&\ddots&\vdots\\
 2H_p&0&0&\cdots&pI_p
\end{pmatrix},
\]
with \(p-1\) lower block rows. Subtract the first lower row from each remaining lower row and add each corresponding later difference-column block to the first difference-column block. These unimodular operations give a direct block \(pI_{p(p-2)}\) and the residual block
\[
M=\begin{pmatrix}pK_p&0\\2H_p&pI_p\end{pmatrix}.
\]
Because \(2H_p\) is invertible over \(\mathbb Z_{(p)}\), using that block as a unit pivot and taking its Schur complement gives the local equivalence
\[
M\ \sim_{\mathbb Z_{(p)}}\ I_p\oplus p^2K_p,
\qquad
K_{p^2}\ \sim_{\mathbb Z_{(p)}}\ I_p\oplus pI_{p(p-2)}\oplus p^2K_p.
\]

**3. No hidden primes.** The original integral triangular block matrix has determinant \(p^{p(p-1)}\det(pK_p)=p^{p^2}\det K_p\). Thus
\[
|\det K_{p^2}|=p^{p^2+(p+1)/2}.
\]
No prime other than \(p\) divides any invariant factor. Combining the prime-local equivalence with the already-proved integral Smith form of \(K_p\) gives exactly the stated factors. There are \(p\) unit factors, and the unique largest factor is \(p^4\), as claimed.

## Verification
The standalone `checker.py` uses exact integer arithmetic and SymPy's integer Smith form. It checks the prime-level Smith form, determinant, modular rank and \(p\)-unit property of \(H_p\) for primes \(3,5,7,11,13,17,19\); the prime-square matrix identity and rank for \(3,5,7,11,13\); and direct prime-square Smith forms at \(3,5\). It passed 46,351 exact assertions. Reproduce with `python checker.py` from the directory containing the supplied checker; Python 3 and SymPy are required. The infinite all-prime conclusion rests on the preceding proof, not on the finite tests.

## Relationship to prior work
Quadratic Gauss and character sums are classical; Chandler–Sin–Xiang's 2014 study gives integral Smith and critical groups of Paley graphs on finite fields. Williams (2014) calculates Smith forms for selected ordinary circulant graph families, and Telloni–Williams (2014) addresses circulant **polynomial** matrices under associated-polynomial hypotheses. These supply context and techniques, but their evaluated results do not give the full integral square-root-count matrix at the nonfield modulus \(p^2\). In particular, the field \(\mathbb F_{p^2}\) is not the ring \(\mathbb Z/p^2\mathbb Z\); their additive groups differ. The new content here is the coset-lifting block reduction and the resulting exact five-level integral Smith classification for every odd \(p\), not the classical Gauss-sum determinant or the base-field Paley spectrum.

## Limitations
The theorem is restricted to odd primes and prime-square modulus. It does not classify square-root convolution at depths \(p^k\) with \(k\ge3\), nor does it claim to classify arbitrary quadratic polynomials. The cited literature comparisons and indexed overlap searches do not constitute a proof of historical priority. The exact numerical checks at finitely many primes do not establish the theorem for all primes; the symbolic proof does.

## References
- Gerald Williams, *Smith forms for adjacency matrices of circulant graphs* (2014), first repository deposit 2014-01-07, https://repository.essex.ac.uk/8578/ .
- David Chandler, Peter Sin and Qing Xiang, *The Smith and critical groups of Paley graphs* (2014), first arXiv posting 2014-01-31, https://arxiv.org/abs/1401.8260 .
- Agnese Ilaria Telloni and Gerald Williams, *Smith forms of circulant polynomial matrices* (2014), first repository deposit 2014-06-23, https://repository.essex.ac.uk/9703/ .
- Misty Long, Vincent Pigno and Christopher Pinner, *Evaluating Prime Power Gauss and Jacobi Sums* (2014), first arXiv posting 2014-10-22, https://arxiv.org/abs/1410.6179 .
