# Sharp square-root residue oscillations in the ternary and quinary Calkin–Wilf levels

## Finding

Build the Calkin–Wilf tree from \(1/1\) by replacing every reduced positive fraction \(a/b\) with \(a/(a+b)\) and \((a+b)/b\). The root is at depth \(0\); depth \(n\) has \(2^n\) fractions. For \(p\in\{3,5\}\) and \(r\in\mathbb P^1(\mathbb F_p)=\mathbb F_p\cup\{\infty\}\), let \(N_{p,n}(r)\) count depth-\(n\) fractions whose primitive numerator-denominator pair represents \(r\) modulo \(p\); a denominator divisible by \(p\) represents \(\infty\).

Write \(A_n=N_{3,n}(0)=N_{3,n}(\infty)\), \(B_n=N_{3,n}(1)\), and \(C_n=N_{3,n}(2)\). Then **all row counts at every depth** are specified by
\[
\sum_{n\ge0}\begin{pmatrix}A_n\\B_n\\C_n\end{pmatrix}z^n
=\frac{1}{1-z-4z^3}\begin{pmatrix}2z^2\\1-z\\2z(1-z)\end{pmatrix}.
\]
For five, write \(U_n=N_{5,n}(0)=N_{5,n}(\infty)\), \(V_n=N_{5,n}(1)\), \(W_n=N_{5,n}(2)=N_{5,n}(3)\), \(X_n=N_{5,n}(4)\). Then
\[
\sum_{n\ge0}\begin{pmatrix}U_n\\V_n\\W_n\\X_n\end{pmatrix}z^n
=\frac{1}{(1-2z)(1+z)(1-z+2z^2)}
\begin{pmatrix}2z^3\\(1-z)^2\\z(1-z)\\2z^2(1-z)\end{pmatrix}.
\]
In either prime, **every** projective residue first occurs at every depth from \(n=4\) onward; depth \(3\) still misses at least one class.

All projective classes are asymptotically equidistributed, with the **optimal** exponential error scale \(2^{n/2}\). More sharply, for the zero and infinite classes,
\[
\limsup_{n\to\infty}\frac{N_{3,n}(0)-2^n/4}{2^{n/2}}=\sqrt{2/7},\quad
\liminf_{n\to\infty}\frac{N_{3,n}(0)-2^n/4}{2^{n/2}}=-\sqrt{2/7},
\]
\[
\limsup_{n\to\infty}\frac{N_{5,n}(0)-2^n/6}{2^{n/2}}=\frac1{\sqrt7},\quad
\liminf_{n\to\infty}\frac{N_{5,n}(0)-2^n/6}{2^{n/2}}=-\frac1{\sqrt7}.
\]
The analogous bound \(N_{p,n}(r)=2^n/(p+1)+O(2^{n/2})\) holds for **each** projective class \(r\) at both primes, and the order of the uniform error cannot be improved to \(o(2^{n/2})\).

## Assumptions and scope

All fractions have coprime positive integer numerator and denominator. Since every child comes from a unimodular transformation, the pair remains primitive modulo every prime; thus no residue pair \((0,0)\) arises. We count distinct nodes with multiplicity one at each fixed depth; the results do **not** assert uniformity over the set of all rationals ordered by denominator, nor any comparable explicit formula at primes beyond \(3\) and \(5\). The labels \(0,\infty\) are different points of the projective line.

## Proof

For every prime, the left and right child maps on the projective line are
\[
L(r)=\frac{r}{r+1},\qquad R(r)=r+1,
\]
where evaluation at poles uses homogeneous coordinates. Inversion \(r\mapsto1/r\) exchanges left and right children and fixes the root, so the counts of inverted classes are equal at each depth.

Modulo \(3\), the four states have transitions \(0\mapsto(0,1)\), \(1\mapsto(2,2)\), \(2\mapsto(\infty,0)\), and \(\infty\mapsto(1,\infty)\). Consequently, with initial vector \((A_0,B_0,C_0)=(0,1,0)\),
\[
\begin{pmatrix}A_{n+1}\\B_{n+1}\\C_{n+1}\end{pmatrix}
=\begin{pmatrix}1&0&1\\2&0&0\\0&2&0\end{pmatrix}
\begin{pmatrix}A_n\\B_n\\C_n\end{pmatrix}.
\]
Its characteristic polynomial is \((t-2)(t^2+t+2)\). Solving \((I-zM)F(z)=F(0)\) gives the displayed ternary generating function.

Modulo \(5\), the transitions, for \(r=0,1,2,3,4,\infty\) respectively, are \((0,1)\), \((3,2)\), \((4,3)\), \((2,4)\), \((\infty,0)\), and \((1,\infty)\). Reciprocal symmetry reduces the counts to \((U,V,W,X)\) with initial vector \((0,1,0,0)\) and
\[
\begin{pmatrix}U_{n+1}\\V_{n+1}\\W_{n+1}\\X_{n+1}\end{pmatrix}
=\begin{pmatrix}1&0&0&1\\2&0&0&0\\0&1&1&0\\0&0&2&0\end{pmatrix}
\begin{pmatrix}U_n\\V_n\\W_n\\X_n\end{pmatrix}.
\]
Its characteristic polynomial is \((t-2)(t+1)(t^2-t+2)\), giving the displayed quinary generating function. Both reduced matrices are nonnegative. At depth \(4\) all of their coordinates are positive; the explicit updates keep them positive for all later depths. At depth \(3\), \(C_3=0\) and \(V_3=0\), respectively. This proves the exact onset.

The two nonreal characteristic roots are \(\lambda_3=(-1+i\sqrt7)/2\) and its conjugate in the ternary case, and \(\lambda_5=(1+i\sqrt7)/2\) and its conjugate in the quinary case. They both have modulus \(\sqrt2\); the other eigenvalues have moduli \(2\) and, in the quinary case, \(1\). The eigenvalue \(2\) contributes exactly \(2^n/(p+1)\) to each original projective-state count, as can also be checked from the partial fractions or the normalization \(\sum_rN_{p,n}(r)=2^n\). Therefore every class has error \(O(2^{n/2})\).

In particular, matching the initial values and recurrences gives the *exact* expansions
\[
A_n=\frac{2^n}{4}+2\operatorname{Re}\!\left(c_3\lambda_3^n\right),\qquad
c_3=-\frac18+\frac{5i}{8\sqrt7},\quad |c_3|=\frac1{\sqrt{14}},
\]
\[
U_n=\frac{2^n}{6}-\frac{(-1)^n}{6}+2\operatorname{Re}\!\left(c_5\lambda_5^n\right),\qquad
c_5=\frac{i\sqrt7}{14},\quad |c_5|=\frac1{2\sqrt7}.
\]
Let \(\lambda_p=\sqrt2e^{i\theta_p}\). A direct calculation yields \(\cos(2\theta_p)=-3/4\) for both primes. If \(\theta_p/\pi\) were rational, \(2\cos(2\theta_p)=-3/2\) would be the sum of a root of unity and its inverse, hence an algebraic integer; a nonintegral rational number cannot be an algebraic integer. Thus \(\theta_p/2\pi\) is irrational, and its integer multiples are dense on the circle. The two cosine terms therefore have normalized limsup/liminf exactly \(\pm2|c_p|\). The bounded alternating term in \(U_n\) disappears upon division by \(2^{n/2}\). This proves both sharp constants and optimality.

## Verification

The standalone `verify.py` implements separate direct, exact projective reductions for every depth through \(15\) at both primes, compares them to the reduced transfer recurrences, checks each rational generating function coefficient through depth \(80\), and verifies normalization and the first all-class depth. Its execution completed with `PASS: 1138 exact assertions`. All infinite-depth claims rest on the transfer identities and characteristic-root analysis above, not on the finite checks.

## Relationship to prior work

Lynch and Mackey (first public 2022) prove an exactly repeating three-class parity law for Calkin–Wilf rationals and discuss a possible extension to \(p\)-adic settings. Their parity partition is a modulo-two statement; it does not give the four- and six-class projective distributions, the generating functions above, or the sharp odd-prime oscillation constants. Stanley (2019) proves finite recurrences for **power sums** in Stern-type rows; the present finite-state residue distribution is a different statistic and the explicit projective spectrum is not stated there. Published numerical-residue studies of three and four consecutive Stern terms establish limiting residue-pattern densities, rather than these exact level-by-level projective counts. The earlier quadratic-character row sum for Stern numerators modulo five likewise does not imply joint numerator/denominator projective frequencies. See the references and limitations below.

## Limitations

The result covers only the two first odd primes, not arbitrary primes or prime powers. The square-root scale is optimal for the displayed point classes and thus for the **uniform** bound; the leading amplitudes of all other individual classes are not tabulated here. No independent audit was performed. There is residual priority risk from equivalent projective-walk transfer-matrix calculations or unpublished notes not located in the inspected sources. The manuscript claims no originality for finite-state methods in general.

## References

1. P. Lynch and M. Mackey, *Parity and Partition of the Rational Numbers*, arXiv:2205.00565, first posted 2022-05-01, https://arxiv.org/abs/2205.00565 ; journal version *College Mathematics Journal* 55 (2024), 387–399, https://doi.org/10.1080/07468342.2024.2311632 .
2. R. P. Stanley, *Some Linear Recurrences Motivated by Stern's Diatomic Array*, arXiv:1901.04647, first posted 2019-01-15, https://arxiv.org/abs/1901.04647 .
3. N. Calkin and H. Wilf, *Recounting the Rationals*, *American Mathematical Monthly* 107 (2000), 360–363.
4. *Exact three-term congruence law for Stern's diatomic sequence* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-exact-three-term-congruence-law-for-stern-s-diatomic-sequence--2ccf8df2e88c .
5. *Exact four-term residue densities and support counts for the Stern sequence* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-exact-four-term-residue-densities-and-support-counts-for-the-ste--ee10caa284d0 .
