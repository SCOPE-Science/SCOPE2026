# Three-term Schatten traces for Jacobi Bernstein–Durrmeyer operators

## Finding
For real \(a,b>-1\), integer \(n\ge1\), and \(s>0\), let \(M_{n,a,b}\) be the Jacobi-weighted Bernstein–Durrmeyer operator on \(L^2((0,1),x^a(1-x)^b\,dx)\), as defined below. Its nonzero eigenvalues are \(\lambda_{n,k}\), \(0\le k\le n\). The following **three-term asymptotic** holds:

\[
\begin{aligned}
\operatorname{tr}(M_{n,a,b}^{s})
={}&\frac{\sqrt{\pi n}}{2\sqrt{s}}-\frac{a+b}{2}\\
&+\frac{\sqrt\pi}{2\sqrt{sn}}\left(\frac{s(a+b+1)^2}{4}+\frac{a+b+2}{4}-\frac{1}{8s}\right)
+O_{a,b,s}(n^{-1}).
\end{aligned}
\]

The error is uniform when \((a,b,s)\) ranges over any compact subset of \((-1,\infty)^2\times(0,\infty)\). Thus the order-one term \(-(a+b)/2\) is independent of the Schatten exponent, and it cancels identically for Jacobi weights whose exponents sum to zero. In the unweighted case, for instance,
\[
\operatorname{tr}(M_{n,0,0}^{2})
=\sqrt{\frac{\pi n}{8}}+\frac{15}{16}\sqrt{\frac{\pi}{8n}}+O(n^{-1}).
\]

The nonzero spectrum itself is classical; the proposed contribution is the stated uniform three-term spectral-power trace expansion, particularly the exponent-independent boundary term and the explicit inverse-square-root coefficient.

## Assumptions and scope
For \(0\le j\le n\), write
\[
p_{n,j}(x)=\binom nj x^j(1-x)^{n-j},\qquad w_{a,b}(x)=x^a(1-x)^b.
\]
Define the finite-rank integral operator
\[
(M_{n,a,b}f)(x)=\sum_{j=0}^{n}p_{n,j}(x)
\frac{\int_0^1 f(t)p_{n,j}(t)w_{a,b}(t)\,dt}
{\int_0^1p_{n,j}(t)w_{a,b}(t)\,dt}.
\]
All denominators are positive. The integral kernel is symmetric with respect to weighted \(L^2\) and positive semidefinite, so all its eigenvalues are real and nonnegative. For \(s>0\), the power \(M_{n,a,b}^s\) is defined by positive-operator functional calculus and has a finite trace; for \(s\ge1\) this is its usual Schatten-power sum. The underlying Hilbert space may be real or complex. Set \(c=a+b+2>0\) and \(\delta=(c-1)/2\). Only fixed-parameter or compact-parameter asymptotics are asserted; simultaneous growth of parameters with \(n\) is not covered.

## Proof
**Step 1: exact finite spectrum.** Positivity and selfadjointness follow from the sum of normalized rank-one kernels. Beta integration gives, for every integer \(0\le k\le n\),
\[
M_{n,a,b}(x^k)
=\frac1{(n+c)^{\overline k}}\sum_{j=0}^n(j+a+1)^{\overline k}p_{n,j}(x),
\]
where the overline denotes rising factorial. The Bernstein factorial-moment identity
\(\sum_j j^{\underline k}p_{n,j}(x)=n^{\underline k}x^k\)
shows that polynomials of degree at most \(k\) are preserved and that the coefficient of \(x^k\) above is
\[
\lambda_{n,k}=\frac{n^{\underline k}}{(n+c)^{\overline k}}
=\prod_{j=0}^{k-1}\frac{n-j}{n+c+j}.
\]
Selfadjointness together with invariance of nested polynomial spaces makes the orthogonal Jacobi polynomials eigenvectors with these eigenvalues. The orthogonal complement of polynomials of degree at most \(n\) is the nullspace. Consequently, for every real \(s>0\),
\[
T_n(c,s):=\operatorname{tr}(M_{n,a,b}^{s})=\sum_{k=0}^{n}\lambda_{n,k}^{s}.
\]
This step can also be checked by exact rational polynomial matrices as in the accompanying checker.

An independent closed-form consistency check is available at \(a=b=0\) and \(s=1\): the binomial half-sum identity gives
\[
\operatorname{tr}(M_{n,0,0})
=\frac{4^n n!(n+1)!}{(2n+1)!},
\]
whose central-binomial expansion reproduces the \(5/8\) inverse-square-root coefficient in the general formula. This exact identity is a check, not the source of the all-power theorem.

**Step 2: uniform Gaussian tails.** For \(0\le j<k\le n\), the logarithm of the \(j\)-th factor in the product is at most \(-(2j+c)/(n+c+j)\), since \(\log(1-u)\le-u\) for \(0\le u<1\). Hence
\[
0<\lambda_{n,k}\le\exp\!\left[-\frac{k(k+c-1)}{2n+c}\right].
\]
On any compact set of \(c>0\) and \(s>0\), for sufficiently large \(n\) and \(k\ge2\), the right-hand side raised to power \(s\) is bounded by \(\exp(-\eta k^2/n)\) with some \(\eta>0\). Thus all terms beyond \(k>n^{3/5}\) have total size \(O(n\exp(-\eta n^{1/5}))\). The corresponding Gaussian-model tails have the same negligible bound.

**Step 3: the lattice-centered logarithmic expansion.** Put \(h=n^{-1/2}\) and \(t_k=h(k+\delta)\). Uniformly over compact \(c\)-sets and integers \(0\le k\le n^{3/5}\), expanding each logarithm in
\[
\log\lambda_{n,k}=\sum_{j=0}^{k-1}
\left[\log(1-j/n)-\log(1+(j+c)/n)\right]
\]
yields
\[
\log\lambda_{n,k}=-t_k^2+h^2 A_c(t_k)
+O\!\left(h^3(1+|t_k|^5)\right),
\quad A_c(t)=\delta^2+\frac c2t^2-\frac16t^4.
\]
Indeed, the first-order sum is exactly \(-k(k+c-1)/n=-t_k^2+h^2\delta^2\); the second-order sum is \(ck(k+c-1)/(2n^2)=h^2ct_k^2/2+O(h^4)\); the leading cubic sum is \(-k^4/(6n^3)=-h^2t_k^4/6+O(h^3(1+|t_k|^3))\). The fourth-order Taylor remainders are \(O(k^5/n^4)=O(h^3(1+|t_k|^5))\). Here \(j/n\) and \((j+c)/n\) are uniformly small on the truncated range. For compact positive \(s\)-sets, exponentiation and Gaussian domination give
\[
\lambda_{n,k}^{s}=e^{-s t_k^2}
\bigl(1+sh^2 A_c(t_k)\bigr)
+e^{-\eta t_k^2}O\!\left(h^3(1+|t_k|^8)\right).
\]
The sum of the displayed remainder is \(O(h^2)=O(n^{-1})\), because fixed Gaussian moments are finite; the tails from Step 2 are negligible. All constants can be chosen uniformly on compact parameter sets.

**Step 4: shifted half-line summation.** Standard shifted Euler–Maclaurin summation applied to the even Gaussian \(f(t)=e^{-st^2}\) gives
\[
\sum_{k=0}^\infty f(h(k+\delta))
=h^{-1}\int_0^\infty f(t)\,dt+\left(\frac12-\delta\right)f(0)+O(h^2).
\]
The potential order-\(h\) term vanishes because \(f'(0)=0\). The formula also holds for a fixed negative \(\delta\), interpreting \(f\) on the real line. Similarly, for the smooth, rapidly decaying \(g(t)=A_c(t)e^{-st^2}\),
\[
sh^2\sum_{k=0}^\infty g(h(k+\delta))=sh\int_0^\infty g(t)\,dt+O(h^2).
\]
The elementary Gaussian moments are
\[
\int_0^\infty e^{-st^2}\,dt=\frac{\sqrt\pi}{2\sqrt s},\quad
\frac{\int_0^\infty t^2e^{-st^2}dt}{\int_0^\infty e^{-st^2}dt}=\frac1{2s},\quad
\frac{\int_0^\infty t^4e^{-st^2}dt}{\int_0^\infty e^{-st^2}dt}=\frac3{4s^2}.
\]
Putting these together,
\[
T_n(c,s)=\frac{\sqrt{\pi n}}{2\sqrt s}
+\left(\frac12-\delta\right)
+\frac{\sqrt\pi}{2\sqrt{sn}}
\left(s\delta^2+\frac c4-\frac1{8s}\right)+O(n^{-1}).
\]
Substituting \(c=a+b+2\) and \(\delta=(a+b+1)/2\) proves the theorem, including the asserted compact-uniform remainder.

## Verification
The standalone `checker.py` uses only Python's standard library. It reconstructs the finite polynomial matrix from beta moments, checks that its entries above the output-degree cutoff vanish exactly, and verifies its diagonal entries against the product eigenvalues for multiple rational Jacobi parameter pairs. It also compares the stated three-term formula with finite real-power spectral sums for several parameters and increasing dimensions. The analytic Gaussian-tail and summation estimates, not the finite computations, prove the asymptotic theorem.

Run `python3 checker.py` in the directory containing the extracted package files. The observed result was: `PASS 28 exact rational triangular spectral identities; 19 exact unweighted trace identities; 24 numerical asymptotic comparisons`.

## Relationship to prior work
The degree-preserving selfadjoint operator and its Jacobi-polynomial eigenbasis are classical. Berdysheva–Jetter (2010), Section 3.2.2 and equation (3.12), provides the general Jacobi-weighted eigenvalue formula. Lara-Velasco–Pérez (2024), Section 2 and Section 5, also gives the same formula and discusses fixed-degree eigenvalue asymptotics and derivative preservation. Those spectral identities and their fixed-degree consequences are not claimed here as new. The present statement instead sums **all** eigenvalues to arbitrary positive real powers on the moving spectral scale \(k\asymp\sqrt n\), extracting two lower-order terms uniformly in the Jacobi weights and power exponent. The 2010 source was available in indexed, relevant sections rather than as a wholly inspectable local copy, so an unlocated equivalent treatment cannot be ruled out.

## Limitations
This is an analytic asymptotic at fixed real Jacobi exponents and fixed positive power; it does not establish uniformity when the Jacobi parameters or the power diverge or approach the boundary of their allowed ranges with \(n\). The \(O(n^{-1})\) bound is compact-uniform but its numerical constant is not optimized. Absolute bibliographic novelty is not proved, and an independent mathematical or literature audit has not been performed. Finite checker tests are consistency checks, not substitutes for the estimates in the proof.

## References
1. E. E. Berdysheva and K. Jetter, *Multivariate Bernstein–Durrmeyer operators with arbitrary weight functions*, Journal of Approximation Theory 162 (2010), 576–598, doi:10.1016/j.jat.2009.11.005 (especially Section 3.2.2 and formula (3.12)).
2. D. Lara-Velasco and T. E. Pérez, *Bernstein–Jacobi-type operators preserving derivatives*, Computational and Applied Mathematics 43 (2024), article 277, doi:10.1007/s40314-024-02796-2 (equations (2.5), (5.1) and related discussion).
3. M. M. Derriennic, *Sur l'approximation de fonctions intégrables sur [0,1] par des polynômes de Bernstein modifiés*, Journal of Approximation Theory 31 (1981), 325–343 (historical origin and eigenstructure).
