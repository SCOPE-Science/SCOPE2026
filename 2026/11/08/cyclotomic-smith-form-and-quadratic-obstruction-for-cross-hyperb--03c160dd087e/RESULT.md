# Cyclotomic Smith form and quadratic obstruction for cross-hyperbola Fourier sampling

## Finding
Let \(p\ge3\) be an odd prime and let \(a,b\in\mathbb F_p^\times\). Define two multiplicative hyperbolas
\[
H_a=\{(s,a/s):s\in\mathbb F_p^\times\},\qquad H_b=\{(t,b/t):t\in\mathbb F_p^\times\}.
\]
With \(\zeta_p=\exp(2\pi i/p)\), their unnormalized cross-Fourier sampling matrix is
\[
M_{a,b}(s,t)=\zeta_p^{st+ab/(st)},\qquad s,t\in\mathbb F_p^\times.
\]
Set \(c=ab\), \(m=(p-1)/2\), and \(\pi=\zeta_p-1\). Over the discrete valuation ring \(R=\mathbb Z_p[\zeta_p]\), the complete Smith invariant-factor **valuation** multiset is
\[
\begin{cases}
\{0,1,1,2,2,\ldots,m-1,m-1,m\},&\text{if }c\text{ is a square},\\
\{0,1,1,2,2,\ldots,m-1,m-1,\infty\},&\text{if }c\text{ is a nonsquare}.
\end{cases}
\]
Here \(\infty\) denotes a zero Smith factor. For \(m=1\), the middle repeated sequence is empty. Consequently,
\[
\operatorname{rank}_{\mathbb C}M_{a,b}=\begin{cases}p-1,&\left(\frac{ab}{p}\right)=1,\\p-2,&\left(\frac{ab}{p}\right)=-1.\end{cases}
\]
In the nonsquare case the right kernel is exactly the line spanned by the quadratic character \(t\mapsto\left(\frac{t}{p}\right)\). In the square case,
\[
v_\pi(\det M_{a,b})=m^2;
\]
in the nonsquare case the sum of the valuations of the nonzero Smith factors is \(m(m-1)\). Thus two critically sampled hyperbolas exhibit a sharp square/nonsquare reconstruction transition with exactly one lost Fourier mode.

## Assumptions and scope
All field inverses and products in the matrix exponent are interpreted in \(\mathbb F_p\); the additive character is the fixed standard primitive \(p\)-th root \(\zeta_p\). Multiplying the exponent by a common nonzero scalar changes the effective hyperbola parameter and should be handled by the same square-class criterion after reparametrization. The Smith factors are local at the totally ramified prime above \(p\), not integer-global Smith factors and not the complex singular values. The word rank denotes rank over \(\mathbb C\) unless otherwise specified. Both parameter sets contain \(p-1\) points; the origin is excluded.

## Proof
Write \(N=p-1=2m\), \(f_c(u)=\zeta_p^{u+c/u}\), and choose the Teichmüller multiplicative characters \(\omega^r:\mathbb F_p^\times\to\mathbb Z_p^\times\), \(0\le r<N\), reducing modulo \(p\) to \(u^r\). The multiplicative Fourier transform is invertible over \(R\), because \(N\) is a unit in \(R\) and all \(N\)-th roots of unity lie in \(\mathbb Z_p\). Changing variables \(u=st\) shows that \(M_{a,b}\) maps the character column \(t\mapsto\omega(t)^r\) to the inverse character column \(s\mapsto\omega(s)^{-r}\) multiplied by
\[
K_r(c)=\sum_{u\in\mathbb F_p^\times}\omega(u)^r\zeta_p^{u+c/u}.
\]
Therefore invertible row and column operations over \(R\) reduce \(M_{a,b}\) to the diagonal \(K_0(c),\ldots,K_{N-1}(c)\). Their valuations, including zero factors, determine the Smith form.

For \(0\le j\le m\), expand \(\zeta_p^{x}=(1+\pi)^{[x]}\), where \([x]\in\{0,\ldots,p-1\}\). Modulo \(p\), the coefficient of \(\pi^j\) in \(K_r(c)\) is
\[
C_{r,j}=\sum_{u\in\mathbb F_p^\times}u^r\binom{u+c/u}{j}\in\mathbb F_p.
\]
The binomial on the right is evaluated as a polynomial over \(\mathbb F_p\), which is legitimate because \(j<p\). It is a polynomial in \(u+c/u\) of degree \(j\) with leading coefficient \(1/j!\). By multiplicative-character orthogonality, a monomial contributes only when its power of \(u\) is divisible by \(N\). Put \(d_r=\min(r,N-r)\). For every \(j<d_r\), the exponents arising from \((u+c/u)^k\), \(k\le j\), lie strictly between \(-d_r\) and \(d_r\); hence \(C_{r,j}=0\). At the first possible degree,
\[
C_{r,d_r}=\begin{cases}
-1,&r=0,\\
-c^r/r!,&0<r<m,\\
-(1+c^m)/m!,&r=m,\\
-1/(N-r)!,&m<r<N.
\end{cases}
\]
All displayed nonzero denominators are units modulo \(p\). The coefficient at \(r=m\) is nonzero precisely when \(c\) is a square, by Euler's criterion \(c^m=\left(\frac cp\right)\). Since \(v_\pi(p)=N\), the coefficients divisible by \(p\) at lower powers \(j<d_r\) cannot cancel a nonzero coefficient at power \(d_r\le m<N\); nor can higher powers do so. Consequently \(v_\pi K_r(c)=d_r\) except possibly \(r=m\) in the nonsquare case.

If \(c\) is a nonsquare, the change of variables \(u\mapsto c/u\) fixes \(u+c/u\) while multiplying the quadratic character \(\omega(u)^m\in\{\pm1\}\) by \(\left(\frac cp\right)=-1\). Thus the summands of \(K_m(c)\) cancel pairwise and \(K_m(c)=0\) **exactly**, not merely modulo a power of \(\pi\). All other \(K_r(c)\) are nonzero by the preceding valuation calculation. In particular, the kernel is the quadratic-character line. Summing \(d_r\) over \(r=0,\ldots,N-1\) gives \(m^2\); deleting the quadratic exponent \(m\) gives \(m(m-1)\), as asserted. This completes the proof in every odd prime characteristic, including \(p=3\).

## Verification
The standalone finite-case checker `verification/check_hyperbola.py` uses exact modular-binomial arithmetic to verify every predicted leading coefficient at all multiplicative characters for each tested prime. In the nonsquare case it also verifies exact cancellation of the quadratic-character coefficient vector in the integral cyclotomic group ring. A separately constructed complex Fourier matrix is checked by complex Gaussian elimination for its rank and proposed kernel. The tested primes are \(3,5,7,11,13,17,19,23,29,31\); one square and one nonsquare parameter are checked for each. Running `python verification/check_hyperbola.py` requires only the Python 3 standard library. The finite checks corroborate, but cannot replace, the infinite-prime argument above.

## Relationship to prior work
The diagonal multipliers are classical multiplicatively twisted Kloosterman sums. Kelmer, *Distribution of twisted Kloosterman sums modulo prime powers* (first arXiv version 2008-01-27, arXiv:0801.4162), defines the same family of exponential sums and discusses the classical Salié quadratic-character cancellation. Its main elementary evaluations and distribution results concern prime-power moduli of exponent greater than one; they do not provide this prime-field cross-hyperbola Smith classification. Gurak, *Kloosterman sums for prime powers in P-adic fields* (2009), also focuses on higher prime powers and different p-adic-field sums. Classical Salié evaluations already establish the quadratic-mode zero, so that cancellation **by itself is not a novelty claim**. The claimed contribution is the joint full-rank-versus-corank-one dichotomy and complete local invariant-factor profile for the entire square cross-sampling transform.

## Limitations
The result is confined to prime base fields of odd characteristic, nonzero hyperbola parameters and the specified bilinear Fourier pairing. It does not describe full complex singular values, quantitative complex condition numbers, extension-field analogues, or integer-global Smith normal forms. Broader historical theorems on twisted Kloosterman valuations might imply parts of the local invariant-factor list; bibliographic priority is not independently certified.

## References
- D. Kelmer, *Distribution of twisted Kloosterman sums modulo prime powers*, arXiv:0801.4162, initial preprint 2008-01-27, https://arxiv.org/html/0801.4162v2.
- S. J. Gurak, *Kloosterman sums for prime powers in P-adic fields*, Journal de théorie des nombres de Bordeaux 21 (2009), 175–201, https://doi.org/10.5802/jtnb.665.
- H. Salié, *Über die Kloostermanschen Summen*, Mathematische Zeitschrift 34 (1932), 91–109 (classical quadratic-character case, as referenced in Kelmer and Gurak).
